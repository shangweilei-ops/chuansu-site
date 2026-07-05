/* ==========================================================================
   Jason Shang · Personal Site
   Mobile nav + scroll reveal
   ========================================================================== */

(function () {
  // Mark JS as loaded so CSS reveal animation can opt-in
  document.documentElement.classList.add('js-reveal');

  // --- Mobile nav toggle ---
  const btn = document.querySelector('.nav__menu-btn');
  const links = document.querySelector('.nav__links');
  if (btn && links) {
    btn.addEventListener('click', () => {
      const open = links.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => links.classList.remove('is-open'));
    });
  }

  // --- Scroll reveal ---
  const targets = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && targets.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          io.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
    targets.forEach(t => io.observe(t));
  } else {
    targets.forEach(t => t.classList.add('is-visible'));
  }

  // --- Update active nav link based on path ---
  const here = location.pathname.replace(/\/$/, '') || '/';
  document.querySelectorAll('.nav__links a').forEach(a => {
    const href = a.getAttribute('href');
    if (!href) return;
    // Build an absolute-style comparison by resolving against current path
    try {
      const resolved = new URL(href, location.origin + here).pathname.replace(/\/$/, '') || '/';
      if (resolved === here) a.classList.add('is-active');
    } catch (e) { /* ignore */ }
  });

  // --- Smooth anchor scroll with nav offset ---
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href').slice(1);
      const el = document.getElementById(id);
      if (!el) return;
      e.preventDefault();
      const top = el.getBoundingClientRect().top + window.scrollY - 70;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });
})();