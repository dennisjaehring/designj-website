/* ============================================================
   DESIGNJ – main.js
   Navigation · Scroll-Animationen · Logo-Slider · Projekt-Filter
   ============================================================ */
(function () {
  'use strict';

  /* ---------- Sticky Nav: Schatten beim Scrollen ---------- */
  const nav = document.querySelector('.nav');
  const onScroll = () => {
    if (!nav) return;
    nav.classList.toggle('is-scrolled', window.scrollY > 8);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Hamburger / Mobile-Menü ---------- */
  const toggle = document.querySelector('.nav__toggle');
  const mobile = document.querySelector('.nav__mobile');
  const closeMobile = () => {
    if (!toggle || !mobile) return;
    toggle.classList.remove('is-open');
    mobile.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('nav-locked');
  };
  if (toggle && mobile) {
    toggle.addEventListener('click', () => {
      const open = mobile.classList.toggle('is-open');
      toggle.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      document.body.classList.toggle('nav-locked', open);
    });
    mobile.querySelectorAll('a').forEach((a) => a.addEventListener('click', closeMobile));
    window.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeMobile(); });
  }

  /* ---------- Aktiven Menüpunkt markieren ---------- */
  const path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav__menu a, .nav__mobile a.m-link').forEach((a) => {
    const href = a.getAttribute('href');
    if (href === path || (path === 'index.html' && href === 'index.html')) {
      a.classList.add('is-active');
    }
  });

  /* ---------- Scroll-Reveal (Intersection Observer) ---------- */
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0, rootMargin: '0px 0px -8% 0px' });
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add('is-visible'));
  }

  /* ---------- Logo-Slider: Inhalt duplizieren für nahtlose Schleife ---------- */
  document.querySelectorAll('.logo-track').forEach((track) => {
    track.innerHTML += track.innerHTML; // 2x → translateX(-50%) loopt nahtlos
  });

  /* ---------- Projekt-Filter (projekte.html) ---------- */
  const filterBtns = document.querySelectorAll('.filter-btn');
  const kacheln = document.querySelectorAll('.projekt-kachel');
  if (filterBtns.length && kacheln.length) {
    filterBtns.forEach((btn) => {
      btn.addEventListener('click', () => {
        filterBtns.forEach((b) => b.classList.remove('is-active'));
        btn.classList.add('is-active');
        const filter = btn.dataset.filter;
        kacheln.forEach((k) => {
          const kat = k.dataset.kategorie || '';
          const show = filter === 'alle' || kat === filter;
          k.classList.toggle('is-hidden', !show);
        });
      });
    });
  }

  /* ---------- Smooth-Scroll für reine #anker (mit Nav-Offset Fallback) ---------- */
  document.querySelectorAll('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href');
      if (id.length < 2) return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      history.replaceState(null, '', id);
    });
  });

  /* ---------- Jahr im Footer ---------- */
  document.querySelectorAll('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });

  /* ---------- Lightbox (Projekt-Galerie) ---------- */
  const galleries = document.querySelectorAll('.proj-gallery');
  if (galleries.length) {
    const links = Array.from(document.querySelectorAll('.proj-gallery a'));
    const lb = document.createElement('div');
    lb.className = 'lightbox';
    lb.innerHTML =
      '<button class="lightbox__close" aria-label="Schließen">&times;</button>' +
      '<button class="lightbox__nav lightbox__prev" aria-label="Vorheriges Bild">&#8249;</button>' +
      '<img alt="">' +
      '<button class="lightbox__nav lightbox__next" aria-label="Nächstes Bild">&#8250;</button>';
    document.body.appendChild(lb);
    const lbImg = lb.querySelector('img');
    let idx = 0;
    const show = (i) => { idx = (i + links.length) % links.length; lbImg.src = links[idx].getAttribute('href'); lbImg.alt = links[idx].querySelector('img') ? links[idx].querySelector('img').alt : ''; };
    const open = (i) => { show(i); lb.classList.add('is-open'); document.body.classList.add('nav-locked'); };
    const close = () => { lb.classList.remove('is-open'); document.body.classList.remove('nav-locked'); };
    links.forEach((a, i) => a.addEventListener('click', (e) => { e.preventDefault(); open(i); }));
    lb.querySelector('.lightbox__close').addEventListener('click', close);
    lb.querySelector('.lightbox__prev').addEventListener('click', (e) => { e.stopPropagation(); show(idx - 1); });
    lb.querySelector('.lightbox__next').addEventListener('click', (e) => { e.stopPropagation(); show(idx + 1); });
    lb.addEventListener('click', (e) => { if (e.target === lb) close(); });
    window.addEventListener('keydown', (e) => {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowLeft') show(idx - 1);
      else if (e.key === 'ArrowRight') show(idx + 1);
    });
  }

})();


