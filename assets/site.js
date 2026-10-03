
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')}),{threshold:.05});
document.querySelectorAll('.reveal').forEach(e=>io.observe(e));
const q=document.querySelector('[data-site-search]');
if(q){
  const cards=[...document.querySelectorAll('[data-search-card]')];
  q.addEventListener('input',()=>{const v=q.value.trim().toLowerCase();cards.forEach(c=>{c.style.display=!v||c.dataset.searchCard.toLowerCase().includes(v)?'block':'none'})});
}

const store=(k,v)=>localStorage.setItem(k,JSON.stringify(v));
const load=(k,d=null)=>{try{const v=localStorage.getItem(k);return v===null?d:JSON.parse(v)}catch(e){return d}};
const esc=s=>(s||'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[m]));

document.querySelectorAll('[data-journal-key]').forEach(el=>{
  const key='palmer:journal:'+el.dataset.journalKey;
  el.value=load(key,'')||'';
  const state=el.parentElement.querySelector('[data-save-state]');
  el.addEventListener('input',()=>{
    store(key,el.value);
    if(state){state.textContent='已自动保存在这台设备';clearTimeout(el._st);el._st=setTimeout(()=>state.textContent='继续写，不必急着整理',1800)}
  });
});

document.querySelectorAll('[data-timer]').forEach(box=>{
  let seconds=Number(box.dataset.defaultSeconds||600), left=seconds, id=null;
  const display=box.querySelector('[data-timer-display]');
  const paint=()=>{const m=String(Math.floor(left/60)).padStart(2,'0'),s=String(left%60).padStart(2,'0');display.textContent=m+':'+s};
  paint();
  box.querySelectorAll('[data-minutes]').forEach(b=>b.addEventListener('click',()=>{clearInterval(id);id=null;seconds=Number(b.dataset.minutes)*60;left=seconds;paint()}));
  const start=box.querySelector('[data-timer-start]'), reset=box.querySelector('[data-timer-reset]');
  start&&start.addEventListener('click',()=>{
    if(id){clearInterval(id);id=null;start.textContent='继续';return}
    start.textContent='暂停';
    id=setInterval(()=>{left=Math.max(0,left-1);paint();if(left===0){clearInterval(id);id=null;start.textContent='开始';box.classList.add('finished');setTimeout(()=>box.classList.remove('finished'),1200)}},1000);
  });
  reset&&reset.addEventListener('click',()=>{clearInterval(id);id=null;left=seconds;paint();if(start)start.textContent='开始'});
});

document.querySelectorAll('[data-record-save]').forEach(btn=>btn.addEventListener('click',()=>{
  const key=btn.dataset.recordSave;
  const ta=document.querySelector('[data-journal-key="'+key+'"]');
  if(!ta||!ta.value.trim()) return;
  const records=load('palmer:records',[]);
  records.unshift({id:Date.now(),key,title:btn.dataset.recordTitle||document.title,text:ta.value.trim(),time:new Date().toISOString()});
  store('palmer:records',records.slice(0,300));
  const state=btn.parentElement.querySelector('[data-record-state]'); if(state) state.textContent='已加入「我的记录」';
}));

const recordsRoot=document.querySelector('[data-record-list]');
if(recordsRoot){
  const renderRecords=()=>{
    const records=load('palmer:records',[]);
    recordsRoot.innerHTML=records.length?records.map(r=>'<div class="recordItem"><time>'+new Date(r.time).toLocaleString()+'</time><h4>'+esc(r.title)+'</h4><p>'+esc(r.text)+'</p><button class="toolButton" data-delete-record="'+r.id+'">删除</button></div>').join(''):'<div class="card"><p>还没有记录。你在概念页或课程页保存的书写，会出现在这里。</p></div>';
    recordsRoot.querySelectorAll('[data-delete-record]').forEach(b=>b.addEventListener('click',()=>{store('palmer:records',load('palmer:records',[]).filter(r=>String(r.id)!==b.dataset.deleteRecord));renderRecords()}));
  };
  renderRecords();
  const exp=document.querySelector('[data-export-records]');
  exp&&exp.addEventListener('click',()=>{const blob=new Blob([JSON.stringify(load('palmer:records',[]),null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='parker-palmer-records.json';a.click();URL.revokeObjectURL(a.href)});
}

const gen=document.querySelector('[data-question-generator]');
if(gen){
  const input=gen.querySelector('[data-question-focus]'), out=gen.querySelector('[data-generated-question]');
  const templates={
    experience:['当你想到「{x}」时，最近一次真实发生的经验是什么？','「{x}」在你生命里曾以什么具体形式出现？'],
    image:['如果「{x}」是一幅画面，它现在更像什么？','有没有一个物件、场景或自然意象能够表达你与「{x}」的关系？'],
    tension:['围绕「{x}」，有哪些两件看似冲突但都真实的事情同时存在？','「{x}」里哪一处张力最难被你同时承认？'],
    body:['当你说到「{x}」时，身体哪里最先有反应？','如果不解释，只留意身体，「{x}」让你感到扩展、收紧，还是别的什么？'],
    possibility:['关于「{x}」，有什么可能性是你还没有允许自己认真考虑的？','如果暂时不问“该不该”，「{x}」正在邀请你看见什么？'],
    next:['关于「{x}」，什么是一个足够小、但更诚实的下一步？','如果只让内外差距缩小一点点，「{x}」里你愿意尝试什么？']
  };
  const make=()=>{const x=(input.value||'这件事').trim();const lens=(gen.querySelector('[name="lens"]:checked')||{}).value||'experience';const arr=templates[lens];out.textContent=arr[Math.floor(Math.random()*arr.length)].replace('{x}',x)};
  gen.querySelector('[data-generate-question]').addEventListener('click',make);make();
}

document.querySelectorAll('[data-module-complete]').forEach(btn=>{
  const key=btn.dataset.moduleComplete; const done=load('palmer:course:hidden-wholeness',[]);
  const paint=()=>btn.textContent=done.includes(key)?'✓ 已完成':'标记本课完成';
  paint();
  btn.addEventListener('click',()=>{const i=done.indexOf(key);if(i>=0)done.splice(i,1);else done.push(key);store('palmer:course:hidden-wholeness',done);paint()});
});
document.querySelectorAll('[data-course-progress]').forEach(el=>{
  const total=Number(el.dataset.total||1), done=load('palmer:course:hidden-wholeness',[]).length, pct=Math.min(100,Math.round(done/total*100));
  el.style.width=pct+'%'; const label=document.querySelector('[data-course-progress-label]'); if(label)label.textContent=done+' / '+total+' 课';
});
document.querySelectorAll('[data-study-record-count]').forEach(el=>el.textContent=load('palmer:records',[]).length);
document.querySelectorAll('[data-study-course-count]').forEach(el=>el.textContent=load('palmer:course:hidden-wholeness',[]).length);
