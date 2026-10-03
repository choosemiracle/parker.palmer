from pathlib import Path
import html
import json
import shutil

ROOT = Path(__file__).resolve().parent
GENERATED_DIRS = [
    "assets", "worldview", "genealogy", "concepts", "books", "practice",
    "applications", "pathways", "glossary", "sources", "self-study", "parker-palmer"
]
for name in GENERATED_DIRS:
    p = ROOT / name
    if p.exists():
        shutil.rmtree(p)
    p.mkdir(parents=True, exist_ok=True)

# Copy curated static media after generated directories are reset.
if (ROOT / "static").exists():
    shutil.copytree(ROOT / "static", ROOT / "assets", dirs_exist_ok=True)

KNOWLEDGE = json.loads((ROOT / "data/knowledge.json").read_text(encoding="utf-8"))
PALMER = json.loads((ROOT / "data/parker-palmer.json").read_text(encoding="utf-8"))
CIRCLE_SITE = KNOWLEDGE["special_sites"]["circle_of_trust"]["url"]

CSS = r"""
:root{
  --paper:#f4efe5;
  --paper-2:#ede4d5;
  --ink:#1f2a25;
  --muted:#59645d;
  --line:#cfc4b3;
  --accent:#8a4f2d;
  --accent-soft:#dcc4ab;
  --deep:#28362f;
  --white:#fffdf8;
  --red:#86514a;
  --shadow:0 18px 45px rgba(48,41,33,.08);
  --r:22px;
  --max:1180px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0;
  background:var(--paper);
  color:var(--ink);
  font-family:"Noto Serif SC","Songti SC","STSong","Source Han Serif SC",serif;
  line-height:1.78;
  letter-spacing:.01em;
  overflow-x:hidden;
}
button,a,input,textarea{font:inherit}
a{color:inherit}
.shell{width:min(var(--max),calc(100% - 48px));margin:auto}
.top{
  position:sticky;top:0;z-index:50;
  border-bottom:1px solid rgba(125,111,94,.22);
  background:rgba(244,239,229,.88);
  backdrop-filter:blur(16px);
}
.topin{min-height:64px;display:flex;align-items:center;justify-content:space-between;gap:22px}
.brand{display:flex;align-items:center;gap:11px;text-decoration:none;color:var(--ink);font-weight:400}
.mark{width:36px;height:36px;border:1px solid var(--accent);border-radius:50%;display:grid;place-items:center;color:var(--accent);font-size:22px;line-height:1}
.brandText strong{display:block;font-size:15px;letter-spacing:.08em;font-weight:700}
.brandText small{display:block;color:var(--muted);font-size:11px;letter-spacing:.12em;margin-top:1px}
nav{display:flex;gap:22px;align-items:center}
nav a{font-family:ui-sans-serif,system-ui,sans-serif;text-decoration:none;color:#4d574f;font-size:13px;position:relative}
nav a:after{content:"";position:absolute;left:0;right:100%;bottom:-5px;height:1px;background:var(--accent);transition:.25s}
nav a:hover:after,nav a:focus-visible:after{right:0}
.crumbs{padding:20px 0 0;color:#7a756e;font-family:ui-sans-serif,system-ui,sans-serif;font-size:12px}
.crumbs a{text-decoration:none}

h1,h2,h3{overflow-wrap:normal;word-break:normal;line-break:strict;hyphens:none}
@supports (word-break:auto-phrase){h1,h2,h3{word-break:auto-phrase}}
h1{font-size:clamp(40px,5.4vw,68px);line-height:1.24;letter-spacing:-.03em;margin:18px 0 24px;font-weight:650}
h1 em{font-style:normal;color:var(--accent)}
h2{font-weight:650}
h3{font-weight:650}
.semanticTitle{display:block;max-width:100%;text-wrap:pretty}
.semanticTitle .titleLine{display:block;width:max-content;max-width:100%;white-space:nowrap}
.semanticTitle .titleLine+.titleLine{margin-top:.03em}
.semanticTitleFit{transition:none}
.eyebrow,.kicker,.tag{
  font-family:ui-sans-serif,system-ui,sans-serif;
  color:var(--accent);
  letter-spacing:.16em;
  text-transform:uppercase;
  font-size:11px;
  font-weight:650;
}

/* Header / page heroes: continue the warm, restrained visual language of the Quaker site */
.hero{
  padding:0;
  position:relative;
  overflow:hidden;
  border-bottom:1px solid var(--line);
  background:
    radial-gradient(circle at 80% 38%,rgba(191,141,91,.15),transparent 24%),
    linear-gradient(135deg,#f7f2e9 0%,#efe5d6 100%);
}
.hero:before{
  content:"";position:absolute;inset:0;
  background-image:linear-gradient(rgba(72,66,58,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(72,66,58,.025) 1px,transparent 1px);
  background-size:34px 34px;
  mask-image:linear-gradient(to right,black,transparent 82%);
}
.hero>.shell{position:relative;z-index:1}
.heroGrid{display:grid;grid-template-columns:1.18fr .82fr;gap:34px;align-items:stretch}
.heroGrid>*,.portraitHero>*,.storyGrid>*,.chapterGrid>*,.studyDock>*,.labGrid>*{min-width:0}
.heroMain,.heroSide{box-shadow:none}
.heroMain{min-height:510px;padding:82px 0 78px;background:transparent;color:var(--ink);position:relative}
.heroMain.compact{min-height:390px;padding-top:72px;padding-bottom:72px}
.hero .eyebrow{color:var(--accent)}
.lead{font-size:19px;line-height:1.85;color:#505a52;max-width:760px}
.actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
.btn,.toolButton{
  display:inline-flex;align-items:center;justify-content:center;
  min-height:44px;padding:0 18px;border-radius:999px;text-decoration:none;
  border:1px solid #8d968f;background:rgba(255,255,255,.38);color:var(--ink);
  font-family:ui-sans-serif,system-ui,sans-serif;font-size:13px;font-weight:650;cursor:pointer;
  transition:transform .2s,box-shadow .2s,background .2s;
}
.btn:hover,.toolButton:hover{transform:translateY(-1px)}
.btn.primary,.toolButton.primary{background:var(--deep);color:#fff;border-color:var(--deep);box-shadow:0 10px 24px rgba(40,54,47,.14)}
.btn.light{background:var(--white);color:var(--deep);border-color:var(--white)}
.heroFoot{position:absolute;left:0;right:0;bottom:28px;padding-top:15px;border-top:1px solid var(--line);font-family:ui-sans-serif,system-ui,sans-serif;font-size:12px;color:#7a756e}
.heroSide{padding:66px 0 58px;display:flex;flex-direction:column;justify-content:center;gap:28px}
.orb{height:270px;display:grid;place-items:center}
.orb .r{width:215px;height:215px;border:1px solid rgba(138,79,45,.28);border-radius:50%;display:grid;place-items:center;box-shadow:0 0 0 38px rgba(138,79,45,.05),0 0 0 76px rgba(138,79,45,.025)}
.orb .r span{width:74px;height:74px;border-radius:50%;background:radial-gradient(circle,#e9bb68 0%,rgba(233,187,104,.65) 35%,rgba(233,187,104,.08) 70%,transparent 74%);box-shadow:0 0 36px rgba(233,187,104,.35);display:grid;place-items:center;text-align:center;font-family:ui-sans-serif,system-ui,sans-serif;font-size:10px;font-weight:700;color:var(--deep)}
.sideCard{background:rgba(255,253,248,.58);border:1px solid var(--line);border-radius:18px;padding:22px}
.sideCard h3{margin:8px 0 8px;font-size:22px;line-height:1.42}
.sideCard p{margin:0;color:var(--muted);font-size:15px}

.section{padding:96px 0}
.head{display:grid;grid-template-columns:1.1fr .9fr;gap:70px;align-items:end;margin-bottom:46px}
.head h2{font-size:clamp(29px,3.2vw,44px);line-height:1.4;letter-spacing:-.018em;margin:8px 0 0;max-width:100%;text-wrap:balance}
.head p{margin:0;color:var(--muted);font-size:17px;line-height:1.85}
.head.wideHead{grid-template-columns:minmax(0,1fr);gap:18px;align-items:start}
.head.wideHead h2{font-size:clamp(34px,4.4vw,56px);line-height:1.34;max-width:none}
.head.wideHead p{max-width:860px}
.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.card{background:rgba(255,253,248,.58);border:1px solid var(--line);border-radius:18px;padding:24px}
.card h3{font-size:23px;line-height:1.42;margin:12px 0 9px}
.card p{margin:0;color:var(--muted);font-size:16px;line-height:1.78}
.mini{margin-top:15px;padding-top:13px;border-top:1px solid var(--line);font-size:13px;color:#77746e}
.tile{display:block;text-decoration:none;min-height:228px;position:relative;overflow:hidden;transition:.2s}
.tile:hover{transform:translateY(-2px);box-shadow:var(--shadow);background:var(--white)}
.tile .arrow{position:absolute;right:18px;bottom:15px;color:var(--accent);font-size:20px}
.tile small{display:block;color:#888;margin-top:12px}
.tileVisual{height:138px;margin:12px 0 16px;display:grid;place-items:center;overflow:hidden;border-radius:14px;background:rgba(238,229,215,.48);border:1px solid rgba(207,196,179,.7)}
.tileVisual>svg,.tileVisual .miniDiagram{width:100%;height:100%;max-height:138px}.tileVisual .mobiusWrap{width:100%;transform:scale(.72)}.tileVisual .mobiusWrap svg{max-height:160px}
.dark{background:var(--deep);color:#fff;border-color:var(--deep)}
.dark p,.dark li{color:#d9dfdb}.dark .mini{border-color:rgba(255,255,255,.14);color:#c8cfca}.dark .tag{color:#e4b379}
.quote{border-left:3px solid var(--accent);padding:6px 0 6px 18px;font-size:20px;line-height:1.72;color:#354139}
.question{background:#efe6d8;color:var(--ink)}.question p{color:var(--ink);font-size:18px;font-weight:650}

.articleLayout{display:grid;grid-template-columns:210px minmax(0,1fr);gap:68px;align-items:start}
.toc{position:sticky;top:96px;align-self:start;padding:18px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.toc .tag{display:block;margin-bottom:6px}
.toc a{display:block;padding:6px 0;text-decoration:none;color:var(--muted);font-family:ui-sans-serif,system-ui,sans-serif;font-size:13px;border:0}
.toc a:hover{color:var(--ink)}
.article{max-width:850px;min-width:0}
.article h2{font-size:clamp(28px,2.4vw,40px);line-height:1.4;margin:10px 0 20px;letter-spacing:-.02em}
.article h3{font-size:23px;line-height:1.4;margin:28px 0 8px}
.article p,.article li{color:#4e5851;font-size:17px}
.article ul,.article ol{padding-left:22px}
.article section{scroll-margin-top:100px;margin-bottom:72px}
.practiceBox{background:#efe6d8;border:1px solid var(--line);border-radius:18px;padding:24px;margin:22px 0}
.practiceBox h3{margin-top:0}
.caution{background:#efe3df;border-left:3px solid var(--red);padding:18px 20px;border-radius:0 14px 14px 0;margin:18px 0}
.sourceBox{background:rgba(255,253,248,.62);border:1px solid var(--line);border-radius:18px;padding:22px;margin-top:26px}
.sourceBox li{margin:7px 0}
.rail{display:flex;gap:8px;flex-wrap:wrap;margin:20px 0}
.rail a,.rail label{padding:7px 11px;border:1px solid var(--line);border-radius:999px;text-decoration:none;font-family:ui-sans-serif,system-ui,sans-serif;font-size:12px;background:rgba(255,255,255,.38);color:var(--muted)}
.rail a.current{background:var(--deep);color:white;border-color:var(--deep)}
.table{width:100%;border-collapse:collapse;background:rgba(255,253,248,.55);border:1px solid var(--line)}
.table th,.table td{text-align:left;padding:13px;border-bottom:1px solid var(--line);vertical-align:top}
.table th{font-family:ui-sans-serif,system-ui,sans-serif;font-size:12px;color:var(--muted);background:#ece3d6}
.steps{counter-reset:step;display:grid;gap:10px}
.step{display:grid;grid-template-columns:48px 1fr;gap:14px;align-items:start;background:rgba(255,253,248,.58);border:1px solid var(--line);border-radius:16px;padding:16px}
.step:before{counter-increment:step;content:counter(step);width:38px;height:38px;border-radius:50%;background:var(--deep);color:white;display:grid;place-items:center;font-family:ui-sans-serif,system-ui,sans-serif;font-weight:700}
.matrix{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}.matrix .card{min-height:170px}
.searchbar{display:flex;gap:10px;margin:18px 0 24px}
.searchbar input{width:100%;border:1px solid var(--line);border-radius:16px;padding:14px 16px;background:var(--white);color:var(--ink);outline:none}
.searchbar input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(138,79,45,.09)}
.badge{display:inline-block;border-radius:999px;background:#ece3d6;padding:5px 9px;font-family:ui-sans-serif,system-ui,sans-serif;font-size:11px;color:#665f56;margin-right:5px;text-decoration:none}

.footer{margin-top:34px;border-top:1px solid var(--line);background:transparent;color:var(--muted);padding:34px 0 50px}
.footer strong{color:var(--ink);font-size:14px}.footer p{max-width:850px;font-size:13px;margin:6px 0 0}
.reveal{opacity:0;transform:translateY(10px);transition:.45s}.reveal.visible{opacity:1;transform:none}

/* Homepage: same visual family as choosemiracle.github.io/quaker */
.experienceHero{
  position:relative;overflow:hidden;border-bottom:1px solid var(--line);
  background:radial-gradient(circle at 73% 42%,rgba(191,141,91,.16),transparent 25%),linear-gradient(135deg,#f7f2e9 0%,#f1e9dc 60%,#e9dfd0 100%);
  padding:0 0 72px;
}
.experienceHero:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(72,66,58,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(72,66,58,.03) 1px,transparent 1px);background-size:34px 34px;mask-image:linear-gradient(to right,black,transparent 78%)}
.experienceHero>.shell{position:relative;z-index:1}
.experienceHero .stage{min-height:76vh;display:flex;flex-direction:column;justify-content:center;position:relative;padding:100px 0 105px;background:transparent;color:var(--ink);overflow:hidden}
.experienceHero .stage:after{content:"";position:absolute;width:min(32vw,380px);height:min(32vw,380px);border:1px solid rgba(138,79,45,.25);border-radius:50%;right:2%;top:50%;transform:translateY(-48%);box-shadow:0 0 0 52px rgba(138,79,45,.055),0 0 0 104px rgba(138,79,45,.026)}
.experienceHero .stage:before{content:"";position:absolute;width:54px;height:54px;border-radius:50%;right:calc(2% + min(16vw,190px) - 27px);top:calc(50% - 27px);background:radial-gradient(circle,#e9bb68 0%,rgba(233,187,104,.72) 30%,rgba(233,187,104,.05) 68%,transparent 72%);box-shadow:0 0 36px rgba(233,187,104,.46);z-index:1}
.experienceHero h1{max-width:900px;font-size:clamp(42px,5.8vw,72px);line-height:1.23;letter-spacing:-.035em;position:relative;z-index:2;margin:18px 0 24px}
.experienceHero h1 em{color:var(--accent)}
.experienceHero .lead{font-size:19px;max-width:720px;color:#505a52;position:relative;z-index:2}
.experienceHero .actions{position:relative;z-index:2}
.journeyStrip{position:relative;z-index:3}
.journeyGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.journeyCard{display:block;text-decoration:none;background:rgba(255,253,248,.55);border:1px solid var(--line);padding:26px;border-radius:var(--r);min-height:240px;transition:.2s}
.journeyCard:hover{transform:translateY(-2px);box-shadow:var(--shadow);background:var(--white)}
.journeyCard .num{font-family:ui-monospace,monospace;color:var(--accent);font-size:11px;letter-spacing:.1em}
.journeyCard h3{font-size:25px;line-height:1.42;margin:42px 0 10px}
.journeyCard p{color:var(--muted);margin:0;font-size:16px}

.questionBand{background:var(--deep);color:white;border-radius:28px;padding:48px;position:relative;overflow:hidden}
.questionBand:after{content:"";position:absolute;width:330px;height:330px;border:1px solid rgba(255,255,255,.08);border-radius:50%;right:-60px;top:-100px;box-shadow:0 0 0 62px rgba(255,255,255,.025),0 0 0 124px rgba(255,255,255,.015)}
.questionBand>*{position:relative;z-index:1}
.questionBand .kicker,.questionBand .tag{color:#e4b379}
.questionBand h2{color:white;margin:0 0 12px;font-size:clamp(30px,4vw,48px);line-height:1.35}
.questionBand p{color:#d7ddd8;font-size:17px}
.questionBand .btn.primary{background:#f3eadb;color:var(--deep);border-color:#f3eadb;box-shadow:none}
.questionBand .card{background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.18);color:white}
.questionBand .card p{color:#d7ddd8}.questionBand .card .tag{color:#e4b379}
.pathwayFlow{display:grid;grid-template-columns:repeat(6,1fr);gap:9px;align-items:stretch}
.flowNode{padding:18px 14px;border-top:1px solid var(--accent);background:rgba(255,253,248,.55);min-height:125px}
.flowNode b{display:block;margin-bottom:6px;font-size:17px}.flowNode small{color:var(--muted)}
.studyDock{background:rgba(255,253,248,.55);border:1px solid var(--line);border-radius:22px;padding:30px;display:grid;grid-template-columns:1.2fr .8fr;gap:24px;align-items:center}
.studyDock h2{font-size:clamp(30px,3.2vw,42px);line-height:1.4;margin:5px 0 12px}
.studyDock p{color:var(--muted)}
.studyStat{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
.studyStat div{background:#ece3d6;padding:18px;border-radius:16px;border:1px solid var(--line)}
.studyStat strong{font-family:ui-monospace,monospace;color:var(--accent);font-size:28px;display:block}

/* Self-study components */
.practiceLab{background:#eee5d7;border:1px solid var(--line);border-radius:22px;padding:24px;margin:28px 0}
.practiceLab h3{margin:4px 0 8px;font-size:24px}.practicePrompt{font-size:18px;line-height:1.75;margin:6px 0 18px;color:#4e5851}
.labGrid{display:grid;grid-template-columns:.72fr 1.28fr;gap:14px}
.timerBox,.journalBox{background:var(--white);border-radius:18px;padding:20px;border:1px solid var(--line)}
.timerDisplay{font-family:ui-monospace,monospace;font-variant-numeric:tabular-nums;font-size:46px;font-weight:700;letter-spacing:-.04em;margin:10px 0;color:var(--deep)}
.timerPresets{display:flex;gap:7px;flex-wrap:wrap}
.timerPresets button{border:1px solid var(--line);background:var(--paper);color:var(--ink);border-radius:999px;padding:8px 12px;font-family:ui-sans-serif,system-ui,sans-serif;font-size:12px;cursor:pointer}
.journalBox textarea,.questionTool textarea,.questionTool input{width:100%;min-height:180px;border:1px solid var(--line);border-radius:14px;padding:14px;background:#fffdfa;color:var(--ink);resize:vertical;outline:none}
.journalBox textarea:focus,.questionTool textarea:focus,.questionTool input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(138,79,45,.08)}
.questionTool input{min-height:auto}
.saveState{font-family:ui-sans-serif,system-ui,sans-serif;font-size:12px;color:#77746e;margin-top:7px}
.smallNote{font-size:12px;color:#77746e}
.relationMap{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.relationCol{background:rgba(255,253,248,.56);border:1px solid var(--line);padding:19px;border-radius:16px}
.relationCol h4{margin:0 0 10px;font-size:18px}.relationCol a{display:block;text-decoration:none;padding:7px 0;border-bottom:1px solid var(--line);font-size:14px;color:#526059}
.networkGrid{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}
.cluster{padding:20px;border:1px solid var(--line);border-radius:18px;min-height:310px;background:rgba(255,253,248,.56)}
.cluster:nth-child(even){background:#eee5d7}.cluster h3{margin:9px 0 18px;font-size:24px}.cluster a{display:block;text-decoration:none;padding:8px 0;border-bottom:1px solid var(--line);font-size:14px;color:#526059}
.courseHero{background:var(--deep);color:white;border-radius:28px;padding:54px;position:relative;overflow:hidden}
.courseHero:after{content:"";position:absolute;width:430px;height:430px;border:1px solid rgba(255,255,255,.09);border-radius:50%;right:-110px;top:-130px;box-shadow:0 0 0 75px rgba(255,255,255,.024),0 0 0 150px rgba(255,255,255,.012)}
.courseHero>*{position:relative;z-index:1}.courseHero .eyebrow{color:#e4b379}
.courseHero h1{font-size:clamp(40px,5vw,64px);line-height:1.3;margin:8px 0 18px}.courseHero h1 em{color:#f3eadb}
.courseHero p{color:#d7ddd8;max-width:800px;font-size:18px}
.courseHero .btn{color:#fff;border-color:rgba(255,255,255,.4);background:transparent}.courseHero .btn.primary{background:#f3eadb;color:var(--deep);border-color:#f3eadb;box-shadow:none}
.progressTrack{height:8px;border-radius:999px;background:#ded4c5;overflow:hidden}.progressFill{height:100%;width:0;background:var(--accent);transition:.3s}
.moduleList{display:grid;gap:10px}.moduleCard{display:grid;grid-template-columns:70px 1fr auto;gap:18px;align-items:center;padding:20px;border:1px solid var(--line);border-radius:18px;background:rgba(255,253,248,.6);text-decoration:none;transition:.2s}
.moduleCard:hover{background:var(--white);box-shadow:var(--shadow);transform:translateY(-1px)}
.moduleCard .moduleNo{font-family:ui-monospace,monospace;font-size:26px;color:var(--accent)}.moduleCard h3{margin:0 0 4px;font-size:22px}.moduleCard p{margin:0;color:var(--muted)}.moduleCard .done{font-family:ui-sans-serif,system-ui,sans-serif;font-size:11px;border:1px solid var(--line);border-radius:999px;padding:5px 9px;color:var(--muted)}
.lessonLayout{display:grid;grid-template-columns:220px minmax(0,1fr);gap:68px;align-items:start}.lessonNav{position:sticky;top:96px;align-self:start;padding:18px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.lessonNav a{display:block;text-decoration:none;padding:6px 0;color:var(--muted);font-family:ui-sans-serif,system-ui,sans-serif;font-size:13px}
.lessonMain>section{margin-bottom:72px;scroll-margin-top:100px}.lessonMain h2{font-size:clamp(28px,2.4vw,40px);line-height:1.4}.lessonMain p{font-size:17px;color:#4e5851}
.thirdThing{background:#efe6d8;border:1px solid var(--line);border-radius:22px;padding:28px}.thirdThing .object{font-size:46px;line-height:1;color:var(--accent)}
.completeBox{background:var(--deep);color:white;border-radius:22px;padding:26px}.completeBox p{color:#d7ddd8}.completeBox .tag{color:#e4b379}.completeBox .toolButton.primary{background:#f3eadb;color:var(--deep);border-color:#f3eadb;box-shadow:none}
.thirdGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.thirdCard{background:rgba(255,253,248,.58);border:1px solid var(--line);border-radius:18px;padding:22px;min-height:220px}.thirdCard .symbol{font-size:38px;color:var(--accent)}.thirdCard h3{margin:10px 0 7px;font-size:22px}.thirdCard p{color:var(--muted)}
.questionTool{background:#eee5d7;border:1px solid var(--line);border-radius:22px;padding:26px}.generatedQuestion{margin-top:14px;padding:20px;background:var(--white);border:1px solid var(--line);border-radius:16px;font-size:20px;min-height:80px}
.recordList{display:grid;gap:10px}.recordItem{background:rgba(255,253,248,.58);border:1px solid var(--line);border-radius:16px;padding:18px}.recordItem time{font-family:ui-sans-serif,system-ui,sans-serif;font-size:11px;color:#77746e}.recordItem h4{margin:5px 0;font-size:20px}.recordItem p{white-space:pre-wrap;color:#4e5851}
.externalLink{display:inline-block;margin-top:10px;font-family:ui-sans-serif,system-ui,sans-serif;font-size:13px;color:var(--accent);text-decoration:none}

/* V3 visual storytelling */
.portraitHero{display:grid;grid-template-columns:1.08fr .92fr;gap:54px;align-items:center}
.portraitFrame{position:relative;max-width:420px;justify-self:end}
.portraitFrame:before{content:"";position:absolute;inset:18px -18px -18px 18px;border:1px solid var(--line);border-radius:50% 50% 44% 56%/46% 52% 48% 54%;z-index:0}
.portraitFrame img{position:relative;z-index:1;display:block;width:100%;aspect-ratio:2/3;object-fit:cover;border-radius:48% 48% 43% 57%/42% 50% 50% 58%;filter:saturate(.78) sepia(.08);box-shadow:var(--shadow)}
.credit{font-family:ui-sans-serif,system-ui,sans-serif;font-size:10px;color:#7a756e;margin-top:12px;line-height:1.5}.credit a{text-decoration:none;border-bottom:1px dotted rgba(122,117,110,.5)}
.storyLead{max-width:780px;font-size:20px;line-height:1.9;color:#465149}
.storyGrid{display:grid;grid-template-columns:1fr 1fr;gap:54px;align-items:center}
.visualPanel{background:rgba(255,253,248,.52);border:1px solid var(--line);border-radius:24px;padding:28px;min-height:320px;display:grid;place-items:center;overflow:hidden;position:relative}
.visualPanel.darkVisual{background:var(--deep);border-color:var(--deep)}
.visualPanel svg{width:100%;height:auto;max-height:360px;overflow:visible}
.visualCaption{font-family:ui-sans-serif,system-ui,sans-serif;font-size:12px;color:#77746e;margin-top:10px;line-height:1.65}
.longArc{display:grid;grid-template-columns:110px 1fr;gap:28px;padding:30px 0;border-top:1px solid var(--line)}
.longArc:last-child{border-bottom:1px solid var(--line)}
.longArc .arcNo{font-family:ui-monospace,monospace;font-size:13px;color:var(--accent);padding-top:8px}
.longArc h3{font-size:clamp(27px,3vw,40px);line-height:1.36;margin:0 0 12px}
.longArc p{font-size:17px;color:var(--muted);max-width:780px;margin:0}
.timeline{position:relative;margin-top:30px}
.timeline:before{content:"";position:absolute;left:25px;top:0;bottom:0;width:1px;background:var(--line)}
.timelineItem{position:relative;display:grid;grid-template-columns:54px 1fr;gap:24px;padding:0 0 44px}
.timelineDot{width:16px;height:16px;border-radius:50%;background:var(--paper);border:2px solid var(--accent);margin:5px 0 0 18px;position:relative;z-index:2}
.timelineBody{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(220px,.8fr);gap:28px;padding-bottom:34px;border-bottom:1px solid var(--line)}
.timelineBody h3{font-size:25px;line-height:1.45;margin:5px 0 10px}.timelineBody p{margin:0;color:var(--muted);font-size:16px}
.timelineVisual{min-height:170px;border-radius:18px;background:#eee5d7;border:1px solid var(--line);display:grid;place-items:center;padding:18px}
.timelineVisual svg{width:100%;max-height:150px}
.influenceMap{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;position:relative}
.influenceNode{background:rgba(255,253,248,.6);border:1px solid var(--line);border-radius:18px;padding:18px;min-height:210px}
.influenceNode h3{font-size:20px;margin:8px 0 8px}.influenceNode p{font-size:14px;color:var(--muted)}
.bookRiver{display:grid;grid-template-columns:repeat(6,1fr);gap:8px;align-items:stretch}
.bookStep{background:rgba(255,253,248,.6);border:1px solid var(--line);padding:18px 14px;border-radius:16px;text-decoration:none;min-height:220px;display:flex;flex-direction:column;justify-content:space-between;position:relative}
.bookStep:after{content:"→";position:absolute;right:-9px;top:50%;transform:translateY(-50%);color:var(--accent);z-index:3}
.bookStep:last-child:after{display:none}.bookStep strong{font-size:17px;line-height:1.45}.bookStep span{font-size:13px;color:var(--muted)}
.conceptTrail{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:18px 0}
.conceptTrail a{font-family:ui-sans-serif,system-ui,sans-serif;font-size:12px;text-decoration:none;padding:7px 11px;border:1px solid var(--line);border-radius:999px;background:rgba(255,255,255,.45)}
.conceptTrail i{font-style:normal;color:var(--accent)}
.worldChapter{padding:84px 0;border-top:1px solid var(--line)}
.worldChapter:nth-child(even){background:rgba(255,253,248,.28)}
.chapterGrid{display:grid;grid-template-columns:minmax(0,.92fr) minmax(0,1.08fr);gap:70px;align-items:center}
.chapterNo{font-family:ui-monospace,monospace;font-size:12px;letter-spacing:.1em;color:var(--accent)}
.chapterText h2{font-size:clamp(30px,3.7vw,49px);line-height:1.38;margin:10px 0 18px;letter-spacing:-.02em}
.chapterText p{font-size:17px;color:var(--muted);line-height:1.9}
.chapterText .coreQuestion{font-size:22px;line-height:1.65;color:var(--ink);border-left:2px solid var(--accent);padding-left:18px;margin:24px 0}
.contrastGrid{display:grid;grid-template-columns:1fr 1fr;gap:12px}.contrastCard{padding:22px;border-radius:18px;border:1px solid var(--line);background:rgba(255,253,248,.62)}.contrastCard.alt{background:#eee5d7}.contrastCard h3{margin:5px 0 12px;font-size:21px}.contrastCard ul{padding-left:18px;margin:0;color:var(--muted)}
.externalCta{background:var(--deep);color:white;border-radius:24px;padding:32px;display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center;margin-top:26px}.externalCta h3{margin:4px 0 8px;font-size:25px}.externalCta p{margin:0;color:#d5dcd7}.externalCta .btn{border-color:#f2e6d5;color:var(--deep);background:#f2e6d5}
.miniDiagram{width:100%;height:260px}.miniDiagram .line{fill:none;stroke:#8a4f2d;stroke-width:2}.miniDiagram .soft{fill:none;stroke:#cfc4b3;stroke-width:1.2}.miniDiagram text{font-family:ui-sans-serif,system-ui,sans-serif;fill:#445149;font-size:12px}.miniDiagram .accentText{fill:#8a4f2d;font-weight:700}
.drawPath{stroke-dasharray:900;stroke-dashoffset:900;animation:drawPath 2.6s ease forwards}.pulseNode{transform-box:fill-box;transform-origin:center;animation:pulseNode 4s ease-in-out infinite}.fadeNode{animation:fadeNode 2.2s ease both}
.whisper{animation:whisper 6s ease-in-out infinite}.whisper.b{animation-delay:-1.5s}.whisper.c{animation-delay:-3s}.whisper.d{animation-delay:-4.5s}
.growBranch{stroke-dasharray:420;stroke-dashoffset:420;animation:drawPath 2.8s ease forwards}
.openPath{stroke-dasharray:440;stroke-dashoffset:440;animation:drawPath 2.7s ease forwards}
.integrityLeft{transform-box:fill-box;transform-origin:center;animation:integrityLeft 6s ease-in-out infinite}.integrityRight{transform-box:fill-box;transform-origin:center;animation:integrityRight 6s ease-in-out infinite}
.communityPerson{transform-box:fill-box;transform-origin:center;animation:communityPerson 5.2s ease-in-out infinite}.communityPerson.p2{animation-delay:-.7s}.communityPerson.p3{animation-delay:-1.4s}.communityPerson.p4{animation-delay:-2.1s}.communityPerson.p5{animation-delay:-2.8s}.communityPerson.p6{animation-delay:-3.5s}.communityPerson.p7{animation-delay:-4.2s}
.relationPulse{stroke-dasharray:5 7;animation:dashMove 8s linear infinite}.subjectLink{stroke-dasharray:90;stroke-dashoffset:90;animation:drawPath 2.2s ease forwards}.balanceNode{transform-box:fill-box;transform-origin:center;animation:balanceNode 5s ease-in-out infinite}
.publicStage{animation:fadeNode 1.2s ease both}.publicStage.s2{animation-delay:.3s}.publicStage.s3{animation-delay:.6s}.publicStage.s4{animation-delay:.9s}
@keyframes drawPath{to{stroke-dashoffset:0}}@keyframes pulseNode{0%,100%{opacity:.58;transform:scale(.94)}50%{opacity:1;transform:scale(1.08)}}@keyframes fadeNode{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}@keyframes whisper{0%,100%{opacity:.28;transform:translateY(0)}50%{opacity:.72;transform:translateY(-4px)}}@keyframes integrityLeft{0%,100%{transform:translateX(-9px)}50%{transform:translateX(7px)}}@keyframes integrityRight{0%,100%{transform:translateX(9px)}50%{transform:translateX(-7px)}}@keyframes communityPerson{0%,100%{opacity:.55;transform:scale(.92)}50%{opacity:1;transform:scale(1.08)}}@keyframes balanceNode{0%,100%{transform:translateX(-12px)}50%{transform:translateX(12px)}}
.mobiusWrap{position:relative;width:min(100%,560px);margin:auto;perspective:900px}.mobiusWrap svg{overflow:visible;transform-origin:50% 50%;animation:mobiusFloat 8s ease-in-out infinite}.mobiusShadow{fill:none;stroke:#1f2924;stroke-width:43;stroke-linecap:round;opacity:.14;filter:url(#mobiusShadow)}.mobiusRibbon{fill:none;stroke:url(#mobiusRibbonGrad);stroke-width:34;stroke-linecap:round;filter:url(#mobiusSoftShadow)}.mobiusEdge{fill:none;stroke:rgba(255,255,255,.66);stroke-width:2;stroke-linecap:round;opacity:.6}.mobiusUnderEdge{fill:none;stroke:#5a3b2c;stroke-width:1.4;stroke-linecap:round;opacity:.55}.mobiusCrossShadow{fill:none;stroke:#1c2a24;stroke-width:43;stroke-linecap:round;opacity:.22;filter:url(#mobiusShadow)}.mobiusCross{fill:none;stroke:url(#mobiusCrossGrad);stroke-width:35;stroke-linecap:round;filter:url(#mobiusSoftShadow)}.mobiusGlint{fill:none;stroke:#fff4d6;stroke-width:5;stroke-linecap:round;stroke-dasharray:30 520;animation:mobiusGlint 6.5s linear infinite;opacity:.82}.mobiusLabel{font-family:ui-sans-serif,system-ui,sans-serif;font-size:12px;fill:#526059}.mobiusLabel.accent{fill:#8a4f2d;font-weight:700}
@keyframes dashMove{to{stroke-dashoffset:-130}}@keyframes mobiusGlint{to{stroke-dashoffset:-550}}@keyframes mobiusFloat{0%,100%{transform:rotateX(7deg) rotateZ(-1.5deg) translateY(0)}50%{transform:rotateX(3deg) rotateZ(1deg) translateY(-5px)}}
.photoBand{display:grid;grid-template-columns:minmax(300px,360px) minmax(0,1fr);gap:54px;align-items:center;padding:44px;background:rgba(255,253,248,.5);border:1px solid var(--line);border-radius:24px}.photoBand img{width:100%;max-height:520px;object-fit:cover;border-radius:18px;filter:saturate(.78) sepia(.06)}.photoBand h2{font-size:clamp(31px,3.25vw,42px);line-height:1.38;margin:8px 0 18px}.photoBand p{font-size:17px;color:var(--muted)}
.sourceNote{font-family:ui-sans-serif,system-ui,sans-serif;font-size:12px;color:#77746e;border-top:1px solid var(--line);padding-top:14px;margin-top:22px}
.bioIntro{display:grid;grid-template-columns:minmax(0,.92fr) minmax(0,1.08fr);gap:64px;align-items:start}
.bioHero h1{max-width:10.8em}
.bioIntro .storyLead{font-size:21px}
.bioFacts{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}.bioFact{padding:18px;border:1px solid var(--line);border-radius:16px;background:rgba(255,253,248,.54)}.bioFact b{display:block;font-family:ui-sans-serif,system-ui,sans-serif;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);margin-bottom:7px}.bioFact span{font-size:17px;line-height:1.6}
.bioNav{display:grid;grid-template-columns:repeat(5,1fr);border:1px solid var(--line);border-radius:18px;overflow:hidden;background:rgba(255,253,248,.62)}.bioNav a{display:block;padding:17px 14px;text-decoration:none;border-right:1px solid var(--line);min-height:76px}.bioNav a:last-child{border-right:0}.bioNav small{display:block;font-family:ui-monospace,monospace;font-size:10px;letter-spacing:.08em;color:var(--accent);margin-bottom:5px}.bioNav strong{font-size:14px;line-height:1.4}.bioNav a:hover{background:var(--white)}
.bioChapter{padding:74px 0;border-top:1px solid var(--line);scroll-margin-top:88px}.bioChapter:nth-of-type(even){background:rgba(255,253,248,.25)}
.bioChapterGrid{display:grid;grid-template-columns:minmax(0,.92fr) minmax(320px,1.08fr);gap:62px;align-items:center}.bioChapter.reverse .bioText{order:2}.bioChapter.reverse .bioMedia{order:1}
.bioYear{font-family:ui-monospace,monospace;font-size:12px;letter-spacing:.12em;color:var(--accent);text-transform:uppercase}.bioText h2{font-size:clamp(32px,4vw,52px);line-height:1.38;margin:10px 0 20px}.bioText p{font-size:17px;line-height:1.95;color:var(--muted)}.bioText p:first-of-type{font-size:20px;color:#465149}
.bioMedia{min-height:320px;border:1px solid var(--line);border-radius:24px;background:rgba(255,253,248,.55);overflow:hidden;display:grid;place-items:center;position:relative}.bioMedia img{width:100%;height:100%;min-height:320px;max-height:500px;object-fit:cover;filter:saturate(.76) sepia(.08)}.bioMedia .credit{padding:0 16px 14px}.bioMedia .visualPanel{width:100%;height:100%;border:0;border-radius:0;background:transparent}
.bioPull{font-size:clamp(25px,3vw,39px);line-height:1.58;margin:24px 0;padding:24px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);color:var(--ink)}
.bioMilestones{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.bioMilestone{padding:20px;border:1px solid var(--line);border-radius:16px;background:rgba(255,253,248,.55)}.bioMilestone b{display:block;font-size:27px;color:var(--accent);margin-bottom:6px}.bioMilestone span{font-size:14px;color:var(--muted)}
.bioResources{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.bioResource{display:block;text-decoration:none;padding:24px;border:1px solid var(--line);border-radius:18px;background:rgba(255,253,248,.62);min-height:190px}.bioResource:hover{background:var(--white);box-shadow:var(--shadow);transform:translateY(-2px)}.bioResource h3{font-size:22px;margin:10px 0}.bioResource p{font-size:15px;color:var(--muted)}
.bioSources{display:grid;gap:10px}.bioSource{padding:18px 20px;border-left:2px solid var(--accent);background:rgba(255,253,248,.48)}.bioSource b{display:block;margin-bottom:4px}.bioSource span{font-size:14px;color:var(--muted)}
.hideOnMain{display:none!important}

@media(prefers-reduced-motion:reduce){
  *,*::before,*::after{scroll-behavior:auto!important;animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important}
  .drawPath{stroke-dashoffset:0}
  .growBranch,.openPath{stroke-dashoffset:0}
}

@media(max-width:1000px){
  nav{display:none}
  .heroGrid,.head,.articleLayout,.lessonLayout,.labGrid,.studyDock,.portraitHero,.storyGrid,.chapterGrid,.photoBand,.bioIntro,.bioChapterGrid{grid-template-columns:minmax(0,1fr)}
  .bioChapter.reverse .bioText,.bioChapter.reverse .bioMedia{order:initial}
  .bioMilestones{grid-template-columns:repeat(2,1fr)}
  .bioResources{grid-template-columns:repeat(2,1fr)}
  .toc,.lessonNav{position:static}
  .heroMain{padding-bottom:74px}
  .heroSide{padding-top:0}
  .grid3,.grid4{grid-template-columns:repeat(2,1fr)}
  .journeyGrid{grid-template-columns:1fr}
  .pathwayFlow{grid-template-columns:repeat(3,1fr)}
  .networkGrid{grid-template-columns:repeat(2,1fr)}
  .thirdGrid{grid-template-columns:repeat(2,1fr)}
  .influenceMap,.bookRiver{grid-template-columns:repeat(2,1fr)}
  .bookStep:after{display:none}
  .portraitFrame{justify-self:start;max-width:330px}
  .timelineBody{grid-template-columns:1fr}
  .externalCta{grid-template-columns:1fr}
  .experienceHero .stage:after,.experienceHero .stage:before{opacity:.45}
}
@media(max-width:680px){
  .shell{width:min(var(--max),calc(100% - 32px))}
  h1,h2,h3{word-break:normal!important;overflow-wrap:anywhere;line-break:auto;text-wrap:balance}
  p,.lead,.storyLead{overflow-wrap:anywhere}
  .semanticTitle .titleLine{width:auto;max-width:100%;white-space:normal;text-wrap:balance}
  .actions{max-width:100%;min-width:0}
  .btn,.toolButton{max-width:100%;white-space:normal;text-align:center}
  h1{font-size:clamp(34px,11vw,48px)}
  .heroMain,.heroMain.compact{min-height:auto;padding:58px 0 78px}
  .heroFoot{bottom:22px}
  .heroSide{padding:0 0 48px}
  .grid2,.grid3,.grid4,.matrix,.relationMap,.networkGrid,.thirdGrid,.influenceMap,.bookRiver,.contrastGrid,.bioMilestones,.bioResources,.bioFacts{grid-template-columns:1fr}
  .bioChapter{padding:58px 0}
  .bioChapterGrid{gap:28px}
  .bioMedia{min-height:240px}
  .bioMedia img{min-height:240px}
  .bioHero h1{font-size:clamp(34px,8.5vw,38px);max-width:none;letter-spacing:-.04em}
  .bioNav{display:grid;grid-template-columns:1fr 1fr;overflow:hidden}
  .bioNav a{min-width:0;border-right:1px solid var(--line);border-bottom:1px solid var(--line)}
  .bioNav a:nth-child(2n){border-right:0}
  .bioNav a:last-child{grid-column:1/-1;border-right:0;border-bottom:0}
  .section{padding:70px 0}
  .head{gap:18px;margin-bottom:34px}
  .table{font-size:13px;display:block;overflow-x:auto}
  .experienceHero{padding-bottom:48px}
  .experienceHero .stage{min-height:620px;padding:68px 0 76px;justify-content:flex-start}
  .experienceHero .stage:after{width:280px;height:280px;right:-120px;top:70%}
  .experienceHero .stage:before{display:none}
  .experienceHero h1{font-size:clamp(39px,9.5vw,43px)}
  .pathwayFlow{grid-template-columns:1fr}
  .moduleCard{grid-template-columns:48px 1fr}.moduleCard .done{grid-column:2}
  .questionBand{padding:30px 24px}
  .courseHero{padding:34px 24px}
  .article section,.lessonMain>section{margin-bottom:56px}
  .worldChapter{padding:64px 0}.chapterGrid{gap:34px}
  .timelineBody{gap:16px}.timelineVisual{min-height:140px}
  .longArc{grid-template-columns:1fr;gap:8px}
  .photoBand{padding:24px;gap:26px}
}
"""
(ROOT/"assets/site.css").write_text(CSS, encoding="utf-8")

