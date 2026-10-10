#!/usr/bin/env python3
"""Build dependency-free static sites and an offline review edition.
Usage: python build.py [--public]
Default is a noindex review build. Public mode changes indexing/banner, not legal facts.
"""
from pathlib import Path
import argparse, base64, html, json, re, shutil, sys, os
from urllib.parse import urlsplit, urljoin
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'src'))
from content import BRANDS, RESOURCES, SOURCES, DATE, SCOPE, RELATIONSHIP
E=html.escape
REVIEW=not ('--public' in sys.argv or os.environ.get('LAUNCH_MODE') == 'public')
NETLIFY_HOSTNAMES='--netlify-hostnames' in sys.argv
ORIGINS={b: ('https://'+('wholemindliving' if b=='wholemind' else 'themaxineproject')+'.netlify.app' if NETLIFY_HOSTNAMES else 'https://'+c['domain']) for b,c in BRANDS.items()}


def paragraphs(s):
 return ''.join('<p>'+E(x)+'</p>' for x in s.split('\n\n') if x)

def src_links(keys):
 if not keys:return ''
 return '<div class="sources"><p class="small-label">Source notes</p>'+''.join('<p><a href="'+E(SOURCES[k]['url'])+'" rel="noreferrer">'+E(SOURCES[k]['name'])+' <span class="external">(external)</span></a></p>' for k in dict.fromkeys(keys))+'</div>'

def relation_panel(b, sibling):
 other=BRANDS['maxine' if b=='wholemind' else 'wholemind']
 return '<section class="relation-panel wrap section"><p class="eyebrow">Shared inspiration. Distinct purposes.</p><h2>Connected by what matters.</h2><p>'+E(RELATIONSHIP)+'</p><a class="text-link" data-brand-link href="'+sibling+'">Explore '+other['name']+' <span aria-hidden="true">→</span></a></section>'

def card(slug, prefix=''):
 r=RESOURCES[slug]
 return '<article class="resource-card"><p class="resource-state">'+E(r['label'])+'</p><h3>'+E(r['title'])+'</h3><p>'+E(r['description'])+'</p><a class="text-link" href="'+prefix+'resources/'+slug+'.html">Open resource <span aria-hidden="true">→</span></a></article>'

def field(prompt, idx):
 return '<div class="worksheet-field"><label for="response-'+str(idx)+'">'+E(prompt)+'</label><textarea id="response-'+str(idx)+'" rows="3" autocomplete="off" spellcheck="false" data-worksheet></textarea><div class="print-response" aria-hidden="true"></div></div>'

def header(b, prefix, sibling, active):
 c=BRANDS[b]
 tab=lambda key,url:'<a href="'+url+'"'+(' aria-current="true"' if key==b else ' data-brand-link')+'>'+BRANDS[key]['name']+'</a>'
 links={'wholemind':prefix+'index.html' if b=='wholemind' else sibling,'maxine':prefix+'index.html' if b=='maxine' else sibling}
 appearance='<fieldset class="appearance" data-appearance hidden aria-describedby="appearance-help"><legend class="visually-hidden">Appearance</legend><span class="appearance-label" aria-hidden="true">Appearance</span><div class="appearance-options">'+''.join('<div class="appearance-option"><input type="radio" name="appearance" id="appearance-'+mode+'" value="'+mode+'"'+(' checked' if mode=='auto' else '')+'><label for="appearance-'+mode+'">'+label+'</label></div>' for mode,label in [('auto','Auto'),('light','Light'),('dark','Dark')])+'</div><span id="appearance-help" class="visually-hidden">Auto follows your device. Your selection is remembered in this browser when storage is available.</span></fieldset>'
 banner='<div class="preview-bar">FIRST RELEASE · Review version</div>' if REVIEW else ''
 nav=''.join('<a href="'+prefix+path+'.html"'+(' aria-current="page"' if active==path else '')+'>'+name+'</a>' for path,name in [('approach','Our approach'),('resources','Resources'),('story','Our story'),('connect','Connect')])
 return '<a class="skip-link" href="#main">Skip to main content</a>'+banner+'<div class="switcher"><div class="wrap"><span class="switcher-label">Shared inspiration. Distinct purposes.</span><div class="switcher-actions"><nav class="tabs" aria-label="Choose a website">'+tab('wholemind',links['wholemind'])+tab('maxine',links['maxine'])+'</nav>'+appearance+'</div></div></div><header class="brand-header wrap"><a href="'+prefix+'index.html" class="wordmark">'+c['name']+'</a><nav class="section-nav" aria-label="Main navigation">'+nav+'</nav></header>'

def footer(b,prefix):
 c=BRANDS[b]
 return '<footer class="site-footer"><div class="wrap"><p class="wordmark">'+c['name']+'</p><p>'+E(c['footer'])+'</p><p class="footer-small">'+E(SCOPE)+'</p><div class="footer-meta"><span>Dignity. Connection. Fuller living.</span><nav aria-label="Footer">'+''.join('<a href="'+prefix+p+'.html">'+label+'</a>' for p,label in [('relationship','Our relationship'),('privacy','Privacy'),('accessibility','Accessibility')])+'</nav></div></div></footer>'

def connect(b):
 c=BRANDS[b]
 return '<section class="wrap section connect"><div><p class="eyebrow">Connect</p><h2>'+c['connect_title']+'</h2><p>'+c['connect_text']+'</p></div><a class="button primary" href="https://davekissinger.com/" rel="noreferrer">Visit David’s website <span aria-hidden="true">↗</span></a></section>'

def page_intro(kicker,title,text):
 return '<div class="page-intro wrap"><p class="eyebrow">'+E(kicker)+'</p><h1>'+E(title)+'</h1><p class="hero-intro">'+E(text)+'</p></div>'

def home(b,sibling):
 c=BRANDS[b]
 future='<details class="future-note"><summary>What is being developed next?</summary><p>The Fuller Living Planner and the educational workshop <em>Making Room for a Fuller Life</em> are planned. Neither is available to purchase or book. This first release focuses on free resources.</p></details>' if b=='wholemind' else ''
 return '<div class="wrap hero"><div class="hero-copy"><p class="eyebrow">'+c['eyebrow']+'</p><h1>'+c['headline']+'</h1><p class="hero-intro">'+c['intro']+'</p><div class="actions"><a class="button primary" href="'+c['primary_url']+'">'+c['primary']+'</a><a class="text-link" href="'+('approach.html' if b=='wholemind' else 'story.html')+'">'+('Explore our approach' if b=='wholemind' else 'Meet the inspiration')+'</a></div><p class="domain">Free resources. No signup required.</p></div><aside class="hero-card"><div><p class="eyebrow">'+('Our starting point' if b=='wholemind' else 'The commitment')+'</p><h2>'+c['aside_title']+'</h2><p>'+c['aside_text']+'</p></div><p class="shared-signature">Dignity. Connection. Fuller living.</p></aside></div><section class="approach-band"><div class="wrap section"><div class="section-heading"><p class="eyebrow">Our approach</p><h2>'+c['approach_title']+'</h2><p>'+c['approach_intro']+'</p></div><div class="three-grid pillars">'+''.join('<article><h3>'+h+'</h3><p>'+t+'</p></article>' for h,t in c['pillars'])+'</div></div></section><section class="wrap section"><div class="section-heading"><p class="eyebrow">The first collection</p><h2>'+c['resource_title']+'</h2><p>'+c['resource_intro']+'</p></div><div class="three-grid">'+''.join(card(s) for s in c['resources'])+'</div>'+future+'</section><section class="story-band"><div class="wrap section story-grid"><div><p class="eyebrow">Inspired by Maxine Boggs</p><h2>'+c['story_title']+'</h2></div><div><p class="story-body">'+c['story_text']+'</p><p class="story-credit">Founder: David E. Kissinger, BSHA, RN</p><a class="text-link" href="story.html">Read our story <span aria-hidden="true">→</span></a></div></div></section>'+relation_panel(b,sibling)+connect(b)

