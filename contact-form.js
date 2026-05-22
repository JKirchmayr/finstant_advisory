(function () {
  const form = document.getElementById("contact-form");
  if (!form) return;

  const statusEl = form.querySelector(".contact-form-status");
  const submitBtn = form.querySelector(".contact-submit");
  const defaultLabel = submitBtn.textContent;

  const messages = {
    sending: form.dataset.msgSending || "Sending…",
    success: form.dataset.msgSuccess || "Thank you. We will be in touch shortly.",
    error: form.dataset.msgError || "Something went wrong. Please try again or email us directly.",
    local:
      form.dataset.msgLocal ||
      "The contact form API is not available in this preview. Please use the email link below.",
  };

  function detectLang() {
    const path = window.location.pathname;
    if (path.includes("/de/")) return "de";
    if (path.includes("/it/")) return "it";
    if (path.includes("/en/")) return "en";
    return "en";
  }

  function setStatus(text, type) {
    statusEl.hidden = false;
    statusEl.textContent = text;
    statusEl.classList.remove("is-success", "is-error");
    if (type) statusEl.classList.add(type);
  }

  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    submitBtn.disabled = true;
    submitBtn.textContent = messages.sending;
    statusEl.hidden = true;

    const data = {
      name: form.name.value.trim(),
      email: form.email.value.trim(),
      company: form.company.value.trim(),
      message: form.message.value.trim(),
      website: form.website.value,
      lang: detectLang(),
    };

    try {
      const res = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      if (!res.ok) {
        let detail = "";
        try {
          const payload = await res.json();
          detail = payload.error || "";
        } catch {
          /* non-JSON response */
        }
        if (res.status === 503 && detail) {
          throw new Error(detail);
        }
        if (res.status === 404) {
          throw new Error("local");
        }
        throw new Error(detail || "Request failed");
      }

      form.reset();
      setStatus(messages.success, "is-success");
    } catch (err) {
      if (err.message === "local") {
        setStatus(messages.local, "is-error");
      } else {
        setStatus(messages.error, "is-error");
      }
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = defaultLabel;
    }
  });
})();