JS = r"""
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')}),{threshold:.05});
document.querySelectorAll('.reveal').forEach(e=>io.observe(e));

/* Keep intentional Chinese title lines intact without ever clipping them.
   On desktop/tablet, shrink the whole heading slightly only when a designed
   semantic line is wider than its real container. On phones CSS allows the
   semantic line itself to wrap naturally instead of forcing tiny type. */
const semanticTitleHeads=[...document.querySelectorAll('h1:has(.semanticTitle),h2:has(.semanticTitle)')];
const fitSemanticTitles=()=>{
  semanticTitleHeads.forEach(h=>{
    if(!h.dataset.fitReady){
      h.dataset.fitReady='1';
      h.dataset.fitInlineFont=h.style.fontSize||'';
    }
    h.style.fontSize=h.dataset.fitInlineFont;
    h.classList.remove('semanticTitleFit');
    if(window.innerWidth<=680) return;
    const title=h.querySelector('.semanticTitle');
    const lines=[...title.querySelectorAll('.titleLine')];
    const available=Math.max(1,h.clientWidth-2);
    const base=parseFloat(getComputedStyle(h).fontSize)||40;
    const min=Math.max(24,base*.64);
    if(lines.some(line=>line.scrollWidth>available+.5)){
      h.classList.add('semanticTitleFit');
      let size=base;
      while(size>min && lines.some(line=>line.scrollWidth>available+.5)){
        size-=.5;
        h.style.fontSize=size+'px';
      }
    }
  });
};
let fitTimer;
const scheduleTitleFit=()=>{clearTimeout(fitTimer);fitTimer=setTimeout(fitSemanticTitles,40)};
requestAnimationFrame(fitSemanticTitles);
if(document.fonts&&document.fonts.ready) document.fonts.ready.then(fitSemanticTitles);
window.addEventListener('resize',scheduleTitleFit,{passive:true});

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
    recordsRoot.innerHTML=records.length?records.map(r=>'<div class="recordItem"><time>'+new Date(r.time).toLocaleString()+'</time><h4>'+esc(r.title)+'</h4><p>'+esc(r.text)+'</p><button class="toolButton" data-delete-record="'+r.id+'">删除</button></div>').join(''):'<div class="card"><p>还没有记录。你在概念页或自修工具里保存的书写，会出现在这里。</p></div>';
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
const reduceMotion=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if(reduceMotion){
  document.querySelectorAll('[data-animated-svg]').forEach(svg=>{try{svg.pauseAnimations&&svg.pauseAnimations()}catch(e){}});
}
"""
(ROOT/"assets/site.js").write_text(JS, encoding="utf-8")

def nav(pref):
    items=[
        ("parker-palmer/","帕克·帕尔默"),("worldview/","思想总图"),("concepts/","核心思想"),("books/","原著地图"),
        ("applications/","教育与生命"),("practice/","实践"),("self-study/","开始探索"),
        (CIRCLE_SITE,"信任圈专题 ↗")
    ]
    links=[]
    for u,t in items:
        if u.startswith("http"):
            links.append(f'<a href="{u}" target="_blank" rel="noopener">{t}</a>')
        else:
            links.append(f'<a href="{pref}{u}">{t}</a>')
    return "<nav>"+"".join(links)+"</nav>"

def wrap(title, body, depth=0, desc=""):
    pref="../"*depth
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#f4efe5"><title>{html.escape(title)}｜帕克·帕尔默思想研究</title><meta name="description" content="{html.escape(desc or title)}"><link rel="stylesheet" href="{pref}assets/site.css"></head><body><header class="top"><div class="shell topin"><a class="brand" href="{pref}index.html" aria-label="返回首页"><span class="mark" aria-hidden="true">◌</span><span class="brandText"><strong>帕克·帕尔默</strong><small>思想 · 原著 · 实践</small></span></a>{nav(pref)}</div></header>{body}<footer class="footer"><div class="shell"><strong>帕克·帕尔默：思想、原著与生命实践</strong><p>独立中文研究项目。内容以帕克·帕尔默原著、带领指南与相关研究文献为基础；本站将“原著思想”“后续实践发展”“本站整理与应用”尽量分开呈现。Circle of Trust® 等相关名称归其权利方所有。</p></div></footer><script src="{pref}assets/site.js"></script></body></html>'''

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

def sem_title(*lines):
    """Render intentional Chinese title breaks. Each line is kept intact on screen."""
    return '<span class="semanticTitle">' + ''.join(f'<span class="titleLine">{line}</span>' for line in lines) + '</span>'

def sem_title_auto(title):
    """Split trusted internal titles only at natural Chinese punctuation."""
    cjk=sum(1 for ch in title if '\u3400' <= ch <= '\u9fff')
    if cjk <= 10:
        return title
    for sep in ("：","，","；"):
        if sep in title:
            left,right=title.split(sep,1)
            if left and right:
                right_cjk=sum(1 for ch in right if '\u3400' <= ch <= '\u9fff')
                if right_cjk > 10:
                    for marker in ("为什么","为何","怎样","如何"):
                        if marker in right:
                            cut=right.index(marker)+len(marker)
                            if cut < len(right):
                                return sem_title(left+sep,right[:cut],right[cut:])
                return sem_title(left+sep,right)
    return title

