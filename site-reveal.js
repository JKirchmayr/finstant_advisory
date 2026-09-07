(function () {
  var nodes = Array.prototype.slice.call(document.querySelectorAll(".reveal"));
  if (!nodes.length) return;

  function revealAll() {
    nodes.forEach(function (el) {
      el.classList.add("visible");
      el.classList.remove("is-waiting");
    });
  }

  window.addEventListener("pageshow", function (event) {
    if (event.persisted) revealAll();
  });

  var reduceMotion = false;
  try {
    reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  } catch (err) {}
  if (reduceMotion) {
    revealAll();
    return;
  }

  var observer = null;
  if ("IntersectionObserver" in window) {
    observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("visible");
          entry.target.classList.remove("is-waiting");
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0, rootMargin: "0px 0px -8% 0px" }
    );
  }

  var vh = window.innerHeight || document.documentElement.clientHeight || 0;
  nodes.forEach(function (el) {
    var rect = el.getBoundingClientRect();
    var inView = rect.top < vh && rect.bottom > 0;
    if (inView || !observer) {
      el.classList.add("visible");
      el.classList.remove("is-waiting");
      return;
    }
    el.classList.add("is-waiting");
    observer.observe(el);
  });

  // Hard failsafe: never leave inbound traffic on a washed-out page.
  window.setTimeout(revealAll, 1200);
})();
