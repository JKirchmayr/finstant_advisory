const RECIPIENTS = (process.env.CONTACT_RECIPIENTS || "jkirchmayr@finstant.ai,riccardo@finstant.ai")
  .split(",")
  .map((e) => e.trim())
  .filter(Boolean);

const FROM = process.env.CONTACT_FROM || "Finstant Advisory <onboarding@resend.dev>";

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

export default async function handler(req, res) {
  if (req.method === "OPTIONS") {
    res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type");
    return res.status(204).end();
  }

  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  if (!process.env.RESEND_API_KEY) {
    return res.status(503).json({ error: "Email service is not configured" });
  }

  try {
    const body = typeof req.body === "string" ? JSON.parse(req.body) : req.body || {};
    const { name, email, company, message, website, lang } = body;

    if (website) {
      return res.status(200).json({ ok: true });
    }

    if (!name || !email || !message) {
      return res.status(400).json({ error: "Missing required fields" });
    }

    if (!isValidEmail(email)) {
      return res.status(400).json({ error: "Invalid email address" });
    }

    if (name.length > 200 || email.length > 254 || (company && company.length > 200) || message.length > 5000) {
      return res.status(400).json({ error: "Input too long" });
    }

    const safeName = escapeHtml(name.trim());
    const safeEmail = escapeHtml(email.trim());
    const safeCompany = company ? escapeHtml(company.trim()) : "";
    const safeMessage = escapeHtml(message.trim()).replace(/\n/g, "<br>");
    const safeLang = escapeHtml(lang || "unknown");

    const subject = `Finstant Advisory — new enquiry from ${name.trim()}`;
    const html = `
      <h2>New website enquiry</h2>
      <p><strong>Name:</strong> ${safeName}</p>
      <p><strong>Email:</strong> <a href="mailto:${safeEmail}">${safeEmail}</a></p>
      ${safeCompany ? `<p><strong>Company:</strong> ${safeCompany}</p>` : ""}
      <p><strong>Language:</strong> ${safeLang}</p>
      <p><strong>Message:</strong></p>
      <p>${safeMessage}</p>
    `;

    const response = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        from: FROM,
        to: RECIPIENTS,
        reply_to: email.trim(),
        subject,
        html,
      }),
    });

    if (!response.ok) {
      const detail = await response.text();
      console.error("Resend error:", response.status, detail);
      return res.status(502).json({ error: "Failed to send email" });
    }

    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error("Contact form error:", err);
    return res.status(500).json({ error: "Server error" });
  }
}