def svg_mobius():
    path="M62,150 C118,46 205,43 260,150 C315,257 402,254 458,150 C402,46 315,43 260,150 C205,257 118,254 62,150"
    cross="M207,88 C231,105 246,132 260,150 C274,169 292,194 316,211"
    return f'''<div class="mobiusWrap"><svg viewBox="0 0 520 310" role="img" aria-label="立体莫比乌斯带：内在生命与外在世界彼此连续、彼此塑造" data-animated-svg>
      <defs>
        <linearGradient id="mobiusRibbonGrad" x1="0%" y1="15%" x2="100%" y2="85%">
          <stop offset="0%" stop-color="#d7c5af"/><stop offset="20%" stop-color="#a66a43"/><stop offset="45%" stop-color="#6d402c"/>
          <stop offset="55%" stop-color="#273b32"/><stop offset="78%" stop-color="#87958b"/><stop offset="100%" stop-color="#e3d6c4"/>
        </linearGradient>
        <linearGradient id="mobiusCrossGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#f0dfc7"/><stop offset="34%" stop-color="#b77a4d"/><stop offset="62%" stop-color="#6f4631"/><stop offset="100%" stop-color="#26372f"/>
        </linearGradient>
        <filter id="mobiusShadow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>
        <filter id="mobiusSoftShadow" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#1f2924" flood-opacity=".18"/></filter>
      </defs>
      <path class="mobiusShadow" d="{path}"/>
      <path class="mobiusRibbon" d="{path}"/>
      <path class="mobiusUnderEdge" d="{path}"/>
      <path class="mobiusEdge" d="{path}"/>
      <path class="mobiusCrossShadow" d="{cross}"/>
      <path class="mobiusCross" d="{cross}"/>
      <path class="mobiusGlint" d="{path}"/>
      <text class="mobiusLabel accent" x="66" y="45">INNER · 内在</text>
      <text class="mobiusLabel" x="365" y="278">OUTER · 外在</text>
      <text class="mobiusLabel" x="171" y="302">沿着同一条带前行，内与外会彼此转化</text>
    </svg></div>'''

def svg_split_whole():
    return '''<svg class="miniDiagram" viewBox="0 0 520 260" role="img" aria-label="从分裂生命走向完整性的示意图">
      <path class="soft fadeNode" d="M90 55 C165 85 165 175 90 205"/><path class="soft fadeNode" style="animation-delay:.25s" d="M200 55 C125 85 125 175 200 205"/>
      <text x="58" y="38">INNER</text><text x="184" y="38">ROLE</text>
      <path class="line drawPath" d="M305 130 C335 55 415 55 445 130 C415 205 335 205 305 130"/>
      <circle class="pulseNode" cx="375" cy="130" r="24" fill="#e2c89f" opacity=".8"/>
      <text class="accentText" x="332" y="235">WHOLENESS</text><text x="88" y="235">DIVIDED</text>
    </svg>'''

def svg_inner_teacher():
    return '''<svg class="miniDiagram" viewBox="0 0 520 260" role="img" aria-label="外部声音变淡，中心内在声音浮现">
      <circle class="soft relationPulse" cx="260" cy="130" r="94"/><circle class="soft relationPulse" style="animation-direction:reverse" cx="260" cy="130" r="68"/><circle class="pulseNode" cx="260" cy="130" r="18" fill="#d89b48"/>
      <text class="whisper" x="78" y="56">评价</text><text class="whisper b" x="404" y="78">期待</text><text class="whisper c" x="60" y="205">角色</text><text class="whisper d" x="405" y="210">成功</text>
      <text class="accentText" x="211" y="175">INNER TEACHER</text>
    </svg>'''

def svg_tree():
    return '''<svg class="miniDiagram" viewBox="0 0 520 260" role="img" aria-label="理想化自我与真实生长的对照">
      <path class="soft" d="M130 220V80M95 120L130 95L165 120M100 155L130 130L160 155"/><rect x="88" y="62" width="84" height="165" rx="42" fill="none" stroke="#cfc4b3"/>
      <path class="line growBranch" d="M365 222 C360 180 370 150 360 120 C340 108 325 92 320 68 M360 120 C385 105 405 87 410 63 M355 152 C330 138 315 125 300 104 M360 162 C390 148 407 130 425 112"/>
      <path class="soft" d="M300 225 C325 205 340 205 360 225 C382 205 400 207 424 225"/>
      <text x="84" y="246">应该成为的人</text><text class="accentText" x="328" y="246">真实生长</text>
    </svg>'''

def svg_paths():
    return '''<svg class="miniDiagram" viewBox="0 0 520 260" role="img" aria-label="使命不是单一路线，打开与关闭的道路共同提供线索">
      <path class="line openPath" d="M260 230 C260 190 235 170 205 145 C170 115 145 93 128 54"/><path class="soft fadeNode" d="M260 230 C275 185 315 166 342 140 C378 105 389 78 391 48"/><path class="soft fadeNode" style="animation-delay:.35s" d="M260 230 C235 190 200 190 164 186 C126 181 90 171 64 146"/>
      <circle class="pulseNode" cx="128" cy="54" r="8" fill="#8a4f2d"/><line class="fadeNode" x1="380" y1="39" x2="402" y2="59" stroke="#86514a" stroke-width="2"/><line class="fadeNode" x1="402" y1="39" x2="380" y2="59" stroke="#86514a" stroke-width="2"/>
      <text class="accentText" x="72" y="32">WAY OPENS</text><text x="350" y="30">WAY CLOSES</text><text x="205" y="250">VOCATION</text>
    </svg>'''

def svg_integrity():
    return '''<svg class="miniDiagram" viewBox="0 0 520 260" role="img" aria-label="身份与生活逐渐形成真实关系">
      <circle class="integrityLeft" cx="205" cy="125" r="82" fill="none" stroke="#8a4f2d" stroke-width="2"/><circle class="integrityRight" cx="315" cy="125" r="82" fill="none" stroke="#28362f" stroke-width="2"/>
      <text class="accentText" x="130" y="128">WHO I AM</text><text x="318" y="128">HOW I LIVE</text><text x="222" y="220">INTEGRITY</text>
    </svg>'''

def svg_community():
    people=''.join(f'<circle class="communityPerson p{i+1}" cx="{x}" cy="{y}" r="18" fill="none" stroke="#8a4f2d" stroke-width="1.7"/>' for i,(x,y) in enumerate([(260,42),(370,88),(408,165),(335,222),(185,222),(112,165),(150,88)]))
    return f'''<svg class="miniDiagram" viewBox="0 0 520 270" role="img" aria-label="围绕共同中心、保留个人空间的可信赖共同体">{people}<circle class="soft" cx="260" cy="140" r="55"/><circle class="pulseNode" cx="260" cy="140" r="11" fill="#d89b48"/><text class="accentText" x="205" y="168">COMMON CENTER</text></svg>'''

def svg_knowing():
    return '''<svg class="miniDiagram" viewBox="0 0 520 260" role="img" aria-label="从关于对象的知识转向在关系中的认识">
      <rect x="54" y="62" width="170" height="130" rx="16" fill="none" stroke="#cfc4b3"/><circle cx="96" cy="126" r="22" fill="none" stroke="#8a4f2d"/><circle cx="181" cy="126" r="22" fill="none" stroke="#28362f"/><line x1="120" y1="126" x2="157" y2="126" stroke="#cfc4b3" stroke-dasharray="4 5"/>
      <text x="72" y="220">KNOWING ABOUT</text>
      <circle class="integrityLeft" cx="360" cy="126" r="52" fill="none" stroke="#8a4f2d"/><circle class="integrityRight" cx="398" cy="126" r="52" fill="none" stroke="#28362f"/><text class="accentText" x="318" y="220">IN RELATIONSHIP</text>
    </svg>'''

def svg_subject_centered():
    return '''<svg class="miniDiagram" viewBox="0 0 520 260" role="img" aria-label="教师、学生共同围绕主题形成学习共同体">
      <circle class="pulseNode" cx="260" cy="130" r="44" fill="#eee5d7" stroke="#8a4f2d"/><text class="accentText" x="228" y="134">SUBJECT</text>
      <circle cx="120" cy="78" r="38" fill="none" stroke="#28362f"/><text x="95" y="82">教师</text>
      <circle cx="400" cy="78" r="38" fill="none" stroke="#28362f"/><text x="375" y="82">学生</text>
      <circle cx="260" cy="225" r="28" fill="none" stroke="#cfc4b3"/><text x="239" y="229">世界</text>
      <path class="soft subjectLink" d="M154 91L218 116M366 91L302 116M260 174V197"/>
    </svg>'''

def svg_paradox():
    return '''<svg class="miniDiagram" viewBox="0 0 520 260" role="img" aria-label="在两种真实之间承载张力">
      <line x1="90" y1="130" x2="430" y2="130" stroke="#cfc4b3" stroke-width="2"/><circle cx="90" cy="130" r="26" fill="#eee5d7" stroke="#8a4f2d"/><circle cx="430" cy="130" r="26" fill="#eee5d7" stroke="#28362f"/><circle class="balanceNode" cx="260" cy="130" r="17" fill="#d89b48"/>
      <text x="57" y="185">SOLITUDE</text><text x="397" y="185">COMMUNITY</text><text class="accentText" x="210" y="95">HOLD THE TENSION</text>
    </svg>'''

def svg_public():
    return '''<svg class="miniDiagram" viewBox="0 0 520 260" role="img" aria-label="内在工作进入关系、工作、制度与公共生活">
      <circle class="publicStage" cx="66" cy="130" r="25" fill="#eee5d7" stroke="#8a4f2d"/><circle class="publicStage s2" cx="172" cy="130" r="32" fill="none" stroke="#8a4f2d"/><rect class="publicStage s3" x="246" y="99" width="72" height="62" rx="10" fill="none" stroke="#28362f"/><rect class="publicStage s4" x="370" y="85" width="96" height="90" rx="8" fill="none" stroke="#cfc4b3"/>
      <path class="line drawPath" d="M92 130H139M205 130H246M318 130H370"/>
      <text x="40" y="185">SELF</text><text x="134" y="185">RELATION</text><text x="248" y="185">WORK</text><text class="accentText" x="369" y="200">PUBLIC LIFE</text>
    </svg>'''

def svg_influences():
    return '''<svg class="miniDiagram" viewBox="0 0 520 290" role="img" aria-label="影响帕尔默思想的多个来源围绕其核心主题">
      <circle cx="260" cy="145" r="54" fill="#eee5d7" stroke="#8a4f2d" stroke-width="1.8"/><text class="accentText" x="218" y="140">PARKER</text><text x="223" y="160">PALMER</text>
      <circle class="soft" cx="260" cy="145" r="112"/>
      <circle cx="260" cy="30" r="29" fill="#fffdf8" stroke="#cfc4b3"/><text x="235" y="34">Quaker</text>
      <circle cx="415" cy="92" r="31" fill="#fffdf8" stroke="#cfc4b3"/><text x="392" y="96">Merton</text>
      <circle cx="390" cy="228" r="31" fill="#fffdf8" stroke="#cfc4b3"/><text x="370" y="232">Poetry</text>
      <circle cx="130" cy="228" r="34" fill="#fffdf8" stroke="#cfc4b3"/><text x="94" y="232">Community</text>
      <circle cx="105" cy="92" r="36" fill="#fffdf8" stroke="#cfc4b3"/><text x="72" y="96">Nonviolence</text>
      <path class="soft" d="M260 84V58M310 121L382 99M302 180L366 213M218 180L158 211M208 121L139 100"/>
    </svg>'''

def timeline_visual(kind):
    if kind=="mobius": return svg_mobius()
    if kind=="teaching": return svg_subject_centered()
    if kind=="public": return svg_public()
    if kind=="community" or kind=="pendle": return svg_community()
    if kind=="merton": return svg_inner_teacher()
    if kind=="study": return svg_knowing()
    return svg_tree()

def concept_visual(slug):
    visual=KNOWLEDGE["concepts"].get(slug,{}).get("visual","inner-light")
    return {
        "inner-light":svg_inner_teacher,
        "tree":svg_tree,
        "paths":svg_paths,
        "integrity":svg_integrity,
        "split":svg_split_whole,
        "mobius":svg_mobius,
        "circle":svg_community,
        "third-thing":svg_tree,
        "questions":svg_inner_teacher,
        "conversation":svg_knowing,
        "knowing":svg_knowing,
        "subject-centered":svg_subject_centered,
        "paradox":svg_paradox,
        "action":svg_public,
        "tragic-gap":svg_paradox,
        "bridge":svg_public,
        "public":svg_public,
        "seasons":svg_tree
    }.get(visual,svg_inner_teacher)()

def practice_visual(slug):
    mapping={
        "silence":svg_inner_teacher,"journaling":svg_tree,"third-things":svg_tree,
        "honest-open-questions":svg_inner_teacher,"paired-listening":svg_community,
        "seasons":svg_tree,"way-closes":svg_paths,"tragic-gap":svg_paradox,
        "action-reaction":svg_public,"failure":svg_split_whole,
        "meeting-for-learning":svg_subject_centered
    }
    return mapping.get(slug,svg_integrity)()

def application_visual(slug):
    return {
        "personal":svg_tree,"education":svg_subject_centered,"leadership":svg_integrity,
        "community":svg_community,"public":svg_public
    }.get(slug,svg_mobius)()

# ---------- Thought architecture ----------
world_movements=[
("01","从外部标准回到生命本身","帕尔默的起点不是“怎样成为更优秀的人”，而是停止只从外部规范、职业角色和他人期待来定义自己。","Let Your Life Speak"),
("02","从人格表演回到真实自我","身份包含天赋，也包含限制、伤痕、恐惧和历史。完整性不是完美，而是更真实地与这些力量相处。","The Courage to Teach"),
("03","从分裂走向“灵魂”与“角色”的重新连接","当角色长期背离内在已经知道的真实，人会进入“分裂的生命”（divided life）；“不再分裂”意味着把内在真实逐步带回工作、关系与制度。","A Hidden Wholeness"),
("04","从孤立内省进入可信赖共同体","内在工作不是独自完成。人需要一种既不侵入、也不回避的关系空间，来保护内在导师的声音。","A Hidden Wholeness"),
("05","从直接纠正转向间接唤醒","第三物、隐喻、诗歌、故事、沉默与开放问题都在减少控制，让真相从参与者内部浮现。","A Hidden Wholeness / Courage to Teach"),
("06","从二元对立进入悖论与张力","许多深层问题不是非此即彼：行动与沉思、个人与共同体、现实与可能，需要在更大的容器里同时被承载。","The Courage to Teach / The Active Life"),
("07","从认识的占有转向关系与忠实","认识不只是把对象变成信息；帕尔默把 knowing 与 loving、troth、community of truth 联系起来。","To Know as We Are Known"),
("08","从私人完整性走向公共世界","内在工作最终进入教学、领导、组织和公民生活；完整性通过共同体、公共表达和制度实践获得社会形态。","The Courage to Teach / Healing the Heart of Democracy")
]

# ---------- Concepts ----------
concepts=[
{
"slug":"inner-teacher","cn":"内在导师","en":"Inner Teacher","verb":"聆听",
"summary":"不是一个替你做决定的神秘权威，而是人内在能够辨认真实、意义与方向的资源。帕尔默的方法不是“告诉人答案”，而是保护这个声音能够被自己听见。",
"where":"在《Let Your Life Speak》中，它表现为“听生命在说什么”；在《A Hidden Wholeness》中，它成为信任圈实践的中心；在教育文本中，它对应教师和学习者不可被外部技术取代的主体性。",
"misread":["不是“第一念头就是真理”——内在导师需要时间、现实检验和关系中的辨识。","不是反智或拒绝他人意见——帕尔默强调从他人学习，但不把最终判断权交出去。"],
"practice":["静默 5 分钟，只记录浮现的念头、感受、身体反应，不判断。","把自己今天说过的一句话写下来，问：这句话可能正在告诉我什么？","分两栏写：别人希望我知道的 / 我其实已经知道但还没承认的。"],
"sources":["Let Your Life Speak，第1章 Listening to Life","A Hidden Wholeness，Circle of Trust touchstones：Attend to your own inner teacher"],
"related":["true-self","vocation","trustworthy-community"]
},
{
"slug":"soul","cn":"灵魂 / 内在生命","en":"Soul","verb":"保护",
"summary":"帕尔默用 soul 指向一个脆弱却坚韧的内在核心。它不像自我展示那样喧闹，更像野生动物：只有在不被追捕、分析和强迫的空间里才会出现。",
"where":"“灵魂”是《A Hidden Wholeness》的核心语言，用来解释为什么信任圈必须强调邀请、边界、沉默、保密与不修理他人。",
"misread":["不是必须接受某种宗教教义才能理解；帕尔默也会用“真实自我”（true self）、“内在导师”（inner teacher）等语言指向相近经验。","不是脆弱到需要被保护免于一切挑战；真正的保护，是免于侵入与操控，从而能够面对真实。"],
"practice":["回想一个你曾经“缩回去”的群体场景，写下当时发生了什么。","回想一个你愿意说真话的空间，列出它的三个条件。","设计一个下次聚会的“少做一件事”：少追问、少点评或少解释。"],
"sources":["A Hidden Wholeness，第3–5章","A Hidden Wholeness Guide，touchstones"],
"related":["inner-teacher","trustworthy-community","third-things"]
},
{
"slug":"true-self","cn":"真实自我","en":"True Self","verb":"认出",
"summary":"真实自我不是理想化的“最好版本”，而是生命经验持续显露出来的气质、天赋、限制、渴望、身体反应与边界。",
"where":"《Let Your Life Speak》把使命建立在“真实自我”（true self）之上；《The Courage to Teach》把身份理解为内外力量交汇的动态中心；《A Hidden Wholeness》则把“真实自我”与“灵魂”（soul）放在同一脉络中。",
"misread":["不是“想做什么就做什么”；真实自我同时包含限制。","不是固定不变的人格标签；帕尔默强调身份是在关系与经验中不断形成的。"],
"practice":["列三件让你持续有生命力的事，以及三件长期让你枯竭的事。","回顾一次失败，暂时不问“哪里做错了”，只问“它让我更清楚自己不是什么了吗？”","观察一周：哪些场景让身体放松，哪些场景让你持续收紧？"],
"sources":["Let Your Life Speak，第1–3章","The Courage to Teach，第1章 Identity and Integrity"],
"related":["inner-teacher","identity-integrity","vocation"]
},
{
"slug":"identity-integrity","cn":"身份与完整性","en":"Identity & Integrity","verb":"对齐",
"summary":"身份回答“我是谁”；完整性关乎我怎样让构成生命的不同力量形成较真实的关系。完整不是没有矛盾，而是不再靠切割自己来维持角色。",
"where":"这是《The Courage to Teach》的基础命题：好的教学来自教师的“身份与完整性”（identity and integrity），而不只是教学技巧（technique）。",
"misread":["完整性不是“始终一致、不改变”；它允许成长、修正与复杂性。","完整性不是道德优越；帕尔默明确把阴影、限制、伤痕和恐惧也纳入身份。"],
"practice":["画两个圆：内在的我 / 外在角色，写出重叠区与断裂区。","写一句：我最常用哪个角色保护自己不被真正看见？","选一个小场景，让下周的内外差距缩小 5%。"],
"sources":["The Courage to Teach，第1章","The Courage to Teach Guide，Identity & Integrity 反思"],
"related":["true-self","undivided-life","paradox"]
},
{
"slug":"vocation","cn":"使命与召唤","en":"Vocation","verb":"辨识",
"summary":"使命不是先设计一个伟大目标，再强迫自己实现；它来自倾听生命已经在说什么。天赋、限制、失败、关闭的道路与反复出现的关切，都是线索。",
"where":"《Let Your Life Speak》把“使命”（vocation）与“声音”（voice）联系起来：召唤不是一个追逐的目标，而是一种需要被听见的声音。",
"misread":["不是“找到唯一正确职业”；使命可能穿过多种角色。","不是把个人欲望神圣化；辨识必须面对限制、关系与现实后果。"],
"practice":["写下三次“路关闭”的经历；每次只问：它让我知道了什么？","列出你反复被吸引去关心的问题，不问是否能成功。","把“我应该做什么？”改写成“什么事情已经在向我提出要求？”"],
"sources":["Let Your Life Speak，第1章 Listening to Life；第3章 When Way Closes","Let Your Life Speak，第5章 Leading from Within"],
"related":["inner-teacher","true-self","seasons"]
},
{
"slug":"wholeness","cn":"完整 / 隐藏的完整性","en":"Wholeness","verb":"记起",
"summary":"帕尔默所说的“完整性”（wholeness）不是完美，而是破碎表面之下仍存在一种更深的连结。成长不是制造一个无缺的自我，而是恢复与自己、他人、世界之间被切断的关系。",
"where":"这一意象贯穿《The Active Life》《The Courage to Teach》《A Hidden Wholeness》，并受到 Thomas Merton 的深刻影响。",
"misread":["不是否认创伤、冲突或制度问题。","不是“万事本来都好”；隐藏的完整性要通过真实关系与行动被重新发现。"],
"practice":["画一张“生命碎片图”：工作、关系、身体、价值、创造、休息分别处在什么位置？","找一条被长期切断的连接，设计一个低风险的恢复动作。","记录本周一次“表面破碎、但仍感到某种完整”的时刻。"],
"sources":["A Hidden Wholeness，Chapter I Images of Integrity","The Active Life，hidden wholeness 主题"],
"related":["identity-integrity","undivided-life","paradox"]
},
{
"slug":"divided-life","cn":"分裂的生命","en":"Divided Life","verb":"看见",
"summary":"“分裂的生命”（divided life）指一个人长期把自己真正知道、真正重视的东西与外在角色分开，甚至靠自我背叛维持安全、地位或归属。",
"where":"《A Hidden Wholeness》前半部诊断分裂的生命及其个人与社会后果；《The Courage to Teach》也用它理解教师的恐惧与制度处境。",
"misread":["不是偶尔妥协就等于“虚伪人格”；帕尔默关心的是长期、结构性的内外断裂。","不是鼓励冲动式“做真实的自己”；从分裂走向完整需要共同体、辨识和承担后果。"],
"practice":["写下一个“我知道 / 我却做”的具体场景。","分别列出保持分裂的收益与代价。","问：我需要什么支持，才可能少分裂一点？"],
"sources":["A Hidden Wholeness，第1–2章","The Courage to Teach，Divided No More movement model"],
"related":["undivided-life","identity-integrity","trustworthy-community"]
},
{
"slug":"undivided-life","cn":"不再分裂地生活","en":"Divided No More","verb":"行动",
"summary":"“不再分裂”不是从此没有冲突，而是不再把自己已经认出的真相长期留在私人角落。它是一种把 inner truth 带进 outer world 的决定。",
"where":"在《A Hidden Wholeness》中，这是整本书的旅程；在《The Courage to Teach Guide》中，它成为社会改变四阶段的第一阶段。",
"misread":["不是戏剧性地一次性辞职、决裂或公开表态。","不是孤勇；帕尔默强调“相互支持、彼此对齐的共同体”对持续行动的重要性。"],
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
"summary":"帕尔默既拒绝“我拥有最终答案”的绝对主义，也拒绝“各有各的真理、互不相干”的相对主义。他把真理理解为关于重要事物的一场持续、严肃而有纪律的对话。",
"where":"《A Hidden Wholeness》讨论 circle of trust 中 truth 如何从差异与关联之间逐渐显现；《To Know as We Are Known》则用 troth 强调真理中的忠实关系。",
"misread":["不是为了达成表面一致。","不是把冲突取消，而是让差异不必以征服对方的方式出现。"],
"practice":["在一个分歧上，用三句话表达自己的经验，不解释对方。","听完对方后先说“我听见了什么”，再说“我仍不同意什么”。","写下：这场对话让我看到的更大事实是什么？"],
"sources":["A Hidden Wholeness，truth / tapestry of truth","To Know as We Are Known，troth / community of truth"],
"related":["knowing-loving","trustworthy-community","public-life"]
},
{
"slug":"knowing-loving","cn":"认识即关系","en":"Knowing Is Loving","verb":"进入关系",
"summary":"帕尔默批评把“认识”变成控制、占有，以及把所认识的对象置于对立面。他主张认识是一种进入关系、接受被改变、对所知之物负责任的方式。",
"where":"《To Know as We Are Known》从 Knowing Is Loving 出发，发展 community of troth、teaching as creating space 等教育思想。",
"misread":["不是取消事实、证据和分析。","不是把知识变成情绪体验；它要求更深的责任与相互校正。"],
"practice":["选一个你熟悉的对象：学生、工作、自然、文本。写下你“关于它知道什么”和“与它处在什么关系”。","找一个你常用来控制的知识动作：分类、打分、诊断、预测。问它遮蔽了什么。","设计一个让对象也能“反过来改变你”的学习动作。"],
"sources":["To Know as We Are Known，第1章 Knowing Is Loving","To Know as We Are Known，第5–6章 Teaching / Truth"],
"related":["truth-conversation","education-space","third-things"]
},
{
"slug":"third-things","cn":"第三物与隐喻","en":"Third Things","verb":"斜着说",
"summary":"诗歌、故事、图像、音乐、自然物等可以成为第三物。参与者先共同面对一个对象，再让它折射自己的经验，避免把人直接放在被审视的位置。",
"where":"《A Hidden Wholeness》第 6 章 “The Truth Told Slant” 详细发展这一方法；《The Courage to Teach》也借“主题中心”（subject-centered）与“第三物”（third thing），避免课堂落入过度教师中心或学生中心。",
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
"summary":"帕尔默不把沉思与行动分成高低两个世界。行动帮助我们共同创造现实；沉思帮助我们揭开伪装成现实的幻象。二者交织，才可能形成更真实的行动。",
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
"misread":["不是无限忍耐伤害。","不是拒绝做决定；帕尔默明确指出，承载张力并不等于犹豫不决。"],
"practice":["写下：现实是……；我仍相信可能……","写下什么会把你拉向犬儒，什么会把你拉向不切实际的乐观。","列出三个帮助你在张力中保持完整的人、地方或习惯。"],
"sources":["A Hidden Wholeness，第10章","Healing the Heart of Democracy，broken-open heart / tension-holding"],
"related":["paradox","nonviolence","public-life"]
},
{
"slug":"nonviolence","cn":"日常非暴力","en":"Nonviolence in Everyday Life","verb":"走第三条路",
"summary":"帕尔默所说的非暴力不是被动退让，而是在不侵犯自己与他人灵魂的前提下寻找第三种回应：不逃跑，也不以暴力和控制反击。",
"where":"《A Hidden Wholeness》第10章把 circle of trust 的纪律带回组织、关系和社会改变：提问替代争辩、真话替代羞辱、支持共同体帮助人持续行动。",
"misread":["不是避免冲突。","不是为了操控一个更好结果；非暴力首先是尊重人的灵魂本身。"],
"practice":["找一个惯常只有“忍 / 爆”两种选择的场景，写出第三种回应。","在一次会议中，把一个反驳改成诚实问题。","行动前先确认：我能否既不背叛自己，也不贬低对方？"],
"sources":["A Hidden Wholeness，第10章 The Third Way","A Hidden Wholeness，agents of nonviolence"],
"related":["tragic-gap","undivided-life","public-life"]
},
{
"slug":"public-life","cn":"公共生活","en":"Public Life","verb":"带回世界",
"summary":"帕尔默的内在工作从来不只为了私人安宁。它最终进入学校、组织、职业共同体与公共空间，检验人能否在差异、压力与制度中仍保持声音、关系和完整性。",
"where":"从早期《The Company of Strangers》到《Healing the Heart of Democracy》，帕尔默持续讨论陌生人、公共空间、差异和公民心灵。",
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
"ideas":["使命（vocation）来自聆听，而不是任性意志（willfulness）。","限制与失败不是使命的反面，也可能成为最重要的线索。","领导不是向外塑造形象，而是让内在身份进入关系与行动。"],
"practices":["生命线索日志","道路关闭回顾","“应该 / 正在召唤”双栏书写","季节隐喻反思"],
"concepts":["vocation","true-self","seasons"]
},
{
"slug":"hidden-wholeness","title":"A Hidden Wholeness","zh":"内在之光 / 隐藏的完整性","year":"2004","focus":"如何从“分裂的生命”走向“不再分裂”，并创造一个让灵魂能够出现的共同体。",
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
"ideas":["公共生活不能只建立在亲密关系上。","与陌生人共处是现代共同体的核心能力。","帕尔默对公共生活的思考早于后来“信任圈”（Circle of Trust）的发展，并与之形成连续的思想脉络。"],
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
"slug":"going-public","title":"Going Public","zh":"走向公共生活","year":"1980s","focus":"早期帕尔默如何思考基督徒与美国公共生活的更新，为后来“陌生人、公共空间、完整性”主题提供历史脉络。",
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
"facilitator":["帕尔默把沉默视为一种认识方式，而不是空档。","对不习惯静默的人，稳定的时间标记比“无限沉默”更安全。"],
"debrief":["静默里什么变得更清楚？","什么让我想逃离安静？","沉默是隔离我的，还是连接我的？"],
"source":"A Hidden Wholeness Chapter IX / Meeting for Learning"
},
{
"slug":"journaling","title":"自由书写与自我聆听","en":"Journaling","duration":"10–25 分钟","size":"个人 / 群体",
"purpose":"让说话者也成为自己的听者，捕捉那些比头脑解释更早出现的语言。",
"when":"第三物之后、重大问题前、回顾失败或季节时。",
"steps":["设置一个具体但开放的问题。","持续写，不编辑，不追求文采。","若停住，就重复写最后一句，直到新内容出现。","结束后圈出一句最有能量或最陌生的话。","如果分享，只分享自己愿意带入圆圈的部分。"],
"facilitator":["帕尔默常建议参与者把注意力从“记录带领者说了什么”转回“记录自己说了什么”。","自由书写不是心理诊断，不需要给内容下解释。"],
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
"facilitator":["避免把所有挫折浪漫化成‘命运安排’。","帕尔默的重点是从真实限制中学习，而不是否认痛苦。"],
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
"facilitator":["教师角色不是消失，而是更细腻：既提供专业资源，也帮助建立可被信任的群体。","帕尔默警惕用情感取代理性；wholeness 不是情绪至上。"],
"debrief":["我是否把学习只当成获取？","今天谁/什么改变了我？","这个主题对我的生活提出了什么要求？"],
"source":"Meeting for Learning / To Know as We Are Known"
}
]

