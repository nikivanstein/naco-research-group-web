// Render project banners from the HTML templates in this folder:
//   node img/projects/src/render.js img/projects [name-filter]
// Each <name>.html gives <name>.png (card, 500x300) and <name>-wide.png (1180x200).
const {chromium}=require('playwright');
const NAMES=['hybrid-intelligence','find'];
const only=process.argv[3]||'';
(async()=>{const b=await chromium.launch();
for(const name of NAMES.filter(n=>n.includes(only)))
 for(const [w,h,o] of [[500,300,name+'.png'],[1180,200,name+'-wide.png']]){
  const p=await b.newPage({viewport:{width:w,height:h}});
  await p.goto(`file://${__dirname}/${name}.html?w=${w}&h=${h}`);
  await p.evaluate(()=>Promise.all([...document.images].map(i=>i.complete?0:new Promise(r=>i.onload=i.onerror=r))));
  await p.screenshot({path:process.argv[2]+'/'+o});await p.close()}
await b.close()})();
