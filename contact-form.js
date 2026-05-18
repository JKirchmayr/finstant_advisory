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

      if (!res.ok) throw new Error("Request failed");

      form.reset();
      setStatus(messages.success, "is-success");
    } catch {
      setStatus(messages.error, "is-error");
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = defaultLabel;
    }
  });
})();
