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
                                                    'B) Prolonged (>30 min) crushing '
                                                    'retrosternal pressure at rest '
                                                    'with diaphoresis suggesting acute '
                                                    'coronary occlusion',
                                                    'C) Sharp pain reproduced by '
                                                    'chest-wall palpation at a single '
                                                    'rib',
                                                    'D) Burning epigastric pain that '
                                                    'resolves only after antacids'],
                                        'answer': 'A) Transient retrosternal pressure '
                                                  'provoked by exertion and relieved '
                                                  'by rest or nitrates',
                                        'explanation': 'Typical angina is transient '
                                                       'demand ischemia: retrosternal '
                                                       'pressure with exertion that '
                                                       'eases when demand falls or '
                                                       'nitrates reduce preload. '
                                                       'Prolonged rest pain with '
                                                       'autonomic features points '
                                                       'toward ACS rather than classic '
                                                       'exertional angina. '
                                                       'Musculoskeletal and purely '
                                                       'reflux patterns imply '
                                                       'non-ischemic mechanisms.',
                                        'choice_explanations': {'A': 'Exertional, '
                                                                     'brief, '
                                                                     'nitrate-responsive '
                                                                     'retrosternal '
                                                                     'pressure is the '
                                                                     'classic ischemic '
                                                                     'angina phenotype '
                                                                     'from '
                                                                     'supply–demand '
                                                                     'mismatch.',
                                                                'B': 'Shares ischemic '
                                                                     'pressure '
                                                                     'language and '
                                                                     'coronary '
                                                                     'context, but '
                                                                     'prolonged rest '
                                                                     'pain with '
                                                                     'diaphoresis '
                                                                     'indicates '
                                                                     'ACS/infarction '
                                                                     'physiology, not '
                                                                     'typical demand '
                                                                     'angina.',
                                                                'C': 'Palpation-reproduced '
                                                                     'focal pain is '
                                                                     'musculoskeletal '
                                                                     'chest-wall pain, '
                                                                     'not myocardial '
                                                                     'ischemia.',
                                                                'D': 'Isolated '
                                                                     'antacid-responsive '
                                                                     'epigastric '
                                                                     'burning '
                                                                     'indicates '
                                                                     'acid-related '
                                                                     'dyspepsia rather '
                                                                     'than coronary '
                                                                     'ischemia.'}},
                                       {'question': 'Aspirin given immediately in ACS '
                                                    'primarily reduces further '
                                                    'coronary thrombosis by which '
                                                    'platelet mechanism?',
                                        'options': ['A) Enhancement of endothelial '
                                                    'nitric-oxide–mediated '
                                                    'vasodilation',
                                                    'B) Irreversible acetylation of '
                                                    'platelet COX-1 blocking '
                                                    'thromboxane A2 synthesis',
                                                    'C) Direct cleavage of fibrin '
                                                    'within an organized thrombus',
                                                    'D) Irreversible P2Y12 '
                                                    'ADP-receptor blockade reducing '
                                                    'amplification of platelet '
                                                    'aggregation'],
                                        'answer': 'B) Irreversible acetylation of '
                                                  'platelet COX-1 blocking thromboxane '
                                                  'A2 synthesis',
                                        'explanation': 'Aspirin permanently acetylates '
                                                       'platelet COX-1, suppressing '
                                                       'thromboxane A2 and limiting '
                                                       'aggregation for the platelet '
                                                       'lifespan—foundational early '
                                                       'ACS therapy. P2Y12 inhibitors '
                                                       'also antiplatelet but via a '
                                                       'different receptor pathway. '
                                                       'Vasodilation and fibrinolysis '
                                                       'are distinct drug classes.',
                                        'choice_explanations': {'A': 'NO-mediated '
                                                                     'coronary '
                                                                     'dilation is a '
                                                                     'nitrate effect, '
                                                                     'not aspirin’s '
                                                                     'antiplatelet '
                                                                     'action.',
                                                                'B': 'Aspirin’s ACS '
                                                                     'benefit is '
                                                                     'irreversible '
                                                                     'COX-1 '
                                                                     'acetylation that '
                                                                     'cuts thromboxane '
                                                                     'A2–driven '
                                                                     'aggregation.',
                                                                'C': 'Fibrinolysis '
                                                                     'dissolves fibrin '
                                                                     'clot; aspirin '
                                                                     'does not '
                                                                     'enzymatically '
                                                                     'lyse thrombus.',
                                                                'D': 'P2Y12 blockade '
                                                                     'is also '
                                                                     'antiplatelet and '
                                                                     'used in ACS, but '
                                                                     'it is not '
                                                                     'aspirin’s '
                                                                     'mechanism; the '
                                                                     'stem asks '
                                                                     'specifically for '
                                                                     'aspirin.'}},
                                       {'question': 'A crescendo–decrescendo systolic '
                                                    'murmur radiating to the carotids '
                                                    'is most consistent with stenosis '
                                                    'of which valve?',
                                        'options': ['A) Aortic regurgitation heard as '
                                                    'an early diastolic decrescendo at '
                                                    'the left sternal border',
                                                    'B) Hypertrophic obstructive '
                                                    'cardiomyopathy with dynamic '
                                                    'left-ventricular outflow tract '
                                                    'obstruction',
                                                    'C) Aortic valve stenosis with '
                                                    'fixed left-ventricular outflow '
                                                    'obstruction',
                                                    'D) Mitral regurgitation with a '
                                                    'holosystolic jet radiating to the '
                                                    'axilla'],
                                        'answer': 'C) Aortic valve stenosis with fixed '
                                                  'left-ventricular outflow '
                                                  'obstruction',
                                        'explanation': 'A harsh crescendo–decrescendo '
                                                       'systolic murmur radiating to '
                                                       'the carotids is classic for '
                                                       'aortic stenosis from fixed '
                                                       'outflow obstruction. HOCM can '
                                                       'mimic AS with a similar murmur '
                                                       'shape but is dynamic and often '
                                                       'louder with Valsalva/standing. '
                                                       'MR and AR have different '
                                                       'timing and radiation.',
                                        'choice_explanations': {'A': 'AR is diastolic, '
                                                                     'not a systolic '
                                                                     'crescendo–decrescendo '
                                                                     'ejection murmur.',
                                                                'B': 'HOCM also '
                                                                     'produces a '
                                                                     'systolic outflow '
                                                                     'murmur and is '
                                                                     'the main '
                                                                     'near-miss, but '
                                                                     'dynamic '
                                                                     'physiology and '
                                                                     'bedside '
                                                                     'maneuvers '
                                                                     'distinguish it '
                                                                     'from fixed '
                                                                     'valvular AS.',
                                                                'C': 'Carotid-radiating '
                                                                     'crescendo–decrescendo '
                                                                     'systolic murmur '
                                                                     'indicates fixed '
                                                                     'aortic valvular '
                                                                     'stenosis.',
                                                                'D': 'MR is '
                                                                     'holosystolic to '
                                                                     'the axilla, not '
                                                                     'a '
                                                                     'carotid-radiating '
                                                                     'ejection '
                                                                     'murmur.'}}],
                              'medium': [{'question': 'A 58-year-old with crushing '
                                                      'chest pain has ST elevation in '
                                                      'leads II, III, and aVF. Which '
                                                      'coronary territory is most '
                                                      'likely occluded?',
                                          'options': ['A) Dominant circumflex artery '
                                                      'causing inferior infarction '
                                                      'when it supplies the posterior '
                                                      'descending artery',
                                                      'B) Proximal left anterior '
                                                      'descending causing extensive '
                                                      'anterior/septal ST elevation',
                                                      'C) Isolated septal perforator '
                                                      'occlusion without inferior-lead '
                                                      'involvement',
                                                      'D) Right coronary artery '
                                                      'supplying the inferior wall'],
                                          'answer': 'D) Right coronary artery '
                                                    'supplying the inferior wall',
                                          'explanation': 'ST elevation in II, III, and '
                                                         'aVF localizes to the '
                                                         'inferior wall, usually the '
                                                         'RCA in a right-dominant '
                                                         'circulation. A dominant LCx '
                                                         'can also infarct the '
                                                         'inferior wall and is the key '
                                                         'anatomic near-miss, but RCA '
                                                         'remains the most common '
                                                         'culprit. LAD and pure septal '
                                                         'patterns do not produce '
                                                         'isolated inferior STE.',
                                          'choice_explanations': {'A': 'A dominant LCx '
                                                                       'can likewise '
                                                                       'cause inferior '
                                                                       'infarction, so '
                                                                       'anatomy '
                                                                       'overlaps; '
                                                                       'prevalence and '
                                                                       'classic '
                                                                       'teaching still '
                                                                       'favor RCA '
                                                                       'unless '
                                                                       'dominance is '
                                                                       'known '
                                                                       'otherwise.',
                                                                  'B': 'Proximal LAD '
                                                                       'produces '
                                                                       'anterior/septal '
                                                                       'STE, not the '
                                                                       'inferior triad '
                                                                       'alone.',
                                                                  'C': 'Septal '
                                                                       'perforators do '
                                                                       'not explain ST '
                                                                       'elevation '
                                                                       'confined to '
                                                                       'the inferior '
                                                                       'leads.',
                                                                  'D': 'Inferior STE '
                                                                       'in II/III/aVF '
                                                                       'most often '
                                                                       'reflects RCA '
                                                                       'occlusion of '
                                                                       'the inferior '
                                                                       'wall.'}},
                                         {'question': 'Which murmur is holosystolic '
                                                      'and typically radiates to the '
                                                      'left axilla?',
                                          'options': ['A) Mitral regurgitation from '
                                                      'systolic leakage into the left '
                                                      'atrium radiating to the axilla',
                                                      'B) Tricuspid regurgitation that '
                                                      'is holosystolic but intensifies '
                                                      'with inspiration',
                                                      'C) Aortic stenosis with a '
                                                      'crescendo–decrescendo murmur '
                                                      'radiating to the carotids',
                                                      'D) Mitral stenosis with an '
                                                      'opening snap and mid-diastolic '
                                                      'rumble'],
                                          'answer': 'A) Mitral regurgitation from '
                                                    'systolic leakage into the left '
                                                    'atrium radiating to the axilla',
                                          'explanation': 'Holosystolic murmur to the '
                                                         'axilla is classic mitral '
                                                         'regurgitation. Tricuspid '
                                                         'regurgitation is also '
                                                         'holosystolic and the main '
                                                         'timing near-miss, but it '
                                                         'increases with inspiration '
                                                         'and is louder at the lower '
                                                         'left sternal border. AS and '
                                                         'MS have different '
                                                         'timing/radiation.',
                                          'choice_explanations': {'A': 'Axilla-radiating '
                                                                       'holosystolic '
                                                                       'murmur '
                                                                       'indicates MR '
                                                                       'into the left '
                                                                       'atrium.',
                                                                  'B': 'TR shares '
                                                                       'holosystolic '
                                                                       'timing, so it '
                                                                       'is tempting, '
                                                                       'but '
                                                                       'inspiratory '
                                                                       'accentuation '
                                                                       'and '
                                                                       'right-sternal '
                                                                       'location '
                                                                       'distinguish it '
                                                                       'from axillary '
                                                                       'MR.',
                                                                  'C': 'AS is an '
                                                                       'ejection '
                                                                       'murmur to the '
                                                                       'carotids, not '
                                                                       'holosystolic '
                                                                       'to the axilla.',
                                                                  'D': 'MS is '
                                                                       'diastolic with '
                                                                       'an opening '
                                                                       'snap, not '
                                                                       'holosystolic.'}},
                                         {'question': 'For an awake patient with '
                                                      'typical angina at rest, which '
                                                      'first-line agent most rapidly '
                                                      'reduces preload and often '
                                                      'relieves symptoms?',
                                          'options': ['A) Routine fibrinolysis without '
                                                      'ECG confirmation of a '
                                                      'STEMI-equivalent',
                                                      'B) Sublingual nitroglycerin to '
                                                      'venodilate and lower wall '
                                                      'stress',
                                                      'C) Immediate high-dose IV '
                                                      'beta-blocker as the sole first '
                                                      'anti-ischemic step before '
                                                      'nitrates',
                                                      'D) Intravenous nitroglycerin '
                                                      'infusion for ongoing ischemic '
                                                      'pain after sublingual doses'],
                                          'answer': 'B) Sublingual nitroglycerin to '
                                                    'venodilate and lower wall stress',
                                          'explanation': 'In awake typical angina at '
                                                         'rest, rapid preload '
                                                         'reduction with sublingual '
                                                         'nitroglycerin often relieves '
                                                         'symptoms by lowering wall '
                                                         'stress. IV nitroglycerin is '
                                                         'related for persistent pain, '
                                                         'but the stem asks the rapid '
                                                         'first-line agent. Blind '
                                                         'fibrinolysis and skipping '
                                                         'nitrates for empiric IV '
                                                         'beta-blockade alone are '
                                                         'incorrect initial concepts.',
                                          'choice_explanations': {'A': 'Fibrinolysis '
                                                                       'requires a '
                                                                       'STEMI/equivalent '
                                                                       'indication, '
                                                                       'not empiric '
                                                                       'use for '
                                                                       'undifferentiated '
                                                                       'rest angina.',
                                                                  'B': 'Sublingual '
                                                                       'nitroglycerin '
                                                                       'acts within '
                                                                       'minutes via '
                                                                       'venodilation '
                                                                       'to cut preload '
                                                                       'and ischemic '
                                                                       'pain.',
                                                                  'C': 'Beta-blockers '
                                                                       'reduce demand '
                                                                       'but are not '
                                                                       'the fastest '
                                                                       'preload-reducing '
                                                                       'first agent '
                                                                       'when nitrates '
                                                                       'are '
                                                                       'appropriate.',
                                                                  'D': 'IV '
                                                                       'nitroglycerin '
                                                                       'is '
                                                                       'mechanistically '
                                                                       'related and '
                                                                       'used if pain '
                                                                       'persists, but '
                                                                       'it is not the '
                                                                       'usual '
                                                                       'immediate '
                                                                       'first bedside '
                                                                       'dose for '
                                                                       'typical '
                                                                       'angina.'}}],
                              'hard': [{'question': 'A 64-year-old with inferior STEMI '
                                                    'becomes hypotensive after '
                                                    'nitrates. JVP is elevated, lungs '
                                                    'are clear, and the ECG shows ST '
                                                    'elevation in II, III, aVF with '
                                                    'reciprocal changes. Which '
                                                    'pathophysiology best explains '
                                                    'this response?',
                                        'options': ['A) Hypertrophic obstructive '
                                                    'cardiomyopathy with dynamic LVOT '
                                                    'obstruction',
                                                    'B) Inferior STEMI with '
                                                    'concomitant bradycardia/AV block '
                                                    'causing hypotension without RV '
                                                    'involvement',
                                                    'C) Right ventricular infarction '
                                                    'making cardiac output '
                                                    'preload-dependent',
                                                    'D) Isolated left-ventricular '
                                                    'failure with pulmonary edema '
                                                    'requiring further preload '
                                                    'reduction'],
                                        'answer': 'C) Right ventricular infarction '
                                                  'making cardiac output '
                                                  'preload-dependent',
                                        'explanation': 'Inferior STEMI plus clear '
                                                       'lungs, raised JVP, and '
                                                       'nitrate-triggered hypotension '
                                                       'strongly indicate RV '
                                                       'infarction, where output '
                                                       'depends on preload. Inferior '
                                                       'MI can also cause AV block and '
                                                       'hypotension (near-miss), but '
                                                       'elevated JVP with clear lungs '
                                                       'after nitrates points '
                                                       'specifically to RV '
                                                       'involvement.',
                                        'choice_explanations': {'A': 'HOCM is '
                                                                     'unrelated to '
                                                                     'acute inferior '
                                                                     'STEMI with this '
                                                                     'preload-collapse '
                                                                     'pattern.',
                                                                'B': 'Inferior '
                                                                     'MI–related '
                                                                     'bradyarrhythmia '
                                                                     'can also drop BP '
                                                                     'and shares the '
                                                                     'inferior STEMI '
                                                                     'setting, but '
                                                                     'raised JVP, '
                                                                     'clear lungs, and '
                                                                     'nitrate '
                                                                     'sensitivity are '
                                                                     'the RV-specific '
                                                                     'clues.',
                                                                'C': 'RV infarct makes '
                                                                     'the right heart '
                                                                     'preload-dependent; '
                                                                     'nitrates drop '
                                                                     'venous return '
                                                                     'and precipitate '
                                                                     'hypotension with '
                                                                     'clear lungs.',
                                                                'D': 'LV failure '
                                                                     'typically '
                                                                     'produces '
                                                                     'pulmonary '
                                                                     'congestion and '
                                                                     'is not explained '
                                                                     'by needing still '
                                                                     'more preload '
                                                                     'reduction '
                                                                     'here.'}},
                                       {'question': 'Among foundational HFrEF '
                                                    'therapies, which listed class has '
                                                    'consistent mortality reduction '
                                                    'when used as disease-modifying '
                                                    'treatment?',
                                        'options': ['A) Evidence-based beta-blockers '
                                                    'that also reduce mortality in '
                                                    'HFrEF when titrated',
                                                    'B) Loop diuretics titrated only '
                                                    'for congestion without '
                                                    'neurohormonal blockade',
                                                    'C) Short-acting nifedipine for '
                                                    'afterload reduction in systolic '
                                                    'heart failure',
                                                    'D) ACE inhibitors (or ARNI) that '
                                                    'interrupt maladaptive '
                                                    'renin–angiotensin signaling'],
                                        'answer': 'D) ACE inhibitors (or ARNI) that '
                                                  'interrupt maladaptive '
                                                  'renin–angiotensin signaling',
                                        'explanation': 'ACE inhibitors/ARNI are '
                                                       'foundational disease-modifying '
                                                       'HFrEF therapy with mortality '
                                                       'benefit via RAAS interruption. '
                                                       'Evidence-based beta-blockers '
                                                       'also reduce mortality and are '
                                                       'the closest rival class, but '
                                                       'the listed correct option is '
                                                       'ACEi/ARNI. Diuretics relieve '
                                                       'congestion without consistent '
                                                       'mortality reduction as primary '
                                                       'disease-modifiers; '
                                                       'short-acting nifedipine is '
                                                       'harmful.',
                                        'choice_explanations': {'A': 'Guideline-directed '
                                                                     'beta-blockers '
                                                                     'also cut '
                                                                     'mortality and '
                                                                     'can be confused '
                                                                     'as “the” answer, '
                                                                     'but among these '
                                                                     'options the '
                                                                     'ACEi/ARNI '
                                                                     'statement is the '
                                                                     'intended class.',
                                                                'B': 'Loop diuretics '
                                                                     'treat volume '
                                                                     'overload but are '
                                                                     'not primary '
                                                                     'mortality-reducing '
                                                                     'neurohormonal '
                                                                     'therapy.',
                                                                'C': 'Short-acting '
                                                                     'nifedipine is '
                                                                     'not appropriate '
                                                                     'disease-modifying '
                                                                     'HFrEF therapy.',
                                                                'D': 'ACEi/ARNI '
                                                                     'interrupt '
                                                                     'maladaptive RAAS '
                                                                     'signaling and '
                                                                     'improve survival '
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
                                                    'B) Activate the cath lab for '
                                                    'presumed NSTEMI with ongoing '
                                                    'ischemia but without treating new '
                                                    'LBBB as a STEMI equivalent',
                                                    'C) Wait 6 hours for serial '
                                                    'troponins before any reperfusion '
                                                    'decision',
                                                    'D) Discharge if pain eases '
                                                    'briefly with one dose of antacid'],
                                        'answer': 'A) Treat as a STEMI equivalent and '
                                                  'pursue urgent reperfusion pathways',
                                        'explanation': 'New LBBB with ongoing ischemic '
                                                       'pain is managed as a STEMI '
                                                       'equivalent with urgent '
                                                       'reperfusion. Ongoing NSTEMI '
                                                       'ischemia also warrants urgent '
                                                       'angiography and is the close '
                                                       'clinical rival, but classic '
                                                       'teaching for new LBBB plus '
                                                       'pain is STEMI-equivalent '
                                                       'pathways.',
                                        'choice_explanations': {'A': 'New LBBB with '
                                                                     'persistent '
                                                                     'ischemic '
                                                                     'symptoms is a '
                                                                     'STEMI equivalent '
                                                                     'needing '
                                                                     'immediate '
                                                                     'reperfusion '
                                                                     'strategy.',
                                                                'B': 'Ongoing ischemia '
                                                                     'in NSTEMI also '
                                                                     'needs urgent '
                                                                     'invasive care, '
                                                                     'but the stem’s '
                                                                     'new LBBB cue '
                                                                     'specifically '
                                                                     'triggers '
                                                                     'STEMI-equivalent '
                                                                     'classification.',
                                                                'C': 'Delaying for '
                                                                     'troponin misses '
                                                                     'the '
                                                                     'time-critical '
                                                                     'reperfusion '
                                                                     'window.',
                                                                'D': 'Antacid response '
                                                                     'does not exclude '
                                                                     'ACS and must not '
                                                                     'drive '
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
                                           'options': ['A) Uncomplicated panic attack '
                                                       'with hyperventilation '
                                                       'alkalosis',
                                                       'B) Acute aortic syndrome (type '
                                                       'A dissection) involving '
                                                       'coronary ostia or aortic '
                                                       'regurgitation',
                                                       'C) Isolated community-acquired '
                                                       'pneumonia explaining unequal '
                                                       'arm pressures',
                                                       'D) Acute coronary syndrome '
                                                       'from plaque rupture presenting '
                                                       'with tearing pain and mild '
                                                       'troponin rise'],
                                           'answer': 'B) Acute aortic syndrome (type A '
                                                     'dissection) involving coronary '
                                                     'ostia or aortic regurgitation',
                                           'explanation': 'Tearing interscapular pain, '
                                                          'pulse deficit/unequal arm '
                                                          'BPs, and flash edema with '
                                                          'nonspecific ECG changes '
                                                          'mandate excluding type A '
                                                          'dissection before full ACS '
                                                          'antithrombotics/cath alone. '
                                                          'True ACS can overlap and is '
                                                          'the dangerous near-miss. '
                                                          'Panic and pneumonia do not '
                                                          'explain this vascular '
                                                          'constellation.',
                                           'choice_explanations': {'A': 'Panic does '
                                                                        'not produce '
                                                                        'pulse '
                                                                        'deficits, '
                                                                        'flash '
                                                                        'pulmonary '
                                                                        'edema, or '
                                                                        'this pain '
                                                                        'pattern.',
                                                                   'B': 'Type A '
                                                                        'dissection '
                                                                        'can mimic ACS '
                                                                        'via ostial '
                                                                        'compromise or '
                                                                        'acute AR and '
                                                                        'must be '
                                                                        'excluded when '
                                                                        'pulse '
                                                                        'deficits and '
                                                                        'tearing pain '
                                                                        'dominate.',
                                                                   'C': 'Pneumonia '
                                                                        'does not '
                                                                        'cause acute '
                                                                        'unequal arm '
                                                                        'blood '
                                                                        'pressures or '
                                                                        'tearing '
                                                                        'aortic pain.',
                                                                   'D': 'ACS shares '
                                                                        'chest pain '
                                                                        'and troponin '
                                                                        'leak, '
                                                                        'creating real '
                                                                        'overlap, but '
                                                                        'unequal arm '
                                                                        'pressures and '
                                                                        'tearing '
                                                                        'interscapular '
                                                                        'pain are '
                                                                        'dissection '
                                                                        'red flags '
                                                                        'that change '
                                                                        'the '
                                                                        'pathway.'}},
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
                                           'options': ['A) Acute massive PE treated '
                                                       'empirically with bedside '
                                                       'full-dose thrombolysis alone',
                                                       'B) Postcardiotomy bleeding '
                                                       'with hypovolemic shock from '
                                                       'chest-tube hemorrhage without '
                                                       'pericardial constraint',
                                                       'C) Cardiac tamponade '
                                                       'physiology—urgent surgical '
                                                       'exploration rather than '
                                                       'waiting for perfect imaging',
                                                       'D) Primary distributive septic '
                                                       'shock; start broad '
                                                       'vasopressors without '
                                                       'considering mechanical '
                                                       'obstruction'],
                                           'answer': 'C) Cardiac tamponade '
                                                     'physiology—urgent surgical '
                                                     'exploration rather than waiting '
                                                     'for perfect imaging',
                                           'explanation': 'Rising CVP, muffled sounds, '
                                                          'equalization, oliguria, and '
                                                          'sudden fall in chest-tube '
                                                          'output after cardiac '
                                                          'surgery indicate tamponade '
                                                          'needing urgent exploration. '
                                                          'Free-bleeding hypovolemia '
                                                          'is the main postoperative '
                                                          'rival but usually shows '
                                                          'high tube output and low '
                                                          'filling pressures.',
                                           'choice_explanations': {'A': 'Empiric '
                                                                        'thrombolysis '
                                                                        'for assumed '
                                                                        'PE is '
                                                                        'dangerous '
                                                                        'without '
                                                                        'evaluation '
                                                                        'and ignores '
                                                                        'tamponade '
                                                                        'clues.',
                                                                   'B': 'Postop '
                                                                        'hemorrhage '
                                                                        'can also '
                                                                        'cause shock '
                                                                        'and shares '
                                                                        'the surgical '
                                                                        'setting, but '
                                                                        'high—not '
                                                                        'falling—tube '
                                                                        'output and '
                                                                        'low preload '
                                                                        'point to '
                                                                        'hypovolemia '
                                                                        'rather than '
                                                                        'pericardial '
                                                                        'constraint.',
                                                                   'C': 'Equalized '
                                                                        'diastolic '
                                                                        'pressures, '
                                                                        'rising CVP, '
                                                                        'and falling '
                                                                        'tube output '
                                                                        'after surgery '
                                                                        'indicate '
                                                                        'tamponade '
                                                                        'needing '
                                                                        'immediate '
                                                                        'surgical '
                                                                        'relief.',
                                                                   'D': 'Distributive '
                                                                        'sepsis lacks '
                                                                        'this '
                                                                        'equalization/obstructive '
                                                                        'pattern as '
                                                                        'the primary '
                                                                        'explanation.'}},
                                          {'question': 'A 28-year-old with known WPW '
                                                       'presents with irregular very '
                                                       'rapid wide-complex tachycardia '
                                                       'and hypotension (BP 78/40). '
                                                       'Which therapy is most '
                                                       'appropriate, and which class '
                                                       'must be avoided?',
                                           'options': ['A) IV ibutilide for '
                                                       'pre-excited AF in a selected '
                                                       'hemodynamically stable patient '
                                                       'under expert monitoring',
                                                       'B) IV metoprolol to slow AV '
                                                       'nodal conduction and protect '
                                                       'the ventricle',
                                                       'C) IV digoxin to increase '
                                                       'vagal tone at the AV node',
                                                       'D) Immediate synchronized '
                                                       'cardioversion (if unstable) or '
                                                       'IV procainamide; avoid '
                                                       'AV-nodal blockers'],
                                           'answer': 'D) Immediate synchronized '
                                                     'cardioversion (if unstable) or '
                                                     'IV procainamide; avoid AV-nodal '
                                                     'blockers',
                                           'explanation': 'Irregular very rapid '
                                                          'wide-complex tachycardia in '
                                                          'WPW is pre-excited AF; if '
                                                          'unstable, cardiovert. '
                                                          'Procainamide may be used '
                                                          'when appropriate; AV-nodal '
                                                          'blockers are '
                                                          'contraindicated. Other '
                                                          'expert antiarrhythmics can '
                                                          'be related near-misses but '
                                                          'do not replace '
                                                          'cardioversion in '
                                                          'hypotension.',
                                           'choice_explanations': {'A': 'Ibutilide may '
                                                                        'be used in '
                                                                        'selected '
                                                                        'stable '
                                                                        'pre-excited '
                                                                        'AF under '
                                                                        'expert care, '
                                                                        'but with BP '
                                                                        '78/40 the '
                                                                        'priority is '
                                                                        'synchronized '
                                                                        'cardioversion.',
                                                                   'B': 'Metoprolol '
                                                                        'blocks the AV '
                                                                        'node and can '
                                                                        'accelerate '
                                                                        'ventricular '
                                                                        'response over '
                                                                        'the accessory '
                                                                        'pathway.',
                                                                   'C': 'Digoxin '
                                                                        'similarly '
                                                                        'enhances '
                                                                        'accessory-pathway '
                                                                        'conduction '
                                                                        'risk in WPW '
                                                                        'AF and is '
                                                                        'contraindicated.',
                                                                   'D': 'Unstable '
                                                                        'pre-excited '
                                                                        'AF needs '
                                                                        'immediate '
                                                                        'cardioversion; '
                                                                        'procainamide '
                                                                        'is preferred '
                                                                        'pharmacologic '
                                                                        'therapy—avoid '
                                                                        'AV nodal '
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
                                                       'B) Direct pupillary light '
                                                       'reflex testing in each eye '
                                                       'without side-to-side '
                                                       'comparison',
                                                       'C) Measuring intraocular '
                                                       'pressure with digital '
                                                       'palpation alone',
                                                       'D) Cover–uncover test for '
                                                       'latent phoria only'],
                                           'answer': 'A) Swinging flashlight test '
                                                     'comparing consensual responses '
                                                     'between eyes',
                                           'explanation': 'RAPD is demonstrated by the '
                                                          'swinging flashlight test, '
                                                          'which compares relative '
                                                          'afferent input between eyes '
                                                          'via consensual responses. '
                                                          'Testing each pupil’s direct '
                                                          'reflex separately can miss '
                                                          'a relative difference and '
                                                          'is the close near-miss. IOP '
                                                          'palpation and cover testing '
                                                          'assess other functions.',
                                           'choice_explanations': {'A': 'The swinging '
                                                                        'flashlight '
                                                                        'maneuver '
                                                                        'detects RAPD '
                                                                        'by comparing '
                                                                        'consensual '
                                                                        'constriction '
                                                                        'when light '
                                                                        'alternates '
                                                                        'between eyes.',
                                                                   'B': 'Checking '
                                                                        'direct '
                                                                        'reflexes one '
                                                                        'eye at a time '
                                                                        'assesses '
                                                                        'afferent '
                                                                        'function '
                                                                        'incompletely; '
                                                                        'without '
                                                                        'comparison '
                                                                        'you can miss '
                                                                        'a relative '
                                                                        'afferent '
                                                                        'defect.',
                                                                   'C': 'Digital IOP '
                                                                        'palpation '
                                                                        'does not '
                                                                        'evaluate '
                                                                        'pupillary '
                                                                        'afferents.',
                                                                   'D': 'Cover–uncover '
                                                                        'testing '
                                                                        'evaluates '
                                                                        'ocular '
                                                                        'alignment/phoria, '
                                                                        'not RAPD.'}},
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
                                                       'D) Acute anterior uveitis with '
                                                       'painful red eye and '
                                                       'photophobia but a small/miotic '
                                                       'pupil'],
                                           'answer': 'B) Acute angle-closure glaucoma '
                                                     'with abrupt IOP rise',
                                           'explanation': 'Painful red eye with '
                                                          'mid-dilated poorly reactive '
                                                          'pupil and corneal edema is '
                                                          'classic acute '
                                                          'angle-closure. Anterior '
                                                          'uveitis is the main painful '
                                                          'red-eye rival but typically '
                                                          'has a small pupil and '
                                                          'ciliary flush without '
                                                          'corneal epithelial edema '
                                                          'from extreme IOP. '
                                                          'Conjunctivitis and '
                                                          'blepharitis lack this '
                                                          'pupil/IOP picture.',
                                           'choice_explanations': {'A': 'Viral '
                                                                        'conjunctivitis '
                                                                        'is '
                                                                        'uncomfortable '
                                                                        'but does not '
                                                                        'produce a '
                                                                        'mid-dilated '
                                                                        'poorly '
                                                                        'reactive '
                                                                        'pupil or '
                                                                        'corneal edema '
                                                                        'from IOP '
                                                                        'crisis.',
                                                                   'B': 'Mid-dilated '
                                                                        'fixed pupil, '
                                                                        'corneal '
                                                                        'edema, and '
                                                                        'severe pain '
                                                                        'indicate '
                                                                        'acute '
                                                                        'angle-closure '
                                                                        'with abrupt '
                                                                        'IOP '
                                                                        'elevation.',
                                                                   'C': 'Blepharitis '
                                                                        'is '
                                                                        'eyelid-margin '
                                                                        'disease '
                                                                        'without acute '
                                                                        'IOP-driven '
                                                                        'corneal '
                                                                        'edema.',
                                                                   'D': 'Uveitis also '
                                                                        'causes '
                                                                        'painful red '
                                                                        'eye and is '
                                                                        'easily '
                                                                        'confused, but '
                                                                        'the pupil is '
                                                                        'usually '
                                                                        'miotic, not '
                                                                        'mid-dilated '
                                                                        'with corneal '
                                                                        'stromal edema '
                                                                        'from acute '
                                                                        'high IOP.'}},
                                          {'question': 'An isolated cranial nerve VI '
                                                       'palsy primarily impairs which '
                                                       'ocular movement?',
                                           'options': ['A) Depression of the eye in '
                                                       'adduction (superior oblique / '
                                                       'CN IV action)',
                                                       'B) Abduction of the eye plus '
                                                       'eyelid elevation and pupillary '
                                                       'constriction (complete CN III '
                                                       'functions)',
                                                       'C) Abduction of the eye '
                                                       '(lateral rectus function)',
                                                       'D) Elevation of the eye in '
                                                       'adduction (inferior oblique '
                                                       'action)'],
                                           'answer': 'C) Abduction of the eye (lateral '
                                                     'rectus function)',
                                           'explanation': 'CN VI innervates lateral '
                                                          'rectus and mediates '
                                                          'abduction. Complete CN III '
                                                          'palsy impairs most other '
                                                          'movements plus lid and '
                                                          'pupil and is the main '
                                                          'cranial-nerve near-miss, '
                                                          'but isolated CN VI does '
                                                          'not. Inferior oblique and '
                                                          'superior oblique are CN '
                                                          'III/IV actions.',
                                           'choice_explanations': {'A': 'Superior '
                                                                        'oblique '
                                                                        'depression-in-adduction '
                                                                        'is CN IV, not '
                                                                        'CN VI.',
                                                                   'B': 'CN III '
                                                                        'controls '
                                                                        'multiple '
                                                                        'extraocular '
                                                                        'muscles plus '
                                                                        'levator and '
                                                                        'pupil; '
                                                                        'students may '
                                                                        'lump '
                                                                        '“cranial-nerve '
                                                                        'palsy” '
                                                                        'together, but '
                                                                        'isolated CN '
                                                                        'VI does not '
                                                                        'include '
                                                                        'lid/pupil '
                                                                        'functions.',
                                                                   'C': 'CN VI palsy '
                                                                        'selectively '
                                                                        'weakens '
                                                                        'lateral '
                                                                        'rectus–mediated '
                                                                        'abduction.',
                                                                   'D': 'Inferior '
                                                                        'oblique '
                                                                        'elevation-in-adduction '
                                                                        'is CN III, '
                                                                        'not CN VI.'}}],
                                 'medium': [{'question': 'Microaneurysms of diabetic '
                                                         'retinopathy are best '
                                                         'appreciated clinically on '
                                                         'which examination?',
                                             'options': ['A) Fluorescein angiography '
                                                         'to map microaneurysm leakage '
                                                         'after retinopathy is already '
                                                         'seen',
                                                         'B) External inspection of '
                                                         'the eyelids only',
                                                         'C) Tonometry without '
                                                         'ophthalmoscopy',
                                                         'D) Dilated fundoscopic (or '
                                                         'fundus photograph) '
                                                         'examination of the retina'],
                                             'answer': 'D) Dilated fundoscopic (or '
                                                       'fundus photograph) examination '
                                                       'of the retina',
                                             'explanation': 'Microaneurysms are '
                                                            'retinal microvascular '
                                                            'lesions seen on dilated '
                                                            'fundus exam or fundus '
                                                            'photography. Fluorescein '
                                                            'angiography can highlight '
                                                            'them exquisitely and is a '
                                                            'related advanced tool, '
                                                            'but clinical first '
                                                            'appreciation is '
                                                            'fundoscopy/photography. '
                                                            'Eyelid inspection and '
                                                            'tonometry alone miss '
                                                            'retinal detail.',
                                             'choice_explanations': {'A': 'Fluorescein '
                                                                          'angiography '
                                                                          'also '
                                                                          'demonstrates '
                                                                          'microaneurysms '
                                                                          'and '
                                                                          'leakage, '
                                                                          'but it is '
                                                                          'adjunctive '
                                                                          'imaging '
                                                                          'after '
                                                                          'retinopathy '
                                                                          'is being '
                                                                          'evaluated—not '
                                                                          'the basic '
                                                                          'bedside '
                                                                          'exam the '
                                                                          'stem asks.',
                                                                     'B': 'Eyelid '
                                                                          'inspection '
                                                                          'cannot '
                                                                          'visualize '
                                                                          'retinal '
                                                                          'microaneurysms.',
                                                                     'C': 'Tonometry '
                                                                          'measures '
                                                                          'IOP and '
                                                                          'does not '
                                                                          'display '
                                                                          'retinal '
                                                                          'microaneurysms.',
                                                                     'D': 'Dilated '
                                                                          'fundus '
                                                                          'examination '
                                                                          'or '
                                                                          'photography '
                                                                          'is how '
                                                                          'microaneurysms '
                                                                          'are '
                                                                          'clinically '
                                                                          'appreciated.'}},
                                            {'question': 'Sudden monocular '
                                                         "'curtain-like' visual field "
                                                         'loss ascending or descending '
                                                         'is most concerning for which '
                                                         'process?',
                                             'options': ['A) Rhegmatogenous retinal '
                                                         'detachment separating '
                                                         'neurosensory retina from RPE',
                                                         'B) Amaurosis fugax from '
                                                         'transient embolic monocular '
                                                         'vision loss that fully '
                                                         'resolves',
                                                         'C) Presbyopia from '
                                                         'age-related lens stiffening',
                                                         'D) Chronic open-angle '
                                                         'glaucoma with painless '
                                                         'gradual field constriction '
                                                         'only'],
                                             'answer': 'A) Rhegmatogenous retinal '
                                                       'detachment separating '
                                                       'neurosensory retina from RPE',
                                             'explanation': 'Curtain-like progressive '
                                                            'field loss strongly '
                                                            'suggests retinal '
                                                            'detachment. Amaurosis '
                                                            'fugax is sudden monocular '
                                                            'loss that typically '
                                                            'resolves within minutes '
                                                            'and is the key vascular '
                                                            'near-miss. Presbyopia and '
                                                            'chronic glaucoma have '
                                                            'different tempos and '
                                                            'symptoms.',
                                             'choice_explanations': {'A': 'Ascending/descending '
                                                                          'curtain '
                                                                          'scotoma is '
                                                                          'classic for '
                                                                          'rhegmatogenous '
                                                                          'retinal '
                                                                          'detachment.',
                                                                     'B': 'Amaurosis '
                                                                          'fugax is '
                                                                          'also sudden '
                                                                          'monocular '
                                                                          'visual loss '
                                                                          'and easily '
                                                                          'confused, '
                                                                          'but it is '
                                                                          'transient '
                                                                          'ischemia '
                                                                          'that '
                                                                          'resolves, '
                                                                          'not a '
                                                                          'persistent '
                                                                          'curtain '
                                                                          'from '
                                                                          'retinal '
                                                                          'separation.',
                                                                     'C': 'Presbyopia '
                                                                          'causes '
                                                                          'near-blur '
                                                                          'with aging, '
                                                                          'not acute '
                                                                          'curtain '
                                                                          'field loss.',
                                                                     'D': 'Chronic '
                                                                          'open-angle '
                                                                          'glaucoma '
                                                                          'causes '
                                                                          'gradual '
                                                                          'peripheral '
                                                                          'constriction, '
                                                                          'not sudden '
                                                                          'curtain '
                                                                          'symptoms.'}},
                                            {'question': 'Compared with preseptal '
                                                         'cellulitis, which features '
                                                         'most raise concern for '
                                                         'orbital cellulitis requiring '
                                                         'urgent imaging and IV '
                                                         'therapy?',
                                             'options': ['A) Isolated conjunctival '
                                                         'follicles without orbital '
                                                         'signs',
                                                         'B) Proptosis, painful '
                                                         'ophthalmoplegia, and '
                                                         'possible afferent pupillary '
                                                         'defect or vision threat',
                                                         'C) Unilateral watery tearing '
                                                         'after allergen exposure only',
                                                         'D) Severe eyelid swelling '
                                                         'with fever but preserved '
                                                         'motility and no proptosis '
                                                         '(preseptal cellulitis)'],
                                             'answer': 'B) Proptosis, painful '
                                                       'ophthalmoplegia, and possible '
                                                       'afferent pupillary defect or '
                                                       'vision threat',
                                             'explanation': 'Orbital cellulitis '
                                                            'threatens vision with '
                                                            'proptosis, painful '
                                                            'limited motility, and '
                                                            'possible RAPD. Severe '
                                                            'preseptal cellulitis can '
                                                            'look dramatic with lid '
                                                            'swelling/fever and is the '
                                                            'main near-miss, but '
                                                            'preserved motility '
                                                            'without proptosis keeps '
                                                            'infection anterior to the '
                                                            'septum. Conjunctival and '
                                                            'allergic patterns lack '
                                                            'orbital signs.',
                                             'choice_explanations': {'A': 'Conjunctival '
                                                                          'follicles '
                                                                          'alone '
                                                                          'indicate '
                                                                          'conjunctivitis, '
                                                                          'not orbital '
                                                                          'invasion.',
                                                                     'B': 'Proptosis, '
                                                                          'painful '
                                                                          'ophthalmoplegia, '
                                                                          'and '
                                                                          'vision/RAPD '
                                                                          'threat '
                                                                          'distinguish '
                                                                          'orbital '
                                                                          'cellulitis '
                                                                          'needing '
                                                                          'imaging and '
                                                                          'IV therapy.',
                                                                     'C': 'Allergic '
                                                                          'tearing/chemosis '
                                                                          'lacks '
                                                                          'infectious '
                                                                          'orbital '
                                                                          'findings.',
                                                                     'D': 'Preseptal '
                                                                          'cellulitis '
                                                                          'shares lid '
                                                                          'erythema/swelling/fever '
                                                                          'and can '
                                                                          'look '
                                                                          'severe, but '
                                                                          'absence of '
                                                                          'proptosis '
                                                                          'and painful '
                                                                          'ophthalmoplegia '
                                                                          'is the key '
                                                                          'separator.'}}],
                                 'hard': [{'question': 'A 42-year-old notes unilateral '
                                                       'dim vision. Pupils show a '
                                                       'clear RAPD, but early '
                                                       'fundoscopy looks nearly '
                                                       'normal. Color desaturation is '
                                                       'present in the affected eye. '
                                                       'Which localization is most '
                                                       'likely?',
                                           'options': ['A) Early cataract limited to '
                                                       'nuclear sclerosis without RAPD',
                                                       'B) Retrochiasmal visual '
                                                       'pathway lesion causing '
                                                       'homonymous field loss without '
                                                       'RAPD when chiasm/optic nerves '
                                                       'are spared',
                                                       'C) Optic neuropathy (e.g., '
                                                       'optic neuritis) affecting '
                                                       'afferent conduction',
                                                       'D) Uncorrected refractive '
                                                       'error alone without neural '
                                                       'pathway disease'],
                                           'answer': 'C) Optic neuropathy (e.g., optic '
                                                     'neuritis) affecting afferent '
                                                     'conduction',
                                           'explanation': 'Unilateral dim vision with '
                                                          'RAPD and color desaturation '
                                                          'despite a nearly normal '
                                                          'early fundus localizes to '
                                                          'optic nerve. Retrochiasmal '
                                                          'lesions cause field defects '
                                                          'but typically not a '
                                                          'unilateral RAPD if both '
                                                          'optic nerves are '
                                                          'intact—students confuse '
                                                          '“afferent pathway” broadly. '
                                                          'Refractive error and '
                                                          'cataract do not cause RAPD.',
                                           'choice_explanations': {'A': 'Cataract may '
                                                                        'dim vision '
                                                                        'but does not '
                                                                        'produce RAPD.',
                                                                   'B': 'Retrochiasmal '
                                                                        'disease also '
                                                                        'impairs '
                                                                        'vision and is '
                                                                        'neurologically '
                                                                        'adjacent, but '
                                                                        'a clear '
                                                                        'unilateral '
                                                                        'RAPD points '
                                                                        'to optic '
                                                                        'nerve (or '
                                                                        'severe '
                                                                        'asymmetric '
                                                                        'retinal) '
                                                                        'disease '
                                                                        'rather than '
                                                                        'pure '
                                                                        'post-chiasmal '
                                                                        'localization.',
                                                                   'C': 'RAPD plus '
                                                                        'color '
                                                                        'desaturation '
                                                                        'with '
                                                                        'relatively '
                                                                        'normal early '
                                                                        'fundus '
                                                                        'indicates '
                                                                        'optic '
                                                                        'neuropathy.',
                                                                   'D': 'Refractive '
                                                                        'error blurs '
                                                                        'vision '
                                                                        'without RAPD '
                                                                        'or color '
                                                                        'desaturation '
                                                                        'of neural '
                                                                        'type.'}},
                                          {'question': 'A 55-year-old develops acute '
                                                       'painful complete third-nerve '
                                                       'palsy with a dilated pupil '
                                                       'poorly reactive to light. '
                                                       'Which diagnosis must be '
                                                       'excluded first?',
                                           'options': ['A) Isolated diabetic '
                                                       'microvascular CN III palsy, '
                                                       'which is typically '
                                                       'pupil-sparing',
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
                                           'explanation': 'Painful complete CN III '
                                                          'palsy with pupil '
                                                          'involvement is a PCOM '
                                                          'aneurysm emergency until '
                                                          'proven otherwise. Diabetic '
                                                          'microvascular CN III is the '
                                                          'classic near-miss but is '
                                                          'usually pupil-sparing. '
                                                          'Myasthenia spares pupils; '
                                                          'Horner causes miosis.',
                                           'choice_explanations': {'A': 'Diabetic '
                                                                        'ischemic CN '
                                                                        'III also '
                                                                        'causes acute '
                                                                        'oculomotor '
                                                                        'palsy and is '
                                                                        'the main '
                                                                        'differential, '
                                                                        'but pupil '
                                                                        'sparing is '
                                                                        'typical—pupillary '
                                                                        'involvement '
                                                                        'pushes toward '
                                                                        'compression.',
                                                                   'B': 'Myasthenia '
                                                                        'can cause '
                                                                        'ptosis/ophthalmoplegia '
                                                                        'but pupils '
                                                                        'remain '
                                                                        'normal.',
                                                                   'C': 'Horner '
                                                                        'syndrome '
                                                                        'produces '
                                                                        'ptosis with '
                                                                        'miosis, not a '
                                                                        'dilated '
                                                                        'poorly '
                                                                        'reactive '
                                                                        'pupil.',
                                                                   'D': 'Pupil-involving '
                                                                        'painful CN '
                                                                        'III palsy '
                                                                        'requires '
                                                                        'urgent '
                                                                        'exclusion of '
                                                                        'compressive '
                                                                        'PCOM '
                                                                        'aneurysm.'}},
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
                                                       'B) Central retinal vein '
                                                       'occlusion with sudden '
                                                       'monocular vision loss and a '
                                                       '“blood-and-thunder” fundus',
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
                                           'explanation': 'CRAO presents with sudden '
                                                          'painless monocular loss, '
                                                          'RAPD, pale retina, and '
                                                          'cherry-red macula. CRVO '
                                                          'also causes sudden '
                                                          'monocular loss and is the '
                                                          'key retinal vascular '
                                                          'near-miss but shows retinal '
                                                          'hemorrhages, not a '
                                                          'cherry-red spot with '
                                                          'arterial pallor. Uveitis '
                                                          'and allergy differ '
                                                          'entirely.',
                                           'choice_explanations': {'A': 'CRAO’s acute '
                                                                        'picture is '
                                                                        'painless '
                                                                        'monocular '
                                                                        'loss, RAPD, '
                                                                        'and '
                                                                        'cherry-red '
                                                                        'spot on a '
                                                                        'pale retina.',
                                                                   'B': 'CRVO likewise '
                                                                        'causes sudden '
                                                                        'monocular '
                                                                        'vision loss '
                                                                        'and can be '
                                                                        'confused as '
                                                                        '“retinal '
                                                                        'vascular '
                                                                        'occlusion,” '
                                                                        'but fundus '
                                                                        'findings are '
                                                                        'hemorrhagic '
                                                                        '“blood and '
                                                                        'thunder,” not '
                                                                        'arterial '
                                                                        'pallor with '
                                                                        'cherry-red '
                                                                        'spot.',
                                                                   'C': 'Uveitis is '
                                                                        'painful with '
                                                                        'ciliary '
                                                                        'flush, not '
                                                                        'this fundus '
                                                                        'pattern.',
                                                                   'D': 'Allergic '
                                                                        'conjunctivitis '
                                                                        'causes '
                                                                        'itch/watering '
                                                                        'without RAPD '
                                                                        'or cherry-red '
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
                                              'options': ['A) Give topical ocular '
                                                          'hypotensive drops alone for '
                                                          'presumed acute glaucoma',
                                                          'B) Start high-dose systemic '
                                                          'corticosteroids '
                                                          'immediately, then arrange '
                                                          'urgent temporal artery '
                                                          'biopsy without delaying '
                                                          'therapy',
                                                          'C) Perform immediate '
                                                          'contralateral prophylactic '
                                                          'enucleation to prevent '
                                                          'spread',
                                                          'D) Arrange temporal artery '
                                                          'biopsy first and start '
                                                          'steroids only after '
                                                          'histologic confirmation'],
                                              'answer': 'B) Start high-dose systemic '
                                                        'corticosteroids immediately, '
                                                        'then arrange urgent temporal '
                                                        'artery biopsy without '
                                                        'delaying therapy',
                                              'explanation': 'Giant-cell arteritis '
                                                             'with acute arteritic '
                                                             'ischemic optic '
                                                             'neuropathy needs '
                                                             'immediate high-dose '
                                                             'steroids to protect the '
                                                             'fellow eye; biopsy '
                                                             'confirms but must not '
                                                             'delay therapy. Waiting '
                                                             'for histology is the '
                                                             'dangerous near-miss. '
                                                             'Glaucoma drops and '
                                                             'enucleation are wrong.',
                                              'choice_explanations': {'A': 'Topical '
                                                                           'IOP drugs '
                                                                           'do not '
                                                                           'treat '
                                                                           'arteritic '
                                                                           'ischemic '
                                                                           'optic '
                                                                           'neuropathy '
                                                                           'from GCA.',
                                                                      'B': 'Immediate '
                                                                           'systemic '
                                                                           'steroids '
                                                                           'protect '
                                                                           'contralateral '
                                                                           'vision; '
                                                                           'biopsy is '
                                                                           'urgent but '
                                                                           'never '
                                                                           'delays '
                                                                           'steroids.',
                                                                      'C': 'Contralateral '
                                                                           'enucleation '
                                                                           'is not a '
                                                                           'preventive '
                                                                           'strategy '
                                                                           'for GCA.',
                                                                      'D': 'Biopsy is '
                                                                           'important '
                                                                           'and '
                                                                           'tempting '
                                                                           'to '
                                                                           '“confirm '
                                                                           'first,” '
                                                                           'but '
                                                                           'waiting '
                                                                           'for '
                                                                           'pathology '
                                                                           'risks '
                                                                           'irreversible '
                                                                           'fellow-eye '
                                                                           'blindness—the '
                                                                           'subtle '
                                                                           'timing '
                                                                           'error.'}},
                                             {'question': 'A laboratory worker '
                                                          'splashes a strong alkali '
                                                          'into both eyes. He arrives '
                                                          'holding his lids shut in '
                                                          'pain. Which action takes '
                                                          'absolute priority over '
                                                          'other interventions?',
                                              'options': ['A) Patch both eyes tightly '
                                                          'and discharge with '
                                                          'outpatient ophthalmology in '
                                                          '48 hours',
                                                          'B) Instill topical '
                                                          'anesthetic to facilitate '
                                                          'lid opening, then irrigate '
                                                          'continuously until pH '
                                                          'normalizes',
                                                          'C) Begin copious irrigation '
                                                          'immediately and continue '
                                                          'until the conjunctival pH '
                                                          'normalizes',
                                                          'D) Obtain detailed pH '
                                                          'history and photograph the '
                                                          'injury before any '
                                                          'irrigation'],
                                              'answer': 'C) Begin copious irrigation '
                                                        'immediately and continue '
                                                        'until the conjunctival pH '
                                                        'normalizes',
                                              'explanation': 'Alkali eye injury: '
                                                             'immediate copious '
                                                             'irrigation until pH '
                                                             'normalizes is absolute '
                                                             'priority. Topical '
                                                             'anesthetic to allow lid '
                                                             'opening is often used to '
                                                             'enable irrigation and is '
                                                             'a close procedural '
                                                             'rival, but irrigation '
                                                             'itself—not anesthesia '
                                                             'alone—is the priority '
                                                             'action. Delaying for '
                                                             'photos or '
                                                             'patching/discharge is '
                                                             'harmful.',
                                              'choice_explanations': {'A': 'Patching '
                                                                           'and '
                                                                           'delayed '
                                                                           'outpatient '
                                                                           'review '
                                                                           'allow '
                                                                           'ongoing '
                                                                           'alkali '
                                                                           'saponification '
                                                                           'injury.',
                                                                      'B': 'Anesthetic '
                                                                           'drops help '
                                                                           'open lids '
                                                                           'so '
                                                                           'irrigation '
                                                                           'can '
                                                                           'proceed '
                                                                           'and may be '
                                                                           'done '
                                                                           'concurrently, '
                                                                           'but the '
                                                                           'stem’s '
                                                                           'absolute '
                                                                           'priority '
                                                                           'is '
                                                                           'irrigation '
                                                                           'to '
                                                                           'neutralize '
                                                                           'alkali—not '
                                                                           'anesthesia '
                                                                           'as the '
                                                                           'named '
                                                                           'priority.',
                                                                      'C': 'Immediate '
                                                                           'prolonged '
                                                                           'irrigation '
                                                                           'until '
                                                                           'conjunctival '
                                                                           'pH '
                                                                           'normalizes '
                                                                           'is the '
                                                                           'first and '
                                                                           'overriding '
                                                                           'step in '
                                                                           'chemical '
                                                                           'eye '
                                                                           'injury.',
                                                                      'D': 'History/photos '
                                                                           'must not '
                                                                           'delay '
                                                                           'irrigation.'}},
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
                                              'options': ['A) Exogenous postoperative '
                                                          'endophthalmitis after '
                                                          'recent intraocular surgery '
                                                          'with similar hypopyon and '
                                                          'vision loss',
                                                          'B) Simple allergic '
                                                          'conjunctivitis treated with '
                                                          'antihistamine drops alone',
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
                                              'explanation': 'Immunosuppression, '
                                                             'fever, hypopyon, and '
                                                             'severe vision loss '
                                                             'suggest endogenous '
                                                             'endophthalmitis from '
                                                             'hematogenous spread. '
                                                             'Exogenous '
                                                             'endophthalmitis looks '
                                                             'similarly catastrophic '
                                                             'intraocularly and is the '
                                                             'morphologic near-miss, '
                                                             'but the stem’s '
                                                             'chemotherapy/fever '
                                                             'context points to '
                                                             'endogenous seeding. '
                                                             'Allergy and migraine do '
                                                             'not fit.',
                                              'choice_explanations': {'A': 'Exogenous '
                                                                           'endophthalmitis '
                                                                           'shares '
                                                                           'hypopyon '
                                                                           'and acute '
                                                                           'vision '
                                                                           'loss, so '
                                                                           'intraocular '
                                                                           'findings '
                                                                           'overlap; '
                                                                           'recent '
                                                                           'surgery vs '
                                                                           'bloodstream '
                                                                           'source is '
                                                                           'the '
                                                                           'distinguishing '
                                                                           'context '
                                                                           'here.',
                                                                      'B': 'Allergic '
                                                                           'conjunctivitis '
                                                                           'lacks '
                                                                           'hypopyon, '
                                                                           'fever, and '
                                                                           'profound '
                                                                           'vision '
                                                                           'loss.',
                                                                      'C': 'Migraine '
                                                                           'aura does '
                                                                           'not '
                                                                           'produce '
                                                                           'hypopyon '
                                                                           'or a '
                                                                           'painful '
                                                                           'red eye '
                                                                           'with dense '
                                                                           'intraocular '
                                                                           'inflammation.',
                                                                      'D': 'Hematogenous '
                                                                           'seeding in '
                                                                           'a febrile '
                                                                           'immunocompromised '
                                                                           'host with '
                                                                           'hypopyon '
                                                                           'is '
                                                                           'endogenous '
                                                                           'endophthalmitis '
                                                                           'needing '
                                                                           'urgent '
                                                                           'systemic '
                                                                           'and '
                                                                           'ophthalmic '
                                                                           'care.'}}]},
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
                                                 'B) Calcium phosphate stones in '
                                                 'distal RTA or alkaline urine as '
                                                 'another calcium-based composition',
                                                 'C) Pure cystine from a transport '
                                                 'defect in every first stone',
                                                 'D) Struvite exclusively without '
                                                 'infection risk factors'],
                                     'answer': 'A) Calcium oxalate (often with some '
                                               'calcium phosphate)',
                                     'explanation': 'Most adult stones are calcium '
                                                    'oxalate (often mixed with some '
                                                    'calcium phosphate). Pure calcium '
                                                    'phosphate stones are related '
                                                    'calcium calculi and the '
                                                    'compositional near-miss, but '
                                                    'oxalate predominates overall. '
                                                    'Cystine and infection-struvite '
                                                    'are less common first-stone '
                                                    'compositions.',
                                     'choice_explanations': {'A': 'Calcium oxalate is '
                                                                  'the majority stone '
                                                                  'type in temperate '
                                                                  'adult populations.',
                                                             'B': 'Calcium phosphate '
                                                                  'stones are also '
                                                                  'calcium-based and '
                                                                  'can confuse '
                                                                  'students, but they '
                                                                  'are less common '
                                                                  'overall than '
                                                                  'oxalate-dominant '
                                                                  'calculi.',
                                                             'C': 'Cystine stones '
                                                                  'reflect a genetic '
                                                                  'transport defect '
                                                                  'and are uncommon as '
                                                                  'the default first '
                                                                  'stone.',
                                                             'D': 'Struvite forms in '
                                                                  'urease-infection '
                                                                  'settings, not as '
                                                                  'the usual first '
                                                                  'stone without those '
                                                                  'risks.'}},
                                    {'question': 'Severe colicky loin pain radiating '
                                                 'to the groin with restlessness is '
                                                 'most classic for which process?',
                                     'options': ['A) Chronic stable BPH without acute '
                                                 'obstruction',
                                                 'B) Ureteric colic from an '
                                                 'obstructing calculus',
                                                 'C) Stress urinary incontinence with '
                                                 'coughing',
                                                 'D) Pyelonephritis with flank pain '
                                                 'and fever from upper-tract '
                                                 'infection'],
                                     'answer': 'B) Ureteric colic from an obstructing '
                                               'calculus',
                                     'explanation': 'Severe colicky loin-to-groin pain '
                                                    'with restlessness is classic '
                                                    'ureteric colic. Acute '
                                                    'pyelonephritis also causes flank '
                                                    'pain and is the infectious '
                                                    'near-miss, but typically includes '
                                                    'fever/toxicity rather than '
                                                    'writhing colic alone. Stable BPH '
                                                    'and stress incontinence do not '
                                                    'produce this pain pattern.',
                                     'choice_explanations': {'A': 'Chronic BPH causes '
                                                                  'voiding symptoms, '
                                                                  'not acute colicky '
                                                                  'loin-to-groin pain.',
                                                             'B': 'Loin-to-groin colic '
                                                                  'with restlessness '
                                                                  'is the hallmark of '
                                                                  'an obstructing '
                                                                  'ureteric stone.',
                                                             'C': 'Stress incontinence '
                                                                  'is leakage with '
                                                                  'effort, not colic.',
                                                             'D': 'Pyelonephritis '
                                                                  'shares flank pain '
                                                                  'localization, so it '
                                                                  'is tempting, but '
                                                                  'high fever and '
                                                                  'systemic infection '
                                                                  'signs dominate over '
                                                                  'intermittent '
                                                                  'colicky '
                                                                  'restlessness.'}},
                                    {'question': 'For suspected urolithiasis in a '
                                                 'non-pregnant adult, which imaging '
                                                 'modality is usually preferred first '
                                                 'for high sensitivity?',
                                     'options': ['A) Immediate invasive retrograde '
                                                 'pyelography before any CT',
                                                 'B) Renal ultrasound first-line when '
                                                 'radiation avoidance is prioritized '
                                                 '(e.g., pregnancy) rather than '
                                                 'maximal sensitivity',
                                                 'C) Non-contrast CT of the kidneys, '
                                                 'ureters, and bladder',
                                                 'D) Plain abdominal radiograph alone '
                                                 'as definitive rule-out'],
                                     'answer': 'C) Non-contrast CT of the kidneys, '
                                               'ureters, and bladder',
                                     'explanation': 'Non-contrast CT KUB has the '
                                                    'highest sensitivity for '
                                                    'urolithiasis in most non-pregnant '
                                                    'adults. Ultrasound is a related '
                                                    'first imaging choice in '
                                                    'pregnancy/radiation-sensitive '
                                                    'settings and is the guideline '
                                                    'near-miss, but for the typical '
                                                    'non-pregnant adult CT is '
                                                    'preferred. Plain film and jumping '
                                                    'to RPG are inadequate/wrong first '
                                                    'steps.',
                                     'choice_explanations': {'A': 'Retrograde '
                                                                  'pyelography is '
                                                                  'invasive and not '
                                                                  'the initial '
                                                                  'diagnostic test.',
                                                             'B': 'Ultrasound is '
                                                                  'appropriate when '
                                                                  'avoiding radiation '
                                                                  'and can show '
                                                                  'hydronephrosis/stones, '
                                                                  'but it is less '
                                                                  'sensitive than CT '
                                                                  'for ureteric '
                                                                  'calculi in the '
                                                                  'standard adult '
                                                                  'pathway.',
                                                             'C': 'Non-contrast CT KUB '
                                                                  'is the usual '
                                                                  'highest-sensitivity '
                                                                  'first test for '
                                                                  'suspected stones in '
                                                                  'non-pregnant '
                                                                  'adults.',
                                                             'D': 'Plain radiographs '
                                                                  'miss many '
                                                                  'radiolucent/small '
                                                                  'stones and cannot '
                                                                  'definitively rule '
                                                                  'out '
                                                                  'urolithiasis.'}}],
                           'medium': [{'question': 'Painless gross hematuria in a '
                                                   '68-year-old long-term smoker most '
                                                   'urgently raises concern for which '
                                                   'diagnosis?',
                                       'options': ['A) Renal cell carcinoma presenting '
                                                   'with hematuria as another '
                                                   'genitourinary malignancy',
                                                   'B) Uncomplicated orthostatic '
                                                   'proteinuria in adolescents',
                                                   'C) Simple orthostatic hypotension '
                                                   'without urinary tract disease',
                                                   'D) Urothelial (bladder) carcinoma '
                                                   'until adequately investigated'],
                                       'answer': 'D) Urothelial (bladder) carcinoma '
                                                 'until adequately investigated',
                                       'explanation': 'Painless gross hematuria in an '
                                                      'older smoker is bladder '
                                                      'urothelial cancer until proven '
                                                      'otherwise. RCC can also present '
                                                      'with hematuria and is a related '
                                                      'GU malignancy near-miss, but '
                                                      'the classic urgent association '
                                                      'for painless gross hematuria is '
                                                      'bladder cancer needing '
                                                      'cystoscopic evaluation.',
                                       'choice_explanations': {'A': 'RCC is also a GU '
                                                                    'cancer that can '
                                                                    'bleed and thus '
                                                                    'overlaps '
                                                                    'conceptually, but '
                                                                    'painless gross '
                                                                    'hematuria’s first '
                                                                    'urgent '
                                                                    'association is '
                                                                    'urothelial '
                                                                    'carcinoma of the '
                                                                    'bladder.',
                                                               'B': 'Orthostatic '
                                                                    'proteinuria is a '
                                                                    'benign protein '
                                                                    'finding in '
                                                                    'adolescents, not '
                                                                    'gross hematuria '
                                                                    'workup.',
                                                               'C': 'Orthostatic '
                                                                    'hypotension is a '
                                                                    'blood-pressure '
                                                                    'phenomenon '
                                                                    'unrelated to '
                                                                    'hematuria '
                                                                    'etiology.',
                                                               'D': 'Painless gross '
                                                                    'hematuria in a '
                                                                    'long-term older '
                                                                    'smoker mandates '
                                                                    'workup for '
                                                                    'urothelial '
                                                                    'bladder '
                                                                    'carcinoma.'}},
                                      {'question': 'Fever, flank pain, and dysuria '
                                                   'with costovertebral angle '
                                                   'tenderness most likely represent '
                                                   'which infection level?',
                                       'options': ['A) Acute pyelonephritis involving '
                                                   'renal parenchyma',
                                                   'B) Acute cystitis confined to the '
                                                   'bladder without parenchymal '
                                                   'invasion',
                                                   'C) Asymptomatic bacteriuria '
                                                   'without tissue invasion',
                                                   'D) Stress urinary incontinence '
                                                   'without infection'],
                                       'answer': 'A) Acute pyelonephritis involving '
                                                 'renal parenchyma',
                                       'explanation': 'Fever, flank pain, dysuria, and '
                                                      'CVA tenderness indicate '
                                                      'pyelonephritis. Cystitis shares '
                                                      'dysuria/UTI symptoms and is the '
                                                      'lower-tract near-miss, but '
                                                      'fever and CVA tenderness imply '
                                                      'upper-tract parenchymal '
                                                      'infection. Asymptomatic '
                                                      'bacteriuria and incontinence '
                                                      'lack this syndrome.',
                                       'choice_explanations': {'A': 'Fever plus CVA '
                                                                    'tenderness with '
                                                                    'UTI symptoms '
                                                                    'indicates acute '
                                                                    'pyelonephritis.',
                                                               'B': 'Cystitis causes '
                                                                    'dysuria and '
                                                                    'frequency and is '
                                                                    'easily confused '
                                                                    'as “UTI,” but '
                                                                    'systemic fever '
                                                                    'and flank/CVA '
                                                                    'findings upgrade '
                                                                    'the infection to '
                                                                    'pyelonephritis.',
                                                               'C': 'Asymptomatic '
                                                                    'bacteriuria has '
                                                                    'organisms without '
                                                                    'invasive clinical '
                                                                    'illness.',
                                                               'D': 'Stress '
                                                                    'incontinence is '
                                                                    'not an infectious '
                                                                    'upper-tract '
                                                                    'process.'}},
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
                                                   'D) Immediate Doppler ultrasound to '
                                                   'assess blood flow when it will not '
                                                   'delay operative exploration'],
                                       'answer': 'B) Urgent urologic exploration—do '
                                                 'not delay for perfect imaging if '
                                                 'clinical suspicion is high',
                                       'explanation': 'Suspected torsion is a surgical '
                                                      'emergency: explore promptly. '
                                                      'Doppler ultrasound is a useful '
                                                      'adjunct if immediately '
                                                      'available without delay and is '
                                                      'the close rival, but imaging '
                                                      'must never postpone surgery '
                                                      'when suspicion is high. '
                                                      'Observation or antibiotics '
                                                      'alone risk testicular loss.',
                                       'choice_explanations': {'A': 'Waiting 48 hours '
                                                                    'allows '
                                                                    'irreversible '
                                                                    'ischemia.',
                                                               'B': 'High clinical '
                                                                    'suspicion for '
                                                                    'torsion mandates '
                                                                    'urgent '
                                                                    'exploration '
                                                                    'without waiting '
                                                                    'for perfect '
                                                                    'imaging.',
                                                               'C': 'Antibiotics treat '
                                                                    'infection (e.g., '
                                                                    'epididymitis), '
                                                                    'not ischemic '
                                                                    'torsion.',
                                                               'D': 'Doppler US can '
                                                                    'support the '
                                                                    'diagnosis and is '
                                                                    'often obtained, '
                                                                    'but the critical '
                                                                    'teaching point is '
                                                                    'that imaging must '
                                                                    'not delay '
                                                                    'definitive '
                                                                    'surgical '
                                                                    'detorsion.'}}],
                           'hard': [{'question': 'A patient with an obstructing '
                                                 'ureteric stone develops high fever, '
                                                 'hypotension, and leukocytosis. Which '
                                                 'management priority is correct?',
                                     'options': ['A) Immediate nephrectomy as the '
                                                 'first procedure in all such cases',
                                                 'B) IV antibiotics alone while '
                                                 'scheduling elective stone treatment '
                                                 'after fever resolves',
                                                 'C) Urgent decompression of the '
                                                 'infected obstructed kidney plus '
                                                 'antibiotics',
                                                 'D) Alpha-blocker trial alone without '
                                                 'source control'],
                                     'answer': 'C) Urgent decompression of the '
                                               'infected obstructed kidney plus '
                                               'antibiotics',
                                     'explanation': 'Infected obstructed kidney is a '
                                                    'urologic emergency requiring '
                                                    'source control '
                                                    '(stent/nephrostomy) plus '
                                                    'antibiotics. Antibiotics without '
                                                    'decompression are the dangerous '
                                                    'near-miss. Alpha-blockers and '
                                                    'routine first-line nephrectomy '
                                                    'are wrong.',
                                     'choice_explanations': {'A': 'Nephrectomy is not '
                                                                  'the initial '
                                                                  'decompression '
                                                                  'strategy in typical '
                                                                  'cases.',
                                                             'B': 'IV antibiotics are '
                                                                  'necessary and '
                                                                  'tempting as '
                                                                  '“enough,” but '
                                                                  'without relieving '
                                                                  'obstruction, source '
                                                                  'control fails and '
                                                                  'sepsis can '
                                                                  'progress—the subtle '
                                                                  'critical gap.',
                                                             'C': 'Obstructive '
                                                                  'pyelonephritis/sepsis '
                                                                  'needs urgent '
                                                                  'drainage plus '
                                                                  'antibiotics—antibiotics '
                                                                  'alone are '
                                                                  'insufficient.',
                                                             'D': 'Medical expulsive '
                                                                  'therapy does not '
                                                                  'treat infected '
                                                                  'obstruction.'}},
                                    {'question': 'After relief of bilateral chronic '
                                                 'urinary obstruction, a patient '
                                                 'produces large volumes of urine with '
                                                 'rising creatinine that then '
                                                 'improves. Which phenomenon is '
                                                 'occurring?',
                                     'options': ['A) Nephrogenic diabetes insipidus '
                                                 'with large dilute urine unrelated to '
                                                 'recent obstruction relief',
                                                 'B) SIADH with inappropriate '
                                                 'free-water retention',
                                                 'C) Acute urinary retention recurring '
                                                 'immediately',
                                                 'D) Post-obstructive diuresis from '
                                                 'excretion of retained solute and '
                                                 'water'],
                                     'answer': 'D) Post-obstructive diuresis from '
                                               'excretion of retained solute and water',
                                     'explanation': 'After relief of bilateral chronic '
                                                    'obstruction, large urine output '
                                                    'from excreted retained '
                                                    'solute/water is post-obstructive '
                                                    'diuresis. Nephrogenic DI also '
                                                    'causes polyuria and is the '
                                                    'physiologic near-miss, but the '
                                                    'temporal link to obstruction '
                                                    'relief defines post-obstructive '
                                                    'diuresis. SIADH causes '
                                                    'oliguria/hyponatremia; recurrent '
                                                    'retention is opposite.',
                                     'choice_explanations': {'A': 'Nephrogenic DI '
                                                                  'produces large '
                                                                  'urine volumes too, '
                                                                  'so polyuria '
                                                                  'overlaps, but the '
                                                                  'setting immediately '
                                                                  'after obstruction '
                                                                  'relief is the '
                                                                  'distinguishing cue.',
                                                             'B': 'SIADH retains free '
                                                                  'water rather than '
                                                                  'causing large '
                                                                  'post-relief '
                                                                  'diuresis.',
                                                             'C': 'Recurrent retention '
                                                                  'means inability to '
                                                                  'void, not high '
                                                                  'urine output.',
                                                             'D': 'Polyuria after '
                                                                  'relieving chronic '
                                                                  'bilateral '
                                                                  'obstruction is '
                                                                  'post-obstructive '
                                                                  'diuresis of '
                                                                  'retained salt and '
                                                                  'water.'}},
                                    {'question': 'A 15-year-old has sudden severe '
                                                 'testicular pain; the testis is '
                                                 'high-riding and the cremasteric '
                                                 'reflex is absent. Which diagnosis is '
                                                 'most likely?',
                                     'options': ['A) Spermatic cord torsion until '
                                                 'proven otherwise',
                                                 'B) Acute epididymitis with severe '
                                                 'scrotal pain and inflammatory '
                                                 'swelling',
                                                 'C) Uncomplicated hydrocele without '
                                                 'ischemia',
                                                 'D) Varicocele that enlarges only on '
                                                 'standing'],
                                     'answer': 'A) Spermatic cord torsion until proven '
                                               'otherwise',
                                     'explanation': 'Sudden severe pain, high-riding '
                                                    'testis, and absent cremasteric '
                                                    'reflex are torsion until proven '
                                                    'otherwise. Epididymitis is the '
                                                    'main painful scrotum near-miss, '
                                                    'usually more subacute with '
                                                    'urinary symptoms and preserved '
                                                    'cremasteric reflex. Hydrocele and '
                                                    'varicocele lack this ischemic '
                                                    'pattern.',
                                     'choice_explanations': {'A': 'Acute high-riding '
                                                                  'testis with absent '
                                                                  'cremasteric reflex '
                                                                  'is spermatic cord '
                                                                  'torsion until '
                                                                  'disproven.',
                                                             'B': 'Epididymitis also '
                                                                  'causes severe '
                                                                  'scrotal pain and is '
                                                                  'the classic '
                                                                  'differential, but '
                                                                  'onset is typically '
                                                                  'more gradual with '
                                                                  'infectious clues '
                                                                  'and a usually '
                                                                  'present cremasteric '
                                                                  'reflex.',
                                                             'C': 'Hydrocele is a '
                                                                  'fluid collection '
                                                                  'without acute '
                                                                  'ischemia signs.',
                                                             'D': 'Varicocele is '
                                                                  'usually a dull '
                                                                  'standing ache with '
                                                                  'a “bag of worms,” '
                                                                  'not an acute '
                                                                  'surgical '
                                                                  'scrotum.'}}],
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
                                                    'C) Isolated UTI without '
                                                    'soft-tissue involvement despite '
                                                    'crepitus and gas on CT',
                                                    'D) Severe scrotal '
                                                    'cellulitis/abscess without '
                                                    'necrotizing fascial gas-forming '
                                                    'infection'],
                                        'answer': 'B) Fournier gangrene—necrotizing '
                                                  'soft-tissue infection needing '
                                                  'immediate surgical debridement plus '
                                                  'broad antibiotics and resuscitation',
                                        'explanation': 'Diabetes, perineal/scrotal '
                                                       'crepitus, gas on CT, and '
                                                       'sepsis define Fournier '
                                                       'gangrene needing immediate '
                                                       'surgery. Severe '
                                                       'non-necrotizing scrotal '
                                                       'infection is the soft-tissue '
                                                       'near-miss but lacks '
                                                       'gas/crepitus/necrotizing pace. '
                                                       'Home antibiotics or “UTI only” '
                                                       'are inadequate.',
                                        'choice_explanations': {'A': 'Uncomplicated '
                                                                     'epididymitis is '
                                                                     'not a '
                                                                     'necrotizing '
                                                                     'soft-tissue '
                                                                     'emergency.',
                                                                'B': 'Gas-forming '
                                                                     'necrotizing '
                                                                     'perineal '
                                                                     'infection '
                                                                     '(Fournier) '
                                                                     'requires '
                                                                     'immediate '
                                                                     'operative '
                                                                     'debridement plus '
                                                                     'broad '
                                                                     'antibiotics and '
                                                                     'resuscitation.',
                                                                'C': 'CT gas and '
                                                                     'crepitus prove '
                                                                     'soft-tissue '
                                                                     'necrotizing '
                                                                     'infection, not '
                                                                     'isolated UTI.',
                                                                'D': 'Severe '
                                                                     'cellulitis/abscess '
                                                                     'can look '
                                                                     'similarly angry '
                                                                     'and systemic, '
                                                                     'but crepitus and '
                                                                     'soft-tissue gas '
                                                                     'mark necrotizing '
                                                                     'infection that '
                                                                     'must go to '
                                                                     'surgery '
                                                                     'immediately.'}},
                                       {'question': 'A T6 spinal cord–injured patient '
                                                    'develops sudden pounding '
                                                    'headache, flushing above the '
                                                    'lesion, and blood pressure '
                                                    '210/120 while his bladder has '
                                                    'been full for hours. Which '
                                                    'mechanism and response are most '
                                                    'accurate?',
                                        'options': ['A) Thyroid storm as the first '
                                                    'explanation for headache and '
                                                    'hypertension',
                                                    'B) Primary hypertensive emergency '
                                                    'from essential hypertension '
                                                    'unrelated to bladder distention',
                                                    'C) Autonomic dysreflexia '
                                                    'triggered by noxious stimulus '
                                                    'below the lesion—sit up, loosen '
                                                    'garments, and empty the bladder '
                                                    'urgently',
                                                    'D) Orthostatic hypotension from '
                                                    'sitting too long'],
                                        'answer': 'C) Autonomic dysreflexia triggered '
                                                  'by noxious stimulus below the '
                                                  'lesion—sit up, loosen garments, and '
                                                  'empty the bladder urgently',
                                        'explanation': 'In SCI above T6, pounding '
                                                       'headache, flushing, and '
                                                       'extreme hypertension with a '
                                                       'full bladder is autonomic '
                                                       'dysreflexia—remove the '
                                                       'stimulus (empty bladder). '
                                                       'Hypertensive emergency from '
                                                       'other causes is the '
                                                       'blood-pressure near-miss, but '
                                                       'the SCI + full bladder cue is '
                                                       'decisive. Orthostasis lowers '
                                                       'BP; thyroid storm is a '
                                                       'different syndrome.',
                                        'choice_explanations': {'A': 'Thyroid storm '
                                                                     'may cause '
                                                                     'tachycardia/fever '
                                                                     'but is not the '
                                                                     'first '
                                                                     'explanation for '
                                                                     'this SCI–bladder '
                                                                     'pattern.',
                                                                'B': 'Any hypertensive '
                                                                     'emergency needs '
                                                                     'BP control and '
                                                                     'can look similar '
                                                                     'numerically, but '
                                                                     'in T6 SCI with a '
                                                                     'distended '
                                                                     'bladder the '
                                                                     'specific '
                                                                     'mechanism and '
                                                                     'first response '
                                                                     'are '
                                                                     'dysreflexia-directed.',
                                                                'C': 'Autonomic '
                                                                     'dysreflexia from '
                                                                     'a noxious '
                                                                     'stimulus below '
                                                                     'the lesion (full '
                                                                     'bladder) needs '
                                                                     'upright '
                                                                     'positioning and '
                                                                     'immediate '
                                                                     'bladder '
                                                                     'emptying.',
                                                                'D': 'Orthostatic '
                                                                     'hypotension '
                                                                     'causes BP fall, '
                                                                     'not 210/120 with '
                                                                     'flushing.'}},
                                       {'question': 'A trauma patient with an unstable '
                                                    'pelvic fracture has blood at the '
                                                    'urethral meatus and a high-riding '
                                                    'prostate. Before attempting Foley '
                                                    'catheterization, which action is '
                                                    'correct?',
                                        'options': ['A) Place a gentle single attempt '
                                                    'at catheterization by an '
                                                    'experienced clinician only if '
                                                    'protocol allows, aborting '
                                                    'immediately if resistance occurs',
                                                    'B) Force a larger Foley '
                                                    'repeatedly until it passes at any '
                                                    'resistance',
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
                                        'explanation': 'Blood at the meatus and '
                                                       'high-riding prostate after '
                                                       'pelvic fracture imply possible '
                                                       'urethral injury—do not blindly '
                                                       'force a Foley; image with RUG '
                                                       'or use urology-guided '
                                                       'placement. A single careful '
                                                       'attempt is sometimes debated '
                                                       'in protocols and is the '
                                                       'procedural near-miss, but '
                                                       'classic teaching here is defer '
                                                       'blind catheterization for RUG. '
                                                       'Forcing and anticoagulation '
                                                       'are wrong.',
                                        'choice_explanations': {'A': 'Some protocols '
                                                                     'allow one gentle '
                                                                     'attempt by '
                                                                     'experts, '
                                                                     'creating '
                                                                     'practice '
                                                                     'variation, but '
                                                                     'with blood at '
                                                                     'the meatus and '
                                                                     'high-riding '
                                                                     'prostate the '
                                                                     'safest exam '
                                                                     'answer is '
                                                                     'imaging before '
                                                                     'catheterization.',
                                                                'B': 'Forcing a larger '
                                                                     'catheter risks '
                                                                     'completing a '
                                                                     'partial urethral '
                                                                     'disruption.',
                                                                'C': 'Anticoagulation '
                                                                     'worsens pelvic '
                                                                     'hemorrhage and '
                                                                     'does not address '
                                                                     'urethral injury.',
                                                                'D': 'Signs of '
                                                                     'urethral injury '
                                                                     'require '
                                                                     'retrograde '
                                                                     'urethrography '
                                                                     '(or specialist '
                                                                     'placement) '
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
                                                   'B) Posterior circulation '
                                                   '(vertebrobasilar) stroke with '
                                                   'crossed findings or prominent '
                                                   'brainstem/cerebellar signs',
                                                   'C) Isolated peripheral facial '
                                                   'nerve palsy with preserved arm '
                                                   'strength',
                                                   'D) Benign positional vertigo '
                                                   'limited to brief spinning with '
                                                   'head turns'],
                                       'answer': 'A) Anterior circulation (often MCA) '
                                                 'ischemic stroke until proven '
                                                 'otherwise',
                                       'explanation': 'Sudden face/arm weakness with '
                                                      'aphasia is classic anterior '
                                                      '(MCA) ischemia. Posterior '
                                                      'circulation stroke is the '
                                                      'anatomic near-miss within '
                                                      'cerebrovascular disease but '
                                                      'usually features '
                                                      'brainstem/cerebellar signs '
                                                      'rather than cortical aphasia '
                                                      'with hemiparesis. Bell’s palsy '
                                                      'and BPPV lack this cortical '
                                                      'pattern.',
                                       'choice_explanations': {'A': 'Cortical signs '
                                                                    '(aphasia) plus '
                                                                    'contralateral '
                                                                    'face/arm weakness '
                                                                    'localize to '
                                                                    'anterior/MCA '
                                                                    'ischemia until '
                                                                    'proven otherwise.',
                                                               'B': 'Vertebrobasilar '
                                                                    'stroke is also '
                                                                    'acute ischemia '
                                                                    'and thus '
                                                                    'overlapping, but '
                                                                    'aphasia with '
                                                                    'face–arm weakness '
                                                                    'is an '
                                                                    'anterior-circulation '
                                                                    'signature rather '
                                                                    'than typical '
                                                                    'posterior '
                                                                    'patterns.',
                                                               'C': 'Peripheral CN VII '
                                                                    'palsy spares the '
                                                                    'arm and lacks '
                                                                    'cortical language '
                                                                    'deficits.',
                                                               'D': 'BPPV causes brief '
                                                                    'positional '
                                                                    'vertigo without '
                                                                    'acute '
                                                                    'hemiparesis/aphasia.'}},
                                      {'question': 'Which triad best captures classic '
                                                   'clinical meningism?',
                                       'options': ['A) Resting tremor, rigidity, and '
                                                   'bradykinesia only',
                                                   'B) Headache, neck stiffness, and '
                                                   'photophobia (often with fever)',
                                                   'C) Stocking-glove numbness from '
                                                   'distal axonopathy',
                                                   'D) Headache with fever from '
                                                   'systemic viral illness without '
                                                   'meningeal irritation'],
                                       'answer': 'B) Headache, neck stiffness, and '
                                                 'photophobia (often with fever)',
                                       'explanation': 'Meningism classically combines '
                                                      'headache, neck stiffness, and '
                                                      'photophobia, often with fever. '
                                                      'Febrile headache without '
                                                      'meningism is the infectious '
                                                      'near-miss. Parkinsonism and '
                                                      'neuropathy are unrelated '
                                                      'triads/patterns.',
                                       'choice_explanations': {'A': 'Parkinsonian '
                                                                    'triad is '
                                                                    'extrapyramidal, '
                                                                    'not meningism.',
                                                               'B': 'Headache, nuchal '
                                                                    'rigidity, and '
                                                                    'photophobia (± '
                                                                    'fever) constitute '
                                                                    'classic '
                                                                    'meningism.',
                                                               'C': 'Distal sensory '
                                                                    'neuropathy is not '
                                                                    'meningism.',
                                                               'D': 'Fever plus '
                                                                    'headache occurs '
                                                                    'in many '
                                                                    'infections and '
                                                                    'can tempt '
                                                                    '“meningitis,” but '
                                                                    'without neck '
                                                                    'stiffness/photophobia '
                                                                    'the meningism '
                                                                    'triad is '
                                                                    'incomplete.'}},
                                      {'question': 'Which finding set is most '
                                                   'consistent with an upper motor '
                                                   'neuron lesion?',
                                       'options': ['A) Pure sensory loss without any '
                                                   'motor pathway involvement',
                                                   'B) Mixed upper- and '
                                                   'lower-motor-neuron signs as in '
                                                   'amyotrophic lateral sclerosis',
                                                   'C) Spastic weakness, '
                                                   'hyperreflexia, and Babinski sign',
                                                   'D) Flaccid paralysis with early '
                                                   'severe atrophy and fasciculations '
                                                   'alone'],
                                       'answer': 'C) Spastic weakness, hyperreflexia, '
                                                 'and Babinski sign',
                                       'explanation': 'UMN lesions produce spasticity, '
                                                      'hyperreflexia, and Babinski. '
                                                      'ALS mixes UMN+LMN and is the '
                                                      'motor-neuron near-miss, but '
                                                      'pure UMN findings match the '
                                                      'stem. Isolated LMN signs or '
                                                      'pure sensory loss do not.',
                                       'choice_explanations': {'A': 'Pure sensory loss '
                                                                    'does not '
                                                                    'establish UMN '
                                                                    'motor '
                                                                    'involvement.',
                                                               'B': 'ALS includes UMN '
                                                                    'features and can '
                                                                    'confuse students, '
                                                                    'but it also '
                                                                    'requires LMN '
                                                                    'signs; the stem '
                                                                    'asks the UMN set '
                                                                    'alone.',
                                                               'C': 'Spastic paresis, '
                                                                    'brisk reflexes, '
                                                                    'and extensor '
                                                                    'plantar responses '
                                                                    'define UMN '
                                                                    'localization.',
                                                               'D': 'Flaccid atrophy '
                                                                    'with '
                                                                    'fasciculations is '
                                                                    'LMN, not UMN.'}}],
                             'medium': [{'question': 'A patient describes a '
                                                     'thunderclap headache reaching '
                                                     'maximal intensity within '
                                                     'seconds. Which diagnosis must be '
                                                     'excluded first?',
                                         'options': ['A) Reversible cerebral '
                                                     'vasoconstriction syndrome '
                                                     'causing thunderclap headache '
                                                     'without aneurysmal bleed',
                                                     'B) Tension-type headache from '
                                                     'muscle contraction alone',
                                                     'C) Medication-overuse headache '
                                                     'after months of analgesics',
                                                     'D) Subarachnoid hemorrhage until '
                                                     'imaging/LP evaluation is '
                                                     'complete'],
                                         'answer': 'D) Subarachnoid hemorrhage until '
                                                   'imaging/LP evaluation is complete',
                                         'explanation': 'Thunderclap headache is SAH '
                                                        'until ruled out. RCVS also '
                                                        'causes thunderclap pain and '
                                                        'is the cerebrovascular '
                                                        'near-miss, but SAH exclusion '
                                                        'comes first. Tension and '
                                                        'medication-overuse headaches '
                                                        'are gradual/chronic patterns.',
                                         'choice_explanations': {'A': 'RCVS can '
                                                                      'produce '
                                                                      'identical '
                                                                      'thunderclap '
                                                                      'onset and is a '
                                                                      'true '
                                                                      'differential, '
                                                                      'but only after '
                                                                      'SAH has been '
                                                                      'excluded—order '
                                                                      'of operations '
                                                                      'is the '
                                                                      'distinguishing '
                                                                      'point.',
                                                                 'B': 'Tension '
                                                                      'headache builds '
                                                                      'as pressure '
                                                                      'band pain, not '
                                                                      'thunderclap.',
                                                                 'C': 'Medication-overuse '
                                                                      'headache is a '
                                                                      'chronic daily '
                                                                      'pattern, not '
                                                                      'abrupt '
                                                                      'peak-in-seconds '
                                                                      'pain.',
                                                                 'D': 'Maximal-within-seconds '
                                                                      'headache '
                                                                      'requires urgent '
                                                                      'SAH exclusion '
                                                                      'with imaging ± '
                                                                      'LP.'}},
                                        {'question': 'Brief staring spells with 3-Hz '
                                                     'spike-and-wave discharges on EEG '
                                                     'are most typical in which '
                                                     'epilepsy syndrome age group?',
                                         'options': ['A) Childhood absence epilepsy in '
                                                     'school-age children',
                                                     'B) Juvenile myoclonic epilepsy '
                                                     'with 4–6 Hz generalized '
                                                     'discharges and myoclonic jerks',
                                                     'C) Late-onset Alzheimer-related '
                                                     'seizures exclusively',
                                                     'D) Alcohol-withdrawal seizures '
                                                     'in middle-aged adults only'],
                                         'answer': 'A) Childhood absence epilepsy in '
                                                   'school-age children',
                                         'explanation': 'Brief staring with 3-Hz '
                                                        'spike-and-wave is childhood '
                                                        'absence epilepsy. JME is '
                                                        'another genetic generalized '
                                                        'epilepsy and the EEG/syndrome '
                                                        'near-miss, but it features '
                                                        'myoclonus and faster '
                                                        'generalized spikes, not '
                                                        'classic 3-Hz absence. '
                                                        'Alzheimer and alcohol '
                                                        'withdrawal are wrong '
                                                        'age/mechanisms.',
                                         'choice_explanations': {'A': '3-Hz '
                                                                      'spike-and-wave '
                                                                      'with staring '
                                                                      'spells defines '
                                                                      'childhood '
                                                                      'absence '
                                                                      'epilepsy.',
                                                                 'B': 'JME is also '
                                                                      'idiopathic '
                                                                      'generalized '
                                                                      'epilepsy and '
                                                                      'easily '
                                                                      'confused, but '
                                                                      'clinical '
                                                                      'myoclonus and '
                                                                      'typically '
                                                                      'faster '
                                                                      'spike-wave '
                                                                      'distinguish it '
                                                                      'from childhood '
                                                                      'absence with '
                                                                      '3-Hz runs.',
                                                                 'C': 'Alzheimer-related '
                                                                      'seizures are '
                                                                      'late-life and '
                                                                      'not 3-Hz '
                                                                      'absence '
                                                                      'syndrome.',
                                                                 'D': 'Alcohol-withdrawal '
                                                                      'seizures are '
                                                                      'provoked events '
                                                                      'in adults, not '
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
                                                     'D) Essential tremor with '
                                                     'action/postural tremor without '
                                                     'bradykinesia'],
                                         'answer': 'B) Bradykinesia with resting '
                                                   'tremor and/or rigidity',
                                         'explanation': 'Parkinsonism requires '
                                                        'bradykinesia plus resting '
                                                        'tremor and/or rigidity. '
                                                        'Essential tremor is the '
                                                        'common tremor near-miss but '
                                                        'lacks bradykinesia/rigidity '
                                                        'and is postural/action. '
                                                        'Neuropathy and acute stroke '
                                                        'patterns differ.',
                                         'choice_explanations': {'A': 'Sensory '
                                                                      'neuropathy does '
                                                                      'not define '
                                                                      'parkinsonism.',
                                                                 'B': 'Bradykinesia '
                                                                      'plus resting '
                                                                      'tremor and/or '
                                                                      'rigidity is the '
                                                                      'core clinical '
                                                                      'definition of '
                                                                      'parkinsonism.',
                                                                 'C': 'Acute pyramidal '
                                                                      'stroke weakness '
                                                                      'is not the '
                                                                      'parkinsonian '
                                                                      'motor '
                                                                      'phenotype.',
                                                                 'D': 'Essential '
                                                                      'tremor also '
                                                                      'presents with '
                                                                      'prominent '
                                                                      'tremor and is '
                                                                      'frequently '
                                                                      'mislabeled '
                                                                      '“Parkinson’s,” '
                                                                      'but it is '
                                                                      'action/postural '
                                                                      'and lacks '
                                                                      'bradykinesia as '
                                                                      'the defining '
                                                                      'motor '
                                                                      'feature.'}}],
                             'hard': [{'question': 'A patient continues convulsing for '
                                                   '8 minutes despite arrival of EMS. '
                                                   'Which initial pharmacologic '
                                                   'management concept is correct?',
                                       'options': ['A) Use only antipsychotic '
                                                   'medication to stop motor activity',
                                                   'B) Load an urgent '
                                                   'non-benzodiazepine antiseizure '
                                                   'medication (e.g., '
                                                   'levetiracetam/phenytoin) after '
                                                   'benzodiazepines for ongoing status',
                                                   'C) Give a rapid-acting '
                                                   'benzodiazepine (e.g., IV '
                                                   'lorazepam) promptly while '
                                                   'supporting airway',
                                                   'D) Defer all benzodiazepines until '
                                                   'an EEG confirms status in the ICU'],
                                       'answer': 'C) Give a rapid-acting '
                                                 'benzodiazepine (e.g., IV lorazepam) '
                                                 'promptly while supporting airway',
                                       'explanation': 'Established convulsive status '
                                                      'needs immediate benzodiazepines '
                                                      'plus airway support. Urgent ASM '
                                                      'loading is the correct next '
                                                      'step after benzos and is the '
                                                      'pathway near-miss if chosen '
                                                      'first. Waiting for EEG or using '
                                                      'antipsychotics is wrong.',
                                       'choice_explanations': {'A': 'Antipsychotics do '
                                                                    'not terminate '
                                                                    'status '
                                                                    'epilepticus.',
                                                               'B': 'Second-line ASMs '
                                                                    'are essential if '
                                                                    'seizures continue '
                                                                    'and thus feel '
                                                                    '“urgent,” but '
                                                                    'they follow '
                                                                    'benzodiazepines—they '
                                                                    'are not the '
                                                                    'initial agent.',
                                                               'C': 'First-line for '
                                                                    'ongoing '
                                                                    'convulsive status '
                                                                    'is a rapid '
                                                                    'benzodiazepine '
                                                                    'while protecting '
                                                                    'the airway.',
                                                               'D': 'Status is a '
                                                                    'clinical '
                                                                    'emergency; do not '
                                                                    'delay benzos for '
                                                                    'ICU EEG '
                                                                    'confirmation.'}},
                                      {'question': 'Ipsilateral cranial-nerve deficits '
                                                   'with contralateral hemiparesis '
                                                   'most precisely localize to which '
                                                   'region?',
                                       'options': ['A) Cervical spinal cord hemicord '
                                                   '(Brown-Séquard) with ipsilateral '
                                                   'motor and contralateral '
                                                   'pain/temperature loss',
                                                   'B) Pure cortical MCA territory '
                                                   'without brainstem involvement',
                                                   'C) Distal peripheral nerve '
                                                   'entrapment in a limb',
                                                   'D) Brainstem (crossed findings '
                                                   'from compact cranial-nerve and '
                                                   'long-tract proximity)'],
                                       'answer': 'D) Brainstem (crossed findings from '
                                                 'compact cranial-nerve and long-tract '
                                                 'proximity)',
                                       'explanation': 'Ipsilateral CN deficits with '
                                                      'contralateral hemiparesis are '
                                                      'crossed brainstem signs. '
                                                      'Cervical hemicord lesions also '
                                                      'produce “crossed” sensory/motor '
                                                      'patterns and are the '
                                                      'localization near-miss, but '
                                                      'cranial-nerve involvement '
                                                      'places the lesion in the '
                                                      'brainstem. Cortex and '
                                                      'peripheral nerve do not create '
                                                      'this combination.',
                                       'choice_explanations': {'A': 'Brown-Séquard '
                                                                    'also yields '
                                                                    'ipsilateral vs '
                                                                    'contralateral '
                                                                    'findings and can '
                                                                    'tempt “crossed '
                                                                    'signs,” but true '
                                                                    'cranial-nerve '
                                                                    'palsies are '
                                                                    'brainstem, not '
                                                                    'cervical cord.',
                                                               'B': 'Pure cortical MCA '
                                                                    'stroke does not '
                                                                    'produce '
                                                                    'ipsilateral CN '
                                                                    'palsy with '
                                                                    'contralateral '
                                                                    'hemiparesis as a '
                                                                    'brainstem crossed '
                                                                    'pattern.',
                                                               'C': 'Peripheral '
                                                                    'entrapment is '
                                                                    'confined to a '
                                                                    'nerve '
                                                                    'distribution '
                                                                    'without '
                                                                    'contralateral '
                                                                    'long-tract signs.',
                                                               'D': 'Crossed '
                                                                    'cranial-nerve and '
                                                                    'long-tract '
                                                                    'findings localize '
                                                                    'compactly to the '
                                                                    'brainstem.'}},
                                      {'question': 'Fatigable weakness that worsens '
                                                   'with activity and often involves '
                                                   'eyelids and extraocular muscles is '
                                                   'most characteristic of which '
                                                   'disorder?',
                                       'options': ['A) Myasthenia gravis from '
                                                   'autoantibodies against the '
                                                   'neuromuscular junction',
                                                   'B) Lambert–Eaton myasthenic '
                                                   'syndrome with fatigable weakness '
                                                   'but autonomic features and reduced '
                                                   'reflexes, often paraneoplastic',
                                                   'C) Amyotrophic lateral sclerosis '
                                                   'presenting only with UMN signs',
                                                   'D) Guillain–Barré acute '
                                                   'demyelinating polyneuropathy with '
                                                   'areflexia as the sole eye finding'],
                                       'answer': 'A) Myasthenia gravis from '
                                                 'autoantibodies against the '
                                                 'neuromuscular junction',
                                       'explanation': 'Fatigable ocular/bulbar '
                                                      'weakness is classic myasthenia '
                                                      'gravis. LEMS is another NMJ '
                                                      'disorder and the '
                                                      'pathophysiology near-miss, but '
                                                      'it more often affects legs, '
                                                      'reflexes, and autonomic '
                                                      'function and improves somewhat '
                                                      'with use. ALS and GBS differ.',
                                       'choice_explanations': {'A': 'Activity-worsened '
                                                                    'fatigable '
                                                                    'ptosis/ophthalmoplegia '
                                                                    'is characteristic '
                                                                    'of myasthenia '
                                                                    'gravis.',
                                                               'B': 'LEMS is also '
                                                                    'antibody-mediated '
                                                                    'NMJ failure and '
                                                                    'thus closely '
                                                                    'related, but '
                                                                    'clinical pattern '
                                                                    '(proximal legs, '
                                                                    'hyporeflexia, '
                                                                    'autonomic '
                                                                    'symptoms, '
                                                                    'post-activation '
                                                                    'facilitation) '
                                                                    'differs from '
                                                                    'ocular MG.',
                                                               'C': 'ALS is a motor '
                                                                    'neuron disease '
                                                                    'without true NMJ '
                                                                    'fatigable '
                                                                    'ophthalmoplegia '
                                                                    'as its hallmark.',
                                                               'D': 'GBS is areflexic '
                                                                    'polyneuropathy, '
                                                                    'not primary '
                                                                    'fatigable NMJ '
                                                                    'ocular '
                                                                    'disease.'}}],
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
                                                      'C) Perform lumbar puncture '
                                                      'first to decompress the cord',
                                                      'D) Obtain emergent MRI first '
                                                      'and withhold steroids until '
                                                      'imaging confirms compression'],
                                          'answer': 'B) Treat as malignant spinal cord '
                                                    'compression—start high-dose '
                                                    'corticosteroids now and arrange '
                                                    'emergent MRI/surgical or '
                                                    'radiation consultation without '
                                                    "waiting for 'perfect' logistics",
                                          'explanation': 'Progressive bilateral leg '
                                                         'weakness, retention, and '
                                                         'saddle anesthesia in '
                                                         'metastatic cancer is '
                                                         'MSCC—start steroids '
                                                         'immediately and pursue '
                                                         'emergent imaging/definitive '
                                                         'therapy. Waiting for MRI '
                                                         'before steroids is the '
                                                         'dangerous near-miss. NSAIDs '
                                                         'or LP are wrong.',
                                          'choice_explanations': {'A': 'Outpatient '
                                                                       'NSAIDs ignore '
                                                                       'an acute '
                                                                       'neurologic '
                                                                       'emergency.',
                                                                  'B': 'Suspected '
                                                                       'malignant cord '
                                                                       'compression '
                                                                       'needs '
                                                                       'immediate '
                                                                       'corticosteroids '
                                                                       'and emergent '
                                                                       'specialty '
                                                                       'pathways even '
                                                                       'if MRI is '
                                                                       'delayed.',
                                                                  'C': 'LP does not '
                                                                       'decompress '
                                                                       'metastatic '
                                                                       'epidural '
                                                                       'compression '
                                                                       'and may be '
                                                                       'harmful.',
                                                                  'D': 'MRI is '
                                                                       'essential and '
                                                                       'tempting to '
                                                                       '“confirm '
                                                                       'first,” but '
                                                                       'steroids '
                                                                       'should start '
                                                                       'on clinical '
                                                                       'suspicion '
                                                                       'because delays '
                                                                       'risk permanent '
                                                                       'paralysis—the '
                                                                       'timing '
                                                                       'distinction.'}},
                                         {'question': 'After basilar artery occlusion, '
                                                      'a patient is mute and '
                                                      'quadriplegic but can '
                                                      'communicate by vertical eye '
                                                      'movements and blinking. '
                                                      'Consciousness appears '
                                                      'preserved. Which localization '
                                                      'best explains locked-in '
                                                      'syndrome?',
                                          'options': ['A) Isolated left MCA '
                                                      'superior-division aphasia with '
                                                      'full limb strength',
                                                      'B) Bilateral midbrain '
                                                      'infarction affecting '
                                                      'consciousness pathways more '
                                                      'than ventral pontine motor '
                                                      'tracts',
                                                      'C) Bilateral ventral pontine '
                                                      'interruption of corticospinal '
                                                      'and corticobulbar tracts with '
                                                      'spared reticular activating '
                                                      'system and vertical gaze '
                                                      'centers',
                                                      'D) Diffuse bilateral cortical '
                                                      'laminar necrosis with coma'],
                                          'answer': 'C) Bilateral ventral pontine '
                                                    'interruption of corticospinal and '
                                                    'corticobulbar tracts with spared '
                                                    'reticular activating system and '
                                                    'vertical gaze centers',
                                          'explanation': 'Locked-in syndrome is '
                                                         'ventral pontine destruction '
                                                         'with preserved arousal and '
                                                         'vertical eye communication. '
                                                         'Midbrain lesions can impair '
                                                         'consciousness and are '
                                                         'neighboring brainstem '
                                                         'near-misses. Cortical coma '
                                                         'and MCA aphasia do not '
                                                         'produce mute quadriplegia '
                                                         'with preserved vertical gaze '
                                                         'awareness.',
                                          'choice_explanations': {'A': 'MCA aphasia '
                                                                       'preserves limb '
                                                                       'strength '
                                                                       'patterns '
                                                                       'inconsistent '
                                                                       'with '
                                                                       'quadriplegia.',
                                                                  'B': 'Midbrain '
                                                                       'disease is '
                                                                       'also brainstem '
                                                                       'and can '
                                                                       'disturb '
                                                                       'alertness/eye '
                                                                       'movements, but '
                                                                       'classic '
                                                                       'locked-in '
                                                                       'localizes to '
                                                                       'bilateral '
                                                                       'ventral pons '
                                                                       'with preserved '
                                                                       'consciousness.',
                                                                  'C': 'Ventral pons '
                                                                       'lesion spares '
                                                                       'RAS and '
                                                                       'vertical gaze '
                                                                       'while '
                                                                       'interrupting '
                                                                       'corticospinal/corticobulbar '
                                                                       'output—locked-in '
                                                                       'physiology.',
                                                                  'D': 'Diffuse '
                                                                       'cortical '
                                                                       'necrosis '
                                                                       'causes coma, '
                                                                       'not locked-in '
                                                                       'awareness.'}},
                                         {'question': 'A 24-year-old woman develops '
                                                      'subacute psychiatric changes, '
                                                      'seizures, orofacial '
                                                      'dyskinesias, and autonomic '
                                                      'instability. MRI is often '
                                                      'near-normal; CSF may show mild '
                                                      'pleocytosis. Which association '
                                                      'is most important to seek?',
                                          'options': ['A) Anti-LGI1 autoimmune '
                                                      'encephalitis with faciobrachial '
                                                      'dystonic seizures, more typical '
                                                      'in older adults',
                                                      'B) Multiple sclerosis plaques '
                                                      'strictly limited to the spinal '
                                                      'cord',
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
                                          'explanation': 'Young woman with psychiatric '
                                                         'features, seizures, '
                                                         'dyskinesias, and '
                                                         'dysautonomia suggests '
                                                         'anti-NMDA encephalitis ± '
                                                         'ovarian teratoma. Other '
                                                         'autoimmune encephalitides '
                                                         '(e.g., LGI1) are related '
                                                         'near-misses with different '
                                                         'demographics/semiology. MS '
                                                         'and IIH do not fit this '
                                                         'constellation.',
                                          'choice_explanations': {'A': 'LGI1 '
                                                                       'encephalitis '
                                                                       'is also '
                                                                       'autoimmune '
                                                                       'encephalitis '
                                                                       'and thus '
                                                                       'overlapping '
                                                                       'conceptually, '
                                                                       'but '
                                                                       'faciobrachial '
                                                                       'dystonic '
                                                                       'seizures in '
                                                                       'older adults '
                                                                       'differ from '
                                                                       'the NMDA '
                                                                       'teratoma-associated '
                                                                       'phenotype.',
                                                                  'B': 'Cord-limited '
                                                                       'MS does not '
                                                                       'produce this '
                                                                       'encephalitis '
                                                                       'syndrome.',
                                                                  'C': 'IIH causes '
                                                                       'headache/papilledema, '
                                                                       'not orofacial '
                                                                       'dyskinesias '
                                                                       'and '
                                                                       'dysautonomia.',
                                                                  'D': 'This subacute '
                                                                       'neuropsychiatric, '
                                                                       'dyskinetic, '
                                                                       'autonomic '
                                                                       'picture in a '
                                                                       'young woman is '
                                                                       'classic '
                                                                       'anti-NMDA '
                                                                       'receptor '
                                                                       'encephalitis—seek '
                                                                       'ovarian '
                                                                       'teratoma.'}}]},
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
                                                     'B) Mycoplasma pneumoniae as a '
                                                     'common cause of atypical '
                                                     '(“walking”) pneumonia',
                                                     'C) Mycobacterium tuberculosis as '
                                                     'the usual outpatient CAP '
                                                     'pathogen',
                                                     'D) Aspergillus fumigatus as '
                                                     'routine CAP in healthy hosts'],
                                         'answer': 'A) Streptococcus pneumoniae as the '
                                                   'leading classic bacterial cause',
                                         'explanation': 'S. pneumoniae is the classic '
                                                        'leading bacterial CAP '
                                                        'pathogen in immunocompetent '
                                                        'adults. Mycoplasma is a '
                                                        'common atypical cause and the '
                                                        'epidemiologic near-miss, but '
                                                        '“typical” CAP teaching '
                                                        'centers on pneumococcus. TB '
                                                        'and Aspergillus are not '
                                                        'routine CAP in healthy hosts.',
                                         'choice_explanations': {'A': 'Streptococcus '
                                                                      'pneumoniae '
                                                                      'remains the '
                                                                      'classic most '
                                                                      'common typical '
                                                                      'bacterial CAP '
                                                                      'organism.',
                                                                 'B': 'Mycoplasma is '
                                                                      'frequent in '
                                                                      'atypical CAP '
                                                                      'and can be '
                                                                      'over-selected '
                                                                      'as “most '
                                                                      'common,” but '
                                                                      'the stem '
                                                                      'specifies '
                                                                      'typical CAP in '
                                                                      'immunocompetent '
                                                                      'adults—pneumococcus.',
                                                                 'C': 'TB is not the '
                                                                      'usual community '
                                                                      'outpatient CAP '
                                                                      'pathogen.',
                                                                 'D': 'Aspergillus is '
                                                                      'opportunistic, '
                                                                      'not routine '
                                                                      'healthy-host '
                                                                      'CAP.'}},
                                        {'question': 'Asthma is pathophysiologically '
                                                     'characterized by which airway '
                                                     'pattern?',
                                         'options': ['A) Pure alveolar destruction '
                                                     'without airway involvement '
                                                     '(emphysema only)',
                                                     'B) Reversible '
                                                     'bronchoconstriction with airway '
                                                     'inflammation and '
                                                     'hyperresponsiveness',
                                                     'C) Pulmonary vascular '
                                                     'obliteration as the primary '
                                                     'lesion',
                                                     'D) Partially reversible airflow '
                                                     'obstruction in COPD with chronic '
                                                     'bronchitis/emphysema overlap'],
                                         'answer': 'B) Reversible bronchoconstriction '
                                                   'with airway inflammation and '
                                                   'hyperresponsiveness',
                                         'explanation': 'Asthma is reversible '
                                                        'obstruction with inflammation '
                                                        'and hyperresponsiveness. COPD '
                                                        'can show partial '
                                                        'reversibility and is the '
                                                        'obstructive near-miss, but '
                                                        'asthma’s hallmark is marked '
                                                        'reversibility/hyperresponsiveness. '
                                                        'Pure emphysema-only or '
                                                        'primary vascular disease miss '
                                                        'the airway inflammatory '
                                                        'definition.',
                                         'choice_explanations': {'A': 'Emphysema alone '
                                                                      'is alveolar '
                                                                      'septal '
                                                                      'destruction, '
                                                                      'not the asthma '
                                                                      'airway pattern.',
                                                                 'B': 'Asthma '
                                                                      'pathophysiology '
                                                                      'is reversible '
                                                                      'bronchoconstriction '
                                                                      'plus '
                                                                      'inflammatory '
                                                                      'hyperresponsiveness.',
                                                                 'C': 'Primary '
                                                                      'pulmonary '
                                                                      'vascular '
                                                                      'disease is not '
                                                                      'asthma.',
                                                                 'D': 'COPD also '
                                                                      'obstructs '
                                                                      'airflow and may '
                                                                      'partly reverse '
                                                                      'with '
                                                                      'bronchodilators, '
                                                                      'creating '
                                                                      'overlap, but it '
                                                                      'is not defined '
                                                                      'by fully '
                                                                      'reversible '
                                                                      'hyperresponsive '
                                                                      'asthma '
                                                                      'physiology.'}},
                                        {'question': 'Pulse oximetry (SpO2) primarily '
                                                     'estimates which physiologic '
                                                     'quantity?',
                                         'options': ['A) Mixed venous oxygen tension '
                                                     'in the pulmonary artery',
                                                     'B) Arterial oxygen partial '
                                                     'pressure (PaO2) measured '
                                                     'directly on arterial blood gas',
                                                     'C) Hemoglobin oxygen saturation '
                                                     'of pulsatile arterial blood',
                                                     'D) Arterial carbon dioxide '
                                                     'partial pressure directly'],
                                         'answer': 'C) Hemoglobin oxygen saturation of '
                                                   'pulsatile arterial blood',
                                         'explanation': 'Pulse oximetry estimates '
                                                        'arterial hemoglobin oxygen '
                                                        'saturation (SpO2). PaO2 is '
                                                        'related oxygenation data from '
                                                        'ABG and is the conceptual '
                                                        'near-miss, but SpO2 is '
                                                        'saturation, not partial '
                                                        'pressure. CO2 and mixed '
                                                        'venous PO2 are different '
                                                        'analytes.',
                                         'choice_explanations': {'A': 'Mixed venous '
                                                                      'oxygen tension '
                                                                      'requires '
                                                                      'invasive PA '
                                                                      'sampling, not '
                                                                      'fingertip '
                                                                      'oximetry.',
                                                                 'B': 'PaO2 also '
                                                                      'reflects '
                                                                      'oxygenation and '
                                                                      'is often '
                                                                      'conflated with '
                                                                      'SpO2, but '
                                                                      'oximetry does '
                                                                      'not directly '
                                                                      'measure partial '
                                                                      'pressure.',
                                                                 'C': 'SpO2 estimates '
                                                                      'pulsatile '
                                                                      'arterial '
                                                                      'oxyhemoglobin '
                                                                      'saturation.',
                                                                 'D': 'Pulse oximeters '
                                                                      'do not report '
                                                                      'PaCO2.'}}],
                               'medium': [{'question': 'The CURB-65 score is used '
                                                       'clinically to help decide '
                                                       'which management question in '
                                                       'pneumonia?',
                                           'options': ['A) Pneumonia Severity Index '
                                                       '(PSI/PORT) as another '
                                                       'validated tool for disposition '
                                                       'severity',
                                                       'B) Exact microbiologic species '
                                                       'before any antibiotics',
                                                       'C) Need for lung transplant '
                                                       'listing acutely',
                                                       'D) Site-of-care severity '
                                                       '(outpatient vs ward vs '
                                                       'higher-level care)'],
                                           'answer': 'D) Site-of-care severity '
                                                     '(outpatient vs ward vs '
                                                     'higher-level care)',
                                           'explanation': 'CURB-65 helps decide '
                                                          'site-of-care intensity. PSI '
                                                          'is another '
                                                          'severity/disposition score '
                                                          'and the tool near-miss. '
                                                          'CURB-65 does not identify '
                                                          'species or transplant need.',
                                           'choice_explanations': {'A': 'PSI similarly '
                                                                        'guides '
                                                                        'disposition '
                                                                        'and can be '
                                                                        'confused with '
                                                                        'CURB-65; both '
                                                                        'are severity '
                                                                        'tools, but '
                                                                        'the stem asks '
                                                                        'what CURB-65 '
                                                                        'is used '
                                                                        'for—site-of-care—not '
                                                                        'which '
                                                                        'alternative '
                                                                        'score exists.',
                                                                   'B': 'Scoring does '
                                                                        'not replace '
                                                                        'microbiologic '
                                                                        'diagnosis.',
                                                                   'C': 'CURB-65 is '
                                                                        'unrelated to '
                                                                        'acute '
                                                                        'transplant '
                                                                        'listing.',
                                                                   'D': 'CURB-65 '
                                                                        'stratifies '
                                                                        'CAP severity '
                                                                        'to guide '
                                                                        'outpatient vs '
                                                                        'inpatient vs '
                                                                        'higher-level '
                                                                        'care.'}},
                                          {'question': 'Wells criteria are most '
                                                       'commonly applied to estimate '
                                                       'pretest probability of which '
                                                       'diagnosis?',
                                           'options': ['A) Pulmonary embolism (and '
                                                       'similarly DVT in related '
                                                       'scores)',
                                                       'B) Community-acquired '
                                                       'pneumonia when applying '
                                                       'CURB-65 severity scoring '
                                                       'instead',
                                                       'C) Asthma exacerbation '
                                                       'peak-flow severity only',
                                                       'D) Idiopathic pulmonary '
                                                       'fibrosis staging'],
                                           'answer': 'A) Pulmonary embolism (and '
                                                     'similarly DVT in related scores)',
                                           'explanation': 'Wells criteria estimate PE '
                                                          '(and related DVT) pretest '
                                                          'probability. CURB-65 for '
                                                          'pneumonia is another common '
                                                          '“score” near-miss students '
                                                          'mix up. Asthma peak flow '
                                                          'and IPF staging are '
                                                          'unrelated.',
                                           'choice_explanations': {'A': 'Wells scoring '
                                                                        'is designed '
                                                                        'for PE/DVT '
                                                                        'pretest '
                                                                        'probability.',
                                                                   'B': 'CURB-65 is '
                                                                        'also a widely '
                                                                        'memorized '
                                                                        'pulmonary '
                                                                        'score, so '
                                                                        'name '
                                                                        'confusion is '
                                                                        'common, but '
                                                                        'Wells is '
                                                                        'thromboembolism-specific.',
                                                                   'C': 'Peak flow '
                                                                        'grades asthma '
                                                                        'obstruction, '
                                                                        'not PE '
                                                                        'probability.',
                                                                   'D': 'IPF staging '
                                                                        'tools are not '
                                                                        'Wells '
                                                                        'criteria.'}},
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
                                                       'D) 94–98% SpO2 targets used '
                                                       'for most acutely ill patients '
                                                       'without COPD CO2 retention '
                                                       'risk'],
                                           'answer': 'B) Approximately 88–92% to '
                                                     'balance hypoxia against '
                                                     'worsening hypercapnia',
                                           'explanation': 'Many CO2-retaining COPD '
                                                          'patients are titrated to '
                                                          '~88–92% SpO2. The usual '
                                                          '94–98% target for other '
                                                          'patients is the protocol '
                                                          'near-miss. Aiming for 100% '
                                                          'always or deliberately <80% '
                                                          'is harmful.',
                                           'choice_explanations': {'A': 'Maximal '
                                                                        'saturation '
                                                                        'with '
                                                                        'unrestricted '
                                                                        'high-flow O2 '
                                                                        'can worsen '
                                                                        'hypercapnia/acidosis.',
                                                                   'B': 'Controlled '
                                                                        'oxygen aiming '
                                                                        'near 88–92% '
                                                                        'SpO2 balances '
                                                                        'hypoxemia '
                                                                        'against '
                                                                        'hypercapnic '
                                                                        'risk in prone '
                                                                        'COPD '
                                                                        'patients.',
                                                                   'C': 'Deliberate '
                                                                        'severe '
                                                                        'hypoxemia is '
                                                                        'not an oxygen '
                                                                        'strategy.',
                                                                   'D': '94–98% is the '
                                                                        'standard '
                                                                        'target for '
                                                                        'many acute '
                                                                        'patients and '
                                                                        'is easy to '
                                                                        'default to, '
                                                                        'but CO2 '
                                                                        'retainers '
                                                                        'often need '
                                                                        'the lower '
                                                                        'controlled '
                                                                        'range.'}}],
                               'hard': [{'question': 'A trauma patient suddenly '
                                                     'develops severe dyspnea, '
                                                     'tracheal deviation away from one '
                                                     'side, absent breath sounds, and '
                                                     'hypotension. Which immediate '
                                                     'treatment concept is correct?',
                                         'options': ['A) Give nebulized '
                                                     'bronchodilators as the primary '
                                                     'therapy',
                                                     'B) Tube thoracostomy alone after '
                                                     'a confirmatory ultrasound in a '
                                                     'stable patient with non-tension '
                                                     'pneumothorax',
                                                     'C) Perform immediate needle '
                                                     'decompression / finger '
                                                     'thoracostomy followed by chest '
                                                     'tube for tension pneumothorax',
                                                     'D) Obtain a confirmatory chest '
                                                     'radiograph before any '
                                                     'decompression if unstable'],
                                         'answer': 'C) Perform immediate needle '
                                                   'decompression / finger '
                                                   'thoracostomy followed by chest '
                                                   'tube for tension pneumothorax',
                                         'explanation': 'Unstable tension pneumothorax '
                                                        'needs immediate decompression '
                                                        'then chest tube. Standard '
                                                        'chest tube for non-tension '
                                                        'pneumothorax is related '
                                                        'management and the procedural '
                                                        'near-miss, but shock with '
                                                        'tracheal deviation demands '
                                                        'instant needle/finger '
                                                        'decompression. Delaying for '
                                                        'CXR or treating as asthma is '
                                                        'wrong.',
                                         'choice_explanations': {'A': 'Bronchodilators '
                                                                      'do not relieve '
                                                                      'tension '
                                                                      'pneumothorax.',
                                                                 'B': 'Chest tube '
                                                                      'drainage treats '
                                                                      'pneumothorax '
                                                                      'generally and '
                                                                      'is part of '
                                                                      'care, but in '
                                                                      'unstable '
                                                                      'tension you '
                                                                      'decompress '
                                                                      'first—do not '
                                                                      'delay for '
                                                                      'confirmatory '
                                                                      'imaging '
                                                                      'pathways used '
                                                                      'in stable '
                                                                      'patients.',
                                                                 'C': 'Tension '
                                                                      'physiology '
                                                                      'requires '
                                                                      'immediate '
                                                                      'decompression '
                                                                      'followed by '
                                                                      'definitive '
                                                                      'chest drainage.',
                                                                 'D': 'Unstable '
                                                                      'patients must '
                                                                      'not wait for '
                                                                      'CXR before '
                                                                      'decompression.'}},
                                        {'question': 'A hospitalized patient has a new '
                                                     'pleural effusion. Thoracentesis '
                                                     'yields fluid for chemistry '
                                                     'compared with simultaneous serum '
                                                     'values. Light’s criteria are '
                                                     'used to distinguish which '
                                                     'pleural fluid categories?',
                                         'options': ['A) Exudate subclassifications '
                                                     '(e.g., Light’s-positive fluid '
                                                     'then smear/cytology/culture for '
                                                     'cause)',
                                                     'B) Bacterial versus viral '
                                                     'pneumonia on sputum Gram stain '
                                                     'alone',
                                                     'C) Restrictive versus '
                                                     'obstructive spirometry patterns',
                                                     'D) Transudate versus exudate '
                                                     'based on fluid/serum protein and '
                                                     'LDH ratios'],
                                         'answer': 'D) Transudate versus exudate based '
                                                   'on fluid/serum protein and LDH '
                                                   'ratios',
                                         'explanation': 'Light’s criteria separate '
                                                        'transudates from exudates '
                                                        'using protein/LDH ratios. '
                                                        'Further exudate workup is the '
                                                        'next diagnostic step and a '
                                                        'conceptual near-miss if '
                                                        'mistaken for what Light’s '
                                                        'itself distinguishes. Gram '
                                                        'stain and spirometry are '
                                                        'different tests.',
                                         'choice_explanations': {'A': 'Causal workup '
                                                                      'of an exudate '
                                                                      'is essential '
                                                                      'and closely '
                                                                      'follows '
                                                                      'Light’s, but '
                                                                      'Light’s '
                                                                      'criteria '
                                                                      'themselves '
                                                                      'answer '
                                                                      'transudate vs '
                                                                      'exudate—not the '
                                                                      'final etiology.',
                                                                 'B': 'Sputum Gram '
                                                                      'stain does not '
                                                                      'classify '
                                                                      'pleural fluid '
                                                                      'by Light’s.',
                                                                 'C': 'Spirometry '
                                                                      'patterns are '
                                                                      'unrelated to '
                                                                      'pleural fluid '
                                                                      'chemistry '
                                                                      'categories.',
                                                                 'D': 'Light’s '
                                                                      'criteria '
                                                                      'dichotomize '
                                                                      'pleural fluid '
                                                                      'as transudate '
                                                                      'vs exudate via '
                                                                      'protein and LDH '
                                                                      'ratios.'}},
                                        {'question': 'In massive hemoptysis, which '
                                                     'priority precedes definitive '
                                                     'embolization or resection '
                                                     'planning?',
                                         'options': ['A) Airway protection—secure '
                                                     'ventilation and position the '
                                                     'bleeding lung dependent when '
                                                     'possible',
                                                     'B) Bronchial artery embolization '
                                                     'as definitive hemorrhage control '
                                                     'after airway is secured',
                                                     'C) Immediate full '
                                                     'anticoagulation to prevent clot '
                                                     'in the bleeding vessel',
                                                     'D) Outpatient CT follow-up in 2 '
                                                     'weeks if vitals are presently '
                                                     'stable enough to walk'],
                                         'answer': 'A) Airway protection—secure '
                                                   'ventilation and position the '
                                                   'bleeding lung dependent when '
                                                   'possible',
                                         'explanation': 'Massive hemoptysis priorities '
                                                        'start with airway protection '
                                                        'and positioning. Embolization '
                                                        'is often definitive and the '
                                                        'therapeutic near-miss if '
                                                        'chosen as the first priority '
                                                        'before airway control. '
                                                        'Anticoagulation and delayed '
                                                        'outpatient care are '
                                                        'harmful/wrong.',
                                         'choice_explanations': {'A': 'First protect '
                                                                      'the airway and '
                                                                      'favor '
                                                                      'positioning '
                                                                      'that protects '
                                                                      'the '
                                                                      'non-bleeding '
                                                                      'lung.',
                                                                 'B': 'Embolization is '
                                                                      'key definitive '
                                                                      'therapy and '
                                                                      'feels urgent, '
                                                                      'but it follows '
                                                                      'airway/ventilatory '
                                                                      'stabilization—sequence '
                                                                      'is the '
                                                                      'distinguishing '
                                                                      'point.',
                                                                 'C': 'Anticoagulation '
                                                                      'worsens '
                                                                      'hemorrhage.',
                                                                 'D': 'Massive '
                                                                      'hemoptysis is '
                                                                      'not managed by '
                                                                      'deferred '
                                                                      'outpatient '
                                                                      'imaging '
                                                                      'alone.'}}],
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
                                            'options': ['A) Chronic fibrotic ILD '
                                                        'present for years before any '
                                                        'acute illness',
                                                        'B) Acute hypoxemic '
                                                        'respiratory failure with '
                                                        'bilateral opacities not '
                                                        'primarily cardiogenic—use '
                                                        'lung-protective low tidal '
                                                        'volume ventilation',
                                                        'C) Simple atelectasis of one '
                                                        'lobe cured by chest '
                                                        'physiotherapy alone always',
                                                        'D) Cardiogenic pulmonary '
                                                        'edema with bilateral '
                                                        'opacities managed with '
                                                        'afterload reduction and '
                                                        'diuresis rather than ARDS '
                                                        'criteria'],
                                            'answer': 'B) Acute hypoxemic respiratory '
                                                      'failure with bilateral '
                                                      'opacities not primarily '
                                                      'cardiogenic—use lung-protective '
                                                      'low tidal volume ventilation',
                                            'explanation': 'Berlin ARDS: acute '
                                                           'hypoxemia, bilateral '
                                                           'opacities, not fully '
                                                           'explained by cardiac '
                                                           'failure—ventilate with low '
                                                           'tidal volumes. Cardiogenic '
                                                           'edema mimics the '
                                                           'radiograph and is the main '
                                                           'physiologic near-miss, '
                                                           'excluded by non-elevated '
                                                           'filling pressures/clinical '
                                                           'judgment. Chronic ILD and '
                                                           'simple atelectasis do not '
                                                           'meet ARDS framing.',
                                            'choice_explanations': {'A': 'Longstanding '
                                                                         'fibrosis is '
                                                                         'chronic ILD, '
                                                                         'not acute '
                                                                         'ARDS '
                                                                         'criteria.',
                                                                    'B': 'ARDS is '
                                                                         'acute '
                                                                         'non-cardiogenic '
                                                                         'bilateral '
                                                                         'hypoxemic '
                                                                         'failure '
                                                                         'managed with '
                                                                         'lung-protective '
                                                                         'ventilation.',
                                                                    'C': 'Lobar '
                                                                         'atelectasis '
                                                                         'is not '
                                                                         'diffuse '
                                                                         'ARDS.',
                                                                    'D': 'Cardiogenic '
                                                                         'edema also '
                                                                         'causes '
                                                                         'bilateral '
                                                                         'opacities '
                                                                         'and '
                                                                         'hypoxemia, '
                                                                         'so imaging '
                                                                         'overlaps; '
                                                                         'absence of '
                                                                         'primary '
                                                                         'left-atrial '
                                                                         'hypertension '
                                                                         'is the '
                                                                         'ARDS-defining '
                                                                         'distinction.'}},
                                           {'question': 'Twenty-four hours after '
                                                        'long-bone fracture fixation, '
                                                        'a young adult develops acute '
                                                        'dyspnea, petechiae over the '
                                                        'chest, and new confusion. '
                                                        'Which triad diagnosis is most '
                                                        'likely?',
                                            'options': ['A) Typical asthma '
                                                        'exacerbation without fracture '
                                                        'association',
                                                        'B) Pulmonary thromboembolism '
                                                        'with acute dyspnea after '
                                                        'immobilization/surgery',
                                                        'C) Fat embolism syndrome '
                                                        'after orthopedic injury',
                                                        'D) Uncomplicated atelectasis '
                                                        'from shallow breathing only'],
                                            'answer': 'C) Fat embolism syndrome after '
                                                      'orthopedic injury',
                                            'explanation': 'Dyspnea, petechiae, and '
                                                           'confusion after long-bone '
                                                           'fixation suggest fat '
                                                           'embolism. Thromboembolic '
                                                           'PE is the major post-ortho '
                                                           'respiratory near-miss but '
                                                           'lacks the '
                                                           'petechial/neurologic '
                                                           'triad. Atelectasis and '
                                                           'asthma do not fit.',
                                            'choice_explanations': {'A': 'Asthma '
                                                                         'exacerbations '
                                                                         'are not tied '
                                                                         'to this '
                                                                         'fracture–petechiae '
                                                                         'pattern.',
                                                                    'B': 'PE is also '
                                                                         'acute '
                                                                         'postoperative '
                                                                         'dyspnea and '
                                                                         'must be '
                                                                         'considered, '
                                                                         'but '
                                                                         'petechiae '
                                                                         'with '
                                                                         'encephalopathy '
                                                                         'after '
                                                                         'long-bone '
                                                                         'instrumentation '
                                                                         'specifically '
                                                                         'suggest fat '
                                                                         'embolism.',
                                                                    'C': 'The '
                                                                         'orthopedic '
                                                                         'temporal '
                                                                         'link plus '
                                                                         'dyspnea, '
                                                                         'petechiae, '
                                                                         'and '
                                                                         'neurologic '
                                                                         'change '
                                                                         'indicates '
                                                                         'fat embolism '
                                                                         'syndrome.',
                                                                    'D': 'Simple '
                                                                         'atelectasis '
                                                                         'lacks '
                                                                         'petechiae '
                                                                         'and acute '
                                                                         'confusion '
                                                                         'triad.'}},
                                           {'question': 'A nonsmoking young adult with '
                                                        'recurrent hemoptysis and a '
                                                        'central endobronchial mass is '
                                                        'found to have a typical '
                                                        'bronchial carcinoid. Which '
                                                        'paraneoplastic theme may '
                                                        'accompany some neuroendocrine '
                                                        'bronchial tumors?',
                                            'options': ['A) SIADH/hyponatremia from '
                                                        'ectopic ADH, more classic '
                                                        'with small-cell carcinoma '
                                                        'than typical carcinoid',
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
                                            'explanation': 'Bronchial neuroendocrine '
                                                           'tumors may secrete ACTH '
                                                           'and cause Cushing '
                                                           'syndrome. Ectopic '
                                                           'ADH/SIADH is another '
                                                           'paraneoplastic endocrine '
                                                           'theme (especially '
                                                           'small-cell) and the '
                                                           'hormone near-miss. Denying '
                                                           'any hormone effect or '
                                                           'calling MG universal is '
                                                           'wrong.',
                                            'choice_explanations': {'A': 'Ectopic ADH '
                                                                         'is also a '
                                                                         'pulmonary '
                                                                         'paraneoplastic '
                                                                         'endocrine '
                                                                         'syndrome and '
                                                                         'easy to mix '
                                                                         'up, but it '
                                                                         'is far more '
                                                                         'classic for '
                                                                         'small-cell '
                                                                         'carcinoma '
                                                                         'than for '
                                                                         'typical '
                                                                         'bronchial '
                                                                         'carcinoid.',
                                                                    'B': 'Carcinoids '
                                                                         'can obstruct '
                                                                         'bronchi and '
                                                                         'also secrete '
                                                                         'hormones—not '
                                                                         '“never.”',
                                                                    'C': 'Myasthenia '
                                                                         'is linked to '
                                                                         'thymoma, not '
                                                                         'universally '
                                                                         'to bronchial '
                                                                         'carcinoid.',
                                                                    'D': 'ACTH '
                                                                         'secretion '
                                                                         'with Cushing '
                                                                         'physiology '
                                                                         'is a '
                                                                         'recognized '
                                                                         'neuroendocrine '
                                                                         'paraneoplastic '
                                                                         'theme of '
                                                                         'some '
                                                                         'bronchial '
                                                                         'carcinoids.'}}]},
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
                                                          'B) Acute cholecystitis with '
                                                          'RUQ pain and fever but '
                                                          'without obstructive '
                                                          'jaundice as a required '
                                                          'feature',
                                                          'C) Uncomplicated duodenal '
                                                          'ulcer without biliary '
                                                          'involvement',
                                                          'D) Irritable bowel syndrome '
                                                          'with normal liver tests'],
                                              'answer': 'A) Ascending cholangitis from '
                                                        'infected biliary obstruction',
                                              'explanation': 'Charcot’s triad '
                                                             'indicates ascending '
                                                             'cholangitis from '
                                                             'infected biliary '
                                                             'obstruction. Acute '
                                                             'cholecystitis is the '
                                                             'nearby biliary near-miss '
                                                             'with RUQ pain/fever but '
                                                             'typically without the '
                                                             'full obstructive '
                                                             'jaundice triad. Ulcer '
                                                             'and IBS do not fit.',
                                              'choice_explanations': {'A': 'RUQ pain, '
                                                                           'jaundice, '
                                                                           'and fever '
                                                                           '(Charcot) '
                                                                           'point to '
                                                                           'ascending '
                                                                           'cholangitis.',
                                                                      'B': 'Cholecystitis '
                                                                           'shares RUQ '
                                                                           'pain and '
                                                                           'fever and '
                                                                           'is '
                                                                           'commonly '
                                                                           'confused, '
                                                                           'but '
                                                                           'jaundice '
                                                                           'from '
                                                                           'common-duct '
                                                                           'obstruction '
                                                                           'is the '
                                                                           'cholangitis-defining '
                                                                           'addition.',
                                                                      'C': 'Duodenal '
                                                                           'ulcer '
                                                                           'lacks the '
                                                                           'obstructive '
                                                                           'biliary '
                                                                           'infection '
                                                                           'triad.',
                                                                      'D': 'IBS has '
                                                                           'normal '
                                                                           'inflammatory '
                                                                           'and '
                                                                           'biliary '
                                                                           'markers.'}},
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
                                                          'D) Chronic gastritis '
                                                          'without ulcer or neoplasia '
                                                          'as a milder H. pylori '
                                                          'phenotype'],
                                              'answer': 'B) Peptic ulcer disease and '
                                                        'increased risk of gastric '
                                                        'adenocarcinoma/MALT lymphoma',
                                              'explanation': 'H. pylori drives peptic '
                                                             'ulcer disease and raises '
                                                             'gastric '
                                                             'adenocarcinoma/MALT '
                                                             'risk. Chronic gastritis '
                                                             'is a related H. pylori '
                                                             'outcome and near-miss, '
                                                             'but the clearest linked '
                                                             'pathology emphasized '
                                                             'here includes ulcer and '
                                                             'neoplastic risk. PBC and '
                                                             'celiac are different '
                                                             'diseases.',
                                              'choice_explanations': {'A': 'PBC is '
                                                                           'autoimmune '
                                                                           'cholangitis, '
                                                                           'not an H. '
                                                                           'pylori '
                                                                           'gastric '
                                                                           'disease.',
                                                                      'B': 'Chronic H. '
                                                                           'pylori '
                                                                           'infection '
                                                                           'is '
                                                                           'strongly '
                                                                           'linked to '
                                                                           'peptic '
                                                                           'ulcer '
                                                                           'disease '
                                                                           'and '
                                                                           'gastric '
                                                                           'adenocarcinoma/MALT '
                                                                           'lymphoma '
                                                                           'risk.',
                                                                      'C': 'Celiac '
                                                                           'disease is '
                                                                           'gluten-triggered '
                                                                           'enteropathy, '
                                                                           'not H. '
                                                                           'pylori '
                                                                           'pathogenesis.',
                                                                      'D': 'H. pylori '
                                                                           'gastritis '
                                                                           'is real '
                                                                           'and '
                                                                           'related, '
                                                                           'but the '
                                                                           'highest-yield '
                                                                           'disease '
                                                                           'associations '
                                                                           'taught '
                                                                           'with '
                                                                           'chronic '
                                                                           'infection '
                                                                           'are ulcers '
                                                                           'and '
                                                                           'gastric '
                                                                           'neoplasia—not '
                                                                           'gastritis '
                                                                           'alone.'}},
                                             {'question': 'McBurney’s point tenderness '
                                                          'is classically associated '
                                                          'with inflammation of which '
                                                          'organ?',
                                              'options': ['A) Sigmoid colon in '
                                                          'diverticulitis of the '
                                                          'elderly',
                                                          'B) Terminal ileum '
                                                          'inflammation (e.g., Crohn) '
                                                          'also causing RLQ peritoneal '
                                                          'findings',
                                                          'C) Appendix in the right '
                                                          'lower quadrant',
                                                          'D) Gallbladder fundus at '
                                                          'the midclavicular costal '
                                                          'margin'],
                                              'answer': 'C) Appendix in the right '
                                                        'lower quadrant',
                                              'explanation': 'McBurney’s point '
                                                             'tenderness classically '
                                                             'indicates appendicitis. '
                                                             'Terminal ileitis can '
                                                             'mimic RLQ peritonitis '
                                                             'and is the anatomic '
                                                             'near-miss. Gallbladder '
                                                             'and sigmoid localize '
                                                             'elsewhere.',
                                              'choice_explanations': {'A': 'Sigmoid '
                                                                           'diverticulitis '
                                                                           'is '
                                                                           'typically '
                                                                           'LLQ.',
                                                                      'B': 'Crohn’s '
                                                                           'ileitis '
                                                                           'can '
                                                                           'produce '
                                                                           'similar '
                                                                           'RLQ '
                                                                           'pain/tenderness, '
                                                                           'so '
                                                                           'localization '
                                                                           'overlaps; '
                                                                           'McBurney’s '
                                                                           'point '
                                                                           'remains '
                                                                           'classically '
                                                                           'taught for '
                                                                           'appendix.',
                                                                      'C': 'McBurney’s '
                                                                           'point '
                                                                           'tenderness '
                                                                           'is the '
                                                                           'classic '
                                                                           'appendiceal '
                                                                           'RLQ sign.',
                                                                      'D': 'Gallbladder '
                                                                           'tenderness '
                                                                           'is at the '
                                                                           'right '
                                                                           'costal '
                                                                           'margin '
                                                                           '(Murphy), '
                                                                           'not '
                                                                           'McBurney’s '
                                                                           'point.'}}],
                                    'medium': [{'question': 'Acute pancreatitis pain '
                                                            'typically radiates in '
                                                            'which pattern?',
                                                'options': ['A) To the right '
                                                            'scapula/shoulder from '
                                                            'biliary colic or '
                                                            'diaphragmatic irritation',
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
                                                'explanation': 'Pancreatitis typically '
                                                               'causes boring '
                                                               'epigastric pain '
                                                               'radiating through to '
                                                               'the back. Biliary pain '
                                                               'radiating to the '
                                                               'scapula is a common '
                                                               'upper-abdominal '
                                                               'near-miss. Arm and '
                                                               'groin radiation '
                                                               'suggest cardiac or '
                                                               'ureteric sources.',
                                                'choice_explanations': {'A': 'Biliary '
                                                                             'colic/cholecystitis '
                                                                             'also '
                                                                             'causes '
                                                                             'severe '
                                                                             'upper '
                                                                             'abdominal '
                                                                             'pain '
                                                                             'with '
                                                                             'scapular '
                                                                             'radiation '
                                                                             'and is '
                                                                             'easily '
                                                                             'mixed '
                                                                             'up; the '
                                                                             '“through '
                                                                             'to the '
                                                                             'back” '
                                                                             'boring '
                                                                             'pattern '
                                                                             'is the '
                                                                             'pancreatic '
                                                                             'clue.',
                                                                        'B': 'Left-arm '
                                                                             'radiation '
                                                                             'suggests '
                                                                             'myocardial '
                                                                             'ischemia, '
                                                                             'not '
                                                                             'pancreatitis.',
                                                                        'C': 'Groin '
                                                                             'radiation '
                                                                             'suggests '
                                                                             'ureteric '
                                                                             'colic.',
                                                                        'D': 'Acute '
                                                                             'pancreatitis '
                                                                             'pain is '
                                                                             'epigastric '
                                                                             'and '
                                                                             'characteristically '
                                                                             'bores '
                                                                             'through '
                                                                             'to the '
                                                                             'back.'}},
                                               {'question': 'Life-threatening '
                                                            'esophageal variceal '
                                                            'hemorrhage risk is '
                                                            'highest in which setting?',
                                                'options': ['A) Portal hypertension '
                                                            'from cirrhosis with '
                                                            'varices',
                                                            'B) Noncirrhotic portal '
                                                            'hypertension (e.g., '
                                                            'portal vein thrombosis) '
                                                            'also producing varices',
                                                            'C) Mild GERD without '
                                                            'portal hypertension',
                                                            'D) Achalasia with failed '
                                                            'LES relaxation only'],
                                                'answer': 'A) Portal hypertension from '
                                                          'cirrhosis with varices',
                                                'explanation': 'Life-threatening '
                                                               'variceal bleeding risk '
                                                               'is highest with portal '
                                                               'hypertension and '
                                                               'varices, usually from '
                                                               'cirrhosis. '
                                                               'Noncirrhotic portal '
                                                               'hypertension can also '
                                                               'form varices and is '
                                                               'the mechanism '
                                                               'near-miss. GERD and '
                                                               'achalasia are not '
                                                               'variceal risk '
                                                               'settings.',
                                                'choice_explanations': {'A': 'Cirrhotic '
                                                                             'portal '
                                                                             'hypertension '
                                                                             'with '
                                                                             'varices '
                                                                             'is the '
                                                                             'dominant '
                                                                             'setting '
                                                                             'for '
                                                                             'life-threatening '
                                                                             'variceal '
                                                                             'hemorrhage.',
                                                                        'B': 'Portal '
                                                                             'vein '
                                                                             'thrombosis/noncirrhotic '
                                                                             'portal '
                                                                             'hypertension '
                                                                             'can '
                                                                             'likewise '
                                                                             'cause '
                                                                             'varices, '
                                                                             'so '
                                                                             'portal '
                                                                             'hypertension '
                                                                             'overlaps; '
                                                                             'cirrhosis '
                                                                             'remains '
                                                                             'the most '
                                                                             'common '
                                                                             'high-risk '
                                                                             'context '
                                                                             'referenced '
                                                                             'here.',
                                                                        'C': 'GERD '
                                                                             'causes '
                                                                             'reflux '
                                                                             'injury, '
                                                                             'not '
                                                                             'variceal '
                                                                             'bleeding '
                                                                             'risk.',
                                                                        'D': 'Achalasia '
                                                                             'is a '
                                                                             'motility '
                                                                             'disorder '
                                                                             'without '
                                                                             'portal '
                                                                             'hypertensive '
                                                                             'varices.'}},
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
                                                            'C) Dietary gas after '
                                                            'legumes without systemic '
                                                            'signs',
                                                            'D) Chronic watery '
                                                            'diarrhea from bile-acid '
                                                            'malabsorption without '
                                                            'alarm features'],
                                                'answer': 'B) Rectal bleeding, '
                                                          'nocturnal diarrhea, fever, '
                                                          'or unintentional weight '
                                                          'loss',
                                                'explanation': 'Alarm features '
                                                               '(bleeding, nocturnal '
                                                               'diarrhea, fever, '
                                                               'weight loss) warrant '
                                                               'urgent evaluation for '
                                                               'serious disease. '
                                                               'Chronic diarrhea from '
                                                               'functional/bile-acid '
                                                               'causes can be '
                                                               'prolonged and is a '
                                                               'symptom near-miss '
                                                               'without alarms. Stress '
                                                               'stools and dietary gas '
                                                               'are benign.',
                                                'choice_explanations': {'A': 'Brief '
                                                                             'stress-related '
                                                                             'stools '
                                                                             'without '
                                                                             'weight '
                                                                             'loss are '
                                                                             'not '
                                                                             'alarms.',
                                                                        'B': 'Bleeding, '
                                                                             'nocturnal '
                                                                             'stools, '
                                                                             'fever, '
                                                                             'or '
                                                                             'weight '
                                                                             'loss are '
                                                                             'alarm '
                                                                             'features '
                                                                             'needing '
                                                                             'urgent '
                                                                             'workup.',
                                                                        'C': 'Dietary '
                                                                             'gas '
                                                                             'without '
                                                                             'systemic '
                                                                             'signs is '
                                                                             'benign.',
                                                                        'D': 'Chronic '
                                                                             'diarrhea '
                                                                             'alone '
                                                                             'can '
                                                                             'sound '
                                                                             'worrisome '
                                                                             'and '
                                                                             'overlap '
                                                                             'with '
                                                                             'IBD/malabsorption '
                                                                             'concerns, '
                                                                             'but '
                                                                             'without '
                                                                             'alarm '
                                                                             'features '
                                                                             'it does '
                                                                             'not '
                                                                             'carry '
                                                                             'the same '
                                                                             'urgent '
                                                                             'malignancy/IBD-complication '
                                                                             'signal.'}}],
                                    'hard': [{'question': 'An elderly patient with '
                                                          'gallstones develops RUQ '
                                                          'pain, jaundice, and fever, '
                                                          'then becomes hypotensive '
                                                          'and confused. Reynolds '
                                                          'pentad adds which findings '
                                                          'to Charcot’s triad in '
                                                          'severe ascending '
                                                          'cholangitis?',
                                              'options': ['A) Migratory arthritis and '
                                                          'erythema nodosum',
                                                          'B) Jaundice deepening from '
                                                          'progressive biliary '
                                                          'obstruction without shock',
                                                          'C) Hypotension and mental '
                                                          'status change indicating '
                                                          'septic shock',
                                                          'D) Asterixis and spider '
                                                          'nevi only from chronic '
                                                          'cirrhosis'],
                                              'answer': 'C) Hypotension and mental '
                                                        'status change indicating '
                                                        'septic shock',
                                              'explanation': 'Reynolds pentad adds '
                                                             'hypotension and '
                                                             'confusion (septic shock) '
                                                             'to Charcot’s triad in '
                                                             'severe cholangitis. '
                                                             'Worsening jaundice from '
                                                             'obstruction is related '
                                                             'biliary severity and a '
                                                             'near-miss, but pentad '
                                                             'specifically denotes '
                                                             'shock/CNS change. '
                                                             'Cirrhosis stigmata and '
                                                             'reactive arthritis '
                                                             'patterns are different.',
                                              'choice_explanations': {'A': 'Migratory '
                                                                           'arthritis/erythema '
                                                                           'nodosum '
                                                                           'are not '
                                                                           'Reynolds '
                                                                           'pentad.',
                                                                      'B': 'Progressive '
                                                                           'obstructive '
                                                                           'jaundice '
                                                                           'marks '
                                                                           'severe '
                                                                           'biliary '
                                                                           'disease '
                                                                           'and can '
                                                                           'coexist, '
                                                                           'but the '
                                                                           'defining '
                                                                           'pentad '
                                                                           'additions '
                                                                           'are shock '
                                                                           'and mental '
                                                                           'status '
                                                                           'change.',
                                                                      'C': 'Reynolds '
                                                                           'pentad = '
                                                                           'Charcot '
                                                                           'triad plus '
                                                                           'hypotension '
                                                                           'and '
                                                                           'altered '
                                                                           'mentation '
                                                                           'from '
                                                                           'septic '
                                                                           'cholangitis.',
                                                                      'D': 'Asterixis/spider '
                                                                           'nevi '
                                                                           'reflect '
                                                                           'chronic '
                                                                           'liver '
                                                                           'disease, '
                                                                           'not acute '
                                                                           'cholangitic '
                                                                           'septic '
                                                                           'shock '
                                                                           'criteria.'}},
                                             {'question': 'Spontaneous bacterial '
                                                          'peritonitis in a cirrhotic '
                                                          'with ascites is diagnosed '
                                                          'primarily by which ascitic '
                                                          'fluid finding?',
                                              'options': ['A) Positive ascitic '
                                                          'bacterial culture with a '
                                                          'normal neutrophil count '
                                                          '(bacterascites) as a '
                                                          'related but distinct '
                                                          'finding',
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
                                              'explanation': 'SBP diagnosis centers on '
                                                             'ascitic ANC ≥250/µL (± '
                                                             'culture). '
                                                             'Culture-positive '
                                                             'bacterascites without '
                                                             'PMN elevation is a '
                                                             'related fluid infection '
                                                             'concept and near-miss, '
                                                             'but standard SBP '
                                                             'treatment thresholds use '
                                                             'the neutrophil count. '
                                                             'SAAG and chylous fluid '
                                                             'answer different '
                                                             'questions.',
                                              'choice_explanations': {'A': 'Culture-positive '
                                                                           'ascites '
                                                                           'with ANC '
                                                                           '<250 is '
                                                                           'bacterascites—related '
                                                                           'microbiology '
                                                                           'but not '
                                                                           'the usual '
                                                                           'SBP '
                                                                           'neutrophil-based '
                                                                           'definition.',
                                                                      'B': 'SAAG '
                                                                           'classifies '
                                                                           'portal '
                                                                           'hypertension '
                                                                           'vs other '
                                                                           'ascites, '
                                                                           'not SBP by '
                                                                           'itself.',
                                                                      'C': 'Chylous '
                                                                           'triglycerides '
                                                                           'define '
                                                                           'chylous '
                                                                           'ascites, '
                                                                           'not SBP.',
                                                                      'D': 'Ascitic '
                                                                           'ANC '
                                                                           '≥250/µL is '
                                                                           'the '
                                                                           'primary '
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
                                              'explanation': 'Boerhaave is '
                                                             'full-thickness rupture '
                                                             'after vomiting, with '
                                                             'mediastinal/pleural '
                                                             'sequelae. Mallory–Weiss '
                                                             'is the vomiting-related '
                                                             'near-miss but only '
                                                             'mucosal. Candida and '
                                                             'Schatzki ring differ.',
                                              'choice_explanations': {'A': 'Boerhaave '
                                                                           'syndrome '
                                                                           'is '
                                                                           'transmural '
                                                                           'esophageal '
                                                                           'perforation '
                                                                           'after '
                                                                           'forceful '
                                                                           'vomiting.',
                                                                      'B': 'Mallory–Weiss '
                                                                           'also '
                                                                           'follows '
                                                                           'vomiting '
                                                                           'and causes '
                                                                           'bleeding, '
                                                                           'so it is '
                                                                           'commonly '
                                                                           'confused; '
                                                                           'thickness '
                                                                           'of the '
                                                                           'tear '
                                                                           '(mucosal '
                                                                           'vs '
                                                                           'full-thickness) '
                                                                           'is the '
                                                                           'decisive '
                                                                           'distinction.',
                                                                      'C': 'Candida '
                                                                           'esophagitis '
                                                                           'is '
                                                                           'infectious '
                                                                           'odynophagia, '
                                                                           'not '
                                                                           'post-emetic '
                                                                           'rupture.',
                                                                      'D': 'Schatzki '
                                                                           'ring '
                                                                           'causes '
                                                                           'intermittent '
                                                                           'dysphagia '
                                                                           'without '
                                                                           'perforation '
                                                                           'syndrome.'}}],
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
                                                             'C) '
                                                             'Constipation-predominant '
                                                             'IBS as the cause of '
                                                             'rising lactate',
                                                             'D) Ischemic colitis from '
                                                             'low-flow colonic injury '
                                                             'with bloody diarrhea and '
                                                             'milder pain usually'],
                                                 'answer': 'B) Acute mesenteric '
                                                           'ischemia—prioritize '
                                                           'resuscitation and urgent '
                                                           'vascular/surgical '
                                                           'revascularization pathways '
                                                           'despite initially subtle '
                                                           'exam',
                                                 'explanation': 'Pain out of '
                                                                'proportion, AF, and '
                                                                'rising lactate '
                                                                'indicate acute '
                                                                'mesenteric ischemia '
                                                                'needing urgent '
                                                                'revascularization. '
                                                                'Ischemic colitis is '
                                                                'the intestinal '
                                                                'ischemia near-miss '
                                                                'but is typically '
                                                                'left-sided bloody '
                                                                'diarrhea with less '
                                                                'catastrophic early '
                                                                'pain. '
                                                                'Gastroenteritis/IBS '
                                                                'do not explain '
                                                                'lactate and this risk '
                                                                'profile.',
                                                 'choice_explanations': {'A': 'Simple '
                                                                              'gastroenteritis '
                                                                              'should '
                                                                              'not '
                                                                              'produce '
                                                                              'progressive '
                                                                              'lactic '
                                                                              'acidosis '
                                                                              'in this '
                                                                              'AF '
                                                                              'context.',
                                                                         'B': 'Acute '
                                                                              'mesenteric '
                                                                              'ischemia '
                                                                              'presents '
                                                                              'with '
                                                                              'pain '
                                                                              'out of '
                                                                              'proportion '
                                                                              'and '
                                                                              'metabolic '
                                                                              'threat—resuscitate '
                                                                              'and '
                                                                              'pursue '
                                                                              'urgent '
                                                                              'vascular/surgical '
                                                                              'therapy.',
                                                                         'C': 'IBS '
                                                                              'does '
                                                                              'not '
                                                                              'cause '
                                                                              'rising '
                                                                              'lactate.',
                                                                         'D': 'Ischemic '
                                                                              'colitis '
                                                                              'is also '
                                                                              'gut '
                                                                              'ischemia '
                                                                              'and '
                                                                              'shares '
                                                                              'the '
                                                                              'word '
                                                                              '“ischemia,” '
                                                                              'but it '
                                                                              'usually '
                                                                              'follows '
                                                                              'a '
                                                                              'different, '
                                                                              'often '
                                                                              'less '
                                                                              'hyperacute, '
                                                                              'bloody-diarrhea '
                                                                              'pattern '
                                                                              'than '
                                                                              'embolic/thrombotic '
                                                                              'mesenteric '
                                                                              'arterial '
                                                                              'occlusion.'}},
                                                {'question': 'A patient with severe '
                                                             'ulcerative colitis '
                                                             'develops fever, marked '
                                                             'abdominal distension, '
                                                             'tachycardia, and a '
                                                             'dilated transverse colon '
                                                             'on radiograph. Which '
                                                             'complication is '
                                                             'occurring?',
                                                 'options': ['A) Uncomplicated '
                                                             'hemorrhoidal bleeding '
                                                             'only',
                                                             'B) Severe ulcerative '
                                                             'colitis flare without '
                                                             'colonic dilation meeting '
                                                             'megacolon criteria',
                                                             'C) Toxic megacolon with '
                                                             'risk of perforation '
                                                             'requiring intensive '
                                                             'medical therapy and '
                                                             'surgical standby',
                                                             'D) Simple irritable '
                                                             'bowel flare without '
                                                             'systemic toxicity'],
                                                 'answer': 'C) Toxic megacolon with '
                                                           'risk of perforation '
                                                           'requiring intensive '
                                                           'medical therapy and '
                                                           'surgical standby',
                                                 'explanation': 'Systemic toxicity '
                                                                'plus markedly dilated '
                                                                'colon in UC indicates '
                                                                'toxic megacolon. '
                                                                'Severe colitis '
                                                                'without dilation is '
                                                                'the severity '
                                                                'near-miss still '
                                                                'needing intensive '
                                                                'care but not yet '
                                                                'megacolon. IBS and '
                                                                'hemorrhoids do not '
                                                                'fit.',
                                                 'choice_explanations': {'A': 'Hemorrhoidal '
                                                                              'bleeding '
                                                                              'is '
                                                                              'anorectal '
                                                                              'and not '
                                                                              'toxic '
                                                                              'megacolon.',
                                                                         'B': 'Severe '
                                                                              'UC '
                                                                              'flare '
                                                                              'overlaps '
                                                                              'in '
                                                                              'systemic '
                                                                              'inflammation '
                                                                              'and can '
                                                                              'look '
                                                                              'similar, '
                                                                              'but '
                                                                              'radiographic '
                                                                              'megacolon '
                                                                              'is the '
                                                                              'complication '
                                                                              'that '
                                                                              'changes '
                                                                              'urgency '
                                                                              'and '
                                                                              'surgical '
                                                                              'readiness.',
                                                                         'C': 'Fever, '
                                                                              'tachycardia, '
                                                                              'distension, '
                                                                              'and a '
                                                                              'dilated '
                                                                              'transverse '
                                                                              'colon '
                                                                              'in UC '
                                                                              'define '
                                                                              'toxic '
                                                                              'megacolon '
                                                                              'with '
                                                                              'perforation '
                                                                              'risk.',
                                                                         'D': 'IBS '
                                                                              'lacks '
                                                                              'toxicity '
                                                                              'and '
                                                                              'colonic '
                                                                              'dilation.'}},
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
                                                 'options': ['A) Portal vein '
                                                             'thrombosis causing '
                                                             'portal hypertension '
                                                             'without hepatic venous '
                                                             'outflow block',
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
                                                                '(hepatic veins ± '
                                                                'suprahepatic IVC). '
                                                                'Portal vein '
                                                                'thrombosis is another '
                                                                'splanchnic thrombosis '
                                                                'near-miss causing '
                                                                'portal hypertension '
                                                                'without the congested '
                                                                'liver outflow '
                                                                'physiology. '
                                                                'IMV/splenic vein '
                                                                'alone are wrong.',
                                                 'choice_explanations': {'A': 'Portal '
                                                                              'vein '
                                                                              'thrombosis '
                                                                              'is also '
                                                                              'abdominal '
                                                                              'venous '
                                                                              'thrombosis '
                                                                              'and '
                                                                              'commonly '
                                                                              'confused, '
                                                                              'but it '
                                                                              'blocks '
                                                                              'inflow/portal '
                                                                              'flow '
                                                                              'rather '
                                                                              'than '
                                                                              'hepatic '
                                                                              'venous '
                                                                              'outflow.',
                                                                         'B': 'IMV '
                                                                              'thrombosis '
                                                                              'is not '
                                                                              'the '
                                                                              'definition '
                                                                              'of '
                                                                              'Budd–Chiari.',
                                                                         'C': 'Isolated '
                                                                              'splenic '
                                                                              'vein '
                                                                              'thrombosis '
                                                                              'causes '
                                                                              'left-sided '
                                                                              'portal '
                                                                              'hypertension/gastric '
                                                                              'varices '
                                                                              'without '
                                                                              'classic '
                                                                              'Budd–Chiari '
                                                                              'liver '
                                                                              'congestion.',
                                                                         'D': 'Budd–Chiari '
                                                                              'involves '
                                                                              'hepatic '
                                                                              'veins '
                                                                              'and/or '
                                                                              'suprahepatic '
                                                                              'IVC '
                                                                              'obstructing '
                                                                              'hepatic '
                                                                              'venous '
                                                                              'outflow.'}}]},
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
                                                       'B) Hyperosmolar hyperglycemic '
                                                       'state with profound '
                                                       'hyperglycemia and minimal '
                                                       'ketoacidosis',
                                                       'C) Isolated hypoglycemia '
                                                       'without ketones or acidosis',
                                                       'D) Euglycemia with respiratory '
                                                       'alkalosis only'],
                                           'answer': 'A) Hyperglycemia, ketosis, and '
                                                     'high anion-gap metabolic '
                                                     'acidosis',
                                           'explanation': 'DKA requires hyperglycemia, '
                                                          'ketosis, and high anion-gap '
                                                          'acidosis. HHS is the '
                                                          'hyperglycemic crisis '
                                                          'near-miss with marked '
                                                          'hyperosmolarity but little '
                                                          'ketosis. Hypoglycemia and '
                                                          'primary respiratory '
                                                          'alkalosis do not define '
                                                          'DKA.',
                                           'choice_explanations': {'A': 'DKA is the '
                                                                        'triad of '
                                                                        'hyperglycemia, '
                                                                        'ketones, and '
                                                                        'high '
                                                                        'anion-gap '
                                                                        'metabolic '
                                                                        'acidosis.',
                                                                   'B': 'HHS is the '
                                                                        'other major '
                                                                        'hyperglycemic '
                                                                        'emergency and '
                                                                        'shares severe '
                                                                        'hyperglycemia, '
                                                                        'but minimal '
                                                                        'ketoacidosis '
                                                                        'distinguishes '
                                                                        'it from DKA.',
                                                                   'C': 'Hypoglycemia '
                                                                        'is the '
                                                                        'opposite '
                                                                        'glucose '
                                                                        'extreme '
                                                                        'without DKA '
                                                                        'chemistry.',
                                                                   'D': 'Euglycemic '
                                                                        'respiratory '
                                                                        'alkalosis is '
                                                                        'not DKA.'}},
                                          {'question': 'Unless contraindicated, which '
                                                       'oral agent is generally '
                                                       'first-line pharmacotherapy for '
                                                       'type 2 diabetes?',
                                           'options': ['A) Propylthiouracil for '
                                                       'glycemic control',
                                                       'B) Metformin, which reduces '
                                                       'hepatic gluconeogenesis and '
                                                       'improves insulin sensitivity',
                                                       'C) Fludrocortisone to raise '
                                                       'blood glucose',
                                                       'D) SGLT2 inhibitor as an '
                                                       'evidence-based add-on with '
                                                       'cardiorenal benefit after or '
                                                       'with metformin'],
                                           'answer': 'B) Metformin, which reduces '
                                                     'hepatic gluconeogenesis and '
                                                     'improves insulin sensitivity',
                                           'explanation': 'Unless contraindicated, '
                                                          'metformin is first-line '
                                                          'oral therapy for type 2 '
                                                          'diabetes. SGLT2 inhibitors '
                                                          'are important '
                                                          'guideline-directed agents '
                                                          'and the therapeutic '
                                                          'near-miss, but they are not '
                                                          'the universal first-line '
                                                          'starter replacing metformin '
                                                          'in standard teaching. PTU '
                                                          'and fludrocortisone are '
                                                          'wrong classes.',
                                           'choice_explanations': {'A': 'Propylthiouracil '
                                                                        'treats '
                                                                        'hyperthyroidism, '
                                                                        'not '
                                                                        'hyperglycemia.',
                                                                   'B': 'Metformin '
                                                                        'remains the '
                                                                        'usual '
                                                                        'first-line '
                                                                        'pharmacologic '
                                                                        'agent for '
                                                                        'type 2 '
                                                                        'diabetes when '
                                                                        'tolerated.',
                                                                   'C': 'Fludrocortisone '
                                                                        'is '
                                                                        'mineralocorticoid '
                                                                        'replacement, '
                                                                        'not an '
                                                                        'antihyperglycemic.',
                                                                   'D': 'SGLT2 '
                                                                        'inhibitors '
                                                                        'are highly '
                                                                        'appropriate '
                                                                        'in many '
                                                                        'patients and '
                                                                        'easy to '
                                                                        'over-select '
                                                                        'as “first,” '
                                                                        'but '
                                                                        'foundational '
                                                                        'first-line '
                                                                        'initiation is '
                                                                        'still '
                                                                        'metformin '
                                                                        'absent '
                                                                        'contraindications.'}},
                                          {'question': 'Primary hypothyroidism '
                                                       'typically shows which '
                                                       'laboratory pattern?',
                                           'options': ['A) Low TSH with low free T4 '
                                                       'from central hypothyroidism',
                                                       'B) Elevated TSH with normal '
                                                       'free T4 indicating subclinical '
                                                       'hypothyroidism',
                                                       'C) Elevated TSH with low free '
                                                       'T4 from thyroid gland failure',
                                                       'D) Low TSH with high free T4 '
                                                       'from primary thyrotoxicosis'],
                                           'answer': 'C) Elevated TSH with low free T4 '
                                                     'from thyroid gland failure',
                                           'explanation': 'Primary hypothyroidism '
                                                          'shows high TSH and low free '
                                                          'T4. Subclinical '
                                                          'hypothyroidism (high TSH, '
                                                          'normal T4) is the lab '
                                                          'near-miss. Thyrotoxicosis '
                                                          'and central hypothyroidism '
                                                          'invert parts of the '
                                                          'pattern.',
                                           'choice_explanations': {'A': 'Central '
                                                                        'hypothyroidism '
                                                                        'lowers TSH '
                                                                        'and T4 '
                                                                        'together.',
                                                                   'B': 'Subclinical '
                                                                        'hypothyroidism '
                                                                        'also elevates '
                                                                        'TSH and is '
                                                                        'easily '
                                                                        'confused, but '
                                                                        'free T4 '
                                                                        'remains '
                                                                        'normal—overt '
                                                                        'primary '
                                                                        'hypothyroidism '
                                                                        'needs low '
                                                                        'free T4.',
                                                                   'C': 'Primary gland '
                                                                        'failure '
                                                                        'drives TSH up '
                                                                        'while free T4 '
                                                                        'falls.',
                                                                   'D': 'High T4 with '
                                                                        'suppressed '
                                                                        'TSH is '
                                                                        'thyrotoxicosis, '
                                                                        'not hypo.'}}],
                                 'medium': [{'question': 'Positive Chvostek and '
                                                         'Trousseau signs most '
                                                         'strongly suggest which '
                                                         'electrolyte disturbance?',
                                             'options': ['A) Hypomagnesemia that '
                                                         'impairs PTH release and can '
                                                         'mimic or cause refractory '
                                                         'hypocalcemic signs',
                                                         'B) Severe hyperkalemia with '
                                                         'peaked T waves only',
                                                         'C) Hypernatremia from pure '
                                                         'water loss exclusively',
                                                         'D) Hypocalcemia with '
                                                         'neuromuscular '
                                                         'hyperexcitability'],
                                             'answer': 'D) Hypocalcemia with '
                                                       'neuromuscular '
                                                       'hyperexcitability',
                                             'explanation': 'Chvostek/Trousseau signs '
                                                            'indicate neuromuscular '
                                                            'irritability from '
                                                            'hypocalcemia. '
                                                            'Hypomagnesemia is closely '
                                                            'linked and can reproduce '
                                                            'or maintain hypocalcemia, '
                                                            'making it the electrolyte '
                                                            'near-miss. Hyperkalemia '
                                                            'and hypernatremia have '
                                                            'different signatures.',
                                             'choice_explanations': {'A': 'Low '
                                                                          'magnesium '
                                                                          'often '
                                                                          'coexists '
                                                                          'and can '
                                                                          'cause '
                                                                          'functional '
                                                                          'hypoparathyroidism, '
                                                                          'so tetany '
                                                                          'workups '
                                                                          'must '
                                                                          'consider '
                                                                          'both—the '
                                                                          'stem’s '
                                                                          'classic '
                                                                          'association '
                                                                          'remains '
                                                                          'hypocalcemia.',
                                                                     'B': 'Hyperkalemia’s '
                                                                          'urgent clue '
                                                                          'is ECG '
                                                                          'conduction '
                                                                          'change, not '
                                                                          'Chvostek/Trousseau.',
                                                                     'C': 'Hypernatremia '
                                                                          'presents '
                                                                          'with '
                                                                          'thirst/neurologic '
                                                                          'dehydration '
                                                                          'signs, not '
                                                                          'these '
                                                                          'tetany '
                                                                          'signs.',
                                                                     'D': 'Chvostek '
                                                                          'and '
                                                                          'Trousseau '
                                                                          'signs '
                                                                          'classically '
                                                                          'reflect '
                                                                          'symptomatic '
                                                                          'hypocalcemia.'}},
                                            {'question': 'Graves disease is an '
                                                         'autoimmune cause of which '
                                                         'thyroid state?',
                                             'options': ['A) Thyrotoxicosis from '
                                                         'TSH-receptor–stimulating '
                                                         'antibodies',
                                                         'B) Toxic multinodular goiter '
                                                         'causing thyrotoxicosis '
                                                         'without TSH-receptor '
                                                         'antibodies',
                                                         'C) Primary hypothyroidism '
                                                         'from gland destruction only',
                                                         'D) Euthyroid sick syndrome '
                                                         'in critical illness'],
                                             'answer': 'A) Thyrotoxicosis from '
                                                       'TSH-receptor–stimulating '
                                                       'antibodies',
                                             'explanation': 'Graves disease is '
                                                            'autoimmune thyrotoxicosis '
                                                            'from '
                                                            'TSH-receptor–stimulating '
                                                            'antibodies. Other '
                                                            'thyrotoxic etiologies '
                                                            '(toxic nodules) are the '
                                                            'functional near-miss '
                                                            'without TRAb. '
                                                            'Hypothyroidism and sick '
                                                            'euthyroid are different '
                                                            'states.',
                                             'choice_explanations': {'A': 'Graves '
                                                                          'disease '
                                                                          'produces '
                                                                          'thyrotoxicosis '
                                                                          'via '
                                                                          'stimulating '
                                                                          'TSH-receptor '
                                                                          'antibodies.',
                                                                     'B': 'Toxic '
                                                                          'multinodular '
                                                                          'goiter also '
                                                                          'causes '
                                                                          'thyrotoxicosis '
                                                                          'and can '
                                                                          'look '
                                                                          'similar '
                                                                          'clinically/biochemically, '
                                                                          'but it is '
                                                                          'not '
                                                                          'TRAb-mediated '
                                                                          'Graves '
                                                                          'autoimmunity.',
                                                                     'C': 'Primary '
                                                                          'hypothyroidism '
                                                                          'is hormone '
                                                                          'deficiency, '
                                                                          'not Graves '
                                                                          'thyrotoxicosis.',
                                                                     'D': 'Nonthyroidal '
                                                                          'illness '
                                                                          'alters labs '
                                                                          'without '
                                                                          'Graves '
                                                                          'pathophysiology.'}},
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
                                                         'D) IV dexamethasone when '
                                                         'used as an alternative '
                                                         'glucocorticoid if cortisol '
                                                         'assays must remain '
                                                         'interpretable'],
                                             'answer': 'B) IV hydrocortisone '
                                                       '(stress-dose glucocorticoids) '
                                                       'plus volume resuscitation with '
                                                       'saline',
                                             'explanation': 'Adrenal crisis needs '
                                                            'immediate IV '
                                                            'glucocorticoids and '
                                                            'saline resuscitation. '
                                                            'Dexamethasone is '
                                                            'sometimes used initially '
                                                            'if cosyntropin testing is '
                                                            'planned and is the '
                                                            'steroid near-miss, but '
                                                            'hydrocortisone is the '
                                                            'usual preferred stress '
                                                            'cover also providing '
                                                            'mineralocorticoid effect. '
                                                            'Delaying steroids or '
                                                            'using fludrocortisone '
                                                            'alone is wrong.',
                                             'choice_explanations': {'A': 'Never '
                                                                          'withhold '
                                                                          'steroids '
                                                                          'for testing '
                                                                          'in unstable '
                                                                          'suspected '
                                                                          'adrenal '
                                                                          'crisis.',
                                                                     'B': 'Give IV '
                                                                          'hydrocortisone '
                                                                          'with saline '
                                                                          'immediately '
                                                                          'in '
                                                                          'suspected '
                                                                          'adrenal '
                                                                          'crisis.',
                                                                     'C': 'Mineralocorticoid '
                                                                          'alone does '
                                                                          'not replace '
                                                                          'acute '
                                                                          'glucocorticoid '
                                                                          'needs.',
                                                                     'D': 'Dexamethasone '
                                                                          'can be an '
                                                                          'interim '
                                                                          'glucocorticoid '
                                                                          'choice in '
                                                                          'selected '
                                                                          'testing '
                                                                          'scenarios, '
                                                                          'but '
                                                                          'standard '
                                                                          'crisis '
                                                                          'therapy '
                                                                          'emphasized '
                                                                          'here is '
                                                                          'hydrocortisone '
                                                                          'plus '
                                                                          'volume.'}}],
                                 'hard': [{'question': 'An older adult with type 2 '
                                                       'diabetes is found profoundly '
                                                       'dehydrated with glucose 900 '
                                                       'mg/dL, effective osmolality '
                                                       '330 mOsm/kg, and only trace '
                                                       'ketones. Hyperosmolar '
                                                       'hyperglycemic state (HHS) '
                                                       'differs from DKA primarily by '
                                                       'which feature set?',
                                           'options': ['A) Exclusive occurrence in '
                                                       'type 1 diabetes with absolute '
                                                       'insulin deficiency only',
                                                       'B) DKA with hyperglycemia plus '
                                                       'prominent ketosis and '
                                                       'anion-gap acidosis',
                                                       'C) Marked hyperosmolarity and '
                                                       'severe dehydration with '
                                                       'minimal ketoacidosis',
                                                       'D) Lower glucose levels than '
                                                       'typical DKA always'],
                                           'answer': 'C) Marked hyperosmolarity and '
                                                     'severe dehydration with minimal '
                                                     'ketoacidosis',
                                           'explanation': 'HHS features extreme '
                                                          'hyperosmolarity/dehydration '
                                                          'with little ketosis. DKA is '
                                                          'the sister hyperglycemic '
                                                          'crisis and near-miss '
                                                          'defined by ketoacidosis. '
                                                          'HHS usually has higher '
                                                          'glucose than DKA and '
                                                          'predominates in type '
                                                          '2/older adults.',
                                           'choice_explanations': {'A': 'HHS is '
                                                                        'classically '
                                                                        'type 2/older '
                                                                        'adults, not '
                                                                        'exclusive to '
                                                                        'type 1.',
                                                                   'B': 'DKA also '
                                                                        'presents as a '
                                                                        'hyperglycemic '
                                                                        'emergency and '
                                                                        'is the main '
                                                                        'differential; '
                                                                        'prominent '
                                                                        'ketones/acidosis '
                                                                        'are what '
                                                                        'separate DKA '
                                                                        'from HHS.',
                                                                   'C': 'HHS is '
                                                                        'distinguished '
                                                                        'by severe '
                                                                        'hyperosmolar '
                                                                        'dehydration '
                                                                        'with minimal '
                                                                        'ketoacidosis.',
                                                                   'D': 'Glucose in '
                                                                        'HHS is '
                                                                        'typically '
                                                                        'higher, not '
                                                                        'lower, than '
                                                                        'in DKA.'}},
                                          {'question': 'In nonthyroidal illness (sick '
                                                       'euthyroid) patterns, which '
                                                       'laboratory change is most '
                                                       'often seen early?',
                                           'options': ['A) Central hypothyroidism with '
                                                       'low TSH and low free T4 from '
                                                       'pituitary/hypothalamic disease',
                                                       'B) Very high free T4 with '
                                                       'suppressed TSH from Graves '
                                                       'disease',
                                                       'C) Isolated TSH elevation with '
                                                       'goiter and anti-TPO antibodies '
                                                       'defining Hashimoto’s',
                                                       'D) Low T3 (and often '
                                                       'low/normal T4 later) with TSH '
                                                       'that may be low-normal without '
                                                       'primary thyroid disease'],
                                           'answer': 'D) Low T3 (and often low/normal '
                                                     'T4 later) with TSH that may be '
                                                     'low-normal without primary '
                                                     'thyroid disease',
                                           'explanation': 'Early nonthyroidal illness '
                                                          'commonly lowers T3 with '
                                                          'variable TSH/T4 without '
                                                          'primary thyroid disease. '
                                                          'Central hypothyroidism also '
                                                          'lowers thyroid hormones '
                                                          'with inappropriate TSH and '
                                                          'is the endocrine near-miss. '
                                                          'Graves and Hashimoto show '
                                                          'different patterns.',
                                           'choice_explanations': {'A': 'Central '
                                                                        'hypothyroidism '
                                                                        'can look '
                                                                        'similar (low '
                                                                        'T4 with '
                                                                        'non-elevated '
                                                                        'TSH); '
                                                                        'clinical '
                                                                        'critical '
                                                                        'illness '
                                                                        'context and '
                                                                        'typical '
                                                                        'low-T3 '
                                                                        'pattern point '
                                                                        'to '
                                                                        'nonthyroidal '
                                                                        'illness '
                                                                        'rather than '
                                                                        'primary '
                                                                        'pituitary '
                                                                        'failure.',
                                                                   'B': 'Graves shows '
                                                                        'high T4 and '
                                                                        'suppressed '
                                                                        'TSH.',
                                                                   'C': 'Hashimoto '
                                                                        'primary hypo '
                                                                        'elevates TSH '
                                                                        'with '
                                                                        'antibodies/goiter.',
                                                                   'D': 'Sick '
                                                                        'euthyroid '
                                                                        'patterns '
                                                                        'often show '
                                                                        'low T3 early '
                                                                        'with TSH that '
                                                                        'may be '
                                                                        'low-normal '
                                                                        'absent '
                                                                        'intrinsic '
                                                                        'thyroid '
                                                                        'disease.'}},
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
                                                       'B) Hyperthyroidism with heat '
                                                       'intolerance, tremor, and '
                                                       'tachycardia without an adrenal '
                                                       'catecholamine tumor',
                                                       'C) Cold intolerance, '
                                                       'bradycardia, and delayed '
                                                       'reflexes from catecholamine '
                                                       'excess',
                                                       'D) Galactorrhea and amenorrhea '
                                                       'from adrenal medulla prolactin '
                                                       'secretion'],
                                           'answer': 'A) Headache, palpitations, and '
                                                     'diaphoresis with paroxysmal '
                                                     'hypertension from catecholamine '
                                                     'excess',
                                           'explanation': 'Pheochromocytoma classic '
                                                          'triad is headache, '
                                                          'palpitations, and sweating '
                                                          'with paroxysmal '
                                                          'hypertension. '
                                                          'Thyrotoxicosis can mimic '
                                                          'adrenergic symptoms and is '
                                                          'the systemic near-miss. The '
                                                          'other options misstate '
                                                          'catecholamine effects or '
                                                          'invent prolactin secretion.',
                                           'choice_explanations': {'A': 'Paroxysmal '
                                                                        'headache, '
                                                                        'palpitations, '
                                                                        'and '
                                                                        'diaphoresis '
                                                                        'with BP '
                                                                        'spikes '
                                                                        'suggest '
                                                                        'catecholamine '
                                                                        'excess from '
                                                                        'pheochromocytoma.',
                                                                   'B': 'Hyperthyroidism '
                                                                        'also causes '
                                                                        'palpitations/sweating/tremor '
                                                                        'and overlaps '
                                                                        'symptomatically, '
                                                                        'but an '
                                                                        'adrenal mass '
                                                                        'with '
                                                                        'paroxysmal '
                                                                        'hypertensive '
                                                                        'crises points '
                                                                        'to pheo '
                                                                        'rather than '
                                                                        'primary '
                                                                        'thyroid '
                                                                        'disease.',
                                                                   'C': 'Catecholamine '
                                                                        'excess does '
                                                                        'not cause '
                                                                        'hypothyroid-like '
                                                                        'bradycardia '
                                                                        'findings.',
                                                                   'D': 'Adrenal '
                                                                        'medulla does '
                                                                        'not secrete '
                                                                        'prolactin to '
                                                                        'cause '
                                                                        'galactorrhea/amenorrhea.'}}],
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
                                                          'C) Immediate therapeutic '
                                                          'hypothermia to 28°C as goal '
                                                          'therapy',
                                                          'D) IV thyroid hormone alone '
                                                          'while withholding '
                                                          'glucocorticoids even if '
                                                          'concurrent adrenal failure '
                                                          'is possible'],
                                              'answer': 'B) IV thyroid hormone '
                                                        'replacement plus supportive '
                                                        'care, and give stress-dose '
                                                        'glucocorticoids if adrenal '
                                                        'insufficiency is possible',
                                              'explanation': 'Myxedema coma needs IV '
                                                             'thyroid hormone, '
                                                             'supportive care, and '
                                                             'empiric stress-dose '
                                                             'steroids if adrenal '
                                                             'insufficiency is '
                                                             'possible. Giving T3/T4 '
                                                             'without considering '
                                                             'adrenal cover is the '
                                                             'management near-miss. '
                                                             'Rewarming-only or '
                                                             'inducing hypothermia is '
                                                             'wrong.',
                                              'choice_explanations': {'A': 'Passive '
                                                                           'rewarming '
                                                                           'alone does '
                                                                           'not '
                                                                           'replace '
                                                                           'hormone '
                                                                           'therapy.',
                                                                      'B': 'Treat '
                                                                           'myxedema '
                                                                           'coma with '
                                                                           'IV thyroid '
                                                                           'hormone '
                                                                           'and '
                                                                           'supportive '
                                                                           'care; add '
                                                                           'stress-dose '
                                                                           'glucocorticoids '
                                                                           'when '
                                                                           'adrenal '
                                                                           'insufficiency '
                                                                           'cannot be '
                                                                           'excluded.',
                                                                      'C': 'Therapeutic '
                                                                           'hypothermia '
                                                                           'is not the '
                                                                           'treatment '
                                                                           'goal in '
                                                                           'myxedema '
                                                                           'coma.',
                                                                      'D': 'Thyroid '
                                                                           'replacement '
                                                                           'is '
                                                                           'necessary '
                                                                           'and '
                                                                           'tempting '
                                                                           'as '
                                                                           'monotherapy, '
                                                                           'but '
                                                                           'untreated '
                                                                           'concurrent '
                                                                           'adrenal '
                                                                           'failure '
                                                                           'can be '
                                                                           'unmasked—glucocorticoid '
                                                                           'cover is '
                                                                           'the subtle '
                                                                           'required '
                                                                           'addition.'}},
                                             {'question': 'A patient with known Graves '
                                                          'disease develops fever '
                                                          '39.5°C, delirium, vomiting, '
                                                          'and heart rate 150 after '
                                                          'infection. Free T4 is very '
                                                          'high. Which statement about '
                                                          'thyroid storm is correct?',
                                              'options': ['A) Aspirin in high doses is '
                                                          'preferred because it frees '
                                                          'less thyroid hormone from '
                                                          'binding proteins',
                                                          'B) It is confirmed solely '
                                                          'by extremely suppressed TSH '
                                                          'without using clinical '
                                                          'severity criteria',
                                                          'C) It is a clinical '
                                                          'diagnosis of '
                                                          'life-threatening '
                                                          'thyrotoxicosis; treatment '
                                                          'includes thionamides, '
                                                          'iodine after blockade, '
                                                          'beta-blockade, steroids, '
                                                          'and supportive care',
                                                          'D) Propylthiouracil is '
                                                          'contraindicated and iodine '
                                                          'should be given before any '
                                                          'thionamide'],
                                              'answer': 'C) It is a clinical diagnosis '
                                                        'of life-threatening '
                                                        'thyrotoxicosis; treatment '
                                                        'includes thionamides, iodine '
                                                        'after blockade, '
                                                        'beta-blockade, steroids, and '
                                                        'supportive care',
                                              'explanation': 'Thyroid storm is a '
                                                             'clinical diagnosis '
                                                             'treated with multimodal '
                                                             'antithyroid and '
                                                             'supportive therapy '
                                                             '(thionamide first, then '
                                                             'iodine; beta-blocker; '
                                                             'steroids). Relying on '
                                                             'TSH alone is the lab '
                                                             'near-miss. Wrong drug '
                                                             'sequencing and high-dose '
                                                             'aspirin are harmful '
                                                             'concepts.',
                                              'choice_explanations': {'A': 'Salicylates '
                                                                           'can '
                                                                           'increase '
                                                                           'free '
                                                                           'hormone '
                                                                           'fractions '
                                                                           'and are '
                                                                           'avoided.',
                                                                      'B': 'TSH is '
                                                                           'suppressed '
                                                                           'in '
                                                                           'thyrotoxicosis '
                                                                           'and may '
                                                                           'mislead as '
                                                                           'a '
                                                                           '“confirming” '
                                                                           'test, but '
                                                                           'storm is '
                                                                           'graded '
                                                                           'clinically—labs '
                                                                           'alone do '
                                                                           'not make '
                                                                           'the '
                                                                           'diagnosis.',
                                                                      'C': 'Thyroid '
                                                                           'storm is '
                                                                           'diagnosed '
                                                                           'clinically '
                                                                           'and '
                                                                           'treated '
                                                                           'with '
                                                                           'thionamides, '
                                                                           'iodine '
                                                                           'after '
                                                                           'synthesis '
                                                                           'blockade, '
                                                                           'beta-blockade, '
                                                                           'steroids, '
                                                                           'and '
                                                                           'support.',
                                                                      'D': 'Iodine '
                                                                           'should '
                                                                           'follow '
                                                                           'thionamide '
                                                                           'blockade; '
                                                                           'PTU is '
                                                                           'often '
                                                                           'preferred '
                                                                           'in storm '
                                                                           'for '
                                                                           'peripheral '
                                                                           'T4→T3 '
                                                                           'inhibition.'}},
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
                                              'options': ['A) Documented '
                                                          'hyperinsulinemic '
                                                          'hypoglycemia with elevated '
                                                          'C-peptide suggesting '
                                                          'endogenous insulin excess',
                                                          'B) Hyperglycemia symptoms '
                                                          'that resolve with insulin '
                                                          'administration',
                                                          'C) Random hyperglycemia '
                                                          'without relation to '
                                                          'symptoms',
                                                          'D) Symptoms of '
                                                          'hypoglycemia, documented '
                                                          'low plasma glucose, and '
                                                          'relief with glucose '
                                                          'administration'],
                                              'answer': 'D) Symptoms of hypoglycemia, '
                                                        'documented low plasma '
                                                        'glucose, and relief with '
                                                        'glucose administration',
                                              'explanation': 'Whipple’s triad is '
                                                             'symptoms of '
                                                             'hypoglycemia, low plasma '
                                                             'glucose, and relief with '
                                                             'glucose. Insulinoma '
                                                             'workup then shows '
                                                             'inappropriate '
                                                             'insulin/C-peptide—the '
                                                             'biochemical near-miss '
                                                             'step after Whipple. '
                                                             'Hyperglycemia patterns '
                                                             'are opposite.',
                                              'choice_explanations': {'A': 'Endogenous '
                                                                           'hyperinsulinism '
                                                                           'testing is '
                                                                           'the next '
                                                                           'diagnostic '
                                                                           'layer for '
                                                                           'insulinoma '
                                                                           'and '
                                                                           'closely '
                                                                           'related, '
                                                                           'but '
                                                                           'Whipple’s '
                                                                           'triad '
                                                                           'itself '
                                                                           'does not '
                                                                           'require '
                                                                           'insulin/C-peptide '
                                                                           'values.',
                                                                      'B': 'Resolution '
                                                                           'of '
                                                                           'hyperglycemia '
                                                                           'with '
                                                                           'insulin is '
                                                                           'not '
                                                                           'Whipple’s '
                                                                           'triad.',
                                                                      'C': 'Random '
                                                                           'hyperglycemia '
                                                                           'unrelated '
                                                                           'to '
                                                                           'symptoms '
                                                                           'is '
                                                                           'irrelevant.',
                                                                      'D': 'Whipple’s '
                                                                           'triad '
                                                                           'requires '
                                                                           'hypoglycemic '
                                                                           'symptoms, '
                                                                           'low '
                                                                           'measured '
                                                                           'glucose, '
                                                                           'and '
                                                                           'resolution '
                                                                           'after '
                                                                           'glucose.'}}]},
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
                                                    'B) Creatinine clearance measured '
                                                    'with timed urine as a related but '
                                                    'distinct filtration estimate',
                                                    'C) Renal tubular concentrating '
                                                    'ability alone',
                                                    'D) Bladder detrusor '
                                                    'contractility'],
                                        'answer': 'A) Glomerular filtration rate as a '
                                                  'marker of kidney filtering function',
                                        'explanation': 'eGFR estimates glomerular '
                                                       'filtration. Measured '
                                                       'creatinine clearance is a '
                                                       'related filtration metric and '
                                                       'the method near-miss. '
                                                       'Concentrating ability and '
                                                       'detrusor function are '
                                                       'different physiology.',
                                        'choice_explanations': {'A': 'Creatinine-based '
                                                                     'eGFR '
                                                                     'approximates '
                                                                     'glomerular '
                                                                     'filtration rate.',
                                                                'B': 'Timed creatinine '
                                                                     'clearance also '
                                                                     'estimates '
                                                                     'filtration and '
                                                                     'can be confused '
                                                                     'with eGFR, but '
                                                                     'eGFR equations '
                                                                     'are calculated '
                                                                     'estimates—not '
                                                                     'the same as a '
                                                                     'measured '
                                                                     'clearance study.',
                                                                'C': 'Tubular '
                                                                     'concentrating '
                                                                     'ability is '
                                                                     'tested by urine '
                                                                     'osmolality/specific '
                                                                     'gravity '
                                                                     'contexts, not '
                                                                     'eGFR.',
                                                                'D': 'Detrusor '
                                                                     'contractility is '
                                                                     'a bladder '
                                                                     'function, not '
                                                                     'GFR.'}},
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
                                                    'D) Nephritic syndrome with '
                                                    'hypertension, hematuria, and mild '
                                                    'proteinuria'],
                                        'answer': 'B) Hypoalbuminemia, edema, and '
                                                  'often hyperlipidemia',
                                        'explanation': 'Nephrotic syndrome = heavy '
                                                       'proteinuria with '
                                                       'hypoalbuminemia, edema, and '
                                                       'often hyperlipidemia. '
                                                       'Nephritic syndrome is the '
                                                       'glomerular near-miss with '
                                                       'active urine sediment/HTN and '
                                                       'less protein. Hematuria-only '
                                                       'or pyuria define other '
                                                       'processes.',
                                        'choice_explanations': {'A': 'Isolated '
                                                                     'microscopic '
                                                                     'hematuria lacks '
                                                                     'nephrotic-range '
                                                                     'protein loss.',
                                                                'B': 'Nephrotic '
                                                                     'syndrome pairs '
                                                                     'heavy '
                                                                     'proteinuria with '
                                                                     'hypoalbuminemia, '
                                                                     'edema, and '
                                                                     'frequently '
                                                                     'hyperlipidemia.',
                                                                'C': 'Pyuria/fever '
                                                                     'suggest '
                                                                     'infection, not '
                                                                     'nephrotic '
                                                                     'criteria.',
                                                                'D': 'Nephritic '
                                                                     'syndrome is the '
                                                                     'other major '
                                                                     'glomerular '
                                                                     'presentation and '
                                                                     'is commonly '
                                                                     'swapped, but it '
                                                                     'features '
                                                                     'hematuria/HTN/oliguria '
                                                                     'more than the '
                                                                     'full nephrotic '
                                                                     'metabolic set.'}},
                                       {'question': 'ACE inhibitors or ARBs are '
                                                    'particularly preferred in '
                                                    'diabetic kidney disease because '
                                                    'they primarily do which of the '
                                                    'following?',
                                        'options': ['A) Dissolve immune complexes '
                                                    'within the glomerular basement '
                                                    'membrane',
                                                    'B) Block the mineralocorticoid '
                                                    'receptor to reduce fibrosis and '
                                                    'proteinuria as with '
                                                    'finerenone/spironolactone '
                                                    'strategies',
                                                    'C) Reduce intraglomerular '
                                                    'hypertension and proteinuria via '
                                                    'efferent arteriolar dilation',
                                                    'D) Increase intraglomerular '
                                                    'pressure to raise GFR short-term '
                                                    'only'],
                                        'answer': 'C) Reduce intraglomerular '
                                                  'hypertension and proteinuria via '
                                                  'efferent arteriolar dilation',
                                        'explanation': 'ACEI/ARB dilate the efferent '
                                                       'arteriole, lowering '
                                                       'intraglomerular pressure and '
                                                       'proteinuria—key in diabetic '
                                                       'kidney disease. '
                                                       'Mineralocorticoid antagonists '
                                                       'also reduce '
                                                       'proteinuria/fibrosis and are '
                                                       'the cardiorenal near-miss '
                                                       'class, but the stem asks '
                                                       'ACEI/ARB mechanism. Raising '
                                                       'glomerular pressure or '
                                                       '“dissolving” deposits is '
                                                       'wrong.',
                                        'choice_explanations': {'A': 'ACEI/ARB do not '
                                                                     'dissolve GBM '
                                                                     'immune '
                                                                     'complexes.',
                                                                'B': 'Nonsteroidal MR '
                                                                     'antagonists also '
                                                                     'protect diabetic '
                                                                     'kidneys and can '
                                                                     'be confused as '
                                                                     'the same '
                                                                     'mechanism, but '
                                                                     'they block '
                                                                     'aldosterone '
                                                                     'receptors rather '
                                                                     'than '
                                                                     'ACE/angiotensin '
                                                                     'II at the '
                                                                     'efferent '
                                                                     'arteriole.',
                                                                'C': 'ACEI/ARB '
                                                                     'preferencing in '
                                                                     'DKD rests on '
                                                                     'efferent '
                                                                     'dilation that '
                                                                     'lowers '
                                                                     'intraglomerular '
                                                                     'hypertension and '
                                                                     'proteinuria.',
                                                                'D': 'Increasing '
                                                                     'intraglomerular '
                                                                     'pressure is the '
                                                                     'opposite of the '
                                                                     'desired ACEI/ARB '
                                                                     'effect.'}}],
                              'medium': [{'question': 'Red blood cell casts on '
                                                      'urinalysis most strongly '
                                                      'suggest which localization?',
                                          'options': ['A) Acute interstitial nephritis '
                                                      'with WBC casts and sterile '
                                                      'pyuria rather than RBC casts',
                                                      'B) Lower urinary tract bleeding '
                                                      'from bladder tumors only',
                                                      'C) Contamination from menstrual '
                                                      'blood exclusively',
                                                      'D) Glomerulonephritis '
                                                      '(glomerular hematuria)'],
                                          'answer': 'D) Glomerulonephritis (glomerular '
                                                    'hematuria)',
                                          'explanation': 'RBC casts indicate '
                                                         'glomerular bleeding/GN. AIN '
                                                         'produces WBC casts and is '
                                                         'the urine-sediment '
                                                         'near-miss. Lower-tract '
                                                         'bleeding and menstrual '
                                                         'contamination do not form '
                                                         'true RBC casts.',
                                          'choice_explanations': {'A': 'AIN also '
                                                                       'yields an '
                                                                       'active '
                                                                       'sediment and '
                                                                       'can be '
                                                                       'confused in '
                                                                       '“intrinsic '
                                                                       'renal” '
                                                                       'disease, but '
                                                                       'white-cell '
                                                                       'casts/eosinophiluria '
                                                                       'patterns '
                                                                       'differ from '
                                                                       'RBC casts.',
                                                                  'B': 'Bladder '
                                                                       'bleeding may '
                                                                       'cause '
                                                                       'hematuria '
                                                                       'without RBC '
                                                                       'casts.',
                                                                  'C': 'Menstrual '
                                                                       'contamination '
                                                                       'is not '
                                                                       'cast-forming '
                                                                       'glomerular '
                                                                       'hematuria.',
                                                                  'D': 'Red-cell casts '
                                                                       'are a hallmark '
                                                                       'of '
                                                                       'glomerulonephritis.'}},
                                         {'question': 'In suspected postrenal AKI, '
                                                      'which bedside check should be '
                                                      'performed early?',
                                          'options': ['A) Bladder scan or assessment '
                                                      'for urinary '
                                                      'retention/obstruction',
                                                      'B) Renal ultrasound to look for '
                                                      'hydronephrosis after confirming '
                                                      'the bladder is empty',
                                                      'C) Immediate kidney biopsy '
                                                      'before bladder assessment',
                                                      'D) Start high-dose NSAIDs to '
                                                      'reduce inflammation'],
                                          'answer': 'A) Bladder scan or assessment for '
                                                    'urinary retention/obstruction',
                                          'explanation': 'Postrenal AKI workup starts '
                                                         'with bladder outflow '
                                                         'assessment. Renal US for '
                                                         'hydronephrosis is closely '
                                                         'related imaging and the '
                                                         'near-miss next step, but a '
                                                         'full bladder/retention check '
                                                         'is the earliest bedside '
                                                         'move. Biopsy and NSAIDs are '
                                                         'inappropriate first actions.',
                                          'choice_explanations': {'A': 'Early bedside '
                                                                       'bladder '
                                                                       'scan/retention '
                                                                       'check is '
                                                                       'essential when '
                                                                       'postrenal AKI '
                                                                       'is possible.',
                                                                  'B': 'Kidney '
                                                                       'ultrasound for '
                                                                       'hydronephrosis '
                                                                       'is part of '
                                                                       'obstruction '
                                                                       'evaluation and '
                                                                       'feels “the” '
                                                                       'imaging '
                                                                       'answer, but '
                                                                       'first exclude '
                                                                       'reversible '
                                                                       'bladder outlet '
                                                                       'obstruction at '
                                                                       'the bedside.',
                                                                  'C': 'Biopsy is not '
                                                                       'the initial '
                                                                       'test for '
                                                                       'suspected '
                                                                       'postrenal AKI.',
                                                                  'D': 'NSAIDs can '
                                                                       'worsen AKI.'}},
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
                                                      'D) Insulin–glucose to shift '
                                                      'potassium intracellularly after '
                                                      'membrane stabilization'],
                                          'answer': 'B) IV calcium to stabilize '
                                                    'cardiac membranes while '
                                                    'shifting/removing potassium',
                                          'explanation': 'With ECG changes, give IV '
                                                         'calcium first to stabilize '
                                                         'membranes, then shift/remove '
                                                         'K+. Insulin–glucose is '
                                                         'essential shifting therapy '
                                                         'and the sequence near-miss '
                                                         'if chosen as the very first '
                                                         'stabilizing step when ECG '
                                                         'changes are present. Binders '
                                                         'alone or giving KCl are '
                                                         'wrong.',
                                          'choice_explanations': {'A': 'Kayexalate is '
                                                                       'slow and never '
                                                                       'the sole first '
                                                                       'response to '
                                                                       'ECG changes.',
                                                                  'B': 'ECG-unstable '
                                                                       'hyperkalemia '
                                                                       'needs '
                                                                       'immediate IV '
                                                                       'calcium for '
                                                                       'membrane '
                                                                       'stabilization.',
                                                                  'C': 'Giving '
                                                                       'potassium '
                                                                       'worsens '
                                                                       'hyperkalemia.',
                                                                  'D': 'Insulin–glucose '
                                                                       'is critical to '
                                                                       'lower serum K+ '
                                                                       'and closely '
                                                                       'follows, but '
                                                                       'with peaked T '
                                                                       'waves/conduction '
                                                                       'risk calcium '
                                                                       'comes first '
                                                                       'for cardiac '
                                                                       'protection.'}}],
                              'hard': [{'question': 'After prolonged intraoperative '
                                                    'hypotension, a patient’s '
                                                    'creatinine rises and the urine '
                                                    'sediment shows muddy brown '
                                                    'granular casts. This pattern most '
                                                    'supports which AKI etiology?',
                                        'options': ['A) Minimal-change disease with '
                                                    'nephrotic syndrome',
                                                    'B) Prerenal azotemia from '
                                                    'hypoperfusion with bland sediment '
                                                    'and low FeNa before tubular '
                                                    'injury establishes',
                                                    'C) Acute tubular necrosis from '
                                                    'ischemic or toxic tubular injury',
                                                    'D) Acute interstitial nephritis '
                                                    'from drug hypersensitivity '
                                                    'primarily'],
                                        'answer': 'C) Acute tubular necrosis from '
                                                  'ischemic or toxic tubular injury',
                                        'explanation': 'Muddy brown granular casts '
                                                       'after ischemic hypotension '
                                                       'indicate ATN. Prerenal '
                                                       'azotemia is the hemodynamic '
                                                       'near-miss that precedes ATN '
                                                       'but has a bland sediment. AIN '
                                                       'and MCD differ.',
                                        'choice_explanations': {'A': 'Minimal-change '
                                                                     'disease is '
                                                                     'nephrotic, not '
                                                                     'this ATN '
                                                                     'sediment.',
                                                                'B': 'Prerenal '
                                                                     'azotemia shares '
                                                                     'the '
                                                                     'hypoperfusion '
                                                                     'context and can '
                                                                     'evolve into ATN; '
                                                                     'muddy brown '
                                                                     'casts mark that '
                                                                     'tubular injury '
                                                                     'has occurred '
                                                                     'rather than pure '
                                                                     'prerenal '
                                                                     'physiology.',
                                                                'C': 'Ischemic/toxic '
                                                                     'injury with '
                                                                     'muddy brown '
                                                                     'casts indicates '
                                                                     'ATN.',
                                                                'D': 'AIN typically '
                                                                     'shows WBC '
                                                                     'casts/eosinophiluria '
                                                                     'after drugs, not '
                                                                     'muddy brown '
                                                                     'casts.'}},
                                       {'question': 'A patient develops fever, rash, '
                                                    'eosinophiluria, and rising '
                                                    'creatinine one week after '
                                                    'starting a new beta-lactam '
                                                    'antibiotic. Acute interstitial '
                                                    'nephritis is most often linked to '
                                                    'which trigger category?',
                                        'options': ['A) Ischemic or toxic ATN as the '
                                                    'more common hospital AKI '
                                                    'mechanism overall',
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
                                        'explanation': 'AIN is classically drug '
                                                       'hypersensitivity (or '
                                                       'infection). ATN is a more '
                                                       'common AKI overall and the '
                                                       'intrinsic-renal near-miss '
                                                       'students over-select, but '
                                                       'fever/rash/eosinophiluria '
                                                       'after a beta-lactam is AIN. '
                                                       'Stones and orthostasis do not '
                                                       'fit.',
                                        'choice_explanations': {'A': 'ATN is a '
                                                                     'frequent '
                                                                     'intrinsic AKI '
                                                                     'and easy to '
                                                                     'default to in '
                                                                     'hospitals, but '
                                                                     'the allergic '
                                                                     'clinical triad '
                                                                     'after a '
                                                                     'beta-lactam '
                                                                     'specifically '
                                                                     'indicates AIN.',
                                                                'B': 'Bilateral stones '
                                                                     'cause postrenal '
                                                                     'AKI without this '
                                                                     'hypersensitivity '
                                                                     'picture.',
                                                                'C': 'Orthostatic '
                                                                     'proteinuria is '
                                                                     'benign and not '
                                                                     'AIN.',
                                                                'D': 'Fever, rash, '
                                                                     'eosinophiluria, '
                                                                     'and creatinine '
                                                                     'rise after a new '
                                                                     'drug point to '
                                                                     'hypersensitivity '
                                                                     'AIN.'}},
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
                                                    'B) Volume-overload pulmonary '
                                                    'edema refractory to diuretics as '
                                                    'another AEIOU dialysis indication',
                                                    'C) Stable CKD stage 3 with '
                                                    'creatinine 1.6 mg/dL and normal '
                                                    'potassium',
                                                    'D) Isolated microscopic hematuria '
                                                    'with preserved urine output'],
                                        'answer': 'A) Refractory hyperkalemia with ECG '
                                                  'changes despite medical therapy',
                                        'explanation': 'Urgent dialysis indications '
                                                       'include refractory '
                                                       'hyperkalemia with ECG changes. '
                                                       'Refractory volume overload is '
                                                       'another AEIOU indication and '
                                                       'the criteria near-miss. Stable '
                                                       'CKD3 or microscopic hematuria '
                                                       'alone are not urgent dialysis '
                                                       'triggers.',
                                        'choice_explanations': {'A': 'Hyperkalemia '
                                                                     'with ECG changes '
                                                                     'refractory to '
                                                                     'medical therapy '
                                                                     'is a classic '
                                                                     'urgent dialysis '
                                                                     'indication.',
                                                                'B': 'Refractory '
                                                                     'pulmonary edema '
                                                                     'is also an '
                                                                     'urgent dialysis '
                                                                     'indication (the '
                                                                     '“O” in AEIOU) '
                                                                     'and thus closely '
                                                                     'related; among '
                                                                     'listed options, '
                                                                     'the stem’s '
                                                                     'scenario is '
                                                                     'refractory '
                                                                     'hyperkalemia.',
                                                                'C': 'Stable stage-3 '
                                                                     'CKD without '
                                                                     'electrolyte '
                                                                     'emergency does '
                                                                     'not need urgent '
                                                                     'dialysis.',
                                                                'D': 'Microscopic '
                                                                     'hematuria alone '
                                                                     'is not a '
                                                                     'dialysis '
                                                                     'indication.'}}],
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
                                                       'D) Rhabdomyolysis with '
                                                       'hyperkalemia, '
                                                       'hyperphosphatemia, and AKI '
                                                       'from myoglobin rather than '
                                                       'uric acid–driven TLS'],
                                           'answer': 'B) Tumor lysis '
                                                     'syndrome—aggressive IV '
                                                     'hydration, uric acid control '
                                                     '(e.g., rasburicase/allopurinol '
                                                     'as indicated), and treat '
                                                     'electrolyte emergencies; '
                                                     'dialysis if refractory',
                                           'explanation': 'After Burkitt therapy, high '
                                                          'K/PO4/uric acid, low Ca, '
                                                          'and AKI indicate TLS '
                                                          'needing hydration and uric '
                                                          'acid control. '
                                                          'Rhabdomyolysis can mimic '
                                                          'electrolyte AKI patterns '
                                                          'and is the lab near-miss, '
                                                          'but extreme uric acid with '
                                                          'lymphoma lysis is TLS. '
                                                          'SIADH and '
                                                          'hyperparathyroidism do not '
                                                          'match this pattern.',
                                           'choice_explanations': {'A': 'SIADH is '
                                                                        'isolated '
                                                                        'hyponatremia, '
                                                                        'not this '
                                                                        'multi-electrolyte '
                                                                        'lysis '
                                                                        'pattern.',
                                                                   'B': 'TLS after '
                                                                        'high-burden '
                                                                        'lysis causes '
                                                                        'hyperkalemia, '
                                                                        'hyperphosphatemia, '
                                                                        'hyperuricemia, '
                                                                        'secondary '
                                                                        'hypocalcemia, '
                                                                        'and '
                                                                        'AKI—hydrate '
                                                                        'and control '
                                                                        'uric acid.',
                                                                   'C': 'Primary '
                                                                        'hyperparathyroidism '
                                                                        'raises '
                                                                        'calcium and '
                                                                        'lowers '
                                                                        'phosphate—opposite '
                                                                        'of TLS '
                                                                        'hypocalcemia/hyperphosphatemia.',
                                                                   'D': 'Rhabdomyolysis '
                                                                        'also releases '
                                                                        'intracellular '
                                                                        'ions and '
                                                                        'causes AKI, '
                                                                        'so '
                                                                        'chemistries '
                                                                        'overlap; '
                                                                        'massive uric '
                                                                        'acid rise '
                                                                        'after '
                                                                        'lymphoma '
                                                                        'induction is '
                                                                        'the '
                                                                        'TLS-specific '
                                                                        'clue.'}},
                                          {'question': 'A cirrhotic patient with tense '
                                                       'ascites develops progressive '
                                                       'oliguric AKI, bland urine '
                                                       'sediment, and no response to '
                                                       'albumin and holding diuretics '
                                                       'after excluding shock, '
                                                       'nephrotoxins, and obstruction. '
                                                       'Which concept fits hepatorenal '
                                                       'syndrome?',
                                           'options': ['A) Acute glomerulonephritis '
                                                       'with active urinary sediment '
                                                       'always',
                                                       'B) Prerenal AKI from '
                                                       'hypovolemia that reverses '
                                                       'promptly with albumin/volume '
                                                       'alone without the full HRS '
                                                       'physiology',
                                                       'C) Functional renal '
                                                       'vasoconstriction in advanced '
                                                       'liver disease with splanchnic '
                                                       'vasodilation—often needs '
                                                       'vasoconstrictors/albumin and '
                                                       'evaluation for transplant',
                                                       'D) Intrinsic ATN with muddy '
                                                       'brown casts as the usual '
                                                       'sediment'],
                                           'answer': 'C) Functional renal '
                                                     'vasoconstriction in advanced '
                                                     'liver disease with splanchnic '
                                                     'vasodilation—often needs '
                                                     'vasoconstrictors/albumin and '
                                                     'evaluation for transplant',
                                           'explanation': 'Hepatorenal syndrome is '
                                                          'functional renal '
                                                          'vasoconstriction in '
                                                          'advanced cirrhosis after '
                                                          'excluding shock, '
                                                          'nephrotoxins, and '
                                                          'obstruction, often needing '
                                                          'vasoconstrictors/albumin. '
                                                          'Ordinary prerenal azotemia '
                                                          'is the reversible '
                                                          'near-miss. ATN/GN show '
                                                          'different sediments.',
                                           'choice_explanations': {'A': 'Active '
                                                                        'sediment '
                                                                        'indicates '
                                                                        'glomerulonephritis, '
                                                                        'not HRS.',
                                                                   'B': 'Hypovolemic '
                                                                        'prerenal AKI '
                                                                        'can look '
                                                                        'similar early '
                                                                        'and must be '
                                                                        'excluded; '
                                                                        'persistence '
                                                                        'after '
                                                                        'adequate '
                                                                        'albumin/holding '
                                                                        'diuretics '
                                                                        'defines the '
                                                                        'HRS pathway.',
                                                                   'C': 'HRS is '
                                                                        'functional '
                                                                        'renal failure '
                                                                        'from '
                                                                        'splanchnic '
                                                                        'vasodilation '
                                                                        'and renal '
                                                                        'vasoconstriction '
                                                                        'in advanced '
                                                                        'liver '
                                                                        'disease.',
                                                                   'D': 'Muddy brown '
                                                                        'casts '
                                                                        'indicate ATN, '
                                                                        'not classic '
                                                                        'HRS bland '
                                                                        'sediment.'}},
                                          {'question': 'An elderly patient with eGFR '
                                                       '28 mL/min and heart failure '
                                                       'needs contrast-enhanced CT '
                                                       'angiography. The team wants to '
                                                       'limit contrast-associated AKI. '
                                                       'Which prevention theme is most '
                                                       'evidence-aligned among the '
                                                       'options?',
                                           'options': ['A) Routine N-acetylcysteine '
                                                       'administration as proven '
                                                       'standalone prevention superior '
                                                       'to volume optimization',
                                                       'B) Routine high-dose NSAIDs '
                                                       'before contrast to reduce '
                                                       'inflammation',
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
                                           'explanation': 'Contrast-AKI prevention '
                                                          'emphasizes minimizing '
                                                          'volume of contrast, '
                                                          'avoiding nephrotoxins, and '
                                                          'isotonic volume expansion '
                                                          'in at-risk patients. NAC is '
                                                          'a historically popular '
                                                          'near-miss without strong '
                                                          'standalone proof over '
                                                          'volume strategies. NSAIDs '
                                                          'and peri-contrast metformin '
                                                          'are harmful/wrong.',
                                           'choice_explanations': {'A': 'NAC is '
                                                                        'frequently '
                                                                        'remembered as '
                                                                        '“the” '
                                                                        'preventive '
                                                                        'drug, but '
                                                                        'evidence does '
                                                                        'not support '
                                                                        'it as '
                                                                        'superior '
                                                                        'standalone '
                                                                        'therapy over '
                                                                        'thoughtful '
                                                                        'volume/contrast '
                                                                        'minimization.',
                                                                   'B': 'NSAIDs '
                                                                        'increase AKI '
                                                                        'risk.',
                                                                   'C': 'Metformin is '
                                                                        'held around '
                                                                        'contrast in '
                                                                        'significant '
                                                                        'CKD because '
                                                                        'of lactic '
                                                                        'acidosis risk '
                                                                        'if AKI '
                                                                        'occurs—not '
                                                                        'given '
                                                                        'immediately '
                                                                        'before.',
                                                                   'D': 'Best-aligned '
                                                                        'prevention is '
                                                                        'less '
                                                                        'contrast, '
                                                                        'hold '
                                                                        'nephrotoxins, '
                                                                        'and '
                                                                        'peri-procedural '
                                                                        'isotonic '
                                                                        'volume '
                                                                        'expansion '
                                                                        'when '
                                                                        'appropriate.'}}]},
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
                                                     'B) MRI for ligamentous detail '
                                                     'after radiographs have excluded '
                                                     'fracture when symptoms persist',
                                                     'C) Immediate surgical fixation '
                                                     'without imaging ever',
                                                     'D) Long-term bisphosphonate '
                                                     'therapy initiation'],
                                         'answer': 'A) Radiographs of the ankle/foot '
                                                   'after acute injury',
                                         'explanation': 'Ottawa ankle rules decide '
                                                        'whether radiographs are '
                                                        'needed. MRI is a related '
                                                        'advanced imaging near-miss '
                                                        'for soft tissue after '
                                                        'fracture is excluded. '
                                                        'Surgery-without-imaging and '
                                                        'bisphosphonates are '
                                                        'unrelated.',
                                         'choice_explanations': {'A': 'Ottawa rules '
                                                                      'triage who '
                                                                      'needs '
                                                                      'ankle/foot '
                                                                      'radiographs '
                                                                      'after injury.',
                                                                 'B': 'MRI evaluates '
                                                                      'ligaments and '
                                                                      'can be '
                                                                      'appropriate '
                                                                      'later, but '
                                                                      'Ottawa rules '
                                                                      'specifically '
                                                                      'address '
                                                                      'radiograph '
                                                                      'necessity—not '
                                                                      'MRI as the '
                                                                      'first decision.',
                                                                 'C': 'Surgical '
                                                                      'fixation is not '
                                                                      'decided by '
                                                                      'Ottawa rules '
                                                                      'without '
                                                                      'imaging.',
                                                                 'D': 'Ottawa rules do '
                                                                      'not initiate '
                                                                      'osteoporosis '
                                                                      'drug therapy.'}},
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
                                                     'D) Fall on an outstretched hand '
                                                     'with volar angulation (Smith '
                                                     'fracture) as a related distal '
                                                     'radius pattern'],
                                         'answer': 'B) Fall on an outstretched hand '
                                                   'with distal radius dorsal '
                                                   'angulation',
                                         'explanation': 'Colles fracture is FOOSH with '
                                                        'dorsal distal radius '
                                                        'angulation. Smith fracture is '
                                                        'the FOOSH-related distal '
                                                        'radius near-miss with volar '
                                                        'angulation. Elbow blow and '
                                                        'meniscus twist are different '
                                                        'injuries.',
                                         'choice_explanations': {'A': 'Flexed-elbow '
                                                                      'blows suggest '
                                                                      'different elbow '
                                                                      'injuries.',
                                                                 'B': 'Colles fracture '
                                                                      'classically '
                                                                      'follows FOOSH '
                                                                      'with dorsal '
                                                                      'angulation of '
                                                                      'the distal '
                                                                      'radius.',
                                                                 'C': 'Meniscal injury '
                                                                      'is a knee '
                                                                      'twisting '
                                                                      'pattern.',
                                                                 'D': 'Smith fracture '
                                                                      'also follows '
                                                                      'wrist '
                                                                      'trauma/FOOSH '
                                                                      'mechanisms and '
                                                                      'involves the '
                                                                      'distal radius, '
                                                                      'but angulation '
                                                                      'is volar—the '
                                                                      'radiographic '
                                                                      'distinction.'}},
                                        {'question': 'An open fracture with '
                                                     'soft-tissue communication to the '
                                                     'bone requires which early '
                                                     'management priority beyond '
                                                     'immobilization?',
                                         'options': ['A) High-dose NSAIDs alone as '
                                                     'definitive care',
                                                     'B) Urgent surgical debridement '
                                                     'alone while delaying antibiotics '
                                                     'until intraoperative cultures '
                                                     'are finalized',
                                                     'C) Urgent antibiotics, tetanus '
                                                     'status, and surgical '
                                                     'irrigation/debridement',
                                                     'D) Delayed antibiotics until '
                                                     'cultures return in 48 hours'],
                                         'answer': 'C) Urgent antibiotics, tetanus '
                                                   'status, and surgical '
                                                   'irrigation/debridement',
                                         'explanation': 'Open fractures need early IV '
                                                        'antibiotics, tetanus care, '
                                                        'and operative '
                                                        'irrigation/debridement. '
                                                        'Debridement is essential and '
                                                        'the surgical near-miss if '
                                                        'antibiotics are delayed for '
                                                        'cultures. Waiting 48 hours or '
                                                        'NSAIDs alone is wrong.',
                                         'choice_explanations': {'A': 'NSAIDs do not '
                                                                      'manage '
                                                                      'open-fracture '
                                                                      'contamination.',
                                                                 'B': 'Operative '
                                                                      'debridement is '
                                                                      'mandatory and '
                                                                      'easy to '
                                                                      'prioritize '
                                                                      'alone, but '
                                                                      'early '
                                                                      'antibiotics '
                                                                      'should not wait '
                                                                      'for culture '
                                                                      'finalization—they '
                                                                      'reduce '
                                                                      'infection risk '
                                                                      'immediately.',
                                                                 'C': 'Open fractures '
                                                                      'require prompt '
                                                                      'antibiotics, '
                                                                      'tetanus '
                                                                      'assessment, and '
                                                                      'surgical '
                                                                      'washout/debridement.',
                                                                 'D': 'Delaying '
                                                                      'antibiotics for '
                                                                      'culture results '
                                                                      'increases '
                                                                      'infection '
                                                                      'risk.'}}],
                               'medium': [{'question': 'Which early clinical feature '
                                                       'is most concerning for acute '
                                                       'compartment syndrome after '
                                                       'tibial fracture?',
                                           'options': ['A) Paresthesias in the nerve '
                                                       'distribution of the '
                                                       'compartment as an early '
                                                       'ischemic nerve finding',
                                                       'B) Isolated mild bruising '
                                                       'without tense swelling or pain',
                                                       'C) Painless chronic deformity '
                                                       'weeks later only',
                                                       'D) Pain out of proportion and '
                                                       'pain on passive stretch of the '
                                                       'compartment'],
                                           'answer': 'D) Pain out of proportion and '
                                                     'pain on passive stretch of the '
                                                     'compartment',
                                           'explanation': 'Compartment syndrome’s '
                                                          'earliest reliable clues are '
                                                          'pain out of proportion and '
                                                          'passive stretch pain. '
                                                          'Paresthesias are also early '
                                                          'ischemic nerve signs and '
                                                          'the neurologic near-miss, '
                                                          'but pain/stretch pain are '
                                                          'the most emphasized initial '
                                                          'features; pulselessness is '
                                                          'late. Mild bruise or late '
                                                          'deformity do not define '
                                                          'acute syndrome.',
                                           'choice_explanations': {'A': 'Paresthesia '
                                                                        'is an '
                                                                        'important '
                                                                        'early finding '
                                                                        'too and can '
                                                                        'be selected '
                                                                        'as “the” '
                                                                        'sign, but '
                                                                        'classic '
                                                                        'teaching '
                                                                        'prioritizes '
                                                                        'pain out of '
                                                                        'proportion/passive '
                                                                        'stretch as '
                                                                        'most '
                                                                        'concerning '
                                                                        'initial '
                                                                        'features.',
                                                                   'B': 'Mild bruising '
                                                                        'alone is '
                                                                        'expected '
                                                                        'soft-tissue '
                                                                        'injury, not '
                                                                        'compartment '
                                                                        'syndrome.',
                                                                   'C': 'Late painless '
                                                                        'deformity is '
                                                                        'not acute '
                                                                        'compartment '
                                                                        'syndrome.',
                                                                   'D': 'Disproportionate '
                                                                        'pain and pain '
                                                                        'on passive '
                                                                        'stretch are '
                                                                        'the key early '
                                                                        'compartment '
                                                                        'syndrome '
                                                                        'warnings.'}},
                                          {'question': 'Fat embolism syndrome '
                                                       'classically follows which '
                                                       'orthopedic setting?',
                                           'options': ['A) Long-bone or pelvic '
                                                       'fractures, especially after '
                                                       'instrumentation',
                                                       'B) Pulmonary thromboembolism '
                                                       'after orthopedic surgery '
                                                       'without the fat-embolism '
                                                       'petechial/neurologic triad',
                                                       'C) Isolated fingertip tuft '
                                                       'fracture without marrow '
                                                       'involvement',
                                                       'D) Chronic tennis elbow from '
                                                       'repetitive strain'],
                                           'answer': 'A) Long-bone or pelvic '
                                                     'fractures, especially after '
                                                     'instrumentation',
                                           'explanation': 'Fat embolism follows '
                                                          'long-bone/pelvic fractures '
                                                          'and instrumentation. '
                                                          'Thromboembolic PE is the '
                                                          'post-ortho respiratory '
                                                          'near-miss. Small tuft '
                                                          'fractures and tennis elbow '
                                                          'are not classic settings.',
                                           'choice_explanations': {'A': 'Fat embolism '
                                                                        'syndrome '
                                                                        'classically '
                                                                        'follows major '
                                                                        'long-bone or '
                                                                        'pelvic '
                                                                        'fractures, '
                                                                        'especially '
                                                                        'with '
                                                                        'instrumentation.',
                                                                   'B': 'PE also '
                                                                        'occurs after '
                                                                        'orthopedic '
                                                                        'injury/surgery '
                                                                        'and causes '
                                                                        'acute '
                                                                        'dyspnea, but '
                                                                        'fat embolism '
                                                                        'is '
                                                                        'specifically '
                                                                        'tied to '
                                                                        'marrow '
                                                                        'embolization '
                                                                        'with its '
                                                                        'clinical '
                                                                        'triad.',
                                                                   'C': 'Fingertip '
                                                                        'tuft '
                                                                        'fractures '
                                                                        'lack '
                                                                        'significant '
                                                                        'marrow '
                                                                        'embolization '
                                                                        'risk.',
                                                                   'D': 'Lateral '
                                                                        'epicondylitis '
                                                                        'is not a '
                                                                        'fat-embolism '
                                                                        'setting.'}},
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
                                                       'D) Empiric IV antibiotics '
                                                       'alone for a native septic '
                                                       'joint without drainage'],
                                           'answer': 'B) Emergent joint '
                                                     'aspiration/drainage and IV '
                                                     'antibiotics—do not delay for '
                                                     "'trial of NSAIDs'",
                                           'explanation': 'Native septic arthritis '
                                                          'needs emergent '
                                                          'aspiration/drainage plus IV '
                                                          'antibiotics. Antibiotics '
                                                          'without source control are '
                                                          'the dangerous near-miss. '
                                                          'Oral-only therapy or '
                                                          'steroids first are wrong.',
                                           'choice_explanations': {'A': 'Home oral '
                                                                        'antibiotics '
                                                                        'without '
                                                                        'aspiration '
                                                                        'risk joint '
                                                                        'destruction.',
                                                                   'B': 'Suspected '
                                                                        'septic '
                                                                        'arthritis '
                                                                        'requires '
                                                                        'urgent '
                                                                        'synovial '
                                                                        'drainage and '
                                                                        'IV '
                                                                        'antibiotics '
                                                                        'without an '
                                                                        'NSAID delay.',
                                                                   'C': 'Intra-articular '
                                                                        'steroids '
                                                                        'worsen septic '
                                                                        'arthritis.',
                                                                   'D': 'IV '
                                                                        'antibiotics '
                                                                        'are necessary '
                                                                        'and tempting '
                                                                        'as '
                                                                        'sufficient, '
                                                                        'but infected '
                                                                        'native joints '
                                                                        'also need '
                                                                        'drainage—antibiotics '
                                                                        'alone are '
                                                                        'incomplete.'}}],
                               'hard': [{'question': 'A 10-year-old falls on an '
                                                     'outstretched wrist and '
                                                     'radiographs show a fracture line '
                                                     'traversing the distal radial '
                                                     'growth plate. Salter–Harris '
                                                     'fractures involve which anatomic '
                                                     'structure in children?',
                                         'options': ['A) Isolated ligament sprains '
                                                     'without bone or physis '
                                                     'involvement',
                                                     'B) Torus (buckle) metaphyseal '
                                                     'fracture in children that does '
                                                     'not traverse the physis',
                                                     'C) The growth plate (physis) '
                                                     'with variable '
                                                     'metaphyseal/epiphyseal extension',
                                                     'D) Only the metaphysis of adults '
                                                     'after physeal closure'],
                                         'answer': 'C) The growth plate (physis) with '
                                                   'variable metaphyseal/epiphyseal '
                                                   'extension',
                                         'explanation': 'Salter–Harris fractures '
                                                        'involve the physis. Torus '
                                                        'fractures are common '
                                                        'pediatric injuries and the '
                                                        'radiographic near-miss but '
                                                        'spare the growth plate. Adult '
                                                        'metaphyseal-only and pure '
                                                        'sprains are not '
                                                        'Salter–Harris.',
                                         'choice_explanations': {'A': 'Ligament '
                                                                      'sprains without '
                                                                      'physeal '
                                                                      'fracture are '
                                                                      'not '
                                                                      'Salter–Harris '
                                                                      'injuries.',
                                                                 'B': 'Buckle '
                                                                      'fractures are '
                                                                      'frequent in the '
                                                                      'same FOOSH '
                                                                      'pediatric '
                                                                      'setting and '
                                                                      'easy to '
                                                                      'confuse, but '
                                                                      'they are '
                                                                      'cortical '
                                                                      'buckling '
                                                                      'without physeal '
                                                                      'crossing.',
                                                                 'C': 'Salter–Harris '
                                                                      'classification '
                                                                      'describes '
                                                                      'fractures '
                                                                      'involving the '
                                                                      'growth plate '
                                                                      '(physis).',
                                                                 'D': 'After physeal '
                                                                      'closure, '
                                                                      'Salter–Harris '
                                                                      'typing no '
                                                                      'longer '
                                                                      'applies.'}},
                                        {'question': 'A 45-year-old with a large '
                                                     'central disc herniation develops '
                                                     'bilateral leg weakness, perineal '
                                                     'numbness, and new urinary '
                                                     'retention. Which set best '
                                                     'represents cauda equina red '
                                                     'flags needing emergent imaging?',
                                         'options': ['A) Unilateral acute '
                                                     'radiculopathy with severe '
                                                     'sciatica but preserved sphincter '
                                                     'function',
                                                     'B) Isolated mechanical low back '
                                                     'pain improving with activity',
                                                     'C) Mild scoliosis without '
                                                     'neurologic deficit',
                                                     'D) Saddle anesthesia, '
                                                     'bowel/bladder dysfunction, and '
                                                     'bilateral leg symptoms'],
                                         'answer': 'D) Saddle anesthesia, '
                                                   'bowel/bladder dysfunction, and '
                                                   'bilateral leg symptoms',
                                         'explanation': 'Cauda equina red flags are '
                                                        'saddle anesthesia, sphincter '
                                                        'dysfunction, and often '
                                                        'bilateral leg symptoms. '
                                                        'Severe unilateral sciatica is '
                                                        'the radicular near-miss '
                                                        'without cauda equina '
                                                        'compression signs. Mechanical '
                                                        'pain and scoliosis lack '
                                                        'neurologic emergencies.',
                                         'choice_explanations': {'A': 'Unilateral '
                                                                      'radiculopathy '
                                                                      'can be '
                                                                      'agonizing and '
                                                                      'urgent for pain '
                                                                      'control, but '
                                                                      'without '
                                                                      'saddle/sphincter '
                                                                      'deficits it is '
                                                                      'not cauda '
                                                                      'equina '
                                                                      'syndrome.',
                                                                 'B': 'Mechanical back '
                                                                      'pain without '
                                                                      'neurologic loss '
                                                                      'is not cauda '
                                                                      'equina.',
                                                                 'C': 'Mild scoliosis '
                                                                      'without deficit '
                                                                      'is not an '
                                                                      'emergency '
                                                                      'red-flag set.',
                                                                 'D': 'Saddle '
                                                                      'anesthesia, '
                                                                      'bowel/bladder '
                                                                      'change, and '
                                                                      'bilateral leg '
                                                                      'findings are '
                                                                      'cauda equina '
                                                                      'red flags.'}},
                                        {'question': 'A pathologic fracture through a '
                                                     'previously painful bone lesion '
                                                     'in an older adult most suggests '
                                                     'which underlying process?',
                                         'options': ['A) Underlying bone weakened by '
                                                     'metastasis, myeloma, or other '
                                                     'bone disease',
                                                     'B) Osteoporotic fragility '
                                                     'fracture from low-energy trauma '
                                                     'without focal metastatic lesion',
                                                     'C) Normal bone failing only from '
                                                     'extreme high-energy trauma in a '
                                                     'young athlete',
                                                     'D) Simple soft-tissue contusion '
                                                     'without skeletal involvement'],
                                         'answer': 'A) Underlying bone weakened by '
                                                   'metastasis, myeloma, or other bone '
                                                   'disease',
                                         'explanation': 'Pathologic fracture implies '
                                                        'bone weakened by local '
                                                        'disease '
                                                        '(metastasis/myeloma/etc.). '
                                                        'Osteoporotic fragility '
                                                        'fracture is the low-energy '
                                                        'near-miss from generalized '
                                                        'bone weakness without a focal '
                                                        'lesion. High-energy athlete '
                                                        'fractures and contusions '
                                                        'differ.',
                                         'choice_explanations': {'A': 'Pathologic '
                                                                      'fracture occurs '
                                                                      'through bone '
                                                                      'locally '
                                                                      'weakened by '
                                                                      'metastasis, '
                                                                      'myeloma, or '
                                                                      'other focal '
                                                                      'bone disease.',
                                                                 'B': 'Osteoporotic '
                                                                      'fractures also '
                                                                      'follow minimal '
                                                                      'trauma and are '
                                                                      'easily '
                                                                      'conflated; '
                                                                      '“pathologic” '
                                                                      'here emphasizes '
                                                                      'focal '
                                                                      'destructive '
                                                                      'bone disease '
                                                                      'rather than '
                                                                      'generalized '
                                                                      'osteoporosis '
                                                                      'alone.',
                                                                 'C': 'High-energy '
                                                                      'fractures in '
                                                                      'normal bone are '
                                                                      'traumatic, not '
                                                                      'pathologic.',
                                                                 'D': 'Soft-tissue '
                                                                      'contusion is '
                                                                      'not a fracture '
                                                                      'through '
                                                                      'diseased '
                                                                      'bone.'}}],
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
                                            'options': ['A) Deep vein thrombosis '
                                                        'managed with anticoagulation '
                                                        'alone',
                                                        'B) Necrotizing soft-tissue '
                                                        'infection—immediate surgical '
                                                        'exploration/debridement plus '
                                                        'broad empiric antibiotics and '
                                                        'resuscitation',
                                                        'C) Chronic venous stasis '
                                                        'dermatitis without systemic '
                                                        'toxicity',
                                                        'D) Severe non-necrotizing '
                                                        'cellulitis with systemic '
                                                        'inflammatory response but '
                                                        'without gas/crepitus/woody '
                                                        'necrosis'],
                                            'answer': 'B) Necrotizing soft-tissue '
                                                      'infection—immediate surgical '
                                                      'exploration/debridement plus '
                                                      'broad empiric antibiotics and '
                                                      'resuscitation',
                                            'explanation': 'Rapid woody swelling, '
                                                           'bullae, crepitus, gas, and '
                                                           'shock indicate necrotizing '
                                                           'infection needing '
                                                           'immediate surgery. Severe '
                                                           'cellulitis is the '
                                                           'soft-tissue near-miss '
                                                           'without necrotizing '
                                                           'features. DVT and stasis '
                                                           'dermatitis do not fit.',
                                            'choice_explanations': {'A': 'DVT causes '
                                                                         'swelling '
                                                                         'without '
                                                                         'necrotizing '
                                                                         'gas '
                                                                         'infection.',
                                                                    'B': 'Gas-forming, '
                                                                         'rapidly '
                                                                         'progressive, '
                                                                         'toxic '
                                                                         'soft-tissue '
                                                                         'infection is '
                                                                         'necrotizing '
                                                                         'and needs '
                                                                         'immediate '
                                                                         'operative '
                                                                         'debridement '
                                                                         'plus broad '
                                                                         'antibiotics.',
                                                                    'C': 'Venous '
                                                                         'stasis '
                                                                         'changes are '
                                                                         'chronic and '
                                                                         'non-toxic.',
                                                                    'D': 'Severe '
                                                                         'cellulitis '
                                                                         'can produce '
                                                                         'fever and '
                                                                         'limb '
                                                                         'erythema '
                                                                         'that look '
                                                                         'alarming, '
                                                                         'but '
                                                                         'crepitus, '
                                                                         'soft-tissue '
                                                                         'gas, purple '
                                                                         'bullae, and '
                                                                         'woody pain '
                                                                         'out of '
                                                                         'proportion '
                                                                         'indicate '
                                                                         'necrotizing '
                                                                         'disease.'}},
                                           {'question': 'A hemodynamically unstable '
                                                        'blunt trauma patient has an '
                                                        'open-book pelvic fracture and '
                                                        'ongoing bleeding. Which '
                                                        'temporizing musculoskeletal '
                                                        'intervention is most '
                                                        'appropriate while arranging '
                                                        'definitive hemorrhage '
                                                        'control?',
                                            'options': ['A) High-dose thrombolysis to '
                                                        'clear pelvic clot',
                                                        'B) Immediate '
                                                        'angioembolization or pelvic '
                                                        'packing as definitive '
                                                        'hemorrhage control after '
                                                        'binder temporization',
                                                        'C) Apply a pelvic binder (or '
                                                        'sheet) to reduce pelvic '
                                                        'volume and help tamponade '
                                                        'venous/cancellous bleeding',
                                                        'D) Remove all binders and '
                                                        'log-roll repeatedly to '
                                                        'inspect the sacrum only'],
                                            'answer': 'C) Apply a pelvic binder (or '
                                                      'sheet) to reduce pelvic volume '
                                                      'and help tamponade '
                                                      'venous/cancellous bleeding',
                                            'explanation': 'Unstable open-book pelvic '
                                                           'bleeding is temporized '
                                                           'with a binder/sheet. '
                                                           'Angioembolization/packing '
                                                           'are definitive near-miss '
                                                           'interventions that follow '
                                                           'resuscitation/binder, not '
                                                           'replace the immediate '
                                                           'musculoskeletal '
                                                           'temporizing step. Removing '
                                                           'binders or giving '
                                                           'thrombolysis is harmful.',
                                            'choice_explanations': {'A': 'Thrombolysis '
                                                                         'exacerbates '
                                                                         'hemorrhage.',
                                                                    'B': 'Embolization '
                                                                         'or surgical '
                                                                         'packing may '
                                                                         'be required '
                                                                         'for '
                                                                         'definitive '
                                                                         'hemostasis '
                                                                         'and feel '
                                                                         'like “the” '
                                                                         'answer, but '
                                                                         'the '
                                                                         'immediate '
                                                                         'musculoskeletal '
                                                                         'intervention '
                                                                         'asked is '
                                                                         'binder '
                                                                         'application.',
                                                                    'C': 'A pelvic '
                                                                         'binder '
                                                                         'reduces '
                                                                         'pelvic '
                                                                         'volume and '
                                                                         'helps '
                                                                         'tamponade '
                                                                         'bleeding '
                                                                         'while '
                                                                         'definitive '
                                                                         'control is '
                                                                         'arranged.',
                                                                    'D': 'Repeated '
                                                                         'log-rolling '
                                                                         'without a '
                                                                         'binder '
                                                                         'worsens '
                                                                         'pelvic '
                                                                         'bleeding.'}},
                                           {'question': 'After prolonged '
                                                        'immobilization under rubble, '
                                                        'a patient develops dark '
                                                        'urine, CK 85,000 U/L, rising '
                                                        'creatinine, and hyperkalemia. '
                                                        'Which mechanism links muscle '
                                                        'injury to AKI?',
                                            'options': ['A) Hemolysis with '
                                                        'hemoglobinuria causing dark '
                                                        'urine and AKI without extreme '
                                                        'CK from muscle',
                                                        'B) Isolated prerenal azotemia '
                                                        'from ADH excess without '
                                                        'myoglobin',
                                                        'C) Immune-complex '
                                                        'glomerulonephritis from '
                                                        'streptococcal skin infection '
                                                        'only',
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
                                            'explanation': 'Crush injury with CK 85k, '
                                                           'dark urine, hyperkalemia, '
                                                           'and AKI is rhabdomyolysis '
                                                           'from myoglobinuric tubular '
                                                           'injury. Hemoglobinuria '
                                                           'from hemolysis is the '
                                                           'pigment-urine near-miss '
                                                           'without massive CK. '
                                                           'Prerenal ADH states and '
                                                           'post-strep GN differ.',
                                            'choice_explanations': {'A': 'Hemolysis '
                                                                         'can also '
                                                                         'darken urine '
                                                                         'with pigment '
                                                                         'nephropathy, '
                                                                         'so “dark '
                                                                         'urine + AKI” '
                                                                         'overlaps; '
                                                                         'massive CK '
                                                                         'after crush '
                                                                         'injury '
                                                                         'identifies '
                                                                         'muscle '
                                                                         'breakdown '
                                                                         'rather than '
                                                                         'primary '
                                                                         'hemolysis.',
                                                                    'B': 'ADH-mediated '
                                                                         'prerenal '
                                                                         'physiology '
                                                                         'lacks '
                                                                         'myoglobinuric '
                                                                         'cast '
                                                                         'nephropathy '
                                                                         'from rhabdo.',
                                                                    'C': 'Post-streptococcal '
                                                                         'GN is an '
                                                                         'immune-complex '
                                                                         'glomerular '
                                                                         'disease, not '
                                                                         'crush '
                                                                         'rhabdomyolysis.',
                                                                    'D': 'Rhabdomyolysis '
                                                                         'releases '
                                                                         'myoglobin '
                                                                         'that injures '
                                                                         'tubules amid '
                                                                         'volume '
                                                                         'depletion '
                                                                         'and '
                                                                         'dangerous '
                                                                         'hyperkalemia.'}}]},
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
                                                     'B) Ecthyma as a deeper '
                                                     'ulcerative streptococcal '
                                                     'infection related to impetigo',
                                                     'C) Pemphigus vulgaris with '
                                                     'flaccid bullae in middle-aged '
                                                     'adults only',
                                                     'D) Tinea corporis with annular '
                                                     'scale as the sole morphology'],
                                         'answer': 'A) Impetigo, usually from '
                                                   'Staphylococcus aureus or '
                                                   'Streptococcus pyogenes',
                                         'explanation': 'Honey-colored facial crusts '
                                                        'in a child are classic '
                                                        'impetigo (S. aureus/S. '
                                                        'pyogenes). Ecthyma is a '
                                                        'deeper related pyoderma and '
                                                        'the bacterial near-miss. '
                                                        'Pemphigus and tinea have '
                                                        'different '
                                                        'morphology/demographics.',
                                         'choice_explanations': {'A': 'Honey-colored '
                                                                      'crusts are the '
                                                                      'hallmark of '
                                                                      'impetigo from '
                                                                      'staph or strep.',
                                                                 'B': 'Ecthyma is also '
                                                                      'streptococcal '
                                                                      'pyoderma and '
                                                                      'closely '
                                                                      'related, but it '
                                                                      'is '
                                                                      'deeper/ulcerative '
                                                                      'rather than the '
                                                                      'classic '
                                                                      'superficial '
                                                                      'honey-crusted '
                                                                      'impetigo '
                                                                      'picture.',
                                                                 'C': 'Pemphigus '
                                                                      'causes flaccid '
                                                                      'bullae/mucosal '
                                                                      'erosions in '
                                                                      'older patients, '
                                                                      'not pediatric '
                                                                      'honey crusts.',
                                                                 'D': 'Tinea corporis '
                                                                      'is annular '
                                                                      'scale without '
                                                                      'honey-colored '
                                                                      'impetigo '
                                                                      'crusts.'}},
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
                                                     'D) Atypical (dysplastic) nevus '
                                                     'screening using similar '
                                                     'ABCDE-type morphologic concern'],
                                         'answer': 'B) Melanoma warning features '
                                                   '(Asymmetry, Border, Color, '
                                                   'Diameter, Evolving)',
                                         'explanation': 'ABCDE screens pigmented '
                                                        'lesions for melanoma. '
                                                        'Dysplastic nevi are assessed '
                                                        'with overlapping morphologic '
                                                        'red flags and are the '
                                                        'pigmented-lesion near-miss. '
                                                        'Psoriasis and scabies tools '
                                                        'differ.',
                                         'choice_explanations': {'A': 'Psoriasis '
                                                                      'grading is not '
                                                                      'ABCDE melanoma '
                                                                      'screening.',
                                                                 'B': 'ABCDE criteria '
                                                                      'flag '
                                                                      'melanoma-concerning '
                                                                      'pigmented '
                                                                      'lesions.',
                                                                 'C': 'Scabies '
                                                                      'assessment '
                                                                      'looks for '
                                                                      'burrows/itch, '
                                                                      'not ABCDE.',
                                                                 'D': 'Dysplastic nevi '
                                                                      'also trigger '
                                                                      'ABCDE-like '
                                                                      'concern and '
                                                                      'biopsy '
                                                                      'decisions, so '
                                                                      'pigmented-lesion '
                                                                      'screening '
                                                                      'overlaps; '
                                                                      'ABCDE’s primary '
                                                                      'taught target '
                                                                      'is melanoma '
                                                                      'warning '
                                                                      'features.'}},
                                        {'question': 'Auspitz sign (pinpoint bleeding '
                                                     'when scale is removed) is '
                                                     'classically associated with '
                                                     'which disease?',
                                         'options': ['A) Urticaria with transient '
                                                     'wheals',
                                                     'B) Seborrheic dermatitis with '
                                                     'greasy scale in sebaceous '
                                                     'distribution without true '
                                                     'Auspitz phenomenon',
                                                     'C) Psoriasis vulgaris with '
                                                     'silvery scale over plaques',
                                                     'D) Atopic dermatitis without '
                                                     'plaques'],
                                         'answer': 'C) Psoriasis vulgaris with silvery '
                                                   'scale over plaques',
                                         'explanation': 'Auspitz sign is classic for '
                                                        'psoriasis. Seborrheic '
                                                        'dermatitis is a scaly '
                                                        'near-miss in a different '
                                                        'distribution without classic '
                                                        'Auspitz. Atopic dermatitis '
                                                        'and urticaria differ.',
                                         'choice_explanations': {'A': 'Urticaria is '
                                                                      'transient '
                                                                      'wheals without '
                                                                      'scale removal '
                                                                      'bleeding.',
                                                                 'B': 'Seborrheic '
                                                                      'dermatitis is '
                                                                      'also scaly and '
                                                                      'commonly '
                                                                      'confused with '
                                                                      'psoriasis, but '
                                                                      'Auspitz sign is '
                                                                      'the '
                                                                      'psoriasis-associated '
                                                                      'finding.',
                                                                 'C': 'Pinpoint '
                                                                      'bleeding on '
                                                                      'scale removal '
                                                                      '(Auspitz) is '
                                                                      'classically '
                                                                      'linked to '
                                                                      'psoriasis '
                                                                      'plaques.',
                                                                 'D': 'Atopic '
                                                                      'dermatitis is '
                                                                      'eczematous '
                                                                      'without '
                                                                      'Auspitz-defined '
                                                                      'silvery '
                                                                      'plaques.'}}],
                               'medium': [{'question': 'Scabies pruritus is '
                                                       'characteristically worst at '
                                                       'which time?',
                                           'options': ['A) Intense pruritus from '
                                                       'atopic dermatitis that may '
                                                       'also worsen at night without '
                                                       'burrows',
                                                       'B) Only during vigorous '
                                                       'exercise in cold air',
                                                       'C) Exclusively after sun '
                                                       'exposure on the face',
                                                       'D) At night, with burrows in '
                                                       'finger webs and genital skin '
                                                       'often involved'],
                                           'answer': 'D) At night, with burrows in '
                                                     'finger webs and genital skin '
                                                     'often involved',
                                           'explanation': 'Scabies itch is '
                                                          'characteristically '
                                                          'nocturnal with burrows in '
                                                          'classic sites. Atopic '
                                                          'dermatitis also itches at '
                                                          'night and is the pruritus '
                                                          'near-miss, but '
                                                          'burrows/distribution '
                                                          'distinguish scabies. '
                                                          'Exercise-cold and sun-only '
                                                          'patterns are wrong.',
                                           'choice_explanations': {'A': 'Atopic '
                                                                        'dermatitis '
                                                                        'frequently '
                                                                        'worsens at '
                                                                        'night too, '
                                                                        'creating '
                                                                        'timing '
                                                                        'overlap; '
                                                                        'burrows and '
                                                                        'acral/genital '
                                                                        'distribution '
                                                                        'separate '
                                                                        'scabies.',
                                                                   'B': 'Cold-air '
                                                                        'exercise itch '
                                                                        'is not the '
                                                                        'scabies '
                                                                        'pattern.',
                                                                   'C': 'Isolated '
                                                                        'facial '
                                                                        'post-sun itch '
                                                                        'is not '
                                                                        'scabies.',
                                                                   'D': 'Scabies '
                                                                        'causes '
                                                                        'night-predominant '
                                                                        'itch with '
                                                                        'burrows in '
                                                                        'webs and '
                                                                        'genital '
                                                                        'skin.'}},
                                          {'question': 'Bacterial cellulitis of the '
                                                       'leg typically features which '
                                                       'clinical pattern?',
                                           'options': ['A) Expanding erythematous, '
                                                       'warm, tender plaque often with '
                                                       'fever',
                                                       'B) Erysipelas as a more '
                                                       'superficial sharply demarcated '
                                                       'streptococcal dermal infection',
                                                       'C) Annular scaly edge without '
                                                       'warmth suggesting tinea only',
                                                       'D) Noninflammatory palpable '
                                                       'purpura of vasculitis alone'],
                                           'answer': 'A) Expanding erythematous, warm, '
                                                     'tender plaque often with fever',
                                           'explanation': 'Cellulitis is an expanding '
                                                          'warm tender erythematous '
                                                          'plaque ± fever. Erysipelas '
                                                          'is a closely related '
                                                          'superficial bacterial '
                                                          'dermal infection and the '
                                                          'morphologic near-miss. '
                                                          'Tinea and vasculitis '
                                                          'differ.',
                                           'choice_explanations': {'A': 'Bacterial '
                                                                        'cellulitis '
                                                                        'presents as '
                                                                        'an expanding '
                                                                        'warm, tender '
                                                                        'erythematous '
                                                                        'plaque, often '
                                                                        'with fever.',
                                                                   'B': 'Erysipelas is '
                                                                        'also acute '
                                                                        'bacterial '
                                                                        'skin '
                                                                        'infection and '
                                                                        'easily '
                                                                        'conflated; it '
                                                                        'is typically '
                                                                        'more '
                                                                        'superficial '
                                                                        'and sharply '
                                                                        'demarcated, '
                                                                        'often on the '
                                                                        'face/legs.',
                                                                   'C': 'Annular scale '
                                                                        'without '
                                                                        'warmth '
                                                                        'suggests '
                                                                        'dermatophyte '
                                                                        'infection.',
                                                                   'D': 'Palpable '
                                                                        'purpura '
                                                                        'indicates '
                                                                        'vasculitis, '
                                                                        'not typical '
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
                                                       'D) Staphylococcal scalded skin '
                                                       'syndrome with superficial '
                                                       'blistering that can mimic '
                                                       'widespread detachment'],
                                           'answer': 'B) Severe mucocutaneous adverse '
                                                     'drug reactions with epidermal '
                                                     'necrosis',
                                           'explanation': 'SJS/TEN are severe '
                                                          'drug-induced mucocutaneous '
                                                          'reactions with epidermal '
                                                          'necrosis. SSSS can mimic '
                                                          'widespread skin detachment '
                                                          'and is the blistering '
                                                          'near-miss, but it is '
                                                          'toxin-mediated superficial '
                                                          'splitting without '
                                                          'full-thickness TEN '
                                                          'necrosis/severe mucosal '
                                                          'drug reaction framing. '
                                                          'Viral exanthem and '
                                                          'localized contact '
                                                          'dermatitis differ.',
                                           'choice_explanations': {'A': 'Mild viral '
                                                                        'exanthems '
                                                                        'lack '
                                                                        'epidermal '
                                                                        'necrosis '
                                                                        'syndromes.',
                                                                   'B': 'SJS/TEN are '
                                                                        'severe drug '
                                                                        'reactions '
                                                                        'featuring '
                                                                        'mucosal '
                                                                        'disease and '
                                                                        'epidermal '
                                                                        'necrosis.',
                                                                   'C': 'Localized '
                                                                        'contact '
                                                                        'dermatitis is '
                                                                        'not SJS/TEN.',
                                                                   'D': 'SSSS also '
                                                                        'causes '
                                                                        'sheet-like '
                                                                        'peeling and '
                                                                        'is a major '
                                                                        'differential '
                                                                        'for “skin '
                                                                        'coming off,” '
                                                                        'but cleavage '
                                                                        'is more '
                                                                        'superficial '
                                                                        'and the '
                                                                        'drug–mucosal '
                                                                        'necrosis '
                                                                        'concept '
                                                                        'defines '
                                                                        'SJS/TEN.'}}],
                               'hard': [{'question': 'A positive Nikolsky sign '
                                                     '(sheet-like epidermal detachment '
                                                     'with gentle pressure) can be '
                                                     'seen in which condition among '
                                                     'the options?',
                                         'options': ['A) Vitiligo without blistering',
                                                     'B) Bullous pemphigoid with tense '
                                                     'bullae and typically negative '
                                                     'Nikolsky sign',
                                                     'C) Pemphigus vulgaris (and '
                                                     'similarly in '
                                                     'SJS/TEN/staphylococcal scalded '
                                                     'skin in related contexts)',
                                                     'D) Chronic plaque psoriasis with '
                                                     'adherent scale only'],
                                         'answer': 'C) Pemphigus vulgaris (and '
                                                   'similarly in '
                                                   'SJS/TEN/staphylococcal scalded '
                                                   'skin in related contexts)',
                                         'explanation': 'Nikolsky sign can be positive '
                                                        'in pemphigus (and '
                                                        'SJS/TEN/SSSS). Bullous '
                                                        'pemphigoid is the autoimmune '
                                                        'blistering near-miss usually '
                                                        'Nikolsky-negative with tense '
                                                        'bullae. Psoriasis and '
                                                        'vitiligo do not blister this '
                                                        'way.',
                                         'choice_explanations': {'A': 'Vitiligo is '
                                                                      'pigment loss '
                                                                      'without '
                                                                      'blistering.',
                                                                 'B': 'Bullous '
                                                                      'pemphigoid is '
                                                                      'the other major '
                                                                      'autoimmune '
                                                                      'bullous disease '
                                                                      'and commonly '
                                                                      'confused, but '
                                                                      'tense blisters '
                                                                      'and usually '
                                                                      'negative '
                                                                      'Nikolsky '
                                                                      'distinguish it '
                                                                      'from pemphigus.',
                                                                 'C': 'Nikolsky-positive '
                                                                      'sheet-like '
                                                                      'detachment is '
                                                                      'seen in '
                                                                      'pemphigus '
                                                                      'vulgaris (and '
                                                                      'related '
                                                                      'necrolytic/toxin '
                                                                      'syndromes).',
                                                                 'D': 'Psoriasis scale '
                                                                      'does not '
                                                                      'produce '
                                                                      'Nikolsky '
                                                                      'detachment.'}},
                                        {'question': 'An expanding erythematous patch '
                                                     'with central clearing after a '
                                                     'tick exposure in an endemic area '
                                                     'most suggests which diagnosis?',
                                         'options': ['A) Southern tick-associated rash '
                                                     'illness (STARI) with a similar '
                                                     'expanding annular tick-bite rash',
                                                     'B) Fixed drug eruption recurring '
                                                     'at the identical site only after '
                                                     'the same drug',
                                                     'C) Tinea versicolor limited to '
                                                     'seborrheic yeast overgrowth on '
                                                     'the trunk',
                                                     'D) Erythema migrans of early '
                                                     'Lyme disease (Borrelia '
                                                     'burgdorferi)'],
                                         'answer': 'D) Erythema migrans of early Lyme '
                                                   'disease (Borrelia burgdorferi)',
                                         'explanation': 'Expanding erythema with '
                                                        'central clearing after tick '
                                                        'exposure is erythema migrans '
                                                        'of Lyme. STARI can look '
                                                        'nearly identical and is the '
                                                        'tick-rash near-miss. Fixed '
                                                        'drug eruption and tinea '
                                                        'versicolor differ.',
                                         'choice_explanations': {'A': 'STARI produces '
                                                                      'a similar '
                                                                      'expanding '
                                                                      'targetoid '
                                                                      'tick-associated '
                                                                      'rash, so '
                                                                      'morphology '
                                                                      'overlaps; '
                                                                      'endemic Lyme '
                                                                      'context and '
                                                                      'Borrelia '
                                                                      'association '
                                                                      'define erythema '
                                                                      'migrans '
                                                                      'teaching here.',
                                                                 'B': 'Fixed drug '
                                                                      'eruption is '
                                                                      'drug-timed and '
                                                                      'recurrent at '
                                                                      'one site, not '
                                                                      'tick-linked '
                                                                      'expanding EM.',
                                                                 'C': 'Tinea '
                                                                      'versicolor '
                                                                      'causes '
                                                                      'hypo/hyperpigmented '
                                                                      'truncal '
                                                                      'macules, not EM '
                                                                      'after ticks.',
                                                                 'D': 'Expanding '
                                                                      'annular '
                                                                      'erythema after '
                                                                      'tick bite in an '
                                                                      'endemic area is '
                                                                      'erythema '
                                                                      'migrans of '
                                                                      'early Lyme '
                                                                      'disease.'}},
                                        {'question': 'Which bedside clue most helps '
                                                     'distinguish necrotizing '
                                                     'soft-tissue infection from '
                                                     'routine cellulitis?',
                                         'options': ['A) Pain out of proportion, rapid '
                                                     'progression, and systemic '
                                                     'toxicity ± crepitus',
                                                     'B) Severe cellulitis with fever '
                                                     'and leukocytosis but without '
                                                     'necrosis/crepitus/pain out of '
                                                     'proportion',
                                                     'C) Mild itch without tenderness '
                                                     'or fever',
                                                     'D) Chronic bilateral venous '
                                                     'stasis changes over years'],
                                         'answer': 'A) Pain out of proportion, rapid '
                                                   'progression, and systemic toxicity '
                                                   '± crepitus',
                                         'explanation': 'Necrotizing infection clues '
                                                        'are pain out of proportion, '
                                                        'rapid spread, toxicity ± '
                                                        'crepitus. Severe cellulitis '
                                                        'is the soft-tissue near-miss '
                                                        'lacking those necrotizing '
                                                        'markers. Itch-only and '
                                                        'chronic stasis differ.',
                                         'choice_explanations': {'A': 'Pain out of '
                                                                      'proportion, '
                                                                      'rapid '
                                                                      'progression, '
                                                                      'and toxicity (± '
                                                                      'crepitus) '
                                                                      'distinguish '
                                                                      'necrotizing '
                                                                      'infection from '
                                                                      'routine '
                                                                      'cellulitis.',
                                                                 'B': 'Cellulitis can '
                                                                      'be febrile and '
                                                                      'look severe, '
                                                                      'creating '
                                                                      'overlap; the '
                                                                      'disproportionate '
                                                                      'pain, pace, and '
                                                                      'crepitus/gas '
                                                                      'are the '
                                                                      'separators.',
                                                                 'C': 'Mild itch '
                                                                      'without '
                                                                      'tenderness is '
                                                                      'not necrotizing '
                                                                      'infection.',
                                                                 'D': 'Chronic venous '
                                                                      'stasis is '
                                                                      'bilateral and '
                                                                      'indolent.'}}],
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
                                                        'D) Meningococcemia with '
                                                        'petechiae/purpura without '
                                                        'frank purpura fulminans '
                                                        'necrosis'],
                                            'answer': 'B) Purpura fulminans from '
                                                      'septicemia-associated '
                                                      'disseminated intravascular '
                                                      'coagulation',
                                            'explanation': 'Retiform purpura '
                                                           'progressing to necrosis '
                                                           'with meningococcal sepsis '
                                                           'indicates purpura '
                                                           'fulminans from DIC. '
                                                           'Meningococcemia with '
                                                           'petechiae is the '
                                                           'overlapping infection '
                                                           'near-miss before fulminant '
                                                           'necrotic purpura. '
                                                           'Psoriasis and roseola do '
                                                           'not fit.',
                                            'choice_explanations': {'A': 'Psoriasis '
                                                                         'plaques are '
                                                                         'not acute '
                                                                         'retiform '
                                                                         'necrotic '
                                                                         'purpura.',
                                                                    'B': 'Rapid '
                                                                         'retiform '
                                                                         'purpura with '
                                                                         'necrosis in '
                                                                         'meningococcal '
                                                                         'septic shock '
                                                                         'illustrates '
                                                                         'purpura '
                                                                         'fulminans '
                                                                         'from DIC.',
                                                                    'C': 'Roseola is a '
                                                                         'self-limited '
                                                                         'viral '
                                                                         'exanthem '
                                                                         'without DIC '
                                                                         'necrosis.',
                                                                    'D': 'Meningococcal '
                                                                         'bacteremia '
                                                                         'commonly '
                                                                         'causes '
                                                                         'petechial/purpuric '
                                                                         'rashes and '
                                                                         'overlaps, '
                                                                         'but '
                                                                         'progressive '
                                                                         'cutaneous '
                                                                         'necrosis '
                                                                         'with DIC '
                                                                         'defines '
                                                                         'purpura '
                                                                         'fulminans.'}},
                                           {'question': 'A dialysis patient with '
                                                        'secondary hyperparathyroidism '
                                                        'develops exquisitely painful '
                                                        'retiform purpura and necrotic '
                                                        'plaques on the thighs and '
                                                        'abdomen. Biopsy shows '
                                                        'vascular calcification. Which '
                                                        'diagnosis fits?',
                                            'options': ['A) Livedo reticularis from '
                                                        'cold exposure without vessel '
                                                        'calcification',
                                                        'B) Warfarin-induced necrosis '
                                                        'with painful purpura in '
                                                        'susceptible patients on '
                                                        'anticoagulation',
                                                        'C) Calciphylaxis (calcific '
                                                        'uremic arteriolopathy) in '
                                                        'end-stage kidney disease',
                                                        'D) Leukocytoclastic '
                                                        'vasculitis from drug '
                                                        'hypersensitivity as the first '
                                                        'choice always'],
                                            'answer': 'C) Calciphylaxis (calcific '
                                                      'uremic arteriolopathy) in '
                                                      'end-stage kidney disease',
                                            'explanation': 'Painful necrotic plaques '
                                                           'with vascular '
                                                           'calcification in '
                                                           'dialysis/hyperparathyroidism '
                                                           'indicate calciphylaxis. '
                                                           'Warfarin necrosis is a '
                                                           'major necrotic-purpura '
                                                           'near-miss with different '
                                                           'timing/mechanism. LCV and '
                                                           'benign livedo differ.',
                                            'choice_explanations': {'A': 'Cold-induced '
                                                                         'livedo lacks '
                                                                         'calcific '
                                                                         'vessel '
                                                                         'disease and '
                                                                         'necrotic '
                                                                         'plaques of '
                                                                         'calciphylaxis.',
                                                                    'B': 'Warfarin-induced '
                                                                         'necrosis '
                                                                         'also causes '
                                                                         'painful '
                                                                         'purpuric '
                                                                         'necrosis and '
                                                                         'is a key '
                                                                         'differential, '
                                                                         'but biopsy '
                                                                         'calcification '
                                                                         'plus uremic '
                                                                         'hyperparathyroid '
                                                                         'context '
                                                                         'points to '
                                                                         'calciphylaxis.',
                                                                    'C': 'Exquisitely '
                                                                         'painful '
                                                                         'retiform '
                                                                         'necrosis '
                                                                         'with '
                                                                         'vascular '
                                                                         'calcification '
                                                                         'in ESKD is '
                                                                         'calciphylaxis.',
                                                                    'D': 'LCV is '
                                                                         'palpable '
                                                                         'purpura from '
                                                                         'leukocytoclastic '
                                                                         'inflammation, '
                                                                         'not calcific '
                                                                         'arteriolopathy.'}},
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
                                            'options': ['A) Kawasaki disease with '
                                                        'prolonged fever and '
                                                        'mucocutaneous inflammation in '
                                                        'young children',
                                                        'B) Solely mosquito bites '
                                                        'without bacterial toxin',
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
                                            'explanation': 'Toxic shock syndrome '
                                                           'associates with tampon use '
                                                           'or toxin-producing '
                                                           'staph/strep infections '
                                                           '(including wounds). '
                                                           'Kawasaki disease shares '
                                                           'mucocutaneous fever themes '
                                                           'in children and is the '
                                                           'inflammatory near-miss. '
                                                           'Mosquito bites and tinea '
                                                           'do not cause TSS.',
                                            'choice_explanations': {'A': 'Kawasaki '
                                                                         'disease also '
                                                                         'features '
                                                                         'fever and '
                                                                         'mucocutaneous '
                                                                         'inflammation '
                                                                         'and can be '
                                                                         'confused in '
                                                                         'pediatrics, '
                                                                         'but the '
                                                                         'menstrual '
                                                                         'tampon/toxin-shock '
                                                                         'picture is '
                                                                         'TSS, not '
                                                                         'Kawasaki.',
                                                                    'B': 'Mosquito '
                                                                         'bites do not '
                                                                         'produce TSS '
                                                                         'toxin '
                                                                         'syndromes.',
                                                                    'C': 'Tinea pedis '
                                                                         'is localized '
                                                                         'fungal '
                                                                         'disease '
                                                                         'without TSS.',
                                                                    'D': 'TSS links to '
                                                                         'tampon use '
                                                                         'or '
                                                                         'toxin-producing '
                                                                         'staphylococcal/streptococcal '
                                                                         'infections '
                                                                         'such as '
                                                                         'postoperative '
                                                                         'wounds.'}}]},
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
                                               'B) Retained placental tissue (one of '
                                               'the other “T”s) causing ongoing '
                                               'postpartum bleeding',
                                               'C) Amniotic fluid embolism as the '
                                               'leading everyday cause',
                                               'D) Inherited hemophilia A presenting '
                                               'first at delivery in all cases'],
                                   'answer': 'A) Uterine atony from inadequate '
                                             'myometrial contraction',
                                   'explanation': 'Uterine atony is the most common '
                                                  'PPH cause. Retained tissue is '
                                                  'another common “T” and the '
                                                  'obstetric near-miss, but atony '
                                                  'leads in frequency. AFE and '
                                                  'universal hemophilia are wrong.',
                                   'choice_explanations': {'A': 'Primary PPH is most '
                                                                'often from uterine '
                                                                'atony with poor '
                                                                'myometrial '
                                                                'contraction.',
                                                           'B': 'Retained products '
                                                                'also cause PPH and '
                                                                'are part of the 4 Ts, '
                                                                'so they are easy to '
                                                                'select; numerically, '
                                                                'atony remains the '
                                                                'most common '
                                                                'mechanism.',
                                                           'C': 'Amniotic fluid '
                                                                'embolism is rare, not '
                                                                'the leading everyday '
                                                                'PPH cause.',
                                                           'D': 'Hemophilia A is not '
                                                                'the usual first '
                                                                'presentation '
                                                                'explaining most '
                                                                'PPH.'}},
                                  {'question': 'Risk of ectopic pregnancy rises most '
                                               'clearly after which history?',
                                   'options': ['A) Exclusive formula feeding in a '
                                               'prior child',
                                               'B) Prior pelvic inflammatory disease / '
                                               'tubal damage or prior ectopic '
                                               'pregnancy',
                                               'C) First-trimester prenatal vitamin '
                                               'use',
                                               'D) Assisted reproductive '
                                               'technology/IVF pregnancy, which also '
                                               'elevates ectopic risk'],
                                   'answer': 'B) Prior pelvic inflammatory disease / '
                                             'tubal damage or prior ectopic pregnancy',
                                   'explanation': 'PID/tubal damage and prior ectopic '
                                                  'most clearly raise ectopic risk. '
                                                  'IVF also increases ectopic risk and '
                                                  'is the reproductive near-miss. '
                                                  'Formula feeding and prenatal '
                                                  'vitamins do not.',
                                   'choice_explanations': {'A': 'Formula feeding is '
                                                                'unrelated to ectopic '
                                                                'risk.',
                                                           'B': 'Tubal damage from PID '
                                                                'or prior ectopic '
                                                                'pregnancy most '
                                                                'clearly elevates '
                                                                'ectopic risk.',
                                                           'C': 'Prenatal vitamins do '
                                                                'not cause ectopic '
                                                                'pregnancy.',
                                                           'D': 'IVF/ART also '
                                                                'increases ectopic '
                                                                'probability and is a '
                                                                'true risk factor, but '
                                                                'classic highest-yield '
                                                                'history remains '
                                                                'PID/tubal injury or '
                                                                'prior ectopic.'}},
                                  {'question': 'Fetal heart tones are often first '
                                               'detectable by handheld Doppler around '
                                               'which gestational age range?',
                                   'options': ['A) Only after 28 weeks in all '
                                               'pregnancies',
                                               'B) Transvaginal ultrasound cardiac '
                                               'activity often detectable earlier '
                                               '(~5.5–6 weeks) than handheld Doppler',
                                               'C) Approximately 10–12 weeks’ '
                                               'gestation in many pregnancies',
                                               'D) At fertilization on day 0 reliably'],
                                   'answer': 'C) Approximately 10–12 weeks’ gestation '
                                             'in many pregnancies',
                                   'explanation': 'Handheld Doppler often detects '
                                                  'fetal heart tones around 10–12 '
                                                  'weeks. TVUS detects cardiac '
                                                  'activity earlier and is the '
                                                  'dating/technology near-miss. Day-0 '
                                                  'and “only after 28 weeks” are '
                                                  'wrong.',
                                   'choice_explanations': {'A': 'Waiting until 28 '
                                                                'weeks is far later '
                                                                'than typical Doppler '
                                                                'detection.',
                                                           'B': 'Ultrasound detects '
                                                                'cardiac activity '
                                                                'earlier, so students '
                                                                'may answer “6 weeks,” '
                                                                'but the stem '
                                                                'specifies handheld '
                                                                'Doppler timing.',
                                                           'C': 'Handheld Doppler '
                                                                'commonly first '
                                                                'detects fetal heart '
                                                                'tones near 10–12 '
                                                                'weeks.',
                                                           'D': 'Fertilization day has '
                                                                'no audible fetal '
                                                                'heart tones.'}}],
                         'medium': [{'question': 'Pre-eclampsia is defined as new '
                                                 'hypertension after 20 weeks plus '
                                                 'which additional element '
                                                 'conceptually?',
                                     'options': ['A) Gestational hypertension with new '
                                                 'BP elevation after 20 weeks without '
                                                 'proteinuria or end-organ criteria',
                                                 'B) Chronic hypertension documented '
                                                 'before conception only',
                                                 'C) Isolated gestational diabetes '
                                                 'without blood pressure change',
                                                 'D) Proteinuria and/or end-organ '
                                                 'dysfunction (e.g., thrombocytopenia, '
                                                 'renal/liver injury, neurologic '
                                                 'symptoms)'],
                                     'answer': 'D) Proteinuria and/or end-organ '
                                               'dysfunction (e.g., thrombocytopenia, '
                                               'renal/liver injury, neurologic '
                                               'symptoms)',
                                     'explanation': 'Pre-eclampsia is new HTN after 20 '
                                                    'weeks plus proteinuria and/or '
                                                    'end-organ dysfunction. '
                                                    'Gestational hypertension is the '
                                                    'BP near-miss without those '
                                                    'features. Chronic HTN and GDM '
                                                    'alone are different diagnoses.',
                                     'choice_explanations': {'A': 'Gestational '
                                                                  'hypertension also '
                                                                  'presents as new '
                                                                  'pregnancy-related '
                                                                  'HTN after 20 weeks '
                                                                  'and is commonly '
                                                                  'confused; absence '
                                                                  'of '
                                                                  'proteinuria/end-organ '
                                                                  'criteria keeps it '
                                                                  'from pre-eclampsia.',
                                                             'B': 'Chronic '
                                                                  'hypertension '
                                                                  'predates 20 '
                                                                  'weeks/conception '
                                                                  'labeling.',
                                                             'C': 'Gestational '
                                                                  'diabetes is a '
                                                                  'glucose disorder, '
                                                                  'not pre-eclampsia '
                                                                  'criteria.',
                                                             'D': 'Pre-eclampsia '
                                                                  'requires new '
                                                                  'hypertension after '
                                                                  '20 weeks plus '
                                                                  'proteinuria and/or '
                                                                  'end-organ '
                                                                  'dysfunction.'}},
                                    {'question': 'The classic clinical combination '
                                                 'raising concern for ectopic '
                                                 'pregnancy is which?',
                                     'options': ['A) Amenorrhea/positive pregnancy '
                                                 'test, unilateral pelvic pain, and '
                                                 'vaginal bleeding',
                                                 'B) Threatened miscarriage with '
                                                 'intrauterine pregnancy, cramping, '
                                                 'and bleeding without ectopic '
                                                 'implantation',
                                                 'C) Painless term contractions with '
                                                 'intact membranes only',
                                                 'D) Postmenopausal hot flashes '
                                                 'without pregnancy'],
                                     'answer': 'A) Amenorrhea/positive pregnancy test, '
                                               'unilateral pelvic pain, and vaginal '
                                               'bleeding',
                                     'explanation': 'Ectopic concern classically '
                                                    'combines positive pregnancy test, '
                                                    'unilateral pain, and bleeding. '
                                                    'Threatened abortion shares early '
                                                    'pregnancy bleeding/pain and is '
                                                    'the obstetric near-miss with an '
                                                    'intrauterine gestation. Term '
                                                    'labor and menopause differ.',
                                     'choice_explanations': {'A': 'Positive pregnancy '
                                                                  'test with '
                                                                  'unilateral pelvic '
                                                                  'pain and bleeding '
                                                                  'is the classic '
                                                                  'ectopic triad.',
                                                             'B': 'Threatened '
                                                                  'miscarriage also '
                                                                  'causes early '
                                                                  'pregnancy bleeding '
                                                                  '± pain, so symptoms '
                                                                  'overlap; unilateral '
                                                                  'peritoneal findings '
                                                                  'and empty '
                                                                  'uterus/ectopic risk '
                                                                  'distinguish ectopic '
                                                                  'concern.',
                                                             'C': 'Term contractions '
                                                                  'are labor, not '
                                                                  'ectopic syndrome.',
                                                             'D': 'Postmenopausal '
                                                                  'symptoms imply no '
                                                                  'pregnancy.'}},
                                    {'question': 'Shoulder dystocia refers to which '
                                                 'obstetric emergency?',
                                     'options': ['A) Cord prolapse after membrane '
                                                 'rupture only',
                                                 'B) Impaction of the fetal shoulder '
                                                 'behind the pubic symphysis after '
                                                 'delivery of the head',
                                                 'C) Retained placenta without any '
                                                 'shoulder involvement',
                                                 'D) Breech delivery with entrapped '
                                                 'aftercoming head as another delivery '
                                                 'dystocia emergency'],
                                     'answer': 'B) Impaction of the fetal shoulder '
                                               'behind the pubic symphysis after '
                                               'delivery of the head',
                                     'explanation': 'Shoulder dystocia is anterior '
                                                    'shoulder impaction behind the '
                                                    'symphysis after the head '
                                                    'delivers. Breech with entrapped '
                                                    'head is another dystocia '
                                                    'emergency and the labor '
                                                    'near-miss. Cord prolapse and '
                                                    'retained placenta are different '
                                                    'emergencies.',
                                     'choice_explanations': {'A': 'Cord prolapse is '
                                                                  'cord '
                                                                  'presentation/compression, '
                                                                  'not shoulder '
                                                                  'impaction.',
                                                             'B': 'Shoulder dystocia '
                                                                  'is failure of the '
                                                                  'shoulders to '
                                                                  'deliver due to '
                                                                  'impaction behind '
                                                                  'the pubic symphysis '
                                                                  'after the head is '
                                                                  'out.',
                                                             'C': 'Retained placenta '
                                                                  'is a third-stage '
                                                                  'problem.',
                                                             'D': 'Breech head '
                                                                  'entrapment is also '
                                                                  'an acute delivery '
                                                                  'dystocia and can be '
                                                                  'confused under '
                                                                  '“stuck delivery,” '
                                                                  'but shoulder '
                                                                  'dystocia '
                                                                  'specifically '
                                                                  'follows cephalic '
                                                                  'head delivery.'}}],
                         'hard': [{'question': 'In obstetrics, magnesium sulfate is '
                                               'primarily indicated for which purpose '
                                               'among the options?',
                                   'options': ['A) Treatment of postpartum hemorrhage '
                                               'from atony as the primary uterotonic',
                                               'B) Short-term fetal neuroprotection '
                                               'with magnesium before early preterm '
                                               'delivery',
                                               'C) Seizure prophylaxis/treatment in '
                                               'pre-eclampsia/eclampsia',
                                               'D) First-line tocolysis for weeks of '
                                               'preterm labor in all guidelines '
                                               'universally'],
                                   'answer': 'C) Seizure prophylaxis/treatment in '
                                             'pre-eclampsia/eclampsia',
                                   'explanation': 'In obstetrics, magnesium sulfate’s '
                                                  'primary listed role here is '
                                                  'eclamptic seizure '
                                                  'prophylaxis/treatment. Fetal '
                                                  'neuroprotection is a related '
                                                  'evidence-based magnesium use and '
                                                  'the indication near-miss. It is not '
                                                  'universal long-term tocolysis or a '
                                                  'uterotonic for PPH.',
                                   'choice_explanations': {'A': 'Uterotonics for atony '
                                                                'are '
                                                                'oxytocin/ergot/prostaglandins, '
                                                                'not magnesium.',
                                                           'B': 'Magnesium also '
                                                                'provides fetal '
                                                                'neuroprotection '
                                                                'before early preterm '
                                                                'birth, so dual '
                                                                'obstetric uses create '
                                                                'confusion; the stem’s '
                                                                '“primarily” among '
                                                                'options points to '
                                                                'eclampsia '
                                                                'prevention/treatment.',
                                                           'C': 'Magnesium sulfate is '
                                                                'primarily used for '
                                                                'seizure '
                                                                'prophylaxis/treatment '
                                                                'in '
                                                                'pre-eclampsia/eclampsia.',
                                                           'D': 'Magnesium is not '
                                                                'reliable prolonged '
                                                                'first-line tocolysis '
                                                                'across guidelines.'}},
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
                                   'explanation': 'Placenta previa classically causes '
                                                  'painless bright third-trimester '
                                                  'bleeding with a soft uterus. '
                                                  'Abruption is the bleeding near-miss '
                                                  'with pain and hypertonic uterus. '
                                                  'Polyps and lochia differ.',
                                   'choice_explanations': {'A': 'Abruption also causes '
                                                                'third-trimester '
                                                                'hemorrhage and is the '
                                                                'critical '
                                                                'differential; pain '
                                                                'and a rigid uterus '
                                                                'distinguish abruption '
                                                                'from previa.',
                                                           'B': 'Cervical polyps cause '
                                                                'lighter '
                                                                'intermenstrual '
                                                                'spotting, not classic '
                                                                'previa hemorrhage.',
                                                           'C': 'Lochia is postpartum, '
                                                                'not antepartum previa '
                                                                'bleeding.',
                                                           'D': 'Previa bleeding is '
                                                                'typically painless '
                                                                'and bright red in the '
                                                                'second/third '
                                                                'trimester.'}},
                                  {'question': 'A pre-eclamptic patient at 34 weeks '
                                               'develops RUQ pain, schistocytes on '
                                               'smear, AST 420 U/L, and platelets '
                                               '48,000/µL. HELLP syndrome is defined '
                                               'by which laboratory cluster?',
                                   'options': ['A) Hemolysis, Elevated Liver enzymes, '
                                               'and Low Platelets',
                                               'B) Pre-eclampsia with severe features '
                                               'including thrombocytopenia but without '
                                               'the full HELLP laboratory cluster',
                                               'C) Hyperglycemia, Elevated Lipase, and '
                                               'Low Potassium only',
                                               'D) Hyponatremia, Elevated cortisol, '
                                               'and Low ACTH exclusively'],
                                   'answer': 'A) Hemolysis, Elevated Liver enzymes, '
                                             'and Low Platelets',
                                   'explanation': 'HELLP = Hemolysis, Elevated Liver '
                                                  'enzymes, Low Platelets. Severe '
                                                  'pre-eclampsia overlaps and is the '
                                                  'obstetric near-miss without '
                                                  'completing HELLP labs. Other '
                                                  'acronyms are fabricated.',
                                   'choice_explanations': {'A': 'HELLP denotes '
                                                                'Hemolysis, Elevated '
                                                                'Liver enzymes, and '
                                                                'Low Platelets.',
                                                           'B': 'Severe pre-eclampsia '
                                                                'can include low '
                                                                'platelets and liver '
                                                                'injury and closely '
                                                                'borders HELLP; '
                                                                'schistocytic '
                                                                'hemolysis plus the '
                                                                'full enzyme/platelet '
                                                                'triad defines HELLP.',
                                                           'C': 'Hyperglycemia/lipase/potassium '
                                                                'is not HELLP.',
                                                           'D': 'Cortisol/ACTH '
                                                                'patterns are adrenal, '
                                                                'not HELLP.'}}],
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
                                                  'D) Pulmonary thromboembolism in '
                                                  'pregnancy with hypoxia and '
                                                  'hypotension but without consumptive '
                                                  'DIC as the hallmark onset'],
                                      'answer': 'B) Amniotic fluid embolism—supportive '
                                                'ABC resuscitation, correct '
                                                'coagulopathy, and advanced critical '
                                                'care; diagnosis is clinical',
                                      'explanation': 'Sudden hypoxia, hypotension, and '
                                                     'DIC after membrane rupture '
                                                     'suggest amniotic fluid '
                                                     'embolism—supportive critical '
                                                     'care. Thrombotic PE is the major '
                                                     'obstetric cardiopulmonary '
                                                     'near-miss, usually without this '
                                                     'explosive DIC onset. Vasovagal '
                                                     'and epidural hypotension differ.',
                                      'choice_explanations': {'A': 'Vasovagal syncope '
                                                                   'lacks DIC and '
                                                                   'refractory shock '
                                                                   'physiology.',
                                                              'B': 'Peripartum '
                                                                   'collapse with '
                                                                   'hypoxia, shock, '
                                                                   'and DIC after '
                                                                   'rupture suggests '
                                                                   'AFE managed with '
                                                                   'aggressive '
                                                                   'supportive '
                                                                   'resuscitation.',
                                                              'C': 'Epidural '
                                                                   'hypotension is '
                                                                   'vasodilatory and '
                                                                   'not a DIC crisis.',
                                                              'D': 'PE also causes '
                                                                   'hypoxia/hypotension '
                                                                   'in pregnancy and '
                                                                   'must be '
                                                                   'considered, but '
                                                                   'abrupt DIC without '
                                                                   'preceding '
                                                                   'hemorrhage is the '
                                                                   'AFE clinical '
                                                                   'hallmark '
                                                                   'distinguishing the '
                                                                   'syndrome.'}},
                                     {'question': 'A third-trimester patient develops '
                                                  'nausea, abdominal pain, '
                                                  'hypoglycemia, rising transaminases, '
                                                  'coagulopathy, and evolving liver '
                                                  'failure. Pre-eclampsia features may '
                                                  'overlap. Which entity is most '
                                                  'concerning?',
                                      'options': ['A) Gilbert syndrome unmasked by '
                                                  'pregnancy as fulminant hepatic '
                                                  'failure',
                                                  'B) HELLP syndrome with overlapping '
                                                  'liver injury and thrombocytopenia '
                                                  'in pre-eclampsia',
                                                  'C) Acute fatty liver of pregnancy—a '
                                                  'obstetric emergency often requiring '
                                                  'prompt delivery and supportive care',
                                                  'D) Intrahepatic cholestasis of '
                                                  'pregnancy with isolated pruritus '
                                                  'and elevated bile acids only'],
                                      'answer': 'C) Acute fatty liver of pregnancy—a '
                                                'obstetric emergency often requiring '
                                                'prompt delivery and supportive care',
                                      'explanation': 'Third-trimester liver failure '
                                                     'with hypoglycemia/coagulopathy '
                                                     'suggests AFLP needing delivery. '
                                                     'HELLP overlaps with hepatic '
                                                     'injury and is the key near-miss; '
                                                     'hypoglycemia and synthetic '
                                                     'failure push toward AFLP. ICP '
                                                     'and Gilbert are '
                                                     'milder/different.',
                                      'choice_explanations': {'A': 'Gilbert syndrome '
                                                                   'is mild '
                                                                   'unconjugated '
                                                                   'hyperbilirubinemia, '
                                                                   'not fulminant '
                                                                   'hepatic failure.',
                                                              'B': 'HELLP also injures '
                                                                   'the liver in '
                                                                   'pre-eclamptic '
                                                                   'women and is the '
                                                                   'closest rival; '
                                                                   'profound '
                                                                   'hypoglycemia, '
                                                                   'coagulopathy, and '
                                                                   'evolving liver '
                                                                   'failure favor AFLP '
                                                                   'over HELLP alone.',
                                                              'C': 'AFLP presents with '
                                                                   'acute hepatic '
                                                                   'failure features '
                                                                   'in late pregnancy '
                                                                   'and usually '
                                                                   'requires prompt '
                                                                   'delivery plus '
                                                                   'support.',
                                                              'D': 'ICP causes '
                                                                   'pruritus and high '
                                                                   'bile acids without '
                                                                   'fulminant '
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
                                      'options': ['A) Labor induction with '
                                                  'prostaglandins in an unscarred '
                                                  'uterus without prior cesarean',
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
                                      'explanation': 'Uterine rupture risk rises most '
                                                     'with TOLAC, especially with '
                                                     'dystocia or prostaglandins on a '
                                                     'scarred uterus. Prostaglandin '
                                                     'induction without a scar is a '
                                                     'related labor intervention '
                                                     'near-miss with far lower rupture '
                                                     'risk. Elective repeat cesarean '
                                                     'and successful ECV without scar '
                                                     'are lower-risk for rupture.',
                                      'choice_explanations': {'A': 'Prostaglandin '
                                                                   'induction can also '
                                                                   'be associated with '
                                                                   'uterine '
                                                                   'hyperstimulation '
                                                                   'in general, so the '
                                                                   'drug is a tempting '
                                                                   'answer; the '
                                                                   'scarred uterus '
                                                                   'undergoing trial '
                                                                   'of labor is the '
                                                                   'decisive high-risk '
                                                                   'setting.',
                                                              'B': 'Elective repeat '
                                                                   'cesarean without '
                                                                   'labor avoids TOLAC '
                                                                   'rupture risk.',
                                                              'C': 'ECV success '
                                                                   'without uterine '
                                                                   'scar is not the '
                                                                   'high-rupture '
                                                                   'scenario.',
                                                              'D': 'TOLAC—particularly '
                                                                   'with dystocia or '
                                                                   'prostaglandin '
                                                                   'induction—most '
                                                                   'significantly '
                                                                   'elevates rupture '
                                                                   'risk in a scarred '
                                                                   'uterus.'}}]},
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
                                                    'B) IV isotonic fluids for severe '
                                                    'dehydration or shock when ORS '
                                                    'cannot be used',
                                                    'C) Immediate IV 3% saline for all '
                                                    'cases regardless of severity',
                                                    'D) Routine antidiarrheal opioids '
                                                    'as primary rehydration'],
                                        'answer': 'A) Oral rehydration solution with '
                                                  'appropriate glucose–sodium balance',
                                        'explanation': 'Mild–moderate dehydration with '
                                                       'ability to drink is treated '
                                                       'first with ORS. IV fluids are '
                                                       'correct for severe '
                                                       'dehydration/shock and are the '
                                                       'severity near-miss. Hypertonic '
                                                       'saline for all and '
                                                       'antidiarrheal opioids are '
                                                       'wrong.',
                                        'choice_explanations': {'A': 'ORS with '
                                                                     'balanced '
                                                                     'glucose–sodium '
                                                                     'is first-line '
                                                                     'for '
                                                                     'mild–moderate '
                                                                     'pediatric '
                                                                     'gastroenteritis '
                                                                     'dehydration when '
                                                                     'the child can '
                                                                     'drink.',
                                                                'B': 'IV rehydration '
                                                                     'is appropriate '
                                                                     'for severe '
                                                                     'dehydration or '
                                                                     'intolerance of '
                                                                     'ORS, so it is a '
                                                                     'close management '
                                                                     'rival—but the '
                                                                     'stem specifies '
                                                                     'mild–moderate '
                                                                     'drinkers, where '
                                                                     'ORS comes first.',
                                                                'C': '3% saline is not '
                                                                     'routine '
                                                                     'rehydration for '
                                                                     'gastroenteritis.',
                                                                'D': 'Antidiarrheal '
                                                                     'opioids are not '
                                                                     'primary '
                                                                     'pediatric '
                                                                     'rehydration '
                                                                     'therapy.'}},
                                       {'question': 'The MMR vaccine is which type of '
                                                    'immunizing agent?',
                                        'options': ['A) Pure polysaccharide vaccine '
                                                    'without protein conjugation',
                                                    'B) Live attenuated viral vaccine '
                                                    'requiring caution in severe '
                                                    'immunodeficiency',
                                                    'C) Toxoid vaccine like tetanus '
                                                    'toxoid',
                                                    'D) Live attenuated varicella '
                                                    'vaccine as another live viral '
                                                    'immunizing agent with similar '
                                                    'immunodeficiency cautions'],
                                        'answer': 'B) Live attenuated viral vaccine '
                                                  'requiring caution in severe '
                                                  'immunodeficiency',
                                        'explanation': 'MMR is live attenuated and '
                                                       'cautioned in severe '
                                                       'immunodeficiency. Varicella '
                                                       'vaccine is also live '
                                                       'attenuated and the '
                                                       'vaccine-class near-miss. '
                                                       'Polysaccharide and toxoid '
                                                       'vaccines are different '
                                                       'platforms.',
                                        'choice_explanations': {'A': 'Pure '
                                                                     'polysaccharide '
                                                                     'vaccines are '
                                                                     'inactivated '
                                                                     'carbohydrate '
                                                                     'antigens, not '
                                                                     'MMR.',
                                                                'B': 'MMR is a live '
                                                                     'attenuated viral '
                                                                     'vaccine used '
                                                                     'cautiously in '
                                                                     'severe '
                                                                     'immunodeficiency.',
                                                                'C': 'Tetanus toxoid '
                                                                     'is inactivated '
                                                                     'toxin, not a '
                                                                     'live viral '
                                                                     'vaccine.',
                                                                'D': 'Varicella '
                                                                     'vaccine is '
                                                                     'likewise live '
                                                                     'attenuated with '
                                                                     'similar '
                                                                     'precautions, so '
                                                                     '“live vaccine” '
                                                                     'knowledge '
                                                                     'overlaps; the '
                                                                     'stem asks '
                                                                     'specifically '
                                                                     'what MMR is.'}},
                                       {'question': 'The Apgar score is traditionally '
                                                    'assessed at which times after '
                                                    'birth?',
                                        'options': ['A) Before delivery during each '
                                                    'contraction',
                                                    'B) Expanded assessments at 10 '
                                                    'minutes when the 5-minute Apgar '
                                                    'remains low',
                                                    'C) At 1 and 5 minutes of life '
                                                    '(with further scores if still '
                                                    'low)',
                                                    'D) Only at 24 hours of life'],
                                        'answer': 'C) At 1 and 5 minutes of life (with '
                                                  'further scores if still low)',
                                        'explanation': 'Apgar scores are traditionally '
                                                       'at 1 and 5 minutes, with '
                                                       'further scores if still low. '
                                                       'The 10-minute score is a '
                                                       'related continuation '
                                                       'near-miss, not the traditional '
                                                       'pair. 24-hour-only or '
                                                       'intrapartum scoring is wrong.',
                                        'choice_explanations': {'A': 'Apgar is not '
                                                                     'scored during '
                                                                     'contractions '
                                                                     'before birth.',
                                                                'B': 'A 10-minute '
                                                                     'Apgar is '
                                                                     'recommended if '
                                                                     'the 5-minute '
                                                                     'score is low, so '
                                                                     'timing can be '
                                                                     'confused; the '
                                                                     'traditional '
                                                                     'standard pair '
                                                                     'remains 1 and 5 '
                                                                     'minutes.',
                                                                'C': 'Apgar scoring is '
                                                                     'classically '
                                                                     'performed at 1 '
                                                                     'and 5 minutes of '
                                                                     'life.',
                                                                'D': 'Waiting until 24 '
                                                                     'hours misses '
                                                                     'transitional '
                                                                     'assessment.'}}],
                              'medium': [{'question': 'The most feared cardiac '
                                                      'complication of Kawasaki '
                                                      'disease is which?',
                                          'options': ['A) Myocarditis/valvulitis '
                                                      'during acute Kawasaki '
                                                      'inflammation without aneurysm '
                                                      'formation',
                                                      'B) Congenital bicuspid aortic '
                                                      'valve present from birth',
                                                      'C) Chronic rheumatic mitral '
                                                      'stenosis within days of fever',
                                                      'D) Coronary artery aneurysms '
                                                      '(and risk of '
                                                      'thrombosis/ischemia)'],
                                          'answer': 'D) Coronary artery aneurysms (and '
                                                    'risk of thrombosis/ischemia)',
                                          'explanation': 'Kawasaki’s most feared '
                                                         'cardiac complication is '
                                                         'coronary artery aneurysms. '
                                                         'Acute myocarditis can occur '
                                                         'and is a cardiac near-miss, '
                                                         'but aneurysm risk drives '
                                                         'long-term surveillance. '
                                                         'Bicuspid valve and rapid '
                                                         'rheumatic MS are unrelated.',
                                          'choice_explanations': {'A': 'Myocarditis '
                                                                       'can accompany '
                                                                       'acute Kawasaki '
                                                                       'disease and is '
                                                                       'truly cardiac, '
                                                                       'but the '
                                                                       'hallmark '
                                                                       'feared sequela '
                                                                       'taught for '
                                                                       'surveillance '
                                                                       'is coronary '
                                                                       'aneurysm '
                                                                       'formation.',
                                                                  'B': 'Bicuspid '
                                                                       'aortic valve '
                                                                       'is congenital, '
                                                                       'not a Kawasaki '
                                                                       'sequela.',
                                                                  'C': 'Rheumatic '
                                                                       'mitral '
                                                                       'stenosis does '
                                                                       'not develop '
                                                                       'within days of '
                                                                       'Kawasaki '
                                                                       'fever.',
                                                                  'D': 'Coronary '
                                                                       'artery '
                                                                       'aneurysms '
                                                                       '(with '
                                                                       'thrombosis/ischemia '
                                                                       'risk) are the '
                                                                       'most feared '
                                                                       'Kawasaki '
                                                                       'cardiac '
                                                                       'complication.'}},
                                         {'question': 'Fever in a neonate (especially '
                                                      '<28 days) is managed with which '
                                                      'guiding principle?',
                                          'options': ['A) Urgent evaluation for '
                                                      'serious bacterial/HSV infection '
                                                      'with empiric antimicrobials per '
                                                      'protocol—do not reassure as '
                                                      'simple viral illness',
                                                      'B) Full sepsis workup with '
                                                      'cultures but delayed '
                                                      'antimicrobials until all '
                                                      'results return',
                                                      'C) Home observation with '
                                                      'antipyretics only for 72 hours '
                                                      'first',
                                                      'D) Oral antibiotics without '
                                                      'cultures as definitive care'],
                                          'answer': 'A) Urgent evaluation for serious '
                                                    'bacterial/HSV infection with '
                                                    'empiric antimicrobials per '
                                                    'protocol—do not reassure as '
                                                    'simple viral illness',
                                          'explanation': 'Neonatal fever needs urgent '
                                                         'evaluation and empiric '
                                                         'antimicrobials for serious '
                                                         'bacterial/HSV infection. '
                                                         'Doing cultures but delaying '
                                                         'drugs is the dangerous '
                                                         'near-miss. Home observation '
                                                         'or culture-free oral therapy '
                                                         'is inadequate.',
                                          'choice_explanations': {'A': 'Fever in a '
                                                                       'neonate '
                                                                       'warrants '
                                                                       'urgent '
                                                                       'infection '
                                                                       'evaluation and '
                                                                       'prompt empiric '
                                                                       'antimicrobials '
                                                                       'per protocol.',
                                                                  'B': 'Cultures are '
                                                                       'essential and '
                                                                       'tempting to '
                                                                       '“wait for,” '
                                                                       'but '
                                                                       'antimicrobials '
                                                                       'should not be '
                                                                       'deferred in '
                                                                       'this age group '
                                                                       'once workup is '
                                                                       'underway.',
                                                                  'C': 'Home '
                                                                       'observation '
                                                                       'risks rapid '
                                                                       'deterioration '
                                                                       'from neonatal '
                                                                       'sepsis/HSV.',
                                                                  'D': 'Oral '
                                                                       'antibiotics '
                                                                       'without a '
                                                                       'proper workup '
                                                                       'are not '
                                                                       'definitive '
                                                                       'neonatal fever '
                                                                       'care.'}},
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
                                                      'C) Unilateral wheeze from '
                                                      'inhaled foreign body always',
                                                      'D) Acute epiglottitis with '
                                                      'toxic appearance, drooling, and '
                                                      'tripoding rather than a barking '
                                                      'cough'],
                                          'answer': 'B) Inspiratory stridor and a '
                                                    'barking cough, often worse at '
                                                    'night',
                                          'explanation': 'Croup features inspiratory '
                                                         'stridor and barking cough, '
                                                         'often nocturnal. '
                                                         'Epiglottitis is the critical '
                                                         'upper-airway near-miss with '
                                                         'drooling/toxicity. Asthma '
                                                         'and foreign body have '
                                                         'different sounds/patterns.',
                                          'choice_explanations': {'A': 'Asthma is '
                                                                       'predominantly '
                                                                       'expiratory '
                                                                       'wheeze from '
                                                                       'lower airways.',
                                                                  'B': 'Viral croup '
                                                                       'classically '
                                                                       'causes barking '
                                                                       'cough and '
                                                                       'inspiratory '
                                                                       'stridor, often '
                                                                       'worse at '
                                                                       'night.',
                                                                  'C': 'Foreign body '
                                                                       'may cause '
                                                                       'unilateral '
                                                                       'findings, not '
                                                                       'the classic '
                                                                       'bilateral '
                                                                       'croup bark.',
                                                                  'D': 'Epiglottitis '
                                                                       'also presents '
                                                                       'with stridor '
                                                                       'and is the '
                                                                       'dangerous '
                                                                       'look-alike; '
                                                                       'drooling, '
                                                                       'tripoding, and '
                                                                       'toxicity '
                                                                       'without a '
                                                                       'barking cough '
                                                                       'separate it '
                                                                       'from typical '
                                                                       'croup.'}}],
                              'hard': [{'question': 'A 4-week-old boy has progressive '
                                                    'nonbilious projectile vomiting, a '
                                                    'palpable olive mass, and '
                                                    'hypochloremic metabolic '
                                                    'alkalosis. Infantile hypertrophic '
                                                    'pyloric stenosis classically '
                                                    'presents with which pattern?',
                                        'options': ['A) Painless bloody stools of '
                                                    'milk-protein allergy only',
                                                    'B) GERD with frequent spit-ups '
                                                    'but without projectile olive-mass '
                                                    'obstruction physiology',
                                                    'C) Progressive nonbilious '
                                                    'projectile vomiting at 2–6 weeks '
                                                    'with hypochloremic metabolic '
                                                    'alkalosis',
                                                    'D) Bilious vomiting from day 1 of '
                                                    'life always'],
                                        'answer': 'C) Progressive nonbilious '
                                                  'projectile vomiting at 2–6 weeks '
                                                  'with hypochloremic metabolic '
                                                  'alkalosis',
                                        'explanation': 'Pyloric stenosis: 2–6 weeks, '
                                                       'nonbilious projectile '
                                                       'vomiting, olive mass, '
                                                       'hypochloremic alkalosis. GERD '
                                                       'is the common vomiting '
                                                       'near-miss without obstructive '
                                                       'alkalosis/olive. Bilious day-1 '
                                                       'vomiting and milk-protein '
                                                       'bloody stools differ.',
                                        'choice_explanations': {'A': 'Milk-protein '
                                                                     'allergy more '
                                                                     'often causes '
                                                                     'blood-streaked '
                                                                     'stools than this '
                                                                     'alkalotic '
                                                                     'projectile '
                                                                     'pattern.',
                                                                'B': 'GERD causes '
                                                                     'frequent '
                                                                     'regurgitation '
                                                                     'and is often '
                                                                     'tried first as '
                                                                     'an explanation, '
                                                                     'but projectile '
                                                                     'progression, '
                                                                     'palpable olive, '
                                                                     'and '
                                                                     'hypochloremic '
                                                                     'alkalosis '
                                                                     'indicate pyloric '
                                                                     'stenosis.',
                                                                'C': 'Infantile '
                                                                     'hypertrophic '
                                                                     'pyloric stenosis '
                                                                     'presents with '
                                                                     'progressive '
                                                                     'nonbilious '
                                                                     'projectile '
                                                                     'vomiting and '
                                                                     'hypochloremic '
                                                                     'metabolic '
                                                                     'alkalosis at 2–6 '
                                                                     'weeks.',
                                                                'D': 'Bilious emesis '
                                                                     'from day 1 '
                                                                     'suggests '
                                                                     'obstruction '
                                                                     'distal to the '
                                                                     'ampulla (e.g., '
                                                                     'malrotation), '
                                                                     'not pyloric '
                                                                     'stenosis.'}},
                                       {'question': 'Intussusception stool is '
                                                    'classically described as which '
                                                    'appearance when ischemia '
                                                    'develops?',
                                        'options': ['A) Occult blood–positive stools '
                                                    'or diarrhea earlier in '
                                                    'intussusception before classic '
                                                    'currant-jelly appearance',
                                                    'B) Acholic pale stools of biliary '
                                                    'atresia',
                                                    'C) Steatorrhea from pancreatic '
                                                    'insufficiency alone',
                                                    'D) Currant-jelly (blood and '
                                                    'mucus) stools'],
                                        'answer': 'D) Currant-jelly (blood and mucus) '
                                                  'stools',
                                        'explanation': 'Ischemic intussusception '
                                                       'classically yields '
                                                       'currant-jelly stools. Earlier '
                                                       'intussusception may have '
                                                       'occult blood only—the temporal '
                                                       'near-miss. Acholic and '
                                                       'steatorrheic stools are '
                                                       'different diseases.',
                                        'choice_explanations': {'A': 'Intussusception '
                                                                     'can present '
                                                                     'before frank '
                                                                     'currant-jelly '
                                                                     'stools with '
                                                                     'occult blood or '
                                                                     'irritability '
                                                                     'only, so earlier '
                                                                     'findings '
                                                                     'overlap; the '
                                                                     'classic ischemic '
                                                                     'descriptor '
                                                                     'remains currant '
                                                                     'jelly.',
                                                                'B': 'Acholic stools '
                                                                     'suggest '
                                                                     'cholestasis/biliary '
                                                                     'atresia.',
                                                                'C': 'Steatorrhea '
                                                                     'reflects fat '
                                                                     'malabsorption, '
                                                                     'not '
                                                                     'intussusception '
                                                                     'ischemia.',
                                                                'D': 'Currant-jelly '
                                                                     '(blood and '
                                                                     'mucus) stools '
                                                                     'are the classic '
                                                                     'ischemic '
                                                                     'intussusception '
                                                                     'stool '
                                                                     'description.'}},
                                       {'question': 'A male neonate with salt-wasting '
                                                    'congenital adrenal hyperplasia '
                                                    'may present in crisis with which '
                                                    'electrolyte pattern?',
                                        'options': ['A) Hyponatremia, hyperkalemia, '
                                                    'and dehydration from aldosterone '
                                                    'deficiency',
                                                    'B) Isolated glucocorticoid '
                                                    'deficiency with '
                                                    'hypoglycemia/shock but less '
                                                    'mineralocorticoid-pattern '
                                                    'electrolyte change',
                                                    'C) Hypernatremia and hypokalemia '
                                                    'from mineralocorticoid excess',
                                                    'D) Metabolic alkalosis with '
                                                    'severe hypokalemia only like '
                                                    'pyloric stenosis'],
                                        'answer': 'A) Hyponatremia, hyperkalemia, and '
                                                  'dehydration from aldosterone '
                                                  'deficiency',
                                        'explanation': 'Salt-wasting CAH crises show '
                                                       'hyponatremia, hyperkalemia, '
                                                       'and dehydration from '
                                                       'aldosterone deficiency. '
                                                       'Isolated glucocorticoid '
                                                       'deficiency is related adrenal '
                                                       'near-miss with less classic '
                                                       'mineralocorticoid electrolyte '
                                                       'pattern. Mineralocorticoid '
                                                       'excess and pyloric alkalosis '
                                                       'are opposite/different.',
                                        'choice_explanations': {'A': 'Aldosterone '
                                                                     'deficiency in '
                                                                     'salt-wasting CAH '
                                                                     'produces '
                                                                     'hyponatremia, '
                                                                     'hyperkalemia, '
                                                                     'and dehydration.',
                                                                'B': 'Glucocorticoid '
                                                                     'deficiency also '
                                                                     'causes adrenal '
                                                                     'crisis features '
                                                                     'and can coexist '
                                                                     'in CAH, but the '
                                                                     'distinctive '
                                                                     'electrolyte '
                                                                     'pattern asked is '
                                                                     'mineralocorticoid '
                                                                     'failure.',
                                                                'C': 'Mineralocorticoid '
                                                                     'excess causes '
                                                                     'the opposite '
                                                                     'sodium/potassium '
                                                                     'pattern.',
                                                                'D': 'Pyloric stenosis '
                                                                     'causes '
                                                                     'hypochloremic '
                                                                     'metabolic '
                                                                     'alkalosis, not '
                                                                     'hyperkalemic '
                                                                     'hyponatremia.'}}],
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
                                                       'C) Physiologic anemia of '
                                                       'infancy as the sole '
                                                       'explanation for acidosis and '
                                                       'weak femorals',
                                                       'D) Ductal-dependent pulmonary '
                                                       'blood flow lesion (e.g., '
                                                       'severe tetralogy) presenting '
                                                       'with cyanosis as the duct '
                                                       'closes'],
                                           'answer': 'B) Possible ductal-dependent '
                                                     'systemic blood flow lesion—ABC '
                                                     'resuscitation and prostaglandin '
                                                     'E1 to reopen the duct while '
                                                     'arranging cardiology/surgery',
                                           'explanation': 'Shock, gray color, '
                                                          'acidosis, and weak femorals '
                                                          'as the duct closes suggest '
                                                          'ductal-dependent systemic '
                                                          'flow (e.g., '
                                                          'coarctation/HLHS)—start '
                                                          'PGE1. Ductal-dependent '
                                                          'pulmonary flow lesions are '
                                                          'the CHD near-miss '
                                                          'presenting with cyanosis '
                                                          'more than systemic '
                                                          'hypoperfusion. Innocent PPS '
                                                          'and physiologic anemia do '
                                                          'not fit.',
                                           'choice_explanations': {'A': 'Innocent '
                                                                        'peripheral '
                                                                        'pulmonic '
                                                                        'stenosis is '
                                                                        'benign and '
                                                                        'not shock '
                                                                        'physiology.',
                                                                   'B': 'Critical '
                                                                        'left-sided/ductal-dependent '
                                                                        'systemic '
                                                                        'lesions '
                                                                        'present with '
                                                                        'shock as the '
                                                                        'duct '
                                                                        'closes—resuscitate '
                                                                        'and start '
                                                                        'prostaglandin '
                                                                        'E1 urgently.',
                                                                   'C': 'Physiologic '
                                                                        'anemia does '
                                                                        'not cause '
                                                                        'ductal-closure '
                                                                        'shock with '
                                                                        'weak '
                                                                        'femorals.',
                                                                   'D': 'Right-sided '
                                                                        'ductal-dependent '
                                                                        'lesions also '
                                                                        'need PGE1 and '
                                                                        'are closely '
                                                                        'related CHD '
                                                                        'emergencies, '
                                                                        'but they '
                                                                        'typically '
                                                                        'declare as '
                                                                        'severe '
                                                                        'cyanosis '
                                                                        'rather than '
                                                                        'weak '
                                                                        'femorals/systemic '
                                                                        'hypoperfusion.'}},
                                          {'question': 'A 4-month-old has bruises on '
                                                       'the pinna and frenulum tear, '
                                                       'retinal hemorrhages, and a '
                                                       'metaphyseal corner fracture, '
                                                       'with a changing caregiver '
                                                       'history. Which interpretation '
                                                       'is most appropriate?',
                                           'options': ['A) Vitamin K deficiency '
                                                       'bleeding as the single '
                                                       'explanation for fractures and '
                                                       'retinal hemorrhages',
                                                       'B) Osteogenesis imperfecta or '
                                                       'bleeding diathesis as medical '
                                                       'mimics that still require '
                                                       'protective evaluation while '
                                                       'workup proceeds',
                                                       'C) Injuries highly concerning '
                                                       'for non-accidental '
                                                       'trauma—protect the child and '
                                                       'perform a full '
                                                       'forensic/medical evaluation',
                                                       'D) Typical accidental bruises '
                                                       'over bony prominences from '
                                                       'rolling only'],
                                           'answer': 'C) Injuries highly concerning '
                                                     'for non-accidental '
                                                     'trauma—protect the child and '
                                                     'perform a full forensic/medical '
                                                     'evaluation',
                                           'explanation': 'Ear bruises, frenulum tear, '
                                                          'retinal hemorrhages, '
                                                          'metaphyseal fractures, and '
                                                          'changing history indicate '
                                                          'non-accidental '
                                                          'trauma—protect and evaluate '
                                                          'fully. OI/coagulopathy are '
                                                          'important mimics and the '
                                                          'diagnostic near-miss, but '
                                                          'they do not remove the duty '
                                                          'to protect and investigate. '
                                                          'Simple rolling bruises or '
                                                          'vitamin K alone do not '
                                                          'explain this pattern.',
                                           'choice_explanations': {'A': 'Vitamin K '
                                                                        'deficiency '
                                                                        'does not '
                                                                        'explain '
                                                                        'metaphyseal '
                                                                        'fractures '
                                                                        'plus this '
                                                                        'multi-injury '
                                                                        'pattern as a '
                                                                        'single cause.',
                                                                   'B': 'OI and '
                                                                        'bleeding '
                                                                        'disorders can '
                                                                        'mimic some '
                                                                        'findings and '
                                                                        'must be '
                                                                        'considered, '
                                                                        'but they are '
                                                                        'evaluated '
                                                                        'within a '
                                                                        'protective '
                                                                        'workup—not '
                                                                        'used to '
                                                                        'dismiss abuse '
                                                                        'concern at '
                                                                        'the outset.',
                                                                   'C': 'This injury '
                                                                        'pattern with '
                                                                        'a changing '
                                                                        'history is '
                                                                        'highly '
                                                                        'concerning '
                                                                        'for '
                                                                        'abuse—ensure '
                                                                        'safety and '
                                                                        'complete '
                                                                        'medical/forensic '
                                                                        'evaluation.',
                                                                   'D': 'Typical '
                                                                        'accidental '
                                                                        'bruises are '
                                                                        'over bony '
                                                                        'prominences, '
                                                                        'not '
                                                                        'pinna/frenulum '
                                                                        'with retinal '
                                                                        'and '
                                                                        'metaphyseal '
                                                                        'injuries.'}},
                                          {'question': 'An unvaccinated toddler '
                                                       'develops high fever, drooling, '
                                                       'muffled voice, and sits '
                                                       'forward tripoding with '
                                                       'stridor. Soft-tissue neck '
                                                       'radiograph is considered. '
                                                       'Which diagnosis and airway '
                                                       'principle apply?',
                                           'options': ['A) Severe croup '
                                                       '(laryngotracheobronchitis) '
                                                       'with stridor that may still '
                                                       'allow careful medical '
                                                       'management without '
                                                       'tripoding/drooling',
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
                                           'explanation': 'Unvaccinated toddler with '
                                                          'drooling, muffled voice, '
                                                          'tripoding, and stridor is '
                                                          'epiglottitis—do not '
                                                          'agitate; secure airway with '
                                                          'experts and give '
                                                          'antibiotics. Severe croup '
                                                          'is the stridor near-miss '
                                                          'without drooling/toxicity '
                                                          'pattern. Foreign body and '
                                                          'PTA explanations are wrong '
                                                          'here.',
                                           'choice_explanations': {'A': 'Severe croup '
                                                                        'also causes '
                                                                        'stridor and '
                                                                        'can look '
                                                                        'frightening, '
                                                                        'but barking '
                                                                        'cough without '
                                                                        'drooling/tripoding '
                                                                        'toxicity is '
                                                                        'more croup; '
                                                                        'this stem’s '
                                                                        'drooling/tripod '
                                                                        'picture is '
                                                                        'epiglottitis.',
                                                                   'B': 'Drooling '
                                                                        'indicates '
                                                                        'secretions '
                                                                        'can’t be '
                                                                        'swallowed—not '
                                                                        'that a '
                                                                        'foreign body '
                                                                        'is gone.',
                                                                   'C': 'Peritonsillar '
                                                                        'abscess is '
                                                                        'uncommon in '
                                                                        'toddlers and '
                                                                        'not the '
                                                                        'classic '
                                                                        'tripoding '
                                                                        'epiglottitis '
                                                                        'syndrome.',
                                                                   'D': 'Toxic '
                                                                        'tripoding '
                                                                        'with drooling '
                                                                        'and stridor '
                                                                        'suggests '
                                                                        'epiglottitis—airway '
                                                                        'first in a '
                                                                        'controlled '
                                                                        'setting, then '
                                                                        'antibiotics.'}}]},
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


# Load expanded MCQ banks (100 unique questions per specialty) when available.
from pathlib import Path as _BankPath
import sys as _sys

_bank_root = _BankPath(__file__).resolve().parent
if str(_bank_root) not in _sys.path:
    _sys.path.insert(0, str(_bank_root))
if str(_bank_root.parent) not in _sys.path:
    _sys.path.insert(0, str(_bank_root.parent))
from bank_loader import apply_question_banks

apply_question_banks(SPECIALTIES, _bank_root / "question_banks")



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
