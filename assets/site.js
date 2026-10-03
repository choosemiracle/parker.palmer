
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')}),{threshold:.05});
document.querySelectorAll('.reveal').forEach(e=>io.observe(e));
const q=document.querySelector('[data-site-search]');
if(q){
  const cards=[...document.querySelectorAll('[data-search-card]')];
  q.addEventListener('input',()=>{const v=q.value.trim().toLowerCase();cards.forEach(c=>{c.style.display=!v||c.dataset.searchCard.toLowerCase().includes(v)?'block':'none'})});
}
