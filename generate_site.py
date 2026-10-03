from pathlib import Path
import html
import json
import shutil

ROOT = Path(__file__).resolve().parent
GENERATED_DIRS = [
    "assets", "worldview", "genealogy", "concepts", "books", "practice",
    "applications", "pathways", "glossary", "sources"
]
for name in GENERATED_DIRS:
    p = ROOT / name
    if p.exists():
        shutil.rmtree(p)
    p.mkdir(parents=True, exist_ok=True)

CSS = r"""
:root{
  --ink:#142338;--ink2:#20364d;--ink3:#2c4760;--paper:#f6f1e8;--paper2:#ece4d7;
  --gold:#b48443;--gold2:#e5c78e;--green:#516d5a;--red:#86514a;--muted:#68717a;
  --line:rgba(20,35,56,.14);--white:#fffdf8;--r:22px;--max:1180px
}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;color:var(--ink);background:radial-gradient(circle at 88% 4%,rgba(180,132,67,.12),transparent 28rem),linear-gradient(#faf7f1,#f1eadf);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;line-height:1.8}
a{color:inherit}.shell{width:min(var(--max),calc(100% - 36px));margin:auto}
.top{position:sticky;top:0;z-index:50;background:rgba(249,246,239,.94);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.topin{min-height:64px;display:flex;align-items:center;justify-content:space-between;gap:18px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:800}.mark{width:31px;height:31px;border:1px solid var(--gold);border-radius:50%;position:relative}
.mark:before,.mark:after{content:"";position:absolute;border-radius:50%;inset:7px;border:1px solid var(--gold)}.mark:after{inset:13px;background:var(--gold);border:0}
nav{display:flex;gap:15px;font-size:13px;color:#59636d}nav a{text-decoration:none}.crumbs{padding:19px 0 0;color:#7b8187;font-size:13px}.crumbs a{text-decoration:none}
.hero{padding:36px 0 34px}.heroGrid{display:grid;grid-template-columns:1.18fr .82fr;gap:18px}.heroMain,.heroSide{border-radius:28px;overflow:hidden;box-shadow:0 22px 60px rgba(20,35,55,.09)}
.heroMain{min-height:510px;padding:50px;background:linear-gradient(145deg,#132238,#223d52);color:white;position:relative}.heroMain.compact{min-height:410px}
.eyebrow,.kicker{font-size:11px;font-weight:800;letter-spacing:.17em;text-transform:uppercase;color:var(--gold)}.hero .eyebrow{color:var(--gold2)}
h1{font-size:clamp(43px,6vw,74px);line-height:1.05;letter-spacing:-.05em;margin:15px 0 20px}h1 em{font-style:normal;color:var(--gold2)}
.lead{font-size:18px;color:rgba(255,255,255,.79);max-width:760px}.actions{display:flex;gap:9px;flex-wrap:wrap;margin-top:27px}
.btn{display:inline-block;text-decoration:none;border-radius:999px;padding:9px 15px;border:1px solid rgba(255,255,255,.22);font-size:13px;font-weight:700}.btn.primary{background:var(--gold2);color:var(--ink);border:0}
.heroFoot{position:absolute;left:50px;right:50px;bottom:27px;padding-top:15px;border-top:1px solid rgba(255,255,255,.15);font-size:12px;color:rgba(255,255,255,.52)}
.heroSide{padding:28px;background:linear-gradient(155deg,#d7cdbb,#9cab9f);display:flex;flex-direction:column;justify-content:space-between}
.orb{height:270px;display:grid;place-items:center}.orb .r{width:210px;height:210px;border:1px solid rgba(255,255,255,.75);border-radius:50%;display:grid;place-items:center;box-shadow:0 0 0 31px rgba(255,255,255,.12),0 0 0 62px rgba(255,255,255,.07)}
.orb .r span{width:70px;height:70px;border-radius:50%;background:#f1d9a9;box-shadow:0 0 44px rgba(250,224,170,.9);display:grid;place-items:center;text-align:center;font-size:10px;font-weight:800}
.sideCard{background:rgba(255,253,248,.86);border-radius:18px;padding:20px}.sideCard h3{margin:4px 0 7px;font-size:21px}.sideCard p{margin:0;color:#5e6670;font-size:14px}
.section{padding:56px 0}.head{display:grid;grid-template-columns:.72fr 1.28fr;gap:28px;align-items:end;margin-bottom:25px}.head h2{font-size:clamp(32px,4.3vw,52px);line-height:1.1;letter-spacing:-.04em;margin:7px 0 0}.head p{margin:0;color:#5c6570;font-size:16px}
.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:15px}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:15px}.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.card{background:rgba(255,255,255,.68);border:1px solid var(--line);border-radius:var(--r);padding:24px}.card h3{font-size:22px;line-height:1.3;margin:8px 0}.card p{margin:0;color:#5e6670}
.tag{font-size:11px;font-weight:800;letter-spacing:.13em;text-transform:uppercase;color:var(--gold)}.mini{margin-top:15px;padding-top:13px;border-top:1px solid var(--line);font-size:13px;color:#777e85}
.tile{display:block;text-decoration:none;min-height:215px;position:relative;overflow:hidden;transition:.18s}.tile:hover{transform:translateY(-3px);border-color:rgba(180,132,67,.55)}.tile .arrow{position:absolute;right:18px;bottom:15px;color:var(--gold);font-size:22px}.tile small{display:block;color:#888;margin-top:12px}
.dark{background:var(--ink2);color:white}.dark p,.dark li{color:rgba(255,255,255,.71)}.dark .mini{border-color:rgba(255,255,255,.14);color:rgba(255,255,255,.56)}
.quote{border-left:3px solid var(--gold);padding:5px 0 5px 18px;font-size:20px;line-height:1.65;color:#2f3d4d}.question{background:var(--gold2);color:var(--ink)}.question p{color:var(--ink);font-size:19px;font-weight:700}
.articleLayout{display:grid;grid-template-columns:245px 1fr;gap:35px}.toc{position:sticky;top:86px;align-self:start}.toc a{display:block;padding:7px 0;text-decoration:none;color:#64707a;border-bottom:1px solid var(--line);font-size:14px}
.article h2{font-size:34px;line-height:1.16;margin:10px 0 15px}.article h3{font-size:23px;margin:28px 0 8px}.article p,.article li{color:#4f5964}.article ul,.article ol{padding-left:22px}.article section{scroll-margin-top:88px}
.practiceBox{background:#e9e1d4;border-radius:22px;padding:23px;margin:22px 0}.practiceBox h3{margin-top:0}.caution{background:#efe3df;border-left:4px solid var(--red);padding:18px 20px;border-radius:12px;margin:18px 0}.sourceBox{background:#f0eadf;border-radius:22px;padding:22px;margin-top:26px}.sourceBox li{margin:7px 0}
.rail{display:flex;gap:8px;flex-wrap:wrap;margin:20px 0}.rail a{padding:7px 11px;border:1px solid var(--line);border-radius:999px;text-decoration:none;font-size:12px;background:rgba(255,255,255,.65)}.rail a.current{background:var(--ink);color:white}
.table{width:100%;border-collapse:collapse;background:rgba(255,255,255,.55);border-radius:18px;overflow:hidden}.table th,.table td{text-align:left;padding:13px;border-bottom:1px solid var(--line);vertical-align:top}.table th{font-size:12px;color:#68717b}
.steps{counter-reset:step;display:grid;gap:10px}.step{display:grid;grid-template-columns:48px 1fr;gap:14px;align-items:start;background:rgba(255,255,255,.64);border:1px solid var(--line);border-radius:18px;padding:16px}.step:before{counter-increment:step;content:counter(step);width:38px;height:38px;border-radius:50%;background:var(--ink);color:white;display:grid;place-items:center;font-weight:800}
.matrix{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}.matrix .card{min-height:170px}
.searchbar{display:flex;gap:10px;margin:18px 0 24px}.searchbar input{width:100%;border:1px solid var(--line);border-radius:999px;padding:11px 16px;background:white;font:inherit}
.badge{display:inline-block;border-radius:999px;background:#e8dfd0;padding:4px 9px;font-size:11px;color:#6a645c;margin-right:5px}
.footer{margin-top:42px;background:var(--ink);color:rgba(255,255,255,.65);padding:38px 0}.footer strong{color:white}.footer p{max-width:850px;font-size:13px}.reveal{opacity:0;transform:translateY(10px);transition:.45s}.reveal.visible{opacity:1;transform:none}
@media(max-width:1000px){nav{display:none}.heroGrid,.head,.articleLayout{grid-template-columns:1fr}.toc{position:static}.grid3,.grid4{grid-template-columns:repeat(2,1fr)}}
@media(max-width:680px){.heroMain{padding:30px 24px;min-height:590px}.heroMain.compact{min-height:480px}.heroFoot{left:24px;right:24px}.heroSide{min-height:420px}.grid2,.grid3,.grid4,.matrix{grid-template-columns:1fr}.section{padding:44px 0}.table{font-size:13px}}
"""
(ROOT/"assets/site.css").write_text(CSS, encoding="utf-8")

JS = r"""
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')}),{threshold:.05});
document.querySelectorAll('.reveal').forEach(e=>io.observe(e));
const q=document.querySelector('[data-site-search]');
if(q){
  const cards=[...document.querySelectorAll('[data-search-card]')];
  q.addEventListener('input',()=>{const v=q.value.trim().toLowerCase();cards.forEach(c=>{c.style.display=!v||c.dataset.searchCard.toLowerCase().includes(v)?'block':'none'})});
}
"""
(ROOT/"assets/site.js").write_text(JS, encoding="utf-8")

def nav(pref):
    items=[
        ("worldview/","思想总图"),("concepts/","核心概念"),("books/","原著研读"),
        ("practice/","操练方法"),("applications/","应用场景"),("pathways/","研修路径"),("sources/","资料说明")
    ]
    return "<nav>"+"".join(f'<a href="{pref}{u}">{t}</a>' for u,t in items)+"</nav>"

