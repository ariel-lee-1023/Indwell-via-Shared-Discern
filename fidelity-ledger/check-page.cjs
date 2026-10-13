// Local HTML regression checks. Requires Playwright supplied by the host.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');
(async()=>{
 const root=path.resolve(process.argv[2]||path.join(__dirname,'..'));
 const browser=await chromium.launch({headless:true, channel:"chrome"});
 const page=await browser.newPage({viewport:{width:1000,height:1100}});
 const issues=[];page.on('pageerror',e=>issues.push(e.message));
 await page.goto(pathToFileURL(path.join(root,'examples/parallel-demo.html')).href);
 const checks=[];
 for(const [n,c,d,t,w] of [[10,3,2,8,4],[10,5,2,4,2],[0,3,2,0,0],[1,8,10,10,1],[24,1,10,240,24],[24,8,1,3,3]]){
  for(const [id,v] of [['count',n],['parallel',c],['duration',d]])await page.locator('#'+id).fill(String(v));
  const actual=await page.locator('#total').innerText();const rows=await page.locator('.batch').count();
  if(actual!==`${t} 分钟`||rows!==w)throw Error('calculation mismatch');checks.push({n,c,d,total:t,waves:w,passed:true});
 }
 for(const [id,v] of [['count',''],['count','1.5'],['count','25'],['parallel','0'],['duration','11']]){
  await page.locator('#count').fill('10');await page.locator('#parallel').fill('3');await page.locator('#duration').fill('2');
  await page.locator('#'+id).fill(v);
  if(await page.locator('#total').innerText()!=='—'||await page.locator('.batch').count()!==0||!await page.locator('#error').isVisible())throw Error('stale invalid result');
  checks.push({invalid:id,value:v,passed:true});
 }
 for(const [c,t,w] of [[4,6,3],[5,4,2],[6,4,2]]){
  await page.locator(`[data-parallel="${c}"]`).click();
  if(await page.locator('#total').innerText()!==`${t} 分钟`||await page.locator('.batch').count()!==w)throw Error('comparison mismatch');
  checks.push({preset:c,passed:true});
 }
 await page.locator('[data-parallel="4"]').focus();await page.keyboard.press('Enter');
 if(await page.locator('#total').innerText()!=='6 分钟')throw Error('keyboard control');
 checks.push({keyboardEnter:true,passed:true});
 await page.screenshot({path:path.join(root,'fidelity-ledger/page-wide.png'),fullPage:true});
 await page.setViewportSize({width:375,height:900});
 const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth);
 if(overflow)throw Error('narrow overflow');
 await page.screenshot({path:path.join(root,'fidelity-ledger/page-narrow.png'),fullPage:true});
 await page.setViewportSize({width:1100,height:1200});
 await page.setContent('<html><body><img style="width:100%;max-width:1000px" src="data:image/svg+xml;base64,'+fs.readFileSync(path.join(root,'examples/flow.svg')).toString('base64')+'"></body></html>');
 await page.screenshot({path:path.join(root,'fidelity-ledger/flow-preview.png'),fullPage:true});
 await browser.close();
 if(issues.length)throw Error(JSON.stringify(issues));
 fs.writeFileSync(path.join(root,'fidelity-ledger/page-checks.json'),JSON.stringify({checks,narrowOverflow:overflow,pageErrors:issues,visualReview:'separately recorded in validation.md'},null,2));
 console.log(`PASS ${checks.length} interaction and calculation checks; narrow overflow false`);
})().catch(e=>{console.error(e);process.exit(1)});
