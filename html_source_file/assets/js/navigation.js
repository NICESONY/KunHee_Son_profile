/* Anchor links work without JavaScript; enhance the visible section. */
(() => {
  const links = [...document.querySelectorAll('.page-navigation a')];
  const sections = links.map(link => document.getElementById(link.hash.slice(1)));
  let scheduled = false;
  function update() {
    const nearBottom = window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 4;
    let active = sections[0];
    for (const section of sections) {
      if (section.getBoundingClientRect().top <= 160) active = section;
    }
    if (nearBottom) active = sections[sections.length - 1];
    links.forEach(link => {
      if (link.hash === '#' + active.id) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    scheduled = false;
  }
  window.addEventListener('scroll', () => {
    if (!scheduled) { scheduled = true; requestAnimationFrame(update); }
  }, { passive: true });
  window.addEventListener('resize', update);
  window.addEventListener('load', update);
  update();
})();
