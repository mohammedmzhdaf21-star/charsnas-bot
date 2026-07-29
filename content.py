"""Undergraduate medicine study content organized by specialty and difficulty."""
from __future__ import annotations

import random

from quiz_bank import DIFFICULTIES, DIFFICULTY_LABELS, LABEL_TO_DIFFICULTY

SPECIALTY_ORDER = ['cardiology', 'ophthalmology', 'urology', 'neurology', 'pulmonology', 'gastroenterology', 'endocrinology', 'nephrology', 'orthopedics', 'dermatology', 'obgyn', 'pediatrics']

SPECIALTIES: dict[str, dict] = {'cardiology': {'label': 'Cardiology',
                'books': ["Braunwald's Heart Disease",
                          "Harrison's Principles of Internal Medicine — Cardiology",
                          'ECG Made Easy — John Hampton'],
                'pdf_notes': ['ACS spectrum: unstable angina, NSTEMI, STEMI — treat as '
                              'time-critical.',
                              'STEMI: ST elevation in contiguous leads ± new LBBB; urgent '
                              'reperfusion.',
                              'HF signs: orthopnea, raised JVP, crackles, edema; confirm with '
                              'BNP/echo.',
                              'MR = holosystolic to axilla; AS = crescendo-decrescendo to '
                              'carotids.',
                              'Secondary prevention after MI: antiplatelet, statin, beta-blocker, '
                              'ACEi as indicated.'],
                'questions': {'easy': [{'question': 'What does ECG primarily record?',
                                        'options': ['A) Blood pressure',
                                                    'B) Electrical activity of the heart',
                                                    'C) Coronary calcium only',
                                                    'D) Lung sounds'],
                                        'answer': 'B) Electrical activity of the heart',
                                        'explanation': 'ECG records cardiac electrical activity '
                                                       'over time.'},
                                       {'question': 'Typical symptom of angina is?',
                                        'options': ['A) Leg swelling only',
                                                    'B) Chest discomfort on exertion',
                                                    'C) Itchy rash',
                                                    'D) Double vision'],
                                        'answer': 'B) Chest discomfort on exertion',
                                        'explanation': 'Classic angina is exertional chest '
                                                       'discomfort relieved by rest/nitrates.'},
                                       {'question': 'Aspirin in ACS is given mainly to?',
                                        'options': ['A) Dilate bronchi',
                                                    'B) Inhibit platelets',
                                                    'C) Kill bacteria',
                                                    'D) Lower potassium'],
                                        'answer': 'B) Inhibit platelets',
                                        'explanation': 'Aspirin antiplatelet effect is '
                                                       'foundational in ACS care.'}],
                              'medium': [{'question': 'ST elevation in leads II, III, and aVF most '
                                                      'suggests occlusion in which territory?',
                                          'options': ['A) Anterior (often LAD)',
                                                      'B) Inferior (often RCA)',
                                                      'C) Purely posterior only',
                                                      'D) Right bundle only'],
                                          'answer': 'B) Inferior (often RCA)',
                                          'explanation': 'Inferior STEMI pattern localizes to '
                                                         'II/III/aVF, commonly RCA.'},
                                         {'question': 'Which murmur is holosystolic and radiates '
                                                      'to the axilla?',
                                          'options': ['A) Aortic stenosis',
                                                      'B) Mitral regurgitation',
                                                      'C) Mitral stenosis',
                                                      'D) Pulmonic stenosis'],
                                          'answer': 'B) Mitral regurgitation',
                                          'explanation': 'MR is holosystolic to the axilla.'},
                                         {'question': 'First-line symptom relief for an acute '
                                                      'angina episode is often?',
                                          'options': ['A) Sublingual nitroglycerin',
                                                      'B) Digoxin bolus always',
                                                      'C) IV amiodarone always',
                                                      'D) High-dose steroid'],
                                          'answer': 'A) Sublingual nitroglycerin',
                                          'explanation': 'SL nitrate reduces preload and can '
                                                         'relieve ischemic pain if not '
                                                         'contraindicated.'}],
                              'hard': [{'question': 'A patient with inferior STEMI becomes '
                                                    'hypotensive after nitrates and has elevated '
                                                    'JVP with clear lungs. Which associated '
                                                    'process should you suspect?',
                                        'options': ['A) Isolated left ventricular apical thrombus '
                                                    'only',
                                                    'B) Right ventricular infarction',
                                                    'C) Chronic stable mitral stenosis only',
                                                    'D) Simple vasovagal without ischemia'],
                                        'answer': 'B) Right ventricular infarction',
                                        'explanation': 'Inferior MI + nitrate hypotension + raised '
                                                       'JVP/clear lungs suggests RV infarction; '
                                                       'avoid nitrates, give fluids carefully.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Which heart-failure therapy class has '
                                                    'strong mortality benefit in HFrEF among the '
                                                    'listed options? Choose the most accurate '
                                                    'option and beware of near-miss distractors.',
                                        'options': ['A) Digoxin alone as sole therapy',
                                                    'B) Evidence-based beta-blocker (e.g. '
                                                    'carvedilol/bisoprolol/nebivolol pathways)',
                                                    'C) Short-acting nifedipine for HFrEF '
                                                    'mortality',
                                                    'D) Routine class Ic antiarrhythmic for all '
                                                    'HF'],
                                        'answer': 'B) Evidence-based beta-blocker (e.g. '
                                                  'carvedilol/bisoprolol/nebivolol pathways)',
                                        'explanation': 'GDMT for HFrEF includes evidence-based '
                                                       'beta-blockers among other cornerstone '
                                                       'classes.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. New LBBB with ischemic symptoms can '
                                                    'be treated as? Choose the most accurate '
                                                    'option and beware of near-miss distractors.',
                                        'options': ['A) Benign finding always',
                                                    'B) STEMI equivalent in appropriate clinical '
                                                    'context',
                                                    'C) Proof of PE only',
                                                    'D) Indication for atropine only'],
                                        'answer': 'B) STEMI equivalent in appropriate clinical '
                                                  'context',
                                        'explanation': 'Ischemic symptoms + new LBBB may warrant '
                                                       'emergent reperfusion pathways per local '
                                                       'protocols.'}],
                              'extreme': [{'question': 'A 72-year-old with prior CABG presents '
                                                       'with flash pulmonary edema, unequal arm '
                                                       'BPs, and a tearing back pain. Troponin is '
                                                       'mildly up; ECG shows non-specific ST '
                                                       'changes. Which diagnosis must be excluded '
                                                       'before dual antiplatelet loading and '
                                                       'anticoagulation for presumed NSTE-ACS?',
                                           'options': ['A) Acute aortic syndrome/dissection',
                                                       'B) Simple costochondritis only',
                                                       'C) Uncomplicated GERD only',
                                                       'D) Stable chronic venous insufficiency'],
                                           'answer': 'A) Acute aortic syndrome/dissection',
                                           'explanation': 'Dissection can mimic ACS; '
                                                          'antiplatelets/anticoagulation/thrombolysis '
                                                          'can be catastrophic if dissection is '
                                                          'present.'},
                                          {'question': 'In a high-stakes ward scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? In suspected tamponade after '
                                                       'cardiac surgery, which constellation is '
                                                       'most suggestive? Avoid premature therapies '
                                                       'that could harm if a critical differential '
                                                       'remains open.',
                                           'options': ['A) Hypertension with bounding pulses only',
                                                       'B) Hypotension, raised filling pressures, '
                                                       'low voltage/electrical alternans ± muffled '
                                                       'sounds',
                                                       'C) Isolated wheeze with normal BP',
                                                       'D) Fever alone without hemodynamic change'],
                                           'answer': 'B) Hypotension, raised filling pressures, '
                                                     'low voltage/electrical alternans ± muffled '
                                                     'sounds',
                                           'explanation': 'Tamponade physiology is obstructive '
                                                          'shock; echo confirms and guides '
                                                          'drainage.'},
                                          {'question': 'In a high-stakes ward scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? A patient in AF with WPW presents '
                                                       'with very fast irregular wide-complex '
                                                       'tachycardia and instability. Which '
                                                       'AV-nodal blocker strategy is '
                                                       'inappropriate? Avoid premature therapies '
                                                       'that could harm if a critical differential '
                                                       'remains open.',
                                           'options': ['A) Avoid AV-nodal blockers; use shock if '
                                                       'unstable',
                                                       'B) Give IV verapamil/digoxin/adenosine as '
                                                       'first-line',
                                                       'C) Synchronized cardioversion when '
                                                       'unstable',
                                                       'D) Expert consultation for antidromic '
                                                       'pathways'],
                                           'answer': 'B) Give IV verapamil/digoxin/adenosine as '
                                                     'first-line',
                                           'explanation': 'AV-nodal blockers can accelerate '
                                                          'accessory pathway conduction in AF+WPW; '
                                                          'unstable patients need electricity.'}]},
                'cases': {'easy': [{'title': 'Mild Exertional Chest Tightness',
                                    'stem': 'A 55-year-old man gets central chest tightness when '
                                            'climbing stairs. It eases after 3 minutes of rest. '
                                            'Exam and resting ECG are normal.',
                                    'question': 'Most likely diagnosis?',
                                    'answer': 'Stable angina (exertional myocardial ischemia).',
                                    'discussion': 'Pattern is predictable exertional pain relieved '
                                                  'by rest. Risk-factor modification and '
                                                  'anti-anginal strategy follow assessment.',
                                    'book_hint': "Harrison's — Ischemic Heart Disease"}],
                          'medium': [{'title': 'Crushing Pain with Anterior STE',
                                      'stem': 'A 58-year-old diabetic has crushing retrosternal '
                                              'pain for 40 minutes with diaphoresis. ECG shows ST '
                                              'elevation in V2–V4.',
                                      'question': 'Diagnosis and immediate reperfusion idea?',
                                      'answer': 'Anterior STEMI — urgent PCI (or timely '
                                                'fibrinolysis if PCI unavailable).',
                                      'discussion': 'Anterior STE is typically LAD territory. '
                                                    'Time-critical reperfusion saves myocardium.',
                                      'book_hint': 'Braunwald — ACS'}],
                          'hard': [{'title': 'Inferior MI then Hypotension',
                                    'stem': 'A 64-year-old with inferior STEMI receives '
                                            'nitroglycerin and becomes hypotensive. JVP is raised, '
                                            'lungs are clear, and right-sided ECG leads show ST '
                                            'elevation.',
                                    'question': 'What complication is most likely and what is a '
                                                'key initial hemodynamic step?',
                                    'answer': 'RV infarction — cautious IV fluids for preload '
                                              '(avoid nitrates/diuretics that drop preload).',
                                    'discussion': 'RV depends on preload; vasodilators can cause '
                                                  'profound hypotension. Reperfusion remains '
                                                  'essential.',
                                    'book_hint': 'Braunwald — RV infarction'}],
                          'extreme': [{'title': 'ACS Mimic with Pulse Deficit',
                                       'stem': 'A 68-year-old hypertensive man has sudden severe '
                                               'tearing chest pain radiating to the back, a pulse '
                                               'deficit between arms, and a new soft aortic '
                                               'regurgitation murmur. Troponin is borderline; ECG '
                                               'is non-diagnostic. The team is about to load dual '
                                               'antiplatelets for NSTE-ACS.',
                                       'question': 'What should you do first conceptually?',
                                       'answer': 'Stop ACS anticoagulation/antiplatelet pathway '
                                                 'and urgently evaluate for aortic dissection (CT '
                                                 'angiography if stable).',
                                       'discussion': 'Dissection can cause coronary ostial '
                                                     'compromise and AR. Wrong therapy worsens '
                                                     'outcomes. Stabilize BP and get definitive '
                                                     'imaging.',
                                       'book_hint': "Braunwald / Harrison's — Aortic "
                                                    'dissection'}]}},
 'ophthalmology': {'label': 'Ophthalmology',
                   'books': ["Kanski's Clinical Ophthalmology",
                             "Vaughan & Asbury's General Ophthalmology",
                             "Clinical Ophthalmology — Parsons' "],
                   'pdf_notes': ['Red eye emergencies: angle-closure glaucoma, keratitis, uveitis, '
                                 'endophthalmitis.',
                                 'RAPD: swinging flashlight test — optic nerve / severe retinal '
                                 'disease.',
                                 'Diabetic retinopathy: microaneurysms, hemorrhages, exudates ± '
                                 'neovascularization.',
                                 "CN III palsy: eye 'down and out'; CN VI: failed abduction.",
                                 'Cataract: reversible surgically; AMD: irreversible central loss '
                                 'if advanced.'],
                   'questions': {'easy': [{'question': 'What test checks for RAPD?',
                                           'options': ['A) Swinging flashlight test',
                                                       'B) Weber test',
                                                       'C) Romberg test',
                                                       'D) Allen test'],
                                           'answer': 'A) Swinging flashlight test',
                                           'explanation': 'RAPD is assessed with swinging '
                                                          'flashlight.'},
                                          {'question': 'Painful red eye with mid-dilated pupil '
                                                       'suggests?',
                                           'options': ['A) Conjunctivitis',
                                                       'B) Acute angle-closure glaucoma',
                                                       'C) Chalazion',
                                                       'D) Simple dry eye'],
                                           'answer': 'B) Acute angle-closure glaucoma',
                                           'explanation': 'Angle closure is an ophthalmic '
                                                          'emergency.'},
                                          {'question': 'CN VI palsy mainly impairs?',
                                           'options': ['A) Adduction',
                                                       'B) Abduction',
                                                       'C) Accommodation only',
                                                       'D) Smell'],
                                           'answer': 'B) Abduction',
                                           'explanation': 'CN VI innervates lateral rectus.'}],
                                 'medium': [{'question': 'Diabetic retinopathy microaneurysms are '
                                                         'seen on?',
                                             'options': ['A) Skin exam only',
                                                         'B) Fundoscopy / retinal exam',
                                                         'C) Audiometry',
                                                         'D) Spirometry'],
                                             'answer': 'B) Fundoscopy / retinal exam',
                                             'explanation': 'Retinal exam detects DR changes.'},
                                            {'question': 'Sudden curtain-like field loss suggests?',
                                             'options': ['A) Cataract',
                                                         'B) Retinal detachment until proven '
                                                         'otherwise',
                                                         'C) Presbyopia',
                                                         'D) Pinguecula'],
                                             'answer': 'B) Retinal detachment until proven '
                                                       'otherwise',
                                             'explanation': 'Flashes/floaters/curtain → urgent '
                                                            'retina care.'},
                                            {'question': 'Orbital cellulitis vs preseptal key '
                                                         'worrying features include?',
                                             'options': ['A) Only mild lid itch',
                                                         'B) Painful eye movements, proptosis, '
                                                         'vision change',
                                                         'C) Dandruff alone',
                                                         'D) Isolated stye without systemic signs '
                                                         'always safe'],
                                             'answer': 'B) Painful eye movements, proptosis, '
                                                       'vision change',
                                             'explanation': 'Orbital cellulitis can threaten '
                                                            'vision and life.'}],
                                 'hard': [{'question': 'A junior colleague asks for the single '
                                                       'best answer. A relative afferent pupillary '
                                                       'defect with normal fundoscopy early on '
                                                       'most suggests? Choose the most accurate '
                                                       'option and beware of near-miss '
                                                       'distractors.',
                                           'options': ['A) Early cataract only',
                                                       'B) Optic neuropathy (e.g., optic '
                                                       'neuritis/ischemic optic neuropathy '
                                                       'pathways)',
                                                       'C) Simple refractive error',
                                                       'D) Unilateral conductive hearing loss'],
                                           'answer': 'B) Optic neuropathy (e.g., optic '
                                                     'neuritis/ischemic optic neuropathy pathways)',
                                           'explanation': 'RAPD localizes to optic nerve/severe '
                                                          'retina.'},
                                          {'question': 'A junior colleague asks for the single '
                                                       'best answer. Painful third-nerve palsy '
                                                       'involving the pupil is concerning for? '
                                                       'Choose the most accurate option and beware '
                                                       'of near-miss distractors.',
                                           'options': ['A) Posterior communicating artery aneurysm '
                                                       'compression until excluded',
                                                       "B) Bell's palsy",
                                                       'C) Otitis externa',
                                                       'D) Simple migraine aura always'],
                                           'answer': 'A) Posterior communicating artery aneurysm '
                                                     'compression until excluded',
                                           'explanation': 'Pupil-involving CN III needs urgent '
                                                          'vascular evaluation.'},
                                          {'question': 'A junior colleague asks for the single '
                                                       'best answer. Central retinal artery '
                                                       'occlusion typically presents as? Choose '
                                                       'the most accurate option and beware of '
                                                       'near-miss distractors.',
                                           'options': ['A) Painful bilateral gradual loss',
                                                       'B) Sudden painless monocular vision loss',
                                                       'C) Itchy eyelids only',
                                                       'D) Photophobia alone'],
                                           'answer': 'B) Sudden painless monocular vision loss',
                                           'explanation': 'CRAO is a retinal stroke emergency.'}],
                                 'extreme': [{'question': 'In a high-stakes ward scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? A patient with giant cell '
                                                          'arteritis risk (age >50, jaw '
                                                          'claudication, ESR high) and sudden '
                                                          'vision loss needs which immediate '
                                                          'concept? Avoid premature therapies that '
                                                          'could harm if a critical differential '
                                                          'remains open.',
                                              'options': ['A) Delay steroids until biopsy returns '
                                                          'even if vision threatened',
                                                          'B) Start high-dose steroids urgently '
                                                          'when GCA/AION strongly suspected',
                                                          'C) Only artificial tears',
                                                          'D) Routine refraction'],
                                              'answer': 'B) Start high-dose steroids urgently when '
                                                        'GCA/AION strongly suspected',
                                              'explanation': 'Do not delay steroids for biopsy if '
                                                             'GCA threatens vision.'},
                                             {'question': 'In a high-stakes ward scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? In chemical eye injury, '
                                                          'the first action is? Avoid premature '
                                                          'therapies that could harm if a critical '
                                                          'differential remains open.',
                                              'options': ['A) Immediate copious irrigation',
                                                          'B) Detailed visual field testing before '
                                                          'any rinse',
                                                          'C) Patch tightly without irrigating',
                                                          'D) Start oral antibiotics only'],
                                              'answer': 'A) Immediate copious irrigation',
                                              'explanation': 'Irrigate first, examine later.'},
                                             {'question': 'In a high-stakes ward scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? An immunosuppressed '
                                                          'patient with painful red eye, hypopyon, '
                                                          'and severe vision loss may have? Avoid '
                                                          'premature therapies that could harm if '
                                                          'a critical differential remains open.',
                                              'options': ['A) Endophthalmitis until proven '
                                                          'otherwise',
                                                          'B) Mild blepharitis only',
                                                          'C) Uncomplicated pinguecula',
                                                          'D) Simple allergic conjunctivitis '
                                                          'always'],
                                              'answer': 'A) Endophthalmitis until proven otherwise',
                                              'explanation': 'Endophthalmitis needs emergency '
                                                             'ophthalmic care.'}]},
                   'cases': {'easy': [{'title': 'Red Eye After Dark Room',
                                       'stem': 'A 54-year-old hyperopic woman develops severe eye '
                                               'pain, halos, and nausea after leaving a dark '
                                               'cinema. Pupil is mid-dilated and poorly reactive.',
                                       'question': 'Most likely diagnosis?',
                                       'answer': 'Acute angle-closure glaucoma.',
                                       'discussion': 'Urgent IOP lowering and ophthalmology '
                                                     'referral; avoid dilating drops.',
                                       'book_hint': "Kanski's Clinical Ophthalmology"}],
                             'medium': [{'title': 'Diabetic Blurry Vision',
                                         'stem': 'A 60-year-old with longstanding diabetes has '
                                                 'gradual blur. Fundus shows hemorrhages, '
                                                 'microaneurysms, and hard exudates near the '
                                                 'macula.',
                                         'question': 'Diagnosis category?',
                                         'answer': 'Diabetic retinopathy with possible macular '
                                                   'involvement.',
                                         'discussion': 'Glycemic/BP control + ophthalmic '
                                                       'management for macular '
                                                       'edema/proliferation.',
                                         'book_hint': "Kanski's Clinical Ophthalmology"}],
                             'hard': [{'title': 'Pupil-Involving CN III',
                                       'stem': 'A 48-year-old with sudden unilateral ptosis, eye '
                                               "'down and out', and a dilated poorly reactive "
                                               'pupil has a severe new headache. Decide the '
                                               'highest-yield urgent concept before results '
                                               'return.',
                                       'question': 'What dangerous cause must be excluded?',
                                       'answer': 'Compressive CN III palsy from PCOM aneurysm.',
                                       'discussion': 'Urgent neuroimaging/vascular study; this is '
                                                     'not a routine outpatient palsy.',
                                       'book_hint': "Kanski's Clinical Ophthalmology"}],
                             'extreme': [{'title': 'GCA Threat to Vision',
                                          'stem': 'A 76-year-old woman with new headache, jaw '
                                                  'claudication, scalp tenderness, and ESR 95 '
                                                  'suddenly loses vision in one eye. Fundus '
                                                  'suggests pale disc swelling. Avoid '
                                                  'interventions that could worsen an unexcluded '
                                                  'catastrophic differential.',
                                          'question': 'Immediate management concept?',
                                          'answer': 'Treat as arteritic ischemic optic '
                                                    'neuropathy/GCA: urgent high-dose steroids and '
                                                    'urgent specialty care; arrange temporal '
                                                    'artery biopsy without delaying steroids.',
                                          'discussion': 'Vision in the fellow eye is at risk '
                                                        'within days if untreated.',
                                          'book_hint': "Kanski's Clinical Ophthalmology"}]}},
 'urology': {'label': 'Urology',
             'books': ['Campbell-Walsh-Wein Urology',
                       "Smith's General Urology",
                       'Bailey & Love — Urology chapters'],
             'pdf_notes': ['Stone types: calcium oxalate most common; struvite with urease '
                           'organisms; uric acid radiolucent.',
                           'Loin→groin pain + hematuria = ureteric colic until proven otherwise.',
                           'Painless hematuria: rule out malignancy (esp. smokers).',
                           'Pyelonephritis: fever + flank pain + UTI signs → antibiotics ± '
                           'imaging.',
                           'BPH: storage/voiding symptoms in older men; assess PSA/exam '
                           'judiciously.'],
             'questions': {'easy': [{'question': 'Most common kidney stone type?',
                                     'options': ['A) Cystine',
                                                 'B) Calcium oxalate',
                                                 'C) Pure xanthine',
                                                 'D) Indinavir only'],
                                     'answer': 'B) Calcium oxalate',
                                     'explanation': 'Calcium oxalate is most common.'},
                                    {'question': 'Loin-to-groin pain classically suggests?',
                                     'options': ['A) Ureteric colic',
                                                 'B) Migraine',
                                                 'C) Otitis media',
                                                 'D) Tennis elbow'],
                                     'answer': 'A) Ureteric colic',
                                     'explanation': 'Ureteric stone pain radiates loin to groin.'},
                                    {'question': 'First imaging often used for stones in '
                                                 'non-pregnant adults?',
                                     'options': ['A) Non-contrast CT KUB',
                                                 'B) PET scan',
                                                 'C) Mammogram',
                                                 'D) EEG'],
                                     'answer': 'A) Non-contrast CT KUB',
                                     'explanation': 'Non-contrast CT is standard for stones.'}],
                           'medium': [{'question': 'Painless gross hematuria in an older smoker is '
                                                   'concerning for?',
                                       'options': ['A) Bladder cancer',
                                                   'B) Simple stress incontinence',
                                                   'C) Hydrocele only',
                                                   'D) Uncomplicated hemorrhoids'],
                                       'answer': 'A) Bladder cancer',
                                       'explanation': 'Needs urologic hematuria workup.'},
                                      {'question': 'Fever + flank pain + UTI signs suggest?',
                                       'options': ['A) Pyelonephritis',
                                                   'B) Simple urethritis without fever always',
                                                   'C) BPH only',
                                                   'D) Varicocele'],
                                       'answer': 'A) Pyelonephritis',
                                       'explanation': 'Upper tract infection with systemic '
                                                      'features.'},
                                      {'question': 'Testicular torsion key theme is?',
                                       'options': ['A) Time-critical ischemia',
                                                   'B) Always observe for weeks',
                                                   'C) Antibiotics alone always cure',
                                                   'D) Only occurs in elderly women'],
                                       'answer': 'A) Time-critical ischemia',
                                       'explanation': 'Do not delay surgical exploration if high '
                                                      'suspicion.'}],
                           'hard': [{'question': 'A junior colleague asks for the single best '
                                                 'answer. Stone with obstructed infected kidney '
                                                 'requires? Choose the most accurate option and '
                                                 'beware of near-miss distractors.',
                                     'options': ['A) Urgent decompression + antibiotics',
                                                 'B) Outpatient observation only',
                                                 'C) No cultures ever',
                                                 'D) Immediate chemotherapy'],
                                     'answer': 'A) Urgent decompression + antibiotics',
                                     'explanation': 'Obstructed pyelonephritis is urosepsis risk.'},
                                    {'question': 'A junior colleague asks for the single best '
                                                 'answer. Post-obstructive diuresis occurs after? '
                                                 'Choose the most accurate option and beware of '
                                                 'near-miss distractors.',
                                     'options': ['A) Relief of chronic urinary obstruction',
                                                 'B) Starting beta-blockers',
                                                 'C) Cataract surgery',
                                                 'D) Routine vaccination'],
                                     'answer': 'A) Relief of chronic urinary obstruction',
                                     'explanation': 'Monitor fluids/electrolytes after '
                                                    'decompression.'},
                                    {'question': 'A junior colleague asks for the single best '
                                                 'answer. High riding testis and absent '
                                                 'cremasteric reflex suggest? Choose the most '
                                                 'accurate option and beware of near-miss '
                                                 'distractors.',
                                     'options': ['A) Torsion until proven otherwise',
                                                 'B) Hydrocele only',
                                                 'C) Epididymitis always',
                                                 'D) Inguinal hernia only'],
                                     'answer': 'A) Torsion until proven otherwise',
                                     'explanation': 'Surgical emergency.'}],
                           'extreme': [{'question': 'In a high-stakes ward scenario with '
                                                    'incomplete data, which statement is MOST '
                                                    'correct? Fournier gangrene is? Avoid '
                                                    'premature therapies that could harm if a '
                                                    'critical differential remains open.',
                                        'options': ['A) Necrotizing infection of '
                                                    'perineum/genitalia needing urgent surgery',
                                                    'B) Mild balanitis always',
                                                    'C) Only a viral exanthem',
                                                    'D) A type of kidney stone'],
                                        'answer': 'A) Necrotizing infection of perineum/genitalia '
                                                  'needing urgent surgery',
                                        'explanation': 'Surgical emergency with broad '
                                                       'antibiotics.'},
                                       {'question': 'In a high-stakes ward scenario with '
                                                    'incomplete data, which statement is MOST '
                                                    'correct? Autonomic dysreflexia in spinal cord '
                                                    'injury with bladder distension can cause? '
                                                    'Avoid premature therapies that could harm if '
                                                    'a critical differential remains open.',
                                        'options': ['A) Dangerous hypertension',
                                                    'B) Only mild thirst',
                                                    'C) Cataracts',
                                                    'D) Alopecia'],
                                        'answer': 'A) Dangerous hypertension',
                                        'explanation': 'Relieve noxious stimulus (often bladder) '
                                                       'urgently.'},
                                       {'question': 'In a high-stakes ward scenario with '
                                                    'incomplete data, which statement is MOST '
                                                    'correct? A trauma patient with pelvic '
                                                    'fracture and blood at meatus should avoid? '
                                                    'Avoid premature therapies that could harm if '
                                                    'a critical differential remains open.',
                                        'options': ['A) Blind urethral catheterization before '
                                                    'assessing urethral injury',
                                                    'B) Pelvic binder when indicated',
                                                    'C) Trauma ABCs',
                                                    'D) Crossmatch'],
                                        'answer': 'A) Blind urethral catheterization before '
                                                  'assessing urethral injury',
                                        'explanation': 'Suspect urethral injury; retrograde '
                                                       'urethrogram pathway.'}]},
             'cases': {'easy': [{'title': 'Sudden Flank Pain',
                                 'stem': 'A 30-year-old man has sudden severe left flank pain '
                                         'radiating to the groin and cannot find a comfortable '
                                         'position. Dipstick shows blood.',
                                 'question': 'Likely diagnosis?',
                                 'answer': 'Ureteric colic from a stone.',
                                 'discussion': 'Analgesia and imaging; watch for '
                                               'infection/obstruction.',
                                 'book_hint': 'Campbell-Walsh-Wein Urology'}],
                       'medium': [{'title': 'Feverish Flank Pain',
                                   'stem': 'A 27-year-old woman has fever, vomiting, and right '
                                           'flank tenderness with nitrite-positive urine.',
                                   'question': 'Diagnosis?',
                                   'answer': 'Acute pyelonephritis.',
                                   'discussion': 'Cultures + antibiotics; image if not improving '
                                                 'or complicated.',
                                   'book_hint': 'Campbell-Walsh-Wein Urology'}],
                       'hard': [{'title': 'Obstructing Stone + Fever',
                                 'stem': 'A 45-year-old with a 9 mm proximal ureteric stone '
                                         'develops fever, rigors, and hypotension. Decide the '
                                         'highest-yield urgent concept before results return.',
                                 'question': 'Priority concept?',
                                 'answer': 'Treat as obstructed infected kidney: resuscitation, '
                                           'antibiotics, urgent drainage (stent/nephrostomy).',
                                 'discussion': 'Delay can lead to septic shock.',
                                 'book_hint': 'Campbell-Walsh-Wein Urology'}],
                       'extreme': [{'title': 'Trauma + Blood at Meatus',
                                    'stem': 'A motorcyclist with pelvic fracture has blood at the '
                                            'urethral meatus and a high-riding prostate on exam. '
                                            'The intern reaches for a Foley catheter. Avoid '
                                            'interventions that could worsen an unexcluded '
                                            'catastrophic differential.',
                                    'question': 'What is the correct concept?',
                                    'answer': 'Do not attempt blind catheterization; evaluate for '
                                              'urethral injury first while continuing trauma '
                                              'resuscitation.',
                                    'discussion': 'Wrong catheterization can convert partial to '
                                                  'complete urethral injury.',
                                    'book_hint': 'Campbell-Walsh-Wein Urology'}]}},
 'neurology': {'label': 'Neurology',
               'books': ["Adams and Victor's Principles of Neurology",
                         "Harrison's — Neurology",
                         'Clinical Neurology — Simon R. / Brazis'],
               'pdf_notes': ['Stroke = sudden focal deficit — time is brain; use FAST/NIHSS '
                             'pathways.',
                             'UMN vs LMN: spasticity/hyperreflexia vs '
                             'flaccid/hyporeflexia/fasciculations.',
                             'SAH: thunderclap headache — urgent non-contrast CT ± LP.',
                             'Meningitis: fever, neck stiffness, altered mentation — early '
                             'antibiotics.',
                             'Migraine: unilateral throbbing ± nausea/photo-phonophobia; rule out '
                             'red flags.'],
               'questions': {'easy': [{'question': 'Sudden face/arm weakness with speech '
                                                   'difficulty suggests?',
                                       'options': ['A) Stroke until proven otherwise',
                                                   'B) Only anxiety',
                                                   'C) Cataract',
                                                   'D) Tinea'],
                                       'answer': 'A) Stroke until proven otherwise',
                                       'explanation': 'FAST pathway.'},
                                      {'question': 'Meningism features include?',
                                       'options': ['A) Neck stiffness with fever/headache',
                                                   'B) Only ankle itch',
                                                   'C) Only tinnitus',
                                                   'D) Clubbing alone'],
                                       'answer': 'A) Neck stiffness with fever/headache',
                                       'explanation': 'Consider meningitis.'},
                                      {'question': 'UMN signs include?',
                                       'options': ['A) Babinski and spasticity',
                                                   'B) Fasciculations and hyporeflexia',
                                                   'C) Only sensory loss without motor change',
                                                   'D) Soft tissue crepitus'],
                                       'answer': 'A) Babinski and spasticity',
                                       'explanation': 'UMN pattern.'}],
                             'medium': [{'question': 'Thunderclap headache first exclude?',
                                         'options': ['A) SAH',
                                                     'B) Tension headache only',
                                                     'C) Sinusitis always',
                                                     'D) Uncomplicated migraine always'],
                                         'answer': 'A) SAH',
                                         'explanation': 'CT ± LP.'},
                                        {'question': 'Absence seizures are most typical in?',
                                         'options': ['A) Children with brief staring spells',
                                                     'B) Only elderly with AF',
                                                     'C) Only neonates with jaundice',
                                                     'D) Only migraine with aura'],
                                         'answer': 'A) Children with brief staring spells',
                                         'explanation': 'Generalized absence pattern.'},
                                        {'question': 'Parkinsonism core motor feature is?',
                                         'options': ['A) Bradykinesia',
                                                     'B) Only hyperreflexia',
                                                     'C) Flaccid paralysis',
                                                     'D) Intention tremor only'],
                                         'answer': 'A) Bradykinesia',
                                         'explanation': 'Bradykinesia is required.'}],
                             'hard': [{'question': 'A junior colleague asks for the single best '
                                                   'answer. Status epilepticus initial concept? '
                                                   'Choose the most accurate option and beware of '
                                                   'near-miss distractors.',
                                       'options': ['A) ABCs + benzodiazepine pathway then escalate '
                                                   'ASM',
                                                   'B) Wait hours without treatment',
                                                   'C) Only oral vitamins',
                                                   'D) Immediate chemotherapy'],
                                       'answer': 'A) ABCs + benzodiazepine pathway then escalate '
                                                 'ASM',
                                       'explanation': 'Follow status protocol.'},
                                      {'question': 'A junior colleague asks for the single best '
                                                   'answer. Crossed cranial nerve + contralateral '
                                                   'body signs localize to? Choose the most '
                                                   'accurate option and beware of near-miss '
                                                   'distractors.',
                                       'options': ['A) Brainstem',
                                                   'B) Distal nerve only',
                                                   'C) Muscle only',
                                                   'D) Middle ear only'],
                                       'answer': 'A) Brainstem',
                                       'explanation': 'Crossed findings = brainstem.'},
                                      {'question': 'A junior colleague asks for the single best '
                                                   'answer. Myasthenia gravis fatigable weakness '
                                                   'often involves? Choose the most accurate '
                                                   'option and beware of near-miss distractors.',
                                       'options': ['A) Eyes/bulbar muscles',
                                                   'B) Only calf hypertrophy',
                                                   'C) Only bones',
                                                   'D) Only skin'],
                                       'answer': 'A) Eyes/bulbar muscles',
                                       'explanation': 'Fatigable ptosis/diplopia classic.'}],
                             'extreme': [{'question': 'In a high-stakes ward scenario with '
                                                      'incomplete data, which statement is MOST '
                                                      'correct? Spinal cord compression with '
                                                      'saddle anesthesia and retention needs? '
                                                      'Avoid premature therapies that could harm '
                                                      'if a critical differential remains open.',
                                          'options': ['A) Urgent imaging and decompression pathway',
                                                      'B) Routine physio only for weeks',
                                                      'C) Only eye drops',
                                                      'D) No neurological exam'],
                                          'answer': 'A) Urgent imaging and decompression pathway',
                                          'explanation': 'Cauda equina/cord emergency.'},
                                         {'question': 'In a high-stakes ward scenario with '
                                                      'incomplete data, which statement is MOST '
                                                      'correct? Locked-in syndrome typically '
                                                      'localizes to? Avoid premature therapies '
                                                      'that could harm if a critical differential '
                                                      'remains open.',
                                          'options': ['A) Bilateral ventral pons',
                                                      'B) Cerebellar hemisphere only',
                                                      'C) Optic nerve only',
                                                      'D) Sciatic nerve'],
                                          'answer': 'A) Bilateral ventral pons',
                                          'explanation': 'Vertical eye movements may be spared.'},
                                         {'question': 'In a high-stakes ward scenario with '
                                                      'incomplete data, which statement is MOST '
                                                      'correct? NMDA-receptor encephalitis '
                                                      'association often discussed with? Avoid '
                                                      'premature therapies that could harm if a '
                                                      'critical differential remains open.',
                                          'options': ['A) Ovarian teratoma in young women',
                                                      'B) Only gout',
                                                      'C) Only otosclerosis',
                                                      'D) Only acne'],
                                          'answer': 'A) Ovarian teratoma in young women',
                                          'explanation': 'Autoimmune encephalitis theme.'}]},
               'cases': {'easy': [{'title': 'Sudden Weakness',
                                   'stem': 'A 70-year-old develops sudden right arm/leg weakness '
                                           'and aphasia 40 minutes ago. Glucose is normal.',
                                   'question': 'Priority diagnosis pathway?',
                                   'answer': 'Acute stroke — activate stroke pathway.',
                                   'discussion': 'Time-critical imaging and reperfusion '
                                                 'eligibility.',
                                   'book_hint': "Adams and Victor / Harrison's Neurology"}],
                         'medium': [{'title': 'Worst Headache',
                                     'stem': 'A 45-year-old has the worst headache of life peaking '
                                             'in seconds with neck stiffness.',
                                     'question': 'What must be excluded?',
                                     'answer': 'Subarachnoid hemorrhage.',
                                     'discussion': 'Urgent non-contrast CT ± LP.',
                                     'book_hint': "Adams and Victor / Harrison's Neurology"}],
                         'hard': [{'title': 'Fatigable Diplopia',
                                   'stem': 'A 34-year-old has fatigable ptosis and diplopia worse '
                                           'at night, improving with rest. Ice-pack test helps '
                                           'transiently. Labs and imaging are pending; you must '
                                           'choose the safest next clinical concept.',
                                   'question': 'Likely diagnosis?',
                                   'answer': 'Myasthenia gravis.',
                                   'discussion': 'Avoid certain drugs; assess respiratory '
                                                 'function; specialty care.',
                                   'book_hint': "Adams and Victor / Harrison's Neurology"}],
                         'extreme': [{'title': 'Young Woman with Psychiatric then Seizure Cascade',
                                      'stem': 'A 24-year-old develops subacute psychosis, '
                                              'dyskinesias, autonomic instability, and refractory '
                                              'seizures. CT finds an ovarian teratoma. Multiple '
                                              'teams are involved; prioritize life/limb/vision '
                                              'threats and avoid harmful premature therapies.',
                                      'question': 'Syndrome to consider?',
                                      'answer': 'Anti-NMDA receptor encephalitis — immunotherapy + '
                                                'tumor removal pathway.',
                                      'discussion': 'Early recognition changes outcome.',
                                      'book_hint': "Adams and Victor / Harrison's Neurology"}]}},
 'pulmonology': {'label': 'Pulmonology',
                 'books': ["West's Respiratory Physiology",
                           "Harrison's — Respiratory Medicine",
                           "Crofton and Douglas's Respiratory Diseases"],
                 'pdf_notes': ['CAP: S. pneumoniae most common; assess CURB-65 severity.',
                               'Asthma: reversible obstruction; COPD: largely irreversible.',
                               'PE: sudden dyspnea/pleuritic pain post-risk — Wells + CT PA '
                               'pathway.',
                               'Tension pneumothorax: shock + tracheal deviation — immediate '
                               'decompression.',
                               'TB: chronic cough, night sweats, weight loss — AFB/GeneXpert as '
                               'available.'],
                 'questions': {'easy': [{'question': 'Common CAP organism?',
                                         'options': ['A) S. pneumoniae',
                                                     'B) HIV only',
                                                     'C) Dermatophytes',
                                                     'D) Plasmodium only'],
                                         'answer': 'A) S. pneumoniae',
                                         'explanation': 'Leading CAP cause.'},
                                        {'question': 'Asthma is characterized by?',
                                         'options': ['A) Reversible airway obstruction',
                                                     'B) Always fixed irreversible obstruction '
                                                     'only',
                                                     'C) Only pleural plaques',
                                                     'D) Only clubbing always'],
                                         'answer': 'A) Reversible airway obstruction',
                                         'explanation': 'Hyperresponsiveness + reversibility.'},
                                        {'question': 'SpO2 measures?',
                                         'options': ['A) Oxygen saturation roughly',
                                                     'B) PaCO2 directly',
                                                     'C) Hemoglobin electrophoresis',
                                                     'D) Peak cortisol'],
                                         'answer': 'A) Oxygen saturation roughly',
                                         'explanation': 'Pulse oximetry estimate.'}],
                               'medium': [{'question': 'CURB-65 assesses?',
                                           'options': ['A) CAP severity',
                                                       'B) Cataract density',
                                                       'C) Bone age',
                                                       'D) Acne severity'],
                                           'answer': 'A) CAP severity',
                                           'explanation': 'Confusion, Urea, RR, BP, age.'},
                                          {'question': 'Wells score helps for?',
                                           'options': ['A) PE probability',
                                                       'B) Appendicitis only',
                                                       'C) Melanoma only',
                                                       'D) Otitis media'],
                                           'answer': 'A) PE probability',
                                           'explanation': 'Guides D-dimer vs CT PA.'},
                                          {'question': 'COPD oxygen target in many retainers is '
                                                       'often?',
                                           'options': ['A) Controlled target (e.g. 88–92%) per '
                                                       'protocol',
                                                       'B) Always 100% indefinitely without '
                                                       'assessment',
                                                       'C) Never give oxygen',
                                                       'D) Only room air if SpO2 70%'],
                                           'answer': 'A) Controlled target (e.g. 88–92%) per '
                                                     'protocol',
                                           'explanation': 'Avoid worsening hypercapnia.'}],
                               'hard': [{'question': 'A junior colleague asks for the single best '
                                                     'answer. Tension pneumothorax treatment '
                                                     'concept? Choose the most accurate option and '
                                                     'beware of near-miss distractors.',
                                         'options': ['A) Immediate decompression',
                                                     'B) Wait for CT before any action if crashing',
                                                     'C) Only nebulizers',
                                                     'D) Diuretics first'],
                                         'answer': 'A) Immediate decompression',
                                         'explanation': 'Clinical diagnosis if peri-arrest.'},
                                        {'question': 'A junior colleague asks for the single best '
                                                     "answer. Light's criteria relate to? Choose "
                                                     'the most accurate option and beware of '
                                                     'near-miss distractors.',
                                         'options': ['A) Pleural effusion exudate vs transudate',
                                                     'B) Stone composition',
                                                     'C) Thyroid nodules only',
                                                     'D) Fracture classification'],
                                         'answer': 'A) Pleural effusion exudate vs transudate',
                                         'explanation': 'Protein/LDH ratios.'},
                                        {'question': 'A junior colleague asks for the single best '
                                                     'answer. Massive hemoptysis priority is? '
                                                     'Choose the most accurate option and beware '
                                                     'of near-miss distractors.',
                                         'options': ['A) Airway protection + side-down of bleeding '
                                                     'lung',
                                                     'B) Immediate outpatient follow-up only',
                                                     'C) Only cough syrup',
                                                     'D) Ignore if BP normal'],
                                         'answer': 'A) Airway protection + side-down of bleeding '
                                                   'lung',
                                         'explanation': 'Life-threatening bleed pathway.'}],
                               'extreme': [{'question': 'In a high-stakes ward scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? ARDS Berlin concept includes? '
                                                        'Avoid premature therapies that could harm '
                                                        'if a critical differential remains open.',
                                            'options': ['A) Acute hypoxemic respiratory failure '
                                                        'with bilateral opacities not fully '
                                                        'explained by HF',
                                                        'B) Only chronic emphysema',
                                                        'C) Simple viral URI',
                                                        'D) Only pneumothorax'],
                                            'answer': 'A) Acute hypoxemic respiratory failure with '
                                                      'bilateral opacities not fully explained by '
                                                      'HF',
                                            'explanation': 'Lung-protective ventilation themes.'},
                                           {'question': 'In a high-stakes ward scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Fat embolism triad after '
                                                        'fracture? Avoid premature therapies that '
                                                        'could harm if a critical differential '
                                                        'remains open.',
                                            'options': ['A) Respiratory distress, neuro change, '
                                                        'petechiae',
                                                        'B) Only jaundice triad of Charcot',
                                                        'C) Only itching',
                                                        'D) Only bradycardia'],
                                            'answer': 'A) Respiratory distress, neuro change, '
                                                      'petechiae',
                                            'explanation': 'After long-bone fracture.'},
                                           {'question': 'In a high-stakes ward scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Bronchial carcinoid can cause '
                                                        'which syndrome theme? Avoid premature '
                                                        'therapies that could harm if a critical '
                                                        'differential remains open.',
                                            'options': ['A) Carcinoid syndrome with '
                                                        'flushing/diarrhea when metastatic',
                                                        'B) Only acne inversa',
                                                        'C) Only gout',
                                                        'D) Only cataracts'],
                                            'answer': 'A) Carcinoid syndrome with '
                                                      'flushing/diarrhea when metastatic',
                                            'explanation': 'Neuroendocrine tumor theme.'}]},
                 'cases': {'easy': [{'title': 'Fever + Productive Cough',
                                     'stem': 'A 60-year-old has fever, rusty sputum, and focal '
                                             'crackles. CXR shows lobar consolidation.',
                                     'question': 'Likely diagnosis?',
                                     'answer': 'Community-acquired pneumonia.',
                                     'discussion': 'Severity score + antibiotics + oxygen if '
                                                   'needed.',
                                     'book_hint': "Harrison's Respiratory / West"}],
                           'medium': [{'title': 'Post-Flight Dyspnea',
                                       'stem': 'A 42-year-old after a long flight has sudden '
                                               'dyspnea and pleuritic pain. SpO2 91%.',
                                       'question': 'Top diagnosis to exclude?',
                                       'answer': 'Pulmonary embolism.',
                                       'discussion': 'Risk stratify and image/treat per pathway.',
                                       'book_hint': "Harrison's Respiratory / West"}],
                           'hard': [{'title': 'Asthma Near-Fatal',
                                     'stem': 'A teen with asthma is silent-chested, hypoxic, and '
                                             'tiring with rising CO2. Labs and imaging are '
                                             'pending; you must choose the safest next clinical '
                                             'concept.',
                                     'question': 'What does this imply?',
                                     'answer': 'Life-threatening asthma — escalate to emergency '
                                               'airway/ventilatory support pathway.',
                                     'discussion': 'A silent chest is ominous.',
                                     'book_hint': "Harrison's Respiratory / West"}],
                           'extreme': [{'title': 'Post-Op Hypoxemia + Petechiae',
                                        'stem': 'Day 2 after femoral nailing, a young man becomes '
                                                'confused and hypoxic with axillary petechiae. CT '
                                                'PA is negative for large PE. Multiple teams are '
                                                'involved; prioritize life/limb/vision threats and '
                                                'avoid harmful premature therapies.',
                                        'question': 'Consider?',
                                        'answer': 'Fat embolism syndrome — supportive care and '
                                                  'orthopaedic/ICU collaboration.',
                                        'discussion': 'Classic triad after long-bone '
                                                      'instrumentation.',
                                        'book_hint': "Harrison's Respiratory / West"}]}},
 'gastroenterology': {'label': 'Gastroenterology',
                      'books': ["Sleisenger and Fordtran's Gastrointestinal and Liver Disease",
                                "Harrison's — Gastroenterology",
                                'Bailey & Love — Abdominal surgery chapters'],
                      'pdf_notes': ['Charcot triad = cholangitis; Reynolds pentad adds hypotension '
                                    '+ confusion.',
                                    'H. pylori → PUD; test-and-treat in appropriate settings.',
                                    'Pancreatitis: epigastric pain to back + ↑ lipase; fluids and '
                                    'support.',
                                    "Appendicitis: periumbilical→RLQ pain, McBurney's tenderness.",
                                    'Cirrhosis complications: varices, ascites, encephalopathy, '
                                    'HCC surveillance.'],
                      'questions': {'easy': [{'question': 'Charcot triad indicates?',
                                              'options': ['A) Ascending cholangitis',
                                                          'B) Simple IBS',
                                                          'C) Hemorrhoids only',
                                                          'D) Aphthous ulcer only'],
                                              'answer': 'A) Ascending cholangitis',
                                              'explanation': 'RUQ pain, fever, jaundice.'},
                                             {'question': 'H. pylori is linked to?',
                                              'options': ['A) Peptic ulcer disease',
                                                          'B) Osteosarcoma',
                                                          'C) Cataract',
                                                          'D) Otitis externa'],
                                              'answer': 'A) Peptic ulcer disease',
                                              'explanation': 'Major PUD cause.'},
                                             {'question': "McBurney's point relates to?",
                                              'options': ['A) Appendicitis',
                                                          'B) Thyroid',
                                                          'C) Meniscus',
                                                          'D) Retina'],
                                              'answer': 'A) Appendicitis',
                                              'explanation': 'RLQ tenderness landmark.'}],
                                    'medium': [{'question': 'Pancreatitis pain often radiates to?',
                                                'options': ['A) Back',
                                                            'B) Sole of foot only',
                                                            'C) Ear lobe only',
                                                            'D) Vertex only'],
                                                'answer': 'A) Back',
                                                'explanation': 'Epigastric to back.'},
                                               {'question': 'Variceal bleed risk is highest in?',
                                                'options': ['A) Portal hypertension/cirrhosis',
                                                            'B) Simple gastritis always',
                                                            'C) Uncomplicated hemorrhoids only',
                                                            'D) Food allergy alone'],
                                                'answer': 'A) Portal hypertension/cirrhosis',
                                                'explanation': 'Airway + resuscitation + endoscopy '
                                                               'pathway.'},
                                               {'question': 'IBD alarm features include?',
                                                'options': ['A) Bleeding, weight loss, nocturnal '
                                                            'diarrhea',
                                                            'B) Only mild bloating after beans',
                                                            'C) Only hiccups',
                                                            'D) Only burping'],
                                                'answer': 'A) Bleeding, weight loss, nocturnal '
                                                          'diarrhea',
                                                'explanation': 'Not simple IBS.'}],
                                    'hard': [{'question': 'A junior colleague asks for the single '
                                                          'best answer. Reynolds pentad adds what '
                                                          'to Charcot? Choose the most accurate '
                                                          'option and beware of near-miss '
                                                          'distractors.',
                                              'options': ['A) Hypotension and confusion',
                                                          'B) Only pruritus',
                                                          'C) Only tinnitus',
                                                          'D) Only clubbing'],
                                              'answer': 'A) Hypotension and confusion',
                                              'explanation': 'Severe cholangitis/sepsis.'},
                                             {'question': 'A junior colleague asks for the single '
                                                          'best answer. SBP in ascites is '
                                                          'diagnosed by? Choose the most accurate '
                                                          'option and beware of near-miss '
                                                          'distractors.',
                                              'options': ['A) Ascitic fluid PMN count threshold + '
                                                          'clinical context',
                                                          'B) Only CXR',
                                                          'C) Only ECG',
                                                          'D) Only throat swab'],
                                              'answer': 'A) Ascitic fluid PMN count threshold + '
                                                        'clinical context',
                                              'explanation': 'Tap early if suspected.'},
                                             {'question': 'A junior colleague asks for the single '
                                                          'best answer. Boerhaave syndrome is? '
                                                          'Choose the most accurate option and '
                                                          'beware of near-miss distractors.',
                                              'options': ['A) Esophageal perforation after '
                                                          'vomiting',
                                                          'B) Simple heartburn',
                                                          'C) Gallstone ileus only',
                                                          'D) Meckel diverticulum only'],
                                              'answer': 'A) Esophageal perforation after vomiting',
                                              'explanation': 'Mediastinitis emergency.'}],
                                    'extreme': [{'question': 'In a high-stakes ward scenario with '
                                                             'incomplete data, which statement is '
                                                             'MOST correct? Mesenteric ischemia '
                                                             'classic risk? Avoid premature '
                                                             'therapies that could harm if a '
                                                             'critical differential remains open.',
                                                 'options': ['A) AF with sudden severe pain out of '
                                                             'proportion',
                                                             'B) Only constipation in teens',
                                                             'C) Only hemorrhoids',
                                                             'D) Only food poisoning mild'],
                                                 'answer': 'A) AF with sudden severe pain out of '
                                                           'proportion',
                                                 'explanation': 'Surgical catastrophe risk.'},
                                                {'question': 'In a high-stakes ward scenario with '
                                                             'incomplete data, which statement is '
                                                             'MOST correct? Toxic megacolon is a '
                                                             'complication of? Avoid premature '
                                                             'therapies that could harm if a '
                                                             'critical differential remains open.',
                                                 'options': ['A) Severe colitis (e.g., IBD/C. '
                                                             'diff)',
                                                             'B) Simple GERD',
                                                             'C) Uncomplicated PUD without colitis',
                                                             'D) Gallbladder polyp only'],
                                                 'answer': 'A) Severe colitis (e.g., IBD/C. diff)',
                                                 'explanation': 'May need emergency surgery.'},
                                                {'question': 'In a high-stakes ward scenario with '
                                                             'incomplete data, which statement is '
                                                             'MOST correct? Budd-Chiari involves? '
                                                             'Avoid premature therapies that could '
                                                             'harm if a critical differential '
                                                             'remains open.',
                                                 'options': ['A) Hepatic venous outflow '
                                                             'obstruction',
                                                             'B) Portal vein only always',
                                                             'C) Cystic duct stone only',
                                                             'D) Pancreatic divisum only'],
                                                 'answer': 'A) Hepatic venous outflow obstruction',
                                                 'explanation': 'Hepatomegaly/ascites/liver '
                                                                'injury.'}]},
                      'cases': {'easy': [{'title': 'RUQ Pain + Jaundice + Fever',
                                          'stem': 'A 50-year-old woman has RUQ pain, fever, and '
                                                  'jaundice.',
                                          'question': 'Likely diagnosis?',
                                          'answer': 'Ascending cholangitis.',
                                          'discussion': 'Antibiotics + biliary drainage.',
                                          'book_hint': "Sleisenger / Harrison's GI"}],
                                'medium': [{'title': 'Alcohol + Epigastric Pain',
                                            'stem': 'A 40-year-old with heavy alcohol use has '
                                                    'severe epigastric pain to the back and lipase '
                                                    '3× ULN.',
                                            'question': 'Diagnosis?',
                                            'answer': 'Acute pancreatitis.',
                                            'discussion': 'Supportive fluids/analgesia; find '
                                                          'cause.',
                                            'book_hint': "Sleisenger / Harrison's GI"}],
                                'hard': [{'title': 'Coffee-Ground Emesis + Shock in Cirrhosis',
                                          'stem': 'A cirrhotic patient vomits blood and is '
                                                  'hypotensive with tense ascites. Labs and '
                                                  'imaging are pending; you must choose the safest '
                                                  'next clinical concept.',
                                          'question': 'Priorities?',
                                          'answer': 'ABCs/resuscitation, restrict transfusion '
                                                    'targets per protocol, reverse coagulopathy '
                                                    'thoughtfully, antibiotics, '
                                                    'terlipressin/octreotide pathways, urgent '
                                                    'endoscopy.',
                                          'discussion': 'Variceal bleed until proven otherwise.',
                                          'book_hint': "Sleisenger / Harrison's GI"}],
                                'extreme': [{'title': 'Pain Out of Proportion',
                                             'stem': 'An elderly patient with AF develops sudden '
                                                     'severe abdominal pain but a soft abdomen '
                                                     'early on. Lactate rises. Multiple teams are '
                                                     'involved; prioritize life/limb/vision '
                                                     'threats and avoid harmful premature '
                                                     'therapies.',
                                             'question': 'Fear which diagnosis?',
                                             'answer': 'Acute mesenteric ischemia — urgent CT '
                                                       'angiography and surgical/interventional '
                                                       'pathway.',
                                             'discussion': 'Early exam can be falsely reassuring.',
                                             'book_hint': "Sleisenger / Harrison's GI"}]}},
 'endocrinology': {'label': 'Endocrinology',
                   'books': ['Williams Textbook of Endocrinology',
                             "Harrison's — Endocrinology",
                             "Greenspan's Basic & Clinical Endocrinology"],
                   'pdf_notes': ['DKA: hyperglycemia + ketones + acidosis; fluids, insulin, K+.',
                                 'Hashimoto → hypothyroidism; Graves → hyperthyroidism.',
                                 'Metformin first-line for many T2DM patients if eGFR allows.',
                                 'Hypocalcemia: Chvostek/Trousseau; check Mg and PTH.',
                                 'Adrenal crisis: shock + hyponatremia/hyperkalemia — give '
                                 'steroids/fluids urgently.'],
                   'questions': {'easy': [{'question': 'DKA includes?',
                                           'options': ['A) Hyperglycemia + ketones + acidosis',
                                                       'B) Only hypoglycemia',
                                                       'C) Only alkalosis',
                                                       'D) Only hypercalcemia'],
                                           'answer': 'A) Hyperglycemia + ketones + acidosis',
                                           'explanation': 'Define DKA triad.'},
                                          {'question': 'First-line drug often for T2DM?',
                                           'options': ['A) Metformin if suitable',
                                                       'B) Propylthiouracil',
                                                       'C) Desmopressin',
                                                       'D) Allopurinol'],
                                           'answer': 'A) Metformin if suitable',
                                           'explanation': 'Common first-line.'},
                                          {'question': 'Primary hypothyroidism labs usually show?',
                                           'options': ['A) High TSH, low free T4',
                                                       'B) Low TSH, high free T4',
                                                       'C) Normal everything always',
                                                       'D) Only high cortisol'],
                                           'answer': 'A) High TSH, low free T4',
                                           'explanation': 'Primary thyroid failure.'}],
                                 'medium': [{'question': 'Chvostek/Trousseau suggest?',
                                             'options': ['A) Hypocalcemia',
                                                         'B) Hypernatremia only',
                                                         'C) Hypoglycemia only',
                                                         'D) Hyperkalemia only'],
                                             'answer': 'A) Hypocalcemia',
                                             'explanation': 'Neuromuscular irritability.'},
                                            {'question': 'Graves disease is a cause of?',
                                             'options': ['A) Hyperthyroidism',
                                                         'B) Primary adrenal failure only',
                                                         'C) DI only',
                                                         'D) Hypoparathyroidism only'],
                                             'answer': 'A) Hyperthyroidism',
                                             'explanation': 'Autoimmune hyperthyroid.'},
                                            {'question': 'Adrenal crisis needs?',
                                             'options': ['A) Urgent steroids + fluids',
                                                         'B) Only thyroxine',
                                                         'C) Only insulin',
                                                         'D) Only calcium channel blockers'],
                                             'answer': 'A) Urgent steroids + fluids',
                                             'explanation': 'Do not delay.'}],
                                 'hard': [{'question': 'A junior colleague asks for the single '
                                                       'best answer. HHS differs from DKA by? '
                                                       'Choose the most accurate option and beware '
                                                       'of near-miss distractors.',
                                           'options': ['A) Marked hyperosmolarity with little/no '
                                                       'ketoacidosis',
                                                       'B) Always heavy ketosis',
                                                       'C) Always in toddlers only',
                                                       'D) Always low glucose'],
                                           'answer': 'A) Marked hyperosmolarity with little/no '
                                                     'ketoacidosis',
                                           'explanation': 'Older T2DM classic.'},
                                          {'question': 'A junior colleague asks for the single '
                                                       'best answer. Sick euthyroid pattern often '
                                                       'shows? Choose the most accurate option and '
                                                       'beware of near-miss distractors.',
                                           'options': ['A) Low T3 in systemic illness without true '
                                                       'thyroid disease necessarily',
                                                       'B) Always Graves',
                                                       'C) Always myxedema coma',
                                                       'D) Always high TSH with high T4'],
                                           'answer': 'A) Low T3 in systemic illness without true '
                                                     'thyroid disease necessarily',
                                           'explanation': 'Interpret TFTs in context.'},
                                          {'question': 'A junior colleague asks for the single '
                                                       'best answer. Pheochromocytoma classic '
                                                       'spells? Choose the most accurate option '
                                                       'and beware of near-miss distractors.',
                                           'options': ['A) Headache, palpitations, sweating + HTN',
                                                       'B) Only constipation',
                                                       'C) Only alopecia',
                                                       'D) Only hearing loss'],
                                           'answer': 'A) Headache, palpitations, sweating + HTN',
                                           'explanation': 'Catecholamine excess.'}],
                                 'extreme': [{'question': 'In a high-stakes ward scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Myxedema coma treatment '
                                                          'concept? Avoid premature therapies that '
                                                          'could harm if a critical differential '
                                                          'remains open.',
                                              'options': ['A) ICU care + thyroid hormone + '
                                                          'supportive care ± steroids if '
                                                          'concurrent AI possible',
                                                          'B) Only outpatient diet advice',
                                                          'C) Immediate radioiodine alone',
                                                          'D) Only beta-blocker'],
                                              'answer': 'A) ICU care + thyroid hormone + '
                                                        'supportive care ± steroids if concurrent '
                                                        'AI possible',
                                              'explanation': 'High mortality if delayed.'},
                                             {'question': 'In a high-stakes ward scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Thyroid storm '
                                                          'scoring/clinical diagnosis needs? Avoid '
                                                          'premature therapies that could harm if '
                                                          'a critical differential remains open.',
                                              'options': ['A) Severe thyrotoxicosis + systemic '
                                                          'decompensation',
                                                          'B) Mild TSH suppression only',
                                                          'C) Only goiter without symptoms',
                                                          'D) Only cold nodule'],
                                              'answer': 'A) Severe thyrotoxicosis + systemic '
                                                        'decompensation',
                                              'explanation': 'Multimodal therapy.'},
                                             {'question': 'In a high-stakes ward scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Insulinoma Whipple triad? '
                                                          'Avoid premature therapies that could '
                                                          'harm if a critical differential remains '
                                                          'open.',
                                              'options': ['A) Symptoms of hypoglycemia, low '
                                                          'glucose, relief with glucose',
                                                          'B) Hyperglycemia triad only',
                                                          'C) Only ketosis without low glucose',
                                                          'D) Only hypertension'],
                                              'answer': 'A) Symptoms of hypoglycemia, low glucose, '
                                                        'relief with glucose',
                                              'explanation': 'Endogenous hyperinsulinism theme.'}]},
                   'cases': {'easy': [{'title': 'Polyuria + Kussmaul',
                                       'stem': 'A teen has polyuria, weight loss, Kussmaul '
                                               'breathing, glucose 430, pH 7.15, urine ketones+++.',
                                       'question': 'Diagnosis?',
                                       'answer': 'DKA.',
                                       'discussion': 'Fluids, insulin, K+ care.',
                                       'book_hint': 'Williams Endocrinology'}],
                             'medium': [{'title': 'Heat Intolerance + Weight Loss',
                                         'stem': 'A 29-year-old has heat intolerance, tremor, '
                                                 'weight loss, diffuse goiter; TSH suppressed, '
                                                 'free T4 high.',
                                         'question': 'Category?',
                                         'answer': 'Thyrotoxicosis (e.g., Graves).',
                                         'discussion': 'Beta-blocker + antithyroid strategy after '
                                                       'workup.',
                                         'book_hint': 'Williams Endocrinology'}],
                             'hard': [{'title': 'Steroid-Dependent Patient Vomiting',
                                       'stem': 'A patient on chronic prednisone for autoimmune '
                                               'disease has gastroenteritis, hypotension, and '
                                               'hyponatremia. Labs and imaging are pending; you '
                                               'must choose the safest next clinical concept.',
                                       'question': 'What emergency?',
                                       'answer': 'Adrenal crisis risk — give stress-dose steroids '
                                                 'and IV fluids while investigating.',
                                       'discussion': 'Never stop chronic steroids abruptly.',
                                       'book_hint': 'Williams Endocrinology'}],
                             'extreme': [{'title': 'Thyroid Storm',
                                          'stem': 'A woman with untreated hyperthyroidism develops '
                                                  'fever, delirium, tachyarrhythmia, and vomiting '
                                                  'after surgery. Multiple teams are involved; '
                                                  'prioritize life/limb/vision threats and avoid '
                                                  'harmful premature therapies.',
                                          'question': 'Management concept?',
                                          'answer': 'Thyroid storm: supportive ICU care, '
                                                    'beta-blockade, antithyroid drugs, iodine '
                                                    'after thionamide, steroids, treat trigger.',
                                          'discussion': 'Delay kills.',
                                          'book_hint': 'Williams Endocrinology'}]}},
 'nephrology': {'label': 'Nephrology',
                'books': ["Brenner & Rector's The Kidney",
                          "Harrison's — Nephrology",
                          'Comprehensive Clinical Nephrology — Feehally'],
                'pdf_notes': ['AKI types: pre-renal, intrinsic (ATN/AIN/GN), post-renal.',
                              'Nephritic vs nephrotic: active sediment/HTN vs heavy protein/edema.',
                              'Diabetic kidney disease: ACEI/ARB cornerstone with glycemic/BP '
                              'control.',
                              'eGFR guides drug dosing and CKD staging.',
                              'Hyperkalemia emergencies: ECG changes → calcium, shift, remove K+.'],
                'questions': {'easy': [{'question': 'eGFR estimates?',
                                        'options': ['A) Kidney filtration function',
                                                    'B) Peak flow',
                                                    'C) Visual acuity',
                                                    'D) Bone density'],
                                        'answer': 'A) Kidney filtration function',
                                        'explanation': 'Creatinine-based estimate.'},
                                       {'question': 'Nephrotic syndrome features heavy?',
                                        'options': ['A) Proteinuria',
                                                    'B) Only hematuria without protein',
                                                    'C) Only glycosuria',
                                                    'D) Only ketonuria'],
                                        'answer': 'A) Proteinuria',
                                        'explanation': 'Also hypoalbuminemia/edema.'},
                                       {'question': 'ACEI/ARB are preferred in?',
                                        'options': ['A) Diabetic albuminuria often',
                                                    'B) Bilateral renal artery stenosis crisis',
                                                    'C) Pregnancy as first choice always',
                                                    'D) Hyperkalemia emergencies as first drug'],
                                        'answer': 'A) Diabetic albuminuria often',
                                        'explanation': 'Renoprotective in albuminuric disease.'}],
                              'medium': [{'question': 'RBC casts suggest?',
                                          'options': ['A) Glomerulonephritis',
                                                      'B) Simple dehydration only',
                                                      'C) Rhabdo only',
                                                      'D) Postrenal stone only'],
                                          'answer': 'A) Glomerulonephritis',
                                          'explanation': 'Active urinary sediment.'},
                                         {'question': 'Post-renal AKI first check?',
                                          'options': ['A) Obstruction (bladder scan/US)',
                                                      'B) Only ANA',
                                                      'C) Only lipid panel',
                                                      'D) Only spirometry'],
                                          'answer': 'A) Obstruction (bladder scan/US)',
                                          'explanation': 'Relieve obstruction.'},
                                         {'question': 'Hyperkalemia with peaked T waves needs?',
                                          'options': ['A) Membrane stabilization (calcium) among '
                                                      'other steps',
                                                      'B) Only oral iron',
                                                      'C) Only thyroxine',
                                                      'D) Only vitamin C'],
                                          'answer': 'A) Membrane stabilization (calcium) among '
                                                    'other steps',
                                          'explanation': 'ECG changes = emergency.'}],
                              'hard': [{'question': 'A junior colleague asks for the single best '
                                                    'answer. ATN muddy brown casts follow? Choose '
                                                    'the most accurate option and beware of '
                                                    'near-miss distractors.',
                                        'options': ['A) Ischemic/toxic tubular injury',
                                                    'B) Only minimal change disease',
                                                    'C) Only pure pre-renal forever',
                                                    'D) Only stones'],
                                        'answer': 'A) Ischemic/toxic tubular injury',
                                        'explanation': 'Intrinsic AKI.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. AIN often linked to? Choose the most '
                                                    'accurate option and beware of near-miss '
                                                    'distractors.',
                                        'options': ['A) Drugs (e.g., antibiotics/NSAIDs/PPIs) + '
                                                    'WBC casts/eosinophiluria themes',
                                                    'B) Only trauma',
                                                    'C) Only diabetes forever',
                                                    'D) Only hypertension alone'],
                                        'answer': 'A) Drugs (e.g., antibiotics/NSAIDs/PPIs) + WBC '
                                                  'casts/eosinophiluria themes',
                                        'explanation': 'Stop culprit.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Indications for urgent dialysis '
                                                    'include? Choose the most accurate option and '
                                                    'beware of near-miss distractors.',
                                        'options': ['A) Severe refractory hyperK/acidosis/volume '
                                                    'overload/uremic emergencies',
                                                    'B) Mild creatinine 1.3 alone always',
                                                    'C) Only microscopic hematuria',
                                                    'D) Only hyponatremia of any degree'],
                                        'answer': 'A) Severe refractory hyperK/acidosis/volume '
                                                  'overload/uremic emergencies',
                                        'explanation': 'AEIOU mnemonic themes.'}],
                              'extreme': [{'question': 'In a high-stakes ward scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Tumor lysis electrolyte pattern? '
                                                       'Avoid premature therapies that could harm '
                                                       'if a critical differential remains open.',
                                           'options': ['A) HyperK, hyperphosphatemia, '
                                                       'hypocalcemia, hyperuricemia',
                                                       'B) Only isolated hyponatremia',
                                                       'C) Only low urea',
                                                       'D) Only metabolic alkalosis always'],
                                           'answer': 'A) HyperK, hyperphosphatemia, hypocalcemia, '
                                                     'hyperuricemia',
                                           'explanation': 'Oncology emergency.'},
                                          {'question': 'In a high-stakes ward scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Hepatorenal syndrome concept? '
                                                       'Avoid premature therapies that could harm '
                                                       'if a critical differential remains open.',
                                           'options': ['A) Functional renal failure in advanced '
                                                       'liver disease after excluding '
                                                       'shock/nephrotoxins/obstruction',
                                                       'B) Always ATN from gentamicin only',
                                                       'C) Always post-renal stone',
                                                       'D) Always AIN'],
                                           'answer': 'A) Functional renal failure in advanced '
                                                     'liver disease after excluding '
                                                     'shock/nephrotoxins/obstruction',
                                           'explanation': 'Vasoconstriction physiology.'},
                                          {'question': 'In a high-stakes ward scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Contrast nephropathy prevention '
                                                       'theme? Avoid premature therapies that '
                                                       'could harm if a critical differential '
                                                       'remains open.',
                                           'options': ['A) Volume status optimization + avoid '
                                                       'unnecessary contrast in high-risk',
                                                       'B) Give NSAIDs before contrast',
                                                       'C) Restrict all fluids always',
                                                       'D) High-dose gentamicin prophylaxis'],
                                           'answer': 'A) Volume status optimization + avoid '
                                                     'unnecessary contrast in high-risk',
                                           'explanation': 'Risk-based prevention.'}]},
                'cases': {'easy': [{'title': 'Oliguria after Diarrhea',
                                    'stem': 'Elderly man with gastroenteritis has dry mucosa and '
                                            'creatinine rise that improves with IV fluids.',
                                    'question': 'AKI type?',
                                    'answer': 'Pre-renal AKI.',
                                    'discussion': 'Restore volume; avoid nephrotoxins.',
                                    'book_hint': "Brenner & Rector / Harrison's"}],
                          'medium': [{'title': 'Edema + 4.8 g/day Protein',
                                      'stem': 'A 21-year-old has periorbital edema, albumin 2.1, '
                                              'proteinuria 4.8 g/day.',
                                      'question': 'Syndrome?',
                                      'answer': 'Nephrotic syndrome.',
                                      'discussion': 'Find cause; manage edema/thrombosis risk.',
                                      'book_hint': "Brenner & Rector / Harrison's"}],
                          'hard': [{'title': 'Pulmonary-Renal Theme',
                                    'stem': 'A young adult has hemoptysis, rising creatinine, and '
                                            'dysmorphic RBCs/RBC casts. Labs and imaging are '
                                            'pending; you must choose the safest next clinical '
                                            'concept.',
                                    'question': 'Concern?',
                                    'answer': 'Pulmonary-renal syndrome (e.g., ANCA/anti-GBM '
                                              'pathways) — urgent specialty labs and therapy.',
                                    'discussion': 'Delay risks irreversible lung/kidney injury.',
                                    'book_hint': "Brenner & Rector / Harrison's"}],
                          'extreme': [{'title': 'Refractory HyperK after TLS',
                                       'stem': 'A leukemia patient day 1 of chemo has K 7.4, '
                                               'phosphate high, calcium low, uric acid high, and '
                                               'ECG changes. Multiple teams are involved; '
                                               'prioritize life/limb/vision threats and avoid '
                                               'harmful premature therapies.',
                                       'question': 'Diagnosis and action concept?',
                                       'answer': 'Tumor lysis syndrome — ECG stabilization, '
                                                 'shift/remove K, rasburicase/allopurinol '
                                                 'pathways, ICU/nephrology, possible dialysis.',
                                       'discussion': 'Anticipate TLS in high-burden tumors.',
                                       'book_hint': "Brenner & Rector / Harrison's"}]}},
 'orthopedics': {'label': 'Orthopedics',
                 'books': ["Apley's System of Orthopaedics and Fractures",
                           "Campbell's Operative Orthopaedics",
                           'Bailey & Love — Orthopaedics chapters'],
                 'pdf_notes': ['Compartment syndrome: pain out of proportion — emergency '
                               'fasciotomy pathway.',
                               'Colles fracture: FOOSH → distal radius dorsal angulation.',
                               'Ottawa ankle rules guide X-ray after sprain.',
                               'Hip fracture: shortened externally rotated limb in elderly fall.',
                               'Fat embolism after long-bone fracture: hypoxia, neuro, petechiae.'],
                 'questions': {'easy': [{'question': 'Ottawa ankle rules help decide need for?',
                                         'options': ['A) X-ray after sprain',
                                                     'B) ECG',
                                                     'C) EEG',
                                                     'D) Spirometry'],
                                         'answer': 'A) X-ray after sprain',
                                         'explanation': 'Reduce unnecessary films.'},
                                        {'question': 'Colles fracture typically follows?',
                                         'options': ['A) FOOSH with distal radius dorsal '
                                                     'angulation',
                                                     'B) Only twisting ankle without fall',
                                                     'C) Only direct shin kick always',
                                                     'D) Only shoulder dislocation'],
                                         'answer': 'A) FOOSH with distal radius dorsal angulation',
                                         'explanation': 'Classic wrist fracture.'},
                                        {'question': 'Open fracture needs?',
                                         'options': ['A) Antibiotics + ortho urgency',
                                                     'B) Only ice for weeks',
                                                     'C) Ignore skin break',
                                                     'D) Only vitamin D'],
                                         'answer': 'A) Antibiotics + ortho urgency',
                                         'explanation': 'Infection risk.'}],
                               'medium': [{'question': 'Compartment syndrome key early feature?',
                                           'options': ['A) Pain out of proportion / pain on '
                                                       'passive stretch',
                                                       'B) Pulselessness always first',
                                                       'C) Only mild ache',
                                                       'D) Only itching'],
                                           'answer': 'A) Pain out of proportion / pain on passive '
                                                     'stretch',
                                           'explanation': 'Pulses may be present.'},
                                          {'question': 'Fat embolism classic setting?',
                                           'options': ['A) After long-bone fracture',
                                                       'B) After cataract surgery only',
                                                       'C) After dental cleaning only',
                                                       'D) After skin tag removal only'],
                                           'answer': 'A) After long-bone fracture',
                                           'explanation': 'Hypoxia, neuro, petechiae.'},
                                          {'question': 'Septic arthritis urgency?',
                                           'options': ['A) Urgent aspiration and antibiotics after '
                                                       'cultures',
                                                       'B) Observe 2 weeks always',
                                                       'C) Only topical cream',
                                                       'D) Only rest forever'],
                                           'answer': 'A) Urgent aspiration and antibiotics after '
                                                     'cultures',
                                           'explanation': 'Joint emergency.'}],
                               'hard': [{'question': 'A junior colleague asks for the single best '
                                                     'answer. Salter-Harris injuries involve? '
                                                     'Choose the most accurate option and beware '
                                                     'of near-miss distractors.',
                                         'options': ['A) Growth plate',
                                                     'B) Only skull sutures',
                                                     'C) Only vertebral discs always',
                                                     'D) Only nails'],
                                         'answer': 'A) Growth plate',
                                         'explanation': 'Pediatric growth disturbance risk.'},
                                        {'question': 'A junior colleague asks for the single best '
                                                     'answer. Cauda equina red flags include? '
                                                     'Choose the most accurate option and beware '
                                                     'of near-miss distractors.',
                                         'options': ['A) Saddle anesthesia + bowel/bladder change',
                                                     'B) Only mild backache after gym',
                                                     'C) Only neck stiffness from cold',
                                                     'D) Only ankle sprain'],
                                         'answer': 'A) Saddle anesthesia + bowel/bladder change',
                                         'explanation': 'Urgent MRI/decomp.'},
                                        {'question': 'A junior colleague asks for the single best '
                                                     'answer. Pathologic fracture suggests? Choose '
                                                     'the most accurate option and beware of '
                                                     'near-miss distractors.',
                                         'options': ['A) Underlying bone weakness '
                                                     '(tumor/osteoporosis/etc.)',
                                                     'B) Only normal bone forever',
                                                     'C) Only ligament sprain',
                                                     'D) Only skin laceration'],
                                         'answer': 'A) Underlying bone weakness '
                                                   '(tumor/osteoporosis/etc.)',
                                         'explanation': 'Investigate cause.'}],
                               'extreme': [{'question': 'In a high-stakes ward scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Necrotizing fasciitis clue? '
                                                        'Avoid premature therapies that could harm '
                                                        'if a critical differential remains open.',
                                            'options': ['A) Pain out of proportion, rapid spread, '
                                                        'systemic toxicity',
                                                        'B) Mild eczema only',
                                                        'C) Only dry skin',
                                                        'D) Only bruise without pain'],
                                            'answer': 'A) Pain out of proportion, rapid spread, '
                                                      'systemic toxicity',
                                            'explanation': 'Surgical emergency.'},
                                           {'question': 'In a high-stakes ward scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Pelvic binder indication theme? '
                                                        'Avoid premature therapies that could harm '
                                                        'if a critical differential remains open.',
                                            'options': ['A) Unstable pelvic fracture with '
                                                        'hemorrhage concern',
                                                        'B) Simple clavicle sprain',
                                                        'C) Finger mallet finger only',
                                                        'D) Only ankle sprain'],
                                            'answer': 'A) Unstable pelvic fracture with hemorrhage '
                                                      'concern',
                                            'explanation': 'Trauma resuscitation.'},
                                           {'question': 'In a high-stakes ward scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Rhabdomyolysis AKI risk from? '
                                                        'Avoid premature therapies that could harm '
                                                        'if a critical differential remains open.',
                                            'options': ['A) Myoglobinuria after crush/extreme '
                                                        'exertion',
                                                        'B) Only dehydration without muscle injury '
                                                        'always',
                                                        'C) Only high calcium diet',
                                                        'D) Only sunlight'],
                                            'answer': 'A) Myoglobinuria after crush/extreme '
                                                      'exertion',
                                            'explanation': 'Fluids + treat cause.'}]},
                 'cases': {'easy': [{'title': 'Elderly Fall + Shortened Leg',
                                     'stem': 'An 83-year-old falls; leg is shortened and '
                                             'externally rotated; cannot bear weight.',
                                     'question': 'Likely injury?',
                                     'answer': 'Hip fracture.',
                                     'discussion': 'X-ray, analgesia, VTE prophylaxis, early '
                                                   'ortho.',
                                     'book_hint': "Apley's Orthopaedics"}],
                           'medium': [{'title': 'Pain After Cast',
                                       'stem': 'A tibial fracture in cast has severe pain on '
                                               'passive toe stretch and a tense leg. Pulses '
                                               'present.',
                                       'question': 'Diagnosis?',
                                       'answer': 'Compartment syndrome — urgent fasciotomy '
                                                 'pathway.',
                                       'discussion': 'Do not wait for pulselessness.',
                                       'book_hint': "Apley's Orthopaedics"}],
                           'hard': [{'title': 'Hot Swollen Knee + Fever',
                                     'stem': 'A 45-year-old cannot bear weight on a hot swollen '
                                             'knee with fever. CRP high. Labs and imaging are '
                                             'pending; you must choose the safest next clinical '
                                             'concept.',
                                     'question': 'Action concept?',
                                     'answer': 'Septic arthritis until proven otherwise — urgent '
                                               'aspiration before antibiotics if possible, then '
                                               'treat.',
                                     'discussion': 'Delay destroys cartilage.',
                                     'book_hint': "Apley's Orthopaedics"}],
                           'extreme': [{'title': 'Crush Injury + Dark Urine',
                                        'stem': 'After an earthquake crush injury, a patient has '
                                                'tense swollen thighs, K 6.8, dark urine, and '
                                                'rising creatinine. Multiple teams are involved; '
                                                'prioritize life/limb/vision threats and avoid '
                                                'harmful premature therapies.',
                                        'question': 'Concerns?',
                                        'answer': 'Rhabdomyolysis ± compartment syndrome — '
                                                  'aggressive fluids per protocol, electrolyte '
                                                  'management, surgical decompression if '
                                                  'compartment syndrome, dialysis if needed.',
                                        'discussion': 'HyperK can kill before renal failure does.',
                                        'book_hint': "Apley's Orthopaedics"}]}},
 'dermatology': {'label': 'Dermatology',
                 'books': ["Rook's Textbook of Dermatology",
                           "Fitzpatrick's Dermatology",
                           "Habif's Clinical Dermatology"],
                 'pdf_notes': ['ABCDE for melanoma; urgent specialist referral for suspicious '
                               'lesions.',
                               'Impetigo: honey-colored crusts — contagious.',
                               'Psoriasis: silvery scale, Auspitz, extensor surfaces common.',
                               'Scabies: nocturnal itch, finger webs — treat patient + contacts.',
                               'Cellulitis vs abscess: antibiotics ± drainage if collection.'],
                 'questions': {'easy': [{'question': 'Honey-colored crusts suggest?',
                                         'options': ['A) Impetigo',
                                                     'B) Melanoma',
                                                     'C) Vitiligo',
                                                     'D) Alopecia areata'],
                                         'answer': 'A) Impetigo',
                                         'explanation': 'Classic pediatric infection.'},
                                        {'question': 'ABCDE screens for?',
                                         'options': ['A) Melanoma',
                                                     'B) Psoriasis only',
                                                     'C) Scabies only',
                                                     'D) Acne only'],
                                         'answer': 'A) Melanoma',
                                         'explanation': 'Evolving pigmented lesions.'},
                                        {'question': 'Auspitz sign relates to?',
                                         'options': ['A) Psoriasis',
                                                     'B) Cellulitis',
                                                     'C) Urticaria',
                                                     'D) Melasma'],
                                         'answer': 'A) Psoriasis',
                                         'explanation': 'Pinpoint bleeding on scale removal.'}],
                               'medium': [{'question': 'Scabies itch is worse?',
                                           'options': ['A) At night, web spaces',
                                                       'B) Only after spicy food',
                                                       'C) Only with bright light',
                                                       'D) Only during exercise forever'],
                                           'answer': 'A) At night, web spaces',
                                           'explanation': 'Treat contacts.'},
                                          {'question': 'Cellulitis features?',
                                           'options': ['A) Spreading erythema, warmth, tenderness',
                                                       'B) Only dry scale without erythema',
                                                       'C) Only comedones',
                                                       'D) Only café-au-lait spots'],
                                           'answer': 'A) Spreading erythema, warmth, tenderness',
                                           'explanation': 'Mark borders.'},
                                          {'question': 'SJS/TEN are?',
                                           'options': ['A) Severe cutaneous adverse drug reactions',
                                                       'B) Mild acne forms',
                                                       'C) Only fungal infections',
                                                       'D) Only viral warts'],
                                           'answer': 'A) Severe cutaneous adverse drug reactions',
                                           'explanation': 'Stop culprit; burn-unit style care.'}],
                               'hard': [{'question': 'A junior colleague asks for the single best '
                                                     'answer. Nikolsky sign can be positive in? '
                                                     'Choose the most accurate option and beware '
                                                     'of near-miss distractors.',
                                         'options': ['A) SJS/TEN / some blistering diseases',
                                                     'B) Simple eczema always',
                                                     'C) Only psoriasis plaques',
                                                     'D) Only alopecia'],
                                         'answer': 'A) SJS/TEN / some blistering diseases',
                                         'explanation': 'Epidermal detachment theme.'},
                                        {'question': 'A junior colleague asks for the single best '
                                                     'answer. Erythema migrans suggests? Choose '
                                                     'the most accurate option and beware of '
                                                     'near-miss distractors.',
                                         'options': ['A) Lyme early disease',
                                                     'B) Only measles',
                                                     'C) Only rubella',
                                                     'D) Only roseola'],
                                         'answer': 'A) Lyme early disease',
                                         'explanation': 'Tick exposure history.'},
                                        {'question': 'A junior colleague asks for the single best '
                                                     'answer. Necrotizing infection vs simple '
                                                     'cellulitis clue? Choose the most accurate '
                                                     'option and beware of near-miss distractors.',
                                         'options': ['A) Extreme pain, crepitus, rapid '
                                                     'deterioration',
                                                     'B) Mild itch only',
                                                     'C) Only dry skin',
                                                     'D) Only comedones'],
                                         'answer': 'A) Extreme pain, crepitus, rapid deterioration',
                                         'explanation': 'Surgery now.'}],
                               'extreme': [{'question': 'In a high-stakes ward scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Purpura fulminans association? '
                                                        'Avoid premature therapies that could harm '
                                                        'if a critical differential remains open.',
                                            'options': ['A) Severe sepsis/meningococcemia themes',
                                                        'B) Only dry eczema',
                                                        'C) Only acne',
                                                        'D) Only tinea versicolor'],
                                            'answer': 'A) Severe sepsis/meningococcemia themes',
                                            'explanation': 'Life-threatening.'},
                                           {'question': 'In a high-stakes ward scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Calciphylaxis occurs mainly in? '
                                                        'Avoid premature therapies that could harm '
                                                        'if a critical differential remains open.',
                                            'options': ['A) Advanced kidney disease patients',
                                                        'B) Healthy athletes only',
                                                        'C) Only neonates with jaundice',
                                                        'D) Only migraineurs'],
                                            'answer': 'A) Advanced kidney disease patients',
                                            'explanation': 'Painful ischemic skin necrosis.'},
                                           {'question': 'In a high-stakes ward scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Toxic shock associations '
                                                        'include? Avoid premature therapies that '
                                                        'could harm if a critical differential '
                                                        'remains open.',
                                            'options': ['A) Certain staphylococcal/streptococcal '
                                                        'toxins',
                                                        'B) Only sunburn',
                                                        'C) Only contact lens overwear without '
                                                        'systemic signs',
                                                        'D) Only food coma'],
                                            'answer': 'A) Certain staphylococcal/streptococcal '
                                                      'toxins',
                                            'explanation': 'Shock + rash + multiorgan.'}]},
                 'cases': {'easy': [{'title': 'Child with Facial Crusts',
                                     'stem': 'A 5-year-old has honey-colored crusts around the '
                                             'mouth after a scratch.',
                                     'question': 'Diagnosis?',
                                     'answer': 'Impetigo.',
                                     'discussion': 'Topical/systemic antibiotics per extent; '
                                                   'hygiene.',
                                     'book_hint': 'Habif / Rook / Fitzpatrick'}],
                           'medium': [{'title': 'Changing Mole',
                                       'stem': 'A 50-year-old has an asymmetrical multi-colored '
                                               'mole that grew over 3 months.',
                                       'question': 'Concern?',
                                       'answer': 'Melanoma — urgent dermatology excision pathway.',
                                       'discussion': 'Do not shave biopsy suspicious melanoma.',
                                       'book_hint': 'Habif / Rook / Fitzpatrick'}],
                           'hard': [{'title': 'Drug Rash + Mucosal Erosions',
                                     'stem': 'Days after a new anticonvulsant, a patient has '
                                             'fever, widespread dusky rash, and oral/genital '
                                             'erosions. Labs and imaging are pending; you must '
                                             'choose the safest next clinical concept.',
                                     'question': 'Fear?',
                                     'answer': 'SJS/TEN spectrum — stop drug, supportive care, '
                                               'specialty/burn pathways.',
                                     'discussion': 'Mucosal involvement is a red flag.',
                                     'book_hint': 'Habif / Rook / Fitzpatrick'}],
                           'extreme': [{'title': 'Purpuric Shock in Student',
                                        'stem': 'A college student rapidly develops fever, '
                                                'hypotension, and extensive purpura. Multiple '
                                                'teams are involved; prioritize life/limb/vision '
                                                'threats and avoid harmful premature therapies.',
                                        'question': 'Priority?',
                                        'answer': 'Meningococcemia/sepsis pathway — immediate '
                                                  'antibiotics after cultures if possible, '
                                                  'resuscitation, infection control.',
                                        'discussion': 'Do not delay antibiotics for LP if '
                                                      'unstable.',
                                        'book_hint': 'Habif / Rook / Fitzpatrick'}]}},
 'obgyn': {'label': 'Obstetrics & Gynecology',
           'books': ['Williams Obstetrics',
                     "Beckmann and Ling's Obstetrics and Gynecology",
                     "DC Dutta's Textbook of Obstetrics"],
           'pdf_notes': ['PPH 4 Ts: Tone (atony most common), Trauma, Tissue, Thrombin.',
                         'Ectopic: positive hCG + empty uterus + pain/spotting — emergency '
                         'awareness.',
                         'Pre-eclampsia after 20 weeks: HTN + proteinuria/organ dysfunction.',
                         'Antenatal care milestones: dating, anomaly scan, Rh, vaccines as '
                         'indicated.',
                         'Doppler FHR typically ~10–12 weeks.'],
           'questions': {'easy': [{'question': 'Most common PPH cause?',
                                   'options': ['A) Uterine atony',
                                               'B) Always amniotic fluid embolism',
                                               'C) Always cervical cancer',
                                               'D) Always fibroids only'],
                                   'answer': 'A) Uterine atony',
                                   'explanation': '4 Ts — Tone first.'},
                                  {'question': 'Ectopic risk rises with?',
                                   'options': ['A) Prior PID/tubal damage',
                                               'B) Only vitamin C use',
                                               'C) Only migraine',
                                               'D) Only asthma'],
                                   'answer': 'A) Prior PID/tubal damage',
                                   'explanation': 'Tubal scarring.'},
                                  {'question': 'Fetal heart by Doppler often from?',
                                   'options': ['A) ~10–12 weeks',
                                               'B) 4 weeks always',
                                               'C) Only after birth',
                                               'D) 40 weeks only'],
                                   'answer': 'A) ~10–12 weeks',
                                   'explanation': 'Antenatal exam.'}],
                         'medium': [{'question': 'Pre-eclampsia is HTN after 20 weeks plus?',
                                     'options': ['A) Proteinuria or organ dysfunction features',
                                                 'B) Only ankle edema always diagnostic alone',
                                                 'C) Only backache',
                                                 'D) Only heartburn'],
                                     'answer': 'A) Proteinuria or organ dysfunction features',
                                     'explanation': 'Definitions evolved but organ involvement '
                                                    'matters.'},
                                    {'question': 'Ectopic classic combo?',
                                     'options': ['A) Positive hCG + empty uterus + pain/bleeding',
                                                 'B) Only fibroids',
                                                 'C) Only PCOS without pain',
                                                 'D) Only yeast infection'],
                                     'answer': 'A) Positive hCG + empty uterus + pain/bleeding',
                                     'explanation': 'Can rupture.'},
                                    {'question': 'Shoulder dystocia is?',
                                     'options': ['A) Obstetric emergency after head delivery',
                                                 'B) Routine finding always safe',
                                                 'C) Only first-trimester issue',
                                                 'D) Only gynecologic clinic issue'],
                                     'answer': 'A) Obstetric emergency after head delivery',
                                     'explanation': 'Drill-based maneuvers.'}],
                         'hard': [{'question': 'A junior colleague asks for the single best '
                                               'answer. Magnesium sulfate in obstetrics is used '
                                               'for? Choose the most accurate option and beware of '
                                               'near-miss distractors.',
                                   'options': ['A) Seizure prophylaxis/treatment in '
                                               'pre-eclampsia/eclampsia pathways',
                                               'B) Only tocolysis forever as sole aim',
                                               'C) Only analgesia for headache',
                                               'D) Only to raise BP'],
                                   'answer': 'A) Seizure prophylaxis/treatment in '
                                             'pre-eclampsia/eclampsia pathways',
                                   'explanation': 'Watch toxicity.'},
                                  {'question': 'A junior colleague asks for the single best '
                                               'answer. Placenta previa bleeding is typically? '
                                               'Choose the most accurate option and beware of '
                                               'near-miss distractors.',
                                   'options': ['A) Painless vaginal bleeding',
                                               'B) Always painful with rigid uterus like abruption '
                                               'classic',
                                               'C) Only after menopause',
                                               'D) Only mucus plug'],
                                   'answer': 'A) Painless vaginal bleeding',
                                   'explanation': 'No digital exam if previa suspected.'},
                                  {'question': 'A junior colleague asks for the single best '
                                               'answer. HELLP relates to? Choose the most accurate '
                                               'option and beware of near-miss distractors.',
                                   'options': ['A) Hemolysis, elevated liver enzymes, low '
                                               'platelets',
                                               'B) Only high lipids',
                                               'C) Only low sodium',
                                               'D) Only high calcium'],
                                   'answer': 'A) Hemolysis, elevated liver enzymes, low platelets',
                                   'explanation': 'Severe pre-eclampsia spectrum.'}],
                         'extreme': [{'question': 'In a high-stakes ward scenario with incomplete '
                                                  'data, which statement is MOST correct? Amniotic '
                                                  'fluid embolism theme? Avoid premature therapies '
                                                  'that could harm if a critical differential '
                                                  'remains open.',
                                      'options': ['A) Sudden collapse/coagulopathy in '
                                                  'labor/immediate postpartum',
                                                  'B) Mild Braxton Hicks only',
                                                  'C) Only morning sickness',
                                                  'D) Only stretch marks'],
                                      'answer': 'A) Sudden collapse/coagulopathy in '
                                                'labor/immediate postpartum',
                                      'explanation': 'High mortality; supportive care.'},
                                     {'question': 'In a high-stakes ward scenario with incomplete '
                                                  'data, which statement is MOST correct? Acute '
                                                  'fatty liver of pregnancy overlaps with? Avoid '
                                                  'premature therapies that could harm if a '
                                                  'critical differential remains open.',
                                      'options': ['A) Late-pregnancy liver failure phenotype',
                                                  'B) Only first-trimester nausea mild',
                                                  'C) Only UTI',
                                                  'D) Only anemia of pregnancy mild'],
                                      'answer': 'A) Late-pregnancy liver failure phenotype',
                                      'explanation': 'Delivery is definitive therapy theme.'},
                                     {'question': 'In a high-stakes ward scenario with incomplete '
                                                  'data, which statement is MOST correct? Uterine '
                                                  'rupture risk rises with? Avoid premature '
                                                  'therapies that could harm if a critical '
                                                  'differential remains open.',
                                      'options': ['A) Prior cesarean scar in labor',
                                                  'B) Only nulliparity without scar always',
                                                  'C) Only contraception use',
                                                  'D) Only breastfeeding'],
                                      'answer': 'A) Prior cesarean scar in labor',
                                      'explanation': 'Pain, CTG change, shock.'}]},
           'cases': {'easy': [{'title': 'Boggy Uterus Bleeding',
                               'stem': 'After vaginal delivery, heavy bleeding with a soft boggy '
                                       'uterus.',
                               'question': 'First concept?',
                               'answer': 'Atony — massage + oxytocin and PPH protocol.',
                               'discussion': 'Tone is most common.',
                               'book_hint': 'Williams Obstetrics'}],
                     'medium': [{'title': 'Positive hCG + Unilateral Pain',
                                 'stem': 'Positive pregnancy test, spotting, unilateral pelvic '
                                         'pain, empty uterus, adnexal mass.',
                                 'question': 'Diagnosis?',
                                 'answer': 'Ectopic pregnancy until proven otherwise.',
                                 'discussion': 'Stability guides medical vs surgical care.',
                                 'book_hint': 'Williams Obstetrics'}],
                     'hard': [{'title': 'Seizure at 34 Weeks',
                               'stem': 'A primip at 34 weeks with headache and HTN has a '
                                       'tonic-clonic seizure. Labs and imaging are pending; you '
                                       'must choose the safest next clinical concept.',
                               'question': 'Diagnosis and drug concept?',
                               'answer': 'Eclampsia — magnesium sulfate and maternal/fetal '
                                         'stabilization; delivery planning.',
                               'discussion': 'Protect airway and control seizure.',
                               'book_hint': 'Williams Obstetrics'}],
                     'extreme': [{'title': 'Collapse Minutes After Delivery',
                                  'stem': 'Suddenly after delivery a woman becomes hypoxic, '
                                          'hypotensive, and coagulopathic without visible atony '
                                          'initially. Multiple teams are involved; prioritize '
                                          'life/limb/vision threats and avoid harmful premature '
                                          'therapies.',
                                  'question': 'Consider?',
                                  'answer': 'Amniotic fluid embolism among other catastrophic '
                                            'differentials — ACLS obstetric modifications, correct '
                                            'coagulopathy, supportive ICU care.',
                                  'discussion': 'Diagnosis of exclusion but act fast.',
                                  'book_hint': 'Williams Obstetrics'}]}},
 'pediatrics': {'label': 'Pediatrics',
                'books': ['Nelson Textbook of Pediatrics',
                          'Illustrated Textbook of Paediatrics — Lissauer',
                          "Forfar and Arneil's Textbook of Pediatrics"],
                'pdf_notes': ['ORS first-line for most pediatric dehydration from diarrhea.',
                              'MMR is live; know live vs inactivated vaccines.',
                              'Kawasaki: prolonged fever + mucocutaneous signs → coronary risk.',
                              'APGAR at 1 and 5 minutes guides immediate newborn status.',
                              'Always calculate pediatric doses by weight; watch fluid rates.'],
                'questions': {'easy': [{'question': 'ORS is first-line for?',
                                        'options': ['A) Most dehydrating diarrheas if child can '
                                                    'drink',
                                                    'B) Always IV antibiotics',
                                                    'C) Always aspirin',
                                                    'D) Always codeine'],
                                        'answer': 'A) Most dehydrating diarrheas if child can '
                                                  'drink',
                                        'explanation': 'Unless shock.'},
                                       {'question': 'MMR vaccine type?',
                                        'options': ['A) Live attenuated',
                                                    'B) Toxoid only',
                                                    'C) Pure polysaccharide only always',
                                                    'D) Inactivated toxin only'],
                                        'answer': 'A) Live attenuated',
                                        'explanation': 'Know live vs inactivated.'},
                                       {'question': 'APGAR is done at?',
                                        'options': ['A) 1 and 5 minutes commonly',
                                                    'B) Only at 1 day',
                                                    'C) Only at 1 month',
                                                    'D) Only prenatally'],
                                        'answer': 'A) 1 and 5 minutes commonly',
                                        'explanation': 'Newborn transition score.'}],
                              'medium': [{'question': 'Kawasaki complication?',
                                          'options': ['A) Coronary aneurysms',
                                                      'B) Only otitis externa',
                                                      'C) Only caries',
                                                      'D) Only myopia'],
                                          'answer': 'A) Coronary aneurysms',
                                          'explanation': 'IVIG early.'},
                                         {'question': 'Fever in a neonate is?',
                                          'options': ['A) Serious until proven otherwise',
                                                      'B) Always viral and ignore',
                                                      'C) Only teething',
                                                      'D) Only overdressing always safe'],
                                          'answer': 'A) Serious until proven otherwise',
                                          'explanation': 'Full infection workup pathways.'},
                                         {'question': 'Croup hallmark?',
                                          'options': ['A) Barking cough/stridor',
                                                      'B) Only wheeze of bronchiolitis always',
                                                      'C) Only whooping forever',
                                                      'D) Only apnea without cough'],
                                          'answer': 'A) Barking cough/stridor',
                                          'explanation': 'Steroids ± nebulized epi if severe.'}],
                              'hard': [{'question': 'A junior colleague asks for the single best '
                                                    'answer. Pyloric stenosis classic? Choose the '
                                                    'most accurate option and beware of near-miss '
                                                    'distractors.',
                                        'options': ['A) Projectile non-bilious vomiting ~2–8 weeks',
                                                    'B) Bilious vomiting day 1 always midgut '
                                                    'volvulus theme',
                                                    'C) Only constipation in teens',
                                                    'D) Only GERD in adults'],
                                        'answer': 'A) Projectile non-bilious vomiting ~2–8 weeks',
                                        'explanation': 'Olive mass; correct electrolytes before '
                                                       'surgery.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Intussusception stool? Choose the '
                                                    'most accurate option and beware of near-miss '
                                                    'distractors.',
                                        'options': ['A) Redcurrant jelly (late)',
                                                    'B) Acholic only',
                                                    'C) Melena of peptic ulcer only',
                                                    'D) Steatorrhea only'],
                                        'answer': 'A) Redcurrant jelly (late)',
                                        'explanation': 'Intermittent pain + currant jelly late.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Congenital adrenal hyperplasia crisis '
                                                    'in boys may show? Choose the most accurate '
                                                    'option and beware of near-miss distractors.',
                                        'options': ['A) Salt-wasting shock',
                                                    'B) Only tall stature forever without crisis',
                                                    'C) Only acne in neonates',
                                                    'D) Only jaundice'],
                                        'answer': 'A) Salt-wasting shock',
                                        'explanation': 'Give steroids/fluids/salt.'}],
                              'extreme': [{'question': 'In a high-stakes ward scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? DUCTAL-dependent congenital heart '
                                                       'lesion presenting in shock when duct '
                                                       'closes needs? Avoid premature therapies '
                                                       'that could harm if a critical differential '
                                                       'remains open.',
                                           'options': ['A) Prostaglandin E1 while resuscitating '
                                                       '(specialty-led)',
                                                       'B) Only fluid restriction forever',
                                                       'C) Only thyroxine',
                                                       'D) Only phototherapy'],
                                           'answer': 'A) Prostaglandin E1 while resuscitating '
                                                     '(specialty-led)',
                                           'explanation': 'Cardiogenic/ductal shock.'},
                                          {'question': 'In a high-stakes ward scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Non-accidental injury clue? Avoid '
                                                       'premature therapies that could harm if a '
                                                       'critical differential remains open.',
                                           'options': ['A) Injury inconsistent with '
                                                       'history/developmental stage',
                                                       'B) Typical toddler forehead bump with '
                                                       'matching history',
                                                       'C) Isolated playground abrasion with '
                                                       'witness',
                                                       'D) Typical sports sprain in teen with '
                                                       'clear mechanism'],
                                           'answer': 'A) Injury inconsistent with '
                                                     'history/developmental stage',
                                           'explanation': 'Safeguarding pathway.'},
                                          {'question': 'In a high-stakes ward scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Acute epiglottitis classic (less '
                                                       'common with Hib vaccine)? Avoid premature '
                                                       'therapies that could harm if a critical '
                                                       'differential remains open.',
                                           'options': ['A) Toxic child, drooling, tripoding — do '
                                                       'not agitate; airway expertise',
                                                       'B) Force tongue depressor exam first '
                                                       'always',
                                                       'C) Send home with syrup only',
                                                       'D) Only mild rhinitis'],
                                           'answer': 'A) Toxic child, drooling, tripoding — do not '
                                                     'agitate; airway expertise',
                                           'explanation': 'Airway first.'}]},
                'cases': {'easy': [{'title': 'Diarrhea + Sunken Eyes',
                                    'stem': 'An 18-month-old with watery diarrhea has sunken eyes '
                                            'but still drinks.',
                                    'question': 'Initial therapy?',
                                    'answer': 'ORS.',
                                    'discussion': 'IV if severe/shock.',
                                    'book_hint': 'Nelson Pediatrics'}],
                          'medium': [{'title': 'Fever 6 Days + Strawberry Tongue',
                                      'stem': 'A 3-year-old has ≥5 days fever, conjunctivitis, '
                                              'strawberry tongue, rash, cervical nodes.',
                                      'question': 'Diagnosis?',
                                      'answer': 'Kawasaki disease.',
                                      'discussion': 'IVIG to reduce coronary risk.',
                                      'book_hint': 'Nelson Pediatrics'}],
                          'hard': [{'title': 'Bilious Vomiting Neonate',
                                    'stem': 'A 3-day-old has bilious vomiting and abdominal '
                                            'distension. Labs and imaging are pending; you must '
                                            'choose the safest next clinical concept.',
                                    'question': 'Emergency concern?',
                                    'answer': 'Malrotation with midgut volvulus until excluded — '
                                              'urgent surgical evaluation.',
                                    'discussion': 'Bilious vomiting in neonate is an emergency.',
                                    'book_hint': 'Nelson Pediatrics'}],
                          'extreme': [{'title': 'Neonate in Shock Day 5',
                                       'stem': 'A previously well term neonate becomes grey, '
                                               'hypotensive, and acidotic on day 5 of life as the '
                                               'duct closes. Femoral pulses are weak. Multiple '
                                               'teams are involved; prioritize life/limb/vision '
                                               'threats and avoid harmful premature therapies.',
                                       'question': 'Concept?',
                                       'answer': 'Possible ductal-dependent congenital heart '
                                                 'disease — ABC resuscitation and urgent '
                                                 'prostaglandin under specialist guidance plus '
                                                 'cardiology.',
                                       'discussion': 'Sepsis remains on the differential too.',
                                       'book_hint': 'Nelson Pediatrics'}]}}}

def specialty_label(key: str) -> str:
    return SPECIALTIES[key]["label"]


def label_to_key(label: str) -> str | None:
    for key, data in SPECIALTIES.items():
        if data["label"] == label:
            return key
    return None


def get_specialty(key: str) -> dict:
    return SPECIALTIES[key]


def next_unique(items: list[dict], remaining: list[int] | None) -> tuple[int, dict, list[int]]:
    pool = list(remaining) if remaining else []
    if not pool:
        pool = list(range(len(items)))
        random.shuffle(pool)
    idx = pool.pop()
    return idx, items[idx], pool


def pick_question(
    specialty_key: str, difficulty: str, remaining: list[int] | None = None
) -> tuple[int, dict, list[int]]:
    items = SPECIALTIES[specialty_key]["questions"][difficulty]
    return next_unique(items, remaining)


def pick_case(
    specialty_key: str, difficulty: str, remaining: list[int] | None = None
) -> tuple[int, dict, list[int]]:
    items = SPECIALTIES[specialty_key]["cases"][difficulty]
    return next_unique(items, remaining)


def correct_letter(item: dict) -> str:
    return item["answer"].strip()[0].upper()


def option_letter(option: str) -> str:
    return option.strip()[0].upper()


def format_question_prompt(item: dict, specialty_label_text: str, difficulty: str) -> str:
    diff = DIFFICULTY_LABELS[difficulty]
    options = "\n".join(item["options"])
    return (
        f"📘 *Short MCQ — {specialty_label_text}*\n"
        f"Difficulty: *{diff}*\n\n"
        f"{item['question']}\n\n"
        f"{options}\n\n"
        f"_Tap A / B / C / D below. Full text is shown above._"
    )
