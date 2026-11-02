// Render project banners: node img/projects/src/render.js img/projects
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const [w,h,o] of [[500,300,'hybrid-intelligence.png'],[1180,200,'hybrid-intelligence-wide.png']]){
 const p=await b.newPage({viewport:{width:w,height:h}});
 await p.goto(`file://${__dirname}/hybrid-intelligence.html?w=${w}&h=${h}`);await p.screenshot({path:process.argv[2]+'/'+o});await p.close()}
await b.close()})();
