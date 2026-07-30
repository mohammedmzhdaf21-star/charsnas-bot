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
                              'STEMI: ST elevation in contiguous leads ± new LBBB; '
                              'urgent reperfusion.',
                              'HF signs: orthopnea, raised JVP, crackles, edema; '
                              'confirm with BNP/echo.',
                              'MR = holosystolic to axilla; AS = crescendo-decrescendo '
                              'to carotids.',
                              'Secondary prevention after MI: antiplatelet, statin, '
                              'beta-blocker, ACEi as indicated.'],
                'questions': {'easy': [{'question': 'During myocardial ischemia, '
                                                    'angina typically occurs because '
                                                    'coronary oxygen supply cannot '
                                                    'meet rising myocardial demand.',
                                        'options': ['A) Transient retrosternal '
                                                    'pressure provoked by exertion and '
                                                    'relieved by rest or nitrates',
                                                    'B) Sharp pain reproduced by '
                                                    'chest-wall palpation at a single '
                                                    'rib',
                                                    'C) Pleuritic pain worse when '
                                                    'supine and improved by leaning '
                                                    'forward',
                                                    'D) Burning epigastric pain that '
                                                    'resolves only after antacids'],
                                        'answer': 'A) Transient retrosternal pressure '
                                                  'provoked by exertion and relieved '
                                                  'by rest or nitrates',
                                        'explanation': 'Angina is transient myocardial '
                                                       'ischemia when coronary flow '
                                                       'reserve is inadequate for '
                                                       'demand. Exertion raises wall '
                                                       'stress and oxygen need, '
                                                       'producing retrosternal '
                                                       'pressure that eases when '
                                                       'demand falls or nitrates '
                                                       'reduce preload. '
                                                       'Musculoskeletal, pericarditic, '
                                                       'and purely reflux patterns '
                                                       'imply different mechanisms.',
                                        'choice_explanations': {'A': 'Ischemic angina '
                                                                     'reflects '
                                                                     'supply–demand '
                                                                     'mismatch; '
                                                                     'exertion '
                                                                     'classically '
                                                                     'triggers '
                                                                     'retrosternal '
                                                                     'pressure that '
                                                                     'resolves with '
                                                                     'rest or '
                                                                     'preload-reducing '
                                                                     'nitrates.',
                                                                'B': 'Pain reproduced '
                                                                     'by palpation is '
                                                                     'musculoskeletal '
                                                                     'chest-wall pain, '
                                                                     'not coronary '
                                                                     'ischemia.',
                                                                'C': 'Pleuritic pain '
                                                                     'worse supine and '
                                                                     'better leaning '
                                                                     'forward is '
                                                                     'typical of '
                                                                     'pericarditis, '
                                                                     'not demand '
                                                                     'ischemia.',
                                                                'D': 'Isolated '
                                                                     'antacid-responsive '
                                                                     'burning '
                                                                     'epigastric pain '
                                                                     'points to '
                                                                     'acid-related '
                                                                     'dyspepsia rather '
                                                                     'than myocardial '
                                                                     'ischemia.'}},
                                       {'question': 'Aspirin given immediately in ACS '
                                                    'primarily reduces further '
                                                    'coronary thrombosis by which '
                                                    'platelet mechanism?',
                                        'options': ['A) Competitive inhibition of '
                                                    'glycoprotein IIb/IIIa receptors',
                                                    'B) Irreversible acetylation of '
                                                    'platelet COX-1 blocking '
                                                    'thromboxane A2 synthesis',
                                                    'C) Enhancement of endothelial '
                                                    'nitric-oxide–mediated '
                                                    'vasodilation',
                                                    'D) Direct cleavage of fibrin '
                                                    'within an organized thrombus'],
                                        'answer': 'B) Irreversible acetylation of '
                                                  'platelet COX-1 blocking thromboxane '
                                                  'A2 synthesis',
                                        'explanation': 'Plaque rupture exposes '
                                                       'thrombogenic material and '
                                                       'activates platelets. Aspirin '
                                                       'irreversibly acetylates COX-1, '
                                                       'suppressing thromboxane A2 and '
                                                       'limiting aggregation for the '
                                                       'platelet lifespan. GPIIb/IIIa '
                                                       'blockade, nitrate-like '
                                                       'vasodilation, and fibrinolysis '
                                                       'are distinct therapies.',
                                        'choice_explanations': {'A': 'GPIIb/IIIa '
                                                                     'inhibitors block '
                                                                     'the final common '
                                                                     'pathway of '
                                                                     'aggregation but '
                                                                     'are not '
                                                                     'aspirin’s '
                                                                     'mechanism.',
                                                                'B': 'Aspirin '
                                                                     'permanently '
                                                                     'disables '
                                                                     'platelet COX-1, '
                                                                     'cutting '
                                                                     'thromboxane A2 '
                                                                     'production and '
                                                                     'aggregation—key '
                                                                     'early ACS '
                                                                     'therapy.',
                                                                'C': 'Nitric-oxide–mediated '
                                                                     'coronary '
                                                                     'dilation is a '
                                                                     'nitrate effect, '
                                                                     'not aspirin’s '
                                                                     'antiplatelet '
                                                                     'action.',
                                                                'D': 'Fibrinolysis '
                                                                     'dissolves fibrin '
                                                                     'clot; aspirin '
                                                                     'does not '
                                                                     'enzymatically '
                                                                     'lyse thrombus.'}},
                                       {'question': 'A crescendo–decrescendo systolic '
                                                    'murmur radiating to the carotids '
                                                    'is most consistent with stenosis '
                                                    'of which valve?',
                                        'options': ['A) Mitral valve (regurgitant jet '
                                                    'to axilla)',
                                                    'B) Tricuspid valve (increases '
                                                    'with inspiration)',
                                                    'C) Aortic valve (fixed outflow '
                                                    'obstruction)',
                                                    'D) Pulmonic valve alone without '
                                                    'aortic involvement'],
                                        'answer': 'C) Aortic valve (fixed outflow '
                                                  'obstruction)',
                                        'explanation': 'Aortic stenosis produces a '
                                                       'harsh mid-systolic ejection '
                                                       'murmur from turbulent flow '
                                                       'across a narrowed aortic '
                                                       'orifice; radiation to the '
                                                       'carotids follows the aortic '
                                                       'jet. Mitral regurgitation is '
                                                       'holosystolic to the axilla; '
                                                       'tricuspid regurgitation varies '
                                                       'with respiration; isolated '
                                                       'pulmonic stenosis is less '
                                                       'common in adults and radiates '
                                                       'differently.',
                                        'choice_explanations': {'A': 'Mitral '
                                                                     'regurgitation is '
                                                                     'holosystolic and '
                                                                     'radiates to the '
                                                                     'axilla, not a '
                                                                     'crescendo–decrescendo '
                                                                     'carotid-radiating '
                                                                     'murmur.',
                                                                'B': 'Tricuspid '
                                                                     'regurgitation is '
                                                                     'holosystolic and '
                                                                     'intensifies with '
                                                                     'inspiration '
                                                                     '(Carvallo), '
                                                                     'unlike fixed AS.',
                                                                'C': 'Aortic stenosis '
                                                                     'creates a '
                                                                     'crescendo–decrescendo '
                                                                     'systolic '
                                                                     'ejection murmur '
                                                                     'that radiates to '
                                                                     'the carotids.',
                                                                'D': 'Isolated '
                                                                     'pulmonic '
                                                                     'stenosis can '
                                                                     'sound similar '
                                                                     'but is uncommon '
                                                                     'in adults and '
                                                                     'does not explain '
                                                                     'the classic '
                                                                     'carotid-radiating '
                                                                     'AS pattern '
                                                                     'described.'}}],
                              'medium': [{'question': 'A 58-year-old with crushing '
                                                      'chest pain has ST elevation in '
                                                      'leads II, III, and aVF. Which '
                                                      'coronary territory is most '
                                                      'likely occluded?',
                                          'options': ['A) Proximal left anterior '
                                                      'descending (extensive anterior '
                                                      'wall)',
                                                      'B) Circumflex alone causing '
                                                      'isolated high lateral ischemia',
                                                      'C) Septal perforators only '
                                                      'without inferior involvement',
                                                      'D) Right coronary artery '
                                                      'supplying the inferior wall'],
                                          'answer': 'D) Right coronary artery '
                                                    'supplying the inferior wall',
                                          'explanation': 'Leads II, III, and aVF view '
                                                         'the inferior wall, usually '
                                                         'supplied by the right '
                                                         'coronary artery (or less '
                                                         'often a dominant '
                                                         'circumflex). Inferior STEMI '
                                                         'therefore localizes to RCA '
                                                         'occlusion in most patients. '
                                                         'Anterior and high-lateral '
                                                         'patterns use different lead '
                                                         'groups.',
                                          'choice_explanations': {'A': 'Proximal LAD '
                                                                       'occlusion '
                                                                       'elevates ST in '
                                                                       'V1–V4 '
                                                                       '(anterior), '
                                                                       'not the '
                                                                       'inferior leads '
                                                                       'II/III/aVF.',
                                                                  'B': 'Isolated '
                                                                       'circumflex '
                                                                       'disease more '
                                                                       'often affects '
                                                                       'I, aVL, and '
                                                                       'V5–V6; '
                                                                       'inferior STEMI '
                                                                       'is usually '
                                                                       'RCA.',
                                                                  'C': 'Septal '
                                                                       'perforator '
                                                                       'ischemia '
                                                                       'affects septal '
                                                                       'leads (V1–V2) '
                                                                       'and does not '
                                                                       'explain ST '
                                                                       'elevation '
                                                                       'confined to '
                                                                       'II/III/aVF.',
                                                                  'D': 'Inferior leads '
                                                                       'II, III, aVF '
                                                                       'correspond to '
                                                                       'RCA territory '
                                                                       'in most '
                                                                       'patients, '
                                                                       'matching this '
                                                                       'STEMI '
                                                                       'pattern.'}},
                                         {'question': 'Which murmur is holosystolic '
                                                      'and typically radiates to the '
                                                      'left axilla?',
                                          'options': ['A) Mitral regurgitation from '
                                                      'systolic leakage into the left '
                                                      'atrium',
                                                      'B) Aortic stenosis with '
                                                      'radiation limited to the '
                                                      'carotids',
                                                      'C) Aortic regurgitation heard '
                                                      'best as an early diastolic '
                                                      'decrescendo',
                                                      'D) Mitral stenosis with an '
                                                      'opening snap and mid-diastolic '
                                                      'rumble'],
                                          'answer': 'A) Mitral regurgitation from '
                                                    'systolic leakage into the left '
                                                    'atrium',
                                          'explanation': 'In mitral regurgitation, the '
                                                         'left ventricle ejects into '
                                                         'the left atrium throughout '
                                                         'systole, producing a '
                                                         'holosystolic murmur that '
                                                         'often radiates to the axilla '
                                                         'along the regurgitant jet. '
                                                         'AS is ejection systolic to '
                                                         'the neck; AR and MS are '
                                                         'diastolic.',
                                          'choice_explanations': {'A': 'MR generates a '
                                                                       'holosystolic '
                                                                       'murmur as '
                                                                       'LV-to-LA flow '
                                                                       'persists '
                                                                       'through '
                                                                       'systole, '
                                                                       'commonly '
                                                                       'radiating to '
                                                                       'the axilla.',
                                                                  'B': 'Aortic '
                                                                       'stenosis is '
                                                                       'crescendo–decrescendo '
                                                                       'and radiates '
                                                                       'to the '
                                                                       'carotids, not '
                                                                       'a holosystolic '
                                                                       'axillary '
                                                                       'murmur.',
                                                                  'C': 'Aortic '
                                                                       'regurgitation '
                                                                       'is an early '
                                                                       'diastolic '
                                                                       'decrescendo '
                                                                       'murmur, not '
                                                                       'systolic.',
                                                                  'D': 'Mitral '
                                                                       'stenosis '
                                                                       'produces a '
                                                                       'diastolic '
                                                                       'rumble after '
                                                                       'an opening '
                                                                       'snap, not a '
                                                                       'holosystolic '
                                                                       'murmur.'}},
                                         {'question': 'For an awake patient with '
                                                      'typical angina at rest, which '
                                                      'first-line agent most rapidly '
                                                      'reduces preload and often '
                                                      'relieves symptoms?',
                                          'options': ['A) Immediate high-dose '
                                                      'intravenous beta-blocker before '
                                                      'nitrates',
                                                      'B) Sublingual nitroglycerin to '
                                                      'venodilate and lower wall '
                                                      'stress',
                                                      'C) Routine thrombolysis without '
                                                      'ECG confirmation of STEMI',
                                                      'D) Calcium-channel blocker as '
                                                      'the sole initial anti-ischemic '
                                                      'drug'],
                                          'answer': 'B) Sublingual nitroglycerin to '
                                                    'venodilate and lower wall stress',
                                          'explanation': 'Sublingual nitroglycerin '
                                                         'rapidly venodilates, cutting '
                                                         'preload and myocardial wall '
                                                         'tension, which lowers oxygen '
                                                         'demand and often eases '
                                                         'angina. Beta-blockers help '
                                                         'later for ongoing ischemia; '
                                                         'fibrinolysis is reserved for '
                                                         'STEMI when PCI is '
                                                         'unavailable; CCBs are not '
                                                         'first-line for typical ACS '
                                                         'angina relief.',
                                          'choice_explanations': {'A': 'IV '
                                                                       'beta-blockade '
                                                                       'may reduce '
                                                                       'demand but is '
                                                                       'not the '
                                                                       'fastest first '
                                                                       'relief step '
                                                                       'and can harm '
                                                                       'unstable or '
                                                                       'RV-infarct '
                                                                       'patients.',
                                                                  'B': 'Nitroglycerin '
                                                                       'promptly '
                                                                       'lowers preload '
                                                                       'via '
                                                                       'venodilation, '
                                                                       'reducing wall '
                                                                       'stress and '
                                                                       'ischemic pain '
                                                                       'in many angina '
                                                                       'episodes.',
                                                                  'C': 'Thrombolysis '
                                                                       'without STEMI '
                                                                       'criteria risks '
                                                                       'bleeding and '
                                                                       'is not '
                                                                       'symptom-relief '
                                                                       'therapy for '
                                                                       'undifferentiated '
                                                                       'angina.',
                                                                  'D': 'Calcium-channel '
                                                                       'blockers are '
                                                                       'adjuncts in '
                                                                       'selected '
                                                                       'settings, not '
                                                                       'the standard '
                                                                       'immediate '
                                                                       'preload-reducing '
                                                                       'relief '
                                                                       'agent.'}}],
                              'hard': [{'question': 'A 64-year-old with inferior STEMI '
                                                    'becomes hypotensive after '
                                                    'nitrates. JVP is elevated, lungs '
                                                    'are clear, and the ECG shows ST '
                                                    'elevation in II, III, aVF with '
                                                    'reciprocal changes. Which '
                                                    'pathophysiology best explains '
                                                    'this response?',
                                        'options': ['A) Isolated left-ventricular '
                                                    'failure with pulmonary edema '
                                                    'requiring more preload reduction',
                                                    'B) Cardiac tamponade from '
                                                    'free-wall rupture presenting '
                                                    'minutes after pain onset',
                                                    'C) Right ventricular infarction '
                                                    'making cardiac output '
                                                    'preload-dependent',
                                                    'D) Hypertrophic obstructive '
                                                    'cardiomyopathy with dynamic LVOT '
                                                    'obstruction'],
                                        'answer': 'C) Right ventricular infarction '
                                                  'making cardiac output '
                                                  'preload-dependent',
                                        'explanation': 'Inferior STEMI often involves '
                                                       'the RCA, which may also supply '
                                                       'the RV. RV infarction impairs '
                                                       'RV stroke volume so LV filling '
                                                       'becomes highly '
                                                       'preload-dependent; nitrates '
                                                       'drop venous return and '
                                                       'precipitate hypotension with '
                                                       'clear lungs and raised JVP. LV '
                                                       'failure would crackle; early '
                                                       'rupture is uncommon minutes '
                                                       'into STEMI; HOCM is unrelated.',
                                        'choice_explanations': {'A': 'LV failure '
                                                                     'typically '
                                                                     'produces '
                                                                     'pulmonary '
                                                                     'congestion; '
                                                                     'clear lungs '
                                                                     'after '
                                                                     'nitrate-induced '
                                                                     'hypotension '
                                                                     'argue against '
                                                                     'primary LV pump '
                                                                     'failure needing '
                                                                     'more preload '
                                                                     'cut.',
                                                                'B': 'Free-wall '
                                                                     'rupture/tamponade '
                                                                     'usually occurs '
                                                                     'days after '
                                                                     'transmural MI, '
                                                                     'not immediately '
                                                                     'with nitrate '
                                                                     'administration.',
                                                                'C': 'RV infarction '
                                                                     '(often RCA) '
                                                                     'makes output '
                                                                     'preload-dependent; '
                                                                     'nitrates reduce '
                                                                     'venous return '
                                                                     'and cause '
                                                                     'hypotension with '
                                                                     'elevated JVP and '
                                                                     'clear lungs.',
                                                                'D': 'HOCM can cause '
                                                                     'nitrate-sensitive '
                                                                     'hypotension but '
                                                                     'does not explain '
                                                                     'acute inferior '
                                                                     'STEMI ECG '
                                                                     'changes.'}},
                                       {'question': 'Among foundational HFrEF '
                                                    'therapies, which listed class has '
                                                    'consistent mortality reduction '
                                                    'when used as disease-modifying '
                                                    'treatment?',
                                        'options': ['A) Loop diuretics titrated only '
                                                    'for congestion without '
                                                    'neurohormonal blockade',
                                                    'B) Digoxin used solely for rate '
                                                    'control without outcome benefit '
                                                    'as primary therapy',
                                                    'C) Short-acting nifedipine for '
                                                    'afterload reduction in systolic '
                                                    'heart failure',
                                                    'D) ACE inhibitors (or ARNI) that '
                                                    'interrupt maladaptive '
                                                    'renin–angiotensin signaling'],
                                        'answer': 'D) ACE inhibitors (or ARNI) that '
                                                  'interrupt maladaptive '
                                                  'renin–angiotensin signaling',
                                        'explanation': 'In HFrEF, chronic RAAS and '
                                                       'sympathetic activation remodel '
                                                       'the ventricle. ACE '
                                                       'inhibitors/ARNI reduce '
                                                       'mortality and hospitalizations '
                                                       'by blocking this cascade; '
                                                       'evidence-based beta-blockers '
                                                       'and mineralocorticoid '
                                                       'antagonists similarly improve '
                                                       'survival. Diuretics relieve '
                                                       'fluid but lack mortality '
                                                       'benefit as sole therapy; '
                                                       'digoxin is adjunctive; '
                                                       'short-acting dihydropyridines '
                                                       'are not disease-modifying '
                                                       'HFrEF therapy.',
                                        'choice_explanations': {'A': 'Loop diuretics '
                                                                     'treat volume '
                                                                     'overload '
                                                                     'symptomatically '
                                                                     'but do not '
                                                                     'themselves '
                                                                     'provide proven '
                                                                     'mortality '
                                                                     'reduction like '
                                                                     'ACEI/ARNI.',
                                                                'B': 'Digoxin may help '
                                                                     'symptoms/rate '
                                                                     'but is not '
                                                                     'first-line '
                                                                     'mortality-reducing '
                                                                     'foundational '
                                                                     'therapy compared '
                                                                     'with ACEI/ARNI.',
                                                                'C': 'Short-acting '
                                                                     'nifedipine can '
                                                                     'worsen outcomes '
                                                                     'in systolic HF '
                                                                     'and is not '
                                                                     'guideline '
                                                                     'disease-modifying '
                                                                     'therapy.',
                                                                'D': 'ACE '
                                                                     'inhibitors/ARNI '
                                                                     'blunt harmful '
                                                                     'RAAS activation '
                                                                     'and consistently '
                                                                     'reduce mortality '
                                                                     'in HFrEF.'}},
                                       {'question': 'A 55-year-old with 40 minutes of '
                                                    'ischemic chest pain has new left '
                                                    'bundle-branch block and ongoing '
                                                    'pain. Troponin is not yet '
                                                    'resulted. Which management '
                                                    'concept is most appropriate?',
                                        'options': ['A) Treat as a STEMI equivalent '
                                                    'and pursue urgent reperfusion '
                                                    'pathways',
                                                    'B) Wait 6 hours for serial '
                                                    'troponins before any reperfusion '
                                                    'decision',
                                                    'C) Give fibrinolysis only after '
                                                    'proving reciprocal ST depression '
                                                    'in all leads',
                                                    'D) Discharge if pain eases '
                                                    'briefly with one dose of antacid'],
                                        'answer': 'A) Treat as a STEMI equivalent and '
                                                  'pursue urgent reperfusion pathways',
                                        'explanation': 'New LBBB with compatible '
                                                       'ischemic symptoms can obscure '
                                                       'ST-segment analysis and is '
                                                       'managed as a STEMI equivalent '
                                                       'when the clinical picture '
                                                       'indicates acute coronary '
                                                       'occlusion. Delaying '
                                                       'reperfusion for late troponin '
                                                       'confirmation risks myocardium; '
                                                       'antacid response does not '
                                                       'exclude ACS.',
                                        'choice_explanations': {'A': 'New or '
                                                                     'presumed-new '
                                                                     'LBBB plus '
                                                                     'ischemic '
                                                                     'symptoms '
                                                                     'warrants urgent '
                                                                     'reperfusion '
                                                                     'consideration as '
                                                                     'a STEMI '
                                                                     'equivalent.',
                                                                'B': 'Waiting many '
                                                                     'hours for '
                                                                     'troponin alone '
                                                                     'delays '
                                                                     'time-critical '
                                                                     'reperfusion in '
                                                                     'suspected '
                                                                     'occlusion MI.',
                                                                'C': 'Requiring '
                                                                     'reciprocal '
                                                                     'changes in every '
                                                                     'lead is neither '
                                                                     'necessary nor '
                                                                     'realistic before '
                                                                     'treating a '
                                                                     'STEMI-equivalent '
                                                                     'presentation.',
                                                                'D': 'Transient '
                                                                     'antacid relief '
                                                                     'does not rule '
                                                                     'out coronary '
                                                                     'occlusion and is '
                                                                     'unsafe grounds '
                                                                     'for '
                                                                     'discharge.'}}],
                              'extreme': [{'question': 'A 72-year-old with prior CABG '
                                                       'develops sudden tearing '
                                                       'interscapular pain, unequal '
                                                       'arm blood pressures, and flash '
                                                       'pulmonary edema. Troponin is '
                                                       'mildly elevated; the ECG shows '
                                                       'nonspecific ST changes without '
                                                       'clear territorial STEMI. He is '
                                                       'hypertensive and diaphoretic. '
                                                       'Which diagnosis must be '
                                                       'excluded before committing to '
                                                       'empiric full ACS '
                                                       'antithrombotic and '
                                                       'catheter-lab pathways alone?',
                                           'options': ['A) Demand ischemia from severe '
                                                       'anemia without structural '
                                                       'emergency',
                                                       'B) Acute aortic syndrome (type '
                                                       'A dissection) involving '
                                                       'coronary ostia or aortic '
                                                       'regurgitation',
                                                       'C) Uncomplicated panic attack '
                                                       'with hyperventilation '
                                                       'alkalosis',
                                                       'D) Isolated community-acquired '
                                                       'pneumonia explaining unequal '
                                                       'arm pressures'],
                                           'answer': 'B) Acute aortic syndrome (type A '
                                                     'dissection) involving coronary '
                                                     'ostia or aortic regurgitation',
                                           'explanation': 'Type A aortic dissection '
                                                          'can mimic ACS by '
                                                          'compromising coronary ostia '
                                                          'or causing acute AR and '
                                                          'flash edema, while pulse '
                                                          'deficits and tearing pain '
                                                          'are classic. Empiric dual '
                                                          'antiplatelet therapy, '
                                                          'heparin, and '
                                                          'catheterization without '
                                                          'excluding dissection can '
                                                          'catastrophically worsen '
                                                          'outcomes. Mild troponin '
                                                          'rise does not prove primary '
                                                          'plaque rupture.',
                                           'choice_explanations': {'A': 'Anemia can '
                                                                        'cause demand '
                                                                        'ischemia but '
                                                                        'does not '
                                                                        'explain '
                                                                        'tearing pain, '
                                                                        'pulse '
                                                                        'deficit, and '
                                                                        'flash edema '
                                                                        'together.',
                                                                   'B': 'Type A '
                                                                        'dissection '
                                                                        'explains '
                                                                        'tearing pain, '
                                                                        'unequal BPs, '
                                                                        'possible '
                                                                        'coronary '
                                                                        'involvement, '
                                                                        'and mild '
                                                                        'troponin '
                                                                        'rise; it must '
                                                                        'be excluded '
                                                                        'before full '
                                                                        'ACS '
                                                                        'anticoagulation/PCI '
                                                                        'pathways.',
                                                                   'C': 'Panic does '
                                                                        'not produce '
                                                                        'unequal arm '
                                                                        'pressures, '
                                                                        'flash '
                                                                        'pulmonary '
                                                                        'edema, or '
                                                                        'significant '
                                                                        'troponin '
                                                                        'elevation.',
                                                                   'D': 'Pneumonia may '
                                                                        'cause hypoxia '
                                                                        'but not acute '
                                                                        'pulse '
                                                                        'deficits or '
                                                                        'tearing '
                                                                        'interscapular '
                                                                        'pain with '
                                                                        'asymmetric '
                                                                        'BPs.'}},
                                          {'question': 'Six hours after cardiac '
                                                       'surgery, a patient becomes '
                                                       'hypotensive with rising CVP, '
                                                       'muffled heart sounds, '
                                                       'oliguria, and equalization of '
                                                       'diastolic pressures on '
                                                       'monitoring. Chest tube output '
                                                       'has suddenly fallen. Bedside '
                                                       'echo windows are limited by '
                                                       'dressings. Which constellation '
                                                       'and next concept are most '
                                                       'appropriate?',
                                           'options': ['A) Primary distributive septic '
                                                       'shock; start broad '
                                                       'vasopressors without '
                                                       'considering mechanical '
                                                       'obstruction',
                                                       'B) Isolated hypovolemia from '
                                                       'under-resuscitation; give '
                                                       'large crystalloid boluses '
                                                       'indefinitely',
                                                       'C) Cardiac tamponade '
                                                       'physiology—urgent surgical '
                                                       'exploration rather than '
                                                       'waiting for perfect imaging',
                                                       'D) Acute massive PE only; '
                                                       'start full-dose thrombolysis '
                                                       'at the bedside without '
                                                       'evaluation'],
                                           'answer': 'C) Cardiac tamponade '
                                                     'physiology—urgent surgical '
                                                     'exploration rather than waiting '
                                                     'for perfect imaging',
                                           'explanation': 'Postoperative tamponade '
                                                          'produces obstructive shock: '
                                                          'impaired filling, high '
                                                          'filling pressures, low '
                                                          'output, and often sudden '
                                                          'drop in drain output as '
                                                          'clot seals the tube. After '
                                                          'cardiac surgery, localized '
                                                          'clot may escape classic '
                                                          'echo views, so clinical '
                                                          'diagnosis prompts urgent '
                                                          're-exploration. Treating as '
                                                          'pure sepsis, endless '
                                                          'fluids, or empiric lytics '
                                                          'delays definitive relief of '
                                                          'obstruction.',
                                           'choice_explanations': {'A': 'Sepsis is '
                                                                        'distributive '
                                                                        'with usually '
                                                                        'low CVP; '
                                                                        'rising CVP '
                                                                        'and '
                                                                        'equalization '
                                                                        'favor '
                                                                        'obstruction, '
                                                                        'not primary '
                                                                        'vasodilation.',
                                                                   'B': 'Hypovolemia '
                                                                        'lowers '
                                                                        'filling '
                                                                        'pressures; '
                                                                        'rising CVP '
                                                                        'with '
                                                                        'hypotension '
                                                                        'argues '
                                                                        'against '
                                                                        'simple '
                                                                        'underfilling.',
                                                                   'C': 'Falling drain '
                                                                        'output plus '
                                                                        'obstructive '
                                                                        'hemodynamics '
                                                                        'after surgery '
                                                                        'indicates '
                                                                        'tamponade '
                                                                        'needing '
                                                                        'urgent '
                                                                        'surgical '
                                                                        'decompression.',
                                                                   'D': 'Massive PE '
                                                                        'can obstruct '
                                                                        'but sudden '
                                                                        'drain '
                                                                        'cessation and '
                                                                        'muffled tones '
                                                                        'after cardiac '
                                                                        'surgery point '
                                                                        'first to '
                                                                        'tamponade; '
                                                                        'empiric '
                                                                        'lytics are '
                                                                        'hazardous '
                                                                        'postoperatively.'}},
                                          {'question': 'A 28-year-old with known WPW '
                                                       'presents with irregular very '
                                                       'rapid wide-complex tachycardia '
                                                       'and hypotension (BP 78/40). '
                                                       'Which therapy is most '
                                                       'appropriate, and which class '
                                                       'must be avoided?',
                                           'options': ['A) IV metoprolol to slow AV '
                                                       'nodal conduction and protect '
                                                       'the ventricle',
                                                       'B) IV digoxin to increase '
                                                       'vagal tone at the AV node',
                                                       'C) IV verapamil for rate '
                                                       'control via calcium-channel '
                                                       'blockade of the AV node',
                                                       'D) Immediate synchronized '
                                                       'cardioversion (if unstable) or '
                                                       'IV procainamide; avoid '
                                                       'AV-nodal blockers'],
                                           'answer': 'D) Immediate synchronized '
                                                     'cardioversion (if unstable) or '
                                                     'IV procainamide; avoid AV-nodal '
                                                     'blockers',
                                           'explanation': 'In AF with WPW, antegrade '
                                                          'conduction over the '
                                                          'accessory pathway can '
                                                          'produce extremely rapid '
                                                          'ventricular rates. AV-nodal '
                                                          'blockers (beta-blockers, '
                                                          'calcium-channel blockers, '
                                                          'digoxin, adenosine) '
                                                          'preferentially block the '
                                                          'node and may facilitate '
                                                          'pathway conduction, risking '
                                                          'VF. Unstable patients need '
                                                          'immediate cardioversion; '
                                                          'stable patients may receive '
                                                          'procainamide (or similar) '
                                                          'that slows pathway '
                                                          'conduction.',
                                           'choice_explanations': {'A': 'Beta-blockade '
                                                                        'is AV-nodal '
                                                                        'and '
                                                                        'contraindicated '
                                                                        'in preexcited '
                                                                        'AF because it '
                                                                        'can enhance '
                                                                        'accessory-pathway '
                                                                        'conduction.',
                                                                   'B': 'Digoxin '
                                                                        'blocks the AV '
                                                                        'node and is '
                                                                        'dangerous in '
                                                                        'WPW-related '
                                                                        'AF for the '
                                                                        'same reason.',
                                                                   'C': 'Verapamil is '
                                                                        'an AV-nodal '
                                                                        'blocker and '
                                                                        'may '
                                                                        'precipitate '
                                                                        'hemodynamic '
                                                                        'collapse or '
                                                                        'VF in '
                                                                        'preexcited '
                                                                        'AF.',
                                                                   'D': 'Unstable '
                                                                        'preexcited AF '
                                                                        'requires '
                                                                        'shock; if '
                                                                        'drugs are '
                                                                        'used, prefer '
                                                                        'procainamide '
                                                                        'and avoid '
                                                                        'AV-nodal '
                                                                        'blockers.'}}]},
                'cases': {'easy': [{'title': 'Mild Exertional Chest Tightness',
                                    'stem': 'A 55-year-old man gets central chest '
                                            'tightness when climbing stairs. It eases '
                                            'after 3 minutes of rest. Exam and resting '
                                            'ECG are normal.',
                                    'question': 'Most likely diagnosis?',
                                    'answer': 'Stable angina (exertional myocardial '
                                              'ischemia).',
                                    'discussion': 'Pattern is predictable exertional '
                                                  'pain relieved by rest. Risk-factor '
                                                  'modification and anti-anginal '
                                                  'strategy follow assessment.',
                                    'book_hint': "Harrison's — Ischemic Heart "
                                                 'Disease'}],
                          'medium': [{'title': 'Crushing Pain with Anterior STE',
                                      'stem': 'A 58-year-old diabetic has crushing '
                                              'retrosternal pain for 40 minutes with '
                                              'diaphoresis. ECG shows ST elevation in '
                                              'V2–V4.',
                                      'question': 'Diagnosis and immediate reperfusion '
                                                  'idea?',
                                      'answer': 'Anterior STEMI — urgent PCI (or '
                                                'timely fibrinolysis if PCI '
                                                'unavailable).',
                                      'discussion': 'Anterior STE is typically LAD '
                                                    'territory. Time-critical '
                                                    'reperfusion saves myocardium.',
                                      'book_hint': 'Braunwald — ACS'}],
                          'hard': [{'title': 'Inferior MI then Hypotension',
                                    'stem': 'A 64-year-old with inferior STEMI '
                                            'receives nitroglycerin and becomes '
                                            'hypotensive. JVP is raised, lungs are '
                                            'clear, and right-sided ECG leads show ST '
                                            'elevation.',
                                    'question': 'What complication is most likely and '
                                                'what is a key initial hemodynamic '
                                                'step?',
                                    'answer': 'RV infarction — cautious IV fluids for '
                                              'preload (avoid nitrates/diuretics that '
                                              'drop preload).',
                                    'discussion': 'RV depends on preload; vasodilators '
                                                  'can cause profound hypotension. '
                                                  'Reperfusion remains essential.',
                                    'book_hint': 'Braunwald — RV infarction'}],
                          'extreme': [{'title': 'ACS Mimic with Pulse Deficit',
                                       'stem': 'A 68-year-old hypertensive man has '
                                               'sudden severe tearing chest pain '
                                               'radiating to the back, a pulse deficit '
                                               'between arms, and a new soft aortic '
                                               'regurgitation murmur. Troponin is '
                                               'borderline; ECG is non-diagnostic. The '
                                               'team is about to load dual '
                                               'antiplatelets for NSTE-ACS.',
                                       'question': 'What should you do first '
                                                   'conceptually?',
                                       'answer': 'Stop ACS '
                                                 'anticoagulation/antiplatelet pathway '
                                                 'and urgently evaluate for aortic '
                                                 'dissection (CT angiography if '
                                                 'stable).',
                                       'discussion': 'Dissection can cause coronary '
                                                     'ostial compromise and AR. Wrong '
                                                     'therapy worsens outcomes. '
                                                     'Stabilize BP and get definitive '
                                                     'imaging.',
                                       'book_hint': "Braunwald / Harrison's — Aortic "
                                                    'dissection'}]}},
 'ophthalmology': {'label': 'Ophthalmology',
                   'books': ["Kanski's Clinical Ophthalmology",
                             "Vaughan & Asbury's General Ophthalmology",
                             "Clinical Ophthalmology — Parsons' "],
                   'pdf_notes': ['Red eye emergencies: angle-closure glaucoma, '
                                 'keratitis, uveitis, endophthalmitis.',
                                 'RAPD: swinging flashlight test — optic nerve / '
                                 'severe retinal disease.',
                                 'Diabetic retinopathy: microaneurysms, hemorrhages, '
                                 'exudates ± neovascularization.',
                                 "CN III palsy: eye 'down and out'; CN VI: failed "
                                 'abduction.',
                                 'Cataract: reversible surgically; AMD: irreversible '
                                 'central loss if advanced.'],
                   'questions': {'easy': [{'question': 'A relative afferent pupillary '
                                                       'defect (RAPD) is best '
                                                       'demonstrated at the bedside by '
                                                       'which examination maneuver?',
                                           'options': ['A) Swinging flashlight test '
                                                       'comparing consensual responses '
                                                       'between eyes',
                                                       'B) Measuring intraocular '
                                                       'pressure with digital '
                                                       'palpation alone',
                                                       'C) Confrontational visual '
                                                       'fields without assessing '
                                                       'pupils',
                                                       'D) Cover–uncover test for '
                                                       'latent phoria only'],
                                           'answer': 'A) Swinging flashlight test '
                                                     'comparing consensual responses '
                                                     'between eyes',
                                           'explanation': 'An RAPD indicates '
                                                          'asymmetric afferent input, '
                                                          'usually optic nerve or '
                                                          'severe retinal disease. The '
                                                          'swinging flashlight test '
                                                          'reveals paradoxical '
                                                          'dilation when light moves '
                                                          'to the affected eye because '
                                                          'that eye drives less '
                                                          'pupillomotor signal. IOP, '
                                                          'fields alone, and cover '
                                                          'testing do not specifically '
                                                          'detect RAPD.',
                                           'choice_explanations': {'A': 'The swinging '
                                                                        'flashlight '
                                                                        'compares '
                                                                        'afferent '
                                                                        'pupillary '
                                                                        'drive; '
                                                                        'paradoxical '
                                                                        'dilation '
                                                                        'marks an '
                                                                        'RAPD.',
                                                                   'B': 'Digital IOP '
                                                                        'estimation '
                                                                        'assesses '
                                                                        'pressure, not '
                                                                        'afferent '
                                                                        'pupillary '
                                                                        'asymmetry.',
                                                                   'C': 'Visual fields '
                                                                        'may be '
                                                                        'abnormal in '
                                                                        'optic '
                                                                        'neuropathy '
                                                                        'but do not '
                                                                        'demonstrate '
                                                                        'RAPD.',
                                                                   'D': 'Cover–uncover '
                                                                        'detects '
                                                                        'strabismus/phoria, '
                                                                        'unrelated to '
                                                                        'afferent '
                                                                        'pupillary '
                                                                        'defect.'}},
                                          {'question': 'A painful red eye with a '
                                                       'mid-dilated, poorly reactive '
                                                       'pupil and corneal edema most '
                                                       'strongly suggests which '
                                                       'emergency?',
                                           'options': ['A) Viral conjunctivitis with '
                                                       'watery discharge and follicles',
                                                       'B) Acute angle-closure '
                                                       'glaucoma with abrupt IOP rise',
                                                       'C) Blepharitis limited to '
                                                       'eyelid margin crusting',
                                                       'D) Uncomplicated dry-eye '
                                                       'syndrome without IOP change'],
                                           'answer': 'B) Acute angle-closure glaucoma '
                                                     'with abrupt IOP rise',
                                           'explanation': 'Acute angle closure blocks '
                                                          'aqueous outflow, spiking '
                                                          'IOP; ischemia and corneal '
                                                          'edema produce a mid-dilated '
                                                          'fixed pupil, pain, and '
                                                          'often nausea. '
                                                          'Conjunctivitis, '
                                                          'blepharitis, and dry eye '
                                                          'lack this pupil/IOP '
                                                          'pattern.',
                                           'choice_explanations': {'A': 'Viral '
                                                                        'conjunctivitis '
                                                                        'is usually '
                                                                        'bilateral or '
                                                                        'sequential '
                                                                        'with '
                                                                        'discharge, '
                                                                        'not a '
                                                                        'mid-dilated '
                                                                        'pupil and '
                                                                        'corneal edema '
                                                                        'from high '
                                                                        'IOP.',
                                                                   'B': 'Angle-closure '
                                                                        'glaucoma '
                                                                        'classically '
                                                                        'causes '
                                                                        'painful red '
                                                                        'eye, '
                                                                        'mid-dilated '
                                                                        'pupil, and '
                                                                        'corneal edema '
                                                                        'from acute '
                                                                        'hypertension '
                                                                        'of the eye.',
                                                                   'C': 'Blepharitis '
                                                                        'affects lid '
                                                                        'margins and '
                                                                        'does not '
                                                                        'dilate the '
                                                                        'pupil or '
                                                                        'acutely '
                                                                        'elevate IOP.',
                                                                   'D': 'Dry eye '
                                                                        'causes '
                                                                        'irritation '
                                                                        'without a '
                                                                        'fixed '
                                                                        'mid-dilated '
                                                                        'pupil or '
                                                                        'acute '
                                                                        'glaucomatous '
                                                                        'corneal '
                                                                        'edema.'}},
                                          {'question': 'An isolated cranial nerve VI '
                                                       'palsy primarily impairs which '
                                                       'ocular movement?',
                                           'options': ['A) Elevation of the eye in '
                                                       'adduction (inferior oblique '
                                                       'action)',
                                                       'B) Depression of the eye in '
                                                       'adduction (superior oblique '
                                                       'action)',
                                                       'C) Abduction of the eye '
                                                       '(lateral rectus function)',
                                                       'D) Lid elevation via levator '
                                                       'palpebrae superioris'],
                                           'answer': 'C) Abduction of the eye (lateral '
                                                     'rectus function)',
                                           'explanation': 'CN VI innervates the '
                                                          'lateral rectus, so palsy '
                                                          'causes impaired abduction '
                                                          'and horizontal diplopia '
                                                          'worse looking toward the '
                                                          'lesion. Vertical muscles '
                                                          'and levator are other '
                                                          'nerves.',
                                           'choice_explanations': {'A': 'Inferior '
                                                                        'oblique '
                                                                        'elevation in '
                                                                        'adduction is '
                                                                        'largely CN '
                                                                        'III, not VI.',
                                                                   'B': 'Superior '
                                                                        'oblique (CN '
                                                                        'IV) depresses '
                                                                        'the adducted '
                                                                        'eye.',
                                                                   'C': 'CN VI drives '
                                                                        'lateral '
                                                                        'rectus '
                                                                        'abduction; '
                                                                        'palsy limits '
                                                                        'looking '
                                                                        'outward.',
                                                                   'D': 'Levator lid '
                                                                        'elevation is '
                                                                        'CN III, not '
                                                                        'abducens.'}}],
                                 'medium': [{'question': 'Microaneurysms of diabetic '
                                                         'retinopathy are best '
                                                         'appreciated clinically on '
                                                         'which examination?',
                                             'options': ['A) External inspection of '
                                                         'the eyelids only',
                                                         'B) Confrontation fields '
                                                         'without fundus viewing',
                                                         'C) Tonometry without '
                                                         'ophthalmoscopy',
                                                         'D) Dilated fundoscopic (or '
                                                         'fundus photograph) '
                                                         'examination of the retina'],
                                             'answer': 'D) Dilated fundoscopic (or '
                                                       'fundus photograph) examination '
                                                       'of the retina',
                                             'explanation': 'Diabetic microaneurysms '
                                                            'are focal capillary '
                                                            'outpouchings seen on '
                                                            'dilated fundus exam or '
                                                            'photography as small red '
                                                            'dots, often early NPDR. '
                                                            'External exam, fields '
                                                            'alone, and IOP do not '
                                                            'visualize retinal '
                                                            'microvasculature.',
                                             'choice_explanations': {'A': 'Lid '
                                                                          'inspection '
                                                                          'cannot show '
                                                                          'retinal '
                                                                          'microaneurysms.',
                                                                     'B': 'Confrontation '
                                                                          'fields '
                                                                          'assess '
                                                                          'gross '
                                                                          'vision, not '
                                                                          'microvascular '
                                                                          'retinal '
                                                                          'lesions.',
                                                                     'C': 'Tonometry '
                                                                          'measures '
                                                                          'IOP and '
                                                                          'misses '
                                                                          'retinopathy '
                                                                          'findings.',
                                                                     'D': 'Dilated '
                                                                          'ophthalmoscopy/photography '
                                                                          'visualizes '
                                                                          'retinal '
                                                                          'microaneurysms '
                                                                          'directly.'}},
                                            {'question': 'Sudden monocular '
                                                         "'curtain-like' visual field "
                                                         'loss ascending or descending '
                                                         'is most concerning for which '
                                                         'process?',
                                             'options': ['A) Rhegmatogenous retinal '
                                                         'detachment separating '
                                                         'neurosensory retina from RPE',
                                                         'B) Typical migraine aura '
                                                         'lasting seconds with '
                                                         'headache always preceding '
                                                         'vision loss',
                                                         'C) Presbyopia from '
                                                         'age-related lens stiffening',
                                                         'D) Chronic open-angle '
                                                         'glaucoma with painless '
                                                         'gradual field constriction '
                                                         'only'],
                                             'answer': 'A) Rhegmatogenous retinal '
                                                       'detachment separating '
                                                       'neurosensory retina from RPE',
                                             'explanation': 'A curtain or shadow often '
                                                            'reflects retinal '
                                                            'detachment as the '
                                                            'neurosensory retina '
                                                            'separates, producing '
                                                            'corresponding field loss. '
                                                            'Migraine aura is usually '
                                                            'bilateral/scintillating '
                                                            'and transient; presbyopia '
                                                            'is refractive; chronic '
                                                            'glaucoma is gradual.',
                                             'choice_explanations': {'A': 'Detachment '
                                                                          'of '
                                                                          'neurosensory '
                                                                          'retina '
                                                                          'creates a '
                                                                          'progressive '
                                                                          'curtain-like '
                                                                          'scotoma '
                                                                          'matching '
                                                                          'the '
                                                                          'detached '
                                                                          'area.',
                                                                     'B': 'Migraine '
                                                                          'aura is '
                                                                          'typically '
                                                                          'transient '
                                                                          'positive '
                                                                          'phenomena, '
                                                                          'not a '
                                                                          'persistent '
                                                                          'curtain of '
                                                                          'monocular '
                                                                          'detachment.',
                                                                     'C': 'Presbyopia '
                                                                          'blurs near '
                                                                          'vision '
                                                                          'without '
                                                                          'acute '
                                                                          'curtain '
                                                                          'field loss.',
                                                                     'D': 'Chronic '
                                                                          'open-angle '
                                                                          'glaucoma '
                                                                          'progresses '
                                                                          'slowly and '
                                                                          'is not an '
                                                                          'abrupt '
                                                                          'curtain.'}},
                                            {'question': 'Compared with preseptal '
                                                         'cellulitis, which features '
                                                         'most raise concern for '
                                                         'orbital cellulitis requiring '
                                                         'urgent imaging and IV '
                                                         'therapy?',
                                             'options': ['A) Mild eyelid edema with '
                                                         'preserved motility and no '
                                                         'pain on eye movement',
                                                         'B) Proptosis, painful '
                                                         'ophthalmoplegia, and '
                                                         'possible afferent pupillary '
                                                         'defect or vision threat',
                                                         'C) Isolated conjunctival '
                                                         'follicles without orbital '
                                                         'signs',
                                                         'D) Unilateral watery tearing '
                                                         'after allergen exposure '
                                                         'only'],
                                             'answer': 'B) Proptosis, painful '
                                                       'ophthalmoplegia, and possible '
                                                       'afferent pupillary defect or '
                                                       'vision threat',
                                             'explanation': 'Orbital cellulitis '
                                                            'involves postseptal '
                                                            'tissues: proptosis, '
                                                            'painful restricted '
                                                            'motility, chemosis, and '
                                                            'risk to vision/optic '
                                                            'nerve or cavernous sinus. '
                                                            'Preseptal disease is '
                                                            'anterior to the septum '
                                                            'without those orbital '
                                                            'signs. Imaging and IV '
                                                            'antibiotics are urgent '
                                                            'when orbital involvement '
                                                            'is suspected.',
                                             'choice_explanations': {'A': 'Preserved '
                                                                          'motility '
                                                                          'without '
                                                                          'pain on '
                                                                          'movement '
                                                                          'fits '
                                                                          'preseptal '
                                                                          'rather than '
                                                                          'orbital '
                                                                          'infection.',
                                                                     'B': 'Proptosis '
                                                                          'and painful '
                                                                          'ophthalmoplegia '
                                                                          'indicate '
                                                                          'postseptal '
                                                                          'orbital '
                                                                          'involvement '
                                                                          'needing '
                                                                          'urgent '
                                                                          'care.',
                                                                     'C': 'Follicles '
                                                                          'suggest '
                                                                          'conjunctivitis, '
                                                                          'not orbital '
                                                                          'cellulitis.',
                                                                     'D': 'Allergic '
                                                                          'tearing '
                                                                          'lacks '
                                                                          'infectious '
                                                                          'orbital '
                                                                          'signs.'}}],
                                 'hard': [{'question': 'A 42-year-old notes unilateral '
                                                       'dim vision. Pupils show a '
                                                       'clear RAPD, but early '
                                                       'fundoscopy looks nearly '
                                                       'normal. Color desaturation is '
                                                       'present in the affected eye. '
                                                       'Which localization is most '
                                                       'likely?',
                                           'options': ['A) Uncorrected refractive '
                                                       'error alone without neural '
                                                       'pathway disease',
                                                       'B) Early cataract limited to '
                                                       'nuclear sclerosis without RAPD',
                                                       'C) Optic neuropathy (e.g., '
                                                       'optic neuritis) affecting '
                                                       'afferent conduction',
                                                       'D) Functional vision loss '
                                                       'without any afferent pupillary '
                                                       'abnormality'],
                                           'answer': 'C) Optic neuropathy (e.g., optic '
                                                     'neuritis) affecting afferent '
                                                     'conduction',
                                           'explanation': 'RAPD plus color '
                                                          'desaturation with a '
                                                          'relatively normal early '
                                                          'fundus points to optic '
                                                          'nerve dysfunction; optic '
                                                          'neuritis may look normal '
                                                          'initially. Pure refractive '
                                                          'error and cataract do not '
                                                          'cause RAPD; functional loss '
                                                          'should not produce '
                                                          'objective RAPD.',
                                           'choice_explanations': {'A': 'Refractive '
                                                                        'blur does not '
                                                                        'create an '
                                                                        'RAPD or color '
                                                                        'desaturation '
                                                                        'of optic '
                                                                        'neuropathy.',
                                                                   'B': 'Cataract '
                                                                        'reduces '
                                                                        'acuity but '
                                                                        'does not '
                                                                        'produce RAPD.',
                                                                   'C': 'Optic '
                                                                        'neuropathy '
                                                                        'impairs '
                                                                        'afferent '
                                                                        'input, '
                                                                        'yielding RAPD '
                                                                        'and '
                                                                        'dyschromatopsia '
                                                                        'even when the '
                                                                        'disc looks '
                                                                        'early-normal.',
                                                                   'D': 'True RAPD is '
                                                                        'an objective '
                                                                        'finding '
                                                                        'inconsistent '
                                                                        'with purely '
                                                                        'functional '
                                                                        'vision '
                                                                        'loss.'}},
                                          {'question': 'A 55-year-old develops acute '
                                                       'painful complete third-nerve '
                                                       'palsy with a dilated pupil '
                                                       'poorly reactive to light. '
                                                       'Which diagnosis must be '
                                                       'excluded first?',
                                           'options': ['A) Isolated diabetic '
                                                       'microvascular CN III palsy '
                                                       'with pupil sparing only',
                                                       'B) Myasthenia gravis with '
                                                       'fatigable ptosis and normal '
                                                       'pupils',
                                                       'C) Horner syndrome with miosis '
                                                       'rather than mydriasis',
                                                       'D) Posterior communicating '
                                                       'artery aneurysm compressing '
                                                       'pupillomotor fibers'],
                                           'answer': 'D) Posterior communicating '
                                                     'artery aneurysm compressing '
                                                     'pupillomotor fibers',
                                           'explanation': 'Pupillomotor fibers travel '
                                                          'on the superficial CN III; '
                                                          'compressive '
                                                          'lesions—especially PCOM '
                                                          'aneurysm—dilate the pupil '
                                                          'and threaten rupture. '
                                                          'Microvascular ischemic '
                                                          'palsy is usually '
                                                          'pupil-sparing; myasthenia '
                                                          'spares pupils; Horner '
                                                          'causes miosis.',
                                           'choice_explanations': {'A': 'Diabetic '
                                                                        'microvascular '
                                                                        'CN III palsy '
                                                                        'typically '
                                                                        'spares the '
                                                                        'pupil; '
                                                                        'painful '
                                                                        'pupil-involving '
                                                                        'palsy is '
                                                                        'compressive '
                                                                        'until proven '
                                                                        'otherwise.',
                                                                   'B': 'Myasthenia '
                                                                        'causes '
                                                                        'fatigable '
                                                                        'weakness with '
                                                                        'normal '
                                                                        'pupils, not '
                                                                        'acute fixed '
                                                                        'mydriasis.',
                                                                   'C': 'Horner '
                                                                        'syndrome '
                                                                        'produces '
                                                                        'ptosis with '
                                                                        'miosis, the '
                                                                        'opposite '
                                                                        'pupil '
                                                                        'finding.',
                                                                   'D': 'PCOM aneurysm '
                                                                        'can compress '
                                                                        'CN III '
                                                                        'including '
                                                                        'pupil '
                                                                        'fibers—an '
                                                                        'emergency to '
                                                                        'exclude.'}},
                                          {'question': 'A 70-year-old with atrial '
                                                       'fibrillation notices sudden '
                                                       'complete vision loss in one '
                                                       'eye. The pupil shows an RAPD '
                                                       'and the fundus has a pale '
                                                       'retina with a cherry-red '
                                                       'macula. Central retinal artery '
                                                       'occlusion typically presents '
                                                       'with which acute clinical '
                                                       'picture?',
                                           'options': ['A) Sudden painless monocular '
                                                       'vision loss with a relative '
                                                       'afferent pupillary defect and '
                                                       'cherry-red spot',
                                                       'B) Gradual bilateral field '
                                                       'loss over years with high IOP '
                                                       'only',
                                                       'C) Painful red eye with '
                                                       'photophobia and ciliary flush '
                                                       'from uveitis',
                                                       'D) Itchy watery eyes with '
                                                       'chemosis from allergic '
                                                       'conjunctivitis'],
                                           'answer': 'A) Sudden painless monocular '
                                                     'vision loss with a relative '
                                                     'afferent pupillary defect and '
                                                     'cherry-red spot',
                                           'explanation': 'CRAO abruptly cuts inner '
                                                          'retinal arterial perfusion, '
                                                          'causing sudden painless '
                                                          'severe monocular loss, '
                                                          'RAPD, and a cherry-red '
                                                          'fovea amid opacified '
                                                          'retina. Chronic glaucoma, '
                                                          'uveitis, and allergy '
                                                          'produce different tempos '
                                                          'and signs.',
                                           'choice_explanations': {'A': 'Arterial '
                                                                        'occlusion '
                                                                        'yields sudden '
                                                                        'painless '
                                                                        'loss, RAPD, '
                                                                        'and classic '
                                                                        'macular '
                                                                        'cherry-red '
                                                                        'spot.',
                                                                   'B': 'Chronic '
                                                                        'glaucoma is '
                                                                        'gradual and '
                                                                        'bilateral or '
                                                                        'asymmetric '
                                                                        'over time, '
                                                                        'not '
                                                                        'hyperacute '
                                                                        'CRAO.',
                                                                   'C': 'Anterior '
                                                                        'uveitis is '
                                                                        'painful with '
                                                                        'photophobia, '
                                                                        'not painless '
                                                                        'vascular '
                                                                        'occlusion.',
                                                                   'D': 'Allergic '
                                                                        'conjunctivitis '
                                                                        'preserves '
                                                                        'vision and '
                                                                        'lacks '
                                                                        'RAPD/cherry-red '
                                                                        'spot.'}}],
                                 'extreme': [{'question': 'A 74-year-old woman reports '
                                                          '48 hours of new headache, '
                                                          'jaw claudication when '
                                                          'chewing, and scalp '
                                                          'tenderness. ESR is 92 mm/h. '
                                                          'She awakens with sudden '
                                                          'profound vision loss in the '
                                                          'right eye; the disc is pale '
                                                          'and swollen. Which '
                                                          'immediate approach best '
                                                          'protects the fellow eye?',
                                              'options': ['A) Observe without steroids '
                                                          'until temporal artery '
                                                          'biopsy returns in 1–2 weeks',
                                                          'B) Start high-dose systemic '
                                                          'corticosteroids '
                                                          'immediately, then arrange '
                                                          'urgent temporal artery '
                                                          'biopsy without delaying '
                                                          'therapy',
                                                          'C) Give topical ocular '
                                                          'hypotensive drops alone for '
                                                          'presumed acute glaucoma',
                                                          'D) Perform immediate '
                                                          'contralateral prophylactic '
                                                          'enucleation to prevent '
                                                          'spread'],
                                              'answer': 'B) Start high-dose systemic '
                                                        'corticosteroids immediately, '
                                                        'then arrange urgent temporal '
                                                        'artery biopsy without '
                                                        'delaying therapy',
                                              'explanation': 'Giant cell arteritis '
                                                             'causes arteritic '
                                                             'anterior ischemic optic '
                                                             'neuropathy and can blind '
                                                             'the second eye within '
                                                             'days. High-dose steroids '
                                                             'must start on clinical '
                                                             'suspicion; biopsy '
                                                             'confirms but must not '
                                                             'delay treatment. Topical '
                                                             'IOP drops and '
                                                             'observation risk '
                                                             'irreversible bilateral '
                                                             'blindness; enucleation '
                                                             'is never indicated.',
                                              'choice_explanations': {'A': 'Waiting '
                                                                           'for biopsy '
                                                                           'before '
                                                                           'steroids '
                                                                           'risks '
                                                                           'contralateral '
                                                                           'arteritic '
                                                                           'AION.',
                                                                      'B': 'Immediate '
                                                                           'systemic '
                                                                           'steroids '
                                                                           'on '
                                                                           'suspicion, '
                                                                           'with '
                                                                           'prompt '
                                                                           'biopsy, is '
                                                                           'the '
                                                                           'vision-saving '
                                                                           'sequence '
                                                                           'in GCA.',
                                                                      'C': 'This is '
                                                                           'ischemic '
                                                                           'optic '
                                                                           'neuropathy '
                                                                           'from '
                                                                           'vasculitis, '
                                                                           'not '
                                                                           'primary '
                                                                           'angle-closure '
                                                                           'glaucoma.',
                                                                      'D': 'Enucleation '
                                                                           'has no '
                                                                           'role; the '
                                                                           'threat is '
                                                                           'systemic '
                                                                           'vasculitis '
                                                                           'to the '
                                                                           'fellow '
                                                                           'optic '
                                                                           'nerve.'}},
                                             {'question': 'A laboratory worker '
                                                          'splashes a strong alkali '
                                                          'into both eyes. He arrives '
                                                          'holding his lids shut in '
                                                          'pain. Which action takes '
                                                          'absolute priority over '
                                                          'other interventions?',
                                              'options': ['A) Obtain detailed pH '
                                                          'history and photograph the '
                                                          'injury before any '
                                                          'irrigation',
                                                          'B) Instill topical '
                                                          'anesthetic and send '
                                                          'immediately for CT orbits '
                                                          'before rinsing',
                                                          'C) Begin copious irrigation '
                                                          'immediately and continue '
                                                          'until the conjunctival pH '
                                                          'normalizes',
                                                          'D) Patch both eyes tightly '
                                                          'and discharge with '
                                                          'outpatient ophthalmology in '
                                                          '48 hours'],
                                              'answer': 'C) Begin copious irrigation '
                                                        'immediately and continue '
                                                        'until the conjunctival pH '
                                                        'normalizes',
                                              'explanation': 'Alkali penetrates ocular '
                                                             'tissues rapidly, '
                                                             'saponifying membranes. '
                                                             'Immediate prolonged '
                                                             'irrigation until neutral '
                                                             'pH limits deeper injury '
                                                             'and outweighs '
                                                             'documentation, imaging, '
                                                             'or delayed care. '
                                                             'Patching without '
                                                             'irrigation traps caustic '
                                                             'agent.',
                                              'choice_explanations': {'A': 'Delaying '
                                                                           'irrigation '
                                                                           'for '
                                                                           'history/photos '
                                                                           'allows '
                                                                           'ongoing '
                                                                           'chemical '
                                                                           'penetration.',
                                                                      'B': 'Imaging '
                                                                           'before '
                                                                           'irrigation '
                                                                           'wastes '
                                                                           'critical '
                                                                           'minutes; '
                                                                           'anesthesia '
                                                                           'may help '
                                                                           'open lids '
                                                                           'but '
                                                                           'irrigation '
                                                                           'is the '
                                                                           'priority.',
                                                                      'C': 'Immediate '
                                                                           'continuous '
                                                                           'irrigation '
                                                                           'until pH '
                                                                           'normalizes '
                                                                           'is the '
                                                                           'first and '
                                                                           'most '
                                                                           'important '
                                                                           'step in '
                                                                           'chemical '
                                                                           'eye '
                                                                           'injury.',
                                                                      'D': 'Delayed '
                                                                           'outpatient '
                                                                           'care after '
                                                                           'patching '
                                                                           'without '
                                                                           'irrigation '
                                                                           'risks '
                                                                           'devastating '
                                                                           'alkali '
                                                                           'burns.'}},
                                             {'question': 'An immunosuppressed '
                                                          '48-year-old after induction '
                                                          'chemotherapy develops a '
                                                          'painful red eye, dense '
                                                          'hypopyon, severe vision '
                                                          'loss, and fever. Blood '
                                                          'cultures are pending. Which '
                                                          'diagnosis must lead '
                                                          'management while cultures '
                                                          'return?',
                                              'options': ['A) Simple allergic '
                                                          'conjunctivitis treated with '
                                                          'antihistamine drops alone',
                                                          'B) Uncomplicated dry eye '
                                                          'managed with lubricant '
                                                          'drops only',
                                                          'C) Migraine aura with '
                                                          'photophobia and preserved '
                                                          'acuity',
                                                          'D) Endogenous '
                                                          'endophthalmitis from '
                                                          'hematogenous seeding '
                                                          'requiring urgent '
                                                          'ophthalmology and systemic '
                                                          'antimicrobials'],
                                              'answer': 'D) Endogenous endophthalmitis '
                                                        'from hematogenous seeding '
                                                        'requiring urgent '
                                                        'ophthalmology and systemic '
                                                        'antimicrobials',
                                              'explanation': 'Hypopyon, pain, and '
                                                             'severe vision loss in a '
                                                             'bacteremic/fungemic host '
                                                             'suggest endogenous '
                                                             'endophthalmitis—infection '
                                                             'inside the eye seeded '
                                                             'from blood. It is an '
                                                             'emergency needing '
                                                             'cultures, systemic '
                                                             'therapy, and often '
                                                             'intravitreal treatment. '
                                                             'Allergy, dry eye, and '
                                                             'migraine do not produce '
                                                             'hypopyon and febrile '
                                                             'vision collapse.',
                                              'choice_explanations': {'A': 'Allergy '
                                                                           'lacks '
                                                                           'hypopyon, '
                                                                           'fever, and '
                                                                           'profound '
                                                                           'vision '
                                                                           'loss.',
                                                                      'B': 'Dry eye is '
                                                                           'chronic '
                                                                           'irritation '
                                                                           'without '
                                                                           'intraocular '
                                                                           'pus or '
                                                                           'sepsis '
                                                                           'signs.',
                                                                      'C': 'Migraine '
                                                                           'does not '
                                                                           'cause '
                                                                           'hypopyon '
                                                                           'or red-eye '
                                                                           'infection '
                                                                           'signs.',
                                                                      'D': 'Endogenous '
                                                                           'endophthalmitis '
                                                                           'fits '
                                                                           'immunosuppression, '
                                                                           'hypopyon, '
                                                                           'and '
                                                                           'systemic '
                                                                           'infection—urgent '
                                                                           'dual '
                                                                           'ocular/systemic '
                                                                           'therapy.'}}]},
                   'cases': {'easy': [{'title': 'Red Eye After Dark Room',
                                       'stem': 'A 54-year-old hyperopic woman develops '
                                               'severe eye pain, halos, and nausea '
                                               'after leaving a dark cinema. Pupil is '
                                               'mid-dilated and poorly reactive.',
                                       'question': 'Most likely diagnosis?',
                                       'answer': 'Acute angle-closure glaucoma.',
                                       'discussion': 'Urgent IOP lowering and '
                                                     'ophthalmology referral; avoid '
                                                     'dilating drops.',
                                       'book_hint': "Kanski's Clinical Ophthalmology"}],
                             'medium': [{'title': 'Diabetic Blurry Vision',
                                         'stem': 'A 60-year-old with longstanding '
                                                 'diabetes has gradual blur. Fundus '
                                                 'shows hemorrhages, microaneurysms, '
                                                 'and hard exudates near the macula.',
                                         'question': 'Diagnosis category?',
                                         'answer': 'Diabetic retinopathy with possible '
                                                   'macular involvement.',
                                         'discussion': 'Glycemic/BP control + '
                                                       'ophthalmic management for '
                                                       'macular edema/proliferation.',
                                         'book_hint': "Kanski's Clinical "
                                                      'Ophthalmology'}],
                             'hard': [{'title': 'Pupil-Involving CN III',
                                       'stem': 'A 48-year-old with sudden unilateral '
                                               "ptosis, eye 'down and out', and a "
                                               'dilated poorly reactive pupil has a '
                                               'severe new headache. Decide the '
                                               'highest-yield urgent concept before '
                                               'results return.',
                                       'question': 'What dangerous cause must be '
                                                   'excluded?',
                                       'answer': 'Compressive CN III palsy from PCOM '
                                                 'aneurysm.',
                                       'discussion': 'Urgent neuroimaging/vascular '
                                                     'study; this is not a routine '
                                                     'outpatient palsy.',
                                       'book_hint': "Kanski's Clinical Ophthalmology"}],
                             'extreme': [{'title': 'GCA Threat to Vision',
                                          'stem': 'A 76-year-old woman with new '
                                                  'headache, jaw claudication, scalp '
                                                  'tenderness, and ESR 95 suddenly '
                                                  'loses vision in one eye. Fundus '
                                                  'suggests pale disc swelling. Avoid '
                                                  'interventions that could worsen an '
                                                  'unexcluded catastrophic '
                                                  'differential.',
                                          'question': 'Immediate management concept?',
                                          'answer': 'Treat as arteritic ischemic optic '
                                                    'neuropathy/GCA: urgent high-dose '
                                                    'steroids and urgent specialty '
                                                    'care; arrange temporal artery '
                                                    'biopsy without delaying steroids.',
                                          'discussion': 'Vision in the fellow eye is '
                                                        'at risk within days if '
                                                        'untreated.',
                                          'book_hint': "Kanski's Clinical "
                                                       'Ophthalmology'}]}},
 'urology': {'label': 'Urology',
             'books': ['Campbell-Walsh-Wein Urology',
                       "Smith's General Urology",
                       'Bailey & Love — Urology chapters'],
             'pdf_notes': ['Stone types: calcium oxalate most common; struvite with '
                           'urease organisms; uric acid radiolucent.',
                           'Loin→groin pain + hematuria = ureteric colic until proven '
                           'otherwise.',
                           'Painless hematuria: rule out malignancy (esp. smokers).',
                           'Pyelonephritis: fever + flank pain + UTI signs → '
                           'antibiotics ± imaging.',
                           'BPH: storage/voiding symptoms in older men; assess '
                           'PSA/exam judiciously.'],
             'questions': {'easy': [{'question': 'In most temperate adult populations, '
                                                 'the majority of kidney stones are '
                                                 'composed of which crystal type?',
                                     'options': ['A) Calcium oxalate (often with some '
                                                 'calcium phosphate)',
                                                 'B) Pure cystine from a transport '
                                                 'defect in every first stone',
                                                 'C) Struvite exclusively without '
                                                 'infection risk factors',
                                                 'D) Uric acid as the single '
                                                 'composition in >90% of first stones'],
                                     'answer': 'A) Calcium oxalate (often with some '
                                               'calcium phosphate)',
                                     'explanation': 'Calcium oxalate stones '
                                                    'predominate in adults, reflecting '
                                                    'urinary calcium and oxalate '
                                                    'supersaturation. Cystine stones '
                                                    'are uncommon genetic stones; '
                                                    'struvite requires '
                                                    'urease-producing infection; uric '
                                                    'acid is important but not the '
                                                    'majority of first stones.',
                                     'choice_explanations': {'A': 'Calcium oxalate is '
                                                                  'the most common '
                                                                  'stone composition '
                                                                  'in typical adult '
                                                                  'nephrolithiasis.',
                                                             'B': 'Cystinuria causes '
                                                                  'recurrent cystine '
                                                                  'stones but is rare, '
                                                                  "not 'most' stones.",
                                                             'C': 'Struvite stones '
                                                                  'form in alkaline '
                                                                  'infected urine, not '
                                                                  'the majority of '
                                                                  'idiopathic stones.',
                                                             'D': 'Uric acid stones '
                                                                  'are a substantial '
                                                                  'minority, not >90% '
                                                                  'of first '
                                                                  'presentations.'}},
                                    {'question': 'Severe colicky loin pain radiating '
                                                 'to the groin with restlessness is '
                                                 'most classic for which process?',
                                     'options': ['A) Chronic stable BPH without '
                                                 'obstruction',
                                                 'B) Ureteric colic from an '
                                                 'obstructing calculus',
                                                 'C) Painless microscopic hematuria '
                                                 'from a tiny bladder tumor only',
                                                 'D) Stress urinary incontinence with '
                                                 'coughing'],
                                     'answer': 'B) Ureteric colic from an obstructing '
                                               'calculus',
                                     'explanation': 'Ureteric obstruction triggers '
                                                    'visceral colic as peristalsis '
                                                    'against a blockage produces '
                                                    'severe loin-to-groin pain and '
                                                    'marked restlessness. BPH, '
                                                    'painless hematuria, and stress '
                                                    'incontinence lack this acute '
                                                    'colic pattern.',
                                     'choice_explanations': {'A': 'BPH causes voiding '
                                                                  'symptoms, not acute '
                                                                  'loin-to-groin '
                                                                  'colic.',
                                                             'B': 'An obstructing '
                                                                  'ureteric stone '
                                                                  'produces classic '
                                                                  'renal/ureteric '
                                                                  'colic radiating to '
                                                                  'the groin.',
                                                             'C': 'Bladder tumors more '
                                                                  'often cause '
                                                                  'painless hematuria '
                                                                  'than violent colic.',
                                                             'D': 'Stress incontinence '
                                                                  'is leakage with '
                                                                  'effort, not colicky '
                                                                  'flank pain.'}},
                                    {'question': 'For suspected urolithiasis in a '
                                                 'non-pregnant adult, which imaging '
                                                 'modality is usually preferred first '
                                                 'for high sensitivity?',
                                     'options': ['A) Plain abdominal radiograph alone '
                                                 'as definitive rule-out',
                                                 'B) Bedside ultrasound only without '
                                                 'any CT consideration',
                                                 'C) Non-contrast CT of the kidneys, '
                                                 'ureters, and bladder',
                                                 'D) Immediate invasive retrograde '
                                                 'pyelography before any CT'],
                                     'answer': 'C) Non-contrast CT of the kidneys, '
                                               'ureters, and bladder',
                                     'explanation': 'Non-contrast CT-KUB detects '
                                                    'nearly all stone sizes/locations '
                                                    'and secondary obstruction signs. '
                                                    'Plain films miss radiolucent '
                                                    'stones; ultrasound is useful '
                                                    '(pregnancy) but less sensitive '
                                                    'for ureteric stones; RPG is '
                                                    'interventional, not first-line '
                                                    'screening.',
                                     'choice_explanations': {'A': 'KUB radiographs '
                                                                  'miss many uric acid '
                                                                  'and small stones.',
                                                             'B': 'Ultrasound can miss '
                                                                  'mid-ureteric stones '
                                                                  'despite '
                                                                  'hydronephrosis '
                                                                  'clues.',
                                                             'C': 'Non-contrast CT is '
                                                                  'the most sensitive '
                                                                  'first-line study '
                                                                  'for adult stone '
                                                                  'disease.',
                                                             'D': 'Retrograde studies '
                                                                  'are '
                                                                  'therapeutic/diagnostic '
                                                                  'invasively, not '
                                                                  'initial imaging.'}}],
                           'medium': [{'question': 'Painless gross hematuria in a '
                                                   '68-year-old long-term smoker most '
                                                   'urgently raises concern for which '
                                                   'diagnosis?',
                                       'options': ['A) Uncomplicated orthostatic '
                                                   'proteinuria in adolescents',
                                                   'B) Exercise-induced hematuria that '
                                                   'always self-limits without '
                                                   'evaluation',
                                                   'C) Simple orthostatic hypotension '
                                                   'without urinary tract disease',
                                                   'D) Urothelial (bladder) carcinoma '
                                                   'until adequately investigated'],
                                       'answer': 'D) Urothelial (bladder) carcinoma '
                                                 'until adequately investigated',
                                       'explanation': 'Painless visible hematuria in '
                                                      'older smokers is a classic '
                                                      'presentation of bladder cancer '
                                                      'from urothelial carcinogen '
                                                      'exposure. It requires '
                                                      'cystoscopic and upper-tract '
                                                      'evaluation rather than '
                                                      'reassurance based on benign '
                                                      'young-adult entities.',
                                       'choice_explanations': {'A': 'Orthostatic '
                                                                    'proteinuria is a '
                                                                    'pediatric/young '
                                                                    'adult protein '
                                                                    'finding, not '
                                                                    'gross hematuria '
                                                                    'in elderly '
                                                                    'smokers.',
                                                               'B': 'Exercise '
                                                                    'hematuria is a '
                                                                    'diagnosis of '
                                                                    'exclusion and '
                                                                    'uncommon '
                                                                    'explanation in '
                                                                    'this demographic.',
                                                               'C': 'Hypotension does '
                                                                    'not cause '
                                                                    'painless gross '
                                                                    'hematuria.',
                                                               'D': 'Age plus smoking '
                                                                    'plus painless '
                                                                    'hematuria mandate '
                                                                    'workup for '
                                                                    'urothelial '
                                                                    'malignancy.'}},
                                      {'question': 'Fever, flank pain, and dysuria '
                                                   'with costovertebral angle '
                                                   'tenderness most likely represent '
                                                   'which infection level?',
                                       'options': ['A) Acute pyelonephritis involving '
                                                   'renal parenchyma',
                                                   'B) Asymptomatic bacteriuria '
                                                   'without tissue invasion',
                                                   'C) Urethritis limited to the '
                                                   'anterior urethra only',
                                                   'D) Epididymitis without any '
                                                   'upper-tract involvement possible'],
                                       'answer': 'A) Acute pyelonephritis involving '
                                                 'renal parenchyma',
                                       'explanation': 'Pyelonephritis is ascending or '
                                                      'hematogenous infection of the '
                                                      'kidney producing fever, CVA '
                                                      'tenderness, and UTI symptoms. '
                                                      'Asymptomatic bacteriuria lacks '
                                                      'fever/flank findings; '
                                                      'urethritis and epididymitis '
                                                      'localize differently.',
                                       'choice_explanations': {'A': 'Parenchymal renal '
                                                                    'infection '
                                                                    '(pyelonephritis) '
                                                                    'explains fever, '
                                                                    'flank pain, and '
                                                                    'CVA tenderness '
                                                                    'with UTI '
                                                                    'symptoms.',
                                                               'B': 'Asymptomatic '
                                                                    'bacteriuria by '
                                                                    'definition lacks '
                                                                    'these '
                                                                    'systemic/local '
                                                                    'inflammatory '
                                                                    'signs.',
                                                               'C': 'Isolated '
                                                                    'urethritis causes '
                                                                    'urethral symptoms '
                                                                    'without high '
                                                                    'fever and CVA '
                                                                    'tenderness.',
                                                               'D': 'Epididymitis '
                                                                    'causes scrotal '
                                                                    'pain; it does not '
                                                                    'produce classic '
                                                                    'pyelonephritis '
                                                                    'flank findings as '
                                                                    'the primary '
                                                                    'pattern.'}},
                                      {'question': 'Suspected testicular torsion in an '
                                                   'adolescent is managed with which '
                                                   'guiding principle?',
                                       'options': ['A) Observe 48 hours for '
                                                   'spontaneous detorsion before '
                                                   'surgical consult',
                                                   'B) Urgent urologic exploration—do '
                                                   'not delay for perfect imaging if '
                                                   'clinical suspicion is high',
                                                   'C) Oral antibiotics alone as '
                                                   'first-line definitive therapy',
                                                   'D) Scrotal elevation and ice packs '
                                                   'as sole therapy for 1 week'],
                                       'answer': 'B) Urgent urologic exploration—do '
                                                 'not delay for perfect imaging if '
                                                 'clinical suspicion is high',
                                       'explanation': 'Torsion strangulates spermatic '
                                                      'cord blood flow; viability '
                                                      'falls within hours. High '
                                                      'clinical suspicion warrants '
                                                      'immediate surgical exploration; '
                                                      'Doppler can support but must '
                                                      'not delay salvage. Antibiotics '
                                                      'treat infection, not ischemia.',
                                       'choice_explanations': {'A': 'Waiting days '
                                                                    'risks '
                                                                    'irreversible '
                                                                    'testicular '
                                                                    'necrosis.',
                                                               'B': 'Time-critical '
                                                                    'ischemia demands '
                                                                    'urgent '
                                                                    'exploration when '
                                                                    'torsion is '
                                                                    'likely.',
                                                               'C': 'Antibiotics '
                                                                    'address '
                                                                    'epididymo-orchitis, '
                                                                    'not cord torsion.',
                                                               'D': 'Supportive care '
                                                                    'alone cannot '
                                                                    'restore arterial '
                                                                    'inflow in '
                                                                    'torsion.'}}],
                           'hard': [{'question': 'A patient with an obstructing '
                                                 'ureteric stone develops high fever, '
                                                 'hypotension, and leukocytosis. Which '
                                                 'management priority is correct?',
                                     'options': ['A) Outpatient oral antibiotics and '
                                                 'elective lithotripsy in 6 weeks',
                                                 'B) Alpha-blocker trial alone without '
                                                 'source control',
                                                 'C) Urgent decompression of the '
                                                 'infected obstructed kidney plus '
                                                 'antibiotics',
                                                 'D) Immediate nephrectomy as the '
                                                 'first procedure in all such cases'],
                                     'answer': 'C) Urgent decompression of the '
                                               'infected obstructed kidney plus '
                                               'antibiotics',
                                     'explanation': 'Infected hydronephrosis is a '
                                                    'urologic emergency: obstruction '
                                                    'plus infection drives sepsis. '
                                                    'Source control via stent or '
                                                    'percutaneous nephrostomy plus '
                                                    'antibiotics is required; delayed '
                                                    'elective stone treatment or '
                                                    'medical therapy alone is unsafe. '
                                                    'Nephrectomy is last-resort for '
                                                    'nonviable kidneys, not first '
                                                    'step.',
                                     'choice_explanations': {'A': 'Outpatient delay in '
                                                                  'septic obstructed '
                                                                  'stone disease risks '
                                                                  'progressive septic '
                                                                  'shock.',
                                                             'B': 'Medical expulsion '
                                                                  'therapy does not '
                                                                  'drain an infected '
                                                                  'obstructed system.',
                                                             'C': 'Urgent drainage '
                                                                  '(stent/nephrostomy) '
                                                                  'plus antibiotics is '
                                                                  'mandatory for '
                                                                  'infected '
                                                                  'obstruction.',
                                                             'D': 'Nephrectomy is not '
                                                                  'the initial '
                                                                  'decompression '
                                                                  'strategy in '
                                                                  'salvageable '
                                                                  'kidneys.'}},
                                    {'question': 'After relief of bilateral chronic '
                                                 'urinary obstruction, a patient '
                                                 'produces large volumes of urine with '
                                                 'rising creatinine that then '
                                                 'improves. Which phenomenon is '
                                                 'occurring?',
                                     'options': ['A) SIADH with inappropriate '
                                                 'free-water retention',
                                                 'B) Acute urinary retention recurring '
                                                 'immediately',
                                                 'C) Primary polydipsia as the sole '
                                                 'driver without prior obstruction',
                                                 'D) Post-obstructive diuresis from '
                                                 'excretion of retained solute and '
                                                 'water'],
                                     'answer': 'D) Post-obstructive diuresis from '
                                               'excretion of retained solute and water',
                                     'explanation': 'Chronic obstruction expands '
                                                    'extracellular volume and '
                                                    'accumulates urea/salt. After '
                                                    'decompression, natriuresis and '
                                                    'water excretion produce polyuria '
                                                    '(post-obstructive diuresis) that '
                                                    'usually self-limits as volume '
                                                    'status normalizes but needs '
                                                    'monitoring for electrolyte '
                                                    'losses.',
                                     'choice_explanations': {'A': 'SIADH causes '
                                                                  'oliguria/hyponatremia '
                                                                  'from water '
                                                                  'retention, opposite '
                                                                  'of polyuria after '
                                                                  'relief.',
                                                             'B': 'Recurrent retention '
                                                                  'would reduce, not '
                                                                  'massively increase, '
                                                                  'urine output.',
                                                             'C': 'Primary polydipsia '
                                                                  'is not the '
                                                                  'mechanism after '
                                                                  'bilateral '
                                                                  'obstruction relief.',
                                                             'D': 'Post-obstructive '
                                                                  'diuresis reflects '
                                                                  'excretion of '
                                                                  'retained '
                                                                  'salt/water/urea '
                                                                  'after '
                                                                  'decompression.'}},
                                    {'question': 'A 15-year-old has sudden severe '
                                                 'testicular pain; the testis is '
                                                 'high-riding and the cremasteric '
                                                 'reflex is absent. Which diagnosis is '
                                                 'most likely?',
                                     'options': ['A) Spermatic cord torsion until '
                                                 'proven otherwise',
                                                 'B) Uncomplicated hydrocele without '
                                                 'ischemia',
                                                 'C) Varicocele that enlarges only on '
                                                 'standing',
                                                 'D) Referred pain from a renal stone '
                                                 'without scrotal findings'],
                                     'answer': 'A) Spermatic cord torsion until proven '
                                               'otherwise',
                                     'explanation': 'Acute pain, high-riding testis, '
                                                    'and lost cremasteric reflex are '
                                                    'classic for torsion. Hydrocele '
                                                    'and varicocele lack this ischemic '
                                                    'acute exam; referred stone pain '
                                                    'does not elevate the testis or '
                                                    'abolish the cremasteric reflex.',
                                     'choice_explanations': {'A': 'These exam findings '
                                                                  'are hallmark of '
                                                                  'testicular torsion '
                                                                  'requiring emergency '
                                                                  'action.',
                                                             'B': 'Hydrocele is a '
                                                                  'fluid collection '
                                                                  'without acute '
                                                                  'high-riding '
                                                                  'ischemic signs.',
                                                             'C': 'Varicocele is '
                                                                  'usually a painless '
                                                                  'bag of worms, not '
                                                                  'an acute surgical '
                                                                  'scrotum.',
                                                             'D': 'Ureteric colic can '
                                                                  'refer to the groin '
                                                                  'but does not '
                                                                  'produce a '
                                                                  'high-riding testis '
                                                                  'with lost '
                                                                  'cremasteric '
                                                                  'reflex.'}}],
                           'extreme': [{'question': 'A 62-year-old with poorly '
                                                    'controlled diabetes presents with '
                                                    'scrotal and perineal pain, fever, '
                                                    'and rapidly spreading erythema '
                                                    'with crepitus and foul discharge. '
                                                    'CT shows gas in soft tissues. He '
                                                    'is hypotensive. Which diagnosis '
                                                    'and priority are correct?',
                                        'options': ['A) Uncomplicated epididymitis '
                                                    'treatable with oral antibiotics '
                                                    'at home',
                                                    'B) Fournier gangrene—necrotizing '
                                                    'soft-tissue infection needing '
                                                    'immediate surgical debridement '
                                                    'plus broad antibiotics and '
                                                    'resuscitation',
                                                    'C) Simple cellulitis deferred for '
                                                    'outpatient review in 1 week',
                                                    'D) Isolated UTI without '
                                                    'soft-tissue involvement despite '
                                                    'crepitus and gas on CT'],
                                        'answer': 'B) Fournier gangrene—necrotizing '
                                                  'soft-tissue infection needing '
                                                  'immediate surgical debridement plus '
                                                  'broad antibiotics and resuscitation',
                                        'explanation': 'Fournier gangrene is '
                                                       'polymicrobial necrotizing '
                                                       'infection of the '
                                                       'perineum/genitalia, often in '
                                                       'diabetics, producing gas, '
                                                       'crepitus, and septic shock. '
                                                       'Survival depends on immediate '
                                                       'radical debridement and '
                                                       'antibiotics; oral outpatient '
                                                       'therapy is inadequate.',
                                        'choice_explanations': {'A': 'Epididymitis '
                                                                     'lacks crepitus, '
                                                                     'soft-tissue gas, '
                                                                     'and rapidly '
                                                                     'spreading '
                                                                     'necrosis.',
                                                                'B': 'Gas-forming '
                                                                     'perineal '
                                                                     'necrotizing '
                                                                     'infection '
                                                                     'defines Fournier '
                                                                     'gangrene and '
                                                                     'mandates '
                                                                     'emergent surgery '
                                                                     'plus '
                                                                     'antimicrobials.',
                                                                'C': 'Delaying care in '
                                                                     'necrotizing '
                                                                     'infection '
                                                                     'increases '
                                                                     'mortality '
                                                                     'dramatically.',
                                                                'D': 'Soft-tissue gas '
                                                                     'and crepitus '
                                                                     'prove deep '
                                                                     'infection beyond '
                                                                     'a simple UTI.'}},
                                       {'question': 'A T6 spinal cord–injured patient '
                                                    'develops sudden pounding '
                                                    'headache, flushing above the '
                                                    'lesion, and blood pressure '
                                                    '210/120 while his bladder has '
                                                    'been full for hours. Which '
                                                    'mechanism and response are most '
                                                    'accurate?',
                                        'options': ['A) Primary essential hypertension '
                                                    'unrelated to bladder volume',
                                                    'B) Orthostatic hypotension from '
                                                    'sitting too long',
                                                    'C) Autonomic dysreflexia '
                                                    'triggered by noxious stimulus '
                                                    'below the lesion—sit up, loosen '
                                                    'garments, and empty the bladder '
                                                    'urgently',
                                                    'D) Thyroid storm as the first '
                                                    'explanation for headache and '
                                                    'hypertension'],
                                        'answer': 'C) Autonomic dysreflexia triggered '
                                                  'by noxious stimulus below the '
                                                  'lesion—sit up, loosen garments, and '
                                                  'empty the bladder urgently',
                                        'explanation': 'In lesions above ~T6, bladder '
                                                       'distension or other noxious '
                                                       'stimuli below the lesion '
                                                       'trigger massive sympathetic '
                                                       'discharge (autonomic '
                                                       'dysreflexia), causing severe '
                                                       'hypertension and reflex '
                                                       'bradycardia/flushing. '
                                                       'Immediate removal of the '
                                                       'trigger (catheterize) and '
                                                       'upright positioning are '
                                                       'essential to prevent '
                                                       'stroke/hemorrhage.',
                                        'choice_explanations': {'A': 'This paroxysmal '
                                                                     'crisis with a '
                                                                     'clear bladder '
                                                                     'trigger is '
                                                                     'dysreflexia, not '
                                                                     'essential '
                                                                     'hypertension.',
                                                                'B': 'Orthostasis '
                                                                     'lowers BP; here '
                                                                     'BP is critically '
                                                                     'high.',
                                                                'C': 'Autonomic '
                                                                     'dysreflexia from '
                                                                     'bladder '
                                                                     'distension '
                                                                     'requires urgent '
                                                                     'stimulus removal '
                                                                     'and BP control '
                                                                     'measures.',
                                                                'D': 'Thyroid storm '
                                                                     'lacks this '
                                                                     'spinal-cord–stimulus '
                                                                     'pairing and is '
                                                                     'not the first '
                                                                     'explanation.'}},
                                       {'question': 'A trauma patient with an unstable '
                                                    'pelvic fracture has blood at the '
                                                    'urethral meatus and a high-riding '
                                                    'prostate. Before attempting Foley '
                                                    'catheterization, which action is '
                                                    'correct?',
                                        'options': ['A) Force a larger Foley '
                                                    'repeatedly until it passes at any '
                                                    'resistance',
                                                    'B) Blindly inflate the balloon in '
                                                    'the urethra if resistance is met',
                                                    'C) Give empiric anticoagulation '
                                                    'to prevent pelvic clot',
                                                    'D) Defer blind catheterization '
                                                    'and obtain retrograde '
                                                    'urethrography (or urology-guided '
                                                    'placement) to exclude urethral '
                                                    'disruption'],
                                        'answer': 'D) Defer blind catheterization and '
                                                  'obtain retrograde urethrography (or '
                                                  'urology-guided placement) to '
                                                  'exclude urethral disruption',
                                        'explanation': 'Blood at the meatus, pelvic '
                                                       'fracture, and high prostate '
                                                       'suggest urethral injury. Blind '
                                                       'catheterization can convert '
                                                       'partial disruption to complete '
                                                       'transection. Imaging or expert '
                                                       'placement is required first; '
                                                       'forcing catheters or balloon '
                                                       'inflation in the urethra '
                                                       'worsens injury; '
                                                       'anticoagulation is '
                                                       'contraindicated in bleeding '
                                                       'pelvic trauma.',
                                        'choice_explanations': {'A': 'Forcing a '
                                                                     'catheter against '
                                                                     'resistance risks '
                                                                     'completing a '
                                                                     'urethral tear.',
                                                                'B': 'Inflating a '
                                                                     'balloon in the '
                                                                     'urethra causes '
                                                                     'further trauma.',
                                                                'C': 'Anticoagulation '
                                                                     'worsens pelvic '
                                                                     'hemorrhage.',
                                                                'D': 'Suspect urethral '
                                                                     'injury—image/consult '
                                                                     'before blind '
                                                                     'Foley '
                                                                     'attempts.'}}]},
             'cases': {'easy': [{'title': 'Sudden Flank Pain',
                                 'stem': 'A 30-year-old man has sudden severe left '
                                         'flank pain radiating to the groin and cannot '
                                         'find a comfortable position. Dipstick shows '
                                         'blood.',
                                 'question': 'Likely diagnosis?',
                                 'answer': 'Ureteric colic from a stone.',
                                 'discussion': 'Analgesia and imaging; watch for '
                                               'infection/obstruction.',
                                 'book_hint': 'Campbell-Walsh-Wein Urology'}],
                       'medium': [{'title': 'Feverish Flank Pain',
                                   'stem': 'A 27-year-old woman has fever, vomiting, '
                                           'and right flank tenderness with '
                                           'nitrite-positive urine.',
                                   'question': 'Diagnosis?',
                                   'answer': 'Acute pyelonephritis.',
                                   'discussion': 'Cultures + antibiotics; image if not '
                                                 'improving or complicated.',
                                   'book_hint': 'Campbell-Walsh-Wein Urology'}],
                       'hard': [{'title': 'Obstructing Stone + Fever',
                                 'stem': 'A 45-year-old with a 9 mm proximal ureteric '
                                         'stone develops fever, rigors, and '
                                         'hypotension. Decide the highest-yield urgent '
                                         'concept before results return.',
                                 'question': 'Priority concept?',
                                 'answer': 'Treat as obstructed infected kidney: '
                                           'resuscitation, antibiotics, urgent '
                                           'drainage (stent/nephrostomy).',
                                 'discussion': 'Delay can lead to septic shock.',
                                 'book_hint': 'Campbell-Walsh-Wein Urology'}],
                       'extreme': [{'title': 'Trauma + Blood at Meatus',
                                    'stem': 'A motorcyclist with pelvic fracture has '
                                            'blood at the urethral meatus and a '
                                            'high-riding prostate on exam. The intern '
                                            'reaches for a Foley catheter. Avoid '
                                            'interventions that could worsen an '
                                            'unexcluded catastrophic differential.',
                                    'question': 'What is the correct concept?',
                                    'answer': 'Do not attempt blind catheterization; '
                                              'evaluate for urethral injury first '
                                              'while continuing trauma resuscitation.',
                                    'discussion': 'Wrong catheterization can convert '
                                                  'partial to complete urethral '
                                                  'injury.',
                                    'book_hint': 'Campbell-Walsh-Wein Urology'}]}},
 'neurology': {'label': 'Neurology',
               'books': ["Adams and Victor's Principles of Neurology",
                         "Harrison's — Neurology",
                         'Clinical Neurology — Simon R. / Brazis'],
               'pdf_notes': ['Stroke = sudden focal deficit — time is brain; use '
                             'FAST/NIHSS pathways.',
                             'UMN vs LMN: spasticity/hyperreflexia vs '
                             'flaccid/hyporeflexia/fasciculations.',
                             'SAH: thunderclap headache — urgent non-contrast CT ± LP.',
                             'Meningitis: fever, neck stiffness, altered mentation — '
                             'early antibiotics.',
                             'Migraine: unilateral throbbing ± '
                             'nausea/photo-phonophobia; rule out red flags.'],
               'questions': {'easy': [{'question': 'Sudden unilateral face and arm '
                                                   'weakness with aphasia most '
                                                   'strongly suggests acute ischemia '
                                                   'in which arterial distribution '
                                                   'conceptually?',
                                       'options': ['A) Anterior circulation (often '
                                                   'MCA) ischemic stroke until proven '
                                                   'otherwise',
                                                   'B) Chronic bilateral vestibular '
                                                   'neuronitis without focal cortical '
                                                   'signs',
                                                   'C) Isolated peripheral facial '
                                                   'nerve palsy with preserved arm '
                                                   'strength',
                                                   'D) Benign positional vertigo '
                                                   'limited to brief spinning with '
                                                   'head turns'],
                                       'answer': 'A) Anterior circulation (often MCA) '
                                                 'ischemic stroke until proven '
                                                 'otherwise',
                                       'explanation': 'Acute focal cortical deficits '
                                                      '(hemiparesis plus language) '
                                                      'localize to carotid/MCA '
                                                      'territory ischemia and are a '
                                                      'stroke emergency. Peripheral '
                                                      'VII palsy spares the arm; BPPV '
                                                      'and vestibular neuronitis lack '
                                                      'cortical motor/language '
                                                      'findings.',
                                       'choice_explanations': {'A': 'Face–arm weakness '
                                                                    'with aphasia is '
                                                                    'classic '
                                                                    'MCA/anterior-circulation '
                                                                    'stroke territory.',
                                                               'B': 'Vestibular '
                                                                    'neuronitis causes '
                                                                    'vertigo without '
                                                                    'aphasia or '
                                                                    'hemiparesis.',
                                                               'C': 'Bell’s palsy '
                                                                    'affects the face '
                                                                    'only and does not '
                                                                    'weaken the arm or '
                                                                    'cause aphasia.',
                                                               'D': 'BPPV is '
                                                                    'positional '
                                                                    'vertigo without '
                                                                    'lasting focal '
                                                                    'cortical '
                                                                    'deficits.'}},
                                      {'question': 'Which triad best captures classic '
                                                   'clinical meningism?',
                                       'options': ['A) Diplopia, ptosis, and '
                                                   'anisocoria only',
                                                   'B) Headache, neck stiffness, and '
                                                   'photophobia (often with fever)',
                                                   'C) Resting tremor, rigidity, and '
                                                   'bradykinesia only',
                                                   'D) Stocking-glove numbness from '
                                                   'distal axonopathy'],
                                       'answer': 'B) Headache, neck stiffness, and '
                                                 'photophobia (often with fever)',
                                       'explanation': 'Meningeal irritation produces '
                                                      'headache, nuchal rigidity, and '
                                                      'photophobia, frequently with '
                                                      'fever when infectious. Other '
                                                      'listed patterns reflect cranial '
                                                      'neuropathy, parkinsonism, or '
                                                      'neuropathy—not meningism.',
                                       'choice_explanations': {'A': 'Those oculomotor '
                                                                    'signs suggest '
                                                                    'cranial nerve '
                                                                    'lesions, not '
                                                                    'meningism per se.',
                                                               'B': 'Headache, stiff '
                                                                    'neck, and '
                                                                    'photophobia are '
                                                                    'the clinical core '
                                                                    'of meningism.',
                                                               'C': 'That triad '
                                                                    'defines '
                                                                    'parkinsonism, not '
                                                                    'meningeal '
                                                                    'irritation.',
                                                               'D': 'Length-dependent '
                                                                    'sensory loss is '
                                                                    'peripheral '
                                                                    'neuropathy, not '
                                                                    'meningism.'}},
                                      {'question': 'Which finding set is most '
                                                   'consistent with an upper motor '
                                                   'neuron lesion?',
                                       'options': ['A) Flaccid paralysis with early '
                                                   'severe atrophy and fasciculations',
                                                   'B) Hyporeflexia and muscle '
                                                   'hypotonia from the onset',
                                                   'C) Spastic weakness, '
                                                   'hyperreflexia, and Babinski sign',
                                                   'D) Pure sensory loss without any '
                                                   'motor pathway involvement'],
                                       'answer': 'C) Spastic weakness, hyperreflexia, '
                                                 'and Babinski sign',
                                       'explanation': 'UMN lesions remove descending '
                                                      'inhibition, yielding '
                                                      'spasticity, brisk reflexes, and '
                                                      'extensor plantar responses. LMN '
                                                      'lesions cause flaccid weakness, '
                                                      'hyporeflexia, and '
                                                      'fasciculations; pure sensory '
                                                      'findings are not motor-neuron '
                                                      'class signs.',
                                       'choice_explanations': {'A': 'Flaccid atrophy '
                                                                    'with '
                                                                    'fasciculations is '
                                                                    'lower motor '
                                                                    'neuron.',
                                                               'B': 'Hyporeflexia/hypotonia '
                                                                    'early suggest LMN '
                                                                    'or acute spinal '
                                                                    'shock, not '
                                                                    'chronic UMN '
                                                                    'pattern.',
                                                               'C': 'Spasticity, '
                                                                    'hyperreflexia, '
                                                                    'and Babinski are '
                                                                    'hallmark UMN '
                                                                    'signs.',
                                                               'D': 'Sensory-only '
                                                                    'findings do not '
                                                                    'define UMN motor '
                                                                    'pathway '
                                                                    'disease.'}}],
                             'medium': [{'question': 'A patient describes a '
                                                     'thunderclap headache reaching '
                                                     'maximal intensity within '
                                                     'seconds. Which diagnosis must be '
                                                     'excluded first?',
                                         'options': ['A) Tension-type headache from '
                                                     'muscle contraction alone',
                                                     'B) Medication-overuse headache '
                                                     'after months of analgesics',
                                                     'C) Typical migraine without any '
                                                     'vascular imaging indication',
                                                     'D) Subarachnoid hemorrhage until '
                                                     'imaging/LP evaluation is '
                                                     'complete'],
                                         'answer': 'D) Subarachnoid hemorrhage until '
                                                   'imaging/LP evaluation is complete',
                                         'explanation': 'Thunderclap onset is the '
                                                        'classic warning for '
                                                        'aneurysmal SAH. Even if '
                                                        'migraine is possible later, '
                                                        'SAH must be ruled out with '
                                                        'noncontrast CT ± LP because '
                                                        'missing it is catastrophic. '
                                                        'Primary headache diagnoses '
                                                        'are exclusions of secondary '
                                                        'causes.',
                                         'choice_explanations': {'A': 'Tension '
                                                                      'headache is '
                                                                      'gradual and '
                                                                      'pressure-like, '
                                                                      'not '
                                                                      'thunderclap.',
                                                                 'B': 'Medication-overuse '
                                                                      'develops '
                                                                      'chronically, '
                                                                      'not as a sudden '
                                                                      'maximal blast.',
                                                                 'C': 'Migraine can be '
                                                                      'severe but '
                                                                      'thunderclap '
                                                                      'requires SAH '
                                                                      'exclusion '
                                                                      'first.',
                                                                 'D': 'SAH presents '
                                                                      'with hyperacute '
                                                                      "'worst "
                                                                      "headache' and "
                                                                      'must be '
                                                                      'excluded '
                                                                      'urgently.'}},
                                        {'question': 'Brief staring spells with 3-Hz '
                                                     'spike-and-wave discharges on EEG '
                                                     'are most typical in which '
                                                     'epilepsy syndrome age group?',
                                         'options': ['A) Childhood absence epilepsy in '
                                                     'school-age children',
                                                     'B) Late-onset Alzheimer-related '
                                                     'seizures exclusively',
                                                     'C) Neonatal hypoxic seizures '
                                                     'only in the first hour of life',
                                                     'D) Alcohol-withdrawal seizures '
                                                     'in middle-aged adults only'],
                                         'answer': 'A) Childhood absence epilepsy in '
                                                   'school-age children',
                                         'explanation': 'Childhood absence epilepsy '
                                                        'features abrupt impaired '
                                                        'awareness with characteristic '
                                                        '3-Hz generalized '
                                                        'spike-and-wave. Other listed '
                                                        'settings have different '
                                                        'EEG/clinical patterns and '
                                                        'ages.',
                                         'choice_explanations': {'A': 'Absence '
                                                                      'seizures with '
                                                                      '3-Hz '
                                                                      'spike-and-wave '
                                                                      'are classic in '
                                                                      'childhood '
                                                                      'absence '
                                                                      'epilepsy.',
                                                                 'B': 'Alzheimer-related '
                                                                      'seizures are '
                                                                      'not defined by '
                                                                      'childhood '
                                                                      'absence EEG '
                                                                      'patterns.',
                                                                 'C': 'Neonatal '
                                                                      'seizures have '
                                                                      'diverse '
                                                                      'causes/EEG; not '
                                                                      'typical 3-Hz '
                                                                      'absence '
                                                                      'syndrome.',
                                                                 'D': 'Withdrawal '
                                                                      'seizures are '
                                                                      'generalized '
                                                                      'tonic-clonic in '
                                                                      'adults, not '
                                                                      'childhood '
                                                                      'absence.'}},
                                        {'question': 'Which motor feature is core to '
                                                     'the clinical diagnosis of '
                                                     'parkinsonism?',
                                         'options': ['A) Distal stocking-glove sensory '
                                                     'loss as the defining finding',
                                                     'B) Bradykinesia with resting '
                                                     'tremor and/or rigidity',
                                                     'C) Acute flaccid hemiplegia from '
                                                     'a single cortical stroke only',
                                                     'D) Fatigable ptosis that '
                                                     'improves after rest exclusively'],
                                         'answer': 'B) Bradykinesia with resting '
                                                   'tremor and/or rigidity',
                                         'explanation': 'Parkinsonism requires '
                                                        'bradykinesia plus resting '
                                                        'tremor and/or rigidity from '
                                                        'nigrostriatal dopamine '
                                                        'deficiency. Sensory '
                                                        'neuropathy, acute UMN stroke, '
                                                        'and myasthenic fatigability '
                                                        'are different syndromes.',
                                         'choice_explanations': {'A': 'Sensory '
                                                                      'neuropathy is '
                                                                      'not a core '
                                                                      'parkinsonian '
                                                                      'motor feature.',
                                                                 'B': 'Bradykinesia '
                                                                      'plus '
                                                                      'tremor/rigidity '
                                                                      'defines '
                                                                      'clinical '
                                                                      'parkinsonism.',
                                                                 'C': 'Stroke '
                                                                      'hemiplegia is '
                                                                      'pyramidal, not '
                                                                      'extrapyramidal '
                                                                      'parkinsonism.',
                                                                 'D': 'Fatigable '
                                                                      'ptosis suggests '
                                                                      'myasthenia '
                                                                      'gravis, not '
                                                                      'Parkinson '
                                                                      'disease.'}}],
                             'hard': [{'question': 'A patient continues convulsing for '
                                                   '8 minutes despite arrival of EMS. '
                                                   'Which initial pharmacologic '
                                                   'management concept is correct?',
                                       'options': ['A) Defer all benzodiazepines until '
                                                   'an EEG confirms status in the ICU',
                                                   'B) Start oral phenytoin loading as '
                                                   'the first drug before any IV '
                                                   'access attempt',
                                                   'C) Give a rapid-acting '
                                                   'benzodiazepine (e.g., IV '
                                                   'lorazepam) promptly while '
                                                   'supporting airway',
                                                   'D) Use only antipsychotic '
                                                   'medication to stop motor activity'],
                                       'answer': 'C) Give a rapid-acting '
                                                 'benzodiazepine (e.g., IV lorazepam) '
                                                 'promptly while supporting airway',
                                       'explanation': 'Convulsive status epilepticus '
                                                      'is time-critical brain injury; '
                                                      'early benzodiazepines terminate '
                                                      'seizures most effectively. '
                                                      'Waiting for EEG, oral loading, '
                                                      'or antipsychotics delays '
                                                      'definitive abortive therapy and '
                                                      'airway protection.',
                                       'choice_explanations': {'A': 'Clinical '
                                                                    'convulsive status '
                                                                    'should be treated '
                                                                    'immediately; EEG '
                                                                    'confirmation must '
                                                                    'not delay benzos.',
                                                               'B': 'Oral phenytoin is '
                                                                    'too slow and '
                                                                    'inappropriate as '
                                                                    'first abortive '
                                                                    'therapy.',
                                                               'C': 'Prompt IV/IM '
                                                                    'benzodiazepine is '
                                                                    'first-line '
                                                                    'abortive therapy '
                                                                    'in status '
                                                                    'epilepticus.',
                                                               'D': 'Antipsychotics do '
                                                                    'not treat '
                                                                    'epileptic status '
                                                                    'and may lower '
                                                                    'seizure '
                                                                    'threshold.'}},
                                      {'question': 'Ipsilateral cranial-nerve deficits '
                                                   'with contralateral hemiparesis '
                                                   'most precisely localize to which '
                                                   'region?',
                                       'options': ['A) Pure cortical MCA territory '
                                                   'without brainstem involvement',
                                                   'B) Distal peripheral nerve '
                                                   'entrapment in a limb',
                                                   'C) Cervical spinal cord hemicord '
                                                   '(Brown-Séquard) only',
                                                   'D) Brainstem (crossed findings '
                                                   'from compact cranial-nerve and '
                                                   'long-tract proximity)'],
                                       'answer': 'D) Brainstem (crossed findings from '
                                                 'compact cranial-nerve and long-tract '
                                                 'proximity)',
                                       'explanation': 'Crossed signs—ipsilateral CN '
                                                      'and contralateral body—are the '
                                                      'topographic signature of '
                                                      'brainstem lesions where nuclei '
                                                      'and corticospinal fibers are '
                                                      'adjacent. Cortex usually makes '
                                                      'ipsilateral face/arm together; '
                                                      'peripheral nerves lack '
                                                      'cranial-nerve crossing; '
                                                      'hemicord has different sensory '
                                                      'patterns.',
                                       'choice_explanations': {'A': 'Hemispheric '
                                                                    'lesions typically '
                                                                    'affect face and '
                                                                    'body on the same '
                                                                    'contralateral '
                                                                    'side without '
                                                                    'ipsilateral CN '
                                                                    'palsy pattern.',
                                                               'B': 'Peripheral '
                                                                    'entrapment cannot '
                                                                    'produce brainstem '
                                                                    'cranial-nerve '
                                                                    'signs.',
                                                               'C': 'Brown-Séquard '
                                                                    'causes '
                                                                    'ipsilateral '
                                                                    'motor/proprioceptive '
                                                                    'and contralateral '
                                                                    'pain/temp loss '
                                                                    'below the level, '
                                                                    'not cranial-nerve '
                                                                    'palsies.',
                                                               'D': 'Crossed '
                                                                    'cranial-nerve '
                                                                    'plus '
                                                                    'contralateral '
                                                                    'body signs '
                                                                    'localize to the '
                                                                    'brainstem.'}},
                                      {'question': 'Fatigable weakness that worsens '
                                                   'with activity and often involves '
                                                   'eyelids and extraocular muscles is '
                                                   'most characteristic of which '
                                                   'disorder?',
                                       'options': ['A) Myasthenia gravis from '
                                                   'autoantibodies against the '
                                                   'neuromuscular junction',
                                                   'B) Amyotrophic lateral sclerosis '
                                                   'presenting only with UMN signs',
                                                   'C) Guillain–Barré acute '
                                                   'demyelinating polyneuropathy with '
                                                   'areflexia as the sole eye finding',
                                                   'D) Parkinson disease defined by '
                                                   'fatigable ophthalmoplegia'],
                                       'answer': 'A) Myasthenia gravis from '
                                                 'autoantibodies against the '
                                                 'neuromuscular junction',
                                       'explanation': 'Myasthenia gravis impairs '
                                                      'acetylcholine receptor '
                                                      'signaling at the NMJ, producing '
                                                      'fatigable ocular and bulbar '
                                                      'weakness that improves with '
                                                      'rest. ALS mixes UMN/LMN without '
                                                      'true fatigable NMJ pattern; GBS '
                                                      'is areflexic paralysis; '
                                                      'Parkinsonism is extrapyramidal, '
                                                      'not fatigable ophthalmoplegia.',
                                       'choice_explanations': {'A': 'Antibody-mediated '
                                                                    'NMJ failure '
                                                                    'causes fatigable '
                                                                    'ptosis/diplopia '
                                                                    'classic for '
                                                                    'myasthenia.',
                                                               'B': 'ALS does not '
                                                                    'primarily present '
                                                                    'as fatigable '
                                                                    'ocular NMJ '
                                                                    'weakness.',
                                                               'C': 'GBS may rarely '
                                                                    'involve cranial '
                                                                    'nerves but is an '
                                                                    'acute areflexic '
                                                                    'neuropathy, not '
                                                                    'fatigable NMJ '
                                                                    'disease.',
                                                               'D': 'Parkinson disease '
                                                                    'features '
                                                                    'bradykinesia/tremor, '
                                                                    'not fatigable '
                                                                    'ocular '
                                                                    'weakness.'}}],
                             'extreme': [{'question': 'A 58-year-old with metastatic '
                                                      'prostate cancer develops '
                                                      'progressive bilateral leg '
                                                      'weakness over 48 hours, new '
                                                      'urinary retention, and saddle '
                                                      'anesthesia. MRI cannot be '
                                                      'obtained for 6 hours. '
                                                      'Dexamethasone has not yet been '
                                                      'given. Which priority is most '
                                                      'appropriate?',
                                          'options': ['A) Discharge with oral NSAIDs '
                                                      'and outpatient oncology in 2 '
                                                      'weeks',
                                                      'B) Treat as malignant spinal '
                                                      'cord compression—start '
                                                      'high-dose corticosteroids now '
                                                      'and arrange emergent '
                                                      'MRI/surgical or radiation '
                                                      'consultation without waiting '
                                                      "for 'perfect' logistics",
                                                      'C) Begin therapeutic '
                                                      'anticoagulation for presumed '
                                                      'cord infarct alone',
                                                      'D) Perform lumbar puncture '
                                                      'first to decompress the cord'],
                                          'answer': 'B) Treat as malignant spinal cord '
                                                    'compression—start high-dose '
                                                    'corticosteroids now and arrange '
                                                    'emergent MRI/surgical or '
                                                    'radiation consultation without '
                                                    "waiting for 'perfect' logistics",
                                          'explanation': 'Metastatic epidural cord '
                                                         'compression is a neurologic '
                                                         'emergency; hours matter for '
                                                         'ambulation. Steroids reduce '
                                                         'edema while definitive '
                                                         'imaging and '
                                                         'decompression/radiotherapy '
                                                         'are arranged. NSAIDs delay '
                                                         'care; empiric '
                                                         'anticoagulation misses the '
                                                         'mechanism; LP can worsen '
                                                         'compression and does not '
                                                         'decompress epidural tumor.',
                                          'choice_explanations': {'A': 'Outpatient '
                                                                       'delay risks '
                                                                       'permanent '
                                                                       'paraplegia in '
                                                                       'cord '
                                                                       'compression.',
                                                                  'B': 'Immediate '
                                                                       'steroids plus '
                                                                       'emergent '
                                                                       'imaging/definitive '
                                                                       'therapy is the '
                                                                       'correct '
                                                                       'sequence for '
                                                                       'suspected '
                                                                       'MSCC.',
                                                                  'C': 'Anticoagulation '
                                                                       'does not treat '
                                                                       'epidural tumor '
                                                                       'compression.',
                                                                  'D': 'LP is '
                                                                       'contraindicated '
                                                                       'conceptually '
                                                                       'as first '
                                                                       "'decompression' "
                                                                       'for epidural '
                                                                       'mass and may '
                                                                       'harm.'}},
                                         {'question': 'After basilar artery occlusion, '
                                                      'a patient is mute and '
                                                      'quadriplegic but can '
                                                      'communicate by vertical eye '
                                                      'movements and blinking. '
                                                      'Consciousness appears '
                                                      'preserved. Which localization '
                                                      'best explains locked-in '
                                                      'syndrome?',
                                          'options': ['A) Diffuse bilateral cortical '
                                                      'laminar necrosis with coma',
                                                      'B) Isolated left MCA '
                                                      'superior-division aphasia with '
                                                      'full limb strength',
                                                      'C) Bilateral ventral pontine '
                                                      'interruption of corticospinal '
                                                      'and corticobulbar tracts with '
                                                      'spared reticular activating '
                                                      'system and vertical gaze '
                                                      'centers',
                                                      'D) Complete cervical cord '
                                                      'transection with '
                                                      'unconsciousness'],
                                          'answer': 'C) Bilateral ventral pontine '
                                                    'interruption of corticospinal and '
                                                    'corticobulbar tracts with spared '
                                                    'reticular activating system and '
                                                    'vertical gaze centers',
                                          'explanation': 'Locked-in syndrome from '
                                                         'ventral pontine destruction '
                                                         'disconnects motor output '
                                                         'while arousal systems '
                                                         '(tegmentum) and often '
                                                         'vertical gaze remain, '
                                                         'allowing communication via '
                                                         'eyes. Cortical coma, MCA '
                                                         'aphasia, and cord '
                                                         'transection do not produce '
                                                         'this awake but de-efferented '
                                                         'pattern.',
                                          'choice_explanations': {'A': 'Diffuse '
                                                                       'cortical '
                                                                       'injury causes '
                                                                       'unconsciousness, '
                                                                       'not an awake '
                                                                       'locked-in '
                                                                       'state.',
                                                                  'B': 'MCA aphasia '
                                                                       'preserves limb '
                                                                       'movement on '
                                                                       'the '
                                                                       'ipsilateral '
                                                                       'side and is '
                                                                       'not '
                                                                       'quadriplegic '
                                                                       'mutism with '
                                                                       'vertical gaze '
                                                                       'only.',
                                                                  'C': 'Ventral pons '
                                                                       'lesion '
                                                                       'explains '
                                                                       'quadriplegia/anarthria '
                                                                       'with preserved '
                                                                       'wakefulness '
                                                                       'and vertical '
                                                                       'eye signaling.',
                                                                  'D': 'Cord '
                                                                       'transection '
                                                                       'does not '
                                                                       'abolish speech '
                                                                       'via '
                                                                       'corticobulbar '
                                                                       'interruption '
                                                                       'at the pons '
                                                                       'and does not '
                                                                       'define '
                                                                       'locked-in '
                                                                       'brainstem '
                                                                       'syndrome.'}},
                                         {'question': 'A 24-year-old woman develops '
                                                      'subacute psychiatric changes, '
                                                      'seizures, orofacial '
                                                      'dyskinesias, and autonomic '
                                                      'instability. MRI is often '
                                                      'near-normal; CSF may show mild '
                                                      'pleocytosis. Which association '
                                                      'is most important to seek?',
                                          'options': ['A) Multiple sclerosis plaques '
                                                      'strictly limited to the spinal '
                                                      'cord',
                                                      'B) Chronic B12 deficiency '
                                                      'without neuropsychiatric '
                                                      'features',
                                                      'C) Idiopathic intracranial '
                                                      'hypertension as the sole '
                                                      'explanation',
                                                      'D) Anti-NMDA receptor '
                                                      'encephalitis, often linked to '
                                                      'ovarian teratoma in young '
                                                      'women'],
                                          'answer': 'D) Anti-NMDA receptor '
                                                    'encephalitis, often linked to '
                                                    'ovarian teratoma in young women',
                                          'explanation': 'Anti-NMDA receptor '
                                                         'encephalitis produces a '
                                                         'characteristic progressive '
                                                         'syndrome of psychosis, '
                                                         'seizures, dyskinesias, and '
                                                         'dysautonomia. Young women '
                                                         'frequently harbor ovarian '
                                                         'teratoma; tumor search and '
                                                         'immunotherapy are critical. '
                                                         'MS, B12, and IIH do not '
                                                         'match this full phenotype.',
                                          'choice_explanations': {'A': 'Spinal MS does '
                                                                       'not produce '
                                                                       'this '
                                                                       'psychiatric–dyskinesia–autonomic '
                                                                       'constellation.',
                                                                  'B': 'B12 deficiency '
                                                                       'causes '
                                                                       'myeloneuropathy/cognitive '
                                                                       'change without '
                                                                       'this '
                                                                       'autoimmune '
                                                                       'encephalitis '
                                                                       'pattern.',
                                                                  'C': 'IIH causes '
                                                                       'headache/papilledema, '
                                                                       'not orofacial '
                                                                       'dyskinesias '
                                                                       'and '
                                                                       'dysautonomia.',
                                                                  'D': 'NMDA-receptor '
                                                                       'encephalitis '
                                                                       'fits the '
                                                                       'syndrome and '
                                                                       'warrants '
                                                                       'teratoma '
                                                                       'evaluation in '
                                                                       'young '
                                                                       'women.'}}]},
               'cases': {'easy': [{'title': 'Sudden Weakness',
                                   'stem': 'A 70-year-old develops sudden right '
                                           'arm/leg weakness and aphasia 40 minutes '
                                           'ago. Glucose is normal.',
                                   'question': 'Priority diagnosis pathway?',
                                   'answer': 'Acute stroke — activate stroke pathway.',
                                   'discussion': 'Time-critical imaging and '
                                                 'reperfusion eligibility.',
                                   'book_hint': "Adams and Victor / Harrison's "
                                                'Neurology'}],
                         'medium': [{'title': 'Worst Headache',
                                     'stem': 'A 45-year-old has the worst headache of '
                                             'life peaking in seconds with neck '
                                             'stiffness.',
                                     'question': 'What must be excluded?',
                                     'answer': 'Subarachnoid hemorrhage.',
                                     'discussion': 'Urgent non-contrast CT ± LP.',
                                     'book_hint': "Adams and Victor / Harrison's "
                                                  'Neurology'}],
                         'hard': [{'title': 'Fatigable Diplopia',
                                   'stem': 'A 34-year-old has fatigable ptosis and '
                                           'diplopia worse at night, improving with '
                                           'rest. Ice-pack test helps transiently. '
                                           'Labs and imaging are pending; you must '
                                           'choose the safest next clinical concept.',
                                   'question': 'Likely diagnosis?',
                                   'answer': 'Myasthenia gravis.',
                                   'discussion': 'Avoid certain drugs; assess '
                                                 'respiratory function; specialty '
                                                 'care.',
                                   'book_hint': "Adams and Victor / Harrison's "
                                                'Neurology'}],
                         'extreme': [{'title': 'Young Woman with Psychiatric then '
                                               'Seizure Cascade',
                                      'stem': 'A 24-year-old develops subacute '
                                              'psychosis, dyskinesias, autonomic '
                                              'instability, and refractory seizures. '
                                              'CT finds an ovarian teratoma. Multiple '
                                              'teams are involved; prioritize '
                                              'life/limb/vision threats and avoid '
                                              'harmful premature therapies.',
                                      'question': 'Syndrome to consider?',
                                      'answer': 'Anti-NMDA receptor encephalitis — '
                                                'immunotherapy + tumor removal '
                                                'pathway.',
                                      'discussion': 'Early recognition changes '
                                                    'outcome.',
                                      'book_hint': "Adams and Victor / Harrison's "
                                                   'Neurology'}]}},
 'pulmonology': {'label': 'Pulmonology',
                 'books': ["West's Respiratory Physiology",
                           "Harrison's — Respiratory Medicine",
                           "Crofton and Douglas's Respiratory Diseases"],
                 'pdf_notes': ['CAP: S. pneumoniae most common; assess CURB-65 '
                               'severity.',
                               'Asthma: reversible obstruction; COPD: largely '
                               'irreversible.',
                               'PE: sudden dyspnea/pleuritic pain post-risk — Wells + '
                               'CT PA pathway.',
                               'Tension pneumothorax: shock + tracheal deviation — '
                               'immediate decompression.',
                               'TB: chronic cough, night sweats, weight loss — '
                               'AFB/GeneXpert as available.'],
                 'questions': {'easy': [{'question': 'In immunocompetent adults, which '
                                                     'organism most commonly causes '
                                                     'typical community-acquired '
                                                     'pneumonia?',
                                         'options': ['A) Streptococcus pneumoniae as '
                                                     'the leading classic bacterial '
                                                     'cause',
                                                     'B) Mycobacterium tuberculosis as '
                                                     'the usual outpatient CAP '
                                                     'pathogen',
                                                     'C) Pneumocystis jirovecii in '
                                                     'patients with normal CD4 counts',
                                                     'D) Aspergillus fumigatus as '
                                                     'routine CAP in healthy hosts'],
                                         'answer': 'A) Streptococcus pneumoniae as the '
                                                   'leading classic bacterial cause',
                                         'explanation': 'S. pneumoniae remains the '
                                                        'most frequently identified '
                                                        'typical bacterial CAP '
                                                        'pathogen in immunocompetent '
                                                        'adults. TB, Pneumocystis, and '
                                                        'invasive Aspergillus occur in '
                                                        'distinct epidemiologic/host '
                                                        'niches, not routine CAP.',
                                         'choice_explanations': {'A': 'Pneumococcus is '
                                                                      'the classic '
                                                                      'leading '
                                                                      'bacterial cause '
                                                                      'of CAP in '
                                                                      'healthy adults.',
                                                                 'B': 'TB is a chronic '
                                                                      'granulomatous '
                                                                      'infection, not '
                                                                      'the usual acute '
                                                                      'CAP organism.',
                                                                 'C': 'Pneumocystis '
                                                                      'pneumonia '
                                                                      'mainly affects '
                                                                      'profound T-cell '
                                                                      'immunosuppression.',
                                                                 'D': 'Invasive '
                                                                      'aspergillosis '
                                                                      'targets '
                                                                      'neutropenic/immunocompromised '
                                                                      'hosts, not '
                                                                      'routine CAP.'}},
                                        {'question': 'Asthma is pathophysiologically '
                                                     'characterized by which airway '
                                                     'pattern?',
                                         'options': ['A) Fixed irreversible fibrosis '
                                                     'without any reversible component',
                                                     'B) Reversible '
                                                     'bronchoconstriction with airway '
                                                     'inflammation and '
                                                     'hyperresponsiveness',
                                                     'C) Pure alveolar destruction '
                                                     'without airway involvement '
                                                     '(emphysema only)',
                                                     'D) Pulmonary vascular '
                                                     'obliteration as the primary '
                                                     'lesion'],
                                         'answer': 'B) Reversible bronchoconstriction '
                                                   'with airway inflammation and '
                                                   'hyperresponsiveness',
                                         'explanation': 'Asthma combines '
                                                        'eosinophilic/inflammatory '
                                                        'airway disease, '
                                                        'hyperresponsiveness, and '
                                                        'largely reversible '
                                                        'obstruction. Fixed COPD '
                                                        'remodeling, pure emphysema, '
                                                        'and primary vasculopathy are '
                                                        'different diseases.',
                                         'choice_explanations': {'A': 'Fixed '
                                                                      'irreversible '
                                                                      'obstruction '
                                                                      'describes '
                                                                      'advanced COPD '
                                                                      'better than '
                                                                      'classic asthma.',
                                                                 'B': 'Asthma features '
                                                                      'reversible '
                                                                      'bronchoconstriction '
                                                                      'plus '
                                                                      'inflammatory '
                                                                      'hyperresponsiveness.',
                                                                 'C': 'Emphysema '
                                                                      'destroys '
                                                                      'alveoli; asthma '
                                                                      'is an airway '
                                                                      'disease.',
                                                                 'D': 'Pulmonary '
                                                                      'vascular '
                                                                      'disease (e.g., '
                                                                      'PAH) is not the '
                                                                      'primary asthma '
                                                                      'lesion.'}},
                                        {'question': 'Pulse oximetry (SpO2) primarily '
                                                     'estimates which physiologic '
                                                     'quantity?',
                                         'options': ['A) Arterial carbon dioxide '
                                                     'partial pressure directly',
                                                     'B) Mixed venous oxygen tension '
                                                     'in the pulmonary artery',
                                                     'C) Hemoglobin oxygen saturation '
                                                     'of pulsatile arterial blood',
                                                     'D) Alveolar minute ventilation '
                                                     'without regard to saturation'],
                                         'answer': 'C) Hemoglobin oxygen saturation of '
                                                   'pulsatile arterial blood',
                                         'explanation': 'SpO2 uses light absorbance of '
                                                        'pulsatile blood to estimate '
                                                        'arterial oxyhemoglobin '
                                                        'saturation. It does not '
                                                        'measure PaCO2, mixed venous '
                                                        'gas, or ventilation '
                                                        'directly—though desaturation '
                                                        'may accompany '
                                                        'hypoventilation.',
                                         'choice_explanations': {'A': 'PaCO2 requires '
                                                                      'blood gas or '
                                                                      'capnography, '
                                                                      'not pulse '
                                                                      'oximetry.',
                                                                 'B': 'Mixed venous O2 '
                                                                      'needs '
                                                                      'pulmonary-artery '
                                                                      'sampling, not '
                                                                      'fingertip SpO2.',
                                                                 'C': 'Pulse oximetry '
                                                                      'estimates '
                                                                      'arterial '
                                                                      'hemoglobin '
                                                                      'oxygen '
                                                                      'saturation.',
                                                                 'D': 'SpO2 does not '
                                                                      'quantify '
                                                                      'alveolar '
                                                                      'ventilation.'}}],
                               'medium': [{'question': 'The CURB-65 score is used '
                                                       'clinically to help decide '
                                                       'which management question in '
                                                       'pneumonia?',
                                           'options': ['A) Exact microbiologic species '
                                                       'before any antibiotics',
                                                       'B) Need for lung transplant '
                                                       'listing acutely',
                                                       'C) Whether latent TB should be '
                                                       'treated with INH alone',
                                                       'D) Site-of-care severity '
                                                       '(outpatient vs ward vs '
                                                       'higher-level care)'],
                                           'answer': 'D) Site-of-care severity '
                                                     '(outpatient vs ward vs '
                                                     'higher-level care)',
                                           'explanation': 'CURB-65 (Confusion, Urea, '
                                                          'Respiratory rate, Blood '
                                                          'pressure, age ≥65) '
                                                          'stratifies CAP severity to '
                                                          'guide disposition. It does '
                                                          'not identify pathogens, '
                                                          'transplant candidacy, or '
                                                          'latent TB therapy.',
                                           'choice_explanations': {'A': 'Scoring does '
                                                                        'not replace '
                                                                        'cultures or '
                                                                        'determine '
                                                                        'organism '
                                                                        'identity.',
                                                                   'B': 'CURB-65 is '
                                                                        'unrelated to '
                                                                        'transplant '
                                                                        'listing.',
                                                                   'C': 'Latent TB '
                                                                        'decisions use '
                                                                        'different '
                                                                        'criteria than '
                                                                        'CURB-65.',
                                                                   'D': 'CURB-65 '
                                                                        'guides '
                                                                        'pneumonia '
                                                                        'severity and '
                                                                        'site-of-care '
                                                                        'decisions.'}},
                                          {'question': 'Wells criteria are most '
                                                       'commonly applied to estimate '
                                                       'pretest probability of which '
                                                       'diagnosis?',
                                           'options': ['A) Pulmonary embolism (and '
                                                       'similarly DVT in related '
                                                       'scores)',
                                                       'B) Community-acquired '
                                                       'pneumonia severity alone',
                                                       'C) Asthma exacerbation '
                                                       'peak-flow severity only',
                                                       'D) Idiopathic pulmonary '
                                                       'fibrosis staging'],
                                           'answer': 'A) Pulmonary embolism (and '
                                                     'similarly DVT in related scores)',
                                           'explanation': 'Wells scoring incorporates '
                                                          'clinical features '
                                                          'suggesting VTE to estimate '
                                                          'PE (or DVT) pretest '
                                                          'probability and guide '
                                                          'D-dimer/imaging pathways. '
                                                          'It is not a pneumonia, '
                                                          'asthma, or IPF staging '
                                                          'tool.',
                                           'choice_explanations': {'A': 'Wells '
                                                                        'criteria '
                                                                        'stratify '
                                                                        'pretest '
                                                                        'probability '
                                                                        'for PE/DVT '
                                                                        'evaluation.',
                                                                   'B': 'Pneumonia '
                                                                        'severity uses '
                                                                        'CURB-65/PSI, '
                                                                        'not Wells.',
                                                                   'C': 'Asthma '
                                                                        'severity uses '
                                                                        'symptoms/peak '
                                                                        'flow/ABG, not '
                                                                        'Wells.',
                                                                   'D': 'IPF staging '
                                                                        'uses '
                                                                        'physiology/imaging, '
                                                                        'not Wells VTE '
                                                                        'scoring.'}},
                                          {'question': 'In many patients with COPD at '
                                                       'risk of CO2 retention, '
                                                       'recommended SpO2 targets '
                                                       'during controlled oxygen '
                                                       'therapy are often near which '
                                                       'range?',
                                           'options': ['A) 100% saturation '
                                                       'indefinitely with high-flow '
                                                       'oxygen regardless of pH',
                                                       'B) Approximately 88–92% to '
                                                       'balance hypoxia against '
                                                       'worsening hypercapnia',
                                                       'C) Below 80% deliberately to '
                                                       'stimulate hypoxic drive only',
                                                       'D) Ignore saturation and '
                                                       'titrate only to respiratory '
                                                       'rate'],
                                           'answer': 'B) Approximately 88–92% to '
                                                     'balance hypoxia against '
                                                     'worsening hypercapnia',
                                           'explanation': 'Excessive oxygen can worsen '
                                                          'V/Q matching and '
                                                          'hypercapnia in some COPD '
                                                          'patients. Target '
                                                          'saturations around 88–92% '
                                                          'correct dangerous hypoxia '
                                                          'while limiting CO2 rise; '
                                                          'aiming for 100% or '
                                                          'intentional deep '
                                                          'desaturation is harmful.',
                                           'choice_explanations': {'A': 'Pushing SpO2 '
                                                                        'to 100% with '
                                                                        'unrestricted '
                                                                        'O2 may '
                                                                        'aggravate '
                                                                        'hypercapnia/acidosis.',
                                                                   'B': '88–92% is the '
                                                                        'usual '
                                                                        'controlled-oxygen '
                                                                        'target band '
                                                                        'in CO2 '
                                                                        'retainers.',
                                                                   'C': 'Deliberate '
                                                                        'SpO2 <80% '
                                                                        'risks tissue '
                                                                        'hypoxia and '
                                                                        'is not '
                                                                        'therapy.',
                                                                   'D': 'Oxygen '
                                                                        'titration '
                                                                        'requires '
                                                                        'saturation '
                                                                        '(and ABG) '
                                                                        'monitoring, '
                                                                        'not rate '
                                                                        'alone.'}}],
                               'hard': [{'question': 'A trauma patient suddenly '
                                                     'develops severe dyspnea, '
                                                     'tracheal deviation away from one '
                                                     'side, absent breath sounds, and '
                                                     'hypotension. Which immediate '
                                                     'treatment concept is correct?',
                                         'options': ['A) Obtain a confirmatory chest '
                                                     'radiograph before any '
                                                     'decompression if unstable',
                                                     'B) Start heparin infusion for PE '
                                                     'without addressing airway '
                                                     'pressure',
                                                     'C) Perform immediate needle '
                                                     'decompression / finger '
                                                     'thoracostomy followed by chest '
                                                     'tube for tension pneumothorax',
                                                     'D) Give nebulized '
                                                     'bronchodilators as the primary '
                                                     'therapy'],
                                         'answer': 'C) Perform immediate needle '
                                                   'decompression / finger '
                                                   'thoracostomy followed by chest '
                                                   'tube for tension pneumothorax',
                                         'explanation': 'Tension pneumothorax traps '
                                                        'pleural air under pressure, '
                                                        'collapsing the lung and '
                                                        'obstructing venous return. '
                                                        'Unstable patients need '
                                                        'immediate decompression, not '
                                                        'imaging delay. Heparin and '
                                                        'bronchodilators miss the '
                                                        'obstructive mechanism.',
                                         'choice_explanations': {'A': 'Imaging delay '
                                                                      'in unstable '
                                                                      'tension '
                                                                      'physiology can '
                                                                      'be fatal.',
                                                                 'B': 'Anticoagulation '
                                                                      'treats PE, not '
                                                                      'pressurized '
                                                                      'pleural air.',
                                                                 'C': 'Urgent pleural '
                                                                      'decompression '
                                                                      'then chest '
                                                                      'drainage is '
                                                                      'definitive '
                                                                      'initial '
                                                                      'management of '
                                                                      'tension '
                                                                      'pneumothorax.',
                                                                 'D': 'Bronchodilators '
                                                                      'treat airway '
                                                                      'obstruction, '
                                                                      'not pleural '
                                                                      'tension.'}},
                                        {'question': 'A hospitalized patient has a new '
                                                     'pleural effusion. Thoracentesis '
                                                     'yields fluid for chemistry '
                                                     'compared with simultaneous serum '
                                                     'values. Light’s criteria are '
                                                     'used to distinguish which '
                                                     'pleural fluid categories?',
                                         'options': ['A) Bacterial versus viral '
                                                     'pneumonia on sputum Gram stain '
                                                     'alone',
                                                     'B) Restrictive versus '
                                                     'obstructive spirometry patterns',
                                                     'C) Cardiogenic versus '
                                                     'noncardiogenic edema on chest '
                                                     'radiograph only',
                                                     'D) Transudate versus exudate '
                                                     'based on fluid/serum protein and '
                                                     'LDH ratios'],
                                         'answer': 'D) Transudate versus exudate based '
                                                   'on fluid/serum protein and LDH '
                                                   'ratios',
                                         'explanation': 'Light’s criteria compare '
                                                        'pleural and serum protein/LDH '
                                                        'to separate exudates '
                                                        '(inflammation/infection/malignancy) '
                                                        'from transudates '
                                                        '(hydrostatic/oncotic '
                                                        'imbalances). They do not '
                                                        'classify pneumonia etiology, '
                                                        'spirometry, or radiographic '
                                                        'edema type alone.',
                                         'choice_explanations': {'A': 'Gram stain '
                                                                      'addresses '
                                                                      'microbiology, '
                                                                      'not Light’s '
                                                                      'biochemical '
                                                                      'classification.',
                                                                 'B': 'Spirometry '
                                                                      'characterizes '
                                                                      'airflow, '
                                                                      'unrelated to '
                                                                      'Light’s '
                                                                      'criteria.',
                                                                 'C': 'Radiographs '
                                                                      'alone do not '
                                                                      'apply Light’s '
                                                                      'pleural '
                                                                      'chemistry '
                                                                      'rules.',
                                                                 'D': 'Light’s '
                                                                      'protein/LDH '
                                                                      'ratios classify '
                                                                      'pleural fluid '
                                                                      'as exudate or '
                                                                      'transudate.'}},
                                        {'question': 'In massive hemoptysis, which '
                                                     'priority precedes definitive '
                                                     'embolization or resection '
                                                     'planning?',
                                         'options': ['A) Airway protection—secure '
                                                     'ventilation and position the '
                                                     'bleeding lung dependent when '
                                                     'possible',
                                                     'B) Immediate full '
                                                     'anticoagulation to prevent clot '
                                                     'in the bleeding vessel',
                                                     'C) Outpatient CT follow-up in 2 '
                                                     'weeks if vitals are presently '
                                                     'stable enough to walk',
                                                     'D) Blind bilateral lung '
                                                     'transplant listing as first '
                                                     'response'],
                                         'answer': 'A) Airway protection—secure '
                                                   'ventilation and position the '
                                                   'bleeding lung dependent when '
                                                   'possible',
                                         'explanation': 'Massive hemoptysis kills by '
                                                        'asphyxiation more than '
                                                        'exsanguination. Protecting '
                                                        'the airway, isolating the '
                                                        'bleeding side when feasible, '
                                                        'and stabilizing gas exchange '
                                                        'come before elective imaging '
                                                        'pathways; anticoagulation '
                                                        'worsens bleeding.',
                                         'choice_explanations': {'A': 'Securing the '
                                                                      'airway and '
                                                                      'protecting the '
                                                                      'non-bleeding '
                                                                      'lung is the '
                                                                      'first priority '
                                                                      'in massive '
                                                                      'hemoptysis.',
                                                                 'B': 'Anticoagulation '
                                                                      'aggravates '
                                                                      'airway '
                                                                      'hemorrhage.',
                                                                 'C': 'Deferring '
                                                                      'unstable or '
                                                                      'large-volume '
                                                                      'hemoptysis is '
                                                                      'unsafe.',
                                                                 'D': 'Transplant is '
                                                                      'not acute '
                                                                      'hemoptysis '
                                                                      'first aid.'}}],
                               'extreme': [{'question': 'A previously healthy '
                                                        '34-year-old develops severe '
                                                        'hypoxemia (PaO2/FiO2 120) '
                                                        'after influenza, bilateral '
                                                        'opacities not fully explained '
                                                        'by effusion or collapse, and '
                                                        'pulmonary artery wedge '
                                                        'pressure is not elevated. '
                                                        'Which Berlin ARDS framework '
                                                        'element is illustrated, and '
                                                        'which ventilator concept '
                                                        'follows?',
                                            'options': ['A) Cardiogenic edema from '
                                                        'left atrial hypertension as '
                                                        'the defining ARDS criterion',
                                                        'B) Acute hypoxemic '
                                                        'respiratory failure with '
                                                        'bilateral opacities not '
                                                        'primarily cardiogenic—use '
                                                        'lung-protective low tidal '
                                                        'volume ventilation',
                                                        'C) Chronic fibrotic ILD '
                                                        'present for years before any '
                                                        'acute illness',
                                                        'D) Simple atelectasis of one '
                                                        'lobe cured by chest '
                                                        'physiotherapy alone always'],
                                            'answer': 'B) Acute hypoxemic respiratory '
                                                      'failure with bilateral '
                                                      'opacities not primarily '
                                                      'cardiogenic—use lung-protective '
                                                      'low tidal volume ventilation',
                                            'explanation': 'Berlin ARDS requires acute '
                                                           'onset, bilateral '
                                                           'opacities, impaired '
                                                           'oxygenation, and exclusion '
                                                           'of isolated hydrostatic '
                                                           'edema. Lung-protective '
                                                           'ventilation (≈6 mL/kg PBW) '
                                                           'reduces volutrauma and '
                                                           'mortality. Cardiogenic '
                                                           'edema, chronic ILD, and '
                                                           'simple atelectasis are '
                                                           'different entities.',
                                            'choice_explanations': {'A': 'Elevated '
                                                                         'left atrial '
                                                                         'pressure '
                                                                         'defines '
                                                                         'cardiogenic '
                                                                         'edema, which '
                                                                         'must be '
                                                                         'excluded for '
                                                                         'ARDS.',
                                                                    'B': 'This meets '
                                                                         'ARDS '
                                                                         'criteria; '
                                                                         'low-tidal-volume '
                                                                         'ventilation '
                                                                         'is '
                                                                         'foundational '
                                                                         'therapy.',
                                                                    'C': 'Chronic ILD '
                                                                         'does not '
                                                                         'fulfill the '
                                                                         'acute ARDS '
                                                                         'timing '
                                                                         'criterion.',
                                                                    'D': 'Lobar '
                                                                         'atelectasis '
                                                                         'is not '
                                                                         'diffuse ARDS '
                                                                         'and is not '
                                                                         'managed '
                                                                         'solely as '
                                                                         'such.'}},
                                           {'question': 'Twenty-four hours after '
                                                        'long-bone fracture fixation, '
                                                        'a young adult develops acute '
                                                        'dyspnea, petechiae over the '
                                                        'chest, and new confusion. '
                                                        'Which triad diagnosis is most '
                                                        'likely?',
                                            'options': ['A) Uncomplicated atelectasis '
                                                        'from shallow breathing only',
                                                        'B) Hospital-acquired '
                                                        'pneumonia on day 1 without '
                                                        'systemic signs',
                                                        'C) Fat embolism syndrome '
                                                        'after orthopedic injury',
                                                        'D) Typical asthma '
                                                        'exacerbation without fracture '
                                                        'association'],
                                            'answer': 'C) Fat embolism syndrome after '
                                                      'orthopedic injury',
                                            'explanation': 'Fat embolism syndrome '
                                                           'classically follows '
                                                           'long-bone/pelvic fractures '
                                                           'with a latent period, then '
                                                           'respiratory distress, '
                                                           'neurologic change, and '
                                                           'axillary/conjunctival '
                                                           'petechiae as marrow fat '
                                                           'embolizes. Isolated '
                                                           'atelectasis, early HAP, '
                                                           'and asthma lack this triad '
                                                           'and setting.',
                                            'choice_explanations': {'A': 'Atelectasis '
                                                                         'does not '
                                                                         'produce '
                                                                         'petechiae '
                                                                         'and acute '
                                                                         'encephalopathy '
                                                                         'triad.',
                                                                    'B': 'Day-1 '
                                                                         'postoperative '
                                                                         'pneumonia is '
                                                                         'less likely '
                                                                         'than fat '
                                                                         'embolism '
                                                                         'given the '
                                                                         'classic '
                                                                         'triad '
                                                                         'timing.',
                                                                    'C': 'Respiratory '
                                                                         'failure + '
                                                                         'petechiae + '
                                                                         'confusion '
                                                                         'after '
                                                                         'fracture '
                                                                         'fixation '
                                                                         'indicates '
                                                                         'fat embolism '
                                                                         'syndrome.',
                                                                    'D': 'Asthma is '
                                                                         'unrelated to '
                                                                         'fracture-associated '
                                                                         'petechial '
                                                                         'encephalopathy.'}},
                                           {'question': 'A nonsmoking young adult with '
                                                        'recurrent hemoptysis and a '
                                                        'central endobronchial mass is '
                                                        'found to have a typical '
                                                        'bronchial carcinoid. Which '
                                                        'paraneoplastic theme may '
                                                        'accompany some neuroendocrine '
                                                        'bronchial tumors?',
                                            'options': ['A) SIADH exclusively from '
                                                        'squamous cell carcinoma only, '
                                                        'never neuroendocrine tumors',
                                                        'B) Pure mechanical '
                                                        'obstruction without any '
                                                        'possible hormone secretion '
                                                        'ever',
                                                        'C) Myasthenia gravis as the '
                                                        'universal presenting feature '
                                                        'of all carcinoids',
                                                        'D) Cushing syndrome from ACTH '
                                                        'secretion as one possible '
                                                        'neuroendocrine manifestation'],
                                            'answer': 'D) Cushing syndrome from ACTH '
                                                      'secretion as one possible '
                                                      'neuroendocrine manifestation',
                                            'explanation': 'Pulmonary neuroendocrine '
                                                           'tumors can secrete '
                                                           'bioactive peptides; ACTH '
                                                           'production may cause '
                                                           'Cushing syndrome, and '
                                                           'carcinoid syndrome is more '
                                                           'typical of metastatic '
                                                           'midgut disease but related '
                                                           'biology exists. Squamous '
                                                           'SIADH is a different '
                                                           'classic pairing; '
                                                           'carcinoids often obstruct '
                                                           'airways; MG is not '
                                                           'universal.',
                                            'choice_explanations': {'A': 'SIADH is '
                                                                         'classically '
                                                                         'small-cell; '
                                                                         'saying '
                                                                         'neuroendocrine '
                                                                         'tumors never '
                                                                         'secrete '
                                                                         'hormones is '
                                                                         'false—ACTH '
                                                                         'is '
                                                                         'recognized.',
                                                                    'B': 'While '
                                                                         'obstruction '
                                                                         'is common, '
                                                                         'some '
                                                                         'carcinoids/neuroendocrine '
                                                                         'tumors do '
                                                                         'secrete '
                                                                         'hormones.',
                                                                    'C': 'Myasthenia '
                                                                         'is linked to '
                                                                         'thymoma, not '
                                                                         'universally '
                                                                         'to bronchial '
                                                                         'carcinoid.',
                                                                    'D': 'Ectopic ACTH '
                                                                         'from '
                                                                         'pulmonary '
                                                                         'neuroendocrine '
                                                                         'tumors can '
                                                                         'produce '
                                                                         'Cushing '
                                                                         'syndrome.'}}]},
                 'cases': {'easy': [{'title': 'Fever + Productive Cough',
                                     'stem': 'A 60-year-old has fever, rusty sputum, '
                                             'and focal crackles. CXR shows lobar '
                                             'consolidation.',
                                     'question': 'Likely diagnosis?',
                                     'answer': 'Community-acquired pneumonia.',
                                     'discussion': 'Severity score + antibiotics + '
                                                   'oxygen if needed.',
                                     'book_hint': "Harrison's Respiratory / West"}],
                           'medium': [{'title': 'Post-Flight Dyspnea',
                                       'stem': 'A 42-year-old after a long flight has '
                                               'sudden dyspnea and pleuritic pain. '
                                               'SpO2 91%.',
                                       'question': 'Top diagnosis to exclude?',
                                       'answer': 'Pulmonary embolism.',
                                       'discussion': 'Risk stratify and image/treat '
                                                     'per pathway.',
                                       'book_hint': "Harrison's Respiratory / West"}],
                           'hard': [{'title': 'Asthma Near-Fatal',
                                     'stem': 'A teen with asthma is silent-chested, '
                                             'hypoxic, and tiring with rising CO2. '
                                             'Labs and imaging are pending; you must '
                                             'choose the safest next clinical concept.',
                                     'question': 'What does this imply?',
                                     'answer': 'Life-threatening asthma — escalate to '
                                               'emergency airway/ventilatory support '
                                               'pathway.',
                                     'discussion': 'A silent chest is ominous.',
                                     'book_hint': "Harrison's Respiratory / West"}],
                           'extreme': [{'title': 'Post-Op Hypoxemia + Petechiae',
                                        'stem': 'Day 2 after femoral nailing, a young '
                                                'man becomes confused and hypoxic with '
                                                'axillary petechiae. CT PA is negative '
                                                'for large PE. Multiple teams are '
                                                'involved; prioritize life/limb/vision '
                                                'threats and avoid harmful premature '
                                                'therapies.',
                                        'question': 'Consider?',
                                        'answer': 'Fat embolism syndrome — supportive '
                                                  'care and orthopaedic/ICU '
                                                  'collaboration.',
                                        'discussion': 'Classic triad after long-bone '
                                                      'instrumentation.',
                                        'book_hint': "Harrison's Respiratory / "
                                                     'West'}]}},
 'gastroenterology': {'label': 'Gastroenterology',
                      'books': ["Sleisenger and Fordtran's Gastrointestinal and Liver "
                                'Disease',
                                "Harrison's — Gastroenterology",
                                'Bailey & Love — Abdominal surgery chapters'],
                      'pdf_notes': ['Charcot triad = cholangitis; Reynolds pentad adds '
                                    'hypotension + confusion.',
                                    'H. pylori → PUD; test-and-treat in appropriate '
                                    'settings.',
                                    'Pancreatitis: epigastric pain to back + ↑ lipase; '
                                    'fluids and support.',
                                    "Appendicitis: periumbilical→RLQ pain, McBurney's "
                                    'tenderness.',
                                    'Cirrhosis complications: varices, ascites, '
                                    'encephalopathy, HCC surveillance.'],
                      'questions': {'easy': [{'question': 'Charcot’s triad of '
                                                          'right-upper-quadrant pain, '
                                                          'jaundice, and fever most '
                                                          'specifically indicates '
                                                          'which process?',
                                              'options': ['A) Ascending cholangitis '
                                                          'from infected biliary '
                                                          'obstruction',
                                                          'B) Uncomplicated duodenal '
                                                          'ulcer without biliary '
                                                          'involvement',
                                                          'C) Simple hepatic steatosis '
                                                          'on ultrasound alone',
                                                          'D) Irritable bowel syndrome '
                                                          'with normal liver tests'],
                                              'answer': 'A) Ascending cholangitis from '
                                                        'infected biliary obstruction',
                                              'explanation': 'Charcot’s triad reflects '
                                                             'infection proximal to an '
                                                             'obstructed bile duct '
                                                             '(ascending cholangitis). '
                                                             'Ulcer, steatosis, and '
                                                             'IBS lack this '
                                                             'obstructive biliary '
                                                             'sepsis pattern.',
                                              'choice_explanations': {'A': 'Infected '
                                                                           'obstructed '
                                                                           'bile ducts '
                                                                           'produce '
                                                                           'RUQ pain, '
                                                                           'jaundice, '
                                                                           'and '
                                                                           'fever—Charcot’s '
                                                                           'triad.',
                                                                      'B': 'Duodenal '
                                                                           'ulcer '
                                                                           'causes '
                                                                           'epigastric '
                                                                           'pain '
                                                                           'without '
                                                                           'the '
                                                                           'classic '
                                                                           'cholangitis '
                                                                           'triad.',
                                                                      'C': 'Fatty '
                                                                           'liver is '
                                                                           'often '
                                                                           'asymptomatic '
                                                                           'and '
                                                                           'afebrile '
                                                                           'without '
                                                                           'acute '
                                                                           'cholangitis.',
                                                                      'D': 'IBS is a '
                                                                           'functional '
                                                                           'bowel '
                                                                           'disorder '
                                                                           'without '
                                                                           'jaundice '
                                                                           'and fever '
                                                                           'from '
                                                                           'biliary '
                                                                           'sepsis.'}},
                                             {'question': 'Chronic Helicobacter pylori '
                                                          'infection is most clearly '
                                                          'linked to which gastric '
                                                          'pathology?',
                                              'options': ['A) Primary biliary '
                                                          'cholangitis of interlobular '
                                                          'bile ducts',
                                                          'B) Peptic ulcer disease and '
                                                          'increased risk of gastric '
                                                          'adenocarcinoma/MALT '
                                                          'lymphoma',
                                                          'C) Celiac disease triggered '
                                                          'by dietary gluten alone',
                                                          'D) Pancreatic '
                                                          'adenocarcinoma as its sole '
                                                          'disease association'],
                                              'answer': 'B) Peptic ulcer disease and '
                                                        'increased risk of gastric '
                                                        'adenocarcinoma/MALT lymphoma',
                                              'explanation': 'H. pylori drives chronic '
                                                             'gastritis, peptic '
                                                             'ulceration, and raises '
                                                             'risks of gastric '
                                                             'adenocarcinoma and MALT '
                                                             'lymphoma. It is not the '
                                                             'cause of PBC, celiac '
                                                             'disease, or pancreatic '
                                                             'cancer as primary '
                                                             'associations.',
                                              'choice_explanations': {'A': 'PBC is an '
                                                                           'autoimmune '
                                                                           'cholangiopathy, '
                                                                           'not an H. '
                                                                           'pylori '
                                                                           'gastric '
                                                                           'infection '
                                                                           'sequel.',
                                                                      'B': 'H. pylori '
                                                                           'is a major '
                                                                           'cause of '
                                                                           'peptic '
                                                                           'ulcers and '
                                                                           'a gastric '
                                                                           'cancer/MALT '
                                                                           'risk '
                                                                           'factor.',
                                                                      'C': 'Celiac '
                                                                           'disease is '
                                                                           'gluten-driven '
                                                                           'autoimmune '
                                                                           'enteropathy, '
                                                                           'not H. '
                                                                           'pylori.',
                                                                      'D': 'Pancreatic '
                                                                           'cancer is '
                                                                           'not the '
                                                                           'primary H. '
                                                                           'pylori '
                                                                           'disease '
                                                                           'link.'}},
                                             {'question': 'McBurney’s point tenderness '
                                                          'is classically associated '
                                                          'with inflammation of which '
                                                          'organ?',
                                              'options': ['A) Gallbladder fundus at '
                                                          'the midclavicular costal '
                                                          'margin',
                                                          'B) Sigmoid colon in '
                                                          'diverticulitis of the '
                                                          'elderly',
                                                          'C) Appendix in the right '
                                                          'lower quadrant',
                                                          'D) Spleen in '
                                                          'left-upper-quadrant trauma '
                                                          'only'],
                                              'answer': 'C) Appendix in the right '
                                                        'lower quadrant',
                                              'explanation': 'McBurney’s point '
                                                             'overlies the usual '
                                                             'appendiceal location in '
                                                             'the RLQ; tenderness '
                                                             'there supports '
                                                             'appendicitis. '
                                                             'Gallbladder, sigmoid '
                                                             'diverticulitis, and '
                                                             'spleen localize '
                                                             'elsewhere.',
                                              'choice_explanations': {'A': 'Gallbladder '
                                                                           'tenderness '
                                                                           'is '
                                                                           'Murphy’s '
                                                                           'sign in '
                                                                           'the RUQ, '
                                                                           'not '
                                                                           'McBurney’s.',
                                                                      'B': 'Sigmoid '
                                                                           'diverticulitis '
                                                                           'is '
                                                                           'typically '
                                                                           'LLQ.',
                                                                      'C': 'McBurney’s '
                                                                           'point is '
                                                                           'the '
                                                                           'classic '
                                                                           'appendicitis '
                                                                           'landmark.',
                                                                      'D': 'Splenic '
                                                                           'pathology '
                                                                           'is '
                                                                           'LUQ/left '
                                                                           'flank, not '
                                                                           'RLQ '
                                                                           'McBurney’s.'}}],
                                    'medium': [{'question': 'Acute pancreatitis pain '
                                                            'typically radiates in '
                                                            'which pattern?',
                                                'options': ['A) To the right shoulder '
                                                            'tip only from '
                                                            'diaphragmatic irritation '
                                                            'always',
                                                            'B) Down the left arm as '
                                                            'anginal equivalent '
                                                            'exclusively',
                                                            'C) To the groin like '
                                                            'ureteric colic without '
                                                            'back involvement',
                                                            'D) Through to the back as '
                                                            'a boring epigastric pain'],
                                                'answer': 'D) Through to the back as a '
                                                          'boring epigastric pain',
                                                'explanation': 'Pancreatic '
                                                               'inflammation in the '
                                                               'retroperitoneum '
                                                               'produces severe '
                                                               'epigastric pain boring '
                                                               'through to the back, '
                                                               'often relieved '
                                                               'somewhat by leaning '
                                                               'forward. Shoulder-tip, '
                                                               'arm, and groin '
                                                               'radiation patterns '
                                                               'suggest other visceral '
                                                               'sources.',
                                                'choice_explanations': {'A': 'Isolated '
                                                                             'shoulder-tip '
                                                                             'pain '
                                                                             'suggests '
                                                                             'diaphragmatic/biliary '
                                                                             'irritation '
                                                                             'patterns '
                                                                             'more '
                                                                             'than '
                                                                             'classic '
                                                                             'pancreatitis.',
                                                                        'B': 'Left-arm '
                                                                             'radiation '
                                                                             'is '
                                                                             'ischemic '
                                                                             'cardiac '
                                                                             'pain, '
                                                                             'not '
                                                                             'pancreatitis.',
                                                                        'C': 'Groin '
                                                                             'radiation '
                                                                             'suggests '
                                                                             'ureteric '
                                                                             'stone '
                                                                             'colic.',
                                                                        'D': 'Boring '
                                                                             'epigastric-to-back '
                                                                             'pain is '
                                                                             'the '
                                                                             'classic '
                                                                             'pancreatitis '
                                                                             'radiation.'}},
                                               {'question': 'Life-threatening '
                                                            'esophageal variceal '
                                                            'hemorrhage risk is '
                                                            'highest in which setting?',
                                                'options': ['A) Portal hypertension '
                                                            'from cirrhosis with '
                                                            'varices',
                                                            'B) Mild GERD without '
                                                            'portal hypertension',
                                                            'C) Uncomplicated peptic '
                                                            'stricture from reflux '
                                                            'alone',
                                                            'D) Achalasia with failed '
                                                            'LES relaxation only'],
                                                'answer': 'A) Portal hypertension from '
                                                          'cirrhosis with varices',
                                                'explanation': 'Portal hypertension '
                                                               'opens portosystemic '
                                                               'collaterals including '
                                                               'esophageal varices '
                                                               'that can bleed '
                                                               'massively. GERD, '
                                                               'peptic stricture, and '
                                                               'achalasia cause other '
                                                               'esophageal symptoms '
                                                               'without variceal '
                                                               'portal pressure '
                                                               'physiology.',
                                                'choice_explanations': {'A': 'Cirrhotic '
                                                                             'portal '
                                                                             'hypertension '
                                                                             'drives '
                                                                             'varices '
                                                                             'and '
                                                                             'high-risk '
                                                                             'GI '
                                                                             'bleeding.',
                                                                        'B': 'GERD '
                                                                             'does not '
                                                                             'create '
                                                                             'varices '
                                                                             'without '
                                                                             'portal '
                                                                             'hypertension.',
                                                                        'C': 'Peptic '
                                                                             'strictures '
                                                                             'cause '
                                                                             'dysphagia, '
                                                                             'not '
                                                                             'variceal '
                                                                             'hemorrhage.',
                                                                        'D': 'Achalasia '
                                                                             'is a '
                                                                             'motility '
                                                                             'disorder, '
                                                                             'not a '
                                                                             'variceal '
                                                                             'bleeding '
                                                                             'risk '
                                                                             'state.'}},
                                               {'question': 'Which features are alarm '
                                                            'findings that should '
                                                            'prompt urgent evaluation '
                                                            'for serious bowel disease '
                                                            '(including IBD '
                                                            'complications or '
                                                            'malignancy)?',
                                                'options': ['A) Brief stress-related '
                                                            'loose stools that resolve '
                                                            'without weight change',
                                                            'B) Rectal bleeding, '
                                                            'nocturnal diarrhea, '
                                                            'fever, or unintentional '
                                                            'weight loss',
                                                            'C) Occasional mucus '
                                                            'without blood in a '
                                                            'long-stable IBS patient',
                                                            'D) Dietary gas after '
                                                            'legumes without systemic '
                                                            'signs'],
                                                'answer': 'B) Rectal bleeding, '
                                                          'nocturnal diarrhea, fever, '
                                                          'or unintentional weight '
                                                          'loss',
                                                'explanation': 'Alarm '
                                                               'features—bleeding, '
                                                               'nocturnal stools, '
                                                               'fever, weight '
                                                               'loss—suggest '
                                                               'inflammation, '
                                                               'infection, or '
                                                               'neoplasia and warrant '
                                                               'endoscopy/workup. '
                                                               'Functional IBS '
                                                               'symptoms without '
                                                               'alarms are managed '
                                                               'differently.',
                                                'choice_explanations': {'A': 'Transient '
                                                                             'stress '
                                                                             'diarrhea '
                                                                             'without '
                                                                             'alarm '
                                                                             'features '
                                                                             'is '
                                                                             'usually '
                                                                             'benign.',
                                                                        'B': 'Bleeding, '
                                                                             'nocturnal '
                                                                             'diarrhea, '
                                                                             'fever, '
                                                                             'or '
                                                                             'weight '
                                                                             'loss are '
                                                                             'red '
                                                                             'flags '
                                                                             'needing '
                                                                             'investigation.',
                                                                        'C': 'Stable '
                                                                             'mucus '
                                                                             'without '
                                                                             'blood '
                                                                             'can '
                                                                             'occur in '
                                                                             'IBS and '
                                                                             'is not '
                                                                             'by '
                                                                             'itself '
                                                                             'an '
                                                                             'alarm.',
                                                                        'D': 'Dietary '
                                                                             'flatulence '
                                                                             'lacks '
                                                                             'inflammatory '
                                                                             'alarm '
                                                                             'signs.'}}],
                                    'hard': [{'question': 'An elderly patient with '
                                                          'gallstones develops RUQ '
                                                          'pain, jaundice, and fever, '
                                                          'then becomes hypotensive '
                                                          'and confused. Reynolds '
                                                          'pentad adds which findings '
                                                          'to Charcot’s triad in '
                                                          'severe ascending '
                                                          'cholangitis?',
                                              'options': ['A) Asterixis and spider '
                                                          'nevi only from chronic '
                                                          'cirrhosis',
                                                          'B) Migratory arthritis and '
                                                          'erythema nodosum',
                                                          'C) Hypotension and mental '
                                                          'status change indicating '
                                                          'septic shock',
                                                          'D) Palpable purpura from '
                                                          'IgA vasculitis alone'],
                                              'answer': 'C) Hypotension and mental '
                                                        'status change indicating '
                                                        'septic shock',
                                              'explanation': 'Reynolds pentad = '
                                                             'Charcot triad plus '
                                                             'hypotension and '
                                                             'confusion, marking '
                                                             'cholangitis with septic '
                                                             'shock and the need for '
                                                             'urgent biliary drainage '
                                                             'plus antibiotics. '
                                                             'Chronic liver stigmata, '
                                                             'IBD extraintestinal '
                                                             'signs, and vasculitis '
                                                             'are different syndromes.',
                                              'choice_explanations': {'A': 'Asterixis/spiders '
                                                                           'mark '
                                                                           'chronic '
                                                                           'liver '
                                                                           'disease, '
                                                                           'not the '
                                                                           'acute '
                                                                           'pentad of '
                                                                           'cholangitis '
                                                                           'shock.',
                                                                      'B': 'Those are '
                                                                           'extraintestinal '
                                                                           'IBD '
                                                                           'features, '
                                                                           'not '
                                                                           'Reynolds '
                                                                           'pentad.',
                                                                      'C': 'Hypotension '
                                                                           'and '
                                                                           'altered '
                                                                           'mentation '
                                                                           'with '
                                                                           'Charcot '
                                                                           'triad '
                                                                           'define '
                                                                           'Reynolds '
                                                                           'pentad of '
                                                                           'severe '
                                                                           'cholangitis.',
                                                                      'D': 'IgA '
                                                                           'vasculitis '
                                                                           'purpura is '
                                                                           'unrelated '
                                                                           'to biliary '
                                                                           'sepsis '
                                                                           'pentad.'}},
                                             {'question': 'Spontaneous bacterial '
                                                          'peritonitis in a cirrhotic '
                                                          'with ascites is diagnosed '
                                                          'primarily by which ascitic '
                                                          'fluid finding?',
                                              'options': ['A) Positive blood cultures '
                                                          'alone without cell count',
                                                          'B) Serum-ascites albumin '
                                                          'gradient <1.1 exclusively '
                                                          'without cells',
                                                          'C) Triglyceride-rich '
                                                          'chylous fluid as the '
                                                          'defining criterion',
                                                          'D) Ascitic fluid absolute '
                                                          'neutrophil count ≥250/µL '
                                                          '(often with culture)'],
                                              'answer': 'D) Ascitic fluid absolute '
                                                        'neutrophil count ≥250/µL '
                                                        '(often with culture)',
                                              'explanation': 'SBP is infected ascites '
                                                             'without an '
                                                             'intra-abdominal '
                                                             'surgically treatable '
                                                             'source. Diagnosis hinges '
                                                             'on ascitic PMN ≥250/µL; '
                                                             'cultures help but may be '
                                                             'negative. SAAG '
                                                             'classifies portal '
                                                             'hypertension; chylous '
                                                             'fluid is lymphatic.',
                                              'choice_explanations': {'A': 'Blood '
                                                                           'cultures '
                                                                           'may be '
                                                                           'positive '
                                                                           'but SBP '
                                                                           'diagnosis '
                                                                           'centers on '
                                                                           'ascitic '
                                                                           'neutrophil '
                                                                           'count.',
                                                                      'B': 'High SAAG '
                                                                           'indicates '
                                                                           'portal '
                                                                           'hypertension; '
                                                                           'it does '
                                                                           'not '
                                                                           'diagnose '
                                                                           'infection.',
                                                                      'C': 'Chylous '
                                                                           'ascites is '
                                                                           'triglyceride-rich '
                                                                           'lymphatic '
                                                                           'fluid, not '
                                                                           'SBP '
                                                                           'criteria.',
                                                                      'D': 'Ascitic '
                                                                           'ANC '
                                                                           '≥250/µL is '
                                                                           'the '
                                                                           'diagnostic '
                                                                           'threshold '
                                                                           'for SBP.'}},
                                             {'question': 'After forceful vomiting, a '
                                                          'middle-aged man develops '
                                                          'severe chest pain, '
                                                          'subcutaneous emphysema, and '
                                                          'pleural effusion. Boerhaave '
                                                          'syndrome refers to which '
                                                          'esophageal injury?',
                                              'options': ['A) Full-thickness '
                                                          'esophageal rupture, '
                                                          'typically after forceful '
                                                          'vomiting',
                                                          'B) Partial mucosal tear of '
                                                          'Mallory–Weiss without '
                                                          'perforation',
                                                          'C) Candida esophagitis in '
                                                          'an immunocompetent host '
                                                          'always',
                                                          'D) Schatzki ring causing '
                                                          'intermittent solid-food '
                                                          'dysphagia only'],
                                              'answer': 'A) Full-thickness esophageal '
                                                        'rupture, typically after '
                                                        'forceful vomiting',
                                              'explanation': 'Boerhaave is transmural '
                                                             'esophageal perforation '
                                                             'from abrupt rise in '
                                                             'intraluminal pressure '
                                                             '(often vomiting), '
                                                             'causing mediastinitis. '
                                                             'Mallory–Weiss is '
                                                             'mucosal; infection and '
                                                             'rings are different '
                                                             'entities.',
                                              'choice_explanations': {'A': 'Boerhaave '
                                                                           'syndrome '
                                                                           'is '
                                                                           'full-thickness '
                                                                           'esophageal '
                                                                           'rupture '
                                                                           'after '
                                                                           'vomiting/strain.',
                                                                      'B': 'Mallory–Weiss '
                                                                           'tears are '
                                                                           'partial-thickness '
                                                                           'mucosal '
                                                                           'bleeding '
                                                                           'lesions.',
                                                                      'C': 'Candida '
                                                                           'esophagitis '
                                                                           'is '
                                                                           'infectious, '
                                                                           'not a '
                                                                           'pressure '
                                                                           'perforation.',
                                                                      'D': 'Schatzki '
                                                                           'rings are '
                                                                           'benign '
                                                                           'strictures '
                                                                           'causing '
                                                                           'dysphagia, '
                                                                           'not '
                                                                           'rupture.'}}],
                                    'extreme': [{'question': 'An elderly patient with '
                                                             'atrial fibrillation and '
                                                             'sudden severe abdominal '
                                                             'pain out of proportion '
                                                             'to early physical '
                                                             'findings develops lactic '
                                                             'acidosis. CT angiography '
                                                             'is delayed 2 hours. '
                                                             'Which diagnosis and '
                                                             'principle apply?',
                                                 'options': ['A) Gastroenteritis with '
                                                             'reassuring soft abdomen '
                                                             'that never progresses',
                                                             'B) Acute mesenteric '
                                                             'ischemia—prioritize '
                                                             'resuscitation and urgent '
                                                             'vascular/surgical '
                                                             'revascularization '
                                                             'pathways despite '
                                                             'initially subtle exam',
                                                             'C) Uncomplicated peptic '
                                                             'ulcer managed with '
                                                             'outpatient PPI only',
                                                             'D) '
                                                             'Constipation-predominant '
                                                             'IBS as the cause of '
                                                             'rising lactate'],
                                                 'answer': 'B) Acute mesenteric '
                                                           'ischemia—prioritize '
                                                           'resuscitation and urgent '
                                                           'vascular/surgical '
                                                           'revascularization pathways '
                                                           'despite initially subtle '
                                                           'exam',
                                                 'explanation': 'Embolic/thrombotic '
                                                                'mesenteric ischemia '
                                                                'produces pain out of '
                                                                'proportion, then '
                                                                'bowel infarction with '
                                                                'rising lactate. Early '
                                                                'exam can be '
                                                                'deceptively soft. '
                                                                'Time to reperfusion '
                                                                'determines survival; '
                                                                'benign outpatient '
                                                                'diagnoses ignore the '
                                                                'vascular emergency.',
                                                 'choice_explanations': {'A': 'Gastroenteritis '
                                                                              'does '
                                                                              'not '
                                                                              'typically '
                                                                              'cause '
                                                                              'pain-out-of-proportion '
                                                                              'with '
                                                                              'lactic '
                                                                              'acidosis '
                                                                              'in AF.',
                                                                         'B': 'AF plus '
                                                                              'disproportionate '
                                                                              'pain '
                                                                              'and '
                                                                              'lactate '
                                                                              'indicate '
                                                                              'mesenteric '
                                                                              'ischemia '
                                                                              'needing '
                                                                              'urgent '
                                                                              'reperfusion.',
                                                                         'C': 'Outpatient '
                                                                              'PPI '
                                                                              'therapy '
                                                                              'is '
                                                                              'inappropriate '
                                                                              'for '
                                                                              'suspected '
                                                                              'dead '
                                                                              'gut '
                                                                              'physiology.',
                                                                         'D': 'IBS '
                                                                              'does '
                                                                              'not '
                                                                              'elevate '
                                                                              'lactate '
                                                                              'or '
                                                                              'threaten '
                                                                              'bowel '
                                                                              'viability.'}},
                                                {'question': 'A patient with severe '
                                                             'ulcerative colitis '
                                                             'develops fever, marked '
                                                             'abdominal distension, '
                                                             'tachycardia, and a '
                                                             'dilated transverse colon '
                                                             'on radiograph. Which '
                                                             'complication is '
                                                             'occurring?',
                                                 'options': ['A) Simple irritable '
                                                             'bowel flare without '
                                                             'systemic toxicity',
                                                             'B) Uncomplicated '
                                                             'hemorrhoidal bleeding '
                                                             'only',
                                                             'C) Toxic megacolon with '
                                                             'risk of perforation '
                                                             'requiring intensive '
                                                             'medical therapy and '
                                                             'surgical standby',
                                                             'D) Celiac crisis from '
                                                             'gluten exposure as the '
                                                             'first diagnosis'],
                                                 'answer': 'C) Toxic megacolon with '
                                                           'risk of perforation '
                                                           'requiring intensive '
                                                           'medical therapy and '
                                                           'surgical standby',
                                                 'explanation': 'Toxic megacolon is '
                                                                'acute nonobstructive '
                                                                'colonic dilation with '
                                                                'systemic toxicity, a '
                                                                'known UC/C. difficile '
                                                                'complication risking '
                                                                'perforation. It needs '
                                                                'ICU-level care, IV '
                                                                'steroids/antibiotics '
                                                                'as indicated, and '
                                                                'early surgical '
                                                                'consultation—not '
                                                                'reassurance as IBS or '
                                                                'hemorrhoids.',
                                                 'choice_explanations': {'A': 'IBS '
                                                                              'lacks '
                                                                              'fever, '
                                                                              'toxic '
                                                                              'dilation, '
                                                                              'and '
                                                                              'radiographic '
                                                                              'megacolon.',
                                                                         'B': 'Hemorrhoids '
                                                                              'bleed '
                                                                              'without '
                                                                              'colonic '
                                                                              'dilation '
                                                                              'and '
                                                                              'sepsis '
                                                                              'signs.',
                                                                         'C': 'Systemic '
                                                                              'toxicity '
                                                                              'plus '
                                                                              'colonic '
                                                                              'dilation '
                                                                              'defines '
                                                                              'toxic '
                                                                              'megacolon.',
                                                                         'D': 'Celiac '
                                                                              'crisis '
                                                                              'is '
                                                                              'malabsorptive; '
                                                                              'it is '
                                                                              'not the '
                                                                              'UC '
                                                                              'megacolon '
                                                                              'syndrome.'}},
                                                {'question': 'A 32-year-old woman on '
                                                             'oral contraceptives '
                                                             'presents with tender '
                                                             'hepatomegaly, new '
                                                             'ascites, and rising '
                                                             'ALT/AST. Doppler '
                                                             'ultrasound suggests '
                                                             'absent hepatic vein '
                                                             'flow. Budd–Chiari '
                                                             'syndrome involves '
                                                             'thrombosis or '
                                                             'obstruction of which '
                                                             'venous structures?',
                                                 'options': ['A) Portal vein only '
                                                             'without hepatic venous '
                                                             'outflow involvement',
                                                             'B) Inferior mesenteric '
                                                             'vein exclusively in all '
                                                             'cases',
                                                             'C) Splenic vein alone '
                                                             'causing gastric varices '
                                                             'without liver congestion',
                                                             'D) Hepatic veins and/or '
                                                             'suprahepatic IVC '
                                                             'impairing hepatic venous '
                                                             'outflow'],
                                                 'answer': 'D) Hepatic veins and/or '
                                                           'suprahepatic IVC impairing '
                                                           'hepatic venous outflow',
                                                 'explanation': 'Budd–Chiari is '
                                                                'hepatic venous '
                                                                'outflow obstruction '
                                                                '(hepatic veins/IVC), '
                                                                'producing congestive '
                                                                'hepatopathy, ascites, '
                                                                'and liver injury. '
                                                                'Isolated portal, IMV, '
                                                                'or splenic vein '
                                                                'thrombosis are '
                                                                'related but distinct '
                                                                'splanchnic '
                                                                'thromboses.',
                                                 'choice_explanations': {'A': 'Portal '
                                                                              'vein '
                                                                              'thrombosis '
                                                                              'is a '
                                                                              'different '
                                                                              'entity '
                                                                              'from '
                                                                              'hepatic '
                                                                              'venous '
                                                                              'outflow '
                                                                              'block.',
                                                                         'B': 'IMV '
                                                                              'thrombosis '
                                                                              'does '
                                                                              'not '
                                                                              'define '
                                                                              'Budd–Chiari.',
                                                                         'C': 'Isolated '
                                                                              'splenic '
                                                                              'vein '
                                                                              'thrombosis '
                                                                              'causes '
                                                                              'left-sided '
                                                                              'portal '
                                                                              'hypertension, '
                                                                              'not '
                                                                              'classic '
                                                                              'Budd–Chiari.',
                                                                         'D': 'Obstruction '
                                                                              'of '
                                                                              'hepatic '
                                                                              'veins/IVC '
                                                                              'defines '
                                                                              'Budd–Chiari '
                                                                              'syndrome.'}}]},
                      'cases': {'easy': [{'title': 'RUQ Pain + Jaundice + Fever',
                                          'stem': 'A 50-year-old woman has RUQ pain, '
                                                  'fever, and jaundice.',
                                          'question': 'Likely diagnosis?',
                                          'answer': 'Ascending cholangitis.',
                                          'discussion': 'Antibiotics + biliary '
                                                        'drainage.',
                                          'book_hint': "Sleisenger / Harrison's GI"}],
                                'medium': [{'title': 'Alcohol + Epigastric Pain',
                                            'stem': 'A 40-year-old with heavy alcohol '
                                                    'use has severe epigastric pain to '
                                                    'the back and lipase 3× ULN.',
                                            'question': 'Diagnosis?',
                                            'answer': 'Acute pancreatitis.',
                                            'discussion': 'Supportive '
                                                          'fluids/analgesia; find '
                                                          'cause.',
                                            'book_hint': "Sleisenger / Harrison's GI"}],
                                'hard': [{'title': 'Coffee-Ground Emesis + Shock in '
                                                   'Cirrhosis',
                                          'stem': 'A cirrhotic patient vomits blood '
                                                  'and is hypotensive with tense '
                                                  'ascites. Labs and imaging are '
                                                  'pending; you must choose the safest '
                                                  'next clinical concept.',
                                          'question': 'Priorities?',
                                          'answer': 'ABCs/resuscitation, restrict '
                                                    'transfusion targets per protocol, '
                                                    'reverse coagulopathy '
                                                    'thoughtfully, antibiotics, '
                                                    'terlipressin/octreotide pathways, '
                                                    'urgent endoscopy.',
                                          'discussion': 'Variceal bleed until proven '
                                                        'otherwise.',
                                          'book_hint': "Sleisenger / Harrison's GI"}],
                                'extreme': [{'title': 'Pain Out of Proportion',
                                             'stem': 'An elderly patient with AF '
                                                     'develops sudden severe abdominal '
                                                     'pain but a soft abdomen early '
                                                     'on. Lactate rises. Multiple '
                                                     'teams are involved; prioritize '
                                                     'life/limb/vision threats and '
                                                     'avoid harmful premature '
                                                     'therapies.',
                                             'question': 'Fear which diagnosis?',
                                             'answer': 'Acute mesenteric ischemia — '
                                                       'urgent CT angiography and '
                                                       'surgical/interventional '
                                                       'pathway.',
                                             'discussion': 'Early exam can be falsely '
                                                           'reassuring.',
                                             'book_hint': "Sleisenger / Harrison's "
                                                          'GI'}]}},
 'endocrinology': {'label': 'Endocrinology',
                   'books': ['Williams Textbook of Endocrinology',
                             "Harrison's — Endocrinology",
                             "Greenspan's Basic & Clinical Endocrinology"],
                   'pdf_notes': ['DKA: hyperglycemia + ketones + acidosis; fluids, '
                                 'insulin, K+.',
                                 'Hashimoto → hypothyroidism; Graves → '
                                 'hyperthyroidism.',
                                 'Metformin first-line for many T2DM patients if eGFR '
                                 'allows.',
                                 'Hypocalcemia: Chvostek/Trousseau; check Mg and PTH.',
                                 'Adrenal crisis: shock + hyponatremia/hyperkalemia — '
                                 'give steroids/fluids urgently.'],
                   'questions': {'easy': [{'question': 'Diabetic ketoacidosis is '
                                                       'defined by which '
                                                       'laboratory–clinical '
                                                       'constellation?',
                                           'options': ['A) Hyperglycemia, ketosis, and '
                                                       'high anion-gap metabolic '
                                                       'acidosis',
                                                       'B) Isolated hypoglycemia '
                                                       'without ketones or acidosis',
                                                       'C) Euglycemia with respiratory '
                                                       'alkalosis only',
                                                       'D) Hyperosmolar state without '
                                                       'any acidosis or ketones '
                                                       'always'],
                                           'answer': 'A) Hyperglycemia, ketosis, and '
                                                     'high anion-gap metabolic '
                                                     'acidosis',
                                           'explanation': 'DKA results from '
                                                          'absolute/relative insulin '
                                                          'deficiency with '
                                                          'counter-regulatory surge: '
                                                          'lipolysis generates '
                                                          'ketones, producing '
                                                          'anion-gap acidosis with '
                                                          'hyperglycemia. Isolated '
                                                          'hypo, pure respiratory '
                                                          'alkalosis, and pure HHS '
                                                          'without ketosis are '
                                                          'different.',
                                           'choice_explanations': {'A': 'DKA = '
                                                                        'hyperglycemia '
                                                                        '+ '
                                                                        'ketonemia/ketonuria '
                                                                        '+ anion-gap '
                                                                        'metabolic '
                                                                        'acidosis.',
                                                                   'B': 'Hypoglycemia '
                                                                        'is insulin '
                                                                        'excess, the '
                                                                        'opposite of '
                                                                        'DKA '
                                                                        'physiology.',
                                                                   'C': 'Respiratory '
                                                                        'alkalosis is '
                                                                        'not the '
                                                                        'acid–base '
                                                                        'lesion of '
                                                                        'DKA.',
                                                                   'D': 'HHS is marked '
                                                                        'hyperosmolar '
                                                                        'hyperglycemia '
                                                                        'with minimal '
                                                                        'ketosis—distinct '
                                                                        'from DKA.'}},
                                          {'question': 'Unless contraindicated, which '
                                                       'oral agent is generally '
                                                       'first-line pharmacotherapy for '
                                                       'type 2 diabetes?',
                                           'options': ['A) High-dose sliding-scale '
                                                       'insulin as sole initial '
                                                       'outpatient therapy always',
                                                       'B) Metformin, which reduces '
                                                       'hepatic gluconeogenesis and '
                                                       'improves insulin sensitivity',
                                                       'C) Propylthiouracil for '
                                                       'glycemic control',
                                                       'D) Fludrocortisone to raise '
                                                       'blood glucose'],
                                           'answer': 'B) Metformin, which reduces '
                                                     'hepatic gluconeogenesis and '
                                                     'improves insulin sensitivity',
                                           'explanation': 'Metformin decreases hepatic '
                                                          'glucose output and is '
                                                          'guideline first-line for '
                                                          'most T2DM unless '
                                                          'eGFR/contraindications '
                                                          'preclude it. '
                                                          'Sliding-scale–only insulin '
                                                          'is outdated as sole '
                                                          'strategy; PTU is '
                                                          'antithyroid; '
                                                          'fludrocortisone is '
                                                          'mineralocorticoid.',
                                           'choice_explanations': {'A': 'Insulin may '
                                                                        'be needed '
                                                                        'when severe, '
                                                                        'but metformin '
                                                                        'is standard '
                                                                        'first oral '
                                                                        'agent for '
                                                                        'many with '
                                                                        'T2DM.',
                                                                   'B': 'Metformin is '
                                                                        'preferred '
                                                                        'initial '
                                                                        'pharmacotherapy '
                                                                        'for most '
                                                                        'patients with '
                                                                        'type 2 '
                                                                        'diabetes.',
                                                                   'C': 'PTU treats '
                                                                        'hyperthyroidism, '
                                                                        'not '
                                                                        'hyperglycemia.',
                                                                   'D': 'Fludrocortisone '
                                                                        'does not '
                                                                        'treat '
                                                                        'diabetes and '
                                                                        'can worsen '
                                                                        'metabolic '
                                                                        'issues.'}},
                                          {'question': 'Primary hypothyroidism '
                                                       'typically shows which '
                                                       'laboratory pattern?',
                                           'options': ['A) Low TSH with high free T4 '
                                                       'from pituitary failure',
                                                       'B) High free T4 and high T3 '
                                                       'with suppressed TSH '
                                                       '(thyrotoxicosis)',
                                                       'C) Elevated TSH with low free '
                                                       'T4 from thyroid gland failure',
                                                       'D) Normal TSH and free T4 with '
                                                       'isolated high cortisol'],
                                           'answer': 'C) Elevated TSH with low free T4 '
                                                     'from thyroid gland failure',
                                           'explanation': 'Primary thyroid failure '
                                                          'lowers T4, removing '
                                                          'negative feedback so TSH '
                                                          'rises. Low TSH/high T4 is '
                                                          'thyrotoxicosis or secondary '
                                                          'patterns differ; cortisol '
                                                          'is a separate axis.',
                                           'choice_explanations': {'A': 'Low TSH with '
                                                                        'low thyroid '
                                                                        'hormones '
                                                                        'suggests '
                                                                        'central '
                                                                        'hypothyroidism, '
                                                                        'not primary.',
                                                                   'B': 'That pattern '
                                                                        'is '
                                                                        'hyperthyroidism/thyrotoxicosis.',
                                                                   'C': 'High TSH + '
                                                                        'low free T4 '
                                                                        'is the '
                                                                        'classic '
                                                                        'primary '
                                                                        'hypothyroidism '
                                                                        'pattern.',
                                                                   'D': 'Normal '
                                                                        'thyroid tests '
                                                                        'with high '
                                                                        'cortisol '
                                                                        'indicate a '
                                                                        'different '
                                                                        'endocrine '
                                                                        'disorder.'}}],
                                 'medium': [{'question': 'Positive Chvostek and '
                                                         'Trousseau signs most '
                                                         'strongly suggest which '
                                                         'electrolyte disturbance?',
                                             'options': ['A) Severe hyperkalemia with '
                                                         'peaked T waves only',
                                                         'B) Hypernatremia from pure '
                                                         'water loss exclusively',
                                                         'C) Metabolic alkalosis '
                                                         'without calcium change',
                                                         'D) Hypocalcemia with '
                                                         'neuromuscular '
                                                         'hyperexcitability'],
                                             'answer': 'D) Hypocalcemia with '
                                                       'neuromuscular '
                                                       'hyperexcitability',
                                             'explanation': 'Low ionized calcium '
                                                            'increases neuronal '
                                                            'excitability, producing '
                                                            'facial twitching '
                                                            '(Chvostek) and carpal '
                                                            'spasm with cuff inflation '
                                                            '(Trousseau). '
                                                            'Hyperkalemia, '
                                                            'hypernatremia, and '
                                                            'alkalosis alone do not '
                                                            'define these classic '
                                                            'signs (alkalosis can '
                                                            'lower ionized Ca '
                                                            'secondarily).',
                                             'choice_explanations': {'A': 'Hyperkalemia '
                                                                          'affects '
                                                                          'cardiac '
                                                                          'conduction, '
                                                                          'not '
                                                                          'Chvostek/Trousseau '
                                                                          'specifically.',
                                                                     'B': 'Hypernatremia '
                                                                          'causes '
                                                                          'neurologic '
                                                                          'dehydration '
                                                                          'signs, not '
                                                                          'these '
                                                                          'tetany '
                                                                          'signs.',
                                                                     'C': 'Alkalosis '
                                                                          'may reduce '
                                                                          'ionized Ca, '
                                                                          'but the '
                                                                          'signs '
                                                                          'indicate '
                                                                          'hypocalcemic '
                                                                          'excitability, '
                                                                          'not '
                                                                          'alkalosis '
                                                                          'per se.',
                                                                     'D': 'Hypocalcemia '
                                                                          'produces '
                                                                          'Chvostek '
                                                                          'and '
                                                                          'Trousseau '
                                                                          'signs from '
                                                                          'nerve '
                                                                          'hyperexcitability.'}},
                                            {'question': 'Graves disease is an '
                                                         'autoimmune cause of which '
                                                         'thyroid state?',
                                             'options': ['A) Thyrotoxicosis from '
                                                         'TSH-receptor–stimulating '
                                                         'antibodies',
                                                         'B) Primary hypothyroidism '
                                                         'from gland destruction only',
                                                         'C) Euthyroid sick syndrome '
                                                         'in critical illness',
                                                         'D) Iodine deficiency goiter '
                                                         'without receptor antibodies'],
                                             'answer': 'A) Thyrotoxicosis from '
                                                       'TSH-receptor–stimulating '
                                                       'antibodies',
                                             'explanation': 'Graves disease features '
                                                            'stimulating TSH-receptor '
                                                            'antibodies that drive '
                                                            'thyroid hormone '
                                                            'overproduction and often '
                                                            'ophthalmopathy. It is '
                                                            'hyperthyroid, not primary '
                                                            'hypo, euthyroid sick, or '
                                                            'simple iodine deficiency.',
                                             'choice_explanations': {'A': 'TSHR-stimulating '
                                                                          'antibodies '
                                                                          'cause '
                                                                          'Graves '
                                                                          'thyrotoxicosis.',
                                                                     'B': 'Autoimmune '
                                                                          'hypothyroidism '
                                                                          'is '
                                                                          'Hashimoto’s, '
                                                                          'not Graves.',
                                                                     'C': 'Euthyroid '
                                                                          'sick is a '
                                                                          'nonthyroidal '
                                                                          'illness '
                                                                          'pattern, '
                                                                          'not Graves.',
                                                                     'D': 'Iodine '
                                                                          'deficiency '
                                                                          'causes '
                                                                          'goiter/hypothyroid '
                                                                          'risk '
                                                                          'without '
                                                                          'Graves '
                                                                          'antibodies.'}},
                                            {'question': 'Acute adrenal crisis in a '
                                                         'patient with known adrenal '
                                                         'insufficiency requires which '
                                                         'immediate therapy?',
                                             'options': ['A) Withhold steroids until a '
                                                         'full ACTH stimulation test '
                                                         'is completed in shock',
                                                         'B) IV hydrocortisone '
                                                         '(stress-dose '
                                                         'glucocorticoids) plus volume '
                                                         'resuscitation with saline',
                                                         'C) Only fludrocortisone '
                                                         'orally without '
                                                         'glucocorticoid coverage',
                                                         'D) Aggressive insulin '
                                                         'infusion as first-line '
                                                         'therapy'],
                                             'answer': 'B) IV hydrocortisone '
                                                       '(stress-dose glucocorticoids) '
                                                       'plus volume resuscitation with '
                                                       'saline',
                                             'explanation': 'Adrenal crisis is '
                                                            'life-threatening cortisol '
                                                            'deficiency with shock. '
                                                            'Empiric IV hydrocortisone '
                                                            'and saline are given '
                                                            'immediately; delaying for '
                                                            'stim testing in shock is '
                                                            'dangerous. '
                                                            'Mineralocorticoid alone '
                                                            'is insufficient acutely; '
                                                            'insulin worsens '
                                                            'hypoglycemia risk '
                                                            'inappropriately as '
                                                            'primary Rx.',
                                             'choice_explanations': {'A': 'Never delay '
                                                                          'steroids '
                                                                          'for testing '
                                                                          'in unstable '
                                                                          'suspected '
                                                                          'adrenal '
                                                                          'crisis.',
                                                                     'B': 'IV '
                                                                          'hydrocortisone '
                                                                          'and saline '
                                                                          'resuscitation '
                                                                          'are the '
                                                                          'emergency '
                                                                          'treatments.',
                                                                     'C': 'Acute '
                                                                          'crisis '
                                                                          'needs '
                                                                          'glucocorticoid '
                                                                          '(± '
                                                                          'mineralocorticoid '
                                                                          'activity of '
                                                                          'hydrocortisone), '
                                                                          'not '
                                                                          'fludrocortisone '
                                                                          'alone.',
                                                                     'D': 'Insulin is '
                                                                          'not '
                                                                          'treatment '
                                                                          'for adrenal '
                                                                          'crisis and '
                                                                          'may '
                                                                          'harm.'}}],
                                 'hard': [{'question': 'An older adult with type 2 '
                                                       'diabetes is found profoundly '
                                                       'dehydrated with glucose 900 '
                                                       'mg/dL, effective osmolality '
                                                       '330 mOsm/kg, and only trace '
                                                       'ketones. Hyperosmolar '
                                                       'hyperglycemic state (HHS) '
                                                       'differs from DKA primarily by '
                                                       'which feature set?',
                                           'options': ['A) Prominent ketosis and rapid '
                                                       'deep Kussmaul breathing as the '
                                                       'dominant findings',
                                                       'B) Lower glucose levels than '
                                                       'typical DKA always',
                                                       'C) Marked hyperosmolarity and '
                                                       'severe dehydration with '
                                                       'minimal ketoacidosis',
                                                       'D) Exclusive occurrence in '
                                                       'type 1 diabetes with absolute '
                                                       'insulin deficiency only'],
                                           'answer': 'C) Marked hyperosmolarity and '
                                                     'severe dehydration with minimal '
                                                     'ketoacidosis',
                                           'explanation': 'HHS, usually in T2DM, '
                                                          'features extreme '
                                                          'hyperglycemia/hyperosmolarity '
                                                          'and volume depletion with '
                                                          'little ketosis because '
                                                          'residual insulin restrains '
                                                          'lipolysis. DKA has '
                                                          'anion-gap ketoacidosis; HHS '
                                                          'glucoses are typically '
                                                          'higher, not lower.',
                                           'choice_explanations': {'A': 'Ketosis and '
                                                                        'Kussmaul '
                                                                        'breathing '
                                                                        'characterize '
                                                                        'DKA more than '
                                                                        'HHS.',
                                                                   'B': 'HHS typically '
                                                                        'has higher '
                                                                        'glucose than '
                                                                        'DKA.',
                                                                   'C': 'HHS = severe '
                                                                        'hyperosmolar '
                                                                        'dehydration '
                                                                        'with minimal '
                                                                        'ketoacidosis.',
                                                                   'D': 'HHS mainly '
                                                                        'affects type '
                                                                        '2 diabetes '
                                                                        'with residual '
                                                                        'insulin.'}},
                                          {'question': 'In nonthyroidal illness (sick '
                                                       'euthyroid) patterns, which '
                                                       'laboratory change is most '
                                                       'often seen early?',
                                           'options': ['A) Very high free T4 with '
                                                       'suppressed TSH from Graves '
                                                       'disease',
                                                       'B) Isolated TSH elevation with '
                                                       'goiter and anti-TPO antibodies '
                                                       'defining Hashimoto’s',
                                                       'C) Markedly elevated '
                                                       'thyroglobulin from thyroid '
                                                       'cancer staging alone',
                                                       'D) Low T3 (and often '
                                                       'low/normal T4 later) with TSH '
                                                       'that may be low-normal without '
                                                       'primary thyroid disease'],
                                           'answer': 'D) Low T3 (and often low/normal '
                                                     'T4 later) with TSH that may be '
                                                     'low-normal without primary '
                                                     'thyroid disease',
                                           'explanation': 'Critical illness reduces '
                                                          'peripheral T4→T3 conversion '
                                                          'and alters binding/TSH, '
                                                          'producing low T3 without '
                                                          'true hypothyroidism '
                                                          'necessarily. Graves and '
                                                          'Hashimoto patterns are '
                                                          'primary thyroid diseases; '
                                                          'thyroglobulin is a tumor '
                                                          'marker context.',
                                           'choice_explanations': {'A': 'High T4/low '
                                                                        'TSH is '
                                                                        'thyrotoxicosis, '
                                                                        'not sick '
                                                                        'euthyroid.',
                                                                   'B': 'Hashimoto’s '
                                                                        'is primary '
                                                                        'hypothyroidism '
                                                                        'with '
                                                                        'antibodies/goiter.',
                                                                   'C': 'Thyroglobulin '
                                                                        'tracking is '
                                                                        'oncology-related, '
                                                                        'not the '
                                                                        'sick-euthyroid '
                                                                        'definition.',
                                                                   'D': 'Low T3 with '
                                                                        'variable '
                                                                        'TSH/T4 is the '
                                                                        'classic '
                                                                        'nonthyroidal '
                                                                        'illness '
                                                                        'pattern.'}},
                                          {'question': 'A 40-year-old has paroxysmal '
                                                       'pounding headaches, sweating, '
                                                       'and palpitations with blood '
                                                       'pressure spikes to 220/130. '
                                                       'Imaging later shows an adrenal '
                                                       'mass. Pheochromocytoma '
                                                       'classically produces which '
                                                       'episodic symptom cluster?',
                                           'options': ['A) Headache, palpitations, and '
                                                       'diaphoresis with paroxysmal '
                                                       'hypertension from '
                                                       'catecholamine excess',
                                                       'B) Cold intolerance, '
                                                       'bradycardia, and delayed '
                                                       'reflexes from catecholamine '
                                                       'excess',
                                                       'C) Salt craving and '
                                                       'hyperpigmentation from '
                                                       'epinephrine alone',
                                                       'D) Galactorrhea and amenorrhea '
                                                       'from adrenal medulla prolactin '
                                                       'secretion'],
                                           'answer': 'A) Headache, palpitations, and '
                                                     'diaphoresis with paroxysmal '
                                                     'hypertension from catecholamine '
                                                     'excess',
                                           'explanation': 'Catecholamine-secreting '
                                                          'tumors cause episodic '
                                                          'headache, sweating, '
                                                          'tachycardia/palpitations, '
                                                          'and hypertension. '
                                                          'Hypothyroid symptoms, '
                                                          'primary adrenal '
                                                          'insufficiency signs, and '
                                                          'prolactin effects are other '
                                                          'endocrine axes.',
                                           'choice_explanations': {'A': 'The classic '
                                                                        'pheo triad is '
                                                                        'headache, '
                                                                        'palpitations, '
                                                                        'and '
                                                                        'diaphoresis '
                                                                        'with '
                                                                        'hypertension.',
                                                                   'B': 'Those '
                                                                        'findings '
                                                                        'suggest '
                                                                        'hypothyroidism, '
                                                                        'not '
                                                                        'catecholamine '
                                                                        'excess.',
                                                                   'C': 'Salt '
                                                                        'craving/hyperpigmentation '
                                                                        'suggest '
                                                                        'Addison '
                                                                        'disease '
                                                                        '(ACTH/MSH), '
                                                                        'not pheo.',
                                                                   'D': 'Prolactinoma '
                                                                        'causes '
                                                                        'galactorrhea/amenorrhea; '
                                                                        'adrenal '
                                                                        'medulla does '
                                                                        'not secrete '
                                                                        'prolactin.'}}],
                                 'extreme': [{'question': 'An elderly woman with '
                                                          'longstanding untreated '
                                                          'hypothyroidism is found '
                                                          'unresponsive in winter with '
                                                          'temperature 30°C, '
                                                          'bradycardia, hyponatremia, '
                                                          'hypoventilation, and '
                                                          'nonpitting edema. Which '
                                                          'treatment concept is most '
                                                          'appropriate?',
                                              'options': ['A) Rewarming alone without '
                                                          'thyroid hormone or '
                                                          'glucocorticoid '
                                                          'consideration',
                                                          'B) IV thyroid hormone '
                                                          'replacement plus supportive '
                                                          'care, and give stress-dose '
                                                          'glucocorticoids if adrenal '
                                                          'insufficiency is possible',
                                                          'C) High-dose IV '
                                                          'liothyronine only while '
                                                          'withholding any '
                                                          'hydrocortisone always',
                                                          'D) Immediate therapeutic '
                                                          'hypothermia to 28°C as goal '
                                                          'therapy'],
                                              'answer': 'B) IV thyroid hormone '
                                                        'replacement plus supportive '
                                                        'care, and give stress-dose '
                                                        'glucocorticoids if adrenal '
                                                        'insufficiency is possible',
                                              'explanation': 'Myxedema coma is '
                                                             'decompensated '
                                                             'hypothyroidism with '
                                                             'hypothermia and '
                                                             'multiorgan slowing. '
                                                             'Management is ICU '
                                                             'support, IV thyroid '
                                                             'hormone, and empiric '
                                                             'glucocorticoids because '
                                                             'concurrent adrenal '
                                                             'insufficiency can be '
                                                             'unmasked. Isolated '
                                                             'rewarming or further '
                                                             'cooling is '
                                                             'inadequate/harmful; '
                                                             'withholding steroids '
                                                             'risks crisis.',
                                              'choice_explanations': {'A': 'Rewarming '
                                                                           'helps but '
                                                                           'does not '
                                                                           'replace '
                                                                           'deficient '
                                                                           'thyroid '
                                                                           'hormone.',
                                                                      'B': 'IV thyroid '
                                                                           'hormone + '
                                                                           'supportive '
                                                                           'care ± '
                                                                           'empiric '
                                                                           'steroids '
                                                                           'is the '
                                                                           'myxedema '
                                                                           'coma '
                                                                           'approach.',
                                                                      'C': 'Steroids '
                                                                           'should not '
                                                                           'be '
                                                                           'universally '
                                                                           'withheld '
                                                                           'when '
                                                                           'adrenal '
                                                                           'failure '
                                                                           'may '
                                                                           'coexist.',
                                                                      'D': 'Further '
                                                                           'intentional '
                                                                           'hypothermia '
                                                                           'worsens '
                                                                           'the '
                                                                           'pathophysiology.'}},
                                             {'question': 'A patient with known Graves '
                                                          'disease develops fever '
                                                          '39.5°C, delirium, vomiting, '
                                                          'and heart rate 150 after '
                                                          'infection. Free T4 is very '
                                                          'high. Which statement about '
                                                          'thyroid storm is correct?',
                                              'options': ['A) It is diagnosed only by '
                                                          'a single TSH value below '
                                                          'assay without clinical '
                                                          'scoring',
                                                          'B) Propylthiouracil is '
                                                          'contraindicated and iodine '
                                                          'should be given before any '
                                                          'thionamide',
                                                          'C) It is a clinical '
                                                          'diagnosis of '
                                                          'life-threatening '
                                                          'thyrotoxicosis; treatment '
                                                          'includes thionamides, '
                                                          'iodine after blockade, '
                                                          'beta-blockade, steroids, '
                                                          'and supportive care',
                                                          'D) Aspirin in high doses is '
                                                          'preferred because it frees '
                                                          'less thyroid hormone from '
                                                          'binding proteins'],
                                              'answer': 'C) It is a clinical diagnosis '
                                                        'of life-threatening '
                                                        'thyrotoxicosis; treatment '
                                                        'includes thionamides, iodine '
                                                        'after blockade, '
                                                        'beta-blockade, steroids, and '
                                                        'supportive care',
                                              'explanation': 'Thyroid storm is '
                                                             'diagnosed clinically '
                                                             '(Burch–Wartofsky) as '
                                                             'decompensated '
                                                             'thyrotoxicosis. Therapy '
                                                             'blocks synthesis '
                                                             '(thionamides), then '
                                                             'release (iodine after '
                                                             'synthesis blockade), '
                                                             'adrenergic effects '
                                                             '(beta-blockers), '
                                                             'peripheral conversion '
                                                             '(steroids), and treats '
                                                             'triggers. Aspirin can '
                                                             'displace hormone from '
                                                             'TBG and is avoided; '
                                                             'iodine before '
                                                             'thionamides can worsen '
                                                             'hormone release.',
                                              'choice_explanations': {'A': 'Storm is a '
                                                                           'clinical '
                                                                           'severity '
                                                                           'diagnosis, '
                                                                           'not TSH '
                                                                           'alone.',
                                                                      'B': 'Iodine '
                                                                           'should '
                                                                           'follow '
                                                                           'thionamide '
                                                                           'blockade '
                                                                           'to avoid '
                                                                           'providing '
                                                                           'substrate '
                                                                           'for more '
                                                                           'hormone '
                                                                           'synthesis/release.',
                                                                      'C': 'Multimodal '
                                                                           'antithyroid/adrenergic/supportive '
                                                                           'therapy '
                                                                           'based on '
                                                                           'clinical '
                                                                           'storm '
                                                                           'diagnosis '
                                                                           'is '
                                                                           'correct.',
                                                                      'D': 'Salicylates '
                                                                           'can '
                                                                           'increase '
                                                                           'free '
                                                                           'hormone '
                                                                           'fractions '
                                                                           'and are '
                                                                           'avoided; '
                                                                           'use other '
                                                                           'antipyretics.'}},
                                             {'question': 'A thin adult has recurrent '
                                                          'fasting spells with '
                                                          'confusion and diaphoresis '
                                                          'that resolve after orange '
                                                          'juice. Supervised fasting '
                                                          'documents a plasma glucose '
                                                          'of 38 mg/dL during '
                                                          'symptoms. Whipple’s triad '
                                                          'supporting endogenous '
                                                          'hyperinsulinism (e.g., '
                                                          'insulinoma) consists of '
                                                          'which elements?',
                                              'options': ['A) Hyperglycemia symptoms '
                                                          'that resolve with insulin '
                                                          'administration',
                                                          'B) Random hyperglycemia '
                                                          'without relation to '
                                                          'symptoms',
                                                          'C) Postprandial flushing '
                                                          'cured by octreotide without '
                                                          'documented hypoglycemia',
                                                          'D) Symptoms of '
                                                          'hypoglycemia, documented '
                                                          'low plasma glucose, and '
                                                          'relief with glucose '
                                                          'administration'],
                                              'answer': 'D) Symptoms of hypoglycemia, '
                                                        'documented low plasma '
                                                        'glucose, and relief with '
                                                        'glucose administration',
                                              'explanation': 'Whipple’s triad links '
                                                             'neuroglycopenic/autonomic '
                                                             'symptoms to measured '
                                                             'hypoglycemia that remits '
                                                             'with glucose—necessary '
                                                             'before attributing '
                                                             'spells to insulinoma. '
                                                             'Giving insulin, random '
                                                             'hyperglycemia, or '
                                                             'flushing without low '
                                                             'glucose do not fulfill '
                                                             'the triad.',
                                              'choice_explanations': {'A': 'Insulin '
                                                                           'would '
                                                                           'worsen '
                                                                           'hypoglycemia; '
                                                                           'relief is '
                                                                           'with '
                                                                           'glucose, '
                                                                           'not '
                                                                           'insulin.',
                                                                      'B': 'Hyperglycemia '
                                                                           'is the '
                                                                           'opposite '
                                                                           'of the '
                                                                           'hypoglycemic '
                                                                           'triad.',
                                                                      'C': 'Flushing '
                                                                           'without '
                                                                           'documented '
                                                                           'hypoglycemia '
                                                                           'is not '
                                                                           'Whipple’s '
                                                                           'triad.',
                                                                      'D': 'Symptoms + '
                                                                           'low '
                                                                           'glucose + '
                                                                           'relief '
                                                                           'with '
                                                                           'glucose '
                                                                           'define '
                                                                           'Whipple’s '
                                                                           'triad.'}}]},
                   'cases': {'easy': [{'title': 'Polyuria + Kussmaul',
                                       'stem': 'A teen has polyuria, weight loss, '
                                               'Kussmaul breathing, glucose 430, pH '
                                               '7.15, urine ketones+++.',
                                       'question': 'Diagnosis?',
                                       'answer': 'DKA.',
                                       'discussion': 'Fluids, insulin, K+ care.',
                                       'book_hint': 'Williams Endocrinology'}],
                             'medium': [{'title': 'Heat Intolerance + Weight Loss',
                                         'stem': 'A 29-year-old has heat intolerance, '
                                                 'tremor, weight loss, diffuse goiter; '
                                                 'TSH suppressed, free T4 high.',
                                         'question': 'Category?',
                                         'answer': 'Thyrotoxicosis (e.g., Graves).',
                                         'discussion': 'Beta-blocker + antithyroid '
                                                       'strategy after workup.',
                                         'book_hint': 'Williams Endocrinology'}],
                             'hard': [{'title': 'Steroid-Dependent Patient Vomiting',
                                       'stem': 'A patient on chronic prednisone for '
                                               'autoimmune disease has '
                                               'gastroenteritis, hypotension, and '
                                               'hyponatremia. Labs and imaging are '
                                               'pending; you must choose the safest '
                                               'next clinical concept.',
                                       'question': 'What emergency?',
                                       'answer': 'Adrenal crisis risk — give '
                                                 'stress-dose steroids and IV fluids '
                                                 'while investigating.',
                                       'discussion': 'Never stop chronic steroids '
                                                     'abruptly.',
                                       'book_hint': 'Williams Endocrinology'}],
                             'extreme': [{'title': 'Thyroid Storm',
                                          'stem': 'A woman with untreated '
                                                  'hyperthyroidism develops fever, '
                                                  'delirium, tachyarrhythmia, and '
                                                  'vomiting after surgery. Multiple '
                                                  'teams are involved; prioritize '
                                                  'life/limb/vision threats and avoid '
                                                  'harmful premature therapies.',
                                          'question': 'Management concept?',
                                          'answer': 'Thyroid storm: supportive ICU '
                                                    'care, beta-blockade, antithyroid '
                                                    'drugs, iodine after thionamide, '
                                                    'steroids, treat trigger.',
                                          'discussion': 'Delay kills.',
                                          'book_hint': 'Williams Endocrinology'}]}},
 'nephrology': {'label': 'Nephrology',
                'books': ["Brenner & Rector's The Kidney",
                          "Harrison's — Nephrology",
                          'Comprehensive Clinical Nephrology — Feehally'],
                'pdf_notes': ['AKI types: pre-renal, intrinsic (ATN/AIN/GN), '
                              'post-renal.',
                              'Nephritic vs nephrotic: active sediment/HTN vs heavy '
                              'protein/edema.',
                              'Diabetic kidney disease: ACEI/ARB cornerstone with '
                              'glycemic/BP control.',
                              'eGFR guides drug dosing and CKD staging.',
                              'Hyperkalemia emergencies: ECG changes → calcium, shift, '
                              'remove K+.'],
                'questions': {'easy': [{'question': 'Estimated GFR (eGFR) from '
                                                    'creatinine-based equations '
                                                    'primarily approximates which '
                                                    'physiologic function?',
                                        'options': ['A) Glomerular filtration rate as '
                                                    'a marker of kidney filtering '
                                                    'function',
                                                    'B) Renal tubular concentrating '
                                                    'ability alone',
                                                    'C) Bladder detrusor contractility',
                                                    'D) Ureteric peristaltic '
                                                    'frequency'],
                                        'answer': 'A) Glomerular filtration rate as a '
                                                  'marker of kidney filtering function',
                                        'explanation': 'Creatinine generation and '
                                                       'excretion allow estimation of '
                                                       'GFR, reflecting glomerular '
                                                       'filtration. Concentrating '
                                                       'ability, bladder function, and '
                                                       'ureteric motility are separate '
                                                       'physiologic domains.',
                                        'choice_explanations': {'A': 'eGFR estimates '
                                                                     'glomerular '
                                                                     'filtration, the '
                                                                     'key summary of '
                                                                     'filtering '
                                                                     'function.',
                                                                'B': 'Concentrating '
                                                                     'ability is '
                                                                     'assessed by '
                                                                     'urine '
                                                                     'osmolality/specific '
                                                                     'gravity, not '
                                                                     'eGFR.',
                                                                'C': 'Detrusor '
                                                                     'function is '
                                                                     'urodynamic, '
                                                                     'unrelated to '
                                                                     'eGFR.',
                                                                'D': 'Ureteric '
                                                                     'peristalsis is '
                                                                     'not measured by '
                                                                     'creatinine-based '
                                                                     'eGFR.'}},
                                       {'question': 'Nephrotic syndrome is '
                                                    'characterized by heavy '
                                                    'proteinuria plus which additional '
                                                    'features conceptually?',
                                        'options': ['A) Isolated microscopic hematuria '
                                                    'without protein loss',
                                                    'B) Hypoalbuminemia, edema, and '
                                                    'often hyperlipidemia',
                                                    'C) Pyuria and fever as defining '
                                                    'criteria',
                                                    'D) Rapid rise in creatinine from '
                                                    'postrenal obstruction only'],
                                        'answer': 'B) Hypoalbuminemia, edema, and '
                                                  'often hyperlipidemia',
                                        'explanation': 'Nephrotic-range protein loss '
                                                       'depletes albumin, lowers '
                                                       'oncotic pressure (edema), and '
                                                       'triggers hepatic lipoprotein '
                                                       'synthesis (hyperlipidemia). '
                                                       'Hematuria-dominant, '
                                                       'infectious, and purely '
                                                       'obstructive syndromes differ.',
                                        'choice_explanations': {'A': 'Isolated '
                                                                     'hematuria '
                                                                     'suggests '
                                                                     'nephritic or '
                                                                     'other processes, '
                                                                     'not nephrotic '
                                                                     'syndrome.',
                                                                'B': 'Heavy '
                                                                     'proteinuria, '
                                                                     'hypoalbuminemia, '
                                                                     'edema, and '
                                                                     'hyperlipidemia '
                                                                     'define nephrotic '
                                                                     'syndrome.',
                                                                'C': 'Pyuria/fever '
                                                                     'suggest '
                                                                     'infection, not '
                                                                     'nephrotic '
                                                                     'criteria.',
                                                                'D': 'Postrenal AKI is '
                                                                     'obstructive, not '
                                                                     'the nephrotic '
                                                                     'protein-loss '
                                                                     'syndrome.'}},
                                       {'question': 'ACE inhibitors or ARBs are '
                                                    'particularly preferred in '
                                                    'diabetic kidney disease because '
                                                    'they primarily do which of the '
                                                    'following?',
                                        'options': ['A) Increase intraglomerular '
                                                    'pressure to raise GFR short-term '
                                                    'only',
                                                    'B) Block aldosterone receptors '
                                                    'more potently than spironolactone',
                                                    'C) Reduce intraglomerular '
                                                    'hypertension and proteinuria via '
                                                    'efferent arteriolar dilation',
                                                    'D) Dissolve immune complexes '
                                                    'within the glomerular basement '
                                                    'membrane'],
                                        'answer': 'C) Reduce intraglomerular '
                                                  'hypertension and proteinuria via '
                                                  'efferent arteriolar dilation',
                                        'explanation': 'ACEI/ARB lower angiotensin '
                                                       'II–mediated efferent '
                                                       'constriction, reducing '
                                                       'glomerular capillary pressure '
                                                       'and proteinuria—renoprotective '
                                                       'in diabetic and proteinuric '
                                                       'CKD. They do not raise '
                                                       'intraglomerular pressure, are '
                                                       'not primarily '
                                                       'mineralocorticoid antagonists, '
                                                       'and do not dissolve deposits.',
                                        'choice_explanations': {'A': 'ACEI/ARB lower, '
                                                                     'rather than '
                                                                     'raise, '
                                                                     'intraglomerular '
                                                                     'pressure.',
                                                                'B': 'Mineralocorticoid '
                                                                     'antagonists '
                                                                     '(spironolactone/eplerenone) '
                                                                     'block '
                                                                     'aldosterone '
                                                                     'receptors; '
                                                                     'ACEI/ARB act '
                                                                     'upstream.',
                                                                'C': 'Efferent '
                                                                     'dilation reduces '
                                                                     'glomerular '
                                                                     'hypertension and '
                                                                     'protein leak—key '
                                                                     'benefit in DKD.',
                                                                'D': 'Immune-complex '
                                                                     'dissolution is '
                                                                     'not their '
                                                                     'mechanism.'}}],
                              'medium': [{'question': 'Red blood cell casts on '
                                                      'urinalysis most strongly '
                                                      'suggest which localization?',
                                          'options': ['A) Lower urinary tract bleeding '
                                                      'from bladder tumors only',
                                                      'B) Contamination from menstrual '
                                                      'blood exclusively',
                                                      'C) Nephrolithiasis without '
                                                      'glomerular inflammation',
                                                      'D) Glomerulonephritis '
                                                      '(glomerular hematuria)'],
                                          'answer': 'D) Glomerulonephritis (glomerular '
                                                    'hematuria)',
                                          'explanation': 'RBC casts form when RBCs '
                                                         'leak through damaged '
                                                         'glomeruli and become '
                                                         'embedded in Tamm–Horsfall '
                                                         'protein in tubules—marker of '
                                                         'glomerulonephritis. '
                                                         'Lower-tract bleeding, '
                                                         'menses, and stones may cause '
                                                         'RBCs without casts.',
                                          'choice_explanations': {'A': 'Bladder '
                                                                       'bleeding '
                                                                       'yields RBCs '
                                                                       'without RBC '
                                                                       'casts.',
                                                                  'B': 'Menstrual '
                                                                       'contamination '
                                                                       'lacks true '
                                                                       'renal casts.',
                                                                  'C': 'Stones cause '
                                                                       'hematuria '
                                                                       'without '
                                                                       'glomerular '
                                                                       'cast formation '
                                                                       'typically.',
                                                                  'D': 'RBC casts '
                                                                       'indicate '
                                                                       'glomerular '
                                                                       'bleeding/inflammation.'}},
                                         {'question': 'In suspected postrenal AKI, '
                                                      'which bedside check should be '
                                                      'performed early?',
                                          'options': ['A) Bladder scan or assessment '
                                                      'for urinary '
                                                      'retention/obstruction',
                                                      'B) Immediate kidney biopsy '
                                                      'before bladder assessment',
                                                      'C) Start high-dose NSAIDs to '
                                                      'reduce inflammation',
                                                      'D) Fluid restriction '
                                                      'irrespective of volume status'],
                                          'answer': 'A) Bladder scan or assessment for '
                                                    'urinary retention/obstruction',
                                          'explanation': 'Postrenal AKI from '
                                                         'obstruction is reversible if '
                                                         'relieved early. Bladder '
                                                         'scanning/catheterization '
                                                         'quickly identifies '
                                                         'lower-tract obstruction. '
                                                         'Biopsy is not first; NSAIDs '
                                                         'worsen AKI; blind fluid '
                                                         'restriction may harm.',
                                          'choice_explanations': {'A': 'Exclude '
                                                                       'obstruction '
                                                                       'promptly with '
                                                                       'bladder '
                                                                       'scan/catheterization '
                                                                       'in postrenal '
                                                                       'AKI.',
                                                                  'B': 'Biopsy is '
                                                                       'inappropriate '
                                                                       'before ruling '
                                                                       'out '
                                                                       'obstruction.',
                                                                  'C': 'NSAIDs reduce '
                                                                       'GFR and can '
                                                                       'worsen kidney '
                                                                       'injury.',
                                                                  'D': 'Volume '
                                                                       'management '
                                                                       'must be '
                                                                       'individualized; '
                                                                       'obstruction '
                                                                       'relief comes '
                                                                       'first.'}},
                                         {'question': 'Severe hyperkalemia with peaked '
                                                      'T waves on ECG requires which '
                                                      'immediate stabilizing step?',
                                          'options': ['A) Oral sodium polystyrene as '
                                                      'the sole first action without '
                                                      'ECG review',
                                                      'B) IV calcium to stabilize '
                                                      'cardiac membranes while '
                                                      'shifting/removing potassium',
                                                      'C) IV potassium chloride to '
                                                      'correct a presumed deficit',
                                                      'D) Spironolactone loading to '
                                                      'antagonize aldosterone acutely'],
                                          'answer': 'B) IV calcium to stabilize '
                                                    'cardiac membranes while '
                                                    'shifting/removing potassium',
                                          'explanation': 'IV calcium antagonizes '
                                                         'hyperkalemic membrane '
                                                         'effects within minutes, '
                                                         'buying time for '
                                                         'insulin/glucose, '
                                                         'beta-agonists, bicarbonate '
                                                         '(selected cases), and '
                                                         'definitive removal '
                                                         '(dialysis/binders/diuretics). '
                                                         'Giving more K+ or '
                                                         'aldosterone antagonists '
                                                         'worsens hyperkalemia; '
                                                         'binders are slower.',
                                          'choice_explanations': {'A': 'Binders act '
                                                                       'slowly and do '
                                                                       'not '
                                                                       'immediately '
                                                                       'stabilize '
                                                                       'myocardium.',
                                                                  'B': 'IV calcium '
                                                                       'promptly '
                                                                       'protects the '
                                                                       'heart in '
                                                                       'ECG-changing '
                                                                       'hyperkalemia.',
                                                                  'C': 'Additional '
                                                                       'potassium is '
                                                                       'contraindicated.',
                                                                  'D': 'Spironolactone '
                                                                       'raises '
                                                                       'potassium and '
                                                                       'is '
                                                                       'contraindicated '
                                                                       'here.'}}],
                              'hard': [{'question': 'After prolonged intraoperative '
                                                    'hypotension, a patient’s '
                                                    'creatinine rises and the urine '
                                                    'sediment shows muddy brown '
                                                    'granular casts. This pattern most '
                                                    'supports which AKI etiology?',
                                        'options': ['A) Acute interstitial nephritis '
                                                    'from drug hypersensitivity '
                                                    'primarily',
                                                    'B) Minimal-change disease with '
                                                    'nephrotic syndrome',
                                                    'C) Acute tubular necrosis from '
                                                    'ischemic or toxic tubular injury',
                                                    'D) Postrenal obstruction from '
                                                    'bilateral stones only'],
                                        'answer': 'C) Acute tubular necrosis from '
                                                  'ischemic or toxic tubular injury',
                                        'explanation': 'Ischemic/toxic ATN sheds '
                                                       'tubular epithelial debris '
                                                       'forming muddy brown casts. AIN '
                                                       'shows WBCs/WBC '
                                                       'casts/eosinophiluria; MCD is '
                                                       'nephrotic without ATN casts; '
                                                       'obstruction lacks these casts '
                                                       'as the hallmark.',
                                        'choice_explanations': {'A': 'AIN is '
                                                                     'allergic/inflammatory '
                                                                     'with sterile '
                                                                     'pyuria, not '
                                                                     'muddy brown ATN '
                                                                     'casts.',
                                                                'B': 'Minimal change '
                                                                     'causes nephrotic '
                                                                     'syndrome without '
                                                                     'ATN cast '
                                                                     'sediment.',
                                                                'C': 'Muddy brown '
                                                                     'casts after '
                                                                     'ischemia are '
                                                                     'classic for ATN.',
                                                                'D': 'Obstruction is '
                                                                     'diagnosed by '
                                                                     'imaging/hydronephrosis, '
                                                                     'not muddy brown '
                                                                     'casts.'}},
                                       {'question': 'A patient develops fever, rash, '
                                                    'eosinophiluria, and rising '
                                                    'creatinine one week after '
                                                    'starting a new beta-lactam '
                                                    'antibiotic. Acute interstitial '
                                                    'nephritis is most often linked to '
                                                    'which trigger category?',
                                        'options': ['A) Ischemic ATN after cardiogenic '
                                                    'shock exclusively',
                                                    'B) Bilateral ureteric stones '
                                                    'without drugs or infection',
                                                    'C) Minimal proteinuria from '
                                                    'orthostasis in adolescents',
                                                    'D) Drug hypersensitivity (e.g., '
                                                    'beta-lactams, NSAIDs, PPIs) or '
                                                    'infection'],
                                        'answer': 'D) Drug hypersensitivity (e.g., '
                                                  'beta-lactams, NSAIDs, PPIs) or '
                                                  'infection',
                                        'explanation': 'AIN is immune-mediated '
                                                       'tubulointerstitial '
                                                       'inflammation commonly from '
                                                       'drugs or infection, with '
                                                       'fever, rash, eosinophilia, and '
                                                       'WBC casts sometimes. Ischemic '
                                                       'ATN, stones, and orthostatic '
                                                       'proteinuria are different '
                                                       'mechanisms.',
                                        'choice_explanations': {'A': 'Shock causes ATN '
                                                                     'more than '
                                                                     'classic '
                                                                     'drug-induced '
                                                                     'AIN.',
                                                                'B': 'Stones cause '
                                                                     'obstructive AKI, '
                                                                     'not AIN.',
                                                                'C': 'Orthostatic '
                                                                     'proteinuria is '
                                                                     'benign and not '
                                                                     'AIN.',
                                                                'D': 'Drugs and '
                                                                     'infections are '
                                                                     'the leading AIN '
                                                                     'triggers.'}},
                                       {'question': 'Despite insulin–glucose, '
                                                    'bicarbonate consideration, and '
                                                    'binders, a patient with AKI still '
                                                    'has potassium 7.1 mEq/L and '
                                                    'widening QRS. Which scenario is a '
                                                    'classic indication for urgent '
                                                    'dialysis among the listed '
                                                    'options?',
                                        'options': ['A) Refractory hyperkalemia with '
                                                    'ECG changes despite medical '
                                                    'therapy',
                                                    'B) Stable CKD stage 3 with '
                                                    'creatinine 1.6 mg/dL and normal '
                                                    'potassium',
                                                    'C) Isolated microscopic hematuria '
                                                    'with preserved urine output',
                                                    'D) Mild edema responsive to a '
                                                    'single oral diuretic dose'],
                                        'answer': 'A) Refractory hyperkalemia with ECG '
                                                  'changes despite medical therapy',
                                        'explanation': 'AEIOU indications include '
                                                       'refractory Acidosis, '
                                                       'Electrolytes (especially K+), '
                                                       'Intoxications, Overload, and '
                                                       'Uremic symptoms. Refractory '
                                                       'hyperkalemia with ECG changes '
                                                       'needs dialysis if medical '
                                                       'shifts fail. Stable CKD3 and '
                                                       'minor findings do not.',
                                        'choice_explanations': {'A': 'Life-threatening '
                                                                     'refractory '
                                                                     'hyperkalemia is '
                                                                     'a standard '
                                                                     'urgent dialysis '
                                                                     'indication.',
                                                                'B': 'Stable stage 3 '
                                                                     'CKD without '
                                                                     'complications '
                                                                     'does not need '
                                                                     'urgent dialysis.',
                                                                'C': 'Microscopic '
                                                                     'hematuria alone '
                                                                     'is not a '
                                                                     'dialysis '
                                                                     'indication.',
                                                                'D': 'Mild '
                                                                     'diuretic-responsive '
                                                                     'edema is managed '
                                                                     'medically.'}}],
                              'extreme': [{'question': 'After induction chemotherapy '
                                                       'for Burkitt lymphoma, a '
                                                       'patient develops oliguria, '
                                                       'rising creatinine, phosphate '
                                                       '8.5 mg/dL, potassium 6.8 '
                                                       'mEq/L, uric acid 14 mg/dL, and '
                                                       'calcium 6.9 mg/dL. Which '
                                                       'diagnosis and initial '
                                                       'management theme are correct?',
                                           'options': ['A) SIADH from cyclophosphamide '
                                                       'with isolated hyponatremia '
                                                       'only',
                                                       'B) Tumor lysis '
                                                       'syndrome—aggressive IV '
                                                       'hydration, uric acid control '
                                                       '(e.g., rasburicase/allopurinol '
                                                       'as indicated), and treat '
                                                       'electrolyte emergencies; '
                                                       'dialysis if refractory',
                                                       'C) Primary hyperparathyroidism '
                                                       'causing high calcium and low '
                                                       'phosphate',
                                                       'D) Refeeding syndrome as the '
                                                       'first explanation for high '
                                                       'phosphate and uric acid'],
                                           'answer': 'B) Tumor lysis '
                                                     'syndrome—aggressive IV '
                                                     'hydration, uric acid control '
                                                     '(e.g., rasburicase/allopurinol '
                                                     'as indicated), and treat '
                                                     'electrolyte emergencies; '
                                                     'dialysis if refractory',
                                           'explanation': 'Tumor lysis releases '
                                                          'intracellular ions and '
                                                          'nucleic acids: '
                                                          'hyperkalemia, '
                                                          'hyperphosphatemia, '
                                                          'secondary hypocalcemia, '
                                                          'hyperuricemia, and AKI. '
                                                          'Prevention/treatment '
                                                          'centers on hydration and '
                                                          'uric acid control, plus '
                                                          'electrolyte/dialysis '
                                                          'management. The electrolyte '
                                                          'pattern is opposite primary '
                                                          'hyperparathyroidism; SIADH '
                                                          'and refeeding differ.',
                                           'choice_explanations': {'A': 'SIADH causes '
                                                                        'hyponatremia '
                                                                        'without this '
                                                                        'phosphate/urate/K+ '
                                                                        'pattern.',
                                                                   'B': 'High '
                                                                        'K+/PO4/urate '
                                                                        'with low Ca '
                                                                        'after bulky '
                                                                        'tumor therapy '
                                                                        'is TLS '
                                                                        'needing '
                                                                        'hydration and '
                                                                        'urate '
                                                                        'control.',
                                                                   'C': 'Primary '
                                                                        'hyperparathyroidism '
                                                                        'raises '
                                                                        'calcium and '
                                                                        'lowers '
                                                                        'phosphate—the '
                                                                        'reverse '
                                                                        'pattern.',
                                                                   'D': 'Refeeding '
                                                                        'causes '
                                                                        'hypophosphatemia, '
                                                                        'not '
                                                                        'hyperphosphatemia/hyperuricemia '
                                                                        'of TLS.'}},
                                          {'question': 'A cirrhotic patient with tense '
                                                       'ascites develops progressive '
                                                       'oliguric AKI, bland urine '
                                                       'sediment, and no response to '
                                                       'albumin and holding diuretics '
                                                       'after excluding shock, '
                                                       'nephrotoxins, and obstruction. '
                                                       'Which concept fits hepatorenal '
                                                       'syndrome?',
                                           'options': ['A) Intrinsic ATN with muddy '
                                                       'brown casts as the usual '
                                                       'sediment',
                                                       'B) Postrenal obstruction from '
                                                       'tense ascites compressing '
                                                       'ureters as the definition',
                                                       'C) Functional renal '
                                                       'vasoconstriction in advanced '
                                                       'liver disease with splanchnic '
                                                       'vasodilation—often needs '
                                                       'vasoconstrictors/albumin and '
                                                       'evaluation for transplant',
                                                       'D) Acute glomerulonephritis '
                                                       'with active urinary sediment '
                                                       'always'],
                                           'answer': 'C) Functional renal '
                                                     'vasoconstriction in advanced '
                                                     'liver disease with splanchnic '
                                                     'vasodilation—often needs '
                                                     'vasoconstrictors/albumin and '
                                                     'evaluation for transplant',
                                           'explanation': 'Hepatorenal syndrome is '
                                                          'functional AKI from intense '
                                                          'renal vasoconstriction '
                                                          'secondary to splanchnic '
                                                          'vasodilation in cirrhosis; '
                                                          'sediment is typically bland '
                                                          'and kidneys are '
                                                          'structurally normal. ATN '
                                                          'has casts; obstruction '
                                                          'needs imaging proof; GN has '
                                                          'active sediment.',
                                           'choice_explanations': {'A': 'Muddy brown '
                                                                        'casts '
                                                                        'indicate ATN, '
                                                                        'a different '
                                                                        'AKI '
                                                                        'phenotype.',
                                                                   'B': 'Ascites does '
                                                                        'not define '
                                                                        'obstructive '
                                                                        'uropathy as '
                                                                        'HRS.',
                                                                   'C': 'HRS is '
                                                                        'hemodynamic '
                                                                        'renal failure '
                                                                        'in cirrhosis '
                                                                        'managed with '
                                                                        'vasoconstrictors/albumin '
                                                                        'and '
                                                                        'transplant '
                                                                        'pathways.',
                                                                   'D': 'Active '
                                                                        'sediment '
                                                                        'points to '
                                                                        'glomerulonephritis, '
                                                                        'not classic '
                                                                        'HRS.'}},
                                          {'question': 'An elderly patient with eGFR '
                                                       '28 mL/min and heart failure '
                                                       'needs contrast-enhanced CT '
                                                       'angiography. The team wants to '
                                                       'limit contrast-associated AKI. '
                                                       'Which prevention theme is most '
                                                       'evidence-aligned among the '
                                                       'options?',
                                           'options': ['A) Routine high-dose NSAIDs '
                                                       'before contrast to reduce '
                                                       'inflammation',
                                                       'B) Withhold all IV fluids to '
                                                       'avoid volume overload '
                                                       'regardless of risk',
                                                       'C) Give metformin immediately '
                                                       'before contrast in all '
                                                       'diabetics',
                                                       'D) Minimize contrast volume, '
                                                       'hold nephrotoxins when '
                                                       'feasible, and provide '
                                                       'peri-procedural isotonic '
                                                       'volume expansion in at-risk '
                                                       'patients'],
                                           'answer': 'D) Minimize contrast volume, '
                                                     'hold nephrotoxins when feasible, '
                                                     'and provide peri-procedural '
                                                     'isotonic volume expansion in '
                                                     'at-risk patients',
                                           'explanation': 'Contrast nephropathy risk '
                                                          'falls with the lowest '
                                                          'necessary contrast dose, '
                                                          'avoiding concurrent '
                                                          'nephrotoxins, and pre/post '
                                                          'isotonic hydration in '
                                                          'susceptible patients. '
                                                          'NSAIDs and dehydration '
                                                          'increase risk; metformin is '
                                                          'held around contrast in '
                                                          'many protocols because of '
                                                          'lactic acidosis risk if AKI '
                                                          'occurs—not given '
                                                          'prophylactically.',
                                           'choice_explanations': {'A': 'NSAIDs are '
                                                                        'nephrotoxic '
                                                                        'and increase '
                                                                        'AKI risk.',
                                                                   'B': 'Volume '
                                                                        'depletion '
                                                                        'worsens '
                                                                        'contrast '
                                                                        'nephropathy '
                                                                        'risk.',
                                                                   'C': 'Metformin is '
                                                                        'typically '
                                                                        'held, not '
                                                                        'administered, '
                                                                        'around '
                                                                        'contrast '
                                                                        'exposure.',
                                                                   'D': 'Low contrast '
                                                                        'dose, avoid '
                                                                        'nephrotoxins, '
                                                                        'and isotonic '
                                                                        'hydration are '
                                                                        'core '
                                                                        'prevention '
                                                                        'strategies.'}}]},
                'cases': {'easy': [{'title': 'Oliguria after Diarrhea',
                                    'stem': 'Elderly man with gastroenteritis has dry '
                                            'mucosa and creatinine rise that improves '
                                            'with IV fluids.',
                                    'question': 'AKI type?',
                                    'answer': 'Pre-renal AKI.',
                                    'discussion': 'Restore volume; avoid nephrotoxins.',
                                    'book_hint': "Brenner & Rector / Harrison's"}],
                          'medium': [{'title': 'Edema + 4.8 g/day Protein',
                                      'stem': 'A 21-year-old has periorbital edema, '
                                              'albumin 2.1, proteinuria 4.8 g/day.',
                                      'question': 'Syndrome?',
                                      'answer': 'Nephrotic syndrome.',
                                      'discussion': 'Find cause; manage '
                                                    'edema/thrombosis risk.',
                                      'book_hint': "Brenner & Rector / Harrison's"}],
                          'hard': [{'title': 'Pulmonary-Renal Theme',
                                    'stem': 'A young adult has hemoptysis, rising '
                                            'creatinine, and dysmorphic RBCs/RBC '
                                            'casts. Labs and imaging are pending; you '
                                            'must choose the safest next clinical '
                                            'concept.',
                                    'question': 'Concern?',
                                    'answer': 'Pulmonary-renal syndrome (e.g., '
                                              'ANCA/anti-GBM pathways) — urgent '
                                              'specialty labs and therapy.',
                                    'discussion': 'Delay risks irreversible '
                                                  'lung/kidney injury.',
                                    'book_hint': "Brenner & Rector / Harrison's"}],
                          'extreme': [{'title': 'Refractory HyperK after TLS',
                                       'stem': 'A leukemia patient day 1 of chemo has '
                                               'K 7.4, phosphate high, calcium low, '
                                               'uric acid high, and ECG changes. '
                                               'Multiple teams are involved; '
                                               'prioritize life/limb/vision threats '
                                               'and avoid harmful premature therapies.',
                                       'question': 'Diagnosis and action concept?',
                                       'answer': 'Tumor lysis syndrome — ECG '
                                                 'stabilization, shift/remove K, '
                                                 'rasburicase/allopurinol pathways, '
                                                 'ICU/nephrology, possible dialysis.',
                                       'discussion': 'Anticipate TLS in high-burden '
                                                     'tumors.',
                                       'book_hint': "Brenner & Rector / Harrison's"}]}},
 'orthopedics': {'label': 'Orthopedics',
                 'books': ["Apley's System of Orthopaedics and Fractures",
                           "Campbell's Operative Orthopaedics",
                           'Bailey & Love — Orthopaedics chapters'],
                 'pdf_notes': ['Compartment syndrome: pain out of proportion — '
                               'emergency fasciotomy pathway.',
                               'Colles fracture: FOOSH → distal radius dorsal '
                               'angulation.',
                               'Ottawa ankle rules guide X-ray after sprain.',
                               'Hip fracture: shortened externally rotated limb in '
                               'elderly fall.',
                               'Fat embolism after long-bone fracture: hypoxia, neuro, '
                               'petechiae.'],
                 'questions': {'easy': [{'question': 'Ottawa ankle rules are clinical '
                                                     'decision tools that primarily '
                                                     'help decide the need for which '
                                                     'action?',
                                         'options': ['A) Radiographs of the ankle/foot '
                                                     'after acute injury',
                                                     'B) Immediate surgical fixation '
                                                     'without imaging ever',
                                                     'C) Long-term bisphosphonate '
                                                     'therapy initiation',
                                                     'D) Empiric IV antibiotics for '
                                                     'all sprains'],
                                         'answer': 'A) Radiographs of the ankle/foot '
                                                   'after acute injury',
                                         'explanation': 'Ottawa rules use tenderness '
                                                        'and weight-bearing ability to '
                                                        'identify who needs X-rays '
                                                        'after ankle/midfoot injury, '
                                                        'reducing unnecessary imaging. '
                                                        'They do not mandate surgery, '
                                                        'osteoporosis drugs, or '
                                                        'antibiotics.',
                                         'choice_explanations': {'A': 'Ottawa ankle '
                                                                      'rules guide '
                                                                      'when to obtain '
                                                                      'ankle/foot '
                                                                      'radiographs.',
                                                                 'B': 'Rules select '
                                                                      'imaging, not '
                                                                      'automatic '
                                                                      'operative '
                                                                      'fixation.',
                                                                 'C': 'Bisphosphonates '
                                                                      'treat '
                                                                      'osteoporosis, '
                                                                      'unrelated to '
                                                                      'acute Ottawa '
                                                                      'decisions.',
                                                                 'D': 'Antibiotics are '
                                                                      'not indicated '
                                                                      'for '
                                                                      'uncomplicated '
                                                                      'sprains.'}},
                                        {'question': 'A Colles fracture typically '
                                                     'follows which injury mechanism '
                                                     'in older adults?',
                                         'options': ['A) Direct blow to a flexed elbow '
                                                     'only',
                                                     'B) Fall on an outstretched hand '
                                                     'with distal radius dorsal '
                                                     'angulation',
                                                     'C) Twisting injury isolated to '
                                                     'the medial meniscus',
                                                     'D) Axial load through the '
                                                     'calcaneus from a fall onto the '
                                                     'heels'],
                                         'answer': 'B) Fall on an outstretched hand '
                                                   'with distal radius dorsal '
                                                   'angulation',
                                         'explanation': 'FOOSH injuries commonly '
                                                        'fracture the distal radius '
                                                        'with dorsal '
                                                        'displacement/angulation '
                                                        '(Colles). Elbow blows, '
                                                        'meniscal twists, and '
                                                        'calcaneal axial loads produce '
                                                        'other injuries.',
                                         'choice_explanations': {'A': 'Elbow trauma '
                                                                      'causes '
                                                                      'different '
                                                                      'fractures '
                                                                      '(e.g., '
                                                                      'olecranon/radial '
                                                                      'head).',
                                                                 'B': 'Fall on '
                                                                      'outstretched '
                                                                      'hand is the '
                                                                      'classic Colles '
                                                                      'mechanism.',
                                                                 'C': 'Meniscal injury '
                                                                      'is a knee '
                                                                      'soft-tissue '
                                                                      'lesion.',
                                                                 'D': 'Heel-strike '
                                                                      'axial load '
                                                                      'risks calcaneal '
                                                                      'fracture, not '
                                                                      'Colles.'}},
                                        {'question': 'An open fracture with '
                                                     'soft-tissue communication to the '
                                                     'bone requires which early '
                                                     'management priority beyond '
                                                     'immobilization?',
                                         'options': ['A) Delayed antibiotics until '
                                                     'cultures return in 48 hours',
                                                     'B) Immediate casting to a '
                                                     'weight-bearing status without '
                                                     'debridement',
                                                     'C) Urgent antibiotics, tetanus '
                                                     'status, and surgical '
                                                     'irrigation/debridement',
                                                     'D) High-dose NSAIDs alone as '
                                                     'definitive care'],
                                         'answer': 'C) Urgent antibiotics, tetanus '
                                                   'status, and surgical '
                                                   'irrigation/debridement',
                                         'explanation': 'Open fractures are '
                                                        'contaminated; early IV '
                                                        'antibiotics, tetanus '
                                                        'prophylaxis, and operative '
                                                        'debridement reduce infection '
                                                        'and osteomyelitis risk. '
                                                        'Delaying antibiotics or '
                                                        'definitive casting without '
                                                        'washout is harmful.',
                                         'choice_explanations': {'A': 'Antibiotics '
                                                                      'should start '
                                                                      'early, not wait '
                                                                      'for cultures.',
                                                                 'B': 'Weight-bearing '
                                                                      'casting without '
                                                                      'debridement '
                                                                      'ignores '
                                                                      'contamination.',
                                                                 'C': 'Antibiotics, '
                                                                      'tetanus care, '
                                                                      'and surgical '
                                                                      'washout are '
                                                                      'open-fracture '
                                                                      'standards.',
                                                                 'D': 'NSAIDs alone do '
                                                                      'not address '
                                                                      'contamination '
                                                                      'or '
                                                                      'stability.'}}],
                               'medium': [{'question': 'Which early clinical feature '
                                                       'is most concerning for acute '
                                                       'compartment syndrome after '
                                                       'tibial fracture?',
                                           'options': ['A) Isolated mild bruising '
                                                       'without tense swelling or pain',
                                                       'B) Painless chronic deformity '
                                                       'weeks later only',
                                                       'C) Fever and erythematous '
                                                       'tracking as the first and only '
                                                       'signs',
                                                       'D) Pain out of proportion and '
                                                       'pain on passive stretch of the '
                                                       'compartment'],
                                           'answer': 'D) Pain out of proportion and '
                                                     'pain on passive stretch of the '
                                                     'compartment',
                                           'explanation': 'Rising intracompartmental '
                                                          'pressure causes ischemic '
                                                          'muscle pain '
                                                          'disproportionate to injury '
                                                          'and aggravated by passive '
                                                          'stretch—earliest reliable '
                                                          'clinical clues. '
                                                          'Pulselessness is late; mild '
                                                          'bruising alone and delayed '
                                                          'deformity are not acute '
                                                          'compartment signals; fever '
                                                          'suggests infection later.',
                                           'choice_explanations': {'A': 'Mild bruising '
                                                                        'without tense '
                                                                        'pain is '
                                                                        'expected '
                                                                        'soft-tissue '
                                                                        'injury, not '
                                                                        'compartment '
                                                                        'syndrome.',
                                                                   'B': 'Chronic '
                                                                        'deformity is '
                                                                        'a late '
                                                                        'sequela, not '
                                                                        'an acute '
                                                                        'diagnosis '
                                                                        'cue.',
                                                                   'C': 'Fever/erythema '
                                                                        'suggest '
                                                                        'infection '
                                                                        'more than '
                                                                        'acute '
                                                                        'pressure '
                                                                        'ischemia.',
                                                                   'D': 'Disproportionate '
                                                                        'pain and '
                                                                        'passive-stretch '
                                                                        'pain are '
                                                                        'hallmark '
                                                                        'early '
                                                                        'compartment '
                                                                        'syndrome '
                                                                        'findings.'}},
                                          {'question': 'Fat embolism syndrome '
                                                       'classically follows which '
                                                       'orthopedic setting?',
                                           'options': ['A) Long-bone or pelvic '
                                                       'fractures, especially after '
                                                       'instrumentation',
                                                       'B) Isolated fingertip tuft '
                                                       'fracture without marrow '
                                                       'involvement',
                                                       'C) Chronic tennis elbow from '
                                                       'repetitive strain',
                                                       'D) Simple ankle sprain with '
                                                       'ligament stretch only'],
                                           'answer': 'A) Long-bone or pelvic '
                                                     'fractures, especially after '
                                                     'instrumentation',
                                           'explanation': 'Marrow fat embolizes after '
                                                          'major long-bone/pelvic '
                                                          'fractures or orthopedic '
                                                          'procedures, producing '
                                                          'respiratory, neurologic, '
                                                          'and petechial findings. '
                                                          'Minor soft-tissue injuries '
                                                          'lack this marrow '
                                                          'embolization risk.',
                                           'choice_explanations': {'A': 'Long-bone/pelvic '
                                                                        'fractures are '
                                                                        'the classic '
                                                                        'fat embolism '
                                                                        'setting.',
                                                                   'B': 'Tuft '
                                                                        'fractures do '
                                                                        'not typically '
                                                                        'embolize '
                                                                        'marrow fat '
                                                                        'systemically.',
                                                                   'C': 'Lateral '
                                                                        'epicondylitis '
                                                                        'is '
                                                                        'tendinopathy '
                                                                        'without fat '
                                                                        'embolism.',
                                                                   'D': 'Sprains lack '
                                                                        'marrow fat '
                                                                        'embolization '
                                                                        'physiology.'}},
                                          {'question': 'Suspected septic arthritis of '
                                                       'a native knee is managed with '
                                                       'which urgency principle?',
                                           'options': ['A) Oral antibiotics at home '
                                                       'for 2 weeks without joint '
                                                       'aspiration',
                                                       'B) Emergent joint '
                                                       'aspiration/drainage and IV '
                                                       'antibiotics—do not delay for '
                                                       "'trial of NSAIDs'",
                                                       'C) Intra-articular steroid '
                                                       'injection as first therapy',
                                                       'D) Observation until cartilage '
                                                       'is radiographically destroyed'],
                                           'answer': 'B) Emergent joint '
                                                     'aspiration/drainage and IV '
                                                     'antibiotics—do not delay for '
                                                     "'trial of NSAIDs'",
                                           'explanation': 'Septic arthritis destroys '
                                                          'cartilage within days via '
                                                          'enzymes and pressure. '
                                                          'Urgent aspiration '
                                                          '(diagnosis/source control) '
                                                          'and IV antibiotics are '
                                                          'mandatory. Steroids without '
                                                          'infection exclusion worsen '
                                                          'sepsis; waiting for '
                                                          'radiographic ruin is too '
                                                          'late.',
                                           'choice_explanations': {'A': 'Empiric oral '
                                                                        'outpatient '
                                                                        'therapy '
                                                                        'without '
                                                                        'drainage '
                                                                        'risks joint '
                                                                        'destruction.',
                                                                   'B': 'Prompt '
                                                                        'aspiration/washout '
                                                                        'and IV '
                                                                        'antibiotics '
                                                                        'are required.',
                                                                   'C': 'Steroids are '
                                                                        'contraindicated '
                                                                        'until '
                                                                        'infection is '
                                                                        'excluded/treated.',
                                                                   'D': 'Delay until '
                                                                        'radiographic '
                                                                        'destruction '
                                                                        'means '
                                                                        'irreversible '
                                                                        'damage.'}}],
                               'hard': [{'question': 'A 10-year-old falls on an '
                                                     'outstretched wrist and '
                                                     'radiographs show a fracture line '
                                                     'traversing the distal radial '
                                                     'growth plate. Salter–Harris '
                                                     'fractures involve which anatomic '
                                                     'structure in children?',
                                         'options': ['A) Only the metaphysis of adults '
                                                     'after physeal closure',
                                                     'B) The vertebral endplates '
                                                     'exclusively in osteoporosis',
                                                     'C) The growth plate (physis) '
                                                     'with variable '
                                                     'metaphyseal/epiphyseal extension',
                                                     'D) Isolated ligament sprains '
                                                     'without bone or physis '
                                                     'involvement'],
                                         'answer': 'C) The growth plate (physis) with '
                                                   'variable metaphyseal/epiphyseal '
                                                   'extension',
                                         'explanation': 'Salter–Harris classification '
                                                        'describes pediatric fractures '
                                                        'through the physis, important '
                                                        'because growth disturbance '
                                                        'may follow. Adult metaphyseal '
                                                        'fractures after closure, '
                                                        'osteoporotic vertebrae, and '
                                                        'pure sprains are different.',
                                         'choice_explanations': {'A': 'After physeal '
                                                                      'closure, '
                                                                      'Salter–Harris '
                                                                      'typing no '
                                                                      'longer applies.',
                                                                 'B': 'Vertebral '
                                                                      'compression '
                                                                      'fractures are '
                                                                      'not '
                                                                      'Salter–Harris '
                                                                      'injuries.',
                                                                 'C': 'Salter–Harris '
                                                                      'injuries '
                                                                      'involve the '
                                                                      'physis ± '
                                                                      'meta/epiphysis '
                                                                      'in children.',
                                                                 'D': 'Ligament '
                                                                      'sprains spare '
                                                                      'the growth '
                                                                      'plate by '
                                                                      'definition.'}},
                                        {'question': 'A 45-year-old with a large '
                                                     'central disc herniation develops '
                                                     'bilateral leg weakness, perineal '
                                                     'numbness, and new urinary '
                                                     'retention. Which set best '
                                                     'represents cauda equina red '
                                                     'flags needing emergent imaging?',
                                         'options': ['A) Isolated mechanical low back '
                                                     'pain improving with activity',
                                                     'B) Unilateral S1 radicular pain '
                                                     'without sphincter change',
                                                     'C) Mild scoliosis without '
                                                     'neurologic deficit',
                                                     'D) Saddle anesthesia, '
                                                     'bowel/bladder dysfunction, and '
                                                     'bilateral leg symptoms'],
                                         'answer': 'D) Saddle anesthesia, '
                                                   'bowel/bladder dysfunction, and '
                                                   'bilateral leg symptoms',
                                         'explanation': 'Cauda equina compression '
                                                        'causes sacral sensory loss, '
                                                        'sphincter dysfunction, and '
                                                        'often bilateral '
                                                        'deficits—surgical emergency. '
                                                        'Ordinary mechanical pain, '
                                                        'unilateral radiculopathy '
                                                        'without sphincters, and '
                                                        'asymptomatic scoliosis lack '
                                                        'this pattern.',
                                         'choice_explanations': {'A': 'Activity-related '
                                                                      'mechanical pain '
                                                                      'is usually '
                                                                      'benign.',
                                                                 'B': 'Unilateral '
                                                                      'radiculopathy '
                                                                      'without '
                                                                      'saddle/sphincter '
                                                                      'signs is '
                                                                      'typical '
                                                                      'sciatica, not '
                                                                      'cauda equina.',
                                                                 'C': 'Scoliosis '
                                                                      'without '
                                                                      'deficits is not '
                                                                      'cauda equina.',
                                                                 'D': 'Saddle '
                                                                      'anesthesia and '
                                                                      'sphincter '
                                                                      'disturbance are '
                                                                      'classic cauda '
                                                                      'equina red '
                                                                      'flags.'}},
                                        {'question': 'A pathologic fracture through a '
                                                     'previously painful bone lesion '
                                                     'in an older adult most suggests '
                                                     'which underlying process?',
                                         'options': ['A) Underlying bone weakened by '
                                                     'metastasis, myeloma, or other '
                                                     'bone disease',
                                                     'B) Normal bone failing only from '
                                                     'extreme high-energy trauma in a '
                                                     'young athlete',
                                                     'C) Simple soft-tissue contusion '
                                                     'without skeletal involvement',
                                                     'D) Vitamin C deficiency scurvy '
                                                     'as the most common adult cause'],
                                         'answer': 'A) Underlying bone weakened by '
                                                   'metastasis, myeloma, or other bone '
                                                   'disease',
                                         'explanation': 'Pathologic fractures occur '
                                                        'through bone abnormal from '
                                                        'tumor (metastasis/myeloma), '
                                                        'infection, or metabolic '
                                                        'disease, often after minimal '
                                                        'trauma. High-energy fractures '
                                                        'in normal bone and '
                                                        'soft-tissue contusions are '
                                                        'different; scurvy is uncommon '
                                                        'in modern adults.',
                                         'choice_explanations': {'A': 'Metastases/myeloma/metabolic '
                                                                      'bone disease '
                                                                      'weaken bone and '
                                                                      'cause '
                                                                      'pathologic '
                                                                      'fracture.',
                                                                 'B': 'High-energy '
                                                                      'trauma in '
                                                                      'normal bone is '
                                                                      'a traumatic, '
                                                                      'not pathologic, '
                                                                      'fracture.',
                                                                 'C': 'Contusions do '
                                                                      'not fracture '
                                                                      'bone.',
                                                                 'D': 'Scurvy is a '
                                                                      'rare '
                                                                      'contemporary '
                                                                      'adult cause '
                                                                      'compared with '
                                                                      'malignancy.'}}],
                               'extreme': [{'question': 'A 45-year-old with diabetes '
                                                        'has rapidly progressive leg '
                                                        'pain, tense woody swelling, '
                                                        'purple bullae, and crepitus '
                                                        'after a minor puncture wound. '
                                                        'He is hypotensive with rising '
                                                        'lactate. Soft-tissue gas is '
                                                        'seen on imaging. Which '
                                                        'diagnosis and action are '
                                                        'correct?',
                                            'options': ['A) Simple cellulitis '
                                                        'treatable with oral '
                                                        'antibiotics and elevation at '
                                                        'home',
                                                        'B) Necrotizing soft-tissue '
                                                        'infection—immediate surgical '
                                                        'exploration/debridement plus '
                                                        'broad empiric antibiotics and '
                                                        'resuscitation',
                                                        'C) Deep vein thrombosis '
                                                        'managed with anticoagulation '
                                                        'alone',
                                                        'D) Chronic venous stasis '
                                                        'dermatitis without systemic '
                                                        'toxicity'],
                                            'answer': 'B) Necrotizing soft-tissue '
                                                      'infection—immediate surgical '
                                                      'exploration/debridement plus '
                                                      'broad empiric antibiotics and '
                                                      'resuscitation',
                                            'explanation': 'Necrotizing '
                                                           'fasciitis/myonecrosis '
                                                           'presents with pain out of '
                                                           'proportion, rapid spread, '
                                                           'bullae, crepitus/gas, and '
                                                           'sepsis. Survival requires '
                                                           'immediate operative source '
                                                           'control plus '
                                                           'antimicrobials—not '
                                                           'outpatient cellulitis '
                                                           'care, anticoagulation '
                                                           'alone, or chronic '
                                                           'dermatitis treatment.',
                                            'choice_explanations': {'A': 'Oral '
                                                                         'outpatient '
                                                                         'therapy is '
                                                                         'inadequate '
                                                                         'for '
                                                                         'gas-forming '
                                                                         'necrotizing '
                                                                         'infection '
                                                                         'with shock.',
                                                                    'B': 'Woody '
                                                                         'swelling, '
                                                                         'gas, bullae, '
                                                                         'and septic '
                                                                         'shock '
                                                                         'mandate '
                                                                         'emergent '
                                                                         'surgical '
                                                                         'debridement.',
                                                                    'C': 'DVT lacks '
                                                                         'crepitus, '
                                                                         'gas, and '
                                                                         'bullae of '
                                                                         'necrotizing '
                                                                         'infection.',
                                                                    'D': 'Stasis '
                                                                         'dermatitis '
                                                                         'is chronic '
                                                                         'and not '
                                                                         'acutely '
                                                                         'septic with '
                                                                         'soft-tissue '
                                                                         'gas.'}},
                                           {'question': 'A hemodynamically unstable '
                                                        'blunt trauma patient has an '
                                                        'open-book pelvic fracture and '
                                                        'ongoing bleeding. Which '
                                                        'temporizing musculoskeletal '
                                                        'intervention is most '
                                                        'appropriate while arranging '
                                                        'definitive hemorrhage '
                                                        'control?',
                                            'options': ['A) Remove all binders and '
                                                        'log-roll repeatedly to '
                                                        'inspect the sacrum only',
                                                        'B) Immediate weight-bearing '
                                                        'ambulation trial to assess '
                                                        'stability',
                                                        'C) Apply a pelvic binder (or '
                                                        'sheet) to reduce pelvic '
                                                        'volume and help tamponade '
                                                        'venous/cancellous bleeding',
                                                        'D) High-dose thrombolysis to '
                                                        'clear pelvic clot'],
                                            'answer': 'C) Apply a pelvic binder (or '
                                                      'sheet) to reduce pelvic volume '
                                                      'and help tamponade '
                                                      'venous/cancellous bleeding',
                                            'explanation': 'Unstable pelvic fractures '
                                                           'expand the pelvic volume '
                                                           'and allow massive '
                                                           'venous/bone bleeding. '
                                                           'Circumferential binders '
                                                           'reduce volume and assist '
                                                           'tamponade as a bridge to '
                                                           'angioembolization/surgery/packing. '
                                                           'Repeated disruption, '
                                                           'ambulation, and '
                                                           'thrombolysis worsen '
                                                           'hemorrhage.',
                                            'choice_explanations': {'A': 'Repeated '
                                                                         'binder '
                                                                         'removal and '
                                                                         'log-rolling '
                                                                         'can '
                                                                         'aggravate '
                                                                         'bleeding.',
                                                                    'B': 'Ambulation '
                                                                         'is '
                                                                         'contraindicated '
                                                                         'in unstable '
                                                                         'pelvic '
                                                                         'hemorrhage.',
                                                                    'C': 'Pelvic '
                                                                         'binding '
                                                                         'reduces '
                                                                         'volume and '
                                                                         'is a key '
                                                                         'temporizing '
                                                                         'hemorrhage-control '
                                                                         'step.',
                                                                    'D': 'Thrombolysis '
                                                                         'would '
                                                                         'exacerbate '
                                                                         'life-threatening '
                                                                         'bleeding.'}},
                                           {'question': 'After prolonged '
                                                        'immobilization under rubble, '
                                                        'a patient develops dark '
                                                        'urine, CK 85,000 U/L, rising '
                                                        'creatinine, and hyperkalemia. '
                                                        'Which mechanism links muscle '
                                                        'injury to AKI?',
                                            'options': ['A) Isolated prerenal azotemia '
                                                        'from ADH excess without '
                                                        'myoglobin',
                                                        'B) Immune-complex '
                                                        'glomerulonephritis from '
                                                        'streptococcal skin infection '
                                                        'only',
                                                        'C) Postrenal obstruction by '
                                                        'myoglobin casts in the '
                                                        'bladder outlet exclusively',
                                                        'D) Rhabdomyolysis—myoglobin '
                                                        'and other muscle contents '
                                                        'cause tubular toxicity and '
                                                        'obstruction, compounded by '
                                                        'volume depletion and '
                                                        'hyperkalemia risk'],
                                            'answer': 'D) Rhabdomyolysis—myoglobin and '
                                                      'other muscle contents cause '
                                                      'tubular toxicity and '
                                                      'obstruction, compounded by '
                                                      'volume depletion and '
                                                      'hyperkalemia risk',
                                            'explanation': 'Crush injury releases '
                                                           'myoglobin, phosphate, '
                                                           'potassium, and organic '
                                                           'acids. Myoglobin is '
                                                           'nephrotoxic and can '
                                                           'obstruct tubules, '
                                                           'especially with '
                                                           'hypovolemia/acidosis—hence '
                                                           'aggressive IV fluids and '
                                                           'electrolyte management. '
                                                           'Isolated ADH, post-strep '
                                                           'GN, and pure '
                                                           'bladder-outlet block are '
                                                           'incorrect mechanisms here.',
                                            'choice_explanations': {'A': 'Volume '
                                                                         'depletion '
                                                                         'contributes, '
                                                                         'but '
                                                                         'myoglobin-mediated '
                                                                         'ATN is '
                                                                         'central—not '
                                                                         'ADH alone.',
                                                                    'B': 'Post-strep '
                                                                         'GN follows '
                                                                         'infection '
                                                                         'with active '
                                                                         'sediment, '
                                                                         'not crush + '
                                                                         'extreme CK.',
                                                                    'C': 'Myoglobin '
                                                                         'affects '
                                                                         'tubules; it '
                                                                         'is not '
                                                                         'primarily a '
                                                                         'bladder-outlet '
                                                                         'stone '
                                                                         'equivalent.',
                                                                    'D': 'Rhabdomyolysis '
                                                                         'explains '
                                                                         'dark urine, '
                                                                         'massive CK, '
                                                                         'AKI, and '
                                                                         'hyperkalemia '
                                                                         'after '
                                                                         'crush.'}}]},
                 'cases': {'easy': [{'title': 'Elderly Fall + Shortened Leg',
                                     'stem': 'An 83-year-old falls; leg is shortened '
                                             'and externally rotated; cannot bear '
                                             'weight.',
                                     'question': 'Likely injury?',
                                     'answer': 'Hip fracture.',
                                     'discussion': 'X-ray, analgesia, VTE prophylaxis, '
                                                   'early ortho.',
                                     'book_hint': "Apley's Orthopaedics"}],
                           'medium': [{'title': 'Pain After Cast',
                                       'stem': 'A tibial fracture in cast has severe '
                                               'pain on passive toe stretch and a '
                                               'tense leg. Pulses present.',
                                       'question': 'Diagnosis?',
                                       'answer': 'Compartment syndrome — urgent '
                                                 'fasciotomy pathway.',
                                       'discussion': 'Do not wait for pulselessness.',
                                       'book_hint': "Apley's Orthopaedics"}],
                           'hard': [{'title': 'Hot Swollen Knee + Fever',
                                     'stem': 'A 45-year-old cannot bear weight on a '
                                             'hot swollen knee with fever. CRP high. '
                                             'Labs and imaging are pending; you must '
                                             'choose the safest next clinical concept.',
                                     'question': 'Action concept?',
                                     'answer': 'Septic arthritis until proven '
                                               'otherwise — urgent aspiration before '
                                               'antibiotics if possible, then treat.',
                                     'discussion': 'Delay destroys cartilage.',
                                     'book_hint': "Apley's Orthopaedics"}],
                           'extreme': [{'title': 'Crush Injury + Dark Urine',
                                        'stem': 'After an earthquake crush injury, a '
                                                'patient has tense swollen thighs, K '
                                                '6.8, dark urine, and rising '
                                                'creatinine. Multiple teams are '
                                                'involved; prioritize life/limb/vision '
                                                'threats and avoid harmful premature '
                                                'therapies.',
                                        'question': 'Concerns?',
                                        'answer': 'Rhabdomyolysis ± compartment '
                                                  'syndrome — aggressive fluids per '
                                                  'protocol, electrolyte management, '
                                                  'surgical decompression if '
                                                  'compartment syndrome, dialysis if '
                                                  'needed.',
                                        'discussion': 'HyperK can kill before renal '
                                                      'failure does.',
                                        'book_hint': "Apley's Orthopaedics"}]}},
 'dermatology': {'label': 'Dermatology',
                 'books': ["Rook's Textbook of Dermatology",
                           "Fitzpatrick's Dermatology",
                           "Habif's Clinical Dermatology"],
                 'pdf_notes': ['ABCDE for melanoma; urgent specialist referral for '
                               'suspicious lesions.',
                               'Impetigo: honey-colored crusts — contagious.',
                               'Psoriasis: silvery scale, Auspitz, extensor surfaces '
                               'common.',
                               'Scabies: nocturnal itch, finger webs — treat patient + '
                               'contacts.',
                               'Cellulitis vs abscess: antibiotics ± drainage if '
                               'collection.'],
                 'questions': {'easy': [{'question': 'Honey-colored crusts on the face '
                                                     'of a child most classically '
                                                     'suggest which infection?',
                                         'options': ['A) Impetigo, usually from '
                                                     'Staphylococcus aureus or '
                                                     'Streptococcus pyogenes',
                                                     'B) Pemphigus vulgaris with '
                                                     'flaccid bullae in middle-aged '
                                                     'adults only',
                                                     'C) Cutaneous lupus limited to '
                                                     'malar erythema without crusts',
                                                     'D) Tinea corporis with annular '
                                                     'scale as the sole morphology'],
                                         'answer': 'A) Impetigo, usually from '
                                                   'Staphylococcus aureus or '
                                                   'Streptococcus pyogenes',
                                         'explanation': 'Nonbullous impetigo produces '
                                                        'characteristic honey-colored '
                                                        'crusts from superficial '
                                                        'staphylococcal/streptococcal '
                                                        'infection. Pemphigus, lupus, '
                                                        'and tinea have different '
                                                        'primary lesions and '
                                                        'demographics.',
                                         'choice_explanations': {'A': 'Honey-colored '
                                                                      'crusts are the '
                                                                      'classic sign of '
                                                                      'impetigo.',
                                                                 'B': 'Pemphigus '
                                                                      'causes flaccid '
                                                                      'bullae/erosions '
                                                                      'in adults, not '
                                                                      'pediatric honey '
                                                                      'crusts.',
                                                                 'C': 'Lupus malar '
                                                                      'rash is '
                                                                      'erythematous '
                                                                      'without '
                                                                      'impetigo '
                                                                      'crusting as the '
                                                                      'hallmark.',
                                                                 'D': 'Tinea shows '
                                                                      'annular scaly '
                                                                      'plaques, not '
                                                                      'honey crusts.'}},
                                        {'question': 'The ABCDE criteria are used '
                                                     'clinically to screen pigmented '
                                                     'lesions for which concern?',
                                         'options': ['A) Psoriasis plaque thickness '
                                                     'only',
                                                     'B) Melanoma warning features '
                                                     '(Asymmetry, Border, Color, '
                                                     'Diameter, Evolving)',
                                                     'C) Scabies burrow counting on '
                                                     'hands',
                                                     'D) Acne comedone grading on the '
                                                     'forehead'],
                                         'answer': 'B) Melanoma warning features '
                                                   '(Asymmetry, Border, Color, '
                                                   'Diameter, Evolving)',
                                         'explanation': 'ABCDE highlights morphologic '
                                                        'clues that raise melanoma '
                                                        'suspicion and prompt biopsy. '
                                                        'It is not a psoriasis, '
                                                        'scabies, or acne severity '
                                                        'scale.',
                                         'choice_explanations': {'A': 'Psoriasis is '
                                                                      'judged by '
                                                                      'plaque '
                                                                      'extent/severity '
                                                                      'scores, not '
                                                                      'ABCDE.',
                                                                 'B': 'ABCDE screens '
                                                                      'moles for '
                                                                      'possible '
                                                                      'melanoma.',
                                                                 'C': 'Scabies '
                                                                      'diagnosis uses '
                                                                      'burrows/itch '
                                                                      'distribution, '
                                                                      'not ABCDE.',
                                                                 'D': 'Acne grading '
                                                                      'uses '
                                                                      'comedones/inflammatory '
                                                                      'lesions, not '
                                                                      'ABCDE.'}},
                                        {'question': 'Auspitz sign (pinpoint bleeding '
                                                     'when scale is removed) is '
                                                     'classically associated with '
                                                     'which disease?',
                                         'options': ['A) Atopic dermatitis without '
                                                     'plaques',
                                                     'B) Vitiligo depigmented macules',
                                                     'C) Psoriasis vulgaris with '
                                                     'silvery scale over plaques',
                                                     'D) Urticaria with transient '
                                                     'wheals'],
                                         'answer': 'C) Psoriasis vulgaris with silvery '
                                                   'scale over plaques',
                                         'explanation': 'In psoriasis, removing scale '
                                                        'exposes dilated dermal '
                                                        'capillaries that bleed as '
                                                        'pinpoint dots (Auspitz). '
                                                        'Atopic dermatitis, vitiligo, '
                                                        'and urticaria lack this sign.',
                                         'choice_explanations': {'A': 'Atopic '
                                                                      'dermatitis is '
                                                                      'eczematous '
                                                                      'without classic '
                                                                      'Auspitz sign.',
                                                                 'B': 'Vitiligo is '
                                                                      'pigment loss '
                                                                      'without '
                                                                      'scale-removal '
                                                                      'bleeding.',
                                                                 'C': 'Auspitz sign is '
                                                                      'a traditional '
                                                                      'psoriasis '
                                                                      'finding.',
                                                                 'D': 'Urticarial '
                                                                      'wheals are '
                                                                      'transient and '
                                                                      'non-scaly.'}}],
                               'medium': [{'question': 'Scabies pruritus is '
                                                       'characteristically worst at '
                                                       'which time?',
                                           'options': ['A) Only during vigorous '
                                                       'exercise in cold air',
                                                       'B) Exclusively after sun '
                                                       'exposure on the face',
                                                       'C) Never at night by '
                                                       'definition',
                                                       'D) At night, with burrows in '
                                                       'finger webs and genital skin '
                                                       'often involved'],
                                           'answer': 'D) At night, with burrows in '
                                                     'finger webs and genital skin '
                                                     'often involved',
                                           'explanation': 'Sarcoptes infestation '
                                                          'produces intense nocturnal '
                                                          'itch and burrows in web '
                                                          'spaces, wrists, and '
                                                          'genitals. Exercise-cold, '
                                                          "facial sun-only, and 'never "
                                                          "nocturnal' patterns do not "
                                                          'fit.',
                                           'choice_explanations': {'A': 'Exercise-triggered '
                                                                        'itch suggests '
                                                                        'cholinergic '
                                                                        'urticaria '
                                                                        'more than '
                                                                        'scabies.',
                                                                   'B': 'Facial '
                                                                        'photosensitivity '
                                                                        'suggests '
                                                                        'other '
                                                                        'photodermatoses; '
                                                                        'scabies '
                                                                        'spares the '
                                                                        'face in '
                                                                        'adults '
                                                                        'usually.',
                                                                   'C': 'Scabies itch '
                                                                        'is famously '
                                                                        'worse at '
                                                                        'night.',
                                                                   'D': 'Nocturnal '
                                                                        'pruritus with '
                                                                        'classic '
                                                                        'burrow sites '
                                                                        'is typical '
                                                                        'scabies.'}},
                                          {'question': 'Bacterial cellulitis of the '
                                                       'leg typically features which '
                                                       'clinical pattern?',
                                           'options': ['A) Expanding erythematous, '
                                                       'warm, tender plaque often with '
                                                       'fever',
                                                       'B) Annular scaly edge without '
                                                       'warmth suggesting tinea only',
                                                       'C) Noninflammatory palpable '
                                                       'purpura of vasculitis alone',
                                                       'D) Flaccid bullae with mucosal '
                                                       'erosions of pemphigus only'],
                                           'answer': 'A) Expanding erythematous, warm, '
                                                     'tender plaque often with fever',
                                           'explanation': 'Cellulitis is '
                                                          'dermal/subcutaneous '
                                                          'bacterial infection causing '
                                                          'spreading erythema, warmth, '
                                                          'tenderness, and systemic '
                                                          'signs. Tinea is scaly and '
                                                          'less inflammatory; '
                                                          'vasculitis is purpuric; '
                                                          'pemphigus is autoimmune '
                                                          'blistering.',
                                           'choice_explanations': {'A': 'Warm tender '
                                                                        'spreading '
                                                                        'erythema ± '
                                                                        'fever defines '
                                                                        'typical '
                                                                        'cellulitis.',
                                                                   'B': 'Annular scale '
                                                                        'without acute '
                                                                        'inflammation '
                                                                        'suggests '
                                                                        'dermatophyte '
                                                                        'infection.',
                                                                   'C': 'Palpable '
                                                                        'purpura '
                                                                        'indicates '
                                                                        'vasculitis, '
                                                                        'not ordinary '
                                                                        'cellulitis.',
                                                                   'D': 'Pemphigus is '
                                                                        'autoimmune '
                                                                        'acantholysis, '
                                                                        'not bacterial '
                                                                        'cellulitis.'}},
                                          {'question': 'Stevens–Johnson syndrome and '
                                                       'toxic epidermal necrolysis are '
                                                       'best conceptualized as which '
                                                       'process?',
                                           'options': ['A) Mild viral exanthem without '
                                                       'mucosal disease',
                                                       'B) Severe mucocutaneous '
                                                       'adverse drug reactions with '
                                                       'epidermal necrosis',
                                                       'C) Simple contact dermatitis '
                                                       'limited to one finger',
                                                       'D) Bacterial folliculitis of '
                                                       'the beard only'],
                                           'answer': 'B) Severe mucocutaneous adverse '
                                                     'drug reactions with epidermal '
                                                     'necrosis',
                                           'explanation': 'SJS/TEN are spectrum '
                                                          'disorders of widespread '
                                                          'keratinocyte necrosis, '
                                                          'usually drug-induced, with '
                                                          'mucosal involvement and '
                                                          'potential multi-organ '
                                                          'failure. Mild exanthems, '
                                                          'localized contact '
                                                          'dermatitis, and '
                                                          'folliculitis are different.',
                                           'choice_explanations': {'A': 'Mild viral '
                                                                        'rashes lack '
                                                                        'extensive '
                                                                        'epidermal '
                                                                        'necrosis and '
                                                                        'severe '
                                                                        'mucositis.',
                                                                   'B': 'SJS/TEN are '
                                                                        'life-threatening '
                                                                        'drug-related '
                                                                        'epidermal '
                                                                        'necrolysis '
                                                                        'syndromes.',
                                                                   'C': 'Contact '
                                                                        'dermatitis is '
                                                                        'localized '
                                                                        'type IV '
                                                                        'reaction, not '
                                                                        'TEN.',
                                                                   'D': 'Folliculitis '
                                                                        'is follicular '
                                                                        'bacterial '
                                                                        'infection, '
                                                                        'not '
                                                                        'necrolysis.'}}],
                               'hard': [{'question': 'A positive Nikolsky sign '
                                                     '(sheet-like epidermal detachment '
                                                     'with gentle pressure) can be '
                                                     'seen in which condition among '
                                                     'the options?',
                                         'options': ['A) Chronic plaque psoriasis with '
                                                     'adherent scale only',
                                                     'B) Vitiligo without blistering',
                                                     'C) Pemphigus vulgaris (and '
                                                     'similarly in '
                                                     'SJS/TEN/staphylococcal scalded '
                                                     'skin in related contexts)',
                                                     'D) Uncomplicated acne comedones'],
                                         'answer': 'C) Pemphigus vulgaris (and '
                                                   'similarly in '
                                                   'SJS/TEN/staphylococcal scalded '
                                                   'skin in related contexts)',
                                         'explanation': 'Nikolsky positivity reflects '
                                                        'loss of keratinocyte cohesion '
                                                        '(acantholysis or extensive '
                                                        'necrosis), as in pemphigus '
                                                        'and necrolysis syndromes. '
                                                        'Psoriasis, vitiligo, and acne '
                                                        'do not produce this sign.',
                                         'choice_explanations': {'A': 'Psoriatic scale '
                                                                      'does not shear '
                                                                      'as '
                                                                      'Nikolsky-positive '
                                                                      'epidermis.',
                                                                 'B': 'Vitiligo lacks '
                                                                      'epidermal '
                                                                      'detachment.',
                                                                 'C': 'Pemphigus '
                                                                      '(acantholysis) '
                                                                      'classically '
                                                                      'shows Nikolsky '
                                                                      'sign; '
                                                                      'necrolysis can '
                                                                      'as well.',
                                                                 'D': 'Comedonal acne '
                                                                      'has no '
                                                                      'sheet-like '
                                                                      'epidermal '
                                                                      'shear.'}},
                                        {'question': 'An expanding erythematous patch '
                                                     'with central clearing after a '
                                                     'tick exposure in an endemic area '
                                                     'most suggests which diagnosis?',
                                         'options': ['A) Fixed drug eruption recurring '
                                                     'at the identical site only after '
                                                     'the same drug',
                                                     'B) Tinea versicolor limited to '
                                                     'seborrheic yeast overgrowth on '
                                                     'the trunk',
                                                     'C) Erysipelas from abrupt '
                                                     'streptococcal dermal infection '
                                                     'without tick link',
                                                     'D) Erythema migrans of early '
                                                     'Lyme disease (Borrelia '
                                                     'burgdorferi)'],
                                         'answer': 'D) Erythema migrans of early Lyme '
                                                   'disease (Borrelia burgdorferi)',
                                         'explanation': 'Erythema migrans is the early '
                                                        'localized Lyme rash: '
                                                        'expanding annular erythema at '
                                                        'the tick bite site. Fixed '
                                                        'drug eruption, tinea '
                                                        'versicolor, and erysipelas '
                                                        'have different triggers and '
                                                        'morphology/tempo.',
                                         'choice_explanations': {'A': 'Fixed drug '
                                                                      'eruption is '
                                                                      'round/oval and '
                                                                      'drug-timed, not '
                                                                      'tick-associated '
                                                                      'expanding EM.',
                                                                 'B': 'Tinea '
                                                                      'versicolor '
                                                                      'causes '
                                                                      'hypo/hyperpigmented '
                                                                      'macules with '
                                                                      'fine scale, not '
                                                                      'EM.',
                                                                 'C': 'Erysipelas is '
                                                                      'acute febrile '
                                                                      'facial/leg '
                                                                      'infection '
                                                                      'without the '
                                                                      'Lyme expanding '
                                                                      'target history.',
                                                                 'D': 'Expanding '
                                                                      'erythema after '
                                                                      'tick bite is '
                                                                      'erythema '
                                                                      'migrans of Lyme '
                                                                      'disease.'}},
                                        {'question': 'Which bedside clue most helps '
                                                     'distinguish necrotizing '
                                                     'soft-tissue infection from '
                                                     'routine cellulitis?',
                                         'options': ['A) Pain out of proportion, rapid '
                                                     'progression, and systemic '
                                                     'toxicity ± crepitus',
                                                     'B) Mild itch without tenderness '
                                                     'or fever',
                                                     'C) Chronic bilateral venous '
                                                     'stasis changes over years',
                                                     'D) Annular scale that improves '
                                                     'with topical antifungal alone '
                                                     'always'],
                                         'answer': 'A) Pain out of proportion, rapid '
                                                   'progression, and systemic toxicity '
                                                   '± crepitus',
                                         'explanation': 'Necrotizing infections '
                                                        'declare themselves with '
                                                        'disproportionate pain, swift '
                                                        'advance, shock, and sometimes '
                                                        'crepitus/bullae—far beyond '
                                                        'typical cellulitis. Mild '
                                                        'itch, chronic stasis, and '
                                                        'fungal annular scale point '
                                                        'elsewhere.',
                                         'choice_explanations': {'A': 'Out-of-proportion '
                                                                      'pain, rapid '
                                                                      'spread, and '
                                                                      'toxicity '
                                                                      'distinguish '
                                                                      'necrotizing '
                                                                      'infection.',
                                                                 'B': 'Mild itch '
                                                                      'without '
                                                                      'inflammatory '
                                                                      'signs is not '
                                                                      'necrotizing '
                                                                      'disease.',
                                                                 'C': 'Chronic stasis '
                                                                      'dermatitis is '
                                                                      'indolent and '
                                                                      'bilateral.',
                                                                 'D': 'Fungal '
                                                                      'infections '
                                                                      'respond to '
                                                                      'antifungals and '
                                                                      'lack deep '
                                                                      'necrosis '
                                                                      'signs.'}}],
                               'extreme': [{'question': 'A previously healthy toddler '
                                                        'develops fever, purpuric '
                                                        'retiform lesions that '
                                                        'progress within hours to '
                                                        'cutaneous necrosis, and '
                                                        'hypotension. Blood cultures '
                                                        'grow Neisseria meningitidis. '
                                                        'Which dermatologic syndrome '
                                                        'association is illustrated?',
                                            'options': ['A) Chronic plaque psoriasis '
                                                        'flared by infection',
                                                        'B) Purpura fulminans from '
                                                        'septicemia-associated '
                                                        'disseminated intravascular '
                                                        'coagulation',
                                                        'C) Simple viral roseola '
                                                        'without coagulopathy',
                                                        'D) Atopic dermatitis with '
                                                        'secondary Staphylococcus '
                                                        'only'],
                                            'answer': 'B) Purpura fulminans from '
                                                      'septicemia-associated '
                                                      'disseminated intravascular '
                                                      'coagulation',
                                            'explanation': 'Purpura fulminans is acute '
                                                           'thrombotic/ consumptive '
                                                           'coagulopathy of skin '
                                                           'vessels, classically with '
                                                           'meningococcemia, producing '
                                                           'retiform purpura and '
                                                           'necrosis with shock. '
                                                           'Psoriasis, roseola, and '
                                                           'atopic dermatitis lack '
                                                           'this fulminant DIC '
                                                           'cutaneous pattern.',
                                            'choice_explanations': {'A': 'Psoriasis '
                                                                         'does not '
                                                                         'produce '
                                                                         'retiform '
                                                                         'necrotic '
                                                                         'purpura with '
                                                                         'septic '
                                                                         'shock.',
                                                                    'B': 'Meningococcal '
                                                                         'sepsis with '
                                                                         'retiform '
                                                                         'purpura/necrosis '
                                                                         'is purpura '
                                                                         'fulminans '
                                                                         'from DIC.',
                                                                    'C': 'Roseola is a '
                                                                         'transient '
                                                                         'viral '
                                                                         'exanthem '
                                                                         'without DIC '
                                                                         'necrosis.',
                                                                    'D': 'Atopic '
                                                                         'dermatitis '
                                                                         'with '
                                                                         'impetiginization '
                                                                         'is '
                                                                         'superficial, '
                                                                         'not purpura '
                                                                         'fulminans.'}},
                                           {'question': 'A dialysis patient with '
                                                        'secondary hyperparathyroidism '
                                                        'develops exquisitely painful '
                                                        'retiform purpura and necrotic '
                                                        'plaques on the thighs and '
                                                        'abdomen. Biopsy shows '
                                                        'vascular calcification. Which '
                                                        'diagnosis fits?',
                                            'options': ['A) Leukocytoclastic '
                                                        'vasculitis from drug '
                                                        'hypersensitivity as the first '
                                                        'choice always',
                                                        'B) Cholesterol emboli after '
                                                        'catheterization in every case',
                                                        'C) Calciphylaxis (calcific '
                                                        'uremic arteriolopathy) in '
                                                        'end-stage kidney disease',
                                                        'D) Livedo reticularis from '
                                                        'cold exposure without vessel '
                                                        'calcification'],
                                            'answer': 'C) Calciphylaxis (calcific '
                                                      'uremic arteriolopathy) in '
                                                      'end-stage kidney disease',
                                            'explanation': 'Calciphylaxis causes '
                                                           'arteriolar calcification '
                                                           'and thrombosis in ESRD '
                                                           '(often with disordered '
                                                           'calcium–phosphate/PTH), '
                                                           'yielding painful ischemic '
                                                           'necrosis. Ordinary LCV, '
                                                           'cholesterol emboli, and '
                                                           'benign cold livedo have '
                                                           'different '
                                                           'contexts/histology.',
                                            'choice_explanations': {'A': 'LCV is '
                                                                         'neutrophilic '
                                                                         'vessel '
                                                                         'inflammation; '
                                                                         'calcification '
                                                                         'on biopsy '
                                                                         'points to '
                                                                         'calciphylaxis.',
                                                                    'B': 'Cholesterol '
                                                                         'emboli '
                                                                         'follow '
                                                                         'instrumentation '
                                                                         'and show '
                                                                         'cholesterol '
                                                                         'clefts, not '
                                                                         'primary '
                                                                         'calciphylaxis.',
                                                                    'C': 'Painful '
                                                                         'necrotic '
                                                                         'plaques with '
                                                                         'vascular '
                                                                         'calcification '
                                                                         'in dialysis '
                                                                         'patients '
                                                                         'define '
                                                                         'calciphylaxis.',
                                                                    'D': 'Physiologic '
                                                                         'livedo lacks '
                                                                         'necrotic '
                                                                         'plaques and '
                                                                         'vascular '
                                                                         'calcification '
                                                                         'of '
                                                                         'calciphylaxis.'}},
                                           {'question': 'A previously healthy '
                                                        'adolescent develops high '
                                                        'fever, diffuse erythroderma '
                                                        'like sunburn, vomiting, '
                                                        'myalgias, and hypotension '
                                                        'with rising creatinine during '
                                                        'menstruation while using '
                                                        'superabsorbent tampons. Toxic '
                                                        'shock syndrome should be '
                                                        'considered when this picture '
                                                        'accompanies which classic '
                                                        'associations?',
                                            'options': ['A) Solely mosquito bites '
                                                        'without bacterial toxin',
                                                        'B) Only chronic plaque '
                                                        'psoriasis treated with '
                                                        'topical steroids',
                                                        'C) Isolated tinea pedis '
                                                        'without systemic signs',
                                                        'D) Tampon use or '
                                                        'staphylococcal/streptococcal '
                                                        'toxin-producing infections '
                                                        '(including postoperative '
                                                        'wounds)'],
                                            'answer': 'D) Tampon use or '
                                                      'staphylococcal/streptococcal '
                                                      'toxin-producing infections '
                                                      '(including postoperative '
                                                      'wounds)',
                                            'explanation': 'TSS is mediated by '
                                                           'superantigen toxins from '
                                                           'S. aureus or invasive '
                                                           'streptococci; historical '
                                                           'tampon association and '
                                                           'wound foci remain '
                                                           'important. Mosquito bites, '
                                                           'psoriasis, and tinea do '
                                                           'not produce toxin-mediated '
                                                           'shock with diffuse '
                                                           'erythroderma.',
                                            'choice_explanations': {'A': 'Mosquito '
                                                                         'bites do not '
                                                                         'cause '
                                                                         'staphylococcal/streptococcal '
                                                                         'toxic shock.',
                                                                    'B': 'Psoriasis '
                                                                         'therapy is '
                                                                         'unrelated to '
                                                                         'classic TSS '
                                                                         'pathogenesis.',
                                                                    'C': 'Tinea pedis '
                                                                         'is '
                                                                         'superficial '
                                                                         'fungal '
                                                                         'disease '
                                                                         'without TSS '
                                                                         'physiology.',
                                                                    'D': 'Tampon-associated '
                                                                         'or other '
                                                                         'toxin-producing '
                                                                         'staph/strep '
                                                                         'infections '
                                                                         'underlie '
                                                                         'TSS.'}}]},
                 'cases': {'easy': [{'title': 'Child with Facial Crusts',
                                     'stem': 'A 5-year-old has honey-colored crusts '
                                             'around the mouth after a scratch.',
                                     'question': 'Diagnosis?',
                                     'answer': 'Impetigo.',
                                     'discussion': 'Topical/systemic antibiotics per '
                                                   'extent; hygiene.',
                                     'book_hint': 'Habif / Rook / Fitzpatrick'}],
                           'medium': [{'title': 'Changing Mole',
                                       'stem': 'A 50-year-old has an asymmetrical '
                                               'multi-colored mole that grew over 3 '
                                               'months.',
                                       'question': 'Concern?',
                                       'answer': 'Melanoma — urgent dermatology '
                                                 'excision pathway.',
                                       'discussion': 'Do not shave biopsy suspicious '
                                                     'melanoma.',
                                       'book_hint': 'Habif / Rook / Fitzpatrick'}],
                           'hard': [{'title': 'Drug Rash + Mucosal Erosions',
                                     'stem': 'Days after a new anticonvulsant, a '
                                             'patient has fever, widespread dusky '
                                             'rash, and oral/genital erosions. Labs '
                                             'and imaging are pending; you must choose '
                                             'the safest next clinical concept.',
                                     'question': 'Fear?',
                                     'answer': 'SJS/TEN spectrum — stop drug, '
                                               'supportive care, specialty/burn '
                                               'pathways.',
                                     'discussion': 'Mucosal involvement is a red flag.',
                                     'book_hint': 'Habif / Rook / Fitzpatrick'}],
                           'extreme': [{'title': 'Purpuric Shock in Student',
                                        'stem': 'A college student rapidly develops '
                                                'fever, hypotension, and extensive '
                                                'purpura. Multiple teams are involved; '
                                                'prioritize life/limb/vision threats '
                                                'and avoid harmful premature '
                                                'therapies.',
                                        'question': 'Priority?',
                                        'answer': 'Meningococcemia/sepsis pathway — '
                                                  'immediate antibiotics after '
                                                  'cultures if possible, '
                                                  'resuscitation, infection control.',
                                        'discussion': 'Do not delay antibiotics for LP '
                                                      'if unstable.',
                                        'book_hint': 'Habif / Rook / Fitzpatrick'}]}},
 'obgyn': {'label': 'Obstetrics & Gynecology',
           'books': ['Williams Obstetrics',
                     "Beckmann and Ling's Obstetrics and Gynecology",
                     "DC Dutta's Textbook of Obstetrics"],
           'pdf_notes': ['PPH 4 Ts: Tone (atony most common), Trauma, Tissue, '
                         'Thrombin.',
                         'Ectopic: positive hCG + empty uterus + pain/spotting — '
                         'emergency awareness.',
                         'Pre-eclampsia after 20 weeks: HTN + proteinuria/organ '
                         'dysfunction.',
                         'Antenatal care milestones: dating, anomaly scan, Rh, '
                         'vaccines as indicated.',
                         'Doppler FHR typically ~10–12 weeks.'],
           'questions': {'easy': [{'question': 'The most common cause of primary '
                                               'postpartum hemorrhage is which '
                                               'mechanism?',
                                   'options': ['A) Uterine atony from inadequate '
                                               'myometrial contraction',
                                               'B) Amniotic fluid embolism as the '
                                               'leading everyday cause',
                                               'C) Uterine inversion in every vaginal '
                                               'delivery',
                                               'D) Inherited hemophilia A presenting '
                                               'first at delivery in all cases'],
                                   'answer': 'A) Uterine atony from inadequate '
                                             'myometrial contraction',
                                   'explanation': 'After placental delivery, '
                                                  'myometrial contraction ligates '
                                                  'spiral arteries. Failure of tone '
                                                  '(atony) is the leading PPH cause. '
                                                  'AFE, inversion, and hemophilia are '
                                                  'important but far less common.',
                                   'choice_explanations': {'A': 'Uterine atony is the '
                                                                'most frequent cause '
                                                                'of primary PPH.',
                                                           'B': 'Amniotic fluid '
                                                                'embolism is rare and '
                                                                'catastrophic, not the '
                                                                'most common PPH '
                                                                'cause.',
                                                           'C': 'Uterine inversion is '
                                                                'uncommon.',
                                                           'D': 'Hemophilia is rare '
                                                                'and does not explain '
                                                                'most PPH.'}},
                                  {'question': 'Risk of ectopic pregnancy rises most '
                                               'clearly after which history?',
                                   'options': ['A) Prior term cesarean alone without '
                                               'tubal disease in every case',
                                               'B) Prior pelvic inflammatory disease / '
                                               'tubal damage or prior ectopic '
                                               'pregnancy',
                                               'C) Exclusive formula feeding in a '
                                               'prior child',
                                               'D) First-trimester prenatal vitamin '
                                               'use'],
                                   'answer': 'B) Prior pelvic inflammatory disease / '
                                             'tubal damage or prior ectopic pregnancy',
                                   'explanation': 'Tubal scarring from PID or prior '
                                                  'ectopic impairs blastocyst '
                                                  'transport, raising ectopic risk. '
                                                  'Cesarean mainly risks accreta/scar '
                                                  'pregnancy in specific settings; '
                                                  'feeding and vitamins do not cause '
                                                  'tubal implantation.',
                                   'choice_explanations': {'A': 'Cesarean is not the '
                                                                'classic strongest '
                                                                'risk compared with '
                                                                'tubal damage/PID.',
                                                           'B': 'Tubal damage from PID '
                                                                'or prior ectopic '
                                                                'strongly increases '
                                                                'ectopic risk.',
                                                           'C': 'Infant feeding method '
                                                                'is unrelated to '
                                                                'ectopic implantation.',
                                                           'D': 'Prenatal vitamins do '
                                                                'not increase ectopic '
                                                                'risk.'}},
                                  {'question': 'Fetal heart tones are often first '
                                               'detectable by handheld Doppler around '
                                               'which gestational age range?',
                                   'options': ['A) At fertilization on day 0 reliably',
                                               'B) Only after 28 weeks in all '
                                               'pregnancies',
                                               'C) Approximately 10–12 weeks’ '
                                               'gestation in many pregnancies',
                                               'D) Never before the third trimester by '
                                               'definition'],
                                   'answer': 'C) Approximately 10–12 weeks’ gestation '
                                             'in many pregnancies',
                                   'explanation': 'Handheld Doppler typically detects '
                                                  'fetal heart activity near the end '
                                                  'of the first trimester (~10–12 '
                                                  'weeks), though timing varies with '
                                                  'habitus and equipment. It is not '
                                                  'present at fertilization nor '
                                                  'delayed universally to the third '
                                                  'trimester.',
                                   'choice_explanations': {'A': 'There is no audible '
                                                                'fetal heart at '
                                                                'fertilization.',
                                                           'B': 'Detection usually '
                                                                'occurs far earlier '
                                                                'than 28 weeks.',
                                                           'C': 'Many pregnancies '
                                                                'allow Doppler '
                                                                'detection around '
                                                                '10–12 weeks.',
                                                           'D': 'First-trimester '
                                                                'detection is common; '
                                                                'third-trimester-only '
                                                                'is false.'}}],
                         'medium': [{'question': 'Pre-eclampsia is defined as new '
                                                 'hypertension after 20 weeks plus '
                                                 'which additional element '
                                                 'conceptually?',
                                     'options': ['A) Chronic hypertension documented '
                                                 'before conception only',
                                                 'B) Isolated gestational diabetes '
                                                 'without blood pressure change',
                                                 'C) Physiologic edema of pregnancy '
                                                 'without proteinuria or end-organ '
                                                 'signs',
                                                 'D) Proteinuria and/or end-organ '
                                                 'dysfunction (e.g., thrombocytopenia, '
                                                 'renal/liver injury, neurologic '
                                                 'symptoms)'],
                                     'answer': 'D) Proteinuria and/or end-organ '
                                               'dysfunction (e.g., thrombocytopenia, '
                                               'renal/liver injury, neurologic '
                                               'symptoms)',
                                     'explanation': 'Pre-eclampsia = new HTN ≥20 weeks '
                                                    'with proteinuria or maternal '
                                                    'organ dysfunction. Chronic HTN '
                                                    'predates pregnancy; GDM and '
                                                    'benign edema alone do not meet '
                                                    'the definition.',
                                     'choice_explanations': {'A': 'Pre-pregnancy HTN '
                                                                  'is chronic '
                                                                  'hypertension, not '
                                                                  'pre-eclampsia by '
                                                                  'itself.',
                                                             'B': 'GDM is a glucose '
                                                                  'disorder, not the '
                                                                  'BP-plus-organ '
                                                                  'definition.',
                                                             'C': 'Dependent edema '
                                                                  'alone is common and '
                                                                  'insufficient for '
                                                                  'diagnosis.',
                                                             'D': 'Proteinuria or '
                                                                  'end-organ features '
                                                                  'with new HTN define '
                                                                  'pre-eclampsia.'}},
                                    {'question': 'The classic clinical combination '
                                                 'raising concern for ectopic '
                                                 'pregnancy is which?',
                                     'options': ['A) Amenorrhea/positive pregnancy '
                                                 'test, unilateral pelvic pain, and '
                                                 'vaginal bleeding',
                                                 'B) Painless term contractions with '
                                                 'intact membranes only',
                                                 'C) Third-trimester painless bright '
                                                 'bleeding of placenta previa '
                                                 'exclusively',
                                                 'D) Postmenopausal hot flashes '
                                                 'without pregnancy'],
                                     'answer': 'A) Amenorrhea/positive pregnancy test, '
                                               'unilateral pelvic pain, and vaginal '
                                               'bleeding',
                                     'explanation': 'Ectopic pregnancy presents in '
                                                    'early gestation with pain, '
                                                    'bleeding, and a positive test, '
                                                    'risking tubal rupture. Labor, '
                                                    'previa, and menopause are '
                                                    'different stages/conditions.',
                                     'choice_explanations': {'A': 'Positive pregnancy '
                                                                  'test + unilateral '
                                                                  'pain + bleeding is '
                                                                  'the classic ectopic '
                                                                  'triad cue.',
                                                             'B': 'Term labor is '
                                                                  'intrauterine '
                                                                  'pregnancy at term, '
                                                                  'not ectopic.',
                                                             'C': 'Painless '
                                                                  'third-trimester '
                                                                  'bleeding suggests '
                                                                  'previa, a '
                                                                  'later-pregnancy '
                                                                  'issue.',
                                                             'D': 'Menopause excludes '
                                                                  'ongoing '
                                                                  'pregnancy.'}},
                                    {'question': 'Shoulder dystocia refers to which '
                                                 'obstetric emergency?',
                                     'options': ['A) Cord prolapse after membrane '
                                                 'rupture only',
                                                 'B) Impaction of the fetal shoulder '
                                                 'behind the pubic symphysis after '
                                                 'delivery of the head',
                                                 'C) Uterine rupture at the fundus '
                                                 'exclusively',
                                                 'D) Retained placenta without any '
                                                 'shoulder involvement'],
                                     'answer': 'B) Impaction of the fetal shoulder '
                                               'behind the pubic symphysis after '
                                               'delivery of the head',
                                     'explanation': 'After the head delivers, an '
                                                    'impacted anterior shoulder behind '
                                                    'the symphysis defines shoulder '
                                                    'dystocia—a bony dystocia needing '
                                                    'calibrated maneuvers. Cord '
                                                    'prolapse, rupture, and retained '
                                                    'placenta are other emergencies.',
                                     'choice_explanations': {'A': 'Cord prolapse is '
                                                                  'umbilical cord '
                                                                  'presentation, not '
                                                                  'shoulder impaction.',
                                                             'B': 'Shoulder dystocia '
                                                                  'is failure of '
                                                                  'shoulder delivery '
                                                                  'after the head due '
                                                                  'to pubic impaction.',
                                                             'C': 'Uterine rupture is '
                                                                  'a different '
                                                                  'catastrophic event.',
                                                             'D': 'Retained placenta '
                                                                  'occurs after fetal '
                                                                  'delivery, not '
                                                                  'during shoulder '
                                                                  'delivery.'}}],
                         'hard': [{'question': 'In obstetrics, magnesium sulfate is '
                                               'primarily indicated for which purpose '
                                               'among the options?',
                                   'options': ['A) First-line tocolysis for weeks of '
                                               'preterm labor in all guidelines '
                                               'universally',
                                               'B) Treatment of postpartum hemorrhage '
                                               'from atony as the primary uterotonic',
                                               'C) Seizure prophylaxis/treatment in '
                                               'pre-eclampsia/eclampsia',
                                               'D) Routine anticoagulation for all '
                                               'cesarean deliveries'],
                                   'answer': 'C) Seizure prophylaxis/treatment in '
                                             'pre-eclampsia/eclampsia',
                                   'explanation': 'Magnesium sulfate is the agent of '
                                                  'choice for eclamptic seizure '
                                                  'prophylaxis and treatment. It is '
                                                  'not the primary long-term tocolytic '
                                                  'in modern practice, not a '
                                                  'uterotonic for PPH (use '
                                                  'oxytocin/etc.), and not an '
                                                  'anticoagulant.',
                                   'choice_explanations': {'A': 'Magnesium is not '
                                                                'preferred prolonged '
                                                                'tocolysis in current '
                                                                'practice.',
                                                           'B': 'Uterotonics '
                                                                '(oxytocin, '
                                                                'ergometrine, '
                                                                'prostaglandins) treat '
                                                                'atony—not magnesium.',
                                                           'C': 'MgSO4 prevents/treats '
                                                                'eclamptic seizures.',
                                                           'D': 'Magnesium has no '
                                                                'anticoagulant role '
                                                                'for cesarean VTE '
                                                                'prevention.'}},
                                  {'question': 'A 32-week pregnant woman presents with '
                                               'sudden painless bright red vaginal '
                                               'bleeding and a soft, nontender uterus; '
                                               'ultrasound shows placenta covering the '
                                               'os. Bleeding from placenta previa is '
                                               'typically characterized by which '
                                               'pattern?',
                                   'options': ['A) Painful dark bleeding with a rigid '
                                               'tender uterus of abruption',
                                               'B) Intermenstrual spotting from a '
                                               'cervical polyp only',
                                               'C) Heavy lochia several weeks '
                                               'postpartum only',
                                               'D) Painless bright red vaginal '
                                               'bleeding in the second/third '
                                               'trimester'],
                                   'answer': 'D) Painless bright red vaginal bleeding '
                                             'in the second/third trimester',
                                   'explanation': 'When the placenta covers the os, '
                                                  'painless bright bleeding occurs as '
                                                  'the lower segment develops. '
                                                  'Abruption is painful with a '
                                                  'hypertonic uterus; polyps and '
                                                  'postpartum lochia are different '
                                                  'timings.',
                                   'choice_explanations': {'A': 'Painful bleeding with '
                                                                'a woody uterus '
                                                                'suggests abruption, '
                                                                'not previa.',
                                                           'B': 'Cervical polyps cause '
                                                                'spotting unrelated to '
                                                                'placental location.',
                                                           'C': 'Postpartum lochia is '
                                                                'after delivery, not '
                                                                'antepartum previa '
                                                                'bleeding.',
                                                           'D': 'Painless '
                                                                'third-trimester '
                                                                'bright bleeding is '
                                                                'classic placenta '
                                                                'previa.'}},
                                  {'question': 'A pre-eclamptic patient at 34 weeks '
                                               'develops RUQ pain, schistocytes on '
                                               'smear, AST 420 U/L, and platelets '
                                               '48,000/µL. HELLP syndrome is defined '
                                               'by which laboratory cluster?',
                                   'options': ['A) Hemolysis, Elevated Liver enzymes, '
                                               'and Low Platelets',
                                               'B) Hyperglycemia, Elevated Lipase, and '
                                               'Low Potassium only',
                                               'C) High hemoglobin, Elevated '
                                               'Leukocytes, and Low Lymphocytes only',
                                               'D) Hyponatremia, Elevated cortisol, '
                                               'and Low ACTH exclusively'],
                                   'answer': 'A) Hemolysis, Elevated Liver enzymes, '
                                             'and Low Platelets',
                                   'explanation': 'HELLP = Hemolysis, Elevated Liver '
                                                  'enzymes, Low Platelets—a '
                                                  'microangiopathic hepatopathy of '
                                                  'severe pre-eclampsia requiring '
                                                  'urgent obstetric management. The '
                                                  'other letter expansions are '
                                                  'fabricated distractors.',
                                   'choice_explanations': {'A': 'HELLP expands to '
                                                                'hemolysis, elevated '
                                                                'liver enzymes, and '
                                                                'low platelets.',
                                                           'B': 'That cluster is not '
                                                                'HELLP and mixes '
                                                                'unrelated labs.',
                                                           'C': 'Blood-count pattern '
                                                                'listed is not the '
                                                                'HELLP definition.',
                                                           'D': 'Adrenal labs do not '
                                                                'define HELLP.'}}],
                         'extreme': [{'question': 'During labor, a multiparous woman '
                                                  'suddenly develops hypoxia, '
                                                  'hypotension, and disseminated '
                                                  'intravascular coagulation after '
                                                  'membrane rupture. There is no '
                                                  'preceding hemorrhage explaining the '
                                                  'coagulopathy. Which diagnosis must '
                                                  'be considered and how is management '
                                                  'framed?',
                                      'options': ['A) Simple vasovagal syncope treated '
                                                  'with observation alone',
                                                  'B) Amniotic fluid '
                                                  'embolism—supportive ABC '
                                                  'resuscitation, correct '
                                                  'coagulopathy, and advanced critical '
                                                  'care; diagnosis is clinical',
                                                  'C) Ordinary epidural hypotension '
                                                  'cured only by stopping oxytocin',
                                                  'D) Pulmonary embolism always '
                                                  'excluded by a normal chest '
                                                  'radiograph alone'],
                                      'answer': 'B) Amniotic fluid embolism—supportive '
                                                'ABC resuscitation, correct '
                                                'coagulopathy, and advanced critical '
                                                'care; diagnosis is clinical',
                                      'explanation': 'Amniotic fluid embolism presents '
                                                     'with abrupt cardiorespiratory '
                                                     'collapse and often profound DIC '
                                                     'during labor/delivery. Treatment '
                                                     'is aggressive supportive care '
                                                     'and blood-product resuscitation; '
                                                     'it is a clinical diagnosis of '
                                                     'exclusion. Syncope and mild '
                                                     'epidural hypotension lack DIC; '
                                                     'CXR cannot rule out PE.',
                                      'choice_explanations': {'A': 'Vasovagal events '
                                                                   'do not cause '
                                                                   'sudden DIC and '
                                                                   'refractory shock.',
                                                              'B': 'Peripartum '
                                                                   'collapse with DIC '
                                                                   'after ROM suggests '
                                                                   'AFE needing '
                                                                   'intensive '
                                                                   'supportive care.',
                                                              'C': 'Epidural '
                                                                   'hypotension is '
                                                                   'usually '
                                                                   'fluid/vasopressor '
                                                                   'responsive without '
                                                                   'DIC.',
                                                              'D': 'Normal CXR does '
                                                                   'not exclude PE; '
                                                                   'AFE remains on the '
                                                                   'differential with '
                                                                   'DIC.'}},
                                     {'question': 'A third-trimester patient develops '
                                                  'nausea, abdominal pain, '
                                                  'hypoglycemia, rising transaminases, '
                                                  'coagulopathy, and evolving liver '
                                                  'failure. Pre-eclampsia features may '
                                                  'overlap. Which entity is most '
                                                  'concerning?',
                                      'options': ['A) Intrahepatic cholestasis of '
                                                  'pregnancy with isolated pruritus '
                                                  'and elevated bile acids only',
                                                  'B) Uncomplicated hyperemesis '
                                                  'continuing from the first trimester '
                                                  'without liver failure',
                                                  'C) Acute fatty liver of pregnancy—a '
                                                  'obstetric emergency often requiring '
                                                  'prompt delivery and supportive care',
                                                  'D) Gilbert syndrome unmasked by '
                                                  'pregnancy as fulminant hepatic '
                                                  'failure'],
                                      'answer': 'C) Acute fatty liver of pregnancy—a '
                                                'obstetric emergency often requiring '
                                                'prompt delivery and supportive care',
                                      'explanation': 'AFLP is microvesicular fatty '
                                                     'infiltration causing acute '
                                                     'hepatic failure in late '
                                                     'pregnancy, overlapping '
                                                     'HELLP/pre-eclampsia. Delivery is '
                                                     'definitive therapy alongside ICU '
                                                     'support. Cholestasis causes '
                                                     'pruritus/bile acids; hyperemesis '
                                                     'is earlier; Gilbert’s is mild '
                                                     'unconjugated hyperbilirubinemia.',
                                      'choice_explanations': {'A': 'ICP lacks '
                                                                   'fulminant liver '
                                                                   'failure and '
                                                                   'hypoglycemia of '
                                                                   'AFLP.',
                                                              'B': 'Hyperemesis is '
                                                                   'primarily first '
                                                                   'trimester without '
                                                                   'this liver-failure '
                                                                   'pattern.',
                                                              'C': 'Late-pregnancy '
                                                                   'liver failure with '
                                                                   'metabolic '
                                                                   'derangement fits '
                                                                   'AFLP needing '
                                                                   'urgent delivery.',
                                                              'D': 'Gilbert syndrome '
                                                                   'does not cause '
                                                                   'fulminant hepatic '
                                                                   'failure.'}},
                                     {'question': 'A woman with one prior '
                                                  'low-transverse cesarean undergoes '
                                                  'induction for post-dates pregnancy. '
                                                  'Labor arrests in the active phase; '
                                                  'she develops sudden tearing pain, '
                                                  'loss of station, and fetal '
                                                  'bradycardia. Uterine rupture risk '
                                                  'rises most significantly in which '
                                                  'clinical setting?',
                                      'options': ['A) Spontaneous labor in an '
                                                  'unscarred uterus with no '
                                                  'augmentation ever',
                                                  'B) Elective repeat cesarean before '
                                                  'labor without trial of labor',
                                                  'C) External cephalic version '
                                                  'success without scar',
                                                  'D) Trial of labor after cesarean '
                                                  '(especially with labor dystocia or '
                                                  'prostaglandin induction in a '
                                                  'scarred uterus)'],
                                      'answer': 'D) Trial of labor after cesarean '
                                                '(especially with labor dystocia or '
                                                'prostaglandin induction in a scarred '
                                                'uterus)',
                                      'explanation': 'A prior uterine scar (usually '
                                                     'cesarean) is the major risk '
                                                     'substrate for rupture during '
                                                     'labor, particularly with '
                                                     'induction/augmentation stresses. '
                                                     'Unscarred spontaneous labor '
                                                     'rupture is rare; scheduled '
                                                     'repeat cesarean before labor '
                                                     'avoids TOLAC rupture risk; '
                                                     'successful ECV without scar is '
                                                     'not the high-risk setting.',
                                      'choice_explanations': {'A': 'Unscarred '
                                                                   'spontaneous labor '
                                                                   'has very low '
                                                                   'rupture risk.',
                                                              'B': 'Elective repeat '
                                                                   'cesarean without '
                                                                   'labor minimizes '
                                                                   'rupture risk '
                                                                   'versus TOLAC.',
                                                              'C': 'ECV risks are '
                                                                   'different; it is '
                                                                   'not the classic '
                                                                   'rupture setting of '
                                                                   'scarred labor.',
                                                              'D': 'TOLAC, especially '
                                                                   'with '
                                                                   'dystocia/induction '
                                                                   'on a scar, '
                                                                   'elevates uterine '
                                                                   'rupture risk.'}}]},
           'cases': {'easy': [{'title': 'Boggy Uterus Bleeding',
                               'stem': 'After vaginal delivery, heavy bleeding with a '
                                       'soft boggy uterus.',
                               'question': 'First concept?',
                               'answer': 'Atony — massage + oxytocin and PPH protocol.',
                               'discussion': 'Tone is most common.',
                               'book_hint': 'Williams Obstetrics'}],
                     'medium': [{'title': 'Positive hCG + Unilateral Pain',
                                 'stem': 'Positive pregnancy test, spotting, '
                                         'unilateral pelvic pain, empty uterus, '
                                         'adnexal mass.',
                                 'question': 'Diagnosis?',
                                 'answer': 'Ectopic pregnancy until proven otherwise.',
                                 'discussion': 'Stability guides medical vs surgical '
                                               'care.',
                                 'book_hint': 'Williams Obstetrics'}],
                     'hard': [{'title': 'Seizure at 34 Weeks',
                               'stem': 'A primip at 34 weeks with headache and HTN has '
                                       'a tonic-clonic seizure. Labs and imaging are '
                                       'pending; you must choose the safest next '
                                       'clinical concept.',
                               'question': 'Diagnosis and drug concept?',
                               'answer': 'Eclampsia — magnesium sulfate and '
                                         'maternal/fetal stabilization; delivery '
                                         'planning.',
                               'discussion': 'Protect airway and control seizure.',
                               'book_hint': 'Williams Obstetrics'}],
                     'extreme': [{'title': 'Collapse Minutes After Delivery',
                                  'stem': 'Suddenly after delivery a woman becomes '
                                          'hypoxic, hypotensive, and coagulopathic '
                                          'without visible atony initially. Multiple '
                                          'teams are involved; prioritize '
                                          'life/limb/vision threats and avoid harmful '
                                          'premature therapies.',
                                  'question': 'Consider?',
                                  'answer': 'Amniotic fluid embolism among other '
                                            'catastrophic differentials — ACLS '
                                            'obstetric modifications, correct '
                                            'coagulopathy, supportive ICU care.',
                                  'discussion': 'Diagnosis of exclusion but act fast.',
                                  'book_hint': 'Williams Obstetrics'}]}},
 'pediatrics': {'label': 'Pediatrics',
                'books': ['Nelson Textbook of Pediatrics',
                          'Illustrated Textbook of Paediatrics — Lissauer',
                          "Forfar and Arneil's Textbook of Pediatrics"],
                'pdf_notes': ['ORS first-line for most pediatric dehydration from '
                              'diarrhea.',
                              'MMR is live; know live vs inactivated vaccines.',
                              'Kawasaki: prolonged fever + mucocutaneous signs → '
                              'coronary risk.',
                              'APGAR at 1 and 5 minutes guides immediate newborn '
                              'status.',
                              'Always calculate pediatric doses by weight; watch fluid '
                              'rates.'],
                'questions': {'easy': [{'question': 'For children with mild to '
                                                    'moderate dehydration from '
                                                    'gastroenteritis who can drink, '
                                                    'which therapy is first-line?',
                                        'options': ['A) Oral rehydration solution with '
                                                    'appropriate glucose–sodium '
                                                    'balance',
                                                    'B) Immediate IV 3% saline for all '
                                                    'cases regardless of severity',
                                                    'C) Routine antidiarrheal opioids '
                                                    'as primary rehydration',
                                                    'D) Withholding all fluids for 12 '
                                                    "hours to 'rest the gut'"],
                                        'answer': 'A) Oral rehydration solution with '
                                                  'appropriate glucose–sodium balance',
                                        'explanation': 'ORS uses glucose–sodium '
                                                       'cotransport to restore ECF '
                                                       'volume and is first-line for '
                                                       'mild–moderate dehydration. '
                                                       'Hypertonic saline, '
                                                       'antimotility opioids, and '
                                                       'prolonged fluid withholding '
                                                       'are inappropriate primary '
                                                       'strategies.',
                                        'choice_explanations': {'A': 'ORS is the '
                                                                     'preferred '
                                                                     'first-line '
                                                                     'rehydration for '
                                                                     'most dehydrated '
                                                                     'children who can '
                                                                     'drink.',
                                                                'B': '3% saline is for '
                                                                     'symptomatic '
                                                                     'hyponatremia, '
                                                                     'not routine '
                                                                     'gastroenteritis '
                                                                     'rehydration.',
                                                                'C': 'Antimotility '
                                                                     'opioids are '
                                                                     'avoided in '
                                                                     'children and do '
                                                                     'not rehydrate.',
                                                                'D': 'Withholding '
                                                                     'fluids worsens '
                                                                     'dehydration.'}},
                                       {'question': 'The MMR vaccine is which type of '
                                                    'immunizing agent?',
                                        'options': ['A) Pure polysaccharide vaccine '
                                                    'without protein conjugation',
                                                    'B) Live attenuated viral vaccine '
                                                    'requiring caution in severe '
                                                    'immunodeficiency',
                                                    'C) Toxoid vaccine like tetanus '
                                                    'toxoid',
                                                    'D) Inactivated whole-cell '
                                                    'bacterial vaccine only'],
                                        'answer': 'B) Live attenuated viral vaccine '
                                                  'requiring caution in severe '
                                                  'immunodeficiency',
                                        'explanation': 'MMR contains live attenuated '
                                                       'measles, mumps, and rubella '
                                                       'viruses and is contraindicated '
                                                       'in significant '
                                                       'immunosuppression. It is not a '
                                                       'polysaccharide, toxoid, or '
                                                       'inactivated bacterial product.',
                                        'choice_explanations': {'A': 'Polysaccharide '
                                                                     'vaccines (e.g., '
                                                                     'some '
                                                                     'pneumococcal) '
                                                                     'differ from live '
                                                                     'MMR.',
                                                                'B': 'MMR is live '
                                                                     'attenuated and '
                                                                     'avoided in '
                                                                     'severe '
                                                                     'immunodeficiency.',
                                                                'C': 'Toxoids are '
                                                                     'inactivated '
                                                                     'toxins '
                                                                     '(tetanus/diphtheria), '
                                                                     'not MMR.',
                                                                'D': 'MMR is viral '
                                                                     'live-attenuated, '
                                                                     'not inactivated '
                                                                     'bacterial.'}},
                                       {'question': 'The Apgar score is traditionally '
                                                    'assessed at which times after '
                                                    'birth?',
                                        'options': ['A) Only at 24 hours of life',
                                                    'B) Before delivery during each '
                                                    'contraction',
                                                    'C) At 1 and 5 minutes of life '
                                                    '(with further scores if still '
                                                    'low)',
                                                    'D) Weekly throughout the neonatal '
                                                    'period only'],
                                        'answer': 'C) At 1 and 5 minutes of life (with '
                                                  'further scores if still low)',
                                        'explanation': 'Apgar evaluates Appearance, '
                                                       'Pulse, Grimace, Activity, and '
                                                       'Respiration at 1 and 5 minutes '
                                                       'to summarize early transition; '
                                                       'repeated scores track response '
                                                       'if depressed. It is not a '
                                                       'prenatal or weekly outpatient '
                                                       'tool.',
                                        'choice_explanations': {'A': 'Apgar is an '
                                                                     'immediate '
                                                                     'postnatal score, '
                                                                     'not a 24-hour '
                                                                     'assessment.',
                                                                'B': 'It is not '
                                                                     'measured during '
                                                                     'labor '
                                                                     'contractions.',
                                                                'C': 'Standard timing '
                                                                     'is 1 and 5 '
                                                                     'minutes after '
                                                                     'birth.',
                                                                'D': 'Weekly scoring '
                                                                     'is not the Apgar '
                                                                     'framework.'}}],
                              'medium': [{'question': 'The most feared cardiac '
                                                      'complication of Kawasaki '
                                                      'disease is which?',
                                          'options': ['A) Congenital bicuspid aortic '
                                                      'valve present from birth',
                                                      'B) Infective endocarditis from '
                                                      'dental flora exclusively',
                                                      'C) Chronic rheumatic mitral '
                                                      'stenosis within days of fever',
                                                      'D) Coronary artery aneurysms '
                                                      '(and risk of '
                                                      'thrombosis/ischemia)'],
                                          'answer': 'D) Coronary artery aneurysms (and '
                                                    'risk of thrombosis/ischemia)',
                                          'explanation': 'Kawasaki vasculitis '
                                                         'preferentially damages '
                                                         'coronary arteries, producing '
                                                         'aneurysms that may '
                                                         'thrombose. Bicuspid valve is '
                                                         'congenital; endocarditis and '
                                                         'acute rheumatic stenosis are '
                                                         'different '
                                                         'diseases/timelines.',
                                          'choice_explanations': {'A': 'Bicuspid '
                                                                       'aortic valve '
                                                                       'is congenital, '
                                                                       'not acquired '
                                                                       'from Kawasaki.',
                                                                  'B': 'Infective '
                                                                       'endocarditis '
                                                                       'is a separate '
                                                                       'infectious '
                                                                       'entity.',
                                                                  'C': 'Rheumatic '
                                                                       'stenosis '
                                                                       'evolves over '
                                                                       'years after '
                                                                       'ARF, not days '
                                                                       'of Kawasaki '
                                                                       'fever.',
                                                                  'D': 'Coronary '
                                                                       'aneurysms are '
                                                                       'the signature '
                                                                       'serious '
                                                                       'Kawasaki '
                                                                       'complication.'}},
                                         {'question': 'Fever in a neonate (especially '
                                                      '<28 days) is managed with which '
                                                      'guiding principle?',
                                          'options': ['A) Urgent evaluation for '
                                                      'serious bacterial/HSV infection '
                                                      'with empiric antimicrobials per '
                                                      'protocol—do not reassure as '
                                                      'simple viral illness',
                                                      'B) Home observation with '
                                                      'antipyretics only for 72 hours '
                                                      'first',
                                                      'C) Oral antibiotics without '
                                                      'cultures as definitive care',
                                                      'D) Lumbar puncture is never '
                                                      'indicated in this age group'],
                                          'answer': 'A) Urgent evaluation for serious '
                                                    'bacterial/HSV infection with '
                                                    'empiric antimicrobials per '
                                                    'protocol—do not reassure as '
                                                    'simple viral illness',
                                          'explanation': 'Neonates have immature '
                                                         'immunity and high risk of '
                                                         'bacteremia/meningitis/HSV. '
                                                         'Guidelines mandate prompt '
                                                         'workup and empiric therapy '
                                                         'rather than watchful waiting '
                                                         'or incomplete oral '
                                                         'treatment.',
                                          'choice_explanations': {'A': 'Neonatal fever '
                                                                       'requires '
                                                                       'urgent septic '
                                                                       'workup and '
                                                                       'empiric '
                                                                       'treatment '
                                                                       'pathways.',
                                                                  'B': 'Home '
                                                                       'observation '
                                                                       'delays '
                                                                       'life-saving '
                                                                       'therapy in '
                                                                       'occult '
                                                                       'neonatal '
                                                                       'sepsis.',
                                                                  'C': 'Cultures and '
                                                                       'IV therapy are '
                                                                       'needed; '
                                                                       'oral-only care '
                                                                       'is inadequate.',
                                                                  'D': 'LP is often '
                                                                       'part of the '
                                                                       'neonatal fever '
                                                                       'evaluation.'}},
                                         {'question': 'Viral croup '
                                                      '(laryngotracheobronchitis) '
                                                      'classically features which '
                                                      'clinical hallmark?',
                                          'options': ['A) Expiratory wheeze only from '
                                                      'small-airway asthma without '
                                                      'upper-airway signs',
                                                      'B) Inspiratory stridor and a '
                                                      'barking cough, often worse at '
                                                      'night',
                                                      'C) Drooling and tripoding from '
                                                      'epiglottitis as the usual mild '
                                                      'pattern',
                                                      'D) Unilateral wheeze from '
                                                      'inhaled foreign body always'],
                                          'answer': 'B) Inspiratory stridor and a '
                                                    'barking cough, often worse at '
                                                    'night',
                                          'explanation': 'Croup inflames the '
                                                         'subglottis, producing barky '
                                                         'cough and inspiratory '
                                                         'stridor. Pure asthma is '
                                                         'lower airway; epiglottitis '
                                                         'is toxic with drooling; '
                                                         'foreign body is often '
                                                         'unilateral/abrupt.',
                                          'choice_explanations': {'A': 'Isolated '
                                                                       'expiratory '
                                                                       'wheeze '
                                                                       'suggests '
                                                                       'asthma/bronchiolitis '
                                                                       'more than '
                                                                       'croup.',
                                                                  'B': 'Barking cough '
                                                                       'with '
                                                                       'inspiratory '
                                                                       'stridor is the '
                                                                       'croup '
                                                                       'hallmark.',
                                                                  'C': 'Drooling/tripoding '
                                                                       'suggests '
                                                                       'epiglottitis, '
                                                                       'a different '
                                                                       'emergency.',
                                                                  'D': 'Foreign body '
                                                                       'aspiration has '
                                                                       'a different '
                                                                       'sudden '
                                                                       'unilateral '
                                                                       'pattern.'}}],
                              'hard': [{'question': 'A 4-week-old boy has progressive '
                                                    'nonbilious projectile vomiting, a '
                                                    'palpable olive mass, and '
                                                    'hypochloremic metabolic '
                                                    'alkalosis. Infantile hypertrophic '
                                                    'pyloric stenosis classically '
                                                    'presents with which pattern?',
                                        'options': ['A) Bilious vomiting from day 1 of '
                                                    'life always',
                                                    'B) Chronic diarrhea and failure '
                                                    'to thrive from celiac disease',
                                                    'C) Progressive nonbilious '
                                                    'projectile vomiting at 2–6 weeks '
                                                    'with hypochloremic metabolic '
                                                    'alkalosis',
                                                    'D) Painless bloody stools of '
                                                    'milk-protein allergy only'],
                                        'answer': 'C) Progressive nonbilious '
                                                  'projectile vomiting at 2–6 weeks '
                                                  'with hypochloremic metabolic '
                                                  'alkalosis',
                                        'explanation': 'Pyloric muscle hypertrophy '
                                                       'obstructs gastric outlet at '
                                                       'weeks 2–6, causing nonbilious '
                                                       'projectile vomiting and loss '
                                                       'of HCl (hypochloremic '
                                                       'alkalosis). Bilious emesis '
                                                       'implies distal obstruction; '
                                                       'celiac and milk-protein '
                                                       'allergy differ.',
                                        'choice_explanations': {'A': 'Bilious emesis '
                                                                     'suggests '
                                                                     'malrotation/other '
                                                                     'intestinal '
                                                                     'obstruction, not '
                                                                     'pyloric '
                                                                     'stenosis.',
                                                                'B': 'Celiac disease '
                                                                     'presents later '
                                                                     'with '
                                                                     'malabsorption, '
                                                                     'not projectile '
                                                                     'nonbilious '
                                                                     'vomiting at 3 '
                                                                     'weeks.',
                                                                'C': 'Age, nonbilious '
                                                                     'projectile '
                                                                     'vomiting, and '
                                                                     'hypochloremic '
                                                                     'alkalosis are '
                                                                     'classic pyloric '
                                                                     'stenosis.',
                                                                'D': 'Allergic colitis '
                                                                     'causes bloody '
                                                                     'stools, not '
                                                                     'gastric-outlet '
                                                                     'alkalosis.'}},
                                       {'question': 'Intussusception stool is '
                                                    'classically described as which '
                                                    'appearance when ischemia '
                                                    'develops?',
                                        'options': ['A) Acholic pale stools of biliary '
                                                    'atresia',
                                                    'B) Melena from duodenal ulcer in '
                                                    'neonates typically',
                                                    'C) Steatorrhea from pancreatic '
                                                    'insufficiency alone',
                                                    'D) Currant-jelly (blood and '
                                                    'mucus) stools'],
                                        'answer': 'D) Currant-jelly (blood and mucus) '
                                                  'stools',
                                        'explanation': 'Ileocolic intussusception '
                                                       'compromises mucosa, mixing '
                                                       'blood and mucus into '
                                                       'currant-jelly stools, often '
                                                       'with intermittent pain and a '
                                                       'sausage mass. Acholic stools, '
                                                       'neonatal ulcer melena, and '
                                                       'steatorrhea are other '
                                                       'conditions.',
                                        'choice_explanations': {'A': 'Acholic stools '
                                                                     'indicate '
                                                                     'cholestasis/biliary '
                                                                     'atresia.',
                                                                'B': 'Duodenal ulcer '
                                                                     'melena is '
                                                                     'uncommon as the '
                                                                     'intussusception '
                                                                     'hallmark.',
                                                                'C': 'Steatorrhea '
                                                                     'reflects fat '
                                                                     'malabsorption, '
                                                                     'not acute '
                                                                     'intussusception.',
                                                                'D': 'Currant-jelly '
                                                                     'stools are the '
                                                                     'classic late '
                                                                     'intussusception '
                                                                     'finding.'}},
                                       {'question': 'A male neonate with salt-wasting '
                                                    'congenital adrenal hyperplasia '
                                                    'may present in crisis with which '
                                                    'electrolyte pattern?',
                                        'options': ['A) Hyponatremia, hyperkalemia, '
                                                    'and dehydration from aldosterone '
                                                    'deficiency',
                                                    'B) Hypernatremia and hypokalemia '
                                                    'from mineralocorticoid excess',
                                                    'C) Isolated hypercalcemia without '
                                                    'sodium change',
                                                    'D) Metabolic alkalosis with '
                                                    'severe hypokalemia only like '
                                                    'pyloric stenosis'],
                                        'answer': 'A) Hyponatremia, hyperkalemia, and '
                                                  'dehydration from aldosterone '
                                                  'deficiency',
                                        'explanation': '21-hydroxylase deficiency '
                                                       'impairs cortisol and '
                                                       'aldosterone; salt wasting '
                                                       'causes hyponatremia, '
                                                       'hyperkalemia, and shock. '
                                                       'Mineralocorticoid excess does '
                                                       'the opposite; hypercalcemia '
                                                       'and pyloric alkalosis are '
                                                       'different.',
                                        'choice_explanations': {'A': 'Aldosterone '
                                                                     'deficiency in '
                                                                     'salt-wasting CAH '
                                                                     'yields '
                                                                     'hyponatremia and '
                                                                     'hyperkalemia.',
                                                                'B': 'That pattern is '
                                                                     'hyperaldosteronism, '
                                                                     'not CAH crisis.',
                                                                'C': 'Calcium is not '
                                                                     'the primary CAH '
                                                                     'crisis '
                                                                     'disturbance.',
                                                                'D': 'Hypochloremic '
                                                                     'alkalosis is '
                                                                     'pyloric '
                                                                     'stenosis, not '
                                                                     'CAH.'}}],
                              'extreme': [{'question': 'A term neonate is well for 4 '
                                                       'days then becomes grey, poorly '
                                                       'perfused, and acidotic with '
                                                       'weak femoral pulses as the '
                                                       'ductus arteriosus closes. '
                                                       'Sepsis workup is started. '
                                                       'Which cardiovascular concept '
                                                       'and therapy must be considered '
                                                       'immediately under specialist '
                                                       'guidance?',
                                           'options': ['A) Innocent peripheral '
                                                       'pulmonic stenosis of infancy '
                                                       'needing no therapy',
                                                       'B) Possible ductal-dependent '
                                                       'systemic blood flow lesion—ABC '
                                                       'resuscitation and '
                                                       'prostaglandin E1 to reopen the '
                                                       'duct while arranging '
                                                       'cardiology/surgery',
                                                       'C) Supraventricular '
                                                       'tachycardia treated first with '
                                                       'AV-nodal blockers only',
                                                       'D) Physiologic anemia of '
                                                       'infancy as the sole '
                                                       'explanation for acidosis and '
                                                       'weak femorals'],
                                           'answer': 'B) Possible ductal-dependent '
                                                     'systemic blood flow lesion—ABC '
                                                     'resuscitation and prostaglandin '
                                                     'E1 to reopen the duct while '
                                                     'arranging cardiology/surgery',
                                           'explanation': 'Left-sided obstructive '
                                                          'lesions (e.g., critical '
                                                          'coarctation/HLHS) rely on '
                                                          'ductal flow to the systemic '
                                                          'circulation. Ductal closure '
                                                          'precipitates shock with '
                                                          'differential pulses. PGE1 '
                                                          'maintains ductal patency '
                                                          'pending intervention; '
                                                          'sepsis remains concurrent, '
                                                          'but ductal dependence must '
                                                          'not be missed. Innocent '
                                                          'murmurs, SVT drugs, and '
                                                          'physiologic anemia do not '
                                                          'fit this shock pattern.',
                                           'choice_explanations': {'A': 'Innocent PPS '
                                                                        'does not '
                                                                        'cause '
                                                                        'ductal-closure '
                                                                        'shock and '
                                                                        'weak '
                                                                        'femorals.',
                                                                   'B': 'Ductal-dependent '
                                                                        'systemic '
                                                                        'outflow '
                                                                        'lesions need '
                                                                        'PGE1 and '
                                                                        'urgent '
                                                                        'cardiology '
                                                                        'care.',
                                                                   'C': 'AV-nodal '
                                                                        'blockers are '
                                                                        'not the '
                                                                        'therapy for '
                                                                        'ductal-closure '
                                                                        'cardiogenic '
                                                                        'shock.',
                                                                   'D': 'Physiologic '
                                                                        'anemia is '
                                                                        'gradual and '
                                                                        'does not '
                                                                        'produce acute '
                                                                        'ductal shock '
                                                                        'with pulse '
                                                                        'deficits.'}},
                                          {'question': 'A 4-month-old has bruises on '
                                                       'the pinna and frenulum tear, '
                                                       'retinal hemorrhages, and a '
                                                       'metaphyseal corner fracture, '
                                                       'with a changing caregiver '
                                                       'history. Which interpretation '
                                                       'is most appropriate?',
                                           'options': ['A) Typical accidental bruises '
                                                       'over bony prominences from '
                                                       'rolling only',
                                                       'B) Vitamin K deficiency '
                                                       'bleeding as the single '
                                                       'explanation for fractures and '
                                                       'retinal hemorrhages',
                                                       'C) Injuries highly concerning '
                                                       'for non-accidental '
                                                       'trauma—protect the child and '
                                                       'perform a full '
                                                       'forensic/medical evaluation',
                                                       'D) Simple osteogenesis '
                                                       'imperfecta diagnosed without '
                                                       'genetic or radiographic '
                                                       'pattern review'],
                                           'answer': 'C) Injuries highly concerning '
                                                     'for non-accidental '
                                                     'trauma—protect the child and '
                                                     'perform a full forensic/medical '
                                                     'evaluation',
                                           'explanation': 'Ear bruises, frenulum '
                                                          'injury, retinal '
                                                          'hemorrhages, and classic '
                                                          'metaphyseal fractures in a '
                                                          'nonambulatory infant are '
                                                          'sentinel non-accidental '
                                                          'trauma findings. Safety '
                                                          'reporting and '
                                                          'skeletal/ophthalmologic/CNS '
                                                          'evaluation are mandatory. '
                                                          'Accidental patterns differ; '
                                                          'vitamin K and OI require '
                                                          'specific contexts and do '
                                                          'not dismiss protective '
                                                          'action.',
                                           'choice_explanations': {'A': 'Pinna/frenulum '
                                                                        'injuries are '
                                                                        'not typical '
                                                                        'accidental '
                                                                        'rolling '
                                                                        'bruises.',
                                                                   'B': 'VKDB causes '
                                                                        'bleeding, not '
                                                                        'metaphyseal '
                                                                        'fractures '
                                                                        'plus retinal '
                                                                        'hemorrhages '
                                                                        'as a package '
                                                                        'without '
                                                                        'trauma.',
                                                                   'C': 'This '
                                                                        'constellation '
                                                                        'is classic '
                                                                        'abusive '
                                                                        'injury '
                                                                        'requiring '
                                                                        'protection '
                                                                        'and full '
                                                                        'workup.',
                                                                   'D': 'OI is a '
                                                                        'consideration '
                                                                        'in '
                                                                        'differentials '
                                                                        'but does not '
                                                                        'override '
                                                                        'safeguarding '
                                                                        'when abuse '
                                                                        'markers '
                                                                        'cluster.'}},
                                          {'question': 'An unvaccinated toddler '
                                                       'develops high fever, drooling, '
                                                       'muffled voice, and sits '
                                                       'forward tripoding with '
                                                       'stridor. Soft-tissue neck '
                                                       'radiograph is considered. '
                                                       'Which diagnosis and airway '
                                                       'principle apply?',
                                           'options': ['A) Mild croup managed at home '
                                                       'with humidity alone',
                                                       'B) Foreign body already '
                                                       'expelled because drooling is '
                                                       'present',
                                                       'C) Peritonsillar abscess in a '
                                                       'toddler as the most common '
                                                       'cause',
                                                       'D) Acute epiglottitis—avoid '
                                                       'agitating the child; secure '
                                                       'airway in a controlled setting '
                                                       'with expert airway support and '
                                                       'give antibiotics'],
                                           'answer': 'D) Acute epiglottitis—avoid '
                                                     'agitating the child; secure '
                                                     'airway in a controlled setting '
                                                     'with expert airway support and '
                                                     'give antibiotics',
                                           'explanation': 'Epiglottitis (Haemophilus '
                                                          'influenzae type b '
                                                          'historically) causes toxic '
                                                          'upper-airway obstruction '
                                                          'with drooling and '
                                                          'tripoding. Agitation can '
                                                          'precipitate complete '
                                                          'obstruction; airway is '
                                                          'secured by experienced '
                                                          'clinicians, then '
                                                          'antibiotics. Home croup '
                                                          'care, assuming expelled FB, '
                                                          'and typical older-child PTA '
                                                          'do not fit.',
                                           'choice_explanations': {'A': 'Toxic '
                                                                        'drooling '
                                                                        'tripoding is '
                                                                        'not mild '
                                                                        'croup.',
                                                                   'B': 'Drooling with '
                                                                        'fever/toxicity '
                                                                        'suggests '
                                                                        'infectious '
                                                                        'epiglottitis '
                                                                        'more than '
                                                                        'resolved FB.',
                                                                   'C': 'Peritonsillar '
                                                                        'abscess is '
                                                                        'uncommon in '
                                                                        'toddlers and '
                                                                        'presents '
                                                                        'differently.',
                                                                   'D': 'Suspected '
                                                                        'epiglottitis '
                                                                        'needs calm '
                                                                        'expert airway '
                                                                        'management '
                                                                        'plus '
                                                                        'antimicrobials.'}}]},
                'cases': {'easy': [{'title': 'Diarrhea + Sunken Eyes',
                                    'stem': 'An 18-month-old with watery diarrhea has '
                                            'sunken eyes but still drinks.',
                                    'question': 'Initial therapy?',
                                    'answer': 'ORS.',
                                    'discussion': 'IV if severe/shock.',
                                    'book_hint': 'Nelson Pediatrics'}],
                          'medium': [{'title': 'Fever 6 Days + Strawberry Tongue',
                                      'stem': 'A 3-year-old has ≥5 days fever, '
                                              'conjunctivitis, strawberry tongue, '
                                              'rash, cervical nodes.',
                                      'question': 'Diagnosis?',
                                      'answer': 'Kawasaki disease.',
                                      'discussion': 'IVIG to reduce coronary risk.',
                                      'book_hint': 'Nelson Pediatrics'}],
                          'hard': [{'title': 'Bilious Vomiting Neonate',
                                    'stem': 'A 3-day-old has bilious vomiting and '
                                            'abdominal distension. Labs and imaging '
                                            'are pending; you must choose the safest '
                                            'next clinical concept.',
                                    'question': 'Emergency concern?',
                                    'answer': 'Malrotation with midgut volvulus until '
                                              'excluded — urgent surgical evaluation.',
                                    'discussion': 'Bilious vomiting in neonate is an '
                                                  'emergency.',
                                    'book_hint': 'Nelson Pediatrics'}],
                          'extreme': [{'title': 'Neonate in Shock Day 5',
                                       'stem': 'A previously well term neonate becomes '
                                               'grey, hypotensive, and acidotic on day '
                                               '5 of life as the duct closes. Femoral '
                                               'pulses are weak. Multiple teams are '
                                               'involved; prioritize life/limb/vision '
                                               'threats and avoid harmful premature '
                                               'therapies.',
                                       'question': 'Concept?',
                                       'answer': 'Possible ductal-dependent congenital '
                                                 'heart disease — ABC resuscitation '
                                                 'and urgent prostaglandin under '
                                                 'specialist guidance plus cardiology.',
                                       'discussion': 'Sepsis remains on the '
                                                     'differential too.',
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


def _option_body(option: str) -> str:
    text = str(option).strip()
    if len(text) > 2 and text[1] in ").]" and text[0].upper() in "ABCD":
        return text[2:].strip()
    return text


def present_question(item: dict) -> dict:
    """Shuffle A–D so the correct letter is not predictable from position.

    Remaps choice_explanations to the new letters so scientific reasons stay
    attached to the same option text after shuffling.
    """
    options = list(item.get("options") or [])
    if len(options) < 2:
        return dict(item)
    bodies = [_option_body(o) for o in options]
    correct_body = _option_body(item.get("answer", ""))

    # Map old letter -> explanation text
    old_expl = item.get("choice_explanations") or item.get("option_explanations") or {}
    body_to_expl: dict[str, str] = {}
    if isinstance(old_expl, dict):
        for opt in options:
            letter = str(opt).strip()[:1].upper()
            body = _option_body(opt)
            raw = old_expl.get(letter) or old_expl.get(letter.lower())
            if isinstance(raw, dict):
                text = " ".join(
                    str(
                        raw.get("why_not")
                        or raw.get("why_wrong")
                        or raw.get("why")
                        or raw.get("reason")
                        or raw.get("meaning")
                        or ""
                    ).split()
                )
            else:
                text = " ".join(str(raw or "").split())
            if text:
                body_to_expl[body] = text

    order = list(range(len(bodies)))
    random.shuffle(order)
    letters = "ABCD"
    new_options = []
    new_answer = item.get("answer")
    new_expl: dict[str, str] = {}
    for i, idx in enumerate(order):
        letter = letters[i]
        body = bodies[idx]
        text = f"{letter}) {body}"
        new_options.append(text)
        if body == correct_body:
            new_answer = text
        if body in body_to_expl:
            new_expl[letter] = body_to_expl[body]
    out = dict(item)
    out["options"] = new_options
    out["answer"] = new_answer
    if new_expl:
        out["choice_explanations"] = new_expl
    return out


def format_question_prompt(item: dict, specialty_label_text: str, difficulty: str) -> str:
    diff = DIFFICULTY_LABELS[difficulty]
    options = "\n".join(item["options"])
    return (
        f"📘 *Short MCQ — {specialty_label_text}*\n"
        f"Difficulty: *{diff}*\n\n"
        f"{item['question']}\n\n"
        f"{options}\n\n"
        f"_Read all options carefully, then tap A / B / C / D._"
    )
def format_question_result(
    item: dict, chosen: str, specialty_label_text: str, difficulty: str
) -> str:
    from pathlib import Path as _P
    import sys

    _root = _P(__file__).resolve().parent
    for _p in (_root, _root.parent):
        if str(_p) not in sys.path:
            sys.path.insert(0, str(_p))
    from choice_explanations import format_all_choice_explanations

    correct = correct_letter(item)
    chosen = chosen.upper()
    verdict = "✅ *Correct!*" if chosen == correct else f"❌ *Incorrect.* You chose *{chosen}*."
    options = "\n".join(item["options"])
    diff = DIFFICULTY_LABELS[difficulty]
    breakdown = format_all_choice_explanations(item)
    return (
        f"📘 *Short MCQ — {specialty_label_text}*\n"
        f"Difficulty: *{diff}*\n\n"
        f"{item['question']}\n\n"
        f"{options}\n\n"
        f"{verdict}\n"
        f"✅ *Answer:* {item['answer']}\n"
        f"📚 *Scientific explanation:* {item['explanation']}\n\n"
        f"{breakdown}"
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
        "🩺 *CharaNas Medicine*\n"
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
