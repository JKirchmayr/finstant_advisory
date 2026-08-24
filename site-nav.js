(function () {
  function closeAll(except) {
    document.querySelectorAll(".nav-dropdown.is-open").forEach(function (item) {
      if (item === except) return;
      item.classList.remove("is-open");
      var btn = item.querySelector(".nav-dropdown-btn");
      if (btn) btn.setAttribute("aria-expanded", "false");
    });
  }

  document.addEventListener("click", function (event) {
    var btn = event.target.closest(".nav-dropdown-btn");
    if (btn) {
      var item = btn.closest(".nav-dropdown");
      var open = !item.classList.contains("is-open");
      closeAll(open ? item : null);
      item.classList.toggle("is-open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      return;
    }
    if (!event.target.closest(".nav-dropdown")) closeAll();
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") closeAll();
  });
})();

(function () {
  document.querySelectorAll(".offer-item").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var acc = btn.closest(".offer-acc");
      if (!acc) return;
      var willOpen = !acc.classList.contains("is-open");
      document.querySelectorAll(".offer-acc").forEach(function (other) {
        other.classList.remove("is-open");
        var otherBtn = other.querySelector(".offer-item");
        var otherPanel = other.querySelector(".offer-panel");
        if (otherBtn) otherBtn.setAttribute("aria-expanded", "false");
        if (otherPanel) otherPanel.hidden = true;
      });
      if (willOpen) {
        acc.classList.add("is-open");
        btn.setAttribute("aria-expanded", "true");
        var panel = acc.querySelector(".offer-panel");
        if (panel) panel.hidden = false;
      }
    });
  });
})();
