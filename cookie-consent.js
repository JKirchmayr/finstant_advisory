(function () {
  var STORAGE_KEY = "finstant-cookie-consent";
  var lang = (document.documentElement.lang || "de").slice(0, 2);
  var i18n = {
    de: {
      title: "Cookies",
      body: "Wir verwenden notwendige Cookies, damit die Website funktioniert. Optionale Cookies setzen wir nur mit Ihrer Einwilligung.",
      accept: "Alle akzeptieren",
      reject: "Nur notwendige",
      settings: "Einstellungen",
      modalTitle: "Cookie-Einstellungen",
      modalBody: "Sie können Ihre Einwilligung jederzeit anpassen. Notwendige Cookies sind für den Betrieb der Seite erforderlich.",
      necessary: "Notwendig",
      necessaryBody: "Erforderlich für grundlegende Funktionen und Speicherung Ihrer Auswahl.",
      analytics: "Analyse",
      analyticsBody: "Helfen uns zu verstehen, wie die Website genutzt wird. Derzeit nicht aktiv.",
      alwaysOn: "Immer aktiv",
      save: "Speichern",
      privacy: "Datenschutzerklärung",
    },
    en: {
      title: "Cookies",
      body: "We use necessary cookies to make this website work. Optional cookies are used only with your consent.",
      accept: "Accept all",
      reject: "Necessary only",
      settings: "Settings",
      modalTitle: "Cookie settings",
      modalBody: "You can change your consent at any time. Necessary cookies are required for the site to function.",
      necessary: "Necessary",
      necessaryBody: "Required for basic functions and to remember your choice.",
      analytics: "Analytics",
      analyticsBody: "Help us understand how the website is used. Currently not active.",
      alwaysOn: "Always on",
      save: "Save",
      privacy: "Privacy policy",
    },
    it: {
      title: "Cookie",
      body: "Utilizziamo cookie necessari al funzionamento del sito. I cookie opzionali vengono usati solo con il vostro consenso.",
      accept: "Accetta tutti",
      reject: "Solo necessari",
      settings: "Impostazioni",
      modalTitle: "Impostazioni cookie",
      modalBody: "Potete modificare il consenso in qualsiasi momento. I cookie necessari sono indispensabili al funzionamento del sito.",
      necessary: "Necessari",
      necessaryBody: "Richiesti per le funzioni di base e per ricordare la vostra scelta.",
      analytics: "Analisi",
      analyticsBody: "Ci aiutano a capire come viene usato il sito. Attualmente non attivi.",
      alwaysOn: "Sempre attivi",
      save: "Salva",
      privacy: "Informativa sulla privacy",
    },
  };
  var t = i18n[lang] || i18n.de;
  var privacyHref =
    lang === "en" ? "/en/privacy/" : lang === "it" ? "/it/privacy/" : "/de/datenschutz/";

  function readConsent() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
    } catch (e) {
      return null;
    }
  }

  function writeConsent(analytics) {
    localStorage.setItem(
      STORAGE_KEY,
      JSON.stringify({ necessary: true, analytics: !!analytics, ts: Date.now() })
    );
  }

  function el(html) {
    var wrap = document.createElement("div");
    wrap.innerHTML = html.trim();
    return wrap.firstElementChild;
  }

  var banner = el(
    '<div class="cookie-banner" role="dialog" aria-live="polite" hidden>' +
      "<h2>" + t.title + "</h2>" +
      "<p>" + t.body + ' <a href="' + privacyHref + '" style="color:#fff;text-decoration:underline;">' + t.privacy + "</a>.</p>" +
      '<div class="cookie-actions">' +
      '<button type="button" class="cookie-btn cookie-btn--primary" data-cookie="accept">' + t.accept + "</button>" +
      '<button type="button" class="cookie-btn cookie-btn--ghost" data-cookie="reject">' + t.reject + "</button>" +
      '<button type="button" class="cookie-btn cookie-btn--ghost" data-cookie="open">' + t.settings + "</button>" +
      "</div></div>"
  );

  var backdrop = el('<div class="cookie-modal-backdrop" hidden></div>');
  var modal = el(
    '<div class="cookie-modal" role="dialog" aria-modal="true" hidden>' +
      "<h2>" + t.modalTitle + "</h2>" +
      "<p>" + t.modalBody + "</p>" +
      '<div class="cookie-row"><div><h3>' + t.necessary + "</h3><p>" + t.necessaryBody +
      '</p></div><label class="cookie-toggle"><input type="checkbox" checked disabled> ' + t.alwaysOn + "</label></div>" +
      '<div class="cookie-row"><div><h3>' + t.analytics + "</h3><p>" + t.analyticsBody +
      '</p></div><label class="cookie-toggle"><input type="checkbox" id="cookie-analytics"> ' + t.analytics + "</label></div>" +
      '<div class="cookie-actions" style="margin-top:1rem;">' +
      '<button type="button" class="cookie-btn cookie-btn--primary" data-cookie="save">' + t.save + "</button>" +
      '<button type="button" class="cookie-btn cookie-btn--ghost" data-cookie="close">' + t.reject + "</button>" +
      "</div></div>"
  );

  function showBanner(on) { banner.hidden = !on; }
  function showModal(on) {
    backdrop.hidden = !on;
    modal.hidden = !on;
    if (on) {
      var stored = readConsent();
      modal.querySelector("#cookie-analytics").checked = !!(stored && stored.analytics);
    }
  }

  function accept(all) {
    writeConsent(all);
    showBanner(false);
    showModal(false);
  }

  document.addEventListener("click", function (e) {
    var open = e.target.closest("[data-cookie-settings], .js-cookie-settings");
    if (open) {
      e.preventDefault();
      showModal(true);
      return;
    }
    var action = e.target.closest("[data-cookie]");
    if (!action) return;
    var type = action.getAttribute("data-cookie");
    if (type === "accept") accept(true);
    if (type === "reject") accept(false);
    if (type === "open") showModal(true);
    if (type === "close") showModal(false);
    if (type === "save") accept(modal.querySelector("#cookie-analytics").checked);
  });

  backdrop.addEventListener("click", function () { showModal(false); });

  document.body.appendChild(banner);
  document.body.appendChild(backdrop);
  document.body.appendChild(modal);

  if (!readConsent()) showBanner(true);
})();