# ---------- Applications ----------
applications=[
("personal","个人生命与使命","把帕尔默的思想用于职业选择、生命转折、使命辨识与内外一致。",["vocation","true-self","seasons","way-closes","journaling"]),
("education","教育与教学","从技术中心转向教师身份、共同中心、关系与学习空间。",["identity-integrity","education-space","knowing-loving","third-things","meeting-for-learning","paired-listening"]),
("leadership","领导与专业生命","从角色绩效转向由内而外的领导、行动/反应辨识与共同体支持。",["active-life","undivided-life","trustworthy-community","failure","action-reaction"]),
("community","社群与引导","用基石、第三物、静默、开放问题与澄心会保护参与者主体性。",["trustworthy-community","third-things","honest-open-questions","clearness-committee","circle-of-trust","touchstones"]),
("public","公共生活","练习在差异中保有声音、谦逊、张力承载与非暴力，不把公共生活缩成阵营对抗。",["public-life","tragic-gap","truth-conversation","nonviolence","paired-listening"])
]

# ---------- Glossary ----------
glossary=[
("Inner Teacher","内在导师","帮助人从自身经验辨认真实与方向的内在资源。"),
("True Self","真实自我","生命中持续显露的气质、天赋、限制、渴望与边界。"),
("Soul","灵魂 / 内在生命","帕尔默用来描述一个脆弱却坚韧、需要非侵入性空间的内在核心。"),
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
("Troth","忠实关系","帕尔默借此说明 truth 不只是正确命题，也包含关系中的忠实。"),
("Paradox","悖论","需要 both-and 承载的深层真理。"),
("Tragic Gap","悲剧性张力","现实与可能之间必须承载的距离。"),
("Public Life","公共生活","人与陌生人、制度和共同世界发生关系的日常空间。")
]

concept_lookup={c["slug"]:c for c in concepts}
practice_lookup={p["slug"]:p for p in practices}

# ---------- Experience / self-study relationships ----------
concept_practice_map={
"inner-teacher":["silence","journaling","honest-open-questions"],"soul":["silence","third-things","circle-of-trust"],
"true-self":["journaling","way-closes","seasons"],"identity-integrity":["journaling","paired-listening","action-reaction"],
"vocation":["way-closes","journaling","seasons"],"wholeness":["third-things","seasons","journaling"],
"divided-life":["journaling","paired-listening","action-reaction"],"undivided-life":["action-reaction","tragic-gap","paired-listening"],
"paradox":["tragic-gap","journaling","third-things"],"trustworthy-community":["touchstones","circle-of-trust","paired-listening"],
"truth-conversation":["paired-listening","honest-open-questions","circle-of-trust"],"knowing-loving":["meeting-for-learning","third-things","silence"],
"third-things":["third-things","journaling","silence"],"honest-open-questions":["honest-open-questions","clearness-committee","paired-listening"],
"education-space":["meeting-for-learning","third-things","silence"],"active-life":["action-reaction","failure","journaling"],
"tragic-gap":["tragic-gap","journaling","paired-listening"],"nonviolence":["tragic-gap","honest-open-questions","paired-listening"],
"public-life":["paired-listening","tragic-gap","meeting-for-learning"],"seasons":["seasons","journaling","silence"]
}
concept_book_map={}
for b in books:
    for s in b["concepts"]:
        concept_book_map.setdefault(s,[]).append(b["slug"])

hidden_course=[
{"id":"00","slug":"prelude","chapter":"Prelude","source":"The Blizzard of the World","title":"世界的暴风雪：先找到回家的绳索","focus":"先不急着解决人生，而是辨认：在混乱、压力和外部噪音中，什么能把我带回更真实的自己？","concepts":["inner-teacher","wholeness"],"practice":"journaling","third":"一根绳索","symbol":"〰","questions":["当外界很嘈杂时，什么会让我重新有方向感？","我生命里有哪些人、地方、习惯或作品，像一根不容易丢失的绳索？"],"action":"为接下来十周选定一个固定的自修时间与地点。"},
{"id":"01","slug":"images-of-integrity","chapter":"Chapter I","source":"Images of Integrity: Living “Divided No More”","title":"完整不是完美：看见“不再分裂”的可能","focus":"完整性不是消除所有矛盾，而是不再用持续的自我切割来维持角色与安全。","concepts":["wholeness","divided-life","undivided-life"],"practice":"journaling","third":"莫比乌斯带","symbol":"∞","questions":["谁让你看见过一种不那么分裂的活法？","你的生命中，哪里已经出现“不再分裂”的微小迹象？"],"action":"写下一个你愿意停止长期配合的自我缩小。","official":"https://couragerenewal.org/library/chapter-3-journey-toward-an-undivided-life/"},
{"id":"02","slug":"great-divide","chapter":"Chapter II","source":"Across the Great Divide: Rejoining Soul and Role","title":"跨越鸿沟：让灵魂与角色重新相遇","focus":"许多分裂不是突然发生的，而是从我们很早学会用角色、表现和防御保护自己开始。","concepts":["divided-life","inner-teacher","vocation"],"practice":"journaling","third":"童年游戏的场景","symbol":"◌","questions":["小时候你最自然地投入什么？其中可能藏着哪些天赋或兴趣？","今天的角色里，哪些部分仍与那份生命力相连，哪些已经断开？"],"action":"找回一种曾让你自然投入、但后来被放下的小活动。","official":"https://couragerenewal.org/library/chapter-2-the-great-divide%ef%bf%bc%ef%bf%bc/"},
{"id":"03","slug":"true-self","chapter":"Chapter III","source":"Explorations in True Self: Intimations of the Soul","title":"真实自我：辨认生命的“原生纹理”","focus":"真实自我既包含礼物，也包含限制。它不是理想人格，而是生命一再显露出来的独特形状。","concepts":["true-self","soul","vocation"],"practice":"journaling","third":"种子","symbol":"✦","questions":["你的生命反复向你显露哪些能力、边界与需要？","什么是别人希望你成为的，什么是生命本身一直在成为的？"],"action":"记录一周中三个“更像自己”和三个“离开自己”的时刻。"},
{"id":"04","slug":"alone-together","chapter":"Chapter IV","source":"Being Alone Together: A Community of Solitudes","title":"独处地在一起：共同体为何不应占领个人","focus":"真正支持内在旅程的共同体，不替人解释、修理或做决定，而是让每个人在陪伴中仍保有自己的孤独与主体性。","concepts":["trustworthy-community","soul","inner-teacher"],"practice":"paired-listening","third":"一圈椅子，中间留空","symbol":"○","questions":["什么样的陪伴会让你更能听见自己？","什么样的“关心”反而让你缩回去或依赖别人？"],"action":"完成一次 10 分钟不打断、不建议的双人聆听。","official":"https://couragerenewal.org/library/chapter-4-circles-of-trust%ef%bf%bc%ef%bf%bc/"},
{"id":"05","slug":"creating-circles","chapter":"Chapter V","source":"Preparing for the Journey: Creating Circles of Trust","title":"创造信任圈：先设计条件，再期待深度","focus":"信任不是气氛词。清楚边界、熟练带领、开放邀请、共同中心和适宜氛围，共同构成可信赖空间。","concepts":["trustworthy-community","third-things","seasons"],"practice":"circle-of-trust","third":"季节","symbol":"❋","questions":["什么条件会让你的灵魂觉得这里可以出现？","在你熟悉的群体中，哪一项条件最缺失？"],"action":"为一个真实小组写出一页“空间条件设计”。","official":"https://couragerenewal.org/library/chapter-5-establishing-conditions-for-circles-of-trust%ef%bf%bc%ef%bf%bc/"},
{"id":"06","slug":"truth-told-slant","chapter":"Chapter VI","source":"The Truth Told Slant: The Power of Metaphor","title":"斜着说出真理：第三物为什么能打开内在","focus":"直接追问常让灵魂躲开；诗、故事、图像、自然物和隐喻可以成为共同中心，让意义从侧面出现。","concepts":["third-things","truth-conversation","knowing-loving"],"practice":"third-things","third":"一块石头 / 一幅画 / 一首短诗","symbol":"◇","questions":["最近什么意象一直留在你心里？","如果不直接谈问题本身，哪个物件或画面最能表达你的处境？"],"action":"从第三物素材库挑一个对象，做一次 15 分钟书写。","official":"https://couragerenewal.org/library/chapter-7-common-ground-third-things%ef%bf%bc%ef%bf%bc/"},
{"id":"07","slug":"deep-speaks","chapter":"Chapter VII","source":"Deep Speaks to Deep: Learning to Speak and Listen","title":"深处回应深处：学习真正地说与听","focus":"说真话并不等于倾倒；聆听也不是沉默等待自己发言。两者都需要把注意力从表现与控制移向关系中的真实。","concepts":["truth-conversation","honest-open-questions","trustworthy-community"],"practice":"paired-listening","third":"两只彼此相对、但不碰触的碗","symbol":"◒","questions":["你什么时候最容易为了被理解而说得更多，反而离开了自己？","什么样的聆听曾让你说出比原先更真实的话？"],"action":"练习一次“说 8 分钟 / 听 8 分钟 / 问 2 个开放问题”的对话。"},
{"id":"08","slug":"living-questions","chapter":"Chapter VIII","source":"Living the Questions: Experiments with Truth","title":"活在问题里：从建议转向澄明","focus":"澄心会要求我们放下“我知道什么对你最好”的幻觉，用开放而诚实的问题帮助一个人听见自己的答案。","concepts":["honest-open-questions","inner-teacher","truth-conversation"],"practice":"clearness-committee","third":"一扇没有标示目的地的门","symbol":"▢","questions":["你最近最想从别人那里得到答案的问题是什么？","如果没有人能给建议，你真正需要被问到什么？"],"action":"用开放问题生成器，把三个建议改写成你真的不知道答案的问题。","official":"https://couragerenewal.org/library/chapter-8-clearness-committee%ef%bf%bc%ef%bf%bc/"},
{"id":"09","slug":"laughter-silence","chapter":"Chapter IX","source":"On Laughter and Silence: Not-So-Strange Bedfellows","title":"笑与静默：让严肃不变成僵硬","focus":"静默可以让深层声音出现；幽默则提醒我们放下自我重要感。两者都在松开控制，让共同体更有生命。","concepts":["soul","inner-teacher","trustworthy-community"],"practice":"silence","third":"一只空杯","symbol":"☕","questions":["你经验过哪些连接人的静默，哪些隔离人的静默？","什么时候幽默帮助你从自我防御中松开？"],"action":"做一次 10 分钟有明确开始与结束的静默，不追求特殊状态。"},
{"id":"10","slug":"third-way","chapter":"Chapter X","source":"The Third Way: Nonviolence in Everyday Life","title":"第三条路：站在悲剧性张力中行动","focus":"面对冲突，我们不必只在逃避与攻击之间选择。帕尔默把信任圈的关系纪律带向非暴力、悲剧性张力与现实行动。","concepts":["nonviolence","tragic-gap","undivided-life","public-life"],"practice":"tragic-gap","third":"两岸之间的一座桥","symbol":"⌁","questions":["你正站在哪一个“现实如此 / 但我仍相信可以不同”的张力里？","什么会把你拉向犬儒？什么会把你拉向虚假乐观？"],"action":"写下一个既不否认现实、也不放弃可能的下一步。","official":"https://couragerenewal.org/library/chapter-11-nonviolence-in-everyday-life%ef%bf%bc%ef%bf%bc/"}
]
course_by_concept={}
for m in hidden_course:
    for s in m["concepts"]:
        course_by_concept.setdefault(s,[]).append(m)

third_things=[
("绳索","〰","方向 / 归属","当你迷路时，什么能把你带回自己？",["inner-teacher","wholeness"]),
("莫比乌斯带","∞","内外相连","哪里看似内外两面，其实属于同一个生命？",["identity-integrity","wholeness"]),
("种子","✦","天赋 / 潜能","什么已经存在，只是在等待适合的条件？",["true-self","vocation"]),
("门","▢","选择 / 关闭","哪扇门正在关闭？它让什么变得更清楚？",["vocation","way-closes"]),
("一圈椅子","○","共同体 / 边界","怎样的空间让每个人既被陪伴、又不被占领？",["trustworthy-community"]),
("空杯","☕","静默 / 接收","我能否暂时不填满这个空白？",["inner-teacher","soul"]),
("石头","◇","重量 / 持久","什么是我生命中无法轻易绕开的事实？",["tragic-gap","wholeness"]),
("桥","⌁","张力 / 第三条路","我能否在两端之间建立连接，而不是消灭一端？",["paradox","nonviolence"]),
("季节","❋","节律 / 更新","我现在更像播种、休眠、新生还是收获？",["seasons","vocation"]),
("树根","⌇","身份 / 根基","哪些经验让我扎根，而不是只长出外在枝叶？",["identity-integrity","true-self"]),
("水面","≈","反映 / 扰动","当水面不再被搅动，我可能看见什么？",["silence","inner-teacher"]),
("两只碗","◒","说与听","关系里怎样既有距离，又能彼此回应？",["truth-conversation","trustworthy-community"])
]

def concept_url(slug, prefix=""):
    return f'{prefix}concepts/{slug}.html'

def practice_url(slug, prefix=""):
    return f'{prefix}practice/{slug}.html'

def practice_lab(key,title,prompt,minutes=10):
    safe=html.escape(prompt)
    return f'''<div class="practiceLab"><span class="kicker">Self Practice</span><h3>现在就做一次，不必等“读懂了”</h3><p class="practicePrompt">{safe}</p><div class="labGrid"><div class="timerBox" data-timer data-default-seconds="{minutes*60}"><span class="tag">静默 / 书写计时</span><div class="timerDisplay" data-timer-display></div><div class="timerPresets"><button data-minutes="5">5 分钟</button><button data-minutes="10">10 分钟</button><button data-minutes="15">15 分钟</button><button class="toolButton primary" data-timer-start>开始</button><button class="toolButton" data-timer-reset>重置</button></div><p class="smallNote">计时器只帮助你守住一段不被打断的时间，不要求进入任何特殊状态。</p></div><div class="journalBox"><span class="tag">自由书写</span><textarea data-journal-key="{key}" placeholder="从第一句真实的话开始。这里的内容只保存在你当前浏览器的本地存储中。"></textarea><div class="saveState" data-save-state>自动保存在这台设备</div><div style="margin-top:10px"><button class="toolButton primary" data-record-save="{key}" data-record-title="{html.escape(title)}">加入我的记录</button> <span class="saveState" data-record-state></span></div></div></div></div>'''

def relation_panel(c):
    data=KNOWLEDGE["concepts"].get(c["slug"],{})
    book_links=[]
    for slug in data.get("books",[]):
        b=next((x for x in books if x["slug"]==slug),None)
        if b:
            book_links.append(f'<a href="../books/{slug}.html">{b["zh"]}</a>')
    practice_links=[]
    for slug in data.get("practices",[])[:4]:
        if slug in practice_lookup:
            practice_links.append(f'<a href="../practice/{slug}.html">{practice_lookup[slug]["title"]}</a>')
    related_links=[]
    for slug in data.get("related",[])[:4]:
        if slug in concept_lookup:
            related_links.append(f'<a href="{slug}.html">{concept_lookup[slug]["cn"]}</a>')
    if c["slug"] in {"trustworthy-community","third-things","honest-open-questions","soul"}:
        related_links.append(f'<a href="{CIRCLE_SITE}" target="_blank" rel="noopener">信任圈 /《内在之光》专题 ↗</a>')
    return f'''<div class="relationMap"><div class="relationCol"><h4>在这些原著中继续</h4>{''.join(book_links) or '<span class="smallNote">暂无单独映射</span>'}</div><div class="relationCol"><h4>用这些方法亲自练</h4>{''.join(practice_links) or '<span class="smallNote">从自由书写开始</span>'}</div><div class="relationCol"><h4>沿着知识关系继续</h4>{''.join(related_links) or '<span class="smallNote">回到思想总图继续探索</span>'}</div></div>'''

# ---------- home ----------
home_books=""
for item in PALMER["books"]:
    b=next((x for x in books if x["slug"]==item["slug"]),None)
    zh=b["zh"] if b else item["title"]
    home_books+=f'<a class="bookStep" href="books/{item["slug"]}.html"><span>{item["title"]}</span><strong>{zh}</strong><span>{item["question"]}</span></a>'