def content_page(b,kind,sibling):
 c=BRANDS[b]
 if kind=='approach':
  return page_intro('Our approach',c['approach_title'],c['approach_intro'])+'<div class="wrap reading section"><h2>Our mission</h2><p>'+c['mission']+'</p><h2>Our vision</h2><p>'+c['vision']+'</p><h2>What the first release offers</h2><p>Free educational resources, practical reflection and preparation tools, and clearly identified links to outside information. You can read and print without creating an account.</p><h2>What it does not offer</h2><p>We do not provide diagnosis, treatment, individualized clinical advice, a staffed support line, or emergency response. No paid products, workshop bookings, or donations are accepted in this release.</p><a class="button primary" href="resources.html">Explore the resources</a></div>'
 if kind=='resources':
  return page_intro('Free to use',c['resource_title'],c['resource_intro'])+'<section class="wrap section"><div class="three-grid">'+''.join(card(s) for s in c['resources'])+'</div><p class="editorial-note">First edition · '+DATE+'. Source notes and scope are included with each guide. These are educational and reflection resources, not clinically validated instruments.</p></section>'
 if kind=='story':
  return page_intro('In honor of Maxine Boggs',re.sub('<[^>]+>',' ',c['story_title']),c['story_text'])+'<div class="wrap reading section">'+paragraphs(c['story_detail'])+'<h2>Dignity. Connection. Fuller living.</h2><p>These words describe the commitment behind the work. They guide what we make, how we write, and the experience we want people to have when they arrive here.</p><p>The founding inspiration is shared. The focus of each brand is distinct. Neither requires a person’s identity to be reduced to a diagnosis or a test result.</p><p class="story-credit">Founder: David E. Kissinger, BSHA, RN</p></div>'+relation_panel(b,sibling)
 if kind=='connect':
  return page_intro('Connect','A thoughtful beginning.','The first step is useful, freely available content—not a mailing-list requirement.')+connect(b)+'<section class="wrap reading section"><h2>About contact and updates</h2><p>This release does not have an email-subscription form. Reading or printing a resource does not subscribe you to either brand. No information is transferred from one brand’s mailing list to another.</p><p>For the founder’s personal website, use the link above. Do not send medical histories, personal health information about another person, or urgent requests through a general website contact route.</p><h2>Looking for established support?</h2><p>'+('The Maxine Project’s directory links to independent information and support services.' if b=='wholemind' else 'Our directory links to independent information and support services; the project does not operate a helpline.')+'</p><a class="text-link" '+('data-brand-link ' if b=='wholemind' else '')+'href="'+(urljoin(sibling, 'resources/find-your-next-step.html') if b=='wholemind' else 'resources/find-your-next-step.html')+'">Find your next step <span aria-hidden="true">→</span></a></section>'
 if kind=='relationship':
  return page_intro('Our relationship','Shared inspiration. Distinct purposes.','Two connected experiences, with their roles stated clearly.')+'<section class="wrap reading section"><h2>The intended structure</h2><p>'+RELATIONSHIP+'</p><h2>What the shared design means</h2><p>Shared typography, navigation, and layout express shared inspiration. They do not establish a parent–subsidiary relationship, a fiscal sponsorship, or a legal affiliation.</p><h2>Current status</h2><p>These brands are in development. This release does not claim that The Maxine Project has recognized tax-exempt status or that donations are tax-deductible. It does not solicit donations, sell products, book paid events, or promise that purchases support a charity.</p><h2>Separate choices</h2><p>Free resources do not require a purchase, donation, account, or subscription. Future email subscriptions, if introduced, will have separate brand-specific choices and a description of the relevant operator and data handling.</p><h2>Educational scope</h2><p>'+SCOPE+'</p></section>'
 if kind=='privacy':
  return page_intro('Privacy','Read without signing up.','This first release is designed around freely accessible pages and locally used worksheets.')+'<section class="wrap reading section"><p class="editorial-note">Version: '+DATE+'. Applies to the features included in this build.</p><h2>No accounts or subscription forms</h2><p>The site does not ask for an email address, collect payments, accept uploaded records, or offer an account. It has no advertising trackers or analytics scripts in its source code.</p><h2>Worksheet responses</h2><p>Worksheet text is held in the open page. The website code does not submit it or save it to local storage. Printing or saving a PDF creates a copy that you control. Your browser or device may retain information; clear a worksheet before leaving a shared device and keep saved copies private.</p><h2>Appearance preference</h2><p>Auto follows your device’s light or dark setting. Choosing Light or Dark stores only that preference in this browser on this website. Choosing Auto removes the saved override. Worksheet responses are not stored with it. If browser storage is blocked, the control still works on the current page.</p><p>Links between WholeMind Living and The Maxine Project carry the appearance choice in the destination address so the next website can apply it. The address parameter is removed after it is read, where the browser permits. The destination host may receive that parameter in its request logs; it contains only auto, light, or dark—not worksheet text or a personal identifier. The two domains keep their saved preferences separately.</p><h2>Hosting and typography</h2><p>A deployed host may process technical request information, such as an IP address, to deliver the site. Online pages request Fraunces and Source Sans 3 from Google Fonts; those requests may expose technical connection information to Google. The pages use local fallback fonts when these requests cannot load. No worksheet text is included in font requests.</p><h2>External websites</h2><p>Links to public agencies, support organizations, and the founder’s website lead to independent websites with their own policies. They do not receive worksheet responses from this website’s code.</p><h2>Before data collection is introduced</h2><p>Any future contact or subscription feature must identify its operator, purpose, retention and deletion practices, and consent choices before it is enabled. The connected visual design does not authorize sharing subscribers between brands.</p></section>'
 if kind=='accessibility':
  return page_intro('Accessibility','Designed to be usable.','Readable text, predictable navigation, and more than one way to use a resource.')+'<section class="wrap reading section"><h2>Reading and navigation</h2><p>Use the skip link to reach the main content. The brand switcher uses ordinary links, and both brands keep navigation in the same order. Pages support browser text zoom and narrow-screen layouts. Keyboard focus is visibly marked.</p><h2>Appearance</h2><p>The header offers Auto, Light, and Dark. Auto follows your device’s preference; Light and Dark override it. Use Tab to reach the appearance group and arrow keys to change its selection. Printed pages remain light. Without JavaScript, the page follows the device setting and the manual control stays hidden.</p><h2>Resources and worksheets</h2><p>Every printable resource has an HTML reading version. Worksheet fields have text labels; you may leave any of them blank. Print controls are added only when JavaScript is available. Without JavaScript, pages and the PDF links still work.</p><h2>Limits of this release</h2><p>The review build has undergone automated and visual checks, but not a full accessibility audit or a comprehensive screen-reader study. The printable PDFs are not certified PDF/UA documents; use the HTML versions when they better meet your needs.</p><h2>Feedback</h2><p>When a dedicated feedback route is introduced, its contact details will appear here. Until then, the founder’s personal website is available from the Connect page.</p><a class="text-link" href="connect.html">Connect <span aria-hidden="true">→</span></a></section>'
 if kind=='404':
  return page_intro('Page not found','Let’s find a useful starting point.','The page may have moved, or the address may be incomplete.')+'<div class="wrap section"><a class="button primary" href="index.html">Return home</a> <a class="text-link" href="resources.html">Explore resources</a></div>'
 raise ValueError(kind)