/* ---- Testimonial-Slider: Autoplay 6s (Pause bei Hover), Pfeile, Punkte, wischbar ---- */
(function(){
  var sl=document.querySelector('.testi-slider'); if(!sl) return;
  var vp=sl.querySelector('.testi-slider__viewport'),
      prev=sl.querySelector('.testi-slider__prev'),
      next=sl.querySelector('.testi-slider__next'),
      dots=sl.querySelector('.testi-slider__dots');
  var reduce=window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  function pages(){ var w=vp.clientWidth; if(!w) return 1; return Math.max(1, Math.min(24, Math.round(vp.scrollWidth / w))); }
  function cur(){ var w=vp.clientWidth; if(!w) return 0; return Math.round(vp.scrollLeft / w); }
  function ease(t){ return t<0.5 ? 4*t*t*t : 1-Math.pow(-2*t+2,3)/2; }
  var animToken=0;
  function go(i){
    var n=pages(); i=((i%n)+n)%n; var w=vp.clientWidth; if(!w) return;
    var startX=vp.scrollLeft, dist=i*w-startX; if(Math.abs(dist)<2){ update(); return; }
    var my=++animToken, t0=null, dur=750;
    vp.style.scrollSnapType='none';
    function step(ts){
      if(my!==animToken) return;
      if(t0===null)t0=ts; var p=Math.min(1,(ts-t0)/dur);
      vp.scrollLeft=startX+dist*ease(p);
      if(p<1){ requestAnimationFrame(step); }
      else { vp.style.scrollSnapType=''; update(); }
    }
    requestAnimationFrame(step);
  }
  function update(){ var c=cur(); Array.prototype.forEach.call(dots.children,function(d,i){ d.classList.toggle('is-active', i===c); }); }
  function build(){ dots.innerHTML=''; var n=pages(); for(var i=0;i<n;i++){ var b=document.createElement('button'); b.className='testi-slider__dot'; b.type='button'; b.setAttribute('aria-label','Seite '+(i+1)); (function(k){ b.addEventListener('click',function(){ go(k); }); })(i); dots.appendChild(b);} update(); }
  if(prev) prev.addEventListener('click',function(){ go(cur()-1); });
  if(next) next.addEventListener('click',function(){ go(cur()+1); });
  vp.addEventListener('scroll',function(){ window.requestAnimationFrame(update); },{passive:true});
  var timer=null;
  function play(){ if(reduce) return; stop(); timer=setInterval(function(){ go(cur()+1); },6000); }
  function stop(){ if(timer){ clearInterval(timer); timer=null; } }
  sl.addEventListener('mouseenter',stop); sl.addEventListener('mouseleave',play);
  sl.addEventListener('focusin',stop); sl.addEventListener('focusout',play);
  vp.addEventListener('touchstart',stop,{passive:true});
  var rt; window.addEventListener('resize',function(){ clearTimeout(rt); rt=setTimeout(build,200); });
  build(); play();
})();