home=f'''<main>
<section class="experienceHero"><div class="shell"><div class="stage"><div class="portraitHero"><div><div class="eyebrow">Parker J. Palmer · Thought × Life × World</div><h1>{sem_title("如何成为自己，","又<em>不离开这个世界</em>")}</h1><p class="lead">帕克·帕尔默一生反复追问：我是谁？我怎样知道什么是真实的？我怎样教、怎样工作、怎样与人共同生活？这些看似分散的问题，最终都指向同一个核心：<strong>怎样活得更完整。</strong></p><div class="actions"><a class="btn primary" href="parker-palmer/">认识帕克·帕尔默</a><a class="btn" href="worldview/">打开思想总图</a><a class="btn" href="self-study/practice-now.html">从一个练习开始</a></div></div><div class="visualPanel">{svg_mobius()}<div class="visualCaption">帕尔默常用莫比乌斯带说明：内在生命与外在世界并非彼此隔绝，而是在不断流动、彼此塑造。</div></div></div></div></div></section>

<section class="section" id="who"><div class="shell"><div class="photoBand"><div><img src="assets/images/parker-j-palmer.jpg" alt="Parker J. Palmer 2010 年在明尼苏达北部 Boundary Waters 的照片"><div class="credit">Parker J. Palmer，Sharon L. Palmer 摄，2010 · CC BY-SA 3.0 · Wikimedia Commons</div></div><div><span class="kicker">Who Is Parker Palmer?</span><h2>{sem_title("一个教师，一个思想者，","一个持续探索完整生命的人")}</h2><p>帕尔默写教育，却很少从“教学技巧”开始；他谈使命，却不是告诉人怎样规划职业；他谈内在生命，也从不把人带离关系与公共世界。他真正关心的是：一个人怎样知道自己是谁，并让这个真实的自己进入教学、工作、关系与社会生活。</p><div class="grid2" style="margin-top:24px"><div class="card"><span class="tag">教师</span><p>教育不仅发生在方法里，也发生在“谁在教”。</p></div><div class="card"><span class="tag">作家</span><p>用故事、诗歌、隐喻与生命经验谈复杂思想。</p></div><div class="card"><span class="tag">探索者</span><p>持续追问真实自我、使命、完整性与内在导师。</p></div><div class="card"><span class="tag">公共知识分子</span><p>把内在生命带入教育、领导、民主与公共世界。</p></div></div><div class="actions"><a class="toolButton primary" href="parker-palmer/">完整认识帕尔默 →</a></div></div></div></div></section>

<section class="section"><div class="shell"><div class="head"><div><span class="kicker">Three Long Arcs</span><h2>如果只抓三条思想长线</h2></div><p>不要先记住二十个术语。先看见帕尔默如何把“成为自己”“不再分裂”和“带回世界”连成一条生命路径。</p></div>
<div class="grid3"><a class="card tile" href="concepts/vocation.html"><span class="tag">01 · 成为自己</span><div class="visualPanel" style="min-height:220px;margin:18px 0">{svg_tree()}</div><h3>Inner Teacher → True Self → Vocation</h3><p>不是先问“我应该成为谁”，而是学习辨认：生命本身正在要求我成为什么。</p><span class="arrow">→</span></a>
<a class="card tile" href="concepts/undivided-life.html"><span class="tag">02 · 不再分裂</span><div class="visualPanel" style="min-height:220px;margin:18px 0">{svg_split_whole()}</div><h3>Divided Life → Wholeness → Divided No More</h3><p>完整不是完美，而是让内在真实逐渐有勇气进入外在生活。</p><span class="arrow">→</span></a>
<a class="card tile" href="concepts/public-life.html"><span class="tag">03 · 带回世界</span><div class="visualPanel" style="min-height:220px;margin:18px 0">{svg_public()}</div><h3>Community → Action → Public Life</h3><p>内在工作如果只停在自己身上还没有完成；它最终要接受关系与现实世界的检验。</p><span class="arrow">→</span></a></div></div></section>

<section class="section" id="worldview-preview"><div class="shell"><div class="head wideHead"><div><span class="kicker">Worldview Preview</span><h2>{sem_title("一张图，","看见帕尔默的思想如何从内在走向世界")}</h2></div><p>核心不是“把自己变得更好”，而是重新建立内在、关系、认识、行动与公共生活之间的联系，让一个人活得更完整。</p></div><div class="visualPanel" style="min-height:420px">
<svg class="miniDiagram" viewBox="0 0 900 360" role="img" aria-label="帕尔默思想总图预览">
<circle cx="450" cy="180" r="54" fill="#eee5d7" stroke="#8a4f2d" stroke-width="2"/><text class="accentText" x="410" y="176">WHOLENESS</text><text x="424" y="197">完整生命</text>
<circle class="soft" cx="450" cy="180" r="104"/><circle class="soft" cx="450" cy="180" r="154"/>
<text x="417" y="72">内在生命</text><text x="590" y="130">辨识</text><text x="596" y="245">关系</text><text x="216" y="248">行动</text><text x="218" y="128">公共世界</text>
<path class="line drawPath" d="M450 126 C520 112 570 120 610 151 C650 184 635 238 592 269 C540 306 455 300 385 285 C314 269 251 230 246 180 C241 132 296 96 365 89"/>
</svg></div><div class="actions"><a class="toolButton primary" href="worldview/">进入完整思想总图</a><a class="toolButton" href="concepts/network.html">打开知识关系图</a></div></div></section>

<section class="section"><div class="shell"><div class="head"><div><span class="kicker">Books As Questions</span><h2>{sem_title("六本代表作，","不是六个孤岛")}</h2></div><p>把书名放回帕尔默长期追问的问题中，会更容易理解他的思想演进。</p></div><div class="bookRiver">{home_books}</div></div></section>

<section class="section"><div class="shell"><div class="studyDock"><div><span class="kicker">Practice</span><h2>先不用读完一整套理论</h2><p>给自己十分钟：让外部声音稍微退后，记录此刻有什么是你已经隐约知道，却一直没有认真聆听的。概念页仍保留计时器、自由书写与本地个人记录。</p><div class="actions"><a class="toolButton primary" href="self-study/practice-now.html">开始 10 分钟练习</a><a class="toolButton" href="self-study/">进入自修工具</a></div></div><div class="visualPanel">{svg_inner_teacher()}</div></div></div></section>

<section class="section"><div class="shell"><div class="head"><div><span class="kicker">Where To Go Next</span><h2>你可以从这里继续</h2></div><p>主站负责呈现帕尔默的整体思想；《内在之光》与信任圈的深入学习，则进入独立专题站。</p></div><div class="grid4">
{tile("parker-palmer/","人物","帕克·帕尔默","从生命经历、影响来源与著作演进理解这个人。")}
{tile("worldview/","思想","思想总图","从分裂生命一直走到公共生活，看清整套思想结构。")}
{tile("books/","原著","原著地图","沿着“我们怎样知道、行动、教学、共同生活”进入主要文本。")}
<a class="card tile reveal" href="{CIRCLE_SITE}" target="_blank" rel="noopener"><span class="tag">专题站 ↗</span><h3>《内在之光》与信任圈</h3><p>章节导读、11 条基石、第三物、澄心会及信任圈的深度实践统一在专题站展开。</p><span class="arrow">↗</span></a>
</div></div></section>
</main>'''
(ROOT/"index.html").write_text(wrap("首页",home,0,"从人物、思想总图、原著与生命实践进入帕克·帕尔默的思想世界"),encoding="utf-8")

# ---------- worldview ----------
world_chapters=[
{"no":"01","eyebrow":"DIVIDED LIFE","title":"我们为什么会变得分裂？","question":"当外在角色越来越熟练，内在的自己去了哪里？","body":"帕尔默所说的“分裂的生命”（divided life），并不只是“虚伪”或偶尔妥协。一个人为了适应学校、职业、家庭与社会评价，会逐渐学会隐藏某些真实经验。外在的角色仍能运作，内在却越来越难说出自己真正知道、真正重视的是什么。分裂之所以危险，不只因为痛苦，更因为我们会把这种断裂带进关系、课堂、组织与制度。","visual":"split","links":["divided-life","identity-integrity"],"books":["courage-to-teach","hidden-wholeness"]},
{"no":"02","eyebrow":"INNER TEACHER","title":"第一步不是改变，而是重新聆听","question":"如果外部声音安静一些，我里面还有什么声音？","body":"帕尔默不急着给人一个新的成功方案。他更先关心：一个人是否还有能力辨认自己内在的经验。“内在导师”（inner teacher）不是一时冲动，也不是拒绝理性或他人的声音；它指向一种能够帮助人辨认生命力、意义、边界与方向的内在资源。静默的作用，不是制造神秘体验，而是让那些长期被评价、角色和焦虑盖住的东西重新可被听见。","visual":"inner","links":["inner-teacher","soul"],"books":["let-your-life-speak","hidden-wholeness"]},
{"no":"03","eyebrow":"TRUE SELF","title":"真实自我不是理想自我","question":"如果不再把自己修剪成“应该的样子”，什么会继续生长？","body":"“真实自我”（true self）不是一个完美、纯净、永远确定的内核。它包含天赋，也包含限制；包含热情，也包含不适合自己的道路。帕尔默一再提醒：人的自我并不是可以无限塑形的。认识自己，因此不是把所有可能性都扩张，而是更诚实地辨认哪些经验使生命变得有生气，哪些长期让自己枯竭。","visual":"tree","links":["true-self","vocation"],"books":["let-your-life-speak","courage-to-teach"]},
{"no":"04","eyebrow":"VOCATION","title":"使命不是职业规划","question":"生命已经在告诉我什么，而我是否愿意听？","body":"在帕尔默那里，“使命”（vocation）与“声音”（voice）紧密相连。使命不是先设想一个宏大的未来，再靠意志把现实推向那个目标；它更像从一生反复出现的天赋、限制、吸引、失败与“道路关闭”中逐渐辨认方向。关上的门并不总是失败，它有时在帮助我们停止成为一个并不属于自己的角色。","visual":"paths","links":["vocation","seasons"],"books":["let-your-life-speak"]},
{"no":"05","eyebrow":"IDENTITY & INTEGRITY","title":"完整性不是“永远一致”","question":"我是谁，与我怎样生活，能否形成更真实的关系？","body":"“身份”（identity）回答“哪些力量构成了我”；“完整性”（integrity）则关乎我怎样与这些力量相处。完整性并不要求消灭矛盾，也不是把自己固定成一种人格。它更像让内在的天赋、限制、恐惧、历史与价值，不再长期被外在角色切断。真正的对齐往往不是一次剧烈决定，而是让日常生活中的内外差距一点点缩小。","visual":"integrity","links":["identity-integrity","wholeness","undivided-life"],"books":["courage-to-teach"]},
{"no":"06","eyebrow":"TRUSTWORTHY COMMUNITY","title":"内在旅程必须自己走，却很难完全独自完成","question":"什么样的共同体能陪伴我，却不占领我？","body":"帕尔默的共同体思想里有一个关键悖论：最终的辨识必须由个人完成，但人又需要关系来保护这项工作。可信赖共同体不是彼此给答案，也不是把亲密当作目标；它创造边界、邀请、共同中心和足够的沉默，使每个人能够在陪伴中仍保有自己的主体性。“信任圈”（Circle of Trust）是这一思想的重要实践发展，但它只是帕尔默整体思想中的一个节点。","visual":"community","links":["trustworthy-community","third-things","honest-open-questions"],"books":["hidden-wholeness"]},
{"no":"07","eyebrow":"KNOWING IN RELATIONSHIP","title":"认识世界，也是在决定怎样与世界相处","question":"知识是占有一个对象，还是进入一段会改变彼此的关系？","body":"在《To Know as We Are Known》中，帕尔默把问题进一步推进到“我们如何认识”这一层：如果知识只意味着把对象拉开距离、分类、预测和控制，我们也会被这种认识方式塑造成更疏离的人。他并不反对事实与分析，而是追问：能不能有一种认识，同时包含严谨、关系、责任和被所知之物改变的可能？","visual":"knowing","links":["knowing-loving","truth-conversation"],"books":["to-know-as-we-are-known"]},
{"no":"08","eyebrow":"SUBJECT-CENTERED EDUCATION","title":"教育的中心既不是教师，也不是学生","question":"我们究竟为了什么而相聚？","body":"帕尔默反对把课堂简化成“教师中心”与“学生中心”的二选一。他提出把值得共同面对的主题、文本、问题或现实放在中心：教师带来专业、经验与边界，学生带来问题与生命经验，双方都要向一个比彼此更大的共同中心负责。这样，课堂才可能成为一个“真理共同体”（community of truth），而不是知识输送或对需求的简单迎合。","visual":"subject","links":["education-space","knowing-loving","identity-integrity"],"books":["courage-to-teach","to-know-as-we-are-known","meeting-for-learning"]},
{"no":"09","eyebrow":"PARADOX","title":"成熟不总是选对一边","question":"我能否让两种都真实的东西，同时留在眼前？","body":"独处与共同体、自由与纪律、沉思与行动、现实与可能——帕尔默经常把重要问题放进悖论之中。“悖论”（paradox）并不是含糊，也不是拒绝判断；它要求我们扩大能够承载复杂性的空间，不让恐惧逼着我们过早消灭其中一端。很多真正的决定，只有在张力被承载一段时间之后，才会显出更有生命力的方向。","visual":"paradox","links":["paradox","tragic-gap","active-life"],"books":["courage-to-teach","active-life"]},
{"no":"10","eyebrow":"DIVIDED NO MORE","title":"如果已经知道什么是真实的，接下来怎么办？","question":"我愿不愿意让内在知道的东西，进入一个可以承担后果的现实行动？","body":"“不再分裂”不是一次戏剧性的宣言，也不是从此毫无矛盾。它意味着停止长期参与自己的缩小：在工作、关系或制度中，逐渐把已经认出的真实带回行动。帕尔默很重视支持性的共同体，因为真正的完整性并不是个人英雄主义；人需要关系来帮助自己在风险、失败与反作用中持续学习。","visual":"whole","links":["undivided-life","active-life","nonviolence"],"books":["hidden-wholeness","courage-to-teach"]},
{"no":"11","eyebrow":"PUBLIC LIFE","title":"从“我是谁”走向“我们怎样共同生活”","question":"我的内在生命，正在帮助共同创造一个怎样的世界？","body":"帕尔默的思想最终并不是一条向内撤退的道路。相反，他不断把完整性推向教育、领导、组织、陌生人关系与公共生活。一个人越能承载自己的恐惧、张力与不确定性，越有可能在差异中保留声音而不把对方去人化。内在工作在这里接受最重要的检验：它是否让我们更能进入现实，而不是更擅长躲开现实。","visual":"public","links":["public-life","tragic-gap","nonviolence"],"books":["company-of-strangers","healing-democracy","going-public"]}
]

world_title_lines={
"01":("我们为什么会","变得分裂？"),
"02":("第一步不是","急着改变，","而是重新聆听"),
"03":("真实自我，","不是理想自我"),
"04":("使命，","不是职业规划"),
"05":("完整性，","不是“永远一致”"),
"06":("内在的路，要自己走，","却很难独自走完"),
"07":("我们怎样认识世界，","也在塑造","怎样与世界相处"),
"08":("教育的中心，","既不是教师，","也不是学生"),
"09":("成熟，","不总是选对一边"),
"10":("当我已经知道","什么是真实的，","接下来怎么办？"),
"11":("从“我是谁”，","走向“我们如何","共同生活”")
}

world_real={
"01":"你在会议里一次次说“都可以”，身体却持续收紧；你在职业角色里表现熟练，却越来越难回答“这真的是我愿意参与的吗？”——分裂常以这种日常、可维持的方式存在。",
"02":"当一个选择被十几种建议包围时，帕尔默式的第一步往往不是再找一个意见，而是创造一段不必马上回应的时间，观察哪些念头、身体反应与关切反复回来。",
"03":"一个人可能很擅长某件事，却长期被它耗尽；也可能在某些不被评价的活动中自然投入、忘记时间。“真实自我”的线索，往往就藏在这些“更有生命 / 更失去生命”的差异里。",
"04":"职业、关系或项目中的“路关闭”，不必被浪漫化成命运安排，但它可以成为信息：什么不属于我？什么限制需要承认？什么关切即使失败后仍然会回来？",
"05":"完整性很少从“把人生全部重做”开始。更常见的是在一次会议、一段关系、一个边界里，让自己真正知道的东西多出现一点，让角色与真实之间的距离缩小一点。",
"06":"当朋友陷入困境时，我们很容易迅速给建议、解释原因、讲自己的类似经历。可信赖共同体训练的是另一种能力：陪伴一个人继续拥有他自己的问题。",
"07":"在教育、管理或帮助行业里，知识很容易变成标签：这个学生“缺乏动力”、这个同事“抗拒改变”。关系性的认识会追问：我的分类让我看见了什么，又让我看不见什么？",
"08":"如果一堂课所有问题最终都回到“老师想听什么”，教师仍是中心；如果只回到“学生喜欢什么”，学生成了中心。“主题中心”的问题是：这个主题本身正在要求我们认真面对什么？",
"09":"“我需要独处”与“我需要共同体”可能同时是真的；“现实很糟”与“仍值得行动”也可能同时是真的。承载悖论，是在行动之前不急着把一半现实删掉。",
"10":"不再分裂有时只是一次小小的“不再配合”：说出一个保留意见、拒绝一个持续伤害自己的安排、为真正重视的工作腾出时间。重点不是戏剧性，而是可持续地让内外重新连接。",
"11":"公共生活不只发生在选举与宏大议题里。家庭会议、学校、团队、社区、邻里和与陌生人的相处，都是练习“既保留自己的声音，又不把对方变成敌人”的地方。"
}

def world_visual(kind):
    return {
        "split":svg_split_whole(),"inner":svg_inner_teacher(),"tree":svg_tree(),"paths":svg_paths(),
        "integrity":svg_integrity(),"whole":svg_mobius(),"community":svg_community(),"knowing":svg_knowing(),
        "subject":svg_subject_centered(),"paradox":svg_paradox(),"public":svg_public()
    }[kind]

world_sections=""
for ch in world_chapters:
    concept_links='<i>→</i>'.join(f'<a href="../concepts/{s}.html">{concept_lookup[s]["cn"]}</a>' for s in ch["links"])
    book_links=''.join(f'<a class="badge" href="../books/{s}.html">{next((b["zh"] for b in books if b["slug"]==s),s)}</a>' for s in ch["books"])
    title_html=sem_title(*world_title_lines[ch["no"]])
    extra=""
    if ch["no"]=="06":
        extra=f'''<div class="externalCta"><div><span class="tag">深入专题</span><h3>《内在之光》与信任圈不在主站重复展开</h3><p>11 条基石、澄心会、第三物、信任圈历史与实践流程，统一进入独立专题网站。</p></div><a class="btn" href="{CIRCLE_SITE}" target="_blank" rel="noopener">进入信任圈专题 ↗</a></div>'''
    world_sections+=f'''<section class="worldChapter" id="chapter-{ch["no"]}"><div class="shell"><div class="chapterGrid"><div class="chapterText"><span class="chapterNo">{ch["no"]} · {ch["eyebrow"]}</span><h2>{title_html}</h2><div class="coreQuestion">{ch["question"]}</div><p>{ch["body"]}</p><div class="practiceBox"><span class="tag">现实中怎样看见</span><p>{world_real[ch["no"]]}</p></div><div class="conceptTrail">{concept_links}</div><div class="mini">主要文本：{book_links}</div>{extra}</div><div class="visualPanel">{world_visual(ch["visual"])}</div></div></div></section>'''

world=f'''<main>{crumbs(1,[("思想总图",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Parker J. Palmer · Worldview</div><h1>{sem_title("从“我是谁”，","走向<em>“我们怎样共同生活”</em>")}</h1><p class="lead">帕尔默的写作跨越使命、教育、灵性、共同体、领导与民主。把书名一个个看，它们似乎分散；沿着更深的一条线来看，他几十年来持续探索的是同一个问题：<strong>我们怎样从分裂走向完整，并让这份完整进入真实世界？</strong></p><div class="actions"><a class="btn primary" href="#map">从总图开始</a><a class="btn" href="../parker-palmer/">先认识帕尔默</a></div><div class="heroFoot">阅读建议：不要把 11 个节点当成线性等级。它们更像彼此往返、互相检验的生命运动。</div></div></div></section>
<section class="section" id="map"><div class="shell"><div class="head wideHead"><div><span class="kicker">The Whole Map</span><h2>{sem_title("帕尔默关心的，","不只是“自我成长”，而是怎样活得更完整")}</h2></div><p>只有把每个概念放回“内在—关系—认识—行动—公共生活”的往返运动中，才能看见它在整套思想里的位置。</p></div><div class="visualPanel" style="min-height:500px">{svg_mobius()}<div class="pathwayFlow" style="width:100%;margin-top:18px"><div class="flowNode"><b>分裂</b><small>Divided Life</small></div><div class="flowNode"><b>聆听</b><small>Inner Teacher</small></div><div class="flowNode"><b>辨识</b><small>True Self · Vocation</small></div><div class="flowNode"><b>关系</b><small>Community · Knowing</small></div><div class="flowNode"><b>承载</b><small>Paradox · Tension</small></div><div class="flowNode"><b>进入世界</b><small>Divided No More · Public Life</small></div></div></div></div></section>
{world_sections}
<section class="section"><div class="shell"><div class="questionBand"><span class="kicker">A Reading Key</span><h2>{sem_title("不要把帕尔默","读成一组漂亮句子")}</h2><p>他的思想有一条清楚的内在脉络：<strong>内在分辨 → 完整生命 → 教育与关系 → 共同体 → 公共世界。</strong> 越深入内在，越需要返回现实；越进入公共世界，越需要能够承载自己的恐惧、限制与张力。</p><div class="actions"><a class="btn primary" href="../concepts/network.html">打开知识关系图</a><a class="btn" href="../books/">进入原著地图</a><a class="btn" href="../self-study/practice-now.html">做一个十分钟练习</a></div></div></div></section>
</main>'''
(ROOT/"worldview/index.html").write_text(wrap("思想总图",world,1,"深入理解帕克·帕尔默从分裂生命、内在导师、真实自我与使命，到教育、悖论、不再分裂与公共生活的完整思想结构"),encoding="utf-8")

principles=[
("01","每个人都有内在导师","Inner teacher",["inner-teacher","soul"]),
("02","内在工作既需要独处，也需要共同体","Solitude + community",["trustworthy-community","inner-teacher"]),
("03","内在工作必须以邀请为前提","Invitation",["trustworthy-community","honest-open-questions"]),
("04","生命像季节一样有周期","Seasonal cycles",["seasons","vocation"]),
("05","欣赏悖论，让我们能承载更大的复杂性","Paradox",["paradox","tragic-gap"]),
("06","当我们完整地看自己，才能活得更有完整性","Integrity",["wholeness","identity-integrity"]),
("07","生命底层存在一种“隐藏的完整性”","Hidden wholeness",["wholeness","undivided-life"])
]
principle_cards=""
for n,zh,en,slugs in principles:
    principle_cards+=f'<div class="card"><span class="tag">{n}</span><h3>{zh}</h3><p>{en}</p><div class="mini">'+''.join(f'<a class="badge" href="../concepts/{s}.html">{concept_lookup[s]["cn"]}</a>' for s in slugs)+'</div></div>'
cr_page=f'''<main>{crumbs(1,[("思想总图","index.html"),("Courage & Renewal 实践框架",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">From Palmer to Courage & Renewal</div><h1>{sem_title("思想如何成为","<em>可以反复实践的结构</em>")}</h1><p class="lead">今天的 Center for Courage & Renewal 把帕尔默长期发展的思想整理为价值、基石、原则与实践。这里把其中七条原则与本站概念网络对接，帮助看见“思想 → 空间条件 → 实践”的连续性。</p><div class="heroFoot">这是对 Courage & Renewal 当前实践框架的整理，并不意味着这七条原则原封不动地来自帕尔默某一本著作。</div></div></div></section><section class="section"><div class="shell"><div class="grid2">{principle_cards}</div></div></section><section class="section"><div class="shell"><div class="questionBand"><h2>{sem_title("为什么这套框架","也适用于自修？")}</h2><p>因为自修不该只是“我一个人看内容”。帕尔默所说的内在工作需要独处，也需要关系；需要邀请，而不是强迫；需要季节和悖论的节律；最后还要回到完整性与现实世界。因此本站把计时器、自由书写、第三物、开放问题、个人记录与知识关系放在同一系统里，而不是做成六个互不相干的小工具。</p><div class="actions"><a class="btn primary" href="../self-study/">进入自修中心</a><a class="btn" href="https://couragerenewal.org/courage-renewal-approach/" target="_blank" rel="noopener">查看官方实践框架 ↗</a></div></div></div></section></main>'''
(ROOT/"worldview/courage-renewal.html").write_text(wrap("Courage & Renewal 实践框架",cr_page,1),encoding="utf-8")

# ---------- genealogy ----------
gene=f'''<main>{crumbs(1,[("思想谱系",None)])}<section class="hero"><div class="shell heroGrid"><div class="heroMain"><div class="eyebrow">Genealogy</div><h1>{sem_title("思想不是凭空出现的，","它有自己的<em>生命史</em>")}</h1><p class="lead">帕尔默的思想语言生长在社会学、社区行动、Pendle Hill 的贵格会共同体、Thomas Merton、Henri Nouwen、教育实践与公共参与之间。</p><div class="heroFoot">这一页帮助理解：为什么“内在之光、静默聚会、完整性、共同体”等词，在帕尔默那里并不是泛化的灵性标签。</div></div><div class="heroSide"><div class="visualPanel">{svg_influences()}</div></div></div></section>
<section class="section"><div class="shell"><div class="grid2">
<div class="card"><span class="tag">Sociology</span><h3>社会学与公共世界</h3><p>早期社会学训练与社区工作，使帕尔默从一开始就关心制度、差异与社会现实，而不是把灵性缩回私人领域。</p></div>
<div class="card"><span class="tag">Pendle Hill</span><h3>从二手信念回到亲身经验</h3><p>贵格会的共同生活、工作、学习与静默让他开始追问：哪些只是“听来的”，哪些是自己真实活过、能够从经验中说出的？</p></div>
<div class="card"><span class="tag">Quaker Meeting</span><h3>Meeting 作为求真结构</h3><p>在《Meeting for Learning》中，worship、business 与 learning 共享一种姿态：停止追赶，等待真理在共同体中显现。</p></div>
<div class="card"><span class="tag">Thomas Merton</span><h3>隐藏的完整性</h3><p>Merton 为帕尔默提供了一个重要意象：在表面破碎之下，仍存在更深的完整与连结。</p></div>
<div class="card"><span class="tag">Henri Nouwen</span><h3>教育、共同体与内在生命</h3><p>帕尔默后来回忆，Nouwen 对自己理解 Merton、教育与共同体等主题有重要影响。</p></div>
<div class="card"><span class="tag">Education</span><h3>从“教什么”到“谁在教”</h3><p>教师身份、恐惧、完整性、主题中心与共同体逐渐形成他最有影响力的教育思想。</p></div>
<div class="card"><span class="tag">Courage & Renewal</span><h3>把思想变成关系结构</h3><p>信任圈、基石、第三物与澄心会把“尊重灵魂”转成可操作的群体实践。</p></div>
<div class="card"><span class="tag">Public Life</span><h3>内在工作进入公共世界</h3><p>从《The Company of Strangers》到《Healing the Heart of Democracy》，他持续把完整性、陌生人、张力和公共空间连接起来。</p></div>
</div></div></section></main>'''
(ROOT/"genealogy/index.html").write_text(wrap("思想谱系",gene,1),encoding="utf-8")