def format_question_result(
    item: dict, chosen: str, specialty_label_text: str, difficulty: str
) -> str:
    correct = correct_letter(item)
    chosen = chosen.upper()
    verdict = "✅ *Correct!*" if chosen == correct else f"❌ *Incorrect.* You chose *{chosen}*."
    options = "\n".join(item["options"])
    diff = DIFFICULTY_LABELS[difficulty]
    return (
        f"📘 *Short MCQ — {specialty_label_text}*\n"
        f"Difficulty: *{diff}*\n\n"
        f"{item['question']}\n\n"
        f"{options}\n\n"
        f"{verdict}\n"
        f"✅ *Answer:* {item['answer']}\n"
        f"💡 {item['explanation']}"
    )


def format_case_prompt(item: dict, specialty_label_text: str, difficulty: str) -> str:
    diff = DIFFICULTY_LABELS[difficulty]
    return (
        f"🏥 *Case-based Question — {specialty_label_text}*\n"
        f"Difficulty: *{diff}*\n"
        f"*{item['title']}*\n\n"
        f"{item['stem']}\n\n"
        f"❓ *Question:* {item['question']}\n\n"
        f"_Tap the button below to reveal the answer._"
    )


def format_case_result(item: dict, specialty_label_text: str, difficulty: str) -> str:
    diff = DIFFICULTY_LABELS[difficulty]
    return (
        f"🏥 *Case-based Question — {specialty_label_text}*\n"
        f"Difficulty: *{diff}*\n"
        f"*{item['title']}*\n\n"
        f"{item['stem']}\n\n"
        f"❓ *Question:* {item['question']}\n\n"
        f"✅ *Answer:* {item['answer']}\n\n"
        f"📝 *Discussion:* {item['discussion']}\n\n"
        f"📚 *Book source:* {item['book_hint']}"
    )