def resource_page(slug):
 r=RESOURCES[slug]
 intro=page_intro(r['label'],r['title'],r['intro'])
 out=intro+'<div class="resource-toolbar wrap"><a class="button primary" href="../downloads/'+r['pdf']+'" download>Download printable PDF</a><button class="button secondary" data-print hidden>Print this page</button><button class="text-link" data-clear hidden>Clear my responses</button></div><div class="wrap resource-layout"><aside class="resource-contents"><p class="small-label">In this resource</p><nav aria-label="Resource contents">'+''.join('<a href="#section-'+str(i+1)+'">'+str(i+1)+'. '+E(s['title'])+'</a>' for i,s in enumerate(r['pages']))+'</nav><p class="editorial-note">Your responses are optional. This website does not save or send them.</p></aside><article class="resource-body">'
 for i,s in enumerate(r['pages']):
  out+='<section class="guide-section" id="section-'+str(i+1)+'"><p class="eyebrow">'+str(i+1).zfill(2)+' / '+str(len(r['pages'])).zfill(2)+'</p><h2>'+E(s['title'])+'</h2>'+paragraphs(s['text'])
  if s['note']:out+='<aside class="scope-note">'+E(s['note'])+'</aside>'
  if s['prompts']:out+='<div class="worksheet">'+''.join(field(p,f'{slug}-{i}-{j}') for j,p in enumerate(s['prompts']))+'</div>'
  out+=src_links(s['source'])+'</section>'
 out+='<section class="guide-section editorial"><h2>About this resource</h2><p>Prepared for '+BRANDS[r['brand']]['name']+'. First edition: '+DATE+'. Drafting and source checking were AI-assisted. No independent clinical review or endorsement by a linked organization is represented.</p><p>'+E(SCOPE)+'</p><p>Use or print for personal, family, and noncommercial educational purposes. Do not present it as a clinical instrument or remove its scope and source notes.</p><p>For the reading version and other formats, return to this resource page. A downloaded PDF is a blank printable copy; it does not include responses typed into the page.</p><a class="text-link" href="../resources.html">Back to the resource collection <span aria-hidden="true">→</span></a></section></article></div><p class="visually-hidden" role="status" aria-live="polite" id="worksheet-status"></p>'
 return out

