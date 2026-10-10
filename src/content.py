"""Editorial source for the two-brand resource-led first release."""
DATE = 'October 9, 2026'
SOURCES = {
 'brain': {'name':'National Institute on Aging — Cognitive Health and Older Adults','url':'https://www.nia.nih.gov/health/brain-health/cognitive-health-and-older-adults'},
 'memory': {'name':'National Institute on Aging — Memory Problems, Forgetfulness, and Aging','url':'https://www.nia.nih.gov/health/memory-loss-and-forgetfulness/memory-problems-forgetfulness-and-aging'},
 'stroke': {'name':'Centers for Disease Control and Prevention — Signs and Symptoms of Stroke','url':'https://www.cdc.gov/stroke/signs-symptoms/index.html'},
 'helpline': {'name':"Alzheimer’s Association — 24/7 Helpline",'url':'https://www.alz.org/help-support/resources/helpline'},
 'locator': {'name':'Administration for Community Living — Eldercare Locator','url':'https://eldercare.acl.gov/home'}
}
SCOPE = 'General education and reflection, not medical advice, diagnosis, treatment, or crisis support. These resources do not replace care from a qualified health professional.'
RELATIONSHIP = 'WholeMind Living and The Maxine Project share an inspiration: honoring Maxine Boggs through work that values dignity, connection, and fuller living. WholeMind Living is being developed as a for-profit education and well-being brand. The Maxine Project is being developed as a nonprofit initiative focused on education and resources for people and families facing cognitive change.'
BRANDS = {
 'wholemind': {
  'name':'WholeMind Living','domain':'wholemindliving.com','accent':'#264D43','tint':'#E4EBE4',
  'eyebrow':'Brain health, well-being, and fuller living',
  'headline':'Make room for<br><em>a fuller life.</em>',
  'intro':'Practical education and thoughtful tools for everyday well-being, meaningful connection, and navigating change.',
  'aside_title':'A whole person.<br>A whole life.',
  'aside_text':'Your relationships, routines, interests, and hopes belong at the center. Start with what matters to you—not with a score or a standard someone else has set.',
  'approach_title':'Useful in everyday life.',
  'approach_intro':'Understand what matters, make space for it, and choose a next step that fits your life.',
  'pillars':[('Understand','Clear information and thoughtful questions, without exaggerated promises.'),('Practice','Simple ways to make room for the routines, interests, and relationships you value.'),('Connect','Conversations and shared moments that do not depend on testing anyone’s memory.')],
  'mission':'Make brain-health education and whole-person well-being practical through thoughtfully designed resources, tools, and learning experiences.',
  'vision':'A world in which people have accessible, trustworthy ways to sustain meaningful routines, relationships, and purpose through life’s changes.',
  'story_title':'A personal beginning.<br>A broader purpose.',
  'story_text':'WholeMind Living was inspired by Maxine Boggs, founder David Kissinger’s grandmother. The work begins with a commitment to seeing the whole person, and carries that commitment into practical education and tools for fuller living.',
  'story_detail':'This is not a promise to prevent every change or optimize every day. It is an invitation to make more room for what matters: a familiar interest, a meaningful conversation, a workable routine, and the freedom to ask for support.',
  'resource_title':'A thoughtful place to begin.',
  'resource_intro':'Read at your own pace, print a page, or return when you need it. The first collection is free and does not require an account.',
  'resources':['everyday-guide','one-meaningful-step','conversation-starters'],
  'primary':'Start with the free guide','primary_url':'resources/everyday-guide.html',
  'connect_title':'An open invitation.',
  'connect_text':'The work is beginning with freely available education and practical tools. Learn more about David, the founder, on his personal website.',
  'footer':'WholeMind Living is an education and well-being brand in development. No paid products or clinical services are offered through this release.'
 },
 'maxine': {
  'name':'The Maxine Project','domain':'themaxineproject.org','accent':'#67465B','tint':'#F0E7EC',
  'eyebrow':'Dignity, connection, and life through cognitive change',
  'headline':'A person is more than<br><em>what they remember.</em>',
  'intro':'Honoring Maxine Boggs through practical education and resources that keep dignity, connection, and the whole person at the center.',
  'aside_title':'See the person.<br>Make room for life.',
  'aside_text':'A person’s worth does not depend on what they can recall. Their voice, preferences, relationships, and place in everyday life deserve to be recognized.',
  'approach_title':'Begin with the person.',
  'approach_intro':'Clear starting points, room for the person’s own perspective, and connections to established sources of information and support.',
  'pillars':[('Understand','Prepare for a conversation about memory or thinking changes without trying to diagnose them yourself.'),('Recognize','Keep the person’s preferences, interests, voice, and relationships visible.'),('Connect','Find established education and community resources, without a purchase or donation requirement.')],
  'mission':'Honor Maxine Boggs by making reliable education, person-centered resources, and community connections more accessible to people and families facing cognitive change.',
  'vision':'A world in which people experiencing cognitive change remain recognized, included, and supported—and families do not have to navigate change alone.',
  'story_title':'A life that inspires<br>how we care.',
  'story_text':'The Maxine Project is named in honor of Maxine Boggs, David Kissinger’s grandmother. It carries a simple commitment: people and families facing cognitive change deserve understanding, dignity, and connection.',
  'story_detail':'Her name is the personal beginning of this work. The larger purpose is to keep a person’s life in view—not only the changes they are experiencing, but the relationships, preferences, and everyday moments that continue to matter.',
  'resource_title':'A starting place for families.',
  'resource_intro':'Practical preparation, a person-led profile, and a path to established resources. Free to use, with no signup or donation required.',
  'resources':['when-memory-changes','what-matters-to-me','find-your-next-step'],
  'primary':'Explore family resources','primary_url':'resources.html',
  'connect_title':'Help the work begin thoughtfully.',
  'connect_text':'The Maxine Project begins with education and practical resources. Learn more about David, the founder, on his personal website.',
  'footer':'The Maxine Project is an initiative in development. This website is not soliciting donations or representing contributions as tax-deductible.'
 }
}