def format_book_sources(specialty_key: str) -> str:
    data = SPECIALTIES[specialty_key]
    books = "\n".join(f"• {b}" for b in data["books"])
    return (
        f"📚 *Book sources — {data['label']}*\n\n"
        f"{books}\n\n"
        f"_Use the edition recommended by your faculty._"
    )


def specialty_menu_text() -> str:
    return (
        "🩺 *CharaNas Medicine Bot*\n"
        "Undergraduate Medicine Department\n\n"
        "Choose a *specialty* first.\n"
        "Then open Short MCQ or Case-based Question and pick a difficulty:\n"
        "*Easy → Medium → Hard → Extreme*\n\n"
        "Higher levels are longer and more tricky.\n"
        "Use *Change specialty* anytime to switch topics."
    )


def feature_menu_text(specialty_key: str) -> str:
    label = specialty_label(specialty_key)
    return (
        f"📍 Specialty: *{label}*\n\n"
        "Choose a feature:\n"
        "• Short MCQ\n"
        "• Case-based Question\n"
        "• PDF files\n"
        "• Book source\n\n"
        "Or tap *Change specialty* to go back."
    )


def difficulty_menu_text(specialty_key: str, mode: str) -> str:
    label = specialty_label(specialty_key)
    kind = "Short MCQ" if mode == "question" else "Case-based Question"
    return (
        f"📍 *{label}* — {kind}\n\n"
        "Choose a difficulty:\n"
        "• Easy\n"
        "• Medium\n"
        "• Hard\n"
        "• Extreme\n\n"
        "Harder levels use longer, trickier stems.\n"
        "Tap *Back to features* to return."
    )
