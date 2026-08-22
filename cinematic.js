(function () {
  const nav = document.getElementById("nav");
  const toggle = document.getElementById("navToggle");
  const links = document.getElementById("navLinks");

  toggle?.addEventListener("click", () => nav.classList.toggle("open"));
  links?.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => nav.classList.remove("open"))
  );

  window.addEventListener(
    "scroll",
    () => nav.classList.toggle("scrolled", window.scrollY > 24),
    { passive: true }
  );

  const focusEls = document.querySelectorAll("[data-focus]");
  if ("IntersectionObserver" in window) {
    const focusObs = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          e.target.classList.toggle(
            "is-focused",
            e.isIntersecting && e.intersectionRatio > 0.35
          );
        });
      },
      { threshold: [0.2, 0.4, 0.6] }
    );
    focusEls.forEach((el) => focusObs.observe(el));

    const revealObs = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("in");
            revealObs.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    document.querySelectorAll(".reveal").forEach((el) => revealObs.observe(el));
  } else {
    document.querySelectorAll(".reveal").forEach((el) => el.classList.add("in"));
    focusEls.forEach((el) => el.classList.add("is-focused"));
  }

  const sections = ["constellation", "proof", "hire", "contact"]
    .map((id) => document.getElementById(id))
    .filter(Boolean);
  const navAnchors = [...document.querySelectorAll(".nav-links a[href^='#']")];
  const sectionObs = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        const id = e.target.id;
        navAnchors.forEach((a) => {
          a.classList.toggle("active", a.getAttribute("href") === "#" + id);
        });
      });
    },
    { rootMargin: "-40% 0px -45% 0px", threshold: 0 }
  );
  sections.forEach((s) => sectionObs.observe(s));
})();