# ---------- Parker Palmer profile ----------
timeline_html=""
for item in PALMER["timeline"]:
    timeline_html+=f'''<div class="timelineItem reveal"><div class="timelineDot"></div><div class="timelineBody"><div><span class="tag">{item["stage"]}</span><h3>{item["title"]}</h3><p>{item["text"]}</p></div><div class="timelineVisual">{timeline_visual(item["visual"])}</div></div></div>'''

influence_html=""
for item in PALMER["influences"]:
    concept_badges=''.join(f'<a class="badge" href="../concepts/{s}.html">{concept_lookup[s]["cn"]}</a>' for s in item["concepts"] if s in concept_lookup)
    influence_html+=f'''<div class="influenceNode reveal"><span class="tag">{item["title"]}</span><h3>{item["cn"]}</h3><p>{item["text"]}</p><div class="mini">{concept_badges}</div></div>'''

book_river=""
for item in PALMER["books"]:
    b=next((x for x in books if x["slug"]==item["slug"]),None)
    zh=b["zh"] if b else item["title"]
    book_river+=f'<a class="bookStep" href="../books/{item["slug"]}.html"><span>{item["title"]}</span><strong>{zh}</strong><span>{item["question"]}</span></a>'

palmer_page=f'''<main>{crumbs(1,[("帕克·帕尔默",None)])}
<section class="hero"><div class="shell"><div class="portraitHero"><div class="heroMain"><div class="eyebrow">Parker J. Palmer</div><h1>{sem_title("一个不断把思想","<em>带回生命的人</em>")}</h1><p class="lead">教师 · 作家 · 教育思想家 · 公共知识分子。理解帕尔默，不能只从概念开始。他的许多思想，都从亲身经历过的矛盾、共同体、静默、失败、诗歌与重新开始中长出来。</p><div class="actions"><a class="btn primary" href="biography.html">阅读详细传记</a><a class="btn" href="#life">看思想形成线</a><a class="btn" href="../worldview/">进入思想总图</a></div></div><div class="heroSide"><figure class="portraitFrame"><img src="../assets/images/parker-j-palmer.jpg" alt="Parker J. Palmer 2010 年肖像"><figcaption class="credit">Sharon L. Palmer 摄，2010 · CC BY-SA 3.0 · Wikimedia Commons</figcaption></figure></div></div></div></section>

<section class="section"><div class="shell"><div class="head"><div><span class="kicker">A Life Behind The Ideas</span><h2>{sem_title("不是先有一套理论，","然后再拿去生活")}</h2></div><p>Elena Soto 的研究把帕尔默的生命经历与教育思想放在同一条线上：他的写作，来自长期追寻真实与完整的生命实践，而不是一套脱离经验、先行完成的理论体系。</p></div><div class="storyGrid"><div><p class="storyLead">帕尔默曾在学术、教学与社区工作中追求改变，也逐渐发现：一个人可以在理念上谈“共同体”，却还没有真正学会怎样与人共同生活；可以非常擅长外在角色，却越来越远离自己。Pendle Hill 的长期共同生活，让工作、学习、静默、诗歌与非暴力从思想变成日常经验。</p><p class="storyLead">后来，他把问题一再带回教育：如果教学是一项真正的人类活动，那么教师的内在状态也会进入课堂。再往后，这条线继续进入领导、公共生活与民主——完整性从来不只是私人的。</p><div class="sourceNote">人物与思想脉络主要参考：Elena Soto, <em>The Spiritual and Educational Vision of Parker J. Palmer: The Birthright Gift of Self</em>；概念解释同时回到帕尔默原著。</div></div><div class="visualPanel">{svg_mobius()}</div></div></div></section>

<section class="section" id="life"><div class="shell"><div class="head"><div><span class="kicker">Life → Thought</span><h2>{sem_title("思想如何","从生命经历中长出来")}</h2></div><p>这里不是一篇完整传记，而是一条“思想形成线”：哪些经历使帕尔默后来不断回到真实自我、完整性、共同体、悖论与公共生活这些主题。</p></div><div class="timeline">{timeline_html}</div></div></section>

<section class="section"><div class="shell"><div class="head"><div><span class="kicker">Five Sources</span><h2>五个重要影响来源</h2></div><p>这些不是简单的“师承名单”。它们分别改变了帕尔默对认识、静默、共同体、隐喻和社会行动的理解。</p></div><div class="influenceMap">{influence_html}</div></div></section>

<section class="section" id="mobius"><div class="shell"><div class="storyGrid"><div><span class="kicker">The Quaker PowerPoint</span><h2 style="font-size:clamp(32px,4vw,50px);line-height:1.4;margin:10px 0 18px">{sem_title("莫比乌斯带：","理解帕尔默思想的重要入口")}</h2><p class="storyLead">帕尔默用一条扭转后首尾相接的纸带来说明内在生命与外在世界的关系：沿着它一直走，你无法找到明确的“这一面是内在、另一面是外在”。里面的东西不断流向世界，世界也不断进入我们里面。</p><p class="storyLead">这使“内在工作”获得完全不同的意义：它不是逃离世界的避难所，而是在参与现实之前，学习辨认自己正在把什么带进现实。</p><div class="conceptTrail"><a href="../concepts/wholeness.html">隐藏的完整性</a><i>→</i><a href="../concepts/identity-integrity.html">身份与完整性</a><i>→</i><a href="../concepts/public-life.html">公共生活</a></div></div><div class="visualPanel">{svg_mobius()}</div></div></div></section>

<section class="section"><div class="shell"><div class="head"><div><span class="kicker">Education</span><h2>{sem_title("教育思想：","问题不只是“怎样教”")}</h2></div><p>帕尔默对教育思想的重要贡献之一，是把常被忽略的“教师这个人”重新带回教学讨论。学生与学科都很复杂，而教师的身份、恐惧、完整性和内在生命同样会进入课堂。</p></div><div class="storyGrid"><div class="visualPanel">{svg_subject_centered()}</div><div><div class="quote">我们不仅用方法教学，也用“自己是谁”在教学。</div><p>这不是否定教学技术，而是把技术放回一个更大的问题：什么样的方法与你的身份、学科和学生形成真实关系？Soto 特别指出，帕尔默所说的“身份”与“完整性”并不只包含一个人的长处，也包括限制、经历与阴影；更诚实地认识自己，是更真实地看见学生与学科的重要前提。</p><div class="grid2" style="margin-top:20px"><div class="card"><span class="tag">IDENTITY</span><h3>我是谁</h3><p>构成我的天赋、历史、恐惧、限制与价值。</p></div><div class="card"><span class="tag">INTEGRITY</span><h3>我怎样活</h3><p>让这些真实力量彼此形成更有生命力的关系。</p></div><div class="card"><span class="tag">SUBJECT</span><h3>我们面对什么</h3><p>把值得学习的主题重新放在共同中心。</p></div><div class="card"><span class="tag">COMMUNITY</span><h3>我们怎样一起寻找</h3><p>让认识发生在关系中，而不是只做信息传递。</p></div></div></div></div></div></section>

<section class="section"><div class="shell"><div class="head"><div><span class="kicker">Books As A Journey</span><h2>{sem_title("主要著作，","其实都在接力追问同一件事")}</h2></div><p>从认识、行动、教学、使命、完整性到公共生活，讨论的范围不断扩大，但同一个问题始终在场：内在真实怎样进入外在世界？</p></div><div class="bookRiver">{book_river}</div><div class="quote" style="margin-top:30px">六本书可以被读成同一条长线：<strong>怎样让内在真实进入外在世界。</strong></div></div></section>

<section class="section"><div class="shell"><div class="questionBand"><span class="kicker">Continue</span><h2>{sem_title("从“这个人”，","继续进入“这套思想”")}</h2><p>人物页帮助你理解这些概念为什么会出现；思想总图则把它们重新放回从“分裂的生命”到公共生活的整体脉络中。</p><div class="actions"><a class="btn primary" href="../worldview/">进入思想总图</a><a class="btn" href="../books/">浏览原著地图</a><a class="btn" href="../genealogy/">继续看思想谱系</a></div></div></div></section>
</main>'''
(ROOT/"parker-palmer/index.html").write_text(wrap("帕克·帕尔默",palmer_page,1,"从生命经历、Pendle Hill、Thomas Merton、贵格会传统、教育思想与代表著作认识 Parker J. Palmer"),encoding="utf-8")

# ---------- detailed Parker J. Palmer biography ----------
bio_book_river=""
for item in PALMER["books"]:
    b=next((x for x in books if x["slug"]==item["slug"]),None)
    zh=b["zh"] if b else item["title"]
    bio_book_river+=f'<a class="bookStep" href="../books/{item["slug"]}.html"><span>{item["title"]}</span><strong>{zh}</strong><span>{item["question"]}</span></a>'

bio_page=f'''<main>{crumbs(1,[("帕克·帕尔默","index.html"),("详细传记",None)])}
<section class="hero bioHero"><div class="shell"><div class="portraitHero"><div class="heroMain"><div class="eyebrow">Biography · Parker J. Palmer</div><h1>{sem_title("走近帕克·帕尔默，","<em>看见思想背后的生命</em>")}</h1><p class="lead">1939 年出生于芝加哥的帕克·J·帕尔默，后来成为美国重要的教育思想家、作家、演讲者与社会行动者。他的道路并不笔直：离开神学院、对学术世界的疏离、共同体生活、抑郁的黑夜、贵格会静默、教育实践与公共行动，一次次使他重新回答同一个问题：<strong>我是谁？我怎样活得不再分裂？</strong></p><div class="actions"><a class="btn primary" href="#story">从生命故事开始</a><a class="btn" href="../worldview/">进入思想总图</a><a class="btn" href="index.html">回到人物页</a></div></div><div class="heroSide"><figure class="portraitFrame"><img src="../assets/images/parker-j-palmer.jpg" alt="Parker J. Palmer 2010 年肖像"><figcaption class="credit"><a href="https://commons.wikimedia.org/wiki/File:Parker_J._Palmer.jpg" target="_blank" rel="noopener">Sharon L. Palmer 摄，2010</a> · CC BY-SA 3.0 · Wikimedia Commons</figcaption></figure></div></div></div></section>

<section class="section" id="story"><div class="shell"><div class="bioIntro"><div><span class="kicker">The Person Before The Ideas</span><h2>{sem_title("先认识这个人，","再理解他的思想")}</h2><p class="storyLead">如果只读帕尔默的概念，很容易把“真实自我”“内在导师”“完整性”“可信赖共同体”理解成一套成熟理论。但从他的生命往回看，会发现这些词几乎都带着经历的痕迹：它们不是从书桌上凭空出现，而是在选择、失望、关系、静默、黑夜与重新开始中慢慢长出来。</p><p>Elena Soto 对帕尔默生命与教育思想的系统研究特别强调这一点：他的思想史，同时也是一部不断学习“怎样成为自己”的生命史。官方资料则显示，他后来成为 Center for Courage & Renewal 的创始人与荣休高级合伙人，长期工作横跨教育、共同体、领导力、灵性与社会变革。</p></div><div class="bioFacts"><div class="bioFact"><b>出生</b><span>1939 年<br>美国芝加哥</span></div><div class="bioFact"><b>学术训练</b><span>Carleton College<br>UC Berkeley 社会学博士</span></div><div class="bioFact"><b>实践传统</b><span>贵格会<br>Religious Society of Friends</span></div><div class="bioFact"><b>长期主题</b><span>教育 · 使命 · 共同体 · 完整性 · 公共生活</span></div></div></div></div></section>

<section class="section"><div class="shell"><div class="bioMilestones"><div class="bioMilestone"><b>10</b><span>本主要著作，横跨教育、灵性、领导与公共生活</span></div><div class="bioMilestone"><b>2.5M+</b><span>官方资料所列累计销量超过 250 万册</span></div><div class="bioMilestone"><b>10</b><span>种语言译本，影响跨出英语世界</span></div><div class="bioMilestone"><b>14</b><span>个荣誉博士学位，另获多项教育与公共领域荣誉</span></div></div><div class="bioNav" style="margin-top:22px"><a href="#early"><small>1939–1961</small><strong>芝加哥与 Carleton</strong></a><a href="#turning"><small>1961–1969</small><strong>神学院与 Berkeley</strong></a><a href="#pendle"><small>1974–1985</small><strong>Pendle Hill</strong></a><a href="#teaching"><small>1980s–2000s</small><strong>教育与写作</strong></a><a href="#public-life"><small>Later Years</small><strong>公共生活与晚年</strong></a></div></div></section>

<section class="bioChapter" id="early"><div class="shell"><div class="bioChapterGrid"><div class="bioText"><span class="bioYear">1939–1961 · Chicago → Carleton</span><h2>{sem_title("一个并不把自己","想成“思想家”的年轻人")}</h2><p>帕尔默出生于芝加哥，在伊利诺伊州北郊长大。进入 Carleton College 后，他最初并没有一条明确的“思想家”路线。按 Soto 的研究，他来自一个以商人和手艺人为主的家庭，是家中第一位大学毕业生；早年甚至想过海军与广告行业。</p><p>真正改变他的，是几位老师。在 Carleton，他同时学习哲学与社会学，逐渐发现，好的教育不只是把知识交给学生，而是有人以自己的完整性，让另一个人开始相信：我也可以长成自己的样子。后来他反复写“教师是谁”，很大程度上可以追溯到这些早年的师生关系。</p><div class="bioPull">他后来关于“身份与完整性”的教育思想，最早并不是一个抽象命题，而是来自被好老师真实看见的经验。</div></div><figure class="bioMedia"><img src="../assets/images/biography/carleton-skinner-chapel.jpg" alt="Carleton College 的 Skinner Memorial Chapel"><figcaption class="credit"><a href="https://commons.wikimedia.org/wiki/File:Skinner_Memorial_Chapel_-_Carleton_College_-_Northfield,_Minnesota_(25932797228).jpg" target="_blank" rel="noopener">Skinner Memorial Chapel, Carleton College</a> · Tony Webster 摄 · CC BY-SA 2.0</figcaption></figure></div></div></section>

<section class="bioChapter reverse" id="turning"><div class="shell"><div class="bioChapterGrid"><div class="bioText"><span class="bioYear">1961–1969 · Seminary → Berkeley</span><h2>{sem_title("当一条路关上，","使命开始换一种方式说话")}</h2><p>大学毕业后，帕尔默进入纽约 Union Theological Seminary，一度相信自己将走向牧职。但持续的不协调感，使他逐渐意识到：成为牧师并不是自己的道路。后来他转往加州大学伯克利分校攻读社会学，把兴趣放在宗教、制度与社会生活之间的关系上。</p><p>这段经历后来成为《让生命说话》中“路打开 / 路关闭”的重要底色：使命不是靠意志替自己设计一个宏大身份，也包括认真听见那些“不适合我”的讯号。伯克利时期，他研究宗教象征与社会变迁，也与 Robert Bellah 等学者工作，最终完成社会学博士训练。</p></div><div class="bioMedia"><div class="visualPanel">{svg_paths()}</div></div></div></div></section>

<section class="bioChapter" id="georgetown"><div class="shell"><div class="bioChapterGrid"><div class="bioText"><span class="bioYear">Late 1960s–1974 · Teaching · Community Organizing · Georgetown</span><h2>{sem_title("从“研究社会”，","走向真实的社会关系")}</h2><p>帕尔默并没有满足于留在学院里研究社会。他投入社区组织工作，面对种族、城市与制度问题；随后进入 Georgetown University 任教。Soto 的研究显示，这一阶段他越来越强烈地感到学术世界中的孤立，也越来越渴望一种能把工作、家庭、关系与价值重新连起来的共同生活。</p><p>这也是一个关键转折：他开始发现，“共同体”不能只是课堂里谈论的概念。一个人如果自己还没有真正生活在共同体里，就很难诚实地教别人什么是共同体。</p></div><figure class="bioMedia"><img src="../assets/images/biography/georgetown-healy-hall.jpg" alt="Georgetown University 的 Healy Hall"><figcaption class="credit"><a href="https://commons.wikimedia.org/wiki/File:Healy_Hall_at_Georgetown_University.jpg" target="_blank" rel="noopener">Healy Hall, Georgetown University</a> · Gtownsfs 摄 · CC BY-SA 3.0</figcaption></figure></div></div></section>

<section class="bioChapter reverse" id="pendle"><div class="shell"><div class="bioChapterGrid"><div class="bioText"><span class="bioYear">1974–1985 · Pendle Hill</span><h2>{sem_title("十一年共同生活，","成为他真正的“隐形学校”")}</h2><p>1974 年，帕尔默带着家人来到宾夕法尼亚州 Wallingford 的 Pendle Hill——一个贵格会生活与学习共同体。原本只是一次休假式停留，后来却成为长达十一年的生命时期。他担任 Dean of Studies，也和其他居民一起学习、劳动、吃饭、礼拜与生活。</p><p>每天的静默聚会一开始让他不适。他习惯的是讲道、解释、思想与语言，而贵格会把人放进没有主持人、没有预设答案的共同静默里。正是在这种静默中，他开始区分：哪些信念只是“听来的”，哪些东西真正从自己的经验里长出来。后来“内在导师”“可信赖空间”“不替别人修理人生”的关系伦理，都与这段生活密不可分。</p><div class="sourceNote">Pendle Hill 是帕尔默思想形成的重要现场：日常劳动、共同吃饭、学习与静默并不是课程之外的背景，而本身就是教育。</div></div><figure class="bioMedia"><img src="../assets/images/biography/pendle-hill-barn.jpg" alt="Pendle Hill 位于宾夕法尼亚州 Wallingford 的建筑"><figcaption class="credit"><a href="https://commons.wikimedia.org/wiki/Category:Quakers_in_Pennsylvania" target="_blank" rel="noopener">Pendle Hill, Wallingford, Pennsylvania</a> · Smallbones 摄 · CC0</figcaption></figure></div></div></section>

<section class="bioChapter" id="influences"><div class="shell"><div class="bioChapterGrid"><div class="bioText"><span class="bioYear">Thomas Merton · Henri Nouwen · Quaker Silence</span><h2>{sem_title("静默不是退避，","而是重新学习从哪里出发")}</h2><p>在 Pendle Hill 前后，帕尔默持续深入 Thomas Merton 的作品，也与 Henri Nouwen 建立长期友谊与合作。Merton 关于真实自我、静默、独处与隐藏完整性的语言，为他提供了重要思想资源；Nouwen 则在教育、共同体与灵性生命上持续影响他。</p><p>帕尔默后来常把内在生命画成莫比乌斯带：内与外并不是两个彼此隔绝的世界。我们里面的恐惧、希望、阴影与爱，会不断进入关系和制度；外部世界也持续进入我们里面。所谓“内在工作”，不是把世界关在门外，而是更诚实地辨认：我正在把什么带进世界？</p></div><div class="bioMedia"><div class="visualPanel">{svg_mobius()}</div></div></div></div></section>

<section class="bioChapter reverse" id="dark-night"><div class="shell"><div class="bioChapterGrid"><div class="bioText"><span class="bioYear">Dark Nights · Depression</span><h2>{sem_title("生命的黑夜，","也进入了他的思想")}</h2><p>帕尔默曾公开谈到自己经历严重的临床抑郁。Soto 的研究也把这些经历视为理解他后来思想的重要线索。这里不把抑郁浪漫化成“灵性成长”，而只是尊重他本人反复公开讲述的事实：那是一段自我感、价值感与意义感几乎被掏空的生命黑夜。</p><p>这段生命史让他的“灵魂”语言有了完全不同的重量：真正的陪伴不是急着劝说一个人振作，也不是替他解释，而是在不入侵、不接管的前提下，帮助一个人慢慢重新和生命建立联系。后来信任圈里那种克制、尊重与“不修理别人”的伦理，也因此不只是技巧。</p><div class="sourceNote">本节依据帕尔默本人公开自述与 Soto 的研究整理，不对其健康状况作额外推断。</div></div><div class="bioMedia"><div class="visualPanel">{svg_inner_teacher()}</div></div></div></div></section>

<section class="bioChapter" id="teaching"><div class="shell"><div class="bioChapterGrid"><div class="bioText"><span class="bioYear">1980s–2000s · Writer · Teacher of Teachers</span><h2>{sem_title("从“怎样教”，","转向“谁在教”")}</h2><p>离开 Pendle Hill 后，帕尔默的写作逐渐进入更广泛的教育世界。《To Know as We Are Known》讨论认识与关系，《The Active Life》重新连接行动与沉思，而《The Courage to Teach》则把一个问题推到教育讨论中心：好的教学是否可以只靠技巧？</p><p>他的回答是否定的。教学当然需要方法，但教师会把自己的恐惧、身份、完整性，以及与学科的关系一起带进课堂。1998 年，一项覆盖 10,000 名教育工作者的全国调查把他列为美国高等教育中最有影响力的资深领导者之一。自 2002 年起，ACGME 还以他的名字设立 “Courage to Teach” 与 “Courage to Lead” 奖项，把这种“内在完整性进入专业实践”的思想带进医学教育。</p></div><div class="bioMedia"><div class="visualPanel">{svg_subject_centered()}</div></div></div></div></section>

<section class="bioChapter reverse" id="courage"><div class="shell"><div class="bioChapterGrid"><div class="bioText"><span class="bioYear">1997–Present · Courage & Renewal</span><h2>{sem_title("让思想“长出轮子”，","进入真实的人与组织")}</h2><p>帕尔默不希望自己的思想只停在书架上。1997 年，他与 Marcy Jackson、Rick Jackson 一起创立了后来成为 Center for Courage & Renewal 的组织。最早的 Courage to Teach 项目帮助教师重新连接“灵魂与角色”；后来这一方法逐渐进入医疗、宗教、非营利、领导与社会行动等领域。</p><p>官方页面里，他把自己的“遗产”理解成一件共同完成的事：重要的不是写过多少页，而是这些思想有没有被人带进自己的生命、共同体、机构与社会。也正因此，他的影响既是一套思想，也是一种实践传统。</p></div><div class="bioMedia"><div class="visualPanel">{svg_integrity()}</div></div></div></div></section>

<section class="bioChapter" id="public-life"><div class="shell"><div class="bioChapterGrid"><div class="bioText"><span class="bioYear">Public Life · Democracy · Aging</span><h2>{sem_title("越往内走，","越要重新回到世界")}</h2><p>帕尔默后期的写作越来越明确地进入公共生活。《Healing the Heart of Democracy》讨论政治分裂、差异与公民心灵；《On the Brink of Everything》则把视线转向老年、失去、爱与生命回望。但这并不是离开早期主题，而是把“完整性”推向更大的尺度。</p><p>一个人能不能在差异中保留自己的声音，又不把对方变成敌人？能不能承载悲剧性张力，而不是急着消灭其中一端？能不能让内在真实进入公共世界，却不把“内在”变成逃避现实的理由？这些问题，让帕尔默从教育思想家逐渐成为一个持续讨论公共生活的人。</p></div><div class="bioMedia"><div class="visualPanel">{svg_public()}</div></div></div></div></section>

<section class="section" id="legacy"><div class="shell"><div class="head wideHead"><div><span class="kicker">Influence & Legacy</span><h2>{sem_title("他的影响，不只留在书里，","而是进入教育、医疗与公共生活")}</h2></div><p>帕尔默晚年谈“遗产”时，刻意不把它理解成个人成就。他更在意的是：这些思想有没有被别人带进自己的生命，再继续带进共同体、机构与更大的社会。</p></div><div class="grid4">
<div class="card"><span class="tag">1998</span><h3>高等教育中的影响力</h3><p>Center for Courage & Renewal 的官方资料记载，一项覆盖 10,000 名教育工作者的全国调查，把帕尔默列为高等教育中最有影响力的资深领导者之一，并列入过去十年的关键“议题设定者”。</p></div>
<div class="card"><span class="tag">2002—Today</span><h3>ACGME 以他的名字设奖</h3><p>美国毕业后医学教育认证委员会持续颁发 Parker J. Palmer “Courage to Teach” 与 “Courage to Lead” 奖，把他的教育与领导思想带进医学训练体系。</p><a class="externalLink" href="https://www.acgme.org/initiatives/awards/parker-j-palmer-courage-to-teach-award/" target="_blank" rel="noopener">查看 ACGME 奖项 ↗</a></div>
<div class="card"><span class="tag">2010 · 2017 · 2021</span><h3>跨越教育与沉思传统的荣誉</h3><p>他先后获得 William Rainey Harper Award、Shalem Institute 的 Contemplative Voices Award，以及 Freedom of Spirit Fund 的终身成就奖。</p></div>
<div class="card"><span class="tag">Legacy</span><h3>“这不是我的遗产，是我们的”</h3><p>在官方人物页中，帕尔默把真正的遗产理解为一种活的传递：人们把文字带进自己的生命，再带进共同体、机构和社会。如今他与妻子 Sharon 居住在威斯康星州 Madison。</p></div>
</div></div></section>

<section class="section"><div class="shell"><div class="head wideHead"><div><span class="kicker">Books As Biography</span><h2>{sem_title("如果把他的书按时间排开，","会看见一条不断扩大的生命轨迹")}</h2></div><p>从“我们怎样认识”，到“我如何听见使命”，再到“我们怎样共同生活”，每一本书都像前一个问题向外迈出的一步。</p></div><div class="bookRiver">{bio_book_river}</div></div></section>

<section class="section" id="resources"><div class="shell"><div class="head"><div><span class="kicker">Listen · Watch · Read</span><h2>{sem_title("如果想继续走近他，","从这些第一手资源开始")}</h2></div><p>下面优先链接官方机构与帕尔默本人的公开演讲、文章和视频，避免只停留在二手介绍。</p></div><div class="bioResources">
<a class="bioResource" href="https://couragerenewal.org/parker-j-palmer/" target="_blank" rel="noopener"><span class="tag">Official Bio</span><h3>Center for Courage & Renewal · Parker J. Palmer</h3><p>官方人物页：生平简介、著作、荣誉与帕尔默本人对“legacy”的回望。</p></a>
<a class="bioResource" href="https://couragerenewal.org/library/what-is-an-undivided-life/" target="_blank" rel="noopener"><span class="tag">Video</span><h3>What is an Undivided Life?</h3><p>由帕尔默本人简要说明：什么叫“不再分裂地活”。</p></a>
<a class="bioResource" href="https://couragerenewal.org/wp-content/uploads/2022/06/Parker-Palmer_The-Heart-of-a-Teacher.pdf" target="_blank" rel="noopener"><span class="tag">Essay</span><h3>The Heart of a Teacher</h3><p>进入“教师的内在风景”最直接的一篇文章，也是理解《教学的勇气》的好入口。</p></a>
<a class="bioResource" href="https://onbeing.org/programs/parker-palmer-courtney-martin-the-inner-life-of-rebellion/" target="_blank" rel="noopener"><span class="tag">Conversation</span><h3>The Inner Life of Rebellion</h3><p>帕尔默回忆神学院、Berkeley、社区组织与 Pendle Hill，能直接听见他的生命故事如何进入思想。</p></a>
<a class="bioResource" href="https://onbeing.org/blog/a-seedbed-for-the-growing-to-come/" target="_blank" rel="noopener"><span class="tag">Personal Essay</span><h3>A Seedbed for the Growing To Come</h3><p>帕尔默本人谈抑郁与生命黑夜。适合与《让生命说话》第四章一起阅读。</p></a>
<a class="bioResource" href="https://couragerenewal.org/library/25th-anniversary-celebration-recording/" target="_blank" rel="noopener"><span class="tag">History</span><h3>Courage & Renewal 25 周年</h3><p>帕尔默、Marcy Jackson、Rick Jackson 等共同回望这项工作的形成、传承与未来。</p></a>
<a class="bioResource" href="https://www.acgme.org/initiatives/awards/parker-j-palmer-courage-to-teach-award/" target="_blank" rel="noopener"><span class="tag">Living Legacy</span><h3>Parker J. Palmer Courage to Teach Award</h3><p>一个很具体的例子：他的“教学勇气”如何离开书本，进入今天的医学教育与专业实践。</p></a>
</div></div></section>

<section class="section" id="sources"><div class="shell"><div class="head"><div><span class="kicker">Sources</span><h2>这页传记依据什么</h2></div><p>人物事实与思想解释分层使用来源：生命史优先使用研究传记与官方资料，思想判断再回到帕尔默原著。</p></div><div class="bioSources">
<div class="bioSource"><b>Elena Soto, <em>The Spiritual and Educational Vision of Parker J. Palmer: The Birthright Gift of Self</em>（2024）</b><span>本页关于 Carleton、Berkeley、Georgetown、Pendle Hill、贵格会实践、导师关系及思想形成过程的主要二级研究来源。</span></div>
<div class="bioSource"><b>Center for Courage & Renewal · Parker J. Palmer 官方人物页</b><span>用于核对职业身份、著作数量、荣誉、影响范围与其晚年对“legacy”的公开说明。</span></div>
<div class="bioSource"><b>Parker J. Palmer 原著与公开访谈</b><span>用于理解使命、分裂生命、内在导师、完整性、教育与公共生活等概念，以及他本人公开谈及的生命经验。</span></div>
<div class="bioSource"><b>Wikimedia Commons</b><span>肖像采用 Sharon L. Palmer 2010 年照片；Carleton、Georgetown 与 Pendle Hill 实景用于帮助读者进入具体历史场景。</span></div>
</div></div></section>

<section class="section"><div class="shell"><div class="questionBand"><span class="kicker">Continue</span><h2>{sem_title("读完一个人的故事，","再进入他的思想世界")}</h2><p>帕尔默的传记不是思想的“背景资料”。它本身就是理解这套思想的入口：为什么他那么重视静默？为什么反复谈“分裂”？为什么共同体必须既靠近、又不侵入？下一步，可以带着这些生命经验进入思想总图。</p><div class="actions"><a class="btn primary" href="../worldview/">进入思想总图</a><a class="btn" href="../books/">浏览原著地图</a><a class="btn" href="index.html">回到人物页</a></div></div></div></section>
</main>'''
(ROOT/"parker-palmer/biography.html").write_text(wrap("帕克·帕尔默详细传记",bio_page,1,"帕克·J·帕尔默详细中文传记：从成长、学术、Pendle Hill、贵格会静默、教育思想、Courage & Renewal 到公共生活。"),encoding="utf-8")

