/* Isolated Web API tests. These do not visit a live site or bypass browser policy. */
'use strict';
const fs = require('fs');
const vm = require('vm');
const path = require('path');
const assert = require('assert');
const code = fs.readFileSync(path.join(__dirname, 'assets/appearance-init.js'), 'utf8');
const checks = [];
const check = (value, name) => { assert(value, name); checks.push(name); };
function boot({url='https://wholemindliving.com/',brand='wholemind',dark=false,store={},blocked=false}={}) {
  const listeners = new Map();
  const mediaListeners = [];
  const root = { dataset: { brand } };
  const meta = { content: '#F7F3EB' };
  const media = { matches: dark, addEventListener(type, fn) {mediaListeners.push(fn);} };
  const w = {
    location: {href: url},
    matchMedia: () => media,
    addEventListener(type, fn) {if(!listeners.has(type))listeners.set(type,[]);listeners.get(type).push(fn);},
    dispatchEvent(event) {(listeners.get(event.type)||[]).forEach(fn=>fn(event));},
    history: {state:{preserved:1}, replaceState(state,title,address){w.history.state=state;w.location.href=address;}},
  };
  Object.defineProperty(w,'localStorage',{get(){
    if(blocked)throw new Error('Storage blocked');
    return {getItem:key=>store[key]??null,setItem:(key,value)=>{store[key]=String(value);},removeItem:key=>{delete store[key];}};
  }});
  const document={documentElement:root,querySelector:()=>meta};
  const ctx={window:w,document,URL,CustomEvent:class {constructor(type,options){this.type=type;this.detail=options.detail;}}};
  vm.createContext(ctx);vm.runInContext(code,ctx);
  return {w,root,store,meta,api:w.WholeMindAppearance,
    device(value){media.matches=value;mediaListeners.forEach(fn=>fn({matches:value}));},
    storageChanged(key){w.dispatchEvent({type:'storage',key});}};
}
const key='wholemind.appearance.v1';
for(const brand of ['wholemind','maxine']) {
 const url='https://'+(brand==='wholemind'?'wholemindliving.com':'themaxineproject.org')+'/';
 const store={unrelated:'preserved'};
 const p=boot({url,brand,dark:true,store});
 check(p.api.get()==='auto'&&p.root.dataset.theme==='dark',brand+': Auto starts from device preference');
 p.device(false);check(p.root.dataset.theme==='light',brand+': Auto responds to live device changes');
 p.api.set('dark');check(p.root.dataset.theme==='dark'&&store[key]==='dark',brand+': manual Dark is saved');
 p.device(false);check(p.root.dataset.theme==='dark',brand+': manual Dark ignores light device');
 const reload=boot({url,brand,store});check(reload.root.dataset.theme==='dark',brand+': saved Dark restored on reload');
 p.api.set('light');p.device(true);check(p.root.dataset.theme==='light',brand+': manual Light overrides dark device');
 p.api.set('auto');check(p.root.dataset.theme==='dark'&&!(key in store),brand+': Auto clears override and restores device preference');
 check(store.unrelated==='preserved',brand+': unrelated storage is untouched');
 const incoming=boot({url:url+'resources.html?keep=1&appearance=dark#main',brand,store});
 check(incoming.root.dataset.theme==='dark'&&incoming.w.location.href===url+'resources.html?keep=1#main',brand+': incoming Dark is applied; only appearance parameter removed');
 check(incoming.w.history.state.preserved===1,brand+': browser history state retained');
 const invalid=boot({url:url+'?appearance=not-a-theme',brand,store});
 check(invalid.api.get()==='dark'&&!invalid.w.location.href.includes('appearance='),brand+': invalid URL value ignored and removed');
 invalid.api.set('<script>');check(invalid.api.get()==='dark',brand+': invalid manual selection ignored');
 store[key]='invalid';const corrupt=boot({url,brand,store});check(corrupt.api.get()==='auto',brand+': corrupt saved value falls back to Auto');
 const b=boot({url,brand,blocked:true});b.api.set('dark');check(b.root.dataset.theme==='dark',brand+': blocked storage does not break manual control');
 const b2=boot({url:url+'?appearance=dark',brand,blocked:true});check(b2.root.dataset.theme==='dark',brand+': incoming preference works with blocked storage');
 store[key]='dark';const tab=boot({url,brand,store});store[key]='light';tab.storageChanged(key);
 check(tab.api.get()==='light',brand+': storage event updates a same-origin tab');
 delete store[key];tab.storageChanged(null);check(tab.api.get()==='auto',brand+': clearing storage resets a tab to Auto');
}
const from=boot({store:{[key]:'dark'}});
const targetStore={[key]:'light'};
const to=boot({url:'https://themaxineproject.org/?appearance='+from.api.get(),brand:'maxine',store:targetStore});
check(to.api.get()==='dark'&&targetStore[key]==='dark','explicit link hand-off overrides a different target-domain preference');
const auto=boot({url:'https://themaxineproject.org/?appearance=auto',brand:'maxine',store:targetStore,dark:true});
check(auto.api.get()==='auto'&&auto.root.dataset.theme==='dark'&&!(key in targetStore),'Auto hand-off removes the target-domain override');
fs.writeFileSync(path.join(__dirname,'APPEARANCE_STATE_TESTS.json'),JSON.stringify({status:'PASS',environment:'Isolated JavaScript contexts with mock Web Storage, URLs, history and media-query events',checks},null,2));
console.log(checks.length+' isolated appearance state checks passed');
