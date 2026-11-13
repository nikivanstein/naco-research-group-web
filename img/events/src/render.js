// Renders every event banner from banner.html + banners.js.
//   node img/events/src/render.js img/events [name-filter]
// Writes <key>.png (card, 1200x628) and <key>-wide.png (1180x200, at 2x).
const {chromium} = require('playwright');
const BANNERS = require('./banners.js');
const out = process.argv[2], only = process.argv[3] || '';
(async () => {
  const b = await chromium.launch();
  const card = await b.newPage({viewport: {width: 1200, height: 628}});
  const wide = await b.newPage({viewport: {width: 1180, height: 200}, deviceScaleFactor: 2});
  for (const id of Object.keys(BANNERS.events)) {
    if (!id.includes(only)) continue;
    for (const [p, size, file] of [[card, 'card', id + '.png'], [wide, 'wide', id + '-wide.png']]) {
      await p.goto(`file://${__dirname}/banner.html?id=${encodeURIComponent(id)}&size=${size}`);
      await p.waitForFunction(() => document.title === 'ready');
      await p.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => i.onload = i.onerror = r))));
      await p.screenshot({path: `${out}/${file}`});
    }
    console.log(id);
  }
  await b.close();
})();