def document(b,path,body,prefix,sibling):
 c=BRANDS[b]; kind=path[:-5]
 slug=Path(path).stem
 title=(RESOURCES[slug]['title'] if path.startswith('resources/') else {'index':c['name'],'approach':'Our approach','resources':'Free resources','story':'Our story','connect':'Connect','relationship':'Our relationship','privacy':'Privacy','accessibility':'Accessibility','404':'Page not found'}[kind])
 description=RESOURCES[slug]['description'] if path.startswith('resources/') else c['intro']
 canonical=ORIGINS[b]+'/'+('' if path=='index.html' else path)
 robots='noindex, nofollow' if REVIEW or path=='404.html' else 'index, follow'
 font='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&amp;family=Source+Sans+3:wght@400;500;600;700&amp;display=swap" rel="stylesheet">'
 head=f'<!doctype html><html lang="en" data-brand="{b}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{E(title)} — {c["name"] if title!=c["name"] else "Dignity. Connection. Fuller living."}</title><meta name="description" content="{E(description,quote=True)}"><meta name="robots" content="{robots}"><link rel="canonical" href="{canonical}"><meta property="og:type" content="website"><meta property="og:title" content="{E(title,quote=True)}"><meta property="og:description" content="{E(description,quote=True)}"><meta property="og:url" content="{canonical}"><meta name="color-scheme" content="light dark"><meta name="theme-color" content="#F7F3EB"><script src="{prefix}assets/appearance-init.js?v=appearance-1"></script>{font}<link rel="stylesheet" href="{prefix}assets/site.css?v=appearance-1"><script src="{prefix}assets/site.js?v=appearance-1" defer></script></head>'
 return head+'<body data-brand="'+b+'">'+header(b,prefix,sibling,kind)+'<main id="main" tabindex="-1">'+body+'</main>'+footer(b,prefix)+'</body></html>'

HEADERS='''/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: no-referrer\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n  Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; connect-src 'none'; form-action 'none'; frame-ancestors 'none'; base-uri 'self'; object-src 'none'\n'''


def build():
 for mode in ('preview','dist'):
  base=ROOT/mode
  if base.exists():shutil.rmtree(base)
  for b,c in BRANDS.items():
   target=base/b;target.mkdir(parents=True)
   shutil.copytree(ROOT/'assets',target/'assets')
   (target/'downloads').mkdir()
   for slug in c['resources']:
    pdf=ROOT/'downloads'/RESOURCES[slug]['pdf']
    if not pdf.is_file(): raise FileNotFoundError('Required resource PDF missing: '+str(pdf))
    shutil.copy2(pdf,target/'downloads'/pdf.name)
   paths=['index.html']+[p+'.html' for p in ('approach','resources','story','connect','relationship','privacy','accessibility','404')]+['resources/'+s+'.html' for s in c['resources']]
   for path in paths:
    sub=path.startswith('resources/');prefix='../' if sub else ''
    other='maxine' if b=='wholemind' else 'wholemind'
    sibling=('../' if not sub else '../../')+other+'/index.html' if mode=='preview' else ORIGINS[other]+'/'
    if path=='404.html' and mode=='dist': prefix='/'
    body=home(b,sibling) if path=='index.html' else resource_page(Path(path).stem) if sub else content_page(b,path[:-5],sibling)
    if path=='404.html' and mode=='dist':
     body=body.replace('href="index.html"','href="/index.html"').replace('href="resources.html"','href="/resources.html"')
    dest=target/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(document(b,path,body,prefix,sibling))
   (target/'_headers').write_text(HEADERS+('  X-Robots-Tag: noindex, nofollow\n' if REVIEW else ''))
   (target/'robots.txt').write_text('User-agent: *\nDisallow: /\n' if REVIEW else 'User-agent: *\nAllow: /\nSitemap: '+ORIGINS[b]+'/sitemap.xml\n')
   entries=''.join('<url><loc>'+ORIGINS[b]+'/'+('' if p=='index.html' else p)+'</loc></url>' for p in paths if p!='404.html')
   (target/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+entries+'</urlset>')
 (ROOT/'preview'/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=wholemind/index.html"><title>WholeMind Living and The Maxine Project</title><a href="wholemind/index.html">Open WholeMind Living</a> <a href="maxine/index.html">Open The Maxine Project</a></html>')
 print('Built two brands in preview/ and dist/. Mode:', 'review/noindex' if REVIEW else 'public')

if __name__=='__main__':
 build()
 if '--deploy' in sys.argv:
  known_sites={
   '259722e8-d265-4f33-8da3-97fe1792a484':'wholemind',
   'b0146eb7-4a71-4b60-a0ad-bee6385698f2':'maxine',
  }
  expected=known_sites.get(os.environ.get('SITE_ID',''))
  selected=os.environ.get('SITE_BRAND') or expected
  if selected not in BRANDS:
   raise SystemExit('Set SITE_BRAND to wholemind or maxine; refusing an ambiguous deployment.')
  if expected and selected!=expected:
   raise SystemExit('SITE_BRAND conflicts with this Netlify project; refusing to publish the wrong brand.')
  publish=ROOT/'publish'
  if publish.exists():shutil.rmtree(publish)
  shutil.copytree(ROOT/'dist'/selected,publish)
  print('Prepared publish/ for:', selected)