def wrap(title, body, depth=0, desc=""):
    pref="../"*depth
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}｜帕克·帕尔默思想研究</title><meta name="description" content="{html.escape(desc or title)}"><link rel="stylesheet" href="{pref}assets/site.css"></head><body><header class="top"><div class="shell topin"><a class="brand" href="{pref}index.html"><span class="mark"></span>帕克·帕尔默思想研究</a>{nav(pref)}</div></header>{body}<footer class="footer"><div class="shell"><strong>帕克·帕尔默思想研究与生命实践</strong><p>独立中文研究项目。内容以 Parker J. Palmer 原著、带领指南与相关研究文献为基础；本站将“原著思想”“后续实践发展”“本站整理与应用”尽量分开呈现。Circle of Trust® 等相关名称归其权利方所有。</p></div></footer><script src="{pref}assets/site.js"></script></body></html>'''

def crumbs(depth, parts):
    pref="../"*depth
    pieces=[f'<a href="{pref}index.html">首页</a>']
    for i,(name,url) in enumerate(parts):
        pieces.append(f'<a href="{url}">{name}</a>' if url else name)
    return '<div class="shell crumbs">'+" / ".join(pieces)+"</div>"

def cards(items, cls="grid3"):
    return f'<div class="{cls}">'+"".join(items)+"</div>"

def tile(url, tag, title, summary, search=""):
    s=html.escape((search+" "+title+" "+summary).lower())
    return f'<a class="card tile reveal" data-search-card="{s}" href="{url}"><span class="tag">{tag}</span><h3>{title}</h3><p>{summary}</p><span class="arrow">→</span></a>'

# ---------- Thought architecture ----------
world_movements=[
("01","从外部标准回到生命本身","Palmer 的起点不是“怎样成为更优秀的人”，而是停止只从外部规范、职业角色和他人期待来定义自己。","Let Your Life Speak"),
("02","从人格表演回到真实自我","身份包含天赋，也包含限制、伤痕、恐惧和历史。完整性不是完美，而是更真实地与这些力量相处。","The Courage to Teach"),
("03","从分裂走向 soul 与 role 的重新连接","当角色长期背叛内在知道的真相，人会进入 divided life；“不再分裂”意味着把内在真实逐步带回工作、关系与制度。","A Hidden Wholeness"),
("04","从孤立内省进入可信赖共同体","内在工作不是独自完成。人需要一种既不侵入、也不回避的关系空间，来保护内在导师的声音。","A Hidden Wholeness"),
("05","从直接纠正转向间接唤醒","第三物、隐喻、诗歌、故事、沉默与开放问题都在减少控制，让真相从参与者内部浮现。","A Hidden Wholeness / Courage to Teach"),
("06","从二元对立进入悖论与张力","许多深层问题不是非此即彼：行动与沉思、个人与共同体、现实与可能，需要在更大的容器里同时被承载。","The Courage to Teach / The Active Life"),
("07","从认识的占有转向关系与忠实","认识不只是把对象变成信息；Palmer 把 knowing 与 loving、troth、community of truth 联系起来。","To Know as We Are Known"),
("08","从私人完整性走向公共世界","内在工作最终进入教学、领导、组织和公民生活；完整性通过共同体、公共表达和制度实践获得社会形态。","The Courage to Teach / Healing the Heart of Democracy")
]

# ---------- Concepts ----------
concepts=[
{
"slug":"inner-teacher","cn":"内在导师","en":"Inner Teacher","verb":"聆听",
"summary":"不是一个替你做决定的神秘权威，而是人内在能够辨认真实、意义与方向的资源。Palmer 的方法不是“告诉人答案”，而是保护这个声音能够被自己听见。",
"where":"在《Let Your Life Speak》中，它表现为“听生命在说什么”；在《A Hidden Wholeness》中，它成为信任圈实践的中心；在教育文本中，它对应教师和学习者不可被外部技术取代的主体性。",
"misread":["不是“第一念头就是真理”——内在导师需要时间、现实检验和关系中的辨识。","不是反智或拒绝他人意见——Palmer 强调从他人学习，但不把最终判断权交出去。"],
"practice":["静默 5 分钟，只记录浮现的念头、感受、身体反应，不判断。","把自己今天说过的一句话写下来，问：这句话可能正在告诉我什么？","分两栏写：别人希望我知道的 / 我其实已经知道但还没承认的。"],
"sources":["Let Your Life Speak，第1章 Listening to Life","A Hidden Wholeness，Circle of Trust touchstones：Attend to your own inner teacher"],
"related":["true-self","vocation","trustworthy-community"]
},
{
"slug":"soul","cn":"灵魂 / 内在生命","en":"Soul","verb":"保护",
"summary":"Palmer 用 soul 指向一个脆弱却坚韧的内在核心。它不像自我展示那样喧闹，更像野生动物：只有在不被追捕、分析和强迫的空间里才会出现。",
"where":"“灵魂”是《A Hidden Wholeness》的核心语言，用来解释为什么信任圈必须强调邀请、边界、沉默、保密与不修理他人。",
"misread":["不是必须接受某种宗教教义才能理解；Palmer 也用 true self、inner teacher 等语言指向相近经验。","不是脆弱到需要被保护免于一切挑战；真正的保护，是免于侵入与操控，从而能够面对真实。"],
"practice":["回想一个你曾经“缩回去”的群体场景，写下当时发生了什么。","回想一个你愿意说真话的空间，列出它的三个条件。","设计一个下次聚会的“少做一件事”：少追问、少点评或少解释。"],
"sources":["A Hidden Wholeness，第3–5章","A Hidden Wholeness Guide，touchstones"],
"related":["inner-teacher","trustworthy-community","third-things"]
},
{
"slug":"true-self","cn":"真实自我","en":"True Self","verb":"认出",
"summary":"真实自我不是理想化的“最好版本”，而是生命经验持续显露出来的气质、天赋、限制、渴望、身体反应与边界。",
"where":"《Let Your Life Speak》把使命建立在 true self 上；《The Courage to Teach》把身份理解为内外力量交汇的动态中心；《A Hidden Wholeness》把 true self 与 soul 放在同一脉络中。",
"misread":["不是“想做什么就做什么”；真实自我同时包含限制。","不是固定不变的人格标签；Palmer 强调身份是不断形成的交汇点。"],
"practice":["列三件让你持续有生命力的事，以及三件长期让你枯竭的事。","回顾一次失败，暂时不问“哪里做错了”，只问“它让我更清楚自己不是什么了吗？”","观察一周：哪些场景让身体放松，哪些场景让你持续收紧？"],
"sources":["Let Your Life Speak，第1–3章","The Courage to Teach，第1章 Identity and Integrity"],
"related":["inner-teacher","identity-integrity","vocation"]
},
{
"slug":"identity-integrity","cn":"身份与完整性","en":"Identity & Integrity","verb":"对齐",
"summary":"身份回答“我是谁”；完整性关乎我怎样让构成生命的不同力量形成较真实的关系。完整不是没有矛盾，而是不再靠切割自己来维持角色。",
"where":"这是《The Courage to Teach》的基础命题：好的教学来自教师的 identity and integrity，而不只是 technique。",
"misread":["完整性不是“始终一致、不改变”；它允许成长、修正与复杂性。","完整性不是道德优越；Palmer 明确把阴影、限制、伤痕和恐惧也纳入身份。"],
"practice":["画两个圆：内在的我 / 外在角色，写出重叠区与断裂区。","写一句：我最常用哪个角色保护自己不被真正看见？","选一个小场景，让下周的内外差距缩小 5%。"],
"sources":["The Courage to Teach，第1章","The Courage to Teach Guide，Identity & Integrity 反思"],
"related":["true-self","undivided-life","paradox"]
},
{
"slug":"vocation","cn":"使命与召唤","en":"Vocation","verb":"辨识",
"summary":"使命不是先设计一个伟大目标，再强迫自己实现；它来自倾听生命已经在说什么。天赋、限制、失败、关闭的道路与反复出现的关切，都是线索。",
"where":"《Let Your Life Speak》把 vocation 与 voice 联系起来：召唤不是一个追逐的目标，而是一种被听见的声音。",
"misread":["不是“找到唯一正确职业”；使命可能穿过多种角色。","不是把个人欲望神圣化；辨识必须面对限制、关系与现实后果。"],
"practice":["写下三次“路关闭”的经历；每次只问：它让我知道了什么？","列出你反复被吸引去关心的问题，不问是否能成功。","把“我应该做什么？”改写成“什么事情已经在向我提出要求？”"],
"sources":["Let Your Life Speak，第1章 Listening to Life；第3章 When Way Closes","Let Your Life Speak，第5章 Leading from Within"],
"related":["inner-teacher","true-self","seasons"]
},
{
"slug":"wholeness","cn":"完整 / 隐藏的完整性","en":"Wholeness","verb":"记起",
"summary":"Palmer 的 wholeness 不是完美，而是破碎表面之下仍存在一种更深的连结。成长不是制造一个无缺的自我，而是恢复与自己、他人、世界之间被切断的关系。",
"where":"这一意象贯穿《The Active Life》《The Courage to Teach》《A Hidden Wholeness》，并受到 Thomas Merton 的深刻影响。",
"misread":["不是否认创伤、冲突或制度问题。","不是“万事本来都好”；隐藏的完整性要通过真实关系与行动被重新发现。"],
"practice":["画一张“生命碎片图”：工作、关系、身体、价值、创造、休息分别处在什么位置？","找一条被长期切断的连接，设计一个低风险的恢复动作。","记录本周一次“表面破碎、但仍感到某种完整”的时刻。"],
"sources":["A Hidden Wholeness，Chapter I Images of Integrity","The Active Life，hidden wholeness 主题"],
"related":["identity-integrity","undivided-life","paradox"]
},
{
"slug":"divided-life","cn":"分裂的生命","en":"Divided Life","verb":"看见",
"summary":"divided life 指一个人长期把自己真正知道、真正重视的东西与外在角色分开，甚至靠自我背叛维持安全、地位或归属。",
"where":"《A Hidden Wholeness》前半部诊断分裂的生命及其个人与社会后果；《The Courage to Teach》也用它理解教师的恐惧与制度处境。",
"misread":["不是偶尔妥协就等于“虚伪人格”；Palmer 关心的是长期结构性的内外断裂。","不是鼓励冲动式“做真实的自己”；从分裂走向完整需要共同体、辨识和承担后果。"],
"practice":["写下一个“我知道 / 我却做”的具体场景。","分别列出保持分裂的收益与代价。","问：我需要什么支持，才可能少分裂一点？"],
"sources":["A Hidden Wholeness，第1–2章","The Courage to Teach，Divided No More movement model"],
"related":["undivided-life","identity-integrity","trustworthy-community"]
},
{
"slug":"undivided-life","cn":"不再分裂地生活","en":"Divided No More","verb":"行动",
"summary":"“不再分裂”不是从此没有冲突，而是不再把自己已经认出的真相长期留在私人角落。它是一种把 inner truth 带进 outer world 的决定。",
"where":"在《A Hidden Wholeness》中，这是整本书的旅程；在《The Courage to Teach Guide》中，它成为社会改变四阶段的第一阶段。",
"misread":["不是戏剧性地一次性辞职、决裂或公开表态。","不是孤勇；Palmer 强调 communities of congruence 对持续行动的重要性。"],
"practice":["只选一个场景：一句话、一次拒绝、一个边界、一次申请。","写清“我要停止配合什么？”与“我要开始支持什么？”","行动后回到伙伴或小组，只复盘经验，不急着证明自己正确。"],
"sources":["A Hidden Wholeness，全书主轴","The Courage to Teach Guide，Four Stages of Social Change"],
"related":["divided-life","trustworthy-community","public-life"]
},
{
"slug":"paradox","cn":"悖论与张力","en":"Paradox & Tension","verb":"承载",
"summary":"许多“深层真理”不能用非此即彼解决：独处与共同体、沉思与行动、个人与公共、现实与可能，都需要 both-and 的容量。",
"where":"《The Courage to Teach》把 paradox 作为思考完整性的核心方式；《The Active Life》以 contemplation-and-action 的悖论开篇。",
"misread":["不是逻辑混乱；经验事实仍需要辨真假。","不是永远不做决定；承载张力是为了让决定更不仓促、更少被恐惧控制。"],
"practice":["把困境写成两句都是真的话：A 是真的；B 也是真的。","分别写出两端最害怕失去什么。","设置一个“暂不裁决期”，只搜集新的经验信息。"],
"sources":["The Courage to Teach，第3章 The Hidden Wholeness: Paradox in Teaching and Learning","The Active Life，Session 1"],
"related":["wholeness","tragic-gap","active-life"]
},
{
"slug":"trustworthy-community","cn":"可信赖的共同体","en":"Trustworthy Community","verb":"相遇",
"summary":"好的共同体既不侵入一个人的完整性，也不逃避他的挣扎。它让人被陪伴，却不被占领。",
"where":"《A Hidden Wholeness》第4–5章讨论为什么孤独的内在旅程仍需要关系，并提出 circle of trust 的空间结构。",
"misread":["不是“彼此什么都不能说”；可以回应，但要避免替对方解释和接管。","不是舒适至上；可信赖空间允许困难真相出现。"],
"practice":["回顾一次被过度建议的谈话，写下你当时真正需要的是什么。","两人轮流说 5 分钟，听者只复述和提问。","小组讨论前先共同确认：什么是邀请，什么是压力？"],
"sources":["A Hidden Wholeness，第4–5章","Courage & Renewal touchstones"],
"related":["inner-teacher","honest-open-questions","third-things"]
},
{
"slug":"truth-conversation","cn":"真理作为持续对话","en":"Truth as Conversation","verb":"共同探寻",
"summary":"Palmer 既拒绝“我拥有最终答案”的绝对主义，也拒绝“各有各的真理、互不相干”的相对主义。他把真理理解为关于重要事物的一场持续、严肃而有纪律的对话。",
"where":"《A Hidden Wholeness》讨论 circle of trust 中 truth 如何从差异与关联之间逐渐显现；《To Know as We Are Known》则用 troth 强调真理中的忠实关系。",
"misread":["不是为了达成表面一致。","不是把冲突取消，而是让差异不必以征服对方的方式出现。"],
"practice":["在一个分歧上，用三句话表达自己的经验，不解释对方。","听完对方后先说“我听见了什么”，再说“我仍不同意什么”。","写下：这场对话让我看到的更大事实是什么？"],
"sources":["A Hidden Wholeness，truth / tapestry of truth","To Know as We Are Known，troth / community of truth"],
"related":["knowing-loving","trustworthy-community","public-life"]
},
{
"slug":"knowing-loving","cn":"认识即关系","en":"Knowing Is Loving","verb":"进入关系",
"summary":"Palmer 批评把“认识”变成控制、占有和把对象置于对立面。他主张认识是一种进入关系、接受被改变、对所知之物负责任的方式。",
"where":"《To Know as We Are Known》从 Knowing Is Loving 出发，发展 community of troth、teaching as creating space 等教育思想。",
"misread":["不是取消事实、证据和分析。","不是把知识变成情绪体验；它要求更深的责任与相互校正。"],
"practice":["选一个你熟悉的对象：学生、工作、自然、文本。写下你“关于它知道什么”和“与它处在什么关系”。","找一个你常用来控制的知识动作：分类、打分、诊断、预测。问它遮蔽了什么。","设计一个让对象也能“反过来改变你”的学习动作。"],
"sources":["To Know as We Are Known，第1章 Knowing Is Loving","To Know as We Are Known，第5–6章 Teaching / Truth"],
"related":["truth-conversation","education-space","third-things"]
},
{
"slug":"third-things","cn":"第三物与隐喻","en":"Third Things","verb":"斜着说",
"summary":"诗歌、故事、图像、音乐、自然物等可以成为第三物。参与者先共同面对一个对象，再让它折射自己的经验，避免把人直接放在被审视的位置。",
"where":"《A Hidden Wholeness》第6章 The Truth Told Slant 详细发展这一方法；《The Courage to Teach》也用 subject-centered / third thing 对抗过度教师中心或学生中心。",
"misread":["不是拿艺术作品做心理测验。","不是要求大家得出同一解释；第三物的价值恰恰在于允许多义。"],
"practice":["先描述你看见/听见什么，再谈它触动了什么；顺序不要倒。","使用“这让我想到……”而不是“这首诗就是在说……”","分享后不点评彼此解释，只让不同声音并置。"],
"sources":["A Hidden Wholeness，第6章","A Hidden Wholeness Guide，Common Ground & Third Things"],
"related":["truth-conversation","trustworthy-community","education-space"]
},
{
"slug":"honest-open-questions","cn":"开放而诚实的问题","en":"Honest, Open Questions","verb":"帮助对方听见自己",
"summary":"真正的开放问题不是把建议藏进问号里，而是提问者并不知道答案，并且愿意让问题服务于对方的发现。",
"where":"这是 circle of trust 与 clearness committee 的核心纪律，用来替代纠正、分析、建议和“修理”。",
"misread":["“你为什么不直接辞职？”不是开放问题，它已经塞入建议。","“你是不是因为童年……”也不是开放问题，它预设了解释。"],
"practice":["把一个建议句改成三个你真的不知道答案的问题。","提问前问自己：这个问题服务谁——我的好奇，还是对方的辨识？","问题后至少留 10 秒，不用第二个问题追赶。"],
"sources":["A Hidden Wholeness，touchstones / clearness committee","The Courage to Teach Guide，Touchstones"],
"related":["honest-open-questions","trustworthy-community","inner-teacher"]
},
{
"slug":"education-space","cn":"教学即创造空间","en":"Teaching as Creating Space","verb":"为真理腾出空间",
"summary":"教学不是把知识搬进学生头脑，而是创造一个教师、学生与主题能够共同面对真理的空间，并在当下练习一种不同的关系方式。",
"where":"《To Know as We Are Known》第5章将 teaching 定义为创造一个能够实践对真理忠实的空间；《Meeting for Learning》进一步把学习理解为 meeting。",
"misread":["不是教师退场或放弃专业性。","不是“只要气氛好就会学习”；空间需要主题、纪律、挑战与关系同时存在。"],
"practice":["设计一节课时，先写“共同中心是什么”，再写教师要讲什么。","找一处可以少讲 5 分钟、让学生直接面对材料的地方。","在结束时问：今天这个主题对我们的生活提出了什么要求？"],
"sources":["To Know as We Are Known，第5–6章","Meeting for Learning"],
"related":["knowing-loving","third-things","identity-integrity"]
},
{
"slug":"active-life","cn":"沉思与行动","en":"Contemplation & Action","verb":"活出来",
"summary":"Palmer 不把沉思与行动分成高低两个世界。行动帮助我们共同创造现实；沉思帮助我们揭开伪装成现实的幻象。二者交织，才可能形成更真实的行动。",
"where":"《The Active Life》以 contemplation-and-action 的悖论为核心，进一步讨论行动的阴影、正确行动、失败、稀缺与丰盛。",
"misread":["沉思不是只有静坐；工作、关系、艺术等也可能揭示现实。","行动不是越多越好；忙碌、控制结果和焦虑反应都可能扭曲行动。"],
"practice":["连续三天记录：这是行动，还是反应？","做一件不以结果证明自己价值的 expressive action。","遇到失败时先问它揭露了什么现实，而不是立刻修复形象。"],
"sources":["The Active Life，Session 1–6","The Active Life Leader's Guide"],
"related":["paradox","vocation","nonviolence"]
},
{
"slug":"tragic-gap","cn":"悲剧性张力","en":"The Tragic Gap","verb":"站在中间",
"summary":"悲剧性张力是现实“现在是什么”与我们深知“它可能成为什么”之间的距离。站在其中，不坠向犬儒，也不逃进虚假乐观。",
"where":"《A Hidden Wholeness》第10章与《Healing the Heart of Democracy》把 tension-holding 与非暴力、公共生活和 broken-open heart 连接起来。",
"misread":["不是无限忍耐伤害。","不是拒绝做决定；Palmer 明确指出承载张力并不等于犹豫不决。"],
"practice":["写下：现实是……；我仍相信可能……","写下什么会把你拉向犬儒，什么会把你拉向不切实际的乐观。","列出三个帮助你在张力中保持完整的人、地方或习惯。"],
"sources":["A Hidden Wholeness，第10章","Healing the Heart of Democracy，broken-open heart / tension-holding"],
"related":["paradox","nonviolence","public-life"]
},
{
"slug":"nonviolence","cn":"日常非暴力","en":"Nonviolence in Everyday Life","verb":"走第三条路",
"summary":"Palmer 所说的非暴力不是被动退让，而是在不侵犯自己与他人灵魂的前提下寻找第三种回应：不逃跑，也不以暴力和控制反击。",
"where":"《A Hidden Wholeness》第10章把 circle of trust 的纪律带回组织、关系和社会改变：提问替代争辩、真话替代羞辱、支持共同体帮助人持续行动。",
"misread":["不是避免冲突。","不是为了操控一个更好结果；非暴力首先是尊重人的灵魂本身。"],
"practice":["找一个惯常只有“忍 / 爆”两种选择的场景，写出第三种回应。","在一次会议中，把一个反驳改成诚实问题。","行动前先确认：我能否既不背叛自己，也不贬低对方？"],
"sources":["A Hidden Wholeness，第10章 The Third Way","A Hidden Wholeness，agents of nonviolence"],
"related":["tragic-gap","undivided-life","public-life"]
},
{
"slug":"public-life","cn":"公共生活","en":"Public Life","verb":"带回世界",
"summary":"Palmer 的内在工作从来不只为了私人安宁。它最终进入学校、组织、职业共同体与公共空间，检验人能否在差异、压力与制度中仍保持声音、关系和完整性。",
"where":"从早期《The Company of Strangers》到《Healing the Heart of Democracy》，Palmer 持续讨论陌生人、公共空间、差异和公民心灵。",
"misread":["不是把内在修炼变成某种政治立场训练。","不是只有宏大公共行动才算；家庭、邻里、学校、工作场所都是公共品格形成的前政治空间。"],
"practice":["选一个你实际参与的公共场景，不从国家政治开始。","练习同时保有声音与谦逊：说出立场，也说出你可能不知道什么。","寻找一个跨差异、但足够小到能够真正交谈的场合。"],
"sources":["The Company of Strangers","Healing the Heart of Democracy，Five Habits of the Heart"],
"related":["truth-conversation","tragic-gap","undivided-life"]
},
{
"slug":"seasons","cn":"季节隐喻","en":"Seasons","verb":"顺应生命节律",
"summary":"季节不是装饰性比喻，而是一种帮助人理解生命周期的第三物：秋天的种子与放下、冬天的隐藏与休眠、春天的新生、夏天的丰盛与收获。",
"where":"《Let Your Life Speak》第6章以及 Courage to Teach 长期退修结构都使用季节组织内在旅程。",
"misread":["不是把人生机械分成四季。","不是给困境贴标签后就停止行动；它帮助人辨认此刻更适合等待、播种、修剪还是收获。"],
"practice":["问：我现在更像哪一个季节？不要解释太快。","写下这个季节正在邀请我做什么，以及不做什么。","三个月后再看同一个问题，观察季节是否变化。"],
"sources":["Let Your Life Speak，第6章 There Is a Season","The Courage to Teach Guide，seasonal themes"],
"related":["vocation","third-things","wholeness"]
}
]

# ---------- Books ----------
books=[
{
"slug":"let-your-life-speak","title":"Let Your Life Speak","zh":"让生命说话","year":"2000","focus":"使命不是意志工程，而是倾听生命已经在说什么。",
"chapters":[("1","Listening to Life","从外在理想转向聆听生命"),("2","Now I Become Myself","从出生禀赋、经验与限制认识自己"),("3","When Way Closes","从关闭的道路辨识方向"),("4","All the Way Down","低谷与自我认识"),("5","Leading from Within","领导从内在身份出发"),("6","There Is a Season","用季节理解生命节律")],
"ideas":["vocation 来自 listening，而不是 willfulness。","限制与失败不是使命的反面，也可能是最重要的线索。","领导不是向外塑造形象，而是让内在身份进入关系与行动。"],
"practices":["生命线索日志","道路关闭回顾","“应该 / 正在召唤”双栏书写","季节隐喻反思"],
"concepts":["vocation","true-self","seasons"]
},
{
"slug":"hidden-wholeness","title":"A Hidden Wholeness","zh":"内在之光 / 隐藏的完整性","year":"2004","focus":"如何从 divided life 走向 undivided life，并创造能让灵魂出现的共同体。",
"chapters":[("Prelude","Blizzard / Rope","在世界的暴风雪中找到回到灵魂的绳索"),("I","Images of Integrity","完整不是完美；开始“不再分裂”"),("II","Across the Great Divide","重新连接 soul 与 role"),("III","Explorations in True Self","真实自我与灵魂"),("IV","Being Alone Together","独自的内在旅程为什么仍需要共同体"),("V","Creating Circles of Trust","边界、带领、邀请、共同中心、氛围"),("VI","The Truth Told Slant","第三物与隐喻"),("VII","Deep Speaks to Deep","开放而诚实的问题"),("VIII","The Clearness Committee","澄心会"),("IX","Laughter and Silence","沉默、幽默与关系"),("X","The Third Way","日常非暴力与悲剧性张力")],
"ideas":["灵魂需要安全，但安全不等于舒适。","共同体不替人解释自己；结构的任务是保护内在导师。","真理可以通过隐喻、沉默与开放问题间接出现。","内在完整性最终需要进入非暴力行动。"],
"practices":["11 条基石","第三物","三人分享 + honest open questions","澄心会","与沉默对话","悲剧性张力日志"],
"concepts":["undivided-life","trustworthy-community","third-things","honest-open-questions","nonviolence"]
},
{
"slug":"courage-to-teach","title":"The Courage to Teach","zh":"教学勇气","year":"1998","focus":"好教学不能被还原成方法；它从教师的身份、完整性和与主题/学生的关系中生长。",
"chapters":[("1","The Heart of a Teacher","identity & integrity"),("2","A Culture of Fear","教师与学生的恐惧"),("3","The Hidden Wholeness","悖论与 both-and"),("4","Knowing in Community","community of truth"),("5","Teaching in Community","subject-centered classroom"),("6","Learning in Community","共同学习的结构"),("7","Divided No More","从个人完整性到教育改革")],
"ideas":["身份不是履历，而是内外力量交汇的动态中心。","教学中的恐惧会制造控制、疏离与防御。","共同中心不是教师，也不是学生，而是值得共同面对的“主题”。","社会改变从拒绝继续分裂开始。"],
"practices":["教师身份地图","恐惧识别","悖论两端练习","第三物 / 共同中心设计","四阶段社会改变地图"],
"concepts":["identity-integrity","paradox","education-space","undivided-life"]
},
{
"slug":"to-know-as-we-are-known","title":"To Know as We Are Known","zh":"我们怎样认识，就怎样存在","year":"1983","focus":"把认识从占有、控制和对立，转向爱、忠实关系与共同体。",
"chapters":[("1","Knowing Is Loving","现代知识走向何处；为“教育的灵性”奠定基础"),("2","第2章（本站概括）","标准教育如何塑造或扭曲我们的看见与存在；反思客观主义"),("3","第3章（本站概括）","分析传统教学方式及其对学生的影响，并引入沙漠教父母的另一种学习图景"),("4","第4章（本站概括）","从“真理作为人格与共同体关系”重新理解科学、社会科学与人文学科中的认识"),("5","To Teach Is to Create a Space","教师如何创造可学习的空间"),("6","第6章（本站概括）","教师与学生如何在这个空间中练习对真理的忠实"),("7","第7章（本站概括）","教师自身需要怎样的灵性操练，才能重新学习完整地看见")],
"ideas":["认识者与所知之物并非完全分离。","真理不是私人意见，也不是征服对象，而是进入更大关系网络。","课堂本身就是世界的一部分；关系方式会塑造我们走向世界的方式。"],
"practices":["知识关系审计","共同中心课堂设计","沉默与等待","把“关于”改成“与……相遇”"],
"concepts":["knowing-loving","truth-conversation","education-space"]
},
{
"slug":"active-life","title":"The Active Life","zh":"行动的生命","year":"1990","focus":"在沉思与行动之间形成活的悖论，理解行动如何被自我、控制欲、失败与稀缺想象扭曲。",
"chapters":[("1–2","The Paradox in Becoming Fully Alive","行动与沉思的悖论"),("3","The Shadow Side of Action","行动的阴影"),("4","The Nature of Right Action","正确行动与不过度控制结果"),("5","The Lessons of Failure","失败、关系与慈悲"),("6–7","Acting on the Truth","稀缺 / 丰盛与真实行动"),("8","The Horizon of the Active Life","生命朝向什么地平线")],
"ideas":["忙碌不等于行动，反应不等于行动。","过度迷恋结果会遮蔽正在发生的现实。","失败可能打破自足幻觉，让人重新进入关系。","正确行动不在远距离控制中，而在真实关系中发生。"],
"practices":["行动/反应日志","expressive action 实验","结果执着检查","失败反思","六次小组研修"],
"concepts":["active-life","paradox","wholeness","nonviolence"]
},
{
"slug":"company-of-strangers","title":"The Company of Strangers","zh":"陌生人的共同体","year":"1981","focus":"现代公共生活中，人如何在陌生、差异与共同责任之间形成有生命力的公共世界。",
"chapters":[("主题","Strangers","陌生人不是问题本身，而是公共生活的基本条件"),("主题","Public Life","公共生活不同于私人亲密，也不同于国家机器"),("主题","Community","共同体需要容纳非亲密关系与差异")],
"ideas":["公共生活不能只建立在亲密关系上。","与陌生人共处是现代共同体的核心能力。","Palmer 的公共思想早于后来的 Circle of Trust 工作，并与之形成连续性。"],
"practices":["陌生人观察日志","公共空间地图","从私人圈层走向低风险公共交往"],
"concepts":["public-life","truth-conversation","trustworthy-community"]
},
{
"slug":"healing-democracy","title":"Healing the Heart of Democracy","zh":"疗愈民主之心","year":"2011","focus":"把“心灵、张力、差异与公共空间”带入公民生活；重点不在选举策略，而在形成能够承载差异的公民习惯。",
"chapters":[("II","Five Habits of the Heart","互相依存、他者价值、承载张力、个人声音、共同创造能力"),("III","Heartbreak","心如何破碎：碎裂或打开"),("IV","Holding Tension","把个人张力承载能力带入公共领域"),("V","Public Life","与陌生人共同生活的前政治层"),("VI","Institutions","学校、大学、宗教共同体等公民形成场所"),("VII","Safe Spaces","沉默、小型面对面圈子与可承载差异的空间"),("VIII","Heart and History","从心灵理解公共历史")],
"ideas":["公民能力既需要声音，也需要谦逊。","承载张力并不等于不行动；它能减少仓促和去人化。","公共生活发生在日常空间，而不只在正式政治机构。"],
"practices":["五种心灵习惯自评","他者练习","broken-open heart 书写","公共空间观察","声音 + 谦逊对话"],
"concepts":["public-life","tragic-gap","truth-conversation","nonviolence"]
},
{
"slug":"meeting-for-learning","title":"Meeting for Learning","zh":"为学习而相聚","year":"1970s","focus":"把贵格会 meeting 的结构带入教育：学习不是快速获取答案，而是共同等待、求真、让整个人进入学习。",
"chapters":[("核心","Teacher and group","教师有专业性，但不垄断真理"),("核心","Silence","知道什么时候停止追赶，让理解沉淀"),("核心","Whole person","理性、情感、关系、行动都进入学习"),("核心","Vulnerability","学习涉及受伤与被疗愈的可能"),("核心","Patience","真正教育的结果不能完全预先规定")],
"ideas":["沉默本身是一种认识方式。","教师的角色因减少可见控制而变得更细腻，而不是更不重要。","学习的‘影子主题’始终包括我们自己。"],
"practices":["meeting for learning 90 分钟结构","停顿与沉默","整个人签到","学习后果反思"],
"concepts":["education-space","knowing-loving","trustworthy-community"]
},
{
"slug":"going-public","title":"Going Public","zh":"走向公共生活","year":"1980s","focus":"早期 Palmer 如何思考基督徒与美国公共生活的更新，为后来“陌生人、公共空间、完整性”主题提供历史脉络。",
"chapters":[("定位","Public vocation","信念如何进入公共生活而不变成支配"),("关系","Strangers","公共世界由非亲密关系构成"),("更新","Renewal","内在信念与公共责任之间的连接")],
"ideas":["公共生活需要超越私人化信仰。","公共表达不能把他人变成被改造的对象。","这一时期的思考与后来 divided no more / public life 形成连续性。"],
"practices":["私人信念 / 公共理由双栏","公共责任地图","陌生人视角重写"],
"concepts":["public-life","truth-conversation","undivided-life"]
}
]

# ---------- Practices ----------
touchstones=[
"给予欢迎，也接受欢迎。","尽可能完整地临在于当下。","这里的一切都是邀请，不是要求。","说出自己的真实，同时尊重他人的真实。",
"不修理、不拯救、不建议、不纠正。","用开放而诚实的问题回应，而不是用建议接管。","遇到困难时，转向好奇。","留意自己的内在导师。",
"信任并学习于沉默。","严守保密与谨慎的伦理。","相信自己可以从圆圈中带走此刻真正需要的东西。"
]

practices=[
{
"slug":"touchstones","title":"信任圈 11 条基石","en":"Touchstones","duration":"5–10 分钟建立 + 全程回看","size":"2–30 人",
"purpose":"把“尊重”从抽象价值变成可观察、可提醒、可共同维护的关系方式。",
"when":"任何信任圈、深度对话、共读、静修或双人聆听开始前。",
"steps":["把基石提前展示给所有人，不要只由带领者掌握。","逐条读出，不急着解释；让参与者先听见其整体气质。","邀请每个人选一条“今天特别需要提醒自己的”。","过程中如出现抢答、建议、压力或沉默焦虑，回到相应基石，而不是批评个人。","结束时问：哪一条今天真正保护了这个空间？"],
"facilitator":["基石不是管控参与者的规章，而是所有人共同承担的约定。","不要把“保密”理解为对伤害风险的绝对沉默；涉及现实安全时需要另行处理。"],
"debrief":["今天哪条最难？","我在哪一刻想要修理别人？","哪一刻我感到自己有选择权？"],
"source":"A Hidden Wholeness / The Courage to Teach Guide"
},
{
"slug":"silence","title":"静默与等待","en":"Silence","duration":"3–20 分钟","size":"个人 / 群体",
"purpose":"停止立即反应，让理解沉淀，让内在导师有机会出现。",
"when":"开场、一个人分享之后、第三物之后、重大问题之前、结束前。",
"steps":["先命名静默：告诉参与者为什么要安静，以及大约多久。","身体安顿：脚落地、注意呼吸，不要求进入特殊状态。","不追求“脑中空白”；只观察什么反复出现。","时间到后先写 3–5 行，再决定是否分享。","群体中允许有人继续保持沉默，不强制轮流。"],
"facilitator":["Palmer 把沉默视为一种认识方式，而不是空档。","对不习惯静默的人，稳定的时间标记比“无限沉默”更安全。"],
"debrief":["静默里什么变得更清楚？","什么让我想逃离安静？","沉默是隔离我的，还是连接我的？"],
"source":"A Hidden Wholeness Chapter IX / Meeting for Learning"
},
{
"slug":"journaling","title":"自由书写与自我聆听","en":"Journaling","duration":"10–25 分钟","size":"个人 / 群体",
"purpose":"让说话者也成为自己的听者，捕捉那些比头脑解释更早出现的语言。",
"when":"第三物之后、重大问题前、回顾失败或季节时。",
"steps":["设置一个具体但开放的问题。","持续写，不编辑，不追求文采。","若停住，就重复写最后一句，直到新内容出现。","结束后圈出一句最有能量或最陌生的话。","如果分享，只分享自己愿意带入圆圈的部分。"],
"facilitator":["Palmer 常建议参与者把注意力从“记录带领者说了什么”转回“记录自己说了什么”。","自由书写不是心理诊断，不需要给内容下解释。"],
"debrief":["哪句话像是从更深处出来的？","哪句话让我有点不愿承认？","下一步不是“怎么办”，而是“还需要听什么”？"],
"source":"Let Your Life Speak / A Hidden Wholeness guides"
},
{
"slug":"third-things","title":"第三物：诗歌、图像、故事与自然物","en":"Third Things","duration":"20–60 分钟","size":"2–30 人",
"purpose":"通过一个共同对象间接进入复杂经验，减少正面自我暴露和彼此分析。",
"when":"共读、静修、信任圈、团队反思、课程讨论。",
"steps":["选择足够开放、不会只有一个正确答案的第三物。","第一次接触时只描述：我看见/听见了什么。","第二轮问：哪一处抓住了我？","个人书写 5–10 分钟。","分享时使用“它让我想到……”；不解释别人的联想。","带领者最后不要揭晓‘正确寓意’。"],
"facilitator":["第三物应当成为共同中心，而不是带领者用来证明观点的道具。","优先选择能够容纳多重解释、但又有足够质感的作品。"],
"debrief":["我为什么被这一处吸引？","它让我以什么角度重新看自己？","有哪些不同理解可以同时存在？"],
"source":"A Hidden Wholeness Chapter VI"
},
{
"slug":"honest-open-questions","title":"开放而诚实的问题","en":"Honest, Open Questions","duration":"10–30 分钟","size":"2–4 人最佳",
"purpose":"用提问支持当事人自己发现，而不是把提问者的答案塞给他。",
"when":"双人聆听、三人小组、澄心会、团队反思。",
"steps":["听完整段分享，不边听边准备问题。","问一个你真的不知道答案的问题。","问题尽量短；一次只问一个。","避免‘为什么不……’‘你是不是因为……’等暗藏建议或解释的问题。","问完停下来，让沉默工作。","当事人可以不回答任何问题。"],
"facilitator":["先训练提问者识别‘伪问题’；这是最需要练习的环节。","开放问题不是为了追求更多信息，而是帮助焦点人物进入更深的自我聆听。"],
"debrief":["哪个问题让我停了一下？","哪个问题其实让我感到被引导？","我作为提问者最难放下什么？"],
"source":"A Hidden Wholeness Chapters VII–VIII / Courage to Teach Guide"
},
{
"slug":"paired-listening","title":"双人深度聆听","en":"Paired Listening","duration":"30–50 分钟","size":"2 人",
"purpose":"用清晰轮替，让说话者拥有完整、不被打断的时间，并训练听者放下介入冲动。",
"when":"初学者练习、共读、线上会议、信任圈前置训练。",
"steps":["A 说 8–10 分钟，B 只听。","停 30 秒。","B 可复述一两句自己听见的内容，并问 1–2 个开放问题。","交换角色。","最后各自说一句：我从自己说的话里听见了什么。"],
"facilitator":["不把复述变成总结或评判。","线上使用时，明确计时和轮替比自由对话更有保护性。"],
"debrief":["被完整听见是什么感觉？","不回应、不建议为什么困难？","我从自己说的话里听见了什么新东西？"],
"source":"Circle of Trust practice logic"
},
{
"slug":"circle-of-trust","title":"信任圈基础结构","en":"Circle of Trust","duration":"90 分钟–多日","size":"6–20 人常见",
"purpose":"创造一种既保护个人主体性、又允许共同体支持内在旅程的空间。",
"when":"深度共读、静修、专业者更新、长期小组。",
"steps":["欢迎与边界：介绍基石，强调邀请而非要求。","共同中心：用第三物而不是先让每个人讲自己。","个人反思：静默与自由书写。","小组/双人：轮流分享，开放问题，不建议。","大组：自由进入，不按顺序强制发言。","静默收束：每人只带走一句或一个意象。"],
"facilitator":["《A Hidden Wholeness》指出 circle of trust 需要清楚边界、熟练带领、开放邀请、共同中心和有助于灵魂出现的氛围。","Circle of Trust® 是相关机构使用的注册名称；本站提供的是教育性理解，不等同于官方 facilitator 培训。"],
"debrief":["什么结构让我更自由？","哪里仍有隐性压力？","这个圆圈是否让我更依赖带领者，还是更能听见自己？"],
"source":"A Hidden Wholeness Chapters IV–V"
},
{
"slug":"clearness-committee","title":"澄心会","en":"Clearness Committee","duration":"通常约 2 小时核心过程；另需准备","size":"焦点人物 + 3–6 人",
"purpose":"帮助一个人围绕真实问题获得澄明，而不是获得委员会的意见。",
"when":"职业选择、关系抉择、使命辨识、复杂而非紧急的生命问题。",
"steps":["焦点人物提前说明问题和背景，并拥有是否回答问题的权利。","开始时再次确认保密、时间结构和“只问诚实开放问题”。","焦点人物陈述问题；其他人不急于回应。","委员会以开放问题工作，问题之间允许长沉默。","避免建议、解释、诊断、比较自己的故事。","结束时由焦点人物说自己带走什么；委员会不宣布结论。","之后只复盘过程，不在大组讨论焦点人物内容。"],
"facilitator":["原始材料强调在带领前认真学习完整步骤与双重保密规则。","它不适合危机干预、紧急安全问题，也不替代专业心理/医疗/法律支持。"],
"debrief":["哪个问题让我看见新的东西？","哪些沉默比问题更有帮助？","我现在更清楚的是问题本身，还是下一步？"],
"source":"A Hidden Wholeness Chapter VIII / Courage to Teach Guide Appendix C"
},
{
"slug":"seasons","title":"生命季节反思","en":"Seasonal Reflection","duration":"20–45 分钟","size":"个人 / 群体",
"purpose":"用季节作为第三物，帮助人辨认此刻生命更像播种、休眠、新生还是收获。",
"when":"季度退修、年度复盘、职业转折、长期小组。",
"steps":["读一段季节相关短文或观察真实自然环境。","问：我现在更像哪个季节？","写下这个季节正在邀请我做什么。","再写：它邀请我暂时不做什么。","若在小组中分享，不争论‘你其实应该是哪一季’。"],
"facilitator":["季节不是人格诊断，只是暂时性的隐喻。","允许一个人的不同生命领域处在不同季节。"],
"debrief":["我是否一直用夏天的标准要求冬天的自己？","什么正在结束？什么正在萌芽？","什么需要等待而不是催促？"],
"source":"Let Your Life Speak Chapter VI / Courage to Teach seasonal retreats"
},
{
"slug":"way-closes","title":"“路关闭”辨识","en":"When Way Closes","duration":"30–60 分钟","size":"个人 / 双人",
"purpose":"不只从机会和成功辨识使命，也从限制、拒绝和失败中读生命。",
"when":"职业转折、项目失败、关系结束、长期卡住。",
"steps":["列出 3–5 次你曾强烈想走、却被关闭的道路。","每次写：我当时失去了什么？","再写：这条路关闭后，什么反而变得清楚？","寻找重复模式：什么样的门总是关？什么样的门反复开？","只提出下一步实验，不急着定义终身使命。"],
"facilitator":["避免把所有挫折浪漫化成‘命运安排’。","Palmer 的重点是从真实限制中学习，而不是否认痛苦。"],
"debrief":["哪次关闭最改变我？","它让我更清楚自己的什么限制或天赋？","我是否仍在撞一扇已经关闭的门？"],
"source":"Let Your Life Speak Chapter III"
},
{
"slug":"tragic-gap","title":"悲剧性张力地图","en":"Standing in the Tragic Gap","duration":"30–60 分钟","size":"个人 / 小组",
"purpose":"在现实与可能之间保持承载力，不用犬儒或虚假乐观快速逃离。",
"when":"长期组织问题、社会议题、关系僵局、职业倦怠。",
"steps":["左栏写：现实现在是什么。","右栏写：我仍然相信可能成为什么。","中间写：这两端之间的张力如何落在我身体和情绪里。","列出把你拉向犬儒的力量。","列出把你拉向虚假乐观的力量。","写下一个既不否认现实、也不放弃可能的小行动。"],
"facilitator":["承载张力不意味着待在危险环境里。","对重大风险场景，优先现实安全与专业支持。"],
"debrief":["什么让我能够继续站在中间？","我的心是在碎裂，还是被打开？","什么行动既不过度，也不逃避？"],
"source":"A Hidden Wholeness Chapter X / Healing the Heart of Democracy"
},
{
"slug":"action-reaction","title":"行动 / 反应日志","en":"Action vs Reaction","duration":"每天 5 分钟，连续 7 天","size":"个人",
"purpose":"识别自己的行为是从身份与真实行动出发，还是从焦虑地读取外界要求而反应。",
"when":"忙碌、职业压力、决策过多、领导角色。",
"steps":["每天选一件做过的事。","问：如果没人评价我，我还会这样做吗？","问：这件事是在表达我的礼物/价值，还是在保护形象？","记录身体状态：扩展、稳定、收紧、慌乱。","一周后找重复模式。"],
"facilitator":["不是把所有外部要求视为不真实；角色本来就包含责任。","重点是辨认‘我是否只剩反应’。"],
"debrief":["我最常对什么做焦虑反应？","什么行动让我更成为自己？","我可以少做哪一个自动反应？"],
"source":"The Active Life Session 2"
},
{
"slug":"failure","title":"失败作为老师","en":"Lessons of Failure","duration":"45–75 分钟","size":"个人 / 双人",
"purpose":"让失败不只成为自我否定，而成为认识限制、关系与现实的入口。",
"when":"项目失败、职业受挫、带领失误、长期目标未达。",
"steps":["选一次仍有情绪重量的失败。","只描述事实：发生了什么。","写下你最初用什么解释保护自己。","问：这次失败揭露了我对控制、自足或结果的什么幻觉？","问：它是否让我更看见关系、限制或真正需要？","写一个不以‘证明自己’为目的的下一步。"],
"facilitator":["不要要求参与者分享过度私人内容。","失败反思不是强迫积极意义；先允许损失本身存在。"],
"debrief":["我失去的是什么？","我被迫承认的现实是什么？","它是否让我更需要共同体？"],
"source":"The Active Life Session 4"
},
{
"slug":"meeting-for-learning","title":"为学习而相聚","en":"Meeting for Learning","duration":"75–120 分钟","size":"6–20 人",
"purpose":"把学习从“快速收获信息”转成教师、学习者与主题共同面对真理的过程。",
"when":"共读、成人教育、教师研修、专业学习小组。",
"steps":["带来一个值得共同面对的主题，而不是一套要灌输的结论。","每人以整个人签到：不仅知识，也可带来困惑、经验、关系和价值。","教师提供必要专业资源，但不垄断意义。","讨论过程中设置停顿，让理解沉淀。","出现分歧时允许经验互相检验，而不是争夺权威。","结束问：今天学习改变了我什么，而不只是我记住了什么？"],
"facilitator":["教师角色不是消失，而是更细腻：既提供专业资源，也帮助建立可被信任的群体。","Palmer 警惕把情感取代理性；wholeness 不是情绪至上。"],
"debrief":["我是否把学习只当成获取？","今天谁/什么改变了我？","这个主题对我的生活提出了什么要求？"],
"source":"Meeting for Learning / To Know as We Are Known"
}
]

# ---------- Applications ----------
applications=[
("personal","个人生命与使命","把 Palmer 用于职业选择、生命转折、使命辨识与内外一致。",["vocation","true-self","seasons","way-closes","journaling"]),
("education","教育与教学","从技术中心转向教师身份、共同中心、关系与学习空间。",["identity-integrity","education-space","knowing-loving","third-things","meeting-for-learning","paired-listening"]),
("leadership","领导与专业生命","从角色绩效转向由内而外的领导、行动/反应辨识与共同体支持。",["active-life","undivided-life","trustworthy-community","failure","action-reaction"]),
("community","社群与引导","用基石、第三物、静默、开放问题与澄心会保护参与者主体性。",["trustworthy-community","third-things","honest-open-questions","clearness-committee","circle-of-trust","touchstones"]),
("public","公共生活","练习在差异中保有声音、谦逊、张力承载与非暴力，不把公共生活缩成阵营对抗。",["public-life","tragic-gap","truth-conversation","nonviolence","paired-listening"])
]

# ---------- Glossary ----------
glossary=[
("Inner Teacher","内在导师","帮助人从自身经验辨认真实与方向的内在资源。"),
("True Self","真实自我","生命中持续显露的气质、天赋、限制、渴望与边界。"),
("Soul","灵魂 / 内在生命","Palmer 用来描述脆弱却坚韧、需要非侵入性空间的内在核心。"),
("Identity","身份","构成一个人的内外力量在生命中不断交汇的动态中心。"),
("Integrity","完整性","以更真实、更有生命力的方式与构成自己的力量相处。"),
("Vocation","使命 / 召唤","不是目标工程，而是听见生命正在召唤什么。"),
("Divided Life","分裂的生命","内在知道的真相与外在角色长期断裂。"),
("Divided No More","不再分裂","决定不再长期参与自己的缩小与背叛。"),
("Circle of Trust","信任圈","一种保护内在工作、以边界和实践维持可信赖空间的圆圈。"),
("Touchstones","基石","共同维护可信赖空间的关系承诺。"),
("Third Things","第三物","诗歌、图像、故事、自然物等共同中心。"),
("Honest, Open Questions","开放而诚实的问题","提问者不知道答案、也不把建议藏进问号里的问题。"),
("Clearness Committee","澄心会","通过开放问题与沉默帮助焦点人物自己获得澄明的辨识结构。"),
("Community of Truth","真理共同体","教师、学习者与主题在关系中共同面对真理。"),
("Troth","忠实关系","Palmer 借此说明 truth 不只是正确命题，也包含关系中的忠实。"),
("Paradox","悖论","需要 both-and 承载的深层真理。"),
("Tragic Gap","悲剧性张力","现实与可能之间必须承载的距离。"),
("Public Life","公共生活","人与陌生人、制度和共同世界发生关系的日常空间。")
]

concept_lookup={c["slug"]:c for c in concepts}
practice_lookup={p["slug"]:p for p in practices}

def concept_url(slug, prefix=""):
    return f'{prefix}concepts/{slug}.html'

def practice_url(slug, prefix=""):
    return f'{prefix}practice/{slug}.html'

# ---------- home ----------
home_tiles=[
("worldview/","思想总图","先看 Palmer 的整套思想如何从内在真实走向教育、共同体与公共世界。"),
("genealogy/","思想谱系","理解 Pendle Hill、贵格会、Thomas Merton 与教育经验如何塑造他的语言。"),
("concepts/","核心概念","18 个互相关联的概念页，不把思想拆成孤立术语。"),
("books/","原著研读","9 部主要文本的章节地图、关键命题与操练入口。"),
("practice/","操练方法","13 套可直接执行的练习，含时间、人数、步骤、带领提醒与复盘问题。"),
("applications/","应用场景","个人、教育、领导、社群、公共生活五条应用路径。"),
("pathways/","研修路径","12 周综合研修、6 次 Active Life、10 次 Hidden Wholeness、教师路径。"),
("glossary/","术语表","统一中文术语，减少翻译腔和概念混淆。"),
]
home=f'''<main><section class="hero"><div class="shell heroGrid">
<div class="heroMain"><div class="eyebrow">Parker J. Palmer · Thought, Practice & Life</div><h1>从思想研究<br>走向<em>不再分裂地生活</em></h1><p class="lead">这不是人物百科，也不是“金句网站”。它试图完整呈现 Palmer 的思想逻辑：从真实自我、内在导师、使命与完整性，到教育、信任圈、澄心会、沉思与行动、非暴力和公共生活；并把每个概念转成可以亲自操练的结构。</p>
<div class="actions"><a class="btn primary" href="worldview/">先看思想总图</a><a class="btn" href="practice/">直接进入操练</a><a class="btn" href="pathways/">开始系统研修</a></div>
<div class="heroFoot">网站原则：原著先于解释；经验先于结论；操练保护主体性；内在工作最终要回到关系与现实世界。</div></div>
<div class="heroSide"><div class="orb"><div class="r"><span>INNER<br>↔<br>OUTER</span></div></div><div class="sideCard"><span class="tag">核心结构</span><h3>听见 → 认出 → 对齐 → 相遇 → 承载 → 行动</h3><p>Palmer 的不同作品不是分散主题，而是同一条生命逻辑在使命、教育、共同体与公共生活中的展开。</p></div></div>
</div></section>
<section class="section"><div class="shell"><div class="head"><div><div class="kicker">Knowledge Architecture</div><h2>八层知识入口</h2></div><p>你可以从一个问题直接进入，也可以按“思想总图 → 原著 → 操练 → 应用”逐层深入。</p></div>
<div class="grid4">{"".join(tile(u,"进入",t,d,t+" "+d) for u,t,d in home_tiles)}</div></div></section>
<section class="section"><div class="shell"><div class="head"><div><div class="kicker">Three Doors</div><h2>如果今天只走一条路</h2></div><p>根据你当前最真实的问题进入，而不是先读完所有材料。</p></div><div class="grid3">
{tile("concepts/vocation.html","生命方向","使命与召唤","当你在问“下一步到底做什么”，先学习听生命已经说了什么。")}
{tile("concepts/trustworthy-community.html","关系与社群","可信赖的共同体","当你在带领人、做社群或教学，先看结构如何保护人的主体性。")}
{tile("concepts/undivided-life.html","现实行动","不再分裂地生活","当你已经知道哪里内外不一，开始设计一个可以承担后果的小行动。")}
</div></div></section></main>'''
(ROOT/"index.html").write_text(wrap("首页",home,0,"完整呈现帕克·帕尔默思想、原著脉络与具体操练方法"),encoding="utf-8")

# ---------- worldview ----------
movement_html="".join(f'<div class="card"><span class="tag">{n}</span><h3>{t}</h3><p>{d}</p><div class="mini">主要文本：{src}</div></div>' for n,t,d,src in world_movements)
world=f'''<main>{crumbs(1,[("思想总图",None)])}<section class="hero"><div class="shell heroGrid"><div class="heroMain"><div class="eyebrow">Worldview</div><h1>Palmer 的思想<br>可以看成<em>八次转向</em></h1><p class="lead">这些转向把个人内在、教育、共同体、行动与公共世界连成一体。它们不是线性阶段，而是反复往返的生命练习。</p><div class="heroFoot">如果只记住一句：真正的内在工作，会让一个人更能进入关系与世界，而不是更远离它们。</div></div><div class="heroSide"><div class="orb"><div class="r"><span>8<br>MOVES</span></div></div><div class="sideCard"><h3>从“我应该是谁”到“我怎样真实地活在世界里”</h3><p>这条线贯穿 Palmer 四十多年的写作。</p></div></div></div></section>
<section class="section"><div class="shell"><div class="grid2">{movement_html}</div></div></section>
<section class="section"><div class="shell"><div class="head"><div><div class="kicker">System Map</div><h2>五个层次彼此嵌套</h2></div><p>网站后续所有内容，都可以放回这五层里理解。</p></div><div class="grid3">
<div class="card dark"><h3>1. 内在</h3><p>灵魂、内在导师、真实自我、使命、完整性。</p></div>
<div class="card dark"><h3>2. 关系</h3><p>可信赖共同体、第三物、开放问题、沉默、澄心会。</p></div>
<div class="card dark"><h3>3. 认识</h3><p>knowing as loving、community of truth、教学即创造空间。</p></div>
<div class="card dark"><h3>4. 行动</h3><p>沉思与行动、失败、非暴力、悲剧性张力。</p></div>
<div class="card dark"><h3>5. 公共</h3><p>教育改革、专业生命、陌生人、公共空间、公民习惯。</p></div>
</div></div></section></main>'''
(ROOT/"worldview/index.html").write_text(wrap("思想总图",world,1),encoding="utf-8")

# ---------- genealogy ----------
gene=f'''<main>{crumbs(1,[("思想谱系",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Genealogy</div><h1>思想不是凭空出现的<br>它有<em>生命史</em></h1><p class="lead">Palmer 的语言生长在社会学、社区行动、Pendle Hill 的贵格会共同体、Thomas Merton、Henri Nouwen、教育工作和公共参与之间。</p><div class="heroFoot">这一页帮助理解：为什么“inner light、meeting、wholeness、community”在 Palmer 那里不是泛化的灵性词汇。</div></div></div></section>
<section class="section"><div class="shell"><div class="grid2">
<div class="card"><span class="tag">Sociology</span><h3>社会学与公共世界</h3><p>早期社会学训练与社区工作使 Palmer 一开始就关心制度、差异和社会现实，而不是只做私人灵性。</p></div>
<div class="card"><span class="tag">Pendle Hill</span><h3>从二手信念回到亲身经验</h3><p>贵格会的共同生活、工作、学习与静默让他开始追问：哪些只是“听来的”，哪些是自己真实活过、能够从经验中说出的？</p></div>
<div class="card"><span class="tag">Quaker Meeting</span><h3>Meeting 作为求真结构</h3><p>在《Meeting for Learning》中，worship、business 与 learning 共享一种姿态：停止追赶，等待真理在共同体中显现。</p></div>
<div class="card"><span class="tag">Thomas Merton</span><h3>隐藏的完整性</h3><p>Merton 为 Palmer 提供了重要意象：在表面破碎之下仍存在更深的完整与连结。</p></div>
<div class="card"><span class="tag">Henri Nouwen</span><h3>教育、共同体与内在生命</h3><p>Palmer 后来回忆 Nouwen 对自己在 Merton、教育与共同体等主题上具有重要影响。</p></div>
<div class="card"><span class="tag">Education</span><h3>从“教什么”到“谁在教”</h3><p>教师身份、恐惧、完整性、主题中心与共同体逐渐形成他最有影响力的教育思想。</p></div>
<div class="card"><span class="tag">Courage & Renewal</span><h3>把思想变成关系结构</h3><p>信任圈、基石、第三物与澄心会把“尊重灵魂”转成可操作的群体实践。</p></div>
<div class="card"><span class="tag">Public Life</span><h3>内在工作进入公共世界</h3><p>从《The Company of Strangers》到《Healing the Heart of Democracy》，他持续把完整性、陌生人、张力和公共空间连接起来。</p></div>
</div></div></section></main>'''
(ROOT/"genealogy/index.html").write_text(wrap("思想谱系",gene,1),encoding="utf-8")

# ---------- concepts index + pages ----------
concept_tiles="".join(tile(f'{c["slug"]}.html',c["en"],c["cn"],c["summary"],c["cn"]+" "+c["en"]+" "+c["summary"]) for c in concepts)
concept_index=f'''<main>{crumbs(1,[("核心概念",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Concept Library</div><h1>18 个概念<br>不是词典，而是<em>关系网络</em></h1><p class="lead">每个页面都包含：概念位置、原著脉络、常见误读、个人操练与相关概念。搜索一个你当下最在意的问题进入。</p><div class="heroFoot">建议入口：使命 / 完整性 / 信任圈 / 沉思与行动 / 悲剧性张力。</div></div></div></section>
<section class="section"><div class="shell"><div class="searchbar"><input data-site-search placeholder="搜索：使命、灵魂、教育、沉默、张力、公共生活……"></div><div class="grid3">{concept_tiles}</div></div></section></main>'''
(ROOT/"concepts/index.html").write_text(wrap("核心概念",concept_index,1),encoding="utf-8")

concept_rail=lambda cur:'<div class="rail">'+''.join(f'<a class="{"current" if c["slug"]==cur else ""}" href="{c["slug"]}.html">{c["cn"]}</a>' for c in concepts)+'</div>'

for c in concepts:
    related="".join(tile(f'{r}.html',"相关概念",concept_lookup[r]["cn"],concept_lookup[r]["summary"]) for r in c["related"])
    body=f'''<main>{crumbs(1,[("核心概念","index.html"),(c["cn"],None)])}
    <section class="hero"><div class="shell heroGrid"><div class="heroMain"><div class="eyebrow">{c["en"]}</div><h1>{c["verb"]}：<em>{c["cn"]}</em></h1><p class="lead">{c["summary"]}</p><div class="actions"><a class="btn primary" href="#practice">进入操练</a><a class="btn" href="#text">查看原著脉络</a></div><div class="heroFoot">概念页结构：在思想中的位置 → 原著脉络 → 误读校准 → 亲自操练 → 相关概念。</div></div><div class="heroSide"><div class="orb"><div class="r"><span>{c["en"].upper()}</span></div></div><div class="sideCard"><span class="tag">核心问题</span><h3>{c["practice"][0] if c["practice"] else c["summary"]}</h3></div></div></div></section>
    <section class="section"><div class="shell articleLayout"><aside class="toc"><span class="tag">本页导航</span><a href="#meaning">概念位置</a><a href="#text">原著脉络</a><a href="#misread">常见误读</a><a href="#practice">操练</a><a href="#sources">来源</a><a href="#related">相关概念</a></aside><article class="article">
    {concept_rail(c["slug"])}
    <section id="meaning"><span class="kicker">Meaning</span><h2>它在 Palmer 思想中的位置</h2><p>{c["where"]}</p><div class="quote">{c["summary"]}</div></section>
    <section id="text"><span class="kicker">Textual Context</span><h2>原著如何展开它</h2><p>{c["where"]}</p></section>
    <section id="misread"><span class="kicker">Calibration</span><h2>不要把它误读成什么</h2><ul>{''.join(f'<li>{x}</li>' for x in c["misread"])}</ul></section>
    <section id="practice"><div class="practiceBox"><span class="kicker">Practice</span><h3>把概念变成一次经验</h3><div class="steps">{''.join(f'<div class="step"><div>{x}</div></div>' for x in c["practice"])}</div></div></section>
    <section id="sources"><div class="sourceBox"><h3>主要原著脉络</h3><ul>{''.join(f'<li>{x}</li>' for x in c["sources"])}</ul><p><span class="badge">原著梳理</span><span class="badge">本站中文解释</span></p></div></section>
    <section id="related"><span class="kicker">Connections</span><h2>继续沿着关系走</h2><div class="grid3">{related}</div></section>
    </article></div></section></main>'''
    (ROOT/"concepts"/f'{c["slug"]}.html').write_text(wrap(c["cn"],body,1,c["summary"]),encoding="utf-8")

# ---------- books index + pages ----------
book_tiles="".join(tile(f'{b["slug"]}.html',b["year"],f'{b["zh"]} · {b["title"]}',b["focus"],b["title"]+" "+b["zh"]+" "+b["focus"]) for b in books)
book_index=f'''<main>{crumbs(1,[("原著研读",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Primary Texts</div><h1>不是书单<br>而是一张<em>问题地图</em></h1><p class="lead">每本书都进入不同现实领域，但它们共享同一套深层问题：我是谁？我怎样知道？我怎样行动？我们怎样共同生活？</p><div class="heroFoot">每个原著页含：章节地图、关键命题、推荐操练、概念连接。</div></div></div></section><section class="section"><div class="shell"><div class="searchbar"><input data-site-search placeholder="搜索：使命、教育、行动、共同体、公共生活……"></div><div class="grid3">{book_tiles}</div></div></section></main>'''
(ROOT/"books/index.html").write_text(wrap("原著研读",book_index,1),encoding="utf-8")

for b in books:
    rows="".join(f'<tr><td>{n}</td><td><strong>{t}</strong></td><td>{d}</td></tr>' for n,t,d in b["chapters"])
    concept_cards="".join(tile(f'../concepts/{s}.html',"概念",concept_lookup[s]["cn"],concept_lookup[s]["summary"]) for s in b["concepts"])
    prac_cards=[]
    for p in practices:
        if any(k.lower() in (p["title"]+" "+p["en"]).lower() for k in b["practices"]):
            prac_cards.append(tile(f'../practice/{p["slug"]}.html',"操练",p["title"],p["purpose"]))
    suggested="".join(f'<li>{x}</li>' for x in b["practices"])
    body=f'''<main>{crumbs(1,[("原著研读","index.html"),(b["zh"],None)])}<section class="hero"><div class="shell heroGrid"><div class="heroMain"><div class="eyebrow">{b["year"]} · {b["title"]}</div><h1>{b["zh"]}</h1><p class="lead">{b["focus"]}</p><div class="actions"><a class="btn primary" href="#chapters">看章节地图</a><a class="btn" href="#practice">进入操练</a></div><div class="heroFoot">本页以资料库中的原著与带领指南为基础，采用中文解释与结构化梳理，不替代原书。</div></div><div class="heroSide"><div class="sideCard"><span class="tag">阅读时一直带着</span><h3>这本书正在要求我怎样重新看自己、关系或行动？</h3><p>不要只划金句；把概念放回自己的具体生活。</p></div></div></div></section>
    <section class="section"><div class="shell articleLayout"><aside class="toc"><span class="tag">本页导航</span><a href="#chapters">章节地图</a><a href="#ideas">关键命题</a><a href="#practice">操练入口</a><a href="#concepts">相关概念</a></aside><article class="article">
    <section id="chapters"><span class="kicker">Chapter Map</span><h2>章节 / 主题地图</h2><table class="table"><thead><tr><th>章节</th><th>主题</th><th>阅读抓手</th></tr></thead><tbody>{rows}</tbody></table></section>
    <section id="ideas"><span class="kicker">Key Ideas</span><h2>读这本书，抓住这些命题</h2><ul>{''.join(f'<li>{x}</li>' for x in b["ideas"])}</ul></section>
    <section id="practice"><div class="practiceBox"><span class="kicker">Practice</span><h3>适合与本书交替进行的操练</h3><ul>{suggested}</ul><p>阅读建议：每读一章，至少选一个问题做 10–20 分钟书写，再进入讨论。</p></div></section>
    <section id="concepts"><span class="kicker">Concept Links</span><h2>与这些核心概念连起来读</h2><div class="grid3">{concept_cards}</div></section>
    </article></div></section></main>'''
    (ROOT/"books"/f'{b["slug"]}.html').write_text(wrap(b["zh"],body,1,b["focus"]),encoding="utf-8")

# ---------- practice index + pages ----------
prac_tiles="".join(tile(f'{p["slug"]}.html',p["en"],p["title"],p["purpose"],p["title"]+" "+p["purpose"]+" "+p["when"]) for p in practices)
matrix_rows="".join(f'<tr><td><strong>{p["title"]}</strong></td><td>{p["duration"]}</td><td>{p["size"]}</td><td>{p["when"]}</td></tr>' for p in practices)
practice_index=f'''<main>{crumbs(1,[("操练方法",None)])}<section class="hero"><div class="shell heroGrid"><div class="heroMain"><div class="eyebrow">Practice Library</div><h1>不是“懂了”<br>而是<em>做一次</em></h1><p class="lead">Palmer 的实践不是为了操控结果，而是设计条件：减慢反应、减少侵入、形成共同中心、让人能够听见自己，并把内在发现带回真实行动。</p><div class="heroFoot">所有流程都应服从一个原则：结构保护主体性，而不是替参与者决定意义。</div></div><div class="heroSide"><div class="orb"><div class="r"><span>SPACE<br>FOR<br>SOUL</span></div></div><div class="sideCard"><h3>先学边界，再追求深度</h3><p>越是深入的内在工作，越需要明确邀请权、保密、时间结构与“不修理”的纪律。</p></div></div></div></section>
<section class="section"><div class="shell"><div class="head"><div><div class="kicker">Practice Matrix</div><h2>先选合适的练习</h2></div><p>不是所有方法都适合所有场景。先根据人数、时间与问题强度选择。</p></div><table class="table"><thead><tr><th>练习</th><th>时间</th><th>人数</th><th>适用场景</th></tr></thead><tbody>{matrix_rows}</tbody></table></div></section>
<section class="section"><div class="shell"><div class="searchbar"><input data-site-search placeholder="搜索：静默、开放问题、第三物、澄心会、失败、张力……"></div><div class="grid3">{prac_tiles}</div></div></section></main>'''
(ROOT/"practice/index.html").write_text(wrap("操练方法",practice_index,1),encoding="utf-8")

for p in practices:
    extra=""
    if p["slug"]=="touchstones":
        extra=f'''<section id="core"><span class="kicker">The 11 Touchstones</span><h2>11 条基石完整呈现</h2><div class="grid2">{''.join(f'<div class="card"><span class="tag">{i+1:02d}</span><h3>{x}</h3></div>' for i,x in enumerate(touchstones))}</div><div class="caution"><strong>使用方式：</strong>基石不是带领者拿来约束参与者的规章，而是所有人共同维护空间的承诺。每次聚会可全部读出，也可邀请参与者选择一条此刻最需要练习的基石。</div></section>'''
    elif p["slug"]=="circle-of-trust":
        features=["清楚的边界 Clear Boundaries","熟练而克制的带领 Skilled Leadership","开放的邀请 Open Invitation","共同中心 / 共同基础 Common Ground","有助于灵魂出现的氛围 Graceful Ambiance"]
        extra=f'''<section id="core"><span class="kicker">Five Essentials</span><h2>一个信任圈成立的五个条件</h2><div class="grid2">{''.join(f'<div class="card"><h3>{x}</h3></div>' for x in features)}</div><p>这些条件来自《A Hidden Wholeness》第五章相关带领材料。它们说明：信任不是靠“大家友善一点”产生，而要由边界、邀请、共同中心、带领方式与整体氛围共同支持。</p></section>'''
    elif p["slug"]=="clearness-committee":
        extra='''<section id="core"><span class="kicker">Structure</span><h2>澄心会的结构重点</h2><div class="grid2"><div class="card"><h3>焦点人物拥有问题</h3><p>问题属于焦点人物；委员会不接管问题，也不宣布结论。焦点人物可以选择不回答任何问题。</p></div><div class="card"><h3>只以开放而诚实的问题工作</h3><p>问题服务于焦点人物的发现，不服务于委员的好奇，也不把建议包装成问句。</p></div><div class="card"><h3>沉默属于过程</h3><p>问题之间可以有较长停顿；不需要为了“效率”连续追问。</p></div><div class="card"><h3>双重保密</h3><p>不仅内容保密，过程结束后的复盘也只讨论方法本身，不把焦点人物的内容带回大组。</p></div></div><div class="caution"><strong>重要边界：</strong>原始带领材料建议在真正带领澄心会前，先完整学习其步骤、角色与保密原则。它不是危机干预，也不替代心理、医疗、法律等专业支持。</div></section>'''
    elif p["slug"]=="silence":
        extra='''<section id="core"><span class="kicker">Deepening</span><h2>一个“与沉默对话”的书写练习</h2><div class="practiceBox"><p>把“沉默”当作一个可以回应你的对象，连续写 15–20 分钟。例如从“沉默，你最近在哪里？”开始，然后让“沉默”回答，再由自己继续回应。重点不是文学创作，而是观察：我为什么会靠近或躲开安静？</p><p>《A Hidden Wholeness》的带领材料曾用类似形式帮助参与者探索自己与沉默的关系。</p></div></section>'''
    body=f'''<main>{crumbs(1,[("操练方法","index.html"),(p["title"],None)])}<section class="hero"><div class="shell heroGrid"><div class="heroMain"><div class="eyebrow">{p["en"]}</div><h1>{p["title"]}</h1><p class="lead">{p["purpose"]}</p><div class="actions"><a class="btn primary" href="#steps">直接看步骤</a><a class="btn" href="#facilitator">带领提醒</a></div><div class="heroFoot">建议时间：{p["duration"]} · 建议人数：{p["size"]}</div></div><div class="heroSide"><div class="sideCard"><span class="tag">适用场景</span><h3>{p["when"]}</h3><p>来源脉络：{p["source"]}</p></div></div></div></section>
    <section class="section"><div class="shell articleLayout"><aside class="toc"><span class="tag">本页导航</span><a href="#purpose">目的</a><a href="#core">核心结构</a><a href="#steps">步骤</a><a href="#facilitator">带领提醒</a><a href="#debrief">复盘问题</a><a href="#source">来源</a></aside><article class="article">
    <section id="purpose"><span class="kicker">Purpose</span><h2>这项练习在保护什么</h2><p>{p["purpose"]}</p><p><strong>适合：</strong>{p["when"]}</p></section>
    {extra}
    <section id="steps"><span class="kicker">Protocol</span><h2>一步一步做</h2><div class="steps">{''.join(f'<div class="step"><div>{x}</div></div>' for x in p["steps"])}</div></section>
    <section id="facilitator"><span class="kicker">Facilitator Notes</span><h2>带领者要特别注意</h2><div class="caution"><ul>{''.join(f'<li>{x}</li>' for x in p["facilitator"])}</ul></div></section>
    <section id="debrief"><span class="kicker">Debrief</span><h2>结束后不要急着总结</h2><ul>{''.join(f'<li>{x}</li>' for x in p["debrief"])}</ul></section>
    <section id="source"><div class="sourceBox"><h3>原著 / 指南脉络</h3><p>{p["source"]}</p><p><span class="badge">源于资料库</span><span class="badge">中文实践化整理</span></p></div></section>
    </article></div></section></main>'''
    (ROOT/"practice"/f'{p["slug"]}.html').write_text(wrap(p["title"],body,1,p["purpose"]),encoding="utf-8")

# ---------- applications ----------
app_tiles=[]
for slug,title,summary,links in applications:
    app_tiles.append(tile(f'{slug}.html',"应用场景",title,summary,title+" "+summary))
app_index=f'''<main>{crumbs(1,[("应用场景",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Applications</div><h1>思想只有进入现实<br>才开始接受<em>检验</em></h1><p class="lead">Palmer 的“内在工作”不是自我沉浸，而是要进入职业、教学、领导、社群和公共生活。</p><div class="heroFoot">这里按现实场景重新组合概念与操练，而不是重复书本章节。</div></div></div></section><section class="section"><div class="shell"><div class="grid3">{''.join(app_tiles)}</div></div></section></main>'''
(ROOT/"applications/index.html").write_text(wrap("应用场景",app_index,1),encoding="utf-8")

for slug,title,summary,links in applications:
    concept_cards=[]
    practice_cards=[]
    for key in links:
        if key in concept_lookup:
            c=concept_lookup[key]; concept_cards.append(tile(f'../concepts/{key}.html',"核心概念",c["cn"],c["summary"]))
        elif key in practice_lookup:
            p=practice_lookup[key]; practice_cards.append(tile(f'../practice/{key}.html',"操练",p["title"],p["purpose"]))
    if slug=="personal":
        seq=["先用“路关闭”回看过去","再用真实自我 / vocation 读当前线索","用季节隐喻判断节律","设计一个最小现实实验"]
    elif slug=="education":
        seq=["先处理教师自己的身份与恐惧","确定课堂共同中心","减少教师/学生二元中心","用第三物与沉默让主题直接说话","把课堂当作世界关系的练习场"]
    elif slug=="leadership":
        seq=["区分行动与反应","识别角色与真实自我的断裂","建立一个支持共同体","用失败与结果执着做反思","让领导行动从身份而非形象出发"]
    elif slug=="community":
        seq=["先立边界与基石","用第三物建立共同中心","静默 + 书写","双人/三人聆听","需要深度辨识时再进入澄心会"]
    else:
        seq=["从日常公共空间而非宏大立场开始","同时练习声音与谦逊","把他者当作能教会我东西的人","承载张力，不急于把差异变成敌意","选择非暴力、可持续的小行动"]
    practice_section=""
    if practice_cards:
        practice_section=f'''<section class="section"><div class="shell"><div class="head"><div><div class="kicker">Practices</div><h2>推荐操练</h2></div><p>这些练习让概念进入具体经验；请先阅读各自的边界与带领提醒。</p></div><div class="grid3">{''.join(practice_cards)}</div></div></section>'''
    body=f'''<main>{crumbs(1,[("应用场景","index.html"),(title,None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Application</div><h1>{title}</h1><p class="lead">{summary}</p><div class="heroFoot">应用不是把 Palmer 变成工具箱，而是保留其核心伦理：主体性、关系、边界、内外一致与现实承担。</div></div></div></section><section class="section"><div class="shell"><div class="head"><div><div class="kicker">Sequence</div><h2>建议顺序</h2></div><p>先处理条件，再处理内容；先减少侵入，再追求深度。</p></div><div class="steps">{''.join(f'<div class="step"><div>{x}</div></div>' for x in seq)}</div></div></section><section class="section"><div class="shell"><div class="head"><div><div class="kicker">Concepts</div><h2>相关概念</h2></div><p>这些概念构成本场景的思想骨架。</p></div><div class="grid3">{''.join(concept_cards)}</div></div></section>{practice_section}</main>'''
    (ROOT/"applications"/f'{slug}.html').write_text(wrap(title,body,1,summary),encoding="utf-8")

# ---------- pathways ----------
weeks=[
("01","倾听生命","Let Your Life Speak：从“应该”转向生命已经在说什么","practice/journaling.html"),
("02","真实自我","天赋、限制、失败与身体线索","concepts/true-self.html"),
("03","身份与完整性","The Courage to Teach：角色与内在真实","concepts/identity-integrity.html"),
("04","恐惧与分裂","看见 divided life 的具体场景","concepts/divided-life.html"),
("05","隐藏的完整性","A Hidden Wholeness：soul / inner teacher","concepts/wholeness.html"),
("06","信任圈","基石、邀请、边界与共同中心","practice/circle-of-trust.html"),
("07","第三物","隐喻、诗歌、故事与间接表达","practice/third-things.html"),
("08","开放问题与澄心","从建议转向辨识","practice/clearness-committee.html"),
("09","认识与真理","To Know as We Are Known：从占有到关系","concepts/knowing-loving.html"),
("10","沉思与行动","The Active Life：行动、反应与失败","concepts/active-life.html"),
("11","悲剧性张力","现实与可能之间的承载","practice/tragic-gap.html"),
("12","带回世界","做一次不再分裂、但可承担后果的行动","concepts/undivided-life.html"),
]
whtml="".join(f'<a class="card tile" href="../{u}"><span class="tag">WEEK {n}</span><h3>{t}</h3><p>{d}</p><span class="arrow">→</span></a>' for n,t,d,u in weeks)
active_sessions=[
("1","The Paradox in Becoming Fully Alive","行动与沉思的悖论"),
("2","The Shadow Side of Action","行动的阴影、焦虑反应与操控"),
("3","The Nature of Right Action","正确行动、关系与不过度控制结果"),
("4","The Lessons of Failure","失败如何打破自足幻觉并打开关系"),
("5","Acting on the Truth","稀缺 / 丰盛、诱惑与真实行动"),
("6","The Horizon of the Active Life","生命朝向什么地平线")
]
ashtml="".join(f'<div class="card"><span class="tag">SESSION {n}</span><h3>{t}</h3><p>{d}</p></div>' for n,t,d in active_sessions)
hh_sessions=[
("1","Blizzard & Rope","在世界暴风雪中寻找回到灵魂的绳索"),("2","Images of Integrity","哪里完整，哪里分裂"),("3","True Self","真实自我的出生禀赋与线索"),
("4","Being Alone Together","为何内在旅程仍需要共同体"),("5","Creating Circles of Trust","边界、邀请、共同中心与氛围"),("6","Third Things","隐喻与斜着说出真理"),
("7","Honest, Open Questions","听彼此进入更深的话语"),("8","Clearness Committee","结构化辨识"),("9","Silence & Laughter","沉默、幽默与关系"),("10","The Third Way","非暴力与悲剧性张力")
]
hhhtml="".join(f'<div class="card"><span class="tag">{n}</span><h3>{t}</h3><p>{d}</p></div>' for n,t,d in hh_sessions)
paths=f'''<main>{crumbs(1,[("研修路径",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Learning Pathways</div><h1>不要“刷完内容”<br>让阅读、静默与行动<em>交替发生</em></h1><p class="lead">下面提供三条可以实际执行的路径：12 周综合研修、6 次《The Active Life》小组、10 次《A Hidden Wholeness》共读。</p><div class="heroFoot">建议每次都保留：第三物 / 静默 / 书写 / 分享 / 开放问题 / 结束带走。</div></div></div></section>
<section class="section"><div class="shell"><div class="head"><div><div class="kicker">12 Weeks</div><h2>综合研修</h2></div><p>每周：原著 30–60 分钟 → 书写 10–20 分钟 → 一项微实践 → 伙伴或小组分享。</p></div><div class="grid3">{whtml}</div></div></section>
<section class="section"><div class="shell"><div class="head"><div><div class="kicker">6 Sessions</div><h2>《The Active Life》小组</h2></div><p>依据 Leader's Guide 的六次结构，适合成人学习小组。</p></div><div class="grid3">{ashtml}</div></div></section>
<section class="section"><div class="shell"><div class="head"><div><div class="kicker">10 Sessions</div><h2>《A Hidden Wholeness》共读</h2></div><p>不是按章节讲解，而是让每一章对应一次内在与群体实践。</p></div><div class="grid2">{hhhtml}</div></div></section></main>'''
(ROOT/"pathways/index.html").write_text(wrap("研修路径",paths,1),encoding="utf-8")

# ---------- glossary ----------
grows="".join(f'<tr><td><strong>{en}</strong></td><td>{zh}</td><td>{d}</td></tr>' for en,zh,d in glossary)
gloss=f'''<main>{crumbs(1,[("术语表",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Glossary</div><h1>术语不是标签<br>先理解它在 Palmer 语境中的<em>功能</em></h1><p class="lead">统一中文译法，减少把英文灵性术语直译后造成的误解。</p><div class="heroFoot">本站优先采用“内在导师、真实自我、完整性、基石、澄心会、第三物、悲剧性张力”等译法。</div></div></div></section><section class="section"><div class="shell"><table class="table"><thead><tr><th>英文</th><th>本站译法</th><th>语境说明</th></tr></thead><tbody>{grows}</tbody></table></div></section></main>'''
(ROOT/"glossary/index.html").write_text(wrap("术语表",gloss,1),encoding="utf-8")

# ---------- sources ----------
sources=f'''<main>{crumbs(1,[("资料说明",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Sources & Method</div><h1>完整，不等于混在一起<br>先建立<em>证据层级</em></h1><p class="lead">本站优先使用 Palmer 原著与正式带领指南，再用学术研究、纪念文集和历史材料补充思想脉络。网站中的“操练化整理”会明确作为本站整理，而不冒充 Palmer 原文。</p><div class="heroFoot">资料不足的地方应标记“尚待核对”，而不是用一般灵性知识补齐。</div></div></div></section>
<section class="section"><div class="shell"><div class="grid3">
<div class="card"><span class="tag">第一层</span><h3>Palmer 原著</h3><p>A Hidden Wholeness、Let Your Life Speak、The Courage to Teach、To Know as We Are Known、The Active Life、The Company of Strangers、Healing the Heart of Democracy、Going Public、Meeting for Learning。</p></div>
<div class="card"><span class="tag">第二层</span><h3>带领与讨论指南</h3><p>The Courage to Teach Guide、The Active Life Leader's Guide、A Hidden Wholeness 的小组带领材料等，主要用于流程与操练结构。</p></div>
<div class="card"><span class="tag">第三层</span><h3>研究与脉络</h3><p>Elena Soto 的系统研究、Living the Questions、Leading from Within，以及 Howard Thurman 等相关思想材料。</p></div>
</div><div class="sourceBox"><h3>本站写作与实践化原则</h3><ol>
<li>先确认原著在说什么，再做中文解释。</li><li>把术语放回上下文，不做“金句化”。</li><li>区分 Palmer 本人的主张、Courage & Renewal 后续实践、本站再设计。</li>
<li>所有操练优先保护参与者主体性：邀请而非要求，不替人决定，不把建议藏进问题。</li><li>涉及澄心会等深入方法时，明确准备要求与边界。</li>
</ol></div></div></section></main>'''
(ROOT/"sources/index.html").write_text(wrap("资料说明",sources,1),encoding="utf-8")

# ---------- search index ----------
index=[]
for c in concepts:index.append({"title":c["cn"],"url":f'concepts/{c["slug"]}.html',"type":"概念","summary":c["summary"]})
for b in books:index.append({"title":b["zh"],"url":f'books/{b["slug"]}.html',"type":"原著","summary":b["focus"]})
for p in practices:index.append({"title":p["title"],"url":f'practice/{p["slug"]}.html',"type":"操练","summary":p["purpose"]})
for slug,title,summary,_ in applications:index.append({"title":title,"url":f'applications/{slug}.html',"type":"应用","summary":summary})
(ROOT/"assets/search-index.json").write_text(json.dumps(index,ensure_ascii=False,indent=2),encoding="utf-8")

print("generated", len(list(ROOT.rglob("*.html"))), "html pages")
