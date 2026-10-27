// Visualizzatore di slide per Ham Radio Pills (pdf.js da CDN, con ripiego su iframe)
const V='4.10.38', CDN=`https://cdn.jsdelivr.net/npm/pdfjs-dist@${V}/build/`;
const box=document.querySelector('.slider'); if(box){
const url=box.dataset.pdf, cv=box.querySelector('canvas'), lab=box.querySelector('.cnt'), stage=box.querySelector('.stage');
const KS='hrp-slides', dk=()=>{try{return localStorage.getItem(KS)!=='light'}catch(e){return true}};
box.classList.toggle('darkslides',dk());
box.querySelector('.tone').onclick=e=>{e.stopPropagation();const on=!box.classList.contains('darkslides');box.classList.toggle('darkslides',on);try{localStorage.setItem(KS,on?'dark':'light')}catch(_){}};
const tb=box.querySelector('.tone'); const vis=()=>{tb.style.display=document.documentElement.getAttribute('data-theme')==='dark'?'':'none'}; vis();
new MutationObserver(vis).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
const fallback=()=>{stage.innerHTML=`<iframe src="${url}#view=FitH" title="PDF"></iframe>`;box.querySelector('.sctl').style.display='none'};
try{
  const pdfjs=await import(CDN+'pdf.min.mjs'); pdfjs.GlobalWorkerOptions.workerSrc=CDN+'pdf.worker.min.mjs';
  const doc=await pdfjs.getDocument(url).promise; let n=1, busy=null;
  const show=async k=>{n=Math.min(Math.max(k,1),doc.numPages); lab.textContent=`${n} / ${doc.numPages}`;
    const pg=await doc.getPage(n); const w=stage.clientWidth*(window.devicePixelRatio||1);
    const vp=pg.getViewport({scale:w/pg.getViewport({scale:1}).width}); cv.width=vp.width; cv.height=vp.height;
    if(busy) busy.cancel(); busy=pg.render({canvasContext:cv.getContext('2d'),viewport:vp}); try{await busy.promise}catch(e){}};
  box.querySelector('.prev').onclick=()=>show(n-1); box.querySelector('.next').onclick=()=>show(n+1);
  box.querySelector('.fs').onclick=()=>{document.fullscreenElement?document.exitFullscreen():box.requestFullscreen?.()};
  document.addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key==='PageDown')show(n+1);if(e.key==='ArrowLeft'||e.key==='PageUp')show(n-1)});
  let x0=null; stage.addEventListener('touchstart',e=>x0=e.touches[0].clientX,{passive:true});
  stage.addEventListener('touchend',e=>{if(x0===null)return;const d=e.changedTouches[0].clientX-x0;if(Math.abs(d)>40)show(n+(d<0?1:-1));x0=null});
  stage.onclick=e=>{const r=stage.getBoundingClientRect();show(n+(e.clientX-r.left>r.width/2?1:-1))};
  let t; addEventListener('resize',()=>{clearTimeout(t);t=setTimeout(()=>show(n),200)}); document.addEventListener('fullscreenchange',()=>setTimeout(()=>show(n),100));
  box.classList.add('ready'); show(1);
}catch(e){console.warn(e);fallback()}}
