// Tema chiaro/scuro di Ham Radio Pills: segue il sistema, oppure la scelta salvata
(function(){
  var K='hrp-theme', d=document.documentElement;
  function saved(){try{return localStorage.getItem(K)}catch(e){return null}}
  function sys(){return window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'}
  function apply(t){d.setAttribute('data-theme',t)}
  apply(saved()||sys());
  if(window.matchMedia) matchMedia('(prefers-color-scheme: dark)').addEventListener('change',function(){if(!saved())apply(sys())});
  document.addEventListener('DOMContentLoaded',function(){
    var b=document.createElement('button'); b.className='themebtn';
    function label(){var dk=d.getAttribute('data-theme')==='dark'; b.textContent=dk?'☀':'☾'; b.title=dk?'Passa al tema chiaro':'Passa al tema scuro'; b.setAttribute('aria-label',b.title)}
    b.onclick=function(){var t=d.getAttribute('data-theme')==='dark'?'light':'dark'; apply(t); try{localStorage.setItem(K,t)}catch(e){} label()};
    label(); document.body.appendChild(b);
  });
})();