# ---------- concepts index + pages ----------
concept_tiles=""
for c in concepts:
    search=html.escape((c["cn"]+" "+c["en"]+" "+c["summary"]).lower())
    concept_tiles+=f'<a class="card tile reveal" data-search-card="{search}" href="{c["slug"]}.html"><span class="tag">{c["en"]}</span><div class="tileVisual">{concept_visual(c["slug"])}</div><h3>{c["cn"]}</h3><p>{c["summary"]}</p><span class="arrow">→</span></a>'
concept_index=f'''<main>{crumbs(1,[("核心概念",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Concept Library</div><h1>{sem_title("20 个核心概念，不是词典，","而是<em>一张关系网</em>")}</h1><p class="lead">每个概念都连接原著、操练、相关概念与现实场景。不要只查定义，顺着关系继续走。</p><div class="actions"><a class="btn primary" href="network.html">打开知识关系图</a><a class="btn" href="../self-study/">进入自修中心</a></div><div class="heroFoot">建议入口：使命 / 完整性 / 信任圈 / 沉思与行动 / 悲剧性张力。</div></div></div></section>
<section class="section"><div class="shell"><div class="searchbar"><input data-site-search placeholder="搜索：使命、灵魂、教育、沉默、张力、公共生活……"></div><div class="grid3">{concept_tiles}</div></div></section></main>'''
(ROOT/"concepts/index.html").write_text(wrap("核心概念",concept_index,1),encoding="utf-8")

concept_rail=lambda cur:'<div class="rail">'+''.join(f'<a class="{"current" if c["slug"]==cur else ""}" href="{c["slug"]}.html">{c["cn"]}</a>' for c in concepts)+'</div>'

for c in concepts:
    related="".join(tile(f'{r}.html',"相关概念",concept_lookup[r]["cn"],concept_lookup[r]["summary"]) for r in c["related"])
    prompt=c["practice"][0] if c["practice"] else c["summary"]
    visual=concept_visual(c["slug"])
    circle_extra=""
    if c["slug"] in {"trustworthy-community","third-things","honest-open-questions","soul"}:
        circle_extra=f'''<div class="externalCta"><div><span class="tag">信任圈专题</span><h3>这个概念在信任圈专题中还有更完整的实践脉络</h3><p>主站保留它在帕尔默整体思想中的位置；信任圈的历史、规则、11 条基石、第三物与澄心会实践统一在专题站继续。</p></div><a class="btn" href="{CIRCLE_SITE}" target="_blank" rel="noopener">进入信任圈专题 ↗</a></div>'''
    body=f'''<main>{crumbs(1,[("核心概念","index.html"),(c["cn"],None)])}
    <section class="hero"><div class="shell heroGrid"><div class="heroMain"><div class="eyebrow">{c["en"]}</div><h1>{sem_title(c["verb"]+"：",f'<em>{c["cn"]}</em>')}</h1><p class="lead">{c["summary"]}</p><div class="actions"><a class="btn primary" href="#practice">现在就练</a><a class="btn" href="#relations">看它与什么相连</a></div><div class="heroFoot">概念不是定义：理解 → 误读校准 → 经验操练 → 原著 → 关系网络 → 现实行动。</div></div><div class="heroSide"><div class="visualPanel">{visual}</div><div class="sideCard"><span class="tag">带着这个问题</span><h3>{prompt}</h3></div></div></div></section>
    <section class="section"><div class="shell articleLayout"><aside class="toc"><span class="tag">本页导航</span><a href="#meaning">概念位置</a><a href="#text">原著脉络</a><a href="#misread">常见误读</a><a href="#practice">现在操练</a><a href="#relations">知识关联</a><a href="#sources">来源</a><a href="#related">继续探索</a></aside><article class="article">
    {concept_rail(c["slug"])}
    <section id="meaning"><span class="kicker">Meaning</span><h2>{sem_title("它在整套思想中，","处在什么位置")}</h2><p>{c["where"]}</p><div class="quote">{c["summary"]}</div></section>
    <section id="text"><span class="kicker">Textual Context</span><h2>{sem_title("不要把概念","从原著里拆出来")}</h2><p>{c["where"]}</p><p>阅读这个概念时，可以同时追问三个层次：它怎样描述<strong>内在经验</strong>？它要求怎样的<strong>关系条件</strong>？当它进入工作、教育或公共世界时，又怎样成为一种<strong>现实行动</strong>？</p></section>
    <section id="misread"><span class="kicker">Calibration</span><h2>不要把它误读成什么</h2><ul>{''.join(f'<li>{x}</li>' for x in c["misread"])}</ul></section>
    <section id="practice"><div class="practiceBox"><span class="kicker">Practice</span><h3>先按步骤走一遍</h3><div class="steps">{''.join(f'<div class="step"><div>{x}</div></div>' for x in c["practice"])}</div></div>{practice_lab("concept-"+c["slug"],c["cn"],prompt,10)}<div class="actions"><a class="toolButton" href="../self-study/third-things.html">换一个第三物进入</a><a class="toolButton" href="../self-study/questions.html">用开放问题继续</a><a class="toolButton" href="../self-study/records.html">查看我的记录</a></div></section>
    <section id="relations"><span class="kicker">Knowledge Connections</span><h2>{sem_title("这个概念，","在整套思想里连接什么")}</h2><p>不要把“{c["cn"]}”单独记住。沿着原著、实践、相关概念与现实场景往返，才能看见它真正的作用。</p>{relation_panel(c)}{circle_extra}</section>
    <section id="sources"><div class="sourceBox"><h3>主要原著脉络</h3><ul>{''.join(f'<li>{x}</li>' for x in c["sources"])}</ul><p><span class="badge">原著梳理</span><span class="badge">本站中文解释</span><span class="badge">自修工具为本站设计</span></p></div></section>
    <section id="related"><span class="kicker">Connections</span><h2>继续沿着关系走</h2><div class="grid3">{related}</div></section>
    </article></div></section></main>'''
    (ROOT/"concepts"/f'{c["slug"]}.html').write_text(wrap(c["cn"],body,1,c["summary"]),encoding="utf-8")

# ---------- concept network ----------
clusters=[
("内在","从听见到认出",["inner-teacher","soul","true-self","vocation"]),
("完整性","从分裂到对齐",["identity-integrity","wholeness","divided-life","undivided-life"]),
("关系","从控制到可信赖空间",["trustworthy-community","third-things","honest-open-questions","truth-conversation"]),
("认识与行动","从占有到参与",["knowing-loving","education-space","paradox","active-life"]),
("进入世界","从内在工作到现实承担",["tragic-gap","nonviolence","public-life","seasons"])
]
cluster_html=""
for title,desc,slugs in clusters:
    cluster_html+=f'<div class="cluster"><span class="tag">{desc}</span><h3>{title}</h3>'+''.join(f'<a href="{s}.html">{concept_lookup[s]["cn"]}</a>' for s in slugs)+'</div>'
network=f'''<main>{crumbs(1,[("核心概念","index.html"),("知识关系图",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Knowledge Network</div><h1>{sem_title("不要把帕尔默","读成<em>二十个孤立术语</em>")}</h1><p class="lead">同一个问题会在不同文本里换一种语言出现：内在导师会连到使命，身份与完整性会连到“不再分裂”，信任圈则把内在工作重新带回共同体与公共世界。</p><div class="actions"><a class="btn primary" href="../self-study/">带着关系图开始自修</a></div><div class="heroFoot">建议阅读方式：横向看同一层，纵向看“内在 → 关系 → 行动 → 公共”的迁移。</div></div></div></section><section class="section"><div class="shell"><div class="networkGrid">{cluster_html}</div></div></section><section class="section"><div class="shell"><div class="head"><div><div class="kicker">Three Long Arcs</div><h2>三条最重要的思想长线</h2></div><p>这些长线比任何单个术语更接近帕尔默思想的整体脉络。</p></div><div class="grid3"><div class="card dark"><span class="tag">ARC 01</span><h3>内在导师 → 真实自我 → 使命</h3><p>从“听谁的声音”走向“生命真正要求我成为谁”。</p></div><div class="card dark"><span class="tag">ARC 02</span><h3>分裂 → 完整性 → 不再分裂</h3><p>从看见内外断裂，走向可承担后果的现实行动。</p></div><div class="card dark"><span class="tag">ARC 03</span><h3>可信赖共同体 → 张力 → 公共生活</h3><p>内在工作不是退回私人世界，而是学习在差异与制度中仍不丢失人性。</p></div></div></div></section></main>'''
(ROOT/"concepts/network.html").write_text(wrap("知识关系图",network,1),encoding="utf-8")

# ---------- books index + pages ----------
book_tiles=""
for b in books:
    bvisual=concept_visual(b["concepts"][0]) if b["concepts"] else svg_mobius()
    search=html.escape((b["title"]+" "+b["zh"]+" "+b["focus"]).lower())
    book_tiles+=f'<a class="card tile reveal" data-search-card="{search}" href="{b["slug"]}.html"><span class="tag">{b["year"]}</span><div class="tileVisual">{bvisual}</div><h3>{b["zh"]}</h3><p><em>{b["title"]}</em><br>{b["focus"]}</p><span class="arrow">→</span></a>'
book_index=f'''<main>{crumbs(1,[("原著研读",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Primary Texts</div><h1>{sem_title("这里不是一张书单，","而是一张<em>问题地图</em>")}</h1><p class="lead">每本书都进入不同现实领域，但它们共享同一套深层问题：我是谁？我怎样知道？我怎样行动？我们怎样共同生活？</p><div class="heroFoot">每个原著页含：章节地图、关键命题、推荐操练、概念连接。</div></div></div></section><section class="section"><div class="shell"><div class="searchbar"><input data-site-search placeholder="搜索：使命、教育、行动、共同体、公共生活……"></div><div class="grid3">{book_tiles}</div></div></section></main>'''
(ROOT/"books/index.html").write_text(wrap("原著研读",book_index,1),encoding="utf-8")

for b in books:
    if b["slug"]=="hidden-wholeness":
        key_slugs=["divided-life","soul","wholeness","trustworthy-community","undivided-life"]
        key_cards="".join(tile(f'../concepts/{s}.html',"关键概念",concept_lookup[s]["cn"],concept_lookup[s]["summary"]) for s in key_slugs)
        body=f'''<main>{crumbs(1,[("原著地图","index.html"),(b["zh"],None)])}
            <section class="hero"><div class="shell heroGrid"><div class="heroMain"><div class="eyebrow">{b["year"]} · {b["title"]}</div><h1>{sem_title_auto(b["zh"])}</h1><p class="lead">{b["focus"]}</p><div class="actions"><a class="btn primary" href="{CIRCLE_SITE}" target="_blank" rel="noopener">进入《内在之光》与信任圈专题 ↗</a><a class="btn" href="../concepts/wholeness.html">理解“完整性”</a></div><div class="heroFoot">主站只保留这本书在帕尔默整体思想中的位置；章节共读与信任圈实践统一在独立专题站展开。</div></div><div class="heroSide"><div class="visualPanel">{svg_mobius()}</div></div></div></section>
        <section class="section"><div class="shell"><div class="head"><div><span class="kicker">Why It Matters</span><h2>{sem_title("内在真实与可信赖共同体，","在这本书里走向同一条路")}</h2></div><p>《A Hidden Wholeness》承接帕尔默长期对“身份”“完整性”与“分裂的生命”的思考，并进一步追问：当一个人想不再分裂地生活时，需要怎样的关系条件，才能既得到陪伴，又不被别人接管。</p></div><div class="storyGrid"><div><p class="storyLead">它不是一本单纯的“内在成长”书。前半部讨论“灵魂”“真实自我”与“分裂的生命”，后半部则不断把问题带回共同体、隐喻、提问、静默和日常非暴力。也就是说：内在工作最终必须进入人与人的关系。</p><p class="storyLead">因此，在帕尔默的整体思想里，这本书处在一个关键中点：它把《Let Your Life Speak》的使命辨识，与《The Courage to Teach》的身份/完整性，以及后来的公共生活主题连接起来。</p></div><div class="visualPanel">{svg_split_whole()}</div></div></div></section>
        <section class="section"><div class="shell"><div class="head"><div><span class="kicker">Five Keys</span><h2>先抓住五个关键词</h2></div><p>如果只是想理解帕尔默的整体思想，从这五个节点已经足够；需要章节研读和实践细节时再进入专题站。</p></div><div class="grid3">{key_cards}</div></div></section>
        <section class="section"><div class="shell"><div class="externalCta"><div><span class="tag">Independent Deep-Dive Site</span><h3>继续深入《内在之光》与信任圈</h3><p>章节导读、信任圈历史、11 条基石、第三物、开放问题、澄心会与带领实践，已经在独立专题网站系统整理，主站不再重复建设。</p></div><a class="btn" href="{CIRCLE_SITE}" target="_blank" rel="noopener">进入专题网站 ↗</a></div></div></section>
        </main>'''
        (ROOT/"books"/f'{b["slug"]}.html').write_text(wrap(b["zh"],body,1,b["focus"]),encoding="utf-8")
        continue
    rows="".join(f'<tr><td>{n}</td><td><strong>{t}</strong></td><td>{d}</td></tr>' for n,t,d in b["chapters"])
    concept_cards="".join(tile(f'../concepts/{s}.html',"概念",concept_lookup[s]["cn"],concept_lookup[s]["summary"]) for s in b["concepts"])
    prac_cards=[]
    for p in practices:
        if any(k.lower() in (p["title"]+" "+p["en"]).lower() for k in b["practices"]):
            prac_cards.append(tile(f'../practice/{p["slug"]}.html',"操练",p["title"],p["purpose"]))
    suggested="".join(f'<li>{x}</li>' for x in b["practices"])
    book_visual=concept_visual(b["concepts"][0]) if b["concepts"] else svg_mobius()
    body=f'''<main>{crumbs(1,[("原著研读","index.html"),(b["zh"],None)])}<section class="hero"><div class="shell heroGrid"><div class="heroMain"><div class="eyebrow">{b["year"]} · {b["title"]}</div><h1>{sem_title_auto(b["zh"])}</h1><p class="lead">{b["focus"]}</p><div class="actions"><a class="btn primary" href="#chapters">看章节地图</a><a class="btn" href="#practice">进入操练</a></div><div class="heroFoot">本页以资料库中的原著与带领指南为基础，采用中文解释与结构化梳理，不替代原书。</div></div><div class="heroSide"><div class="visualPanel">{book_visual}</div><div class="sideCard"><span class="tag">阅读时一直带着</span><h3>这本书正在要求我怎样重新看自己、关系或行动？</h3><p>不要只划金句；把概念放回自己的具体生活。</p></div></div></div></section>
    <section class="section"><div class="shell articleLayout"><aside class="toc"><span class="tag">本页导航</span><a href="#chapters">章节地图</a><a href="#ideas">关键命题</a><a href="#practice">操练入口</a><a href="#concepts">相关概念</a></aside><article class="article">
    <section id="chapters"><span class="kicker">Chapter Map</span><h2>章节 / 主题地图</h2><table class="table"><thead><tr><th>章节</th><th>主题</th><th>阅读抓手</th></tr></thead><tbody>{rows}</tbody></table></section>
    <section id="ideas"><span class="kicker">Key Ideas</span><h2>读这本书，抓住这些命题</h2><ul>{''.join(f'<li>{x}</li>' for x in b["ideas"])}</ul></section>
    <section id="practice"><div class="practiceBox"><span class="kicker">Practice</span><h3>适合与本书交替进行的操练</h3><ul>{suggested}</ul><p>阅读建议：每读一章，至少选一个问题做 10–20 分钟书写，再进入讨论。</p></div></section>
    <section id="concepts"><span class="kicker">Concept Links</span><h2>{sem_title("与这些核心概念，","连起来读")}</h2><div class="grid3">{concept_cards}</div></section>
    </article></div></section></main>'''
    (ROOT/"books"/f'{b["slug"]}.html').write_text(wrap(b["zh"],body,1,b["focus"]),encoding="utf-8")

# ---------- practice index + pages ----------
circle_special_slugs={"touchstones","circle-of-trust","clearness-committee"}
visible_practices=[p for p in practices if p["slug"] not in circle_special_slugs]
prac_tiles=""
for p in visible_practices:
    search=html.escape((p["title"]+" "+p["en"]+" "+p["purpose"]+" "+p["when"]).lower())
    prac_tiles+=f'<a class="card tile reveal" data-search-card="{search}" href="{p["slug"]}.html"><span class="tag">{p["en"]}</span><div class="tileVisual">{practice_visual(p["slug"])}</div><h3>{p["title"]}</h3><p>{p["purpose"]}</p><span class="arrow">→</span></a>'
matrix_rows="".join(f'<tr><td><strong>{p["title"]}</strong></td><td>{p["duration"]}</td><td>{p["size"]}</td><td>{p["when"]}</td></tr>' for p in visible_practices)
practice_index=f'''<main>{crumbs(1,[("实践",None)])}<section class="hero"><div class="shell heroGrid"><div class="heroMain"><div class="eyebrow">Practice Library</div><h1>{sem_title("不只停在“懂了”，","而是<em>亲自做一次</em>")}</h1><p class="lead">帕尔默的实践不是为了操控结果，而是设计条件：减慢反应、减少侵入、形成共同中心、让人能够听见自己，并把内在发现带回真实行动。</p><div class="heroFoot">这里保留可独立理解和使用的帕尔默实践；信任圈、11 条基石与澄心会的完整体系统一进入信任圈专题站。</div></div><div class="heroSide"><div class="visualPanel">{svg_inner_teacher()}</div><div class="sideCard"><h3>先学边界，再追求深度</h3><p>越是深入的内在工作，越需要明确邀请权、保密、时间结构与“不修理”的纪律。</p></div></div></div></section>
<section class="section"><div class="shell"><div class="head"><div><div class="kicker">Practice Matrix</div><h2>先选合适的练习</h2></div><p>不是所有方法都适合所有场景。先根据人数、时间与问题强度选择。</p></div><table class="table"><thead><tr><th>练习</th><th>时间</th><th>人数</th><th>适用场景</th></tr></thead><tbody>{matrix_rows}</tbody></table></div></section>
<section class="section"><div class="shell"><div class="searchbar"><input data-site-search placeholder="搜索：静默、开放问题、第三物、失败、张力、行动……"></div><div class="grid3">{prac_tiles}</div><div class="externalCta"><div><span class="tag">信任圈专题</span><h3>信任圈、11 条基石与澄心会</h3><p>这些方法具有完整的伦理、边界与带领结构。主站不再复制细节，请进入独立信任圈专题站系统学习。</p></div><a class="btn" href="{CIRCLE_SITE}" target="_blank" rel="noopener">进入信任圈专题 ↗</a></div></div></section></main>'''
(ROOT/"practice/index.html").write_text(wrap("操练方法",practice_index,1),encoding="utf-8")