def section(title, text='', prompts=None, note=None, source=None):
 return {'title':title,'text':text,'prompts':prompts or [],'note':note,'source':source or []}

RESOURCES = {
 'everyday-guide': {
  'brand':'wholemind','title':'The WholeMind Everyday Guide','label':'Free guide · 8 pages',
  'description':'A practical starting point for reflection, meaningful connection, and one manageable next step.',
  'intro':'You do not need to change everything to begin. This guide helps you notice what matters, choose something workable, and reflect without grading yourself.',
  'pdf':'WholeMind_Everyday_Guide.pdf',
  'pages':[
   section('Begin with your own life',
    'Fuller living does not have to mean a busier calendar or a more impressive routine. It can mean more room for a familiar interest, a relationship, a quiet moment, or a question you have been putting off.\n\nUse this guide in any order. Skip a prompt, speak your answers instead of writing them, or work through a page with someone you trust. There is no score, streak, or required pace.',
    ['What would I like a little more room for?','What am I already doing that I want to keep?'],
    'This is a reflection and planning guide, not a cognitive assessment or an individualized health plan.'),
   section('Put brain health in perspective',
    'Cognitive health includes the ability to think, learn, and remember. The National Institute on Aging discusses physical health, sleep, physical activity, social connection, and meaningful activities as relevant to cognitive health. These are areas for conversation and everyday care—not a promise that a particular routine prevents dementia.\n\nUse the questions below to prepare a conversation with a health professional. Do not change prescribed medicines based on this guide.',
    ['Is there a concern about sleep, memory, mood, hearing, vision, or medication effects I want to discuss?','What question would help me make an informed decision?'],
    'This guide does not recommend supplements, treatment, or a specific exercise program.', ['brain']),
   section('Notice the shape of your day',
    'Begin with what a typical day actually looks like, rather than what you think it should look like. Think about meals, work, rest, travel, interests, and time with other people.\n\nLook for one moment where a small adjustment might create room for something you value. The aim is not to fill every gap. Rest and unstructured time can belong in your plan, too.',
    ['A part of my day that already works for me:','A part of my day I would like to make easier:','Something I can simplify, share, postpone, or leave out:']),
   section('Make connection possible',
    'Connection can take different forms: a call, a shared meal, listening to music together, a short visit, or being comfortably in the same room. Choose a form that fits the relationship, your preferences, and what is possible right now.\n\nAn invitation can be specific without becoming a demand: “Would you like to have tea together this week?” Leave room for the other person to suggest something different or decline.',
    ['Someone I would enjoy connecting with:','A simple invitation I could offer:','What would make it easier for both of us?']),
   section('Keep interests in the picture',
    'An interest does not need to be productive to deserve space. Think about music, stories, cooking, nature, making something, spirituality, learning, humor, or a place you enjoy.\n\nAn activity can be adapted to your energy, access, or preferences. Listening can count as participation. Watching, choosing, sharing an opinion, and simply enjoying something together can matter, too.',
    ['Something I enjoy or feel curious about:','A version that would fit my life this week:','Something I would like to try, without pressure to become good at it:']),
   section('Choose one manageable step',
    'Choose one thing, not a complete overhaul. Make it specific enough that you can picture doing it. A useful plan also has room for things not going as expected.\n\nExample: “On Wednesday afternoon, I will ask a friend whether they would like a short phone call. If Wednesday becomes difficult, I will suggest the weekend.” This is an example of planning, not a prescription.',
    ['My one step:','When or where I will try it:','What might get in the way—and a gentler alternative:','Who or what could help:']),
   section('Prepare a useful conversation',
    'Some questions belong with a health professional rather than in a self-guided plan. Write your concern in ordinary language and include what matters to you.\n\nA starting sentence might be: “I have noticed a change, and I would like to understand it.” You do not need to arrive with a diagnosis. Keep your own observations separate from what someone else has noticed.',
    ['What I would like to discuss:','An example or date I want to remember:','The question I most want answered:'],
    'For memory or thinking concerns, talk with a health professional. For sudden possible stroke symptoms, call 911 rather than waiting for an appointment.', ['memory','stroke']),
   section('Reflect, then make room again',
    'After you have tried your step, pause without giving yourself a grade. What felt meaningful? What was inconvenient or too demanding? What would you change?\n\nYou can repeat a useful step, make it smaller, choose something different, or decide that this is not the right time. The point is to build a plan around your life—not judge your life against a plan.',
    ['What felt worthwhile?','What would I keep, simplify, or change?','My next step—or what I am choosing to set aside:'],
    'The companion “One Meaningful Step” worksheet collects these prompts on a single printable page. Keep completed pages private and share only what you choose.')
  ]
 },
 'one-meaningful-step': {
  'brand':'wholemind','title':'One Meaningful Step','label':'Free reflection sheet · 1 page',
  'description':'A one-page plan for something that matters to you, with room to adjust rather than a score to chase.',
  'intro':'Use this sheet on its own or alongside The WholeMind Everyday Guide. Write only what feels useful. You may skip any prompt.',
  'pdf':'One_Meaningful_Step.pdf',
  'pages':[section('A plan that belongs to you','Choose a manageable action, then revisit the plan with curiosity rather than judgment.',
   ['What matters to me right now:','One step I would like to try:','When or where I will try it:','What could help—or make it easier:','A smaller option if things change:','What felt worthwhile, and what I would adjust:'],
   'Optional personal worksheet. Not a clinical care plan. Keep your completed copy somewhere private.')]
 },
 'conversation-starters': {
  'brand':'wholemind','title':'A Conversation, Not a Test','label':'Free conversation prompts · 1 page',
  'description':'Open invitations to talk, listen, and enjoy time together—without putting anyone’s memory on the spot.',
  'intro':'Choose one prompt, not the entire page. There is no correct answer, and nobody has to respond. Follow the person’s interest rather than a script.',
  'pdf':'A_Conversation_Not_a_Test.pdf',
  'pages':[section('Make room for a response',
   '“What would you enjoy doing together today?”\n\n“Would you like music, a story, or a little quiet?”\n\n“What do you like about this?”\n\n“Would you like to tell me more?”\n\n“Is there something you want me to understand?”\n\n“Would you like company, or some space?”\n\nYou can share something about yourself instead of asking another question. You can also sit together without making conversation the task.',
   ['An invitation I would like to try:','Something the person would like more—or less—of:'],
   'These are optional conversation ideas, not a communication treatment or memory assessment. Respect the person’s preferences and right to decline.')]
 },
 'when-memory-changes': {
  'brand':'maxine','title':'When Memory Changes','label':'Free preparation guide · 4 pages',
  'description':'Organize what you have noticed, the person’s priorities, and questions for a health professional.',
  'intro':'You do not need to decide what a change means before asking about it. This guide helps prepare for an appointment while keeping the person’s own perspective in view.',
  'pdf':'When_Memory_Changes.pdf',
  'pages':[
   section('Start with a conversation, not a conclusion',
    'Memory and thinking concerns can have different explanations. A health professional can assess the concern and discuss next steps. This worksheet cannot tell you whether someone has dementia.\n\nWhere possible, invite the person to describe what they have noticed and what they want help understanding. Ask whether they would like another person involved. Do not use the worksheet to test, confront, or correct them.',
    ['What I have noticed, in my own words:','What I would like help understanding:'],
    'Sudden confusion or trouble speaking, sudden one-sided weakness, new trouble seeing or walking, or a sudden severe unexplained headache can be stroke symptoms. Call 911 immediately; do not wait to complete this guide.', ['memory','stroke']),
   section('Describe a few specific observations',
    'Brief examples can be easier to discuss than a broad label. Record what happened, roughly when it happened, and how it affected an ordinary activity. Separate direct observations from assumptions.\n\nFor example, a neutral note describes an event rather than calling someone “careless” or “confused all the time.” Include the person’s own explanation when they want it included.',
    ['What happened, and approximately when?','Was this new or different from what is usual for the person?','How did it affect the activity or the person?','What did the person say about it?'],
    'Write only what is needed for the conversation. This is not a symptom score or a diagnostic checklist.'),
   section('Bring questions and practical information',
    'Choose a few questions that matter most. Bring an up-to-date medication list, including nonprescription medicines and supplements, so the clinician can review it. Do not stop or change prescribed medication on your own.\n\nPossible questions: “What could explain the changes?” “What assessment would be useful?” “What should we watch for?” “Who should we contact, and when?” “What support is available while we work through this?”',
    ['The person’s top question:','Another question we want to ask:','Information or documents we plan to bring:'],
    'Tell the office in advance about communication or access needs. Ask the person whether they would like a support person at the appointment.', ['brain']),
   section('Leave with a clear next step',
    'Before the appointment ends, ask for an explanation of the plan in language you understand. A support person can help record it when the person agrees. Ask for written instructions or an accessible format where needed.\n\nThe website directory “Find Your Next Step” identifies established information and support services. These are independent organizations, not services delivered by The Maxine Project.',
    ['What we understand from the appointment:','The next step, and who is responsible:','When to follow up—and whom to contact with questions:','Support the person would welcome:'],
    'This worksheet is not a diagnosis, medical record, or substitute for the clinician’s instructions. Store it privately and share it only with appropriate permission.')
  ]
 },
 'what-matters-to-me': {
  'brand':'maxine','title':'What Matters to Me','label':'Free person-led profile · 1 page',
  'description':'Space for preferences, meaningful routines, relationships, communication, and comfort.',
  'intro':'This page belongs to the person it describes. Complete it with their participation wherever possible. Use their words and leave room for preferences to change.',
  'pdf':'What_Matters_to_Me.pdf',
  'pages':[section('See the person, not just the change','Skip any prompt. No diagnosis or sensitive identifying information is required.',
   ['What I enjoy and would like to keep in my life:','People or relationships that matter to me:','How I prefer people to communicate with me:','Routines, places, or traditions I value:','What helps me feel comfortable—and what I prefer to avoid:','What I would like others to understand:'],
   'Share only with permission. This is a conversation aid, not a legal directive, clinical care plan, capacity assessment, or substitute for supported decision-making.')]
 },
 'find-your-next-step': {
  'brand':'maxine','title':'Find Your Next Step','label':'Free resource directory · 2 pages',
  'description':'Established information and support, with named operators and clearly marked external links.',
  'intro':'Choose the kind of information or connection you need. The organizations below operate independently; a link does not imply endorsement, sponsorship, or a formal relationship.',
  'pdf':'Find_Your_Next_Step.pdf',
  'pages':[
   section('Information and a person to talk with',
    'National Institute on Aging (United States) — Public education on cognitive health and on memory changes. A starting point for learning; it does not replace an individual assessment.\n\nAlzheimer’s Association (United States) — Its free, 24/7 helpline offers dementia-related information, support, and connections to resources for people living with dementia, families, caregivers, and the public. Call 800-272-3900. The helpline belongs to the Association, not to The Maxine Project.',
    [], 'In an emergency, call 911. Do not use this directory or a website contact route to delay urgent care.', ['brain','memory','helpline']),
   section('Find community services',
    'Eldercare Locator (United States) — A public service of the Administration for Community Living connecting older adults and families with community services. Search by location or call 800-677-1116.\n\nWhen you contact a service, ask whom it serves, what it offers, whether there is a fee, what eligibility rules apply, and how it handles personal information. Availability and requirements differ by service.\n\nThe Maxine Project does not book appointments, make eligibility decisions, provide a staffed helpline, or guarantee access to an outside service.',
    ['The organization I plan to contact:','The question I would like answered:'],
    'Directory links and service descriptions were checked October 9, 2026. Services can change; confirm details directly with the operator.', ['locator'])
  ]
 }
}
