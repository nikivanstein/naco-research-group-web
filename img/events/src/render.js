const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:628}});
for(const [h,o] of [['evollms','evollms2027'],['beyondscalar','beyondscalar2027'],['llmfwec2027','llmfwec2027'],['llmmeta2027','llmmeta-gecco2027'],['ijcci2027','ijcci2027']]){
  if(process.argv[3]&&!o.includes(process.argv[3]))continue;
  await p.goto('file://'+__dirname+'/'+h+'.html');await p.screenshot({path:process.argv[2]+'/'+o+'.png'})}
await b.close()})();