for p in practices:
    if p["slug"] in circle_special_slugs:
        bridge_visual=svg_community() if p["slug"]!="clearness-committee" else svg_inner_teacher()
        bridge=f'''<main>{crumbs(1,[("实践","index.html"),(p["title"],None)])}<section class="hero"><div class="shell heroGrid"><div class="heroMain"><div class="eyebrow">{p["en"]}</div><h1>{sem_title_auto(p["title"])}</h1><p class="lead">{p["purpose"]}</p><div class="actions"><a class="btn primary" href="{CIRCLE_SITE}" target="_blank" rel="noopener">进入信任圈专题深入学习 ↗</a><a class="btn" href="../concepts/trustworthy-community.html">理解可信赖共同体</a></div><div class="heroFoot">本页只保留它在帕尔默思想中的位置；完整规则、步骤、案例与带领边界统一在独立专题站展开。</div></div><div class="heroSide"><div class="visualPanel">{bridge_visual}</div></div></div></section><section class="section"><div class="shell"><div class="head"><div><span class="kicker">Where It Fits</span><h2>它不是一个孤立技巧</h2></div><p>{p["purpose"]}</p></div><div class="grid3"><div class="card"><span class="tag">内在导师</span><h3>最终答案不由群体代替</h3><p>结构的作用是帮助一个人更能听见自己，而不是用群体意见取代个人辨识。</p></div><div class="card"><span class="tag">可信赖共同体</span><h3>关系需要边界</h3><p>邀请、保密、不过度建议与不侵入，是保护主体性的条件。</p></div><div class="card"><span class="tag">现实行动</span><h3>澄明最终要回到生活</h3><p>帕尔默的实践不会以“深度体验”结束，而要回到关系、角色与行动。</p></div></div><div class="externalCta"><div><h3>继续到独立专题站</h3><p>那里包含完整历史、11 条基石、第三物、澄心会、Circle of Trust 的实践结构与中文导读。</p></div><a class="btn" href="{CIRCLE_SITE}" target="_blank" rel="noopener">打开专题 ↗</a></div></div></section></main>'''
        (ROOT/"practice"/f'{p["slug"]}.html').write_text(wrap(p["title"],bridge,1,p["purpose"]),encoding="utf-8")
        continue
    extra=""
    if p["slug"]=="silence":
        extra='''<section id="core"><span class="kicker">Deepening</span><h2>{sem_title("与沉默对话：","一个自由书写练习")}</h2><div class="practiceBox"><p>把“沉默”当作一个可以回应你的对象，连续写 15–20 分钟。例如从“沉默，你最近在哪里？”开始，然后让“沉默”回答，再由自己继续回应。重点不是文学创作，而是观察：我为什么会靠近或躲开安静？</p><p>《A Hidden Wholeness》的带领材料曾用类似形式帮助参与者探索自己与沉默的关系。</p></div></section>'''
    pvisual=practice_visual(p["slug"])
    body=f'''<main>{crumbs(1,[("操练方法","index.html"),(p["title"],None)])}<section class="hero"><div class="shell heroGrid"><div class="heroMain"><div class="eyebrow">{p["en"]}</div><h1>{sem_title_auto(p["title"])}</h1><p class="lead">{p["purpose"]}</p><div class="actions"><a class="btn primary" href="#steps">直接看步骤</a><a class="btn" href="#facilitator">带领提醒</a></div><div class="heroFoot">建议时间：{p["duration"]} · 建议人数：{p["size"]}</div></div><div class="heroSide"><div class="visualPanel">{pvisual}</div><div class="sideCard"><span class="tag">适用场景</span><h3>{p["when"]}</h3><p>来源脉络：{p["source"]}</p></div></div></div></section>
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
    app_tiles.append(f'<a class="card tile reveal" href="{slug}.html"><span class="tag">应用场景</span><div class="tileVisual">{application_visual(slug)}</div><h3>{title}</h3><p>{summary}</p><span class="arrow">→</span></a>')
app_index=f'''<main>{crumbs(1,[("应用场景",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Applications</div><h1>{sem_title("思想只有进入现实，","才真正开始接受<em>检验</em>")}</h1><p class="lead">帕尔默的“内在工作”不是自我沉浸，而是要进入职业、教学、领导、社群和公共生活。</p><div class="heroFoot">这里按现实场景重新组合概念与操练，而不是重复书本章节。</div></div></div></section><section class="section"><div class="shell"><div class="grid3">{''.join(app_tiles)}</div></div></section></main>'''
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
    avisual=application_visual(slug)
    body=f'''<main>{crumbs(1,[("应用场景","index.html"),(title,None)])}<section class="hero"><div class="shell heroGrid"><div class="heroMain"><div class="eyebrow">Application</div><h1>{title}</h1><p class="lead">{summary}</p><div class="heroFoot">应用不是把帕尔默变成工具箱，而是保留其核心伦理：主体性、关系、边界、内外一致与现实承担。</div></div><div class="heroSide"><div class="visualPanel">{avisual}</div></div></div></section><section class="section"><div class="shell"><div class="head"><div><div class="kicker">Sequence</div><h2>建议顺序</h2></div><p>先处理条件，再处理内容；先减少侵入，再追求深度。</p></div><div class="steps">{''.join(f'<div class="step"><div>{x}</div></div>' for x in seq)}</div></div></section><section class="section"><div class="shell"><div class="head"><div><div class="kicker">Concepts</div><h2>相关概念</h2></div><p>这些概念构成本场景的思想骨架。</p></div><div class="grid3">{''.join(concept_cards)}</div></div></section>{practice_section}</main>'''
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
paths=f'''<main>{crumbs(1,[("研修路径",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Learning Pathways</div><h1>{sem_title("不要急着“刷完内容”，","让阅读、静默与行动<em>交替发生</em>")}</h1><p class="lead">主站保留两条跨文本研修路径：12 周综合研修与 6 次《The Active Life》小组；《A Hidden Wholeness》与信任圈的系统学习统一进入独立专题站。</p><div class="heroFoot">建议每次都保留：阅读 / 静默 / 书写 / 分享 / 开放问题 / 带回现实。</div></div></div></section>
<section class="section"><div class="shell"><div class="head"><div><div class="kicker">12 Weeks</div><h2>综合研修</h2></div><p>每周：原著 30–60 分钟 → 书写 10–20 分钟 → 一项微实践 → 伙伴或小组分享。</p></div><div class="grid3">{whtml}</div></div></section>
<section class="section"><div class="shell"><div class="head"><div><div class="kicker">6 Sessions</div><h2>《The Active Life》小组</h2></div><p>依据 Leader's Guide 的六次结构，适合成人学习小组。</p></div><div class="grid3">{ashtml}</div></div></section>
    <section class="section"><div class="shell"><div class="externalCta"><div><span class="tag">A Hidden Wholeness · 信任圈</span><h3>《内在之光》与信任圈的系统学习已独立成站</h3><p>章节导读、11 条基石、信任圈历史、第三物、澄心会与带领实践，请直接进入专题站；帕尔默主站不再重复维护两套内容。</p></div><a class="btn" href="{CIRCLE_SITE}" target="_blank" rel="noopener">进入专题站 ↗</a></div></div></section></main>'''
(ROOT/"pathways/index.html").write_text(wrap("研修路径",paths,1),encoding="utf-8")

# ---------- self-study system ----------
study_dir=ROOT/"self-study"
course_dir=study_dir/"hidden-wholeness"
course_dir.mkdir(parents=True,exist_ok=True)

study_home=f'''<main>{crumbs(1,[("自修中心",None)])}<section class="hero"><div class="shell"><div class="courseHero"><div class="eyebrow">Self-Study Studio</div><h1>{sem_title("读一点，停一停，","<em>让生命自己回应</em>")}</h1><p>自修不是把帕尔默的概念背下来，而是让“阅读—静默—书写—关系—行动”形成循环。这里保留轻量、可重复的个人工具；《内在之光》与信任圈的完整课程进入独立专题站。</p><div class="actions"><a class="btn primary" href="practice-now.html">先做 10 分钟</a><a class="btn" href="{CIRCLE_SITE}" target="_blank" rel="noopener">《内在之光》与信任圈专题 ↗</a></div></div></div></section>
<section class="section"><div class="shell"><div class="studyDock"><div><span class="kicker">Your Practice Space</span><h2>{sem_title("这是你的练习空间，","不是成绩单")}</h2><p>真正重要的不是完成多少模块，而是：你是否更能听见自己、更能在关系里不侵入别人、更能把内在真实带回现实。你主动保存的书写只存在当前浏览器。</p><div class="actions"><a class="toolButton primary" href="records.html">查看我的记录</a></div></div><div class="studyStat"><div><strong data-study-record-count>0</strong><span>条个人记录</span></div><div><strong>4</strong><span>个可重复使用的工具入口</span></div></div></div></div></section>
<section class="section"><div class="shell"><div class="head"><div><div class="kicker">Four Tools</div><h2>四个随时可用的入口</h2></div><p>工具的目的不是制造“深度感”，而是帮助你减慢反应、留下空白、记录线索，并沿知识关系继续探索。</p></div><div class="grid4">
{tile("practice-now.html","10 分钟","现在练一次","静默、计时与自由书写，从一个真实问题开始。")}
{tile("third-things.html","第三物","第三物素材库","不用直接逼问自己，让一个物件、画面或隐喻从侧面打开经验。")}
{tile("questions.html","提问","开放问题生成器","把建议、诊断和暗示，练习改写成帮助对方自我辨识的问题。")}
{tile("records.html","记录","我的个人记录","集中查看你主动保存的书写，并可导出 JSON 备份。")}
</div></div></section>
<section class="section"><div class="shell"><div class="head"><div><div class="kicker">Study Rhythm</div><h2>{sem_title("一次完整自修，","建议留出 35–60 分钟")}</h2></div><p>不用每次都做全，但尽量不要只停在阅读。</p></div><div class="pathwayFlow"><div class="flowNode"><b>5–15 分钟</b><small>读一小段原著</small></div><div class="flowNode"><b>3 分钟</b><small>静默，不解释</small></div><div class="flowNode"><b>10 分钟</b><small>自由书写</small></div><div class="flowNode"><b>5 分钟</b><small>第三物 / 开放问题</small></div><div class="flowNode"><b>5 分钟</b><small>提炼一句带走</small></div><div class="flowNode"><b>现实中</b><small>做一个小行动</small></div></div><div class="externalCta"><div><span class="tag">深入专题</span><h3>想系统学习《内在之光》与信任圈？</h3><p>请进入独立专题站，那里维护章节研读、历史脉络与完整实践结构。</p></div><a class="btn" href="{CIRCLE_SITE}" target="_blank" rel="noopener">进入专题站 ↗</a></div></div></section></main>'''
(study_dir/"index.html").write_text(wrap("自修中心",study_home,1),encoding="utf-8")

practice_now=f'''<main>{crumbs(1,[("自修中心","index.html"),("10 分钟操练",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Practice Now</div><h1>{sem_title("现在，给自己","<em>十分钟</em>")}</h1><p class="lead">不分析整个人生。只把一个问题放在面前，安静下来，写出第一句真实的话。</p><div class="heroFoot">建议问题：此刻，有什么是我已经隐约知道，却一直没有认真聆听的？</div></div></div></section><section class="section"><div class="shell"><div class="thirdThing"><div class="object">〰</div><span class="tag">今天的第三物 · 绳索</span><h2>{sem_title("在暴风雪里，","什么能把你带回自己？")}</h2><p>先不要解释“绳索象征什么”。只回想一个真实的人、地方、习惯、声音或物件：在你混乱的时候，它怎样帮助你不至于迷失？</p></div>{practice_lab("practice-now","10 分钟操练","此刻，有什么是我已经隐约知道，却一直没有认真聆听的？",10)}<div class="actions"><a class="toolButton" href="third-things.html">换一个第三物</a><a class="toolButton" href="questions.html">换一个开放问题</a></div></div></section></main>'''
(study_dir/"practice-now.html").write_text(wrap("10 分钟操练",practice_now,1),encoding="utf-8")

third_cards=""
for name,symbol,theme,prompt,links in third_things:
    rel=[]
    for s in links:
        if s in concept_lookup: rel.append(f'<a class="badge" href="../concepts/{s}.html">{concept_lookup[s]["cn"]}</a>')
        elif s in practice_lookup: rel.append(f'<a class="badge" href="../practice/{s}.html">{practice_lookup[s]["title"]}</a>')
    third_cards+=f'''<div class="thirdCard"><div class="symbol">{symbol}</div><span class="tag">{theme}</span><h3>{name}</h3><p>{prompt}</p><div class="mini">{''.join(rel)}</div></div>'''
third_page=f'''<main>{crumbs(1,[("自修中心","index.html"),("第三物素材库",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Third Things Library</div><h1>{sem_title("不必总是直接追问，","让第三物从侧面<em>打开经验</em>")}</h1><p class="lead">第三物让注意力先落在一个共同对象上，再由它折射自己的经验。它不是心理测验，也没有标准答案。</p><div class="heroFoot">使用顺序：先描述看见什么 → 哪一处抓住我 → 它让我想到什么 → 回到自己的生活。</div></div></div></section><section class="section"><div class="shell"><div class="thirdGrid">{third_cards}</div></div></section><section class="section"><div class="shell"><div class="questionBand"><h2>怎样选一个好的第三物？</h2><p>尽量短、透明、有多重可能；不要挑只有一个“正确寓意”的作品。也不要用第三物偷偷教育参与者得出带领者预设的结论。一个好的第三物既能触动你本人，也能给别人保留自己的解释空间。</p><div class="actions"><a class="btn primary" href="../practice/third-things.html">查看完整带领方法</a></div></div></div></section></main>'''
(study_dir/"third-things.html").write_text(wrap("第三物素材库",third_page,1),encoding="utf-8")

questions_page=f'''<main>{crumbs(1,[("自修中心","index.html"),("开放问题生成器",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Honest, Open Questions</div><h1>{sem_title("开放问题的关键，","不是聪明，而是<em>少一点接管</em>")}</h1><p class="lead">真正开放的问题，是提问者并不知道答案，也愿意让问题服务于对方的发现，而不是服务于自己的建议、判断或好奇。</p></div></div></section><section class="section"><div class="shell"><div class="questionTool" data-question-generator><span class="kicker">Question Generator</span><h2>把一个真实议题放进来</h2><input data-question-focus placeholder="例如：我要不要离开现在的工作？"><div class="rail"><label><input type="radio" name="lens" value="experience" checked> 经验</label><label><input type="radio" name="lens" value="image"> 意象</label><label><input type="radio" name="lens" value="tension"> 张力</label><label><input type="radio" name="lens" value="body"> 身体</label><label><input type="radio" name="lens" value="possibility"> 可能性</label><label><input type="radio" name="lens" value="next"> 下一步</label></div><button class="toolButton primary" data-generate-question>生成一个问题</button><div class="generatedQuestion" data-generated-question></div><p class="smallNote">生成器只提供问题句式练习。真正使用前仍要问自己：我是否已经知道答案？我是不是把建议藏在问号里？</p></div><div class="grid2" style="margin-top:20px"><div class="card"><span class="tag">避免</span><h3>伪装成问题的建议</h3><p>“你为什么不直接辞职？”“你是不是因为童年才会这样？”——这些句子已经把提问者的答案塞进去了。</p></div><div class="card"><span class="tag">练习</span><h3>短、真、不追赶</h3><p>一次只问一个问题。问完以后，让沉默出现。对方也始终拥有不回答的权利。</p></div></div></div></section></main>'''
(study_dir/"questions.html").write_text(wrap("开放问题生成器",questions_page,1),encoding="utf-8")

records_page=f'''<main>{crumbs(1,[("自修中心","index.html"),("我的记录",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">My Notes</div><h1>{sem_title("把零散的书写，","慢慢看成<em>生命的线索</em>")}</h1><p class="lead">这里汇总你主动保存的个人记录。数据只保存在当前浏览器；清理浏览器数据会丢失，请定期导出备份。</p><div class="actions"><button class="btn primary" data-export-records>导出 JSON 备份</button></div></div></div></section><section class="section"><div class="shell"><div class="recordList" data-record-list></div></div></section></main>'''
(study_dir/"records.html").write_text(wrap("我的记录",records_page,1),encoding="utf-8")

# A Hidden Wholeness now lives on the dedicated Circle of Trust site.
course_bridge=f'''<main>{crumbs(2,[("自修中心","../index.html"),("《内在之光》专题",None)])}<section class="hero"><div class="shell"><div class="courseHero"><div class="eyebrow">A Hidden Wholeness · Circle of Trust</div><h1>{sem_title("《内在之光》与信任圈，","<em>已经独立成站</em>")}</h1><p>为了避免两套内容重复维护，帕尔默主站只保留这本书在整体思想中的位置；章节共读、11 条基石、第三物、澄心会、历史与带领实践统一在“信任圈入门”专题站继续。</p><div class="actions"><a class="btn primary" href="{CIRCLE_SITE}" target="_blank" rel="noopener">进入专题站 ↗</a><a class="btn" href="../../books/hidden-wholeness.html">回到原著导览</a></div></div></div></section><section class="section"><div class="shell"><div class="storyGrid"><div><span class="kicker">Why Separate?</span><h2>{sem_title("主站呈现整体思想，","专题站深入实践")}</h2><p class="storyLead">《A Hidden Wholeness》是理解帕尔默如何从“分裂的生命”（divided life）走向“不再分裂”（undivided life）的关键文本，也孕育出信任圈的重要实践语言。但如果把章节研读、11 条基石与带领流程全部留在主站，反而会遮蔽他在认识、教育、行动和公共生活上的更大思想版图。</p></div><div class="visualPanel">{svg_community()}</div></div></div></section></main>'''
(course_dir/"index.html").write_text(wrap("《内在之光》专题入口",course_bridge,2),encoding="utf-8")

# Preserve old lesson URLs as lightweight bridges so existing bookmarks do not break.
for m in hidden_course:
    lesson_bridge=f'''<main>{crumbs(2,[("自修中心","../index.html"),("《内在之光》专题","index.html"),(m["title"],None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">{m["chapter"]} · {m["source"]}</div><h1>{sem_title_auto(m["title"])}</h1><p class="lead">这一章节的完整共读与实践内容已迁移到独立“信任圈入门”专题站。主站保留旧地址，方便已有链接继续可用。</p><div class="actions"><a class="btn primary" href="{CIRCLE_SITE}" target="_blank" rel="noopener">前往专题站继续 ↗</a><a class="btn" href="../../books/hidden-wholeness.html">查看《内在之光》在帕尔默思想中的位置</a></div></div></div></section></main>'''
    (course_dir/f'{m["slug"]}.html').write_text(wrap(m["title"],lesson_bridge,2,m["focus"]),encoding="utf-8")

# ---------- glossary ----------
grows="".join(f'<tr><td><strong>{en}</strong></td><td>{zh}</td><td>{d}</td></tr>' for en,zh,d in glossary)
gloss=f'''<main>{crumbs(1,[("术语表",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Glossary</div><h1>{sem_title("术语不是标签，","先理解它在帕尔默语境中的<em>作用</em>")}</h1><p class="lead">统一中文译法，减少把英文灵性术语直译后造成的误解。</p><div class="heroFoot">本站优先采用“内在导师、真实自我、完整性、基石、澄心会、第三物、悲剧性张力”等译法。</div></div></div></section><section class="section"><div class="shell"><table class="table"><thead><tr><th>英文</th><th>本站译法</th><th>语境说明</th></tr></thead><tbody>{grows}</tbody></table></div></section></main>'''
(ROOT/"glossary/index.html").write_text(wrap("术语表",gloss,1),encoding="utf-8")

# ---------- sources ----------
sources=f'''<main>{crumbs(1,[("资料说明",None)])}<section class="hero"><div class="shell"><div class="heroMain compact"><div class="eyebrow">Sources & Method</div><h1>{sem_title("内容可以丰富，","来源必须有清楚的<em>证据层级</em>")}</h1><p class="lead">本站优先使用帕尔默原著与正式带领指南，再用学术研究、纪念文集和历史材料补充思想脉络。网站中的“操练化整理”会明确作为本站整理，而不冒充帕尔默原文。</p><div class="heroFoot">资料不足的地方应标记“尚待核对”，而不是用一般灵性知识补齐。</div></div></div></section>
<section class="section"><div class="shell"><div class="grid4">
<div class="card"><span class="tag">第一层</span><h3>帕尔默原著</h3><p>A Hidden Wholeness、Let Your Life Speak、The Courage to Teach、To Know as We Are Known、The Active Life、The Company of Strangers、Healing the Heart of Democracy、Going Public、Meeting for Learning。</p></div>
<div class="card"><span class="tag">第二层</span><h3>带领与讨论指南</h3><p>The Courage to Teach Guide、The Active Life Leader's Guide、A Hidden Wholeness 的读者与小组带领材料，主要用于流程与操练结构。</p></div>
<div class="card"><span class="tag">第三层</span><h3>研究与思想脉络</h3><p>人物与思想形成史重点参考 Elena Soto 的 <em>The Spiritual and Educational Vision of Parker J. Palmer: The Birthright Gift of Self</em>，并辅以 <em>Living the Questions</em>、<em>Leading from Within</em> 等研究与纪念文集。</p></div>
<div class="card"><span class="tag">第四层</span><h3>当前 Courage & Renewal 框架</h3><p>用于了解帕尔默思想在今天如何被整理为价值、基石、原则、实践与课程资源；本站会把这一层与帕尔默原著明确区分。</p><a class="externalLink" href="https://couragerenewal.org/courage-renewal-approach/" target="_blank" rel="noopener">官方 Approach 页面 ↗</a></div>
</div><div class="sourceBox"><h3>本站写作与实践化原则</h3><ol>
<li>先确认原著在说什么，再做中文解释。</li><li>把术语放回上下文，不做“金句化”。</li><li>区分帕尔默本人的主张、Courage & Renewal 后续实践、本站再设计。</li>
<li>所有操练优先保护参与者主体性：邀请而非要求，不替人决定，不把建议藏进问题。</li><li>涉及澄心会等深入方法时，明确准备要求与边界。</li>
</ol></div></div></section></main>'''
(ROOT/"sources/index.html").write_text(wrap("资料说明",sources,1),encoding="utf-8")

# ---------- search index ----------
index=[]
for c in concepts:index.append({"title":c["cn"],"url":f'concepts/{c["slug"]}.html',"type":"概念","summary":c["summary"]})
for b in books:index.append({"title":b["zh"],"url":f'books/{b["slug"]}.html',"type":"原著","summary":b["focus"]})
for p in visible_practices:index.append({"title":p["title"],"url":f'practice/{p["slug"]}.html',"type":"操练","summary":p["purpose"]})
for slug,title,summary,_ in applications:index.append({"title":title,"url":f'applications/{slug}.html',"type":"应用","summary":summary})
index.extend([
{"title":"帕克·帕尔默","url":"parker-palmer/","type":"人物","summary":"从生命经历、Pendle Hill、Thomas Merton、贵格会传统、教育思想与代表著作认识 Parker J. Palmer。"},
{"title":"帕克·帕尔默详细传记","url":"parker-palmer/biography.html","type":"人物传记","summary":"从芝加哥、Carleton、Berkeley、Georgetown、Pendle Hill、贵格会静默与抑郁的黑夜，一路读到教育思想、Courage & Renewal 与公共生活。"},
{"title":"思想总图","url":"worldview/","type":"思想","summary":"从分裂生命、内在导师、真实自我与使命，一直走到教育、悖论、不再分裂与公共生活。"},
{"title":"自修中心","url":"self-study/","type":"自修","summary":"静默、自由书写、第三物、开放问题与个人记录组成的轻量练习空间。"},
{"title":"第三物素材库","url":"self-study/third-things.html","type":"自修工具","summary":"使用物件、意象与隐喻，从侧面进入内在经验。"},
{"title":"开放问题生成器","url":"self-study/questions.html","type":"自修工具","summary":"练习把建议、诊断与暗示改写成开放而诚实的问题。"},
{"title":"我的个人记录","url":"self-study/records.html","type":"自修工具","summary":"汇总并导出在概念页和自修工具中保存的个人书写。"},
{"title":"知识关系图","url":"concepts/network.html","type":"关联","summary":"从内在、完整性、关系、认识与行动、进入世界五个层次理解概念之间的关系。"},
{"title":"Courage & Renewal 实践框架","url":"worldview/courage-renewal.html","type":"思想框架","summary":"把当前 Courage & Renewal 的原则与 Palmer 核心概念建立连接。"},
{"title":"《内在之光》与信任圈专题","url":"self-study/hidden-wholeness/","type":"专题入口","summary":"主站保留桥接页，完整章节研读与 Circle of Trust 实践进入独立专题站。"}
])
(ROOT/"assets/search-index.json").write_text(json.dumps(index,ensure_ascii=False,indent=2),encoding="utf-8")

print("generated", len(list(ROOT.rglob("*.html"))), "html pages")
