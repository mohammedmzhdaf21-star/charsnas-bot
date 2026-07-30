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
                'questions': {'easy': [{'question': 'What does ECG primarily record?',
                                        'options': ['A) Electrical activity of the '
                                                    'heart',
                                                    'B) Mechanical contractility of '
                                                    'the ventricles',
                                                    'C) Coronary artery blood flow '
                                                    'velocity',
                                                    'D) Central venous pressure '
                                                    'waveform'],
                                        'answer': 'A) Electrical activity of the heart',
                                        'explanation': 'The electrocardiogram records '
                                                       'summed electrical potentials '
                                                       'from atrial and ventricular '
                                                       'myocytes as depolarization and '
                                                       'repolarization sweep across '
                                                       'the heart. Surface electrodes '
                                                       'display these voltage changes '
                                                       'as P, QRS, and T waves over '
                                                       'time. It does not directly '
                                                       'measure contractility, '
                                                       'coronary flow, or filling '
                                                       'pressures.'},
                                       {'question': 'Typical symptom of angina is?',
                                        'options': ['A) Pleuritic pain worse when '
                                                    'lying flat only',
                                                    'B) Retrosternal chest discomfort '
                                                    'provoked by exertion',
                                                    'C) Sharp chest pain reproduced by '
                                                    'chest-wall palpation',
                                                    'D) Burning epigastric pain '
                                                    'relieved solely by antacids'],
                                        'answer': 'B) Retrosternal chest discomfort '
                                                  'provoked by exertion',
                                        'explanation': 'Angina reflects myocardial '
                                                       'ischemia when coronary oxygen '
                                                       'supply cannot meet demand, '
                                                       'typically during exertion or '
                                                       'stress. Patients describe '
                                                       'retrosternal pressure or '
                                                       'tightness that may radiate to '
                                                       'the arm, neck, or jaw and '
                                                       'eases with rest or nitrates. '
                                                       'Musculoskeletal, purely '
                                                       'pleuritic, or isolated reflux '
                                                       'pain patterns point away from '
                                                       'classic ischemic angina.'},
                                       {'question': 'Aspirin in ACS is given mainly '
                                                    'to?',
                                        'options': ['A) Acute coronary vasodilation '
                                                    'via nitric oxide',
                                                    'B) Reduction of myocardial oxygen '
                                                    'demand via beta-blockade',
                                                    'C) Irreversible inhibition of '
                                                    'platelet aggregation',
                                                    'D) Dissolution of fibrin within '
                                                    'established thrombus'],
                                        'answer': 'C) Irreversible inhibition of '
                                                  'platelet aggregation',
                                        'explanation': 'In ACS, platelet activation at '
                                                       'a ruptured plaque drives '
                                                       'thrombus growth. Aspirin '
                                                       'irreversibly acetylates '
                                                       'platelet COX-1, blocking '
                                                       'thromboxane A2 synthesis and '
                                                       'reducing further aggregation. '
                                                       'Vasodilation, beta-blockade, '
                                                       'and fibrinolysis are separate '
                                                       'therapeutic mechanisms used in '
                                                       'other contexts.'}],
                              'medium': [{'question': 'ST elevation in leads II, III, '
                                                      'and aVF most suggests occlusion '
                                                      'in which territory?',
                                          'options': ['A) Anterior wall (commonly LAD)',
                                                      'B) Lateral wall (commonly LCx)',
                                                      'C) Right ventricular free wall '
                                                      'alone without inferior '
                                                      'involvement',
                                                      'D) Inferior wall (commonly '
                                                      'RCA)'],
                                          'answer': 'D) Inferior wall (commonly RCA)',
                                          'explanation': 'Leads II, III, and aVF view '
                                                         'the inferior '
                                                         'left-ventricular wall, '
                                                         'usually supplied by the '
                                                         'right coronary artery (or a '
                                                         'dominant circumflex). ST '
                                                         'elevation in these '
                                                         'contiguous leads localizes '
                                                         'transmural ischemia to the '
                                                         'inferior territory. Anterior '
                                                         'STEMI involves precordial '
                                                         'leads; isolated lateral '
                                                         'changes map to LCx '
                                                         'territory.'},
                                         {'question': 'Which murmur is holosystolic '
                                                      'and radiates to the axilla?',
                                          'options': ['A) Mitral regurgitation',
                                                      'B) Aortic stenosis',
                                                      'C) Mitral stenosis',
                                                      'D) Aortic regurgitation'],
                                          'answer': 'A) Mitral regurgitation',
                                          'explanation': 'Mitral regurgitation '
                                                         'produces a high-velocity '
                                                         'systolic jet from LV to LA '
                                                         'throughout systole, yielding '
                                                         'a holosystolic murmur that '
                                                         'radiates to the axilla. '
                                                         'Aortic stenosis is a '
                                                         'crescendo-decrescendo '
                                                         'systolic murmur to the '
                                                         'carotids; mitral stenosis is '
                                                         'diastolic; aortic '
                                                         'regurgitation is an early '
                                                         'diastolic decrescendo '
                                                         'murmur.'},
                                         {'question': 'First-line symptom relief for '
                                                      'an acute angina episode is '
                                                      'often?',
                                          'options': ['A) Intravenous digoxin loading',
                                                      'B) Sublingual nitroglycerin',
                                                      'C) Immediate IV amiodarone '
                                                      'bolus',
                                                      'D) High-dose systemic '
                                                      'corticosteroid'],
                                          'answer': 'B) Sublingual nitroglycerin',
                                          'explanation': 'Sublingual nitroglycerin is '
                                                         'rapidly absorbed and '
                                                         'releases nitric oxide, '
                                                         'dilating veins (reducing '
                                                         'preload) and coronary '
                                                         'arteries. Lower wall tension '
                                                         'decreases myocardial oxygen '
                                                         'demand and often relieves an '
                                                         'acute angina episode within '
                                                         'minutes. Digoxin, '
                                                         'amiodarone, and steroids are '
                                                         'not first-line acute '
                                                         'anti-anginal relief.'}],
                              'hard': [{'question': 'A patient with inferior STEMI '
                                                    'becomes hypotensive after '
                                                    'nitrates and has elevated JVP '
                                                    'with clear lungs. Which '
                                                    'associated process should you '
                                                    'suspect?',
                                        'options': ['A) Isolated left ventricular '
                                                    'apical aneurysm',
                                                    'B) Acute severe mitral stenosis',
                                                    'C) Right ventricular infarction',
                                                    'D) Primary hypertensive pulmonary '
                                                    'edema without RV involvement'],
                                        'answer': 'C) Right ventricular infarction',
                                        'explanation': 'The RV is often co-infarcted '
                                                       'with inferior STEMI because '
                                                       'both are commonly '
                                                       'RCA-dependent, and RV stroke '
                                                       'volume is highly '
                                                       'preload-dependent. Nitrates '
                                                       'pool venous blood, abruptly '
                                                       'cut RV preload, and cause '
                                                       'hypotension with elevated JVP '
                                                       'and clear lungs. This pattern '
                                                       'should prompt RV infarction '
                                                       'recognition and cautious fluid '
                                                       'resuscitation rather than '
                                                       'further preload reduction.'},
                                       {'question': 'Which heart-failure therapy class '
                                                    'has strong mortality benefit in '
                                                    'HFrEF among the listed options?',
                                        'options': ['A) Digoxin monotherapy as sole '
                                                    'disease-modifying therapy',
                                                    'B) Short-acting dihydropyridine '
                                                    'calcium-channel blocker',
                                                    'C) Class Ic antiarrhythmic '
                                                    'started routinely in all HFrEF',
                                                    'D) Evidence-based beta-blocker '
                                                    '(e.g., carvedilol, bisoprolol, '
                                                    'metoprolol succinate)'],
                                        'answer': 'D) Evidence-based beta-blocker '
                                                  '(e.g., carvedilol, bisoprolol, '
                                                  'metoprolol succinate)',
                                        'explanation': 'In HFrEF, sustained '
                                                       'sympathetic activation worsens '
                                                       'remodeling, arrhythmias, and '
                                                       'mortality. Evidence-based '
                                                       'beta-blockers blunt this drive '
                                                       'and reduce mortality when '
                                                       'titrated appropriately. '
                                                       'Digoxin may help symptoms/rate '
                                                       'control but is not sole '
                                                       'mortality therapy; '
                                                       'short-acting nifedipine and '
                                                       'routine class Ic agents can '
                                                       'harm HFrEF patients.'},
                                       {'question': 'New LBBB with ischemic symptoms '
                                                    'can be treated as?',
                                        'options': ['A) STEMI equivalent in the '
                                                    'appropriate ischemic clinical '
                                                    'context',
                                                    'B) Benign age-related conduction '
                                                    'change requiring no urgency',
                                                    'C) Definitive '
                                                    'electrocardiographic proof of '
                                                    'pulmonary embolism',
                                                    'D) Isolated indication for '
                                                    'atropine without reperfusion '
                                                    'consideration'],
                                        'answer': 'A) STEMI equivalent in the '
                                                  'appropriate ischemic clinical '
                                                  'context',
                                        'explanation': 'New LBBB can accompany '
                                                       'extensive ischemic injury and '
                                                       'obscures ST-segment '
                                                       'interpretation. When it '
                                                       'appears with ongoing ischemic '
                                                       'symptoms, guidelines treat it '
                                                       'as a STEMI equivalent '
                                                       'warranting urgent reperfusion '
                                                       'assessment. It is not proof of '
                                                       'PE and does not by itself '
                                                       'mandate atropine.'}],
                              'extreme': [{'question': 'A 72-year-old with prior CABG '
                                                       'presents with flash pulmonary '
                                                       'edema, unequal arm BPs, and a '
                                                       'tearing back pain. Troponin is '
                                                       'mildly up; ECG shows '
                                                       'non-specific ST changes. Which '
                                                       'diagnosis must be excluded '
                                                       'before dual antiplatelet '
                                                       'loading and anticoagulation '
                                                       'for presumed NSTE-ACS?',
                                           'options': ['A) Uncomplicated '
                                                       'non–ST-elevation ACS without '
                                                       'vascular complication',
                                                       'B) Acute aortic '
                                                       'syndrome/dissection',
                                                       'C) Isolated takotsubo '
                                                       'cardiomyopathy',
                                                       'D) Type 2 myocardial injury '
                                                       'from sepsis alone'],
                                           'answer': 'B) Acute aortic '
                                                     'syndrome/dissection',
                                           'explanation': 'Acute aortic dissection can '
                                                          'present with severe tearing '
                                                          'back/chest pain, pulse or '
                                                          'BP asymmetry, flash edema, '
                                                          'and secondary troponin '
                                                          'rise, closely mimicking '
                                                          'NSTE-ACS. Dual antiplatelet '
                                                          'therapy and anticoagulation '
                                                          'can catastrophically extend '
                                                          'dissection or delay '
                                                          'surgery. Unequal arm BPs '
                                                          'and tearing pain mandate '
                                                          'exclusion of aortic '
                                                          'syndrome first.'},
                                          {'question': 'In suspected tamponade after '
                                                       'cardiac surgery, which '
                                                       'constellation is most '
                                                       'suggestive?',
                                           'options': ['A) Hypertension with bounding '
                                                       'pulses and wide pulse pressure',
                                                       'B) Isolated wheeze with normal '
                                                       'blood pressure and clear heart '
                                                       'sounds',
                                                       'C) Hypotension, raised filling '
                                                       'pressures, low '
                                                       'voltage/electrical alternans ± '
                                                       'muffled sounds',
                                                       'D) Fever alone without '
                                                       'hemodynamic or ECG change'],
                                           'answer': 'C) Hypotension, raised filling '
                                                     'pressures, low '
                                                     'voltage/electrical alternans ± '
                                                     'muffled sounds',
                                           'explanation': 'Cardiac tamponade is '
                                                          'obstructive shock: '
                                                          'pericardial fluid impairs '
                                                          'diastolic filling and '
                                                          'stroke volume falls. Clues '
                                                          'include hypotension, '
                                                          'elevated venous pressures, '
                                                          'muffled sounds, low '
                                                          'voltage, and electrical '
                                                          'alternans. Hypertension '
                                                          'with bounding pulses '
                                                          'suggests the opposite '
                                                          'physiology; isolated wheeze '
                                                          'or fever alone do not '
                                                          'define tamponade.'},
                                          {'question': 'A patient in AF with WPW '
                                                       'presents with very fast '
                                                       'irregular wide-complex '
                                                       'tachycardia and instability. '
                                                       'Which AV-nodal blocker '
                                                       'strategy is inappropriate?',
                                           'options': ['A) Avoid AV-nodal blockers and '
                                                       'perform synchronized '
                                                       'cardioversion if unstable',
                                                       'B) Proceed to expert-guided '
                                                       'management of '
                                                       'accessory-pathway conduction',
                                                       'C) Use procainamide or shock '
                                                       'pathways preferred over '
                                                       'AV-nodal blockers when stable '
                                                       'enough',
                                                       'D) Give IV verapamil, digoxin, '
                                                       'or adenosine as first-line '
                                                       'AV-nodal blockade'],
                                           'answer': 'D) Give IV verapamil, digoxin, '
                                                     'or adenosine as first-line '
                                                     'AV-nodal blockade',
                                           'explanation': 'In AF with WPW, atrial '
                                                          'impulses can conduct '
                                                          'rapidly over an accessory '
                                                          'pathway. AV-nodal blockers '
                                                          'preferentially block the AV '
                                                          'node and may paradoxically '
                                                          'increase accessory-pathway '
                                                          'conduction, risking VF. '
                                                          'Unstable patients need '
                                                          'immediate synchronized '
                                                          'cardioversion; AV-nodal '
                                                          'blockers are inappropriate '
                                                          'first-line therapy.'}]},
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
                   'questions': {'easy': [{'question': 'What test checks for RAPD?',
                                           'options': ['A) Swinging flashlight test',
                                                       'B) Cover-uncover test for '
                                                       'tropia',
                                                       'C) Schirmer test for tear '
                                                       'production',
                                                       'D) Amsler grid for macular '
                                                       'distortion'],
                                           'answer': 'A) Swinging flashlight test',
                                           'explanation': 'An RAPD indicates '
                                                          'asymmetric afferent input '
                                                          'to the pupillary light '
                                                          'reflex, usually from '
                                                          'optic-nerve or severe '
                                                          'retinal disease. In the '
                                                          'swinging flashlight test, '
                                                          'light moved from the good '
                                                          'eye to the affected eye '
                                                          'causes paradoxical '
                                                          'dilation. Cover testing, '
                                                          'Schirmer, and Amsler assess '
                                                          'alignment, tears, and '
                                                          'macula—not RAPD.'},
                                          {'question': 'Painful red eye with '
                                                       'mid-dilated pupil suggests?',
                                           'options': ['A) Viral conjunctivitis',
                                                       'B) Acute angle-closure '
                                                       'glaucoma',
                                                       'C) Anterior uveitis (iritis)',
                                                       'D) Bacterial keratitis'],
                                           'answer': 'B) Acute angle-closure glaucoma',
                                           'explanation': 'Acute angle-closure occurs '
                                                          'when the peripheral iris '
                                                          'blocks the trabecular '
                                                          'meshwork, abruptly raising '
                                                          'IOP. High pressure produces '
                                                          'a painful red eye, corneal '
                                                          'edema, and a mid-dilated, '
                                                          'poorly reactive pupil. '
                                                          'Conjunctivitis usually has '
                                                          'a normal pupil; uveitis '
                                                          'often has a small pupil; '
                                                          'keratitis features a focal '
                                                          'corneal infiltrate.'},
                                          {'question': 'CN VI palsy mainly impairs?',
                                           'options': ['A) Adduction of the eye',
                                                       'B) Elevation in abduction '
                                                       '(superior rectus primary '
                                                       'action)',
                                                       'C) Abduction of the eye',
                                                       'D) Depression in adduction '
                                                       '(superior oblique primary '
                                                       'action)'],
                                           'answer': 'C) Abduction of the eye',
                                           'explanation': 'CN VI (abducens) innervates '
                                                          'only the lateral rectus, '
                                                          'which abducts the eye. '
                                                          'Palsy causes impaired '
                                                          'abduction and horizontal '
                                                          'diplopia worse on looking '
                                                          'toward the affected side. '
                                                          'Adduction is mediated by '
                                                          'medial rectus (CN III); '
                                                          'vertical actions map to '
                                                          'other extraocular '
                                                          'muscles.'}],
                                 'medium': [{'question': 'Diabetic retinopathy '
                                                         'microaneurysms are seen on?',
                                             'options': ['A) Slit-lamp exam of the '
                                                         'anterior chamber alone',
                                                         'B) Tonometry for intraocular '
                                                         'pressure alone',
                                                         'C) Color vision testing '
                                                         'alone',
                                                         'D) Dilated fundoscopy / '
                                                         'retinal examination'],
                                             'answer': 'D) Dilated fundoscopy / '
                                                       'retinal examination',
                                             'explanation': 'Diabetic retinopathy '
                                                            'begins with retinal '
                                                            'microvascular damage '
                                                            'forming microaneurysms, '
                                                            'hemorrhages, and '
                                                            'exudates. These lesions '
                                                            'are visualized by dilated '
                                                            'fundoscopy or retinal '
                                                            'imaging. Anterior-segment '
                                                            'slit-lamp exam, IOP '
                                                            'measurement, and color '
                                                            'testing do not '
                                                            'demonstrate '
                                                            'microaneurysms.'},
                                            {'question': 'Sudden curtain-like field '
                                                         'loss suggests?',
                                             'options': ['A) Rhegmatogenous retinal '
                                                         'detachment until proven '
                                                         'otherwise',
                                                         'B) Central retinal vein '
                                                         'occlusion',
                                                         'C) Non-arteritic ischemic '
                                                         'optic neuropathy',
                                                         'D) Vitreous hemorrhage from '
                                                         'proliferative diabetic '
                                                         'retinopathy'],
                                             'answer': 'A) Rhegmatogenous retinal '
                                                       'detachment until proven '
                                                       'otherwise',
                                             'explanation': 'Rhegmatogenous detachment '
                                                            'separates neurosensory '
                                                            'retina from RPE; patients '
                                                            'often describe '
                                                            'photopsias, floaters, '
                                                            'then curtain-like field '
                                                            'loss. CRVO causes sudden '
                                                            'blurred vision with '
                                                            'retinal hemorrhages; '
                                                            'NAION causes altitudinal '
                                                            'field loss with disc '
                                                            'edema; vitreous '
                                                            'hemorrhage causes sudden '
                                                            'floaters/haze without a '
                                                            'progressive curtain of '
                                                            'detached retina.'},
                                            {'question': 'Orbital cellulitis vs '
                                                         'preseptal key worrying '
                                                         'features include?',
                                             'options': ['A) Isolated eyelid erythema '
                                                         'without motility or vision '
                                                         'change',
                                                         'B) Painful ophthalmoplegia, '
                                                         'proptosis, and vision change',
                                                         'C) Mild conjunctival '
                                                         'injection with clear cornea '
                                                         'and full motility',
                                                         'D) Unilateral lid swelling '
                                                         'that is painless and '
                                                         'non-tender'],
                                             'answer': 'B) Painful ophthalmoplegia, '
                                                       'proptosis, and vision change',
                                             'explanation': 'Orbital cellulitis '
                                                            'involves tissues '
                                                            'posterior to the septum, '
                                                            'often from ethmoid sinus '
                                                            'disease. Painful eye '
                                                            'movements, proptosis, and '
                                                            'vision change indicate '
                                                            'orbital involvement and '
                                                            'risk of cavernous sinus '
                                                            'or optic-nerve '
                                                            'compromise. Preseptal '
                                                            'cellulitis is limited to '
                                                            'the lid without orbital '
                                                            'signs.'}],
                                 'hard': [{'question': 'A relative afferent pupillary '
                                                       'defect with normal fundoscopy '
                                                       'early on most suggests?',
                                           'options': ['A) Uncomplicated early nuclear '
                                                       'lens opacity without afferent '
                                                       'defect',
                                                       'B) Uncorrected refractive '
                                                       'error alone',
                                                       'C) Optic neuropathy (e.g., '
                                                       'optic neuritis or ischemic '
                                                       'optic neuropathy)',
                                                       'D) Mild dry-eye disease '
                                                       'without optic-nerve '
                                                       'involvement'],
                                           'answer': 'C) Optic neuropathy (e.g., optic '
                                                     'neuritis or ischemic optic '
                                                     'neuropathy)',
                                           'explanation': 'An RAPD means the afferent '
                                                          'limb of the pupillary light '
                                                          'reflex is weaker in one '
                                                          'eye. When the fundus still '
                                                          'looks normal, the lesion is '
                                                          'usually in the optic nerve '
                                                          '(neuritis, ischemic '
                                                          'neuropathy). Cataract, '
                                                          'refractive error, and dry '
                                                          'eye do not produce a true '
                                                          'RAPD.'},
                                          {'question': 'Painful third-nerve palsy '
                                                       'involving the pupil is '
                                                       'concerning for?',
                                           'options': ['A) Isolated microvascular '
                                                       'ischemic CN III palsy with '
                                                       'spared pupil',
                                                       'B) Myasthenia gravis '
                                                       'presenting as fatigable ptosis '
                                                       'alone',
                                                       'C) Horner syndrome from '
                                                       'sympathetic pathway '
                                                       'interruption',
                                                       'D) Posterior communicating '
                                                       'artery aneurysm compression '
                                                       'until excluded'],
                                           'answer': 'D) Posterior communicating '
                                                     'artery aneurysm compression '
                                                     'until excluded',
                                           'explanation': 'Parasympathetic '
                                                          'pupilloconstrictor fibers '
                                                          'travel superficially on CN '
                                                          'III and are compressed '
                                                          'early by a PCOM aneurysm. '
                                                          'Pupil-involving, painful '
                                                          'third-nerve palsy is a '
                                                          'neurosurgical emergency '
                                                          'until aneurysm is excluded. '
                                                          'Pupil-sparing microvascular '
                                                          'palsy, myasthenia, and '
                                                          'Horner syndrome have '
                                                          'different mechanisms and '
                                                          'pupil patterns.'},
                                          {'question': 'Central retinal artery '
                                                       'occlusion typically presents '
                                                       'as?',
                                           'options': ['A) Sudden painless monocular '
                                                       'vision loss',
                                                       'B) Gradual bilateral painless '
                                                       'central blur over months',
                                                       'C) Painful vision loss with '
                                                       'photophobia and ciliary flush',
                                                       'D) Transient binocular '
                                                       'diplopia without acuity loss'],
                                           'answer': 'A) Sudden painless monocular '
                                                     'vision loss',
                                           'explanation': 'CRAO abruptly stops '
                                                          'arterial perfusion to the '
                                                          'inner retina, causing '
                                                          'sudden, profound, painless '
                                                          'monocular vision loss—a '
                                                          'retinal arterial stroke. '
                                                          'Gradual bilateral blur '
                                                          'suggests cataract or '
                                                          'macular disease; painful '
                                                          'red-eye loss suggests '
                                                          'uveitis/keratitis/glaucoma; '
                                                          'binocular diplopia '
                                                          'localizes to motility, not '
                                                          'CRAO.'}],
                                 'extreme': [{'question': 'A patient with giant cell '
                                                          'arteritis risk (age >50, '
                                                          'jaw claudication, high ESR) '
                                                          'and sudden vision loss '
                                                          'needs which immediate '
                                                          'approach?',
                                              'options': ['A) Delay all steroids until '
                                                          'temporal-artery biopsy '
                                                          'returns, even if vision is '
                                                          'threatened',
                                                          'B) Start high-dose '
                                                          'corticosteroids urgently '
                                                          'when GCA/AION is strongly '
                                                          'suspected',
                                                          'C) Begin only topical '
                                                          'lubricants while awaiting '
                                                          'outpatient review',
                                                          'D) Proceed first to routine '
                                                          'refraction and spectacle '
                                                          'correction'],
                                              'answer': 'B) Start high-dose '
                                                        'corticosteroids urgently when '
                                                        'GCA/AION is strongly '
                                                        'suspected',
                                              'explanation': 'GCA can occlude '
                                                             'posterior ciliary '
                                                             'arteries and cause '
                                                             'arteritic AION with '
                                                             'abrupt vision loss. Once '
                                                             'GCA/AION is strongly '
                                                             'suspected (age >50, jaw '
                                                             'claudication, elevated '
                                                             'ESR/CRP), high-dose '
                                                             'steroids are started '
                                                             'immediately to protect '
                                                             'the fellow eye; biopsy '
                                                             'should not delay '
                                                             'treatment.'},
                                             {'question': 'In chemical eye injury, the '
                                                          'first action is?',
                                              'options': ['A) Complete visual-field '
                                                          'testing before any '
                                                          'irrigation',
                                                          'B) Tight patching of the '
                                                          'eye without irrigation',
                                                          'C) Immediate copious '
                                                          'irrigation',
                                                          'D) Oral antibiotics as the '
                                                          'sole initial measure'],
                                              'answer': 'C) Immediate copious '
                                                        'irrigation',
                                              'explanation': 'Chemical injury '
                                                             'continues damaging '
                                                             'ocular surface and '
                                                             'deeper tissues until the '
                                                             'agent is diluted and '
                                                             'removed. Immediate '
                                                             'copious irrigation is '
                                                             'therefore the first '
                                                             'action, before detailed '
                                                             'examination or other '
                                                             'therapies. Patching '
                                                             'without irrigation traps '
                                                             'the chemical; oral '
                                                             'antibiotics do not '
                                                             'neutralize alkali/acid '
                                                             'injury.'},
                                             {'question': 'An immunosuppressed patient '
                                                          'with painful red eye, '
                                                          'hypopyon, and severe vision '
                                                          'loss may have?',
                                              'options': ['A) Uncomplicated allergic '
                                                          'conjunctivitis',
                                                          'B) Blepharitis without '
                                                          'intraocular involvement',
                                                          'C) Episcleritis with '
                                                          'preserved vision',
                                                          'D) Endophthalmitis until '
                                                          'proven otherwise'],
                                              'answer': 'D) Endophthalmitis until '
                                                        'proven otherwise',
                                              'explanation': 'Endophthalmitis is '
                                                             'infection of the '
                                                             'vitreous and aqueous, '
                                                             'producing severe pain, '
                                                             'marked vision loss, '
                                                             'injection, and often '
                                                             'hypopyon. '
                                                             'Immunosuppression and '
                                                             'recent intraocular '
                                                             'surgery raise risk and '
                                                             'demand urgent specialist '
                                                             'management. Mild surface '
                                                             'disease does not cause '
                                                             'hypopyon with profound '
                                                             'vision loss.'}]},
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
             'questions': {'easy': [{'question': 'Most common kidney stone type?',
                                     'options': ['A) Calcium oxalate',
                                                 'B) Uric acid',
                                                 'C) Struvite (magnesium ammonium '
                                                 'phosphate)',
                                                 'D) Cystine'],
                                     'answer': 'A) Calcium oxalate',
                                     'explanation': 'Most urinary calculi are '
                                                    'calcium-based, and calcium '
                                                    'oxalate is the predominant '
                                                    'composition worldwide. '
                                                    'Supersaturation of calcium and '
                                                    'oxalate promotes crystal growth. '
                                                    'Uric acid, struvite, and cystine '
                                                    'stones are important but less '
                                                    'common overall.'},
                                    {'question': 'Loin-to-groin pain classically '
                                                 'suggests?',
                                     'options': ['A) Acute pyelonephritis without '
                                                 'obstruction',
                                                 'B) Ureteric colic',
                                                 'C) Acute prostatitis',
                                                 'D) Renal vein thrombosis'],
                                     'answer': 'B) Ureteric colic',
                                     'explanation': 'A stone in the ureter triggers '
                                                    'visceral pain from spasm and '
                                                    'obstruction. Pain typically '
                                                    'begins in the flank and radiates '
                                                    'to the ipsilateral groin as the '
                                                    'stone migrates. Pyelonephritis '
                                                    'features fever and CVA '
                                                    'tenderness; prostatitis is '
                                                    'pelvic/perineal; renal vein '
                                                    'thrombosis has a different risk '
                                                    'context.'},
                                    {'question': 'First imaging often used for stones '
                                                 'in non-pregnant adults?',
                                     'options': ['A) Contrast-enhanced CT abdomen as '
                                                 'first test for all stone suspects',
                                                 'B) MRI pelvis as first-line stone '
                                                 'protocol',
                                                 'C) Non-contrast CT of the kidneys, '
                                                 'ureters, and bladder',
                                                 'D) Renal angiography'],
                                     'answer': 'C) Non-contrast CT of the kidneys, '
                                               'ureters, and bladder',
                                     'explanation': 'Non-contrast CT KUB detects '
                                                    'nearly all stone types by density '
                                                    'and shows size, location, and '
                                                    'secondary obstruction. It is '
                                                    'first-line imaging for suspected '
                                                    'urolithiasis in most non-pregnant '
                                                    'adults. Contrast CT, MRI, and '
                                                    'angiography are not first-line '
                                                    'stone protocols.'}],
                           'medium': [{'question': 'Painless gross hematuria in an '
                                                   'older smoker is concerning for?',
                                       'options': ['A) Benign prostatic hyperplasia '
                                                   'alone',
                                                   'B) Stress urinary incontinence',
                                                   'C) Uncomplicated varicocele',
                                                   'D) Urothelial (bladder) carcinoma'],
                                       'answer': 'D) Urothelial (bladder) carcinoma',
                                       'explanation': 'Painless gross hematuria '
                                                      'implies urinary-tract bleeding '
                                                      'without obvious infection or '
                                                      'colic. In older adults, '
                                                      'especially smokers, urothelial '
                                                      'carcinoma of the bladder is a '
                                                      'leading concern requiring '
                                                      'cystoscopic evaluation. BPH may '
                                                      'cause LUTS or microhematuria '
                                                      'but painless gross hematuria '
                                                      'still needs cancer exclusion.'},
                                      {'question': 'Fever + flank pain + UTI signs '
                                                   'suggest?',
                                       'options': ['A) Acute pyelonephritis',
                                                   'B) Uncomplicated cystitis without '
                                                   'upper-tract involvement',
                                                   'C) Asymptomatic bacteriuria',
                                                   'D) Chronic orchialgia without '
                                                   'infection'],
                                       'answer': 'A) Acute pyelonephritis',
                                       'explanation': 'Acute pyelonephritis is '
                                                      'bacterial infection of the '
                                                      'renal parenchyma and pelvis, '
                                                      'usually ascending from the '
                                                      'lower tract. Fever with flank '
                                                      'pain and UTI symptoms indicates '
                                                      'upper-tract infection needing '
                                                      'prompt antibiotics and risk '
                                                      'assessment for obstruction. '
                                                      'Cystitis lacks fever/flank '
                                                      'findings of pyelonephritis.'},
                                      {'question': 'Testicular torsion key management '
                                                   'theme is?',
                                       'options': ['A) Elective outpatient ultrasound '
                                                   'follow-up in weeks',
                                                   'B) Time-critical testicular '
                                                   'ischemia requiring urgent '
                                                   'exploration',
                                                   'C) Antibiotics alone as definitive '
                                                   'therapy',
                                                   'D) Watchful waiting until '
                                                   'cremasteric reflex returns'],
                                       'answer': 'B) Time-critical testicular ischemia '
                                                 'requiring urgent exploration',
                                       'explanation': 'Testicular torsion twists the '
                                                      'spermatic cord, occluding '
                                                      'venous then arterial flow so '
                                                      'the gonad becomes ischemic '
                                                      'within hours. Salvage depends '
                                                      'on rapid surgical detorsion and '
                                                      'orchidopexy; imaging must not '
                                                      'delay exploration when clinical '
                                                      'suspicion is high.'}],
                           'hard': [{'question': 'Stone with obstructed infected '
                                                 'kidney requires?',
                                     'options': ['A) Oral antibiotics alone with '
                                                 'delayed imaging in weeks',
                                                 'B) Elective lithotripsy after '
                                                 'infection resolves spontaneously '
                                                 'without drainage',
                                                 'C) Urgent decompression plus '
                                                 'antibiotics',
                                                 'D) Immediate systemic chemotherapy'],
                                     'answer': 'C) Urgent decompression plus '
                                               'antibiotics',
                                     'explanation': 'An obstructing stone with '
                                                    'infection creates closed-space '
                                                    'pyohydronephrosis; bacteria '
                                                    'proliferate under pressure and '
                                                    'seed the bloodstream. Antibiotics '
                                                    'alone cannot reliably sterilize '
                                                    'an obstructed system—urgent '
                                                    'drainage (stent or nephrostomy) '
                                                    'plus antibiotics is required.'},
                                    {'question': 'Post-obstructive diuresis occurs '
                                                 'after?',
                                     'options': ['A) Initiation of alpha-blocker '
                                                 'therapy for BPH symptoms',
                                                 'B) Elective ureteroscopy for an '
                                                 'asymptomatic non-obstructing stone',
                                                 'C) Treatment of uncomplicated '
                                                 'cystitis without prior retention',
                                                 'D) Relief of chronic urinary '
                                                 'obstruction'],
                                     'answer': 'D) Relief of chronic urinary '
                                               'obstruction',
                                     'explanation': 'After relief of prolonged urinary '
                                                    'obstruction, previously '
                                                    'compressed tubules may '
                                                    'transiently fail to concentrate '
                                                    'urine and reabsorb sodium and '
                                                    'water, producing post-obstructive '
                                                    'diuresis. Careful fluid and '
                                                    'electrolyte monitoring is '
                                                    'required. Beta-blockers, '
                                                    'orthopedic surgery, and vaccines '
                                                    'are unrelated triggers.'},
                                    {'question': 'High-riding testis and absent '
                                                 'cremasteric reflex suggest?',
                                     'options': ['A) Testicular torsion until proven '
                                                 'otherwise',
                                                 'B) Isolated hydrocele without '
                                                 'ischemia',
                                                 'C) Epididymo-orchitis as the only '
                                                 'possibility',
                                                 'D) Reducible inguinal hernia alone'],
                                     'answer': 'A) Testicular torsion until proven '
                                               'otherwise',
                                     'explanation': 'Intravaginal torsion shortens the '
                                                    'spermatic cord, pulling the '
                                                    'testis higher and interrupting '
                                                    'the cremasteric reflex. With '
                                                    'acute unilateral scrotal pain, '
                                                    'this constellation is torsion '
                                                    'until proven otherwise and '
                                                    'warrants urgent surgical '
                                                    'exploration.'}],
                           'extreme': [{'question': 'Fournier gangrene is?',
                                        'options': ['A) Uncomplicated candidal '
                                                    'balanitis',
                                                    'B) Necrotizing infection of the '
                                                    'perineum/genitalia needing urgent '
                                                    'surgical debridement',
                                                    'C) Localized cellulitis without '
                                                    'fascial necrosis',
                                                    'D) Simple scrotal edema from '
                                                    'hypoalbuminemia'],
                                        'answer': 'B) Necrotizing infection of the '
                                                  'perineum/genitalia needing urgent '
                                                  'surgical debridement',
                                        'explanation': 'Fournier gangrene is a '
                                                       'synergistic necrotizing '
                                                       'soft-tissue infection of the '
                                                       'perineum and genitalia that '
                                                       'spreads along fascial planes. '
                                                       'Rapid necrosis and sepsis '
                                                       'demand immediate surgical '
                                                       'debridement plus broad '
                                                       'antibiotics—not topical '
                                                       'therapy for simple surface '
                                                       'infections.'},
                                       {'question': 'Autonomic dysreflexia in spinal '
                                                    'cord injury with bladder '
                                                    'distension can cause?',
                                        'options': ['A) Isolated orthostatic '
                                                    'hypotension',
                                                    'B) Primary bradycardia without '
                                                    'blood-pressure change',
                                                    'C) Dangerous hypertensive crisis '
                                                    'from unchecked sympathetic '
                                                    'discharge',
                                                    'D) Transient mild thirst without '
                                                    'autonomic instability'],
                                        'answer': 'C) Dangerous hypertensive crisis '
                                                  'from unchecked sympathetic '
                                                  'discharge',
                                        'explanation': 'In SCI above splanchnic '
                                                       'sympathetic outflow, a noxious '
                                                       'stimulus below the lesion '
                                                       '(commonly bladder distension) '
                                                       'triggers unchecked sympathetic '
                                                       'vasoconstriction, causing '
                                                       'dangerous hypertension. '
                                                       'Management centers on sitting '
                                                       'upright and relieving the '
                                                       'precipitant (empty the '
                                                       'bladder).'},
                                       {'question': 'A trauma patient with pelvic '
                                                    'fracture and blood at the meatus '
                                                    'should avoid?',
                                        'options': ['A) Application of a pelvic binder '
                                                    'when indicated for unstable '
                                                    'pelvic fracture',
                                                    'B) Standard trauma primary survey '
                                                    '(ABCs)',
                                                    'C) Early blood typing and '
                                                    'crossmatch',
                                                    'D) Blind urethral catheterization '
                                                    'before assessing for urethral '
                                                    'injury'],
                                        'answer': 'D) Blind urethral catheterization '
                                                  'before assessing for urethral '
                                                  'injury',
                                        'explanation': 'Pelvic fracture with blood at '
                                                       'the meatus suggests urethral '
                                                       'disruption. Blind '
                                                       'catheterization can convert a '
                                                       'partial tear into complete '
                                                       'transection or create a false '
                                                       'passage. Retrograde '
                                                       'urethrogram (or specialist '
                                                       'assessment) should precede '
                                                       'catheter attempts; binder, '
                                                       'ABCs, and crossmatch remain '
                                                       'appropriate trauma care.'}]},
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
               'questions': {'easy': [{'question': 'Sudden face/arm weakness with '
                                                   'speech difficulty suggests?',
                                       'options': ['A) Acute stroke (ischemic or '
                                                   'hemorrhagic) until proven '
                                                   'otherwise',
                                                   'B) Bell palsy without limb or '
                                                   'speech involvement',
                                                   'C) Migraine aura without '
                                                   'persistent focal deficit',
                                                   'D) Peripheral vestibular neuritis '
                                                   'alone'],
                                       'answer': 'A) Acute stroke (ischemic or '
                                                 'hemorrhagic) until proven otherwise',
                                       'explanation': 'Sudden focal neurologic '
                                                      'deficits such as facial droop, '
                                                      'arm weakness, and speech '
                                                      'difficulty reflect acute '
                                                      'ischemia or hemorrhage in a '
                                                      'corresponding brain region. '
                                                      'Because neuronal injury is '
                                                      'time-dependent, this '
                                                      'presentation is stroke until '
                                                      'proven otherwise and triggers '
                                                      'urgent stroke pathways.'},
                                      {'question': 'Meningism features include?',
                                       'options': ['A) Isolated tension-type headache '
                                                   'without fever or meningism',
                                                   'B) Neck stiffness with fever and '
                                                   'headache',
                                                   'C) Benign positional vertigo '
                                                   'without systemic signs',
                                                   'D) Cluster headache with autonomic '
                                                   'tearing alone'],
                                       'answer': 'B) Neck stiffness with fever and '
                                                 'headache',
                                       'explanation': 'Meningeal inflammation '
                                                      'sensitizes pain fibers, '
                                                      'producing headache with neck '
                                                      'stiffness (meningism), often '
                                                      'with fever and photophobia. '
                                                      'These features raise concern '
                                                      'for meningitis or subarachnoid '
                                                      'blood and warrant urgent '
                                                      'evaluation. Isolated primary '
                                                      'headache syndromes lack true '
                                                      'meningism with fever.'},
                                      {'question': 'UMN signs include?',
                                       'options': ['A) Fasciculations with '
                                                   'hyporeflexia and atrophy',
                                                   'B) Flaccid paralysis with '
                                                   'areflexia from acute LMN lesion',
                                                   'C) Extensor plantar response '
                                                   '(Babinski) and spasticity',
                                                   'D) Pure sensory loss without '
                                                   'pyramidal signs'],
                                       'answer': 'C) Extensor plantar response '
                                                 '(Babinski) and spasticity',
                                       'explanation': 'Upper motor neuron lesions '
                                                      'remove descending inhibition of '
                                                      'spinal reflex arcs, yielding '
                                                      'spasticity, hyperreflexia, and '
                                                      'an extensor plantar (Babinski) '
                                                      'response. Fasciculations, '
                                                      'hyporeflexia, and flaccid '
                                                      'areflexic weakness indicate '
                                                      'lower motor neuron or '
                                                      'peripheral pathology.'}],
                             'medium': [{'question': 'Thunderclap headache first '
                                                     'exclude?',
                                         'options': ['A) Typical migraine without '
                                                     'thunderclap onset',
                                                     'B) Acute bacterial sinusitis',
                                                     'C) Uncomplicated tension-type '
                                                     'headache',
                                                     'D) Aneurysmal subarachnoid '
                                                     'hemorrhage'],
                                         'answer': 'D) Aneurysmal subarachnoid '
                                                   'hemorrhage',
                                         'explanation': 'Thunderclap headache reaches '
                                                        'maximal intensity within '
                                                        'seconds and is the classic '
                                                        'presentation of aneurysmal '
                                                        'SAH. Missed SAH is '
                                                        'catastrophic, so '
                                                        'sudden-maximal headache '
                                                        'requires urgent CT and, if '
                                                        'needed, LP—not attribution to '
                                                        'primary headache until SAH is '
                                                        'excluded.'},
                                        {'question': 'Absence seizures are most '
                                                     'typical in?',
                                         'options': ['A) School-age children with '
                                                     'brief staring spells',
                                                     'B) Elderly patients with new '
                                                     'atrial fibrillation',
                                                     'C) Neonates with physiologic '
                                                     'jaundice alone',
                                                     'D) Adults with classic migraine '
                                                     'with visual aura'],
                                         'answer': 'A) School-age children with brief '
                                                   'staring spells',
                                         'explanation': 'Absence seizures are '
                                                        'generalized childhood '
                                                        'seizures from oscillatory '
                                                        'thalamocortical discharges '
                                                        '(3-Hz spike-and-wave on EEG). '
                                                        'They appear as brief staring '
                                                        'spells lasting seconds with '
                                                        'immediate recovery. They are '
                                                        'not the typical seizure type '
                                                        'of AF-related stroke, '
                                                        'neonatal jaundice, or '
                                                        'migraine aura.'},
                                        {'question': 'Parkinsonism core motor feature '
                                                     'is?',
                                         'options': ['A) Hyperreflexia as the defining '
                                                     'core feature',
                                                     'B) Bradykinesia',
                                                     'C) Flaccid paralysis',
                                                     'D) Pure intention tremor without '
                                                     'bradykinesia'],
                                         'answer': 'B) Bradykinesia',
                                         'explanation': 'Parkinsonism reflects '
                                                        'nigrostriatal dopamine '
                                                        'deficiency slowing movement '
                                                        'initiation and execution. '
                                                        'Bradykinesia is the core '
                                                        'required motor feature; rest '
                                                        'tremor and rigidity commonly '
                                                        'accompany it. Hyperreflexia '
                                                        'suggests UMN disease; flaccid '
                                                        'paralysis and isolated '
                                                        'intention tremor suggest '
                                                        'other localizations.'}],
                             'hard': [{'question': 'Status epilepticus initial '
                                                   'management concept?',
                                       'options': ['A) Observation for several hours '
                                                   'before any antiseizure medication',
                                                   'B) Levetiracetam monotherapy '
                                                   'without initial benzodiazepine '
                                                   'when seizing',
                                                   'C) Airway support plus early '
                                                   'benzodiazepine, then escalate '
                                                   'antiseizure medicines',
                                                   'D) Immediate neurosurgical '
                                                   'resection as the first step in all '
                                                   'SE'],
                                       'answer': 'C) Airway support plus early '
                                                 'benzodiazepine, then escalate '
                                                 'antiseizure medicines',
                                       'explanation': 'Status epilepticus causes '
                                                      'progressive neuronal injury and '
                                                      'systemic complications. After '
                                                      'ABCs, a benzodiazepine is given '
                                                      'promptly, then second-line '
                                                      'antiseizure drugs if seizures '
                                                      'continue. Delayed treatment '
                                                      'worsens outcomes; skipping the '
                                                      'benzodiazepine step or jumping '
                                                      'first to surgery is '
                                                      'inappropriate for initial SE '
                                                      'care.'},
                                      {'question': 'Crossed cranial-nerve plus '
                                                   'contralateral body signs localize '
                                                   'to?',
                                       'options': ['A) Pure cortical convexity lesion '
                                                   'without brainstem signs',
                                                   'B) Distal peripheral nerve only',
                                                   'C) Muscle end-plate disorder alone',
                                                   'D) Brainstem'],
                                       'answer': 'D) Brainstem',
                                       'explanation': 'Crossed findings—ipsilateral '
                                                      'cranial-nerve signs with '
                                                      'contralateral body weakness or '
                                                      'sensory loss—are the hallmark '
                                                      'of brainstem localization where '
                                                      'cranial-nerve nuclei and long '
                                                      'tracts are closely packed. '
                                                      'Cortex, peripheral nerve, and '
                                                      'NMJ disorders do not produce '
                                                      'this crossed pattern.'},
                                      {'question': 'Myasthenia gravis fatigable '
                                                   'weakness often involves?',
                                       'options': ['A) Ocular and bulbar muscles '
                                                   '(fatigable ptosis, diplopia, '
                                                   'dysarthria)',
                                                   'B) Distal sensory neuropathy as '
                                                   'the primary feature',
                                                   'C) Upper motor neuron spastic '
                                                   'paraparesis alone',
                                                   'D) Cerebellar ataxia without '
                                                   'fatigable weakness'],
                                       'answer': 'A) Ocular and bulbar muscles '
                                                 '(fatigable ptosis, diplopia, '
                                                 'dysarthria)',
                                       'explanation': 'Myasthenia gravis is an '
                                                      'autoimmune attack on '
                                                      'postsynaptic acetylcholine '
                                                      'receptors, causing fatigable '
                                                      'weakness that preferentially '
                                                      'affects ocular and bulbar '
                                                      'muscles. Sensory loss, pure UMN '
                                                      'spasticity, and cerebellar '
                                                      'ataxia indicate other disease '
                                                      'categories.'}],
                             'extreme': [{'question': 'Spinal cord compression with '
                                                      'saddle anesthesia and retention '
                                                      'needs?',
                                          'options': ['A) Elective outpatient '
                                                      'physiotherapy starting in weeks',
                                                      'B) Urgent MRI and surgical '
                                                      'decompression pathway',
                                                      'C) Oral analgesia alone without '
                                                      'imaging',
                                                      'D) Delayed review after '
                                                      'incomplete bladder emptying is '
                                                      'ignored'],
                                          'answer': 'B) Urgent MRI and surgical '
                                                    'decompression pathway',
                                          'explanation': 'Saddle anesthesia with '
                                                         'urinary retention suggests '
                                                         'cauda equina or cord '
                                                         'compression. Cord/cauda '
                                                         'compression is '
                                                         'time-critical: urgent '
                                                         'imaging and decompression '
                                                         'can preserve sphincter and '
                                                         'motor function. Delayed '
                                                         'conservative care risks '
                                                         'permanent deficit.'},
                                         {'question': 'Locked-in syndrome typically '
                                                      'localizes to?',
                                          'options': ['A) Bilateral occipital lobes',
                                                      'B) Dominant parietal cortex '
                                                      'alone',
                                                      'C) Bilateral ventral pons',
                                                      'D) Cervical dorsal columns '
                                                      'only'],
                                          'answer': 'C) Bilateral ventral pons',
                                          'explanation': 'Locked-in syndrome reflects '
                                                         'bilateral ventral pontine '
                                                         'injury (often basilar artery '
                                                         'occlusion) disrupting '
                                                         'corticospinal and '
                                                         'corticobulbar fibers while '
                                                         'sparing consciousness and '
                                                         'vertical eye movements '
                                                         'mediated more dorsally. '
                                                         'Occipital, parietal, and '
                                                         'dorsal-column lesions '
                                                         'produce different '
                                                         'syndromes.'},
                                         {'question': 'NMDA-receptor encephalitis is '
                                                      'often discussed in association '
                                                      'with?',
                                          'options': ['A) Thymoma as the most classic '
                                                      'tumor link',
                                                      'B) Small-cell lung cancer as '
                                                      'the primary association',
                                                      'C) Pheochromocytoma as the '
                                                      'usual trigger',
                                                      'D) Ovarian teratoma in young '
                                                      'women'],
                                          'answer': 'D) Ovarian teratoma in young '
                                                    'women',
                                          'explanation': 'Anti-NMDA-receptor '
                                                         'encephalitis often presents '
                                                         'with psychiatric features, '
                                                         'seizures, dyskinesias, and '
                                                         'autonomic instability; in '
                                                         'young women it is '
                                                         'classically associated with '
                                                         'ovarian teratoma. Thymoma '
                                                         'links to myasthenia; SCLC to '
                                                         'Lambert-Eaton and other '
                                                         'paraneoplastic syndromes.'}]},
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
                 'questions': {'easy': [{'question': 'Common CAP organism?',
                                         'options': ['A) Streptococcus pneumoniae',
                                                     'B) Mycobacterium tuberculosis as '
                                                     'the usual CAP pathogen',
                                                     'C) Pneumocystis jirovecii in '
                                                     'immunocompetent hosts',
                                                     'D) Pseudomonas aeruginosa in '
                                                     'previously healthy adults'],
                                         'answer': 'A) Streptococcus pneumoniae',
                                         'explanation': 'Streptococcus pneumoniae '
                                                        'remains the most common '
                                                        'identified bacterial cause of '
                                                        'community-acquired pneumonia '
                                                        'in adults. TB, Pneumocystis, '
                                                        'and Pseudomonas are important '
                                                        'in specific host or exposure '
                                                        'contexts but are not the '
                                                        'typical CAP organism in '
                                                        'otherwise healthy community '
                                                        'patients.'},
                                        {'question': 'Asthma is characterized by?',
                                         'options': ['A) Fixed irreversible '
                                                     'obstruction from birth without '
                                                     'variability',
                                                     'B) Reversible airflow '
                                                     'obstruction with airway '
                                                     'hyperresponsiveness',
                                                     'C) Alveolar filling with '
                                                     'bacteria as the defining '
                                                     'mechanism',
                                                     'D) Pulmonary vascular '
                                                     'obliteration as the primary '
                                                     'process'],
                                         'answer': 'B) Reversible airflow obstruction '
                                                   'with airway hyperresponsiveness',
                                         'explanation': 'Asthma is characterized by '
                                                        'variable, reversible airway '
                                                        'obstruction and bronchial '
                                                        'hyperresponsiveness driven by '
                                                        'airway inflammation. Fixed '
                                                        'irreversible obstruction '
                                                        'describes COPD '
                                                        'emphysema/chronic bronchitis '
                                                        'patterns better; alveolar '
                                                        'infection and pure vascular '
                                                        'disease are different '
                                                        'entities.'},
                                        {'question': 'SpO2 measures?',
                                         'options': ['A) Partial pressure of arterial '
                                                     'carbon dioxide',
                                                     'B) Hemoglobin concentration',
                                                     'C) Approximate arterial oxygen '
                                                     'saturation of hemoglobin',
                                                     'D) Alveolar minute ventilation '
                                                     'directly'],
                                         'answer': 'C) Approximate arterial oxygen '
                                                   'saturation of hemoglobin',
                                         'explanation': 'Pulse oximetry estimates the '
                                                        'percentage of hemoglobin '
                                                        'saturated with oxygen using '
                                                        'light absorption. It does not '
                                                        'measure PaCO2, hemoglobin '
                                                        'amount, or ventilation '
                                                        'directly—ABG and other tests '
                                                        'are needed for those '
                                                        'parameters.'}],
                               'medium': [{'question': 'CURB-65 assesses?',
                                           'options': ['A) Pulmonary embolism pretest '
                                                       'probability',
                                                       'B) Asthma control over the '
                                                       'prior four weeks',
                                                       'C) Lung-cancer staging',
                                                       'D) Community-acquired '
                                                       'pneumonia severity and '
                                                       'disposition risk'],
                                           'answer': 'D) Community-acquired pneumonia '
                                                     'severity and disposition risk',
                                           'explanation': 'CURB-65 (Confusion, Urea, '
                                                          'Respiratory rate, Blood '
                                                          'pressure, age ≥65) '
                                                          'stratifies CAP severity and '
                                                          'helps guide site-of-care '
                                                          'decisions. Wells scoring '
                                                          'addresses PE probability; '
                                                          'asthma control and cancer '
                                                          'staging use different '
                                                          'tools.'},
                                          {'question': 'Wells score helps for?',
                                           'options': ['A) Pulmonary embolism pretest '
                                                       'probability',
                                                       'B) COPD exacerbation severity '
                                                       'alone',
                                                       'C) Community-acquired '
                                                       'pneumonia mortality alone',
                                                       'D) Pulmonary hypertension WHO '
                                                       'group classification'],
                                           'answer': 'A) Pulmonary embolism pretest '
                                                     'probability',
                                           'explanation': 'The Wells score combines '
                                                          'clinical features to '
                                                          'estimate pretest '
                                                          'probability of PE and guide '
                                                          'D-dimer versus imaging '
                                                          'pathways. It is not a COPD, '
                                                          'CAP, or PH classification '
                                                          'instrument.'},
                                          {'question': 'COPD oxygen target in many '
                                                       'retainers is often?',
                                           'options': ['A) Unrestricted high-flow '
                                                       'oxygen to SpO2 100% in all '
                                                       'COPD patients',
                                                       'B) A controlled SpO2 target '
                                                       'such as 88–92% per protocol in '
                                                       'CO2 retainers',
                                                       'C) No supplemental oxygen even '
                                                       'if SpO2 is 70%',
                                                       'D) Oxygen titrated only to '
                                                       'relieve dyspnea without SpO2 '
                                                       'targets'],
                                           'answer': 'B) A controlled SpO2 target such '
                                                     'as 88–92% per protocol in CO2 '
                                                     'retainers',
                                           'explanation': 'In chronic CO2 retainers, '
                                                          'excessive oxygen can worsen '
                                                          'hypercapnia via V/Q change '
                                                          'and reduced hypoxic drive. '
                                                          'Controlled oxygen targeting '
                                                          '(often 88–92%) balances '
                                                          'hypoxemia treatment against '
                                                          'CO2 retention risk, guided '
                                                          'by protocol and ABG.'}],
                               'hard': [{'question': 'Tension pneumothorax treatment '
                                                     'concept?',
                                         'options': ['A) Urgent CT confirmation before '
                                                     'any decompression if unstable',
                                                     'B) High-dose IV steroid as '
                                                     'primary therapy',
                                                     'C) Immediate needle/finger '
                                                     'thoracostomy decompression then '
                                                     'definitive chest drain',
                                                     'D) Noninvasive ventilation alone '
                                                     'without decompression'],
                                         'answer': 'C) Immediate needle/finger '
                                                   'thoracostomy decompression then '
                                                   'definitive chest drain',
                                         'explanation': 'Tension pneumothorax causes '
                                                        'obstructive shock by raising '
                                                        'intrapleural pressure, '
                                                        'collapsing the lung, and '
                                                        'impairing venous return. '
                                                        'Unstable patients need '
                                                        'immediate decompression '
                                                        'followed by chest-tube '
                                                        'drainage; imaging must not '
                                                        'delay treatment.'},
                                        {'question': "Light's criteria relate to?",
                                         'options': ['A) Staging primary lung cancer',
                                                     'B) Calculating A-a oxygen '
                                                     'gradient',
                                                     'C) Diagnosing pulmonary '
                                                     'hypertension by echo criteria',
                                                     'D) Distinguishing pleural '
                                                     'exudate from transudate'],
                                         'answer': 'D) Distinguishing pleural exudate '
                                                   'from transudate',
                                         'explanation': "Light's criteria compare "
                                                        'pleural and serum protein/LDH '
                                                        'ratios to separate exudates '
                                                        '(infection, malignancy, '
                                                        'inflammation) from '
                                                        'transudates (heart failure, '
                                                        'cirrhosis). They do not stage '
                                                        'cancer, compute A-a gradient, '
                                                        'or diagnose PH.'},
                                        {'question': 'Massive hemoptysis priority is?',
                                         'options': ['A) Airway protection with '
                                                     'bleeding lung dependent (down)',
                                                     'B) Encourage vigorous coughing '
                                                     'unsupervised as sole therapy',
                                                     'C) Immediate full '
                                                     'anticoagulation before airway '
                                                     'control',
                                                     'D) Routine outpatient follow-up '
                                                     'without emergency assessment'],
                                         'answer': 'A) Airway protection with bleeding '
                                                   'lung dependent (down)',
                                         'explanation': 'Massive hemoptysis threatens '
                                                        'asphyxiation more than '
                                                        'exsanguination. Priority is '
                                                        'airway protection—often '
                                                        'positioning the bleeding side '
                                                        'down so blood does not flood '
                                                        'the good lung—then urgent '
                                                        'specialist control of '
                                                        'bleeding.'}],
                               'extreme': [{'question': 'ARDS Berlin concept includes?',
                                            'options': ['A) Chronic stable hypoxemia '
                                                        'from COPD without acute '
                                                        'bilateral infiltrates',
                                                        'B) Acute hypoxemic '
                                                        'respiratory failure with '
                                                        'bilateral opacities not fully '
                                                        'explained by heart failure',
                                                        'C) Isolated lobar pneumonia '
                                                        'fully explained by typical '
                                                        'CAP alone',
                                                        'D) Cardiogenic edema as the '
                                                        'required sole explanation for '
                                                        'all bilateral opacities'],
                                            'answer': 'B) Acute hypoxemic respiratory '
                                                      'failure with bilateral '
                                                      'opacities not fully explained '
                                                      'by heart failure',
                                            'explanation': 'The Berlin definition of '
                                                           'ARDS requires acute onset, '
                                                           'bilateral opacities, and '
                                                           'hypoxemia not fully '
                                                           'explained by cardiac '
                                                           'failure or fluid overload, '
                                                           'reflecting diffuse '
                                                           'alveolar damage. Chronic '
                                                           'COPD hypoxemia and simple '
                                                           'lobar CAP do not meet this '
                                                           'construct.'},
                                           {'question': 'Fat embolism triad after '
                                                        'fracture?',
                                            'options': ['A) Isolated deep-vein '
                                                        'thrombosis without pulmonary '
                                                        'or skin findings',
                                                        'B) Fever and productive cough '
                                                        'alone without neurologic or '
                                                        'petechial signs',
                                                        'C) Respiratory distress, '
                                                        'neurologic change, and '
                                                        'petechial rash',
                                                        'D) Chronic exertional dyspnea '
                                                        'without acute fracture '
                                                        'context'],
                                            'answer': 'C) Respiratory distress, '
                                                      'neurologic change, and '
                                                      'petechial rash',
                                            'explanation': 'Fat embolism syndrome '
                                                           'classically follows '
                                                           'long-bone or pelvic '
                                                           'fracture and presents with '
                                                           'the triad of acute '
                                                           'respiratory distress, '
                                                           'neurologic dysfunction, '
                                                           'and petechiae (often '
                                                           'axillary/conjunctival). '
                                                           'Isolated DVT or simple '
                                                           'pneumonia lacks this '
                                                           'triad.'},
                                           {'question': 'Bronchial carcinoid can cause '
                                                        'which syndrome theme?',
                                            'options': ['A) Cushing syndrome from '
                                                        'ectopic ACTH as the usual '
                                                        'presentation of all bronchial '
                                                        'carcinoids',
                                                        'B) Isolated SIADH as the '
                                                        'defining carcinoid syndrome '
                                                        'feature',
                                                        'C) Hypoglycemia from insulin '
                                                        'secretion as the classic '
                                                        'carcinoid mediator effect',
                                                        'D) Carcinoid syndrome with '
                                                        'flushing and diarrhea when '
                                                        'vasoactive mediators reach '
                                                        'the systemic circulation '
                                                        '(often with metastases)'],
                                            'answer': 'D) Carcinoid syndrome with '
                                                      'flushing and diarrhea when '
                                                      'vasoactive mediators reach the '
                                                      'systemic circulation (often '
                                                      'with metastases)',
                                            'explanation': 'Bronchial carcinoid can '
                                                           'release vasoactive '
                                                           'mediators; classic '
                                                           'carcinoid syndrome '
                                                           '(flushing, diarrhea, '
                                                           'bronchospasm) typically '
                                                           'appears when mediators '
                                                           'escape hepatic metabolism, '
                                                           'often with metastatic '
                                                           'disease. Ectopic ACTH, '
                                                           'SIADH, and insulinoma '
                                                           'physiology are different '
                                                           'neuroendocrine '
                                                           'syndromes.'}]},
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
                      'questions': {'easy': [{'question': 'Charcot triad indicates?',
                                              'options': ['A) Ascending cholangitis',
                                                          'B) Uncomplicated '
                                                          'cholelithiasis without '
                                                          'infection',
                                                          'C) Acute hepatitis A '
                                                          'without biliary obstruction',
                                                          'D) Peptic ulcer disease '
                                                          'without biliary sepsis'],
                                              'answer': 'A) Ascending cholangitis',
                                              'explanation': 'Charcot '
                                                             'triad—right-upper-quadrant '
                                                             'pain, fever, and '
                                                             'jaundice—indicates '
                                                             'ascending cholangitis '
                                                             'from infected biliary '
                                                             'obstruction. '
                                                             'Uncomplicated stones, '
                                                             'viral hepatitis, and '
                                                             'peptic ulcer lack this '
                                                             'infected-obstruction '
                                                             'pattern.'},
                                             {'question': 'H. pylori is linked to?',
                                              'options': ['A) Celiac disease as the '
                                                          'primary H. pylori '
                                                          'manifestation',
                                                          'B) Peptic ulcer disease',
                                                          'C) Pancreatic '
                                                          'adenocarcinoma as the main '
                                                          'H. pylori link',
                                                          'D) Gilbert syndrome'],
                                              'answer': 'B) Peptic ulcer disease',
                                              'explanation': 'Helicobacter pylori '
                                                             'colonizes gastric '
                                                             'mucosa, driving chronic '
                                                             'gastritis and '
                                                             'substantially increasing '
                                                             'risk of duodenal and '
                                                             'gastric peptic ulcers '
                                                             '(and some gastric '
                                                             'cancers). It is not the '
                                                             'primary mechanism of '
                                                             'celiac disease, '
                                                             'pancreatic '
                                                             'adenocarcinoma, or '
                                                             'Gilbert syndrome.'},
                                             {'question': "McBurney's point relates "
                                                          'to?',
                                              'options': ['A) Acute cholecystitis',
                                                          'B) Sigmoid diverticulitis',
                                                          'C) Appendicitis',
                                                          'D) Left-sided ureteric '
                                                          'colic'],
                                              'answer': 'C) Appendicitis',
                                              'explanation': "McBurney's point lies "
                                                             'one-third of the way '
                                                             'from the right anterior '
                                                             'superior iliac spine to '
                                                             'the umbilicus and is the '
                                                             'classic site of maximal '
                                                             'tenderness in acute '
                                                             'appendicitis. '
                                                             'Cholecystitis, '
                                                             'diverticulitis, and left '
                                                             'ureteric colic localize '
                                                             'elsewhere.'}],
                                    'medium': [{'question': 'Pancreatitis pain often '
                                                            'radiates to?',
                                                'options': ['A) The right shoulder tip '
                                                            'alone as the only '
                                                            'radiation pattern',
                                                            'B) The left groin '
                                                            'exclusively',
                                                            'C) The occiput',
                                                            'D) The back'],
                                                'answer': 'D) The back',
                                                'explanation': 'Acute pancreatitis '
                                                               'typically causes '
                                                               'severe epigastric pain '
                                                               'that radiates through '
                                                               'to the back because '
                                                               'the inflamed '
                                                               'retroperitoneal '
                                                               'pancreas lies against '
                                                               'posterior structures. '
                                                               'Shoulder-tip pain '
                                                               'suggests diaphragmatic '
                                                               'irritation (e.g., '
                                                               'biliary), and groin '
                                                               'pain suggests urologic '
                                                               'referred pain.'},
                                               {'question': 'Variceal bleed risk is '
                                                            'highest in?',
                                                'options': ['A) Portal hypertension '
                                                            'from cirrhosis',
                                                            'B) Uncomplicated peptic '
                                                            'ulcer without portal '
                                                            'hypertension',
                                                            'C) Mild gastroesophageal '
                                                            'reflux disease',
                                                            'D) Diverticular bleeding '
                                                            'from colonic diverticula '
                                                            'as the same mechanism'],
                                                'answer': 'A) Portal hypertension from '
                                                          'cirrhosis',
                                                'explanation': 'Esophageal varices '
                                                               'form when portal '
                                                               'hypertension opens '
                                                               'portosystemic '
                                                               'collaterals; rupture '
                                                               'causes '
                                                               'life-threatening upper '
                                                               'GI bleeding, most '
                                                               'often in cirrhosis. '
                                                               'Peptic ulcer and '
                                                               'diverticular bleeding '
                                                               'are important but '
                                                               'mechanistically '
                                                               'distinct.'},
                                               {'question': 'IBD alarm features '
                                                            'include?',
                                                'options': ['A) Occasional '
                                                            'postprandial bloating '
                                                            'alone',
                                                            'B) Bleeding, weight loss, '
                                                            'and nocturnal diarrhea',
                                                            'C) Infrequent soft stools '
                                                            'without systemic features',
                                                            'D) Mild intermittent '
                                                            'abdominal discomfort '
                                                            'without alarm signs'],
                                                'answer': 'B) Bleeding, weight loss, '
                                                          'and nocturnal diarrhea',
                                                'explanation': 'Alarm features in '
                                                               'suspected IBD include '
                                                               'rectal bleeding, '
                                                               'unintentional weight '
                                                               'loss, and nocturnal '
                                                               'diarrhea, which '
                                                               'increase likelihood of '
                                                               'inflammatory or '
                                                               'serious organic '
                                                               'disease and warrant '
                                                               'urgent investigation '
                                                               'rather than assuming '
                                                               'functional bowel '
                                                               'disease.'}],
                                    'hard': [{'question': 'Reynolds pentad adds what '
                                                          'to Charcot triad?',
                                              'options': ['A) Isolated pruritus '
                                                          'without sepsis',
                                                          'B) Mild steatorrhea alone',
                                                          'C) Hypotension and mental '
                                                          'status change (confusion)',
                                                          'D) Asymptomatic '
                                                          'hyperbilirubinemia alone'],
                                              'answer': 'C) Hypotension and mental '
                                                        'status change (confusion)',
                                              'explanation': 'Reynolds pentad adds '
                                                             'hypotension and '
                                                             'confusion to Charcot '
                                                             'triad, indicating '
                                                             'cholangitis with septic '
                                                             'shock and organ '
                                                             'dysfunction. These '
                                                             'additions mark a '
                                                             'surgical/endoscopic '
                                                             'emergency beyond '
                                                             'uncomplicated biliary '
                                                             'colic or isolated '
                                                             'jaundice.'},
                                             {'question': 'SBP in ascites is diagnosed '
                                                          'by?',
                                              'options': ['A) Serum-ascites albumin '
                                                          'gradient alone without cell '
                                                          'count',
                                                          'B) Stool culture as the '
                                                          'primary SBP test',
                                                          'C) Abdominal wall '
                                                          'ultrasound without '
                                                          'paracentesis',
                                                          'D) Ascitic fluid PMN count '
                                                          'above diagnostic threshold '
                                                          'plus clinical context'],
                                              'answer': 'D) Ascitic fluid PMN count '
                                                        'above diagnostic threshold '
                                                        'plus clinical context',
                                              'explanation': 'Spontaneous bacterial '
                                                             'peritonitis is diagnosed '
                                                             'by ascitic fluid '
                                                             'analysis, typically an '
                                                             'absolute PMN count ≥250 '
                                                             'cells/µL in the '
                                                             'appropriate clinical '
                                                             'setting, often with '
                                                             'culture in blood-culture '
                                                             'bottles. SAAG classifies '
                                                             'portal hypertension; it '
                                                             'does not replace the '
                                                             'cell count for SBP.'},
                                             {'question': 'Boerhaave syndrome is?',
                                              'options': ['A) Full-thickness '
                                                          'esophageal perforation '
                                                          'after forceful vomiting',
                                                          'B) Partial mucosal tear of '
                                                          'Mallory-Weiss syndrome only',
                                                          'C) Spontaneous pneumothorax '
                                                          'unrelated to the esophagus',
                                                          'D) Perforated peptic ulcer '
                                                          'as the same entity'],
                                              'answer': 'A) Full-thickness esophageal '
                                                        'perforation after forceful '
                                                        'vomiting',
                                              'explanation': 'Boerhaave syndrome is '
                                                             'transmural esophageal '
                                                             'rupture, classically '
                                                             'after forceful vomiting, '
                                                             'causing mediastinitis '
                                                             'and septic shock. '
                                                             'Mallory-Weiss is a '
                                                             'mucosal tear with '
                                                             'bleeding; peptic '
                                                             'perforation and primary '
                                                             'pneumothorax are '
                                                             'different diagnoses.'}],
                                    'extreme': [{'question': 'Mesenteric ischemia '
                                                             'classic risk pattern?',
                                                 'options': ['A) Young patient with '
                                                             'chronic epigastric '
                                                             'burning relieved by food',
                                                             'B) Atrial fibrillation '
                                                             'with sudden severe '
                                                             'abdominal pain out of '
                                                             'proportion to '
                                                             'examination',
                                                             'C) Gradual '
                                                             'left-lower-quadrant pain '
                                                             'with diverticulosis risk '
                                                             'only',
                                                             'D) Biliary colic after '
                                                             'fatty meals without '
                                                             'vascular risk'],
                                                 'answer': 'B) Atrial fibrillation '
                                                           'with sudden severe '
                                                           'abdominal pain out of '
                                                           'proportion to examination',
                                                 'explanation': 'Acute mesenteric '
                                                                'ischemia from embolus '
                                                                'often occurs in AF: '
                                                                'sudden severe pain '
                                                                'out of proportion to '
                                                                'early physical '
                                                                'findings as bowel '
                                                                'becomes ischemic '
                                                                'before peritonitis '
                                                                'develops. Early CT '
                                                                'angiography and '
                                                                'revascularization '
                                                                'pathways are '
                                                                'critical.'},
                                                {'question': 'Toxic megacolon is a '
                                                             'complication of?',
                                                 'options': ['A) Uncomplicated peptic '
                                                             'ulcer disease',
                                                             'B) Gilbert syndrome',
                                                             'C) Severe colitis such '
                                                             'as IBD flare or '
                                                             'Clostridioides difficile '
                                                             'infection',
                                                             'D) Mild gastroesophageal '
                                                             'reflux'],
                                                 'answer': 'C) Severe colitis such as '
                                                           'IBD flare or '
                                                           'Clostridioides difficile '
                                                           'infection',
                                                 'explanation': 'Toxic megacolon is '
                                                                'acute colonic '
                                                                'dilation with '
                                                                'systemic toxicity '
                                                                'complicating severe '
                                                                'colitis—classically '
                                                                'IBD or C. difficile. '
                                                                'It risks perforation '
                                                                'and requires urgent '
                                                                'medical/surgical '
                                                                'management, unlike '
                                                                'ulcer, Gilbert, or '
                                                                'reflux disease.'},
                                                {'question': 'Budd-Chiari involves?',
                                                 'options': ['A) Portal vein '
                                                             'thrombosis alone as the '
                                                             'identical syndrome',
                                                             'B) Extrahepatic '
                                                             'bile-duct stone without '
                                                             'venous occlusion',
                                                             'C) Hepatic artery '
                                                             'stenosis after '
                                                             'transplant as the '
                                                             'classic Budd-Chiari '
                                                             'definition',
                                                             'D) Hepatic venous '
                                                             'outflow obstruction'],
                                                 'answer': 'D) Hepatic venous outflow '
                                                           'obstruction',
                                                 'explanation': 'Budd-Chiari syndrome '
                                                                'is hepatic venous '
                                                                'outflow obstruction '
                                                                '(hepatic veins or '
                                                                'IVC), causing '
                                                                'congestion, '
                                                                'hepatomegaly, '
                                                                'ascites, and liver '
                                                                'dysfunction. Portal '
                                                                'vein thrombosis is a '
                                                                'related but distinct '
                                                                'vascular disorder; '
                                                                'biliary stones are '
                                                                'not venous outflow '
                                                                'disease.'}]},
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
                   'questions': {'easy': [{'question': 'DKA includes?',
                                           'options': ['A) Hyperglycemia, '
                                                       'ketonemia/ketonuria, and '
                                                       'metabolic acidosis',
                                                       'B) Isolated hyperglycemia '
                                                       'without ketones or acidosis',
                                                       'C) Hypoglycemia with elevated '
                                                       'insulin alone',
                                                       'D) Hyperosmolar state without '
                                                       'acidosis or ketones as the DKA '
                                                       'definition'],
                                           'answer': 'A) Hyperglycemia, '
                                                     'ketonemia/ketonuria, and '
                                                     'metabolic acidosis',
                                           'explanation': 'Diabetic ketoacidosis '
                                                          'combines absolute/relative '
                                                          'insulin deficiency with '
                                                          'counter-regulatory hormone '
                                                          'excess, producing '
                                                          'hyperglycemia, ketone '
                                                          'generation, and '
                                                          'high-anion-gap metabolic '
                                                          'acidosis. Isolated '
                                                          'hyperglycemia or HHS '
                                                          'without significant '
                                                          'ketoacidosis are different '
                                                          'entities.'},
                                          {'question': 'First-line drug often for '
                                                       'T2DM?',
                                           'options': ['A) Immediate insulin pump '
                                                       'therapy for all new T2DM',
                                                       'B) Metformin when not '
                                                       'contraindicated',
                                                       'C) High-dose glucocorticoid as '
                                                       'glucose-lowering therapy',
                                                       'D) Somatostatin analogue as '
                                                       'first-line oral agent'],
                                           'answer': 'B) Metformin when not '
                                                     'contraindicated',
                                           'explanation': 'Metformin is guideline '
                                                          'first-line pharmacotherapy '
                                                          'for many adults with type 2 '
                                                          'diabetes when eGFR and '
                                                          'tolerability allow, '
                                                          'improving insulin '
                                                          'sensitivity and lowering '
                                                          'hepatic glucose output. '
                                                          'Insulin pumps, steroids, '
                                                          'and somatostatin analogues '
                                                          'are not standard first-line '
                                                          'T2DM drugs.'},
                                          {'question': 'Primary hypothyroidism labs '
                                                       'usually show?',
                                           'options': ['A) Suppressed TSH with high '
                                                       'free T4',
                                                       'B) Normal TSH with high free '
                                                       'T4',
                                                       'C) Elevated TSH with low free '
                                                       'T4',
                                                       'D) Low TSH with low free T4 as '
                                                       'the typical primary pattern'],
                                           'answer': 'C) Elevated TSH with low free T4',
                                           'explanation': 'Primary hypothyroidism is '
                                                          'failure of the thyroid '
                                                          'gland; pituitary TSH rises '
                                                          'in response while free T4 '
                                                          'falls. Suppressed TSH with '
                                                          'high T4 indicates '
                                                          'hyperthyroidism; low TSH '
                                                          'with low T4 suggests '
                                                          'central (secondary) '
                                                          'hypothyroidism.'}],
                                 'medium': [{'question': 'Chvostek/Trousseau suggest?',
                                             'options': ['A) Hypercalcemia of '
                                                         'malignancy',
                                                         'B) Isolated hyperkalemia '
                                                         'without calcium change',
                                                         'C) Hyponatremia from SIADH',
                                                         'D) Hypocalcemia'],
                                             'answer': 'D) Hypocalcemia',
                                             'explanation': 'Chvostek and Trousseau '
                                                            'signs reflect '
                                                            'neuromuscular '
                                                            'irritability from low '
                                                            'ionized calcium. '
                                                            'Hypercalcemia tends to '
                                                            'cause the opposite '
                                                            '(lethargy, polyuria); '
                                                            'potassium and sodium '
                                                            'disorders have different '
                                                            'neuromuscular '
                                                            'signatures.'},
                                            {'question': 'Graves disease is a cause '
                                                         'of?',
                                             'options': ['A) Hyperthyroidism '
                                                         '(thyrotoxicosis)',
                                                         'B) Primary hypothyroidism '
                                                         'from gland failure',
                                                         'C) Central diabetes '
                                                         'insipidus',
                                                         'D) Primary adrenal '
                                                         'insufficiency as the main '
                                                         'Graves effect'],
                                             'answer': 'A) Hyperthyroidism '
                                                       '(thyrotoxicosis)',
                                             'explanation': 'Graves disease is '
                                                            'TSH-receptor-stimulating '
                                                            'antibody–mediated '
                                                            'hyperthyroidism with '
                                                            'goiter and often '
                                                            'orbitopathy. It raises '
                                                            'thyroid hormone '
                                                            'production rather than '
                                                            'causing primary '
                                                            'hypothyroidism, DI, or '
                                                            'Addison disease as its '
                                                            'core lesion.'},
                                            {'question': 'Adrenal crisis needs?',
                                             'options': ['A) Fluid restriction as the '
                                                         'primary intervention',
                                                         'B) Urgent glucocorticoids '
                                                         'plus volume resuscitation',
                                                         'C) High-dose insulin '
                                                         'infusion without steroid '
                                                         'replacement',
                                                         'D) Radioiodine ablation '
                                                         'during shock'],
                                             'answer': 'B) Urgent glucocorticoids plus '
                                                       'volume resuscitation',
                                             'explanation': 'Adrenal crisis is '
                                                            'life-threatening cortisol '
                                                            'deficiency with shock and '
                                                            'electrolyte disturbance. '
                                                            'Immediate IV '
                                                            'hydrocortisone and '
                                                            'aggressive saline '
                                                            'resuscitation are '
                                                            'required; delay for '
                                                            'confirmatory testing is '
                                                            'dangerous once the '
                                                            'diagnosis is suspected.'}],
                                 'hard': [{'question': 'HHS differs from DKA by?',
                                           'options': ['A) Prominent high-anion-gap '
                                                       'ketoacidosis as the defining '
                                                       'HHS feature',
                                                       'B) Severe hypoglycemia as the '
                                                       'usual presenting lab pattern',
                                                       'C) Marked hyperosmolarity with '
                                                       'little or no ketoacidosis',
                                                       'D) Isolated hyponatremia '
                                                       'without hyperglycemia'],
                                           'answer': 'C) Marked hyperosmolarity with '
                                                     'little or no ketoacidosis',
                                           'explanation': 'Hyperosmolar hyperglycemic '
                                                          'state features extreme '
                                                          'hyperglycemia and '
                                                          'hyperosmolarity with '
                                                          'profound dehydration, '
                                                          'typically with absent or '
                                                          'minimal ketosis—contrasting '
                                                          "with DKA's prominent "
                                                          'ketoacidosis. Management '
                                                          'emphasizes careful fluid '
                                                          'and electrolyte correction '
                                                          'plus insulin.'},
                                          {'question': 'Sick euthyroid pattern often '
                                                       'shows?',
                                           'options': ['A) High free T4 with '
                                                       'suppressed TSH as the '
                                                       'sick-euthyroid hallmark',
                                                       'B) Very high TSH with '
                                                       'rock-bottom free T4 as the '
                                                       'typical nonthyroidal pattern',
                                                       'C) Isolated elevated '
                                                       'thyroglobulin as the defining '
                                                       'finding',
                                                       'D) Low T3 during systemic '
                                                       'illness without necessarily '
                                                       'indicating primary thyroid '
                                                       'disease'],
                                           'answer': 'D) Low T3 during systemic '
                                                     'illness without necessarily '
                                                     'indicating primary thyroid '
                                                     'disease',
                                           'explanation': 'Nonthyroidal illness (sick '
                                                          'euthyroid) commonly lowers '
                                                          'T3 via reduced peripheral '
                                                          'conversion during critical '
                                                          'illness; TSH and T4 may '
                                                          'also change, but this does '
                                                          'not automatically equal '
                                                          'primary thyroid failure. '
                                                          'Interpretation requires '
                                                          'clinical context once the '
                                                          'acute illness resolves.'},
                                          {'question': 'Pheochromocytoma classic '
                                                       'spells?',
                                           'options': ['A) Paroxysmal headache, '
                                                       'palpitations, and sweating '
                                                       'with hypertension',
                                                       'B) Painless progressive weight '
                                                       'gain with moon facies alone',
                                                       'C) Cold intolerance and '
                                                       'delayed reflexes alone',
                                                       'D) Polyuria and polydipsia '
                                                       'from osmotic diuresis alone'],
                                           'answer': 'A) Paroxysmal headache, '
                                                     'palpitations, and sweating with '
                                                     'hypertension',
                                           'explanation': 'Pheochromocytoma '
                                                          'episodically releases '
                                                          'catecholamines, producing '
                                                          'the classic spell of '
                                                          'headache, palpitations, and '
                                                          'diaphoresis with '
                                                          'hypertension. Cushingoid '
                                                          'habitus, hypothyroid '
                                                          'features, and osmotic '
                                                          'polyuria point to other '
                                                          'endocrine disorders.'}],
                                 'extreme': [{'question': 'Myxedema coma treatment '
                                                          'concept?',
                                              'options': ['A) Outpatient oral '
                                                          'levothyroxine increase '
                                                          'alone without supportive '
                                                          'care',
                                                          'B) ICU-level care with '
                                                          'thyroid hormone '
                                                          'replacement, supportive '
                                                          'measures, and steroids if '
                                                          'concurrent adrenal '
                                                          'insufficiency is possible',
                                                          'C) Urgent thyroidectomy as '
                                                          'the first step in coma',
                                                          'D) Iodine loading without '
                                                          'hormone replacement or '
                                                          'supportive care'],
                                              'answer': 'B) ICU-level care with '
                                                        'thyroid hormone replacement, '
                                                        'supportive measures, and '
                                                        'steroids if concurrent '
                                                        'adrenal insufficiency is '
                                                        'possible',
                                              'explanation': 'Myxedema coma is '
                                                             'decompensated '
                                                             'hypothyroidism with '
                                                             'hypothermia, altered '
                                                             'mentation, and organ '
                                                             'dysfunction. Management '
                                                             'is ICU supportive care '
                                                             'plus thyroid hormone; '
                                                             'empiric glucocorticoids '
                                                             'are given until adrenal '
                                                             'insufficiency is '
                                                             'excluded because '
                                                             'concurrent AI can '
                                                             'coexist (e.g., '
                                                             'hypopituitarism).'},
                                             {'question': 'Thyroid storm clinical '
                                                          'diagnosis needs?',
                                              'options': ['A) Mild TSH suppression '
                                                          'without clinical '
                                                          'thyrotoxicosis',
                                                          'B) Isolated anxiety without '
                                                          'fever, tachycardia, or '
                                                          'organ dysfunction',
                                                          'C) Severe thyrotoxicosis '
                                                          'with systemic '
                                                          'decompensation '
                                                          '(thermoregulatory, '
                                                          'cardiovascular, CNS)',
                                                          'D) Subclinical '
                                                          'hypothyroidism alone'],
                                              'answer': 'C) Severe thyrotoxicosis with '
                                                        'systemic decompensation '
                                                        '(thermoregulatory, '
                                                        'cardiovascular, CNS)',
                                              'explanation': 'Thyroid storm is a '
                                                             'clinical diagnosis of '
                                                             'life-threatening '
                                                             'thyrotoxicosis with '
                                                             'multiorgan '
                                                             'decompensation (fever, '
                                                             'tachyarrhythmia, CNS/GI '
                                                             'dysfunction). Scoring '
                                                             'systems aid recognition, '
                                                             'but treatment must not '
                                                             'await a single lab '
                                                             'threshold once the '
                                                             'syndrome is evident.'},
                                             {'question': 'Insulinoma Whipple triad?',
                                              'options': ['A) Hyperglycemia with '
                                                          'ketones as the diagnostic '
                                                          'triad',
                                                          'B) Hypertension spells with '
                                                          'catecholamine excess alone',
                                                          'C) Weight loss with free T4 '
                                                          'elevation alone',
                                                          'D) Hypoglycemic symptoms, '
                                                          'documented low glucose, and '
                                                          'relief with glucose '
                                                          'administration'],
                                              'answer': 'D) Hypoglycemic symptoms, '
                                                        'documented low glucose, and '
                                                        'relief with glucose '
                                                        'administration',
                                              'explanation': "Whipple's triad supports "
                                                             'true hypoglycemia: '
                                                             'symptoms consistent with '
                                                             'low glucose, a low '
                                                             'measured glucose, and '
                                                             'resolution when glucose '
                                                             'is raised. Insulinoma is '
                                                             'a classic endogenous '
                                                             'hyperinsulinemic cause '
                                                             'once factitious and '
                                                             'other etiologies are '
                                                             'considered.'}]},
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
                'questions': {'easy': [{'question': 'eGFR estimates?',
                                        'options': ['A) Kidney filtration function '
                                                    '(glomerular filtration rate)',
                                                    'B) Tubular concentrating ability '
                                                    'alone',
                                                    'C) Renal artery stenosis severity '
                                                    'by velocity alone',
                                                    'D) Bladder detrusor '
                                                    'contractility'],
                                        'answer': 'A) Kidney filtration function '
                                                  '(glomerular filtration rate)',
                                        'explanation': 'eGFR estimates glomerular '
                                                       'filtration rate from '
                                                       'creatinine (and sometimes '
                                                       'cystatin C) using demographic '
                                                       'variables. It reflects '
                                                       'filtration capacity, not '
                                                       'primarily concentrating '
                                                       'ability, renal-artery Doppler '
                                                       'stenosis grading, or bladder '
                                                       'function.'},
                                       {'question': 'Nephrotic syndrome features '
                                                    'heavy?',
                                        'options': ['A) Isolated microscopic hematuria '
                                                    'without protein loss',
                                                    'B) Proteinuria (typically ≥3.5 '
                                                    'g/day) with hypoalbuminemia and '
                                                    'edema',
                                                    'C) Sterile pyuria alone',
                                                    'D) Mild reduction in eGFR without '
                                                    'protein leak'],
                                        'answer': 'B) Proteinuria (typically ≥3.5 '
                                                  'g/day) with hypoalbuminemia and '
                                                  'edema',
                                        'explanation': 'Nephrotic syndrome is defined '
                                                       'by heavy proteinuria, '
                                                       'hypoalbuminemia, edema, and '
                                                       'often hyperlipidemia from '
                                                       'glomerular barrier failure. '
                                                       'Isolated hematuria or pyuria '
                                                       'without heavy protein loss '
                                                       'indicates other glomerular or '
                                                       'interstitial patterns.'},
                                       {'question': 'ACEI/ARB are preferred in?',
                                        'options': ['A) Bilateral renal artery '
                                                    'stenosis as first-line ACEI '
                                                    'indication without caution',
                                                    'B) Acute hyperkalemia with anuria '
                                                    'as the preferred start setting',
                                                    'C) Diabetic kidney disease with '
                                                    'albuminuria',
                                                    'D) Pregnancy as a routine '
                                                    'initiation setting'],
                                        'answer': 'C) Diabetic kidney disease with '
                                                  'albuminuria',
                                        'explanation': 'ACE inhibitors and ARBs reduce '
                                                       'intraglomerular pressure and '
                                                       'albuminuria and slow diabetic '
                                                       'CKD progression when monitored '
                                                       'for creatinine and potassium. '
                                                       'They are contraindicated or '
                                                       'used with extreme caution in '
                                                       'bilateral RAS, advanced '
                                                       'hyperkalemia, and pregnancy.'}],
                              'medium': [{'question': 'RBC casts suggest?',
                                          'options': ['A) Acute tubular necrosis',
                                                      'B) Postrenal obstruction alone',
                                                      'C) Simple orthostatic '
                                                      'proteinuria',
                                                      'D) Glomerulonephritis'],
                                          'answer': 'D) Glomerulonephritis',
                                          'explanation': 'RBC casts form when '
                                                         'erythrocytes leak through '
                                                         'damaged glomeruli and become '
                                                         'embedded in Tamm–Horsfall '
                                                         'protein in tubules—highly '
                                                         'suggestive of '
                                                         'glomerulonephritis. ATN '
                                                         'shows muddy-brown granular '
                                                         'casts; obstruction lacks '
                                                         'active urinary sediment of '
                                                         'that type.'},
                                         {'question': 'Post-renal AKI first check?',
                                          'options': ['A) Urinary tract obstruction '
                                                      '(bladder scan / renal '
                                                      'ultrasound)',
                                                      'B) Immediate kidney biopsy '
                                                      'before excluding obstruction',
                                                      'C) Empiric high-dose loop '
                                                      'diuretic without assessing '
                                                      'retention',
                                                      'D) Assuming prerenal azotemia '
                                                      'without imaging when retention '
                                                      'is possible'],
                                          'answer': 'A) Urinary tract obstruction '
                                                    '(bladder scan / renal ultrasound)',
                                          'explanation': 'Postrenal AKI is reversible '
                                                         'if obstruction is relieved '
                                                         'promptly. Bladder '
                                                         'catheterization/scan and '
                                                         'ultrasound look for '
                                                         'hydronephrosis or retention '
                                                         'before invasive workups. '
                                                         'Missing obstruction while '
                                                         'pursuing biopsy or diuresis '
                                                         'delays salvage of renal '
                                                         'function.'},
                                         {'question': 'Hyperkalemia with peaked T '
                                                      'waves needs?',
                                          'options': ['A) Oral sodium polystyrene as '
                                                      'the only immediate step for ECG '
                                                      'changes',
                                                      'B) Membrane stabilization with '
                                                      'intravenous calcium among other '
                                                      'stepwise measures',
                                                      'C) Hemodialysis as the sole '
                                                      'option before any temporizing '
                                                      'therapy',
                                                      'D) Fluid restriction alone '
                                                      'without cardiac protection'],
                                          'answer': 'B) Membrane stabilization with '
                                                    'intravenous calcium among other '
                                                    'stepwise measures',
                                          'explanation': 'Peaked T waves signal '
                                                         'cardiac membrane instability '
                                                         'from hyperkalemia. IV '
                                                         'calcium antagonizes cardiac '
                                                         'effects within minutes while '
                                                         'insulin/glucose, '
                                                         'beta-agonists, bicarbonate '
                                                         '(selected cases), and '
                                                         'removal therapies address '
                                                         'potassium shift and '
                                                         'elimination.'}],
                              'hard': [{'question': 'ATN muddy brown casts follow?',
                                        'options': ['A) Glomerular basement-membrane '
                                                    'rupture as the primary ATN lesion',
                                                    'B) Isolated collecting-system '
                                                    'stone without tubular necrosis',
                                                    'C) Ischemic or toxic tubular '
                                                    'injury',
                                                    'D) Minimal-change disease '
                                                    'podocytopathy'],
                                        'answer': 'C) Ischemic or toxic tubular injury',
                                        'explanation': 'Acute tubular necrosis follows '
                                                       'ischemic or nephrotoxic insult '
                                                       'to tubular epithelium; '
                                                       'muddy-brown granular casts are '
                                                       'the classic urinary finding. '
                                                       'GBM rupture suggests '
                                                       'aggressive GN; stones and '
                                                       'minimal-change disease have '
                                                       'different sediment and '
                                                       'clinical pictures.'},
                                       {'question': 'AIN often linked to?',
                                        'options': ['A) Ischemic ATN from prolonged '
                                                    'hypotension as the identical '
                                                    'mechanism',
                                                    'B) Anti-GBM disease as the usual '
                                                    'AIN cause',
                                                    'C) Simple prerenal azotemia from '
                                                    'volume depletion alone',
                                                    'D) Drug hypersensitivity (e.g., '
                                                    'antibiotics, NSAIDs, PPIs) with '
                                                    'interstitial inflammation ± WBC '
                                                    'casts/eosinophiluria'],
                                        'answer': 'D) Drug hypersensitivity (e.g., '
                                                  'antibiotics, NSAIDs, PPIs) with '
                                                  'interstitial inflammation ± WBC '
                                                  'casts/eosinophiluria',
                                        'explanation': 'Acute interstitial nephritis '
                                                       'is often a drug-induced '
                                                       'T-cell–mediated reaction '
                                                       'presenting with AKI, sterile '
                                                       'pyuria, WBC casts, and '
                                                       'sometimes '
                                                       'rash/fever/eosinophiluria. It '
                                                       'is distinct from ischemic ATN, '
                                                       'anti-GBM crescentic disease, '
                                                       'and pure prerenal physiology.'},
                                       {'question': 'Indications for urgent dialysis '
                                                    'include?',
                                        'options': ['A) Severe refractory '
                                                    'hyperkalemia, acidosis, volume '
                                                    'overload, or uremic emergencies',
                                                    'B) Mild creatinine rise without '
                                                    'complications',
                                                    'C) Asymptomatic microscopic '
                                                    'hematuria alone',
                                                    'D) Stable CKD stage 3 without '
                                                    'acute indications'],
                                        'answer': 'A) Severe refractory hyperkalemia, '
                                                  'acidosis, volume overload, or '
                                                  'uremic emergencies',
                                        'explanation': 'Urgent dialysis indications '
                                                       'are often remembered as AEIOU: '
                                                       'acidosis, electrolytes (severe '
                                                       'hyperK), intoxications, '
                                                       'overload, and uremic symptoms '
                                                       '(pericarditis, '
                                                       'encephalopathy). Mild lab '
                                                       'changes without these '
                                                       'complications do not mandate '
                                                       'emergency dialysis.'}],
                              'extreme': [{'question': 'Tumor lysis electrolyte '
                                                       'pattern?',
                                           'options': ['A) Hypokalemia, '
                                                       'hypophosphatemia, '
                                                       'hypercalcemia, and '
                                                       'hypouricemia',
                                                       'B) Hyperkalemia, '
                                                       'hyperphosphatemia, '
                                                       'hypocalcemia, and '
                                                       'hyperuricemia',
                                                       'C) Isolated hyponatremia '
                                                       'without phosphate or urate '
                                                       'change',
                                                       'D) Hypercalcemia with '
                                                       'hypophosphatemia as the TLS '
                                                       'signature'],
                                           'answer': 'B) Hyperkalemia, '
                                                     'hyperphosphatemia, hypocalcemia, '
                                                     'and hyperuricemia',
                                           'explanation': 'Tumor lysis releases '
                                                          'intracellular potassium, '
                                                          'phosphate, and nucleic '
                                                          'acids; uric acid rises and '
                                                          'phosphate binds calcium, '
                                                          'lowering serum calcium. '
                                                          'Recognizing this pattern '
                                                          'guides prevention with '
                                                          'hydration, uric-acid '
                                                          'lowering, and electrolyte '
                                                          'management.'},
                                          {'question': 'Hepatorenal syndrome concept?',
                                           'options': ['A) Intrinsic ATN as the '
                                                       'required first diagnosis in '
                                                       'all cirrhotic AKI',
                                                       'B) Postrenal obstruction as '
                                                       'the defining HRS mechanism',
                                                       'C) Functional renal failure in '
                                                       'advanced liver disease after '
                                                       'excluding shock, nephrotoxins, '
                                                       'and obstruction',
                                                       'D) Primary glomerular '
                                                       'nephrotic syndrome unrelated '
                                                       'to liver disease'],
                                           'answer': 'C) Functional renal failure in '
                                                     'advanced liver disease after '
                                                     'excluding shock, nephrotoxins, '
                                                     'and obstruction',
                                           'explanation': 'Hepatorenal syndrome is '
                                                          'functional renal '
                                                          'vasoconstriction in '
                                                          'advanced cirrhosis with '
                                                          'portal hypertension after '
                                                          'volume resuscitation and '
                                                          'exclusion of shock, '
                                                          'nephrotoxins, and '
                                                          'obstruction. Distinguishing '
                                                          'HRS from ATN guides '
                                                          'vasoconstrictor and '
                                                          'transplant-oriented '
                                                          'therapy.'},
                                          {'question': 'Contrast nephropathy '
                                                       'prevention theme?',
                                           'options': ['A) Mandate high-osmolar '
                                                       'contrast in all CKD patients',
                                                       'B) Routine NSAID loading '
                                                       'before contrast exposure',
                                                       'C) Withhold all IV fluids in '
                                                       'dehydrated high-risk patients',
                                                       'D) Optimize volume status and '
                                                       'avoid unnecessary contrast in '
                                                       'high-risk patients'],
                                           'answer': 'D) Optimize volume status and '
                                                     'avoid unnecessary contrast in '
                                                     'high-risk patients',
                                           'explanation': 'Contrast-associated AKI '
                                                          'risk rises with CKD, '
                                                          'diabetes, and hypovolemia. '
                                                          'Prevention emphasizes '
                                                          'assessing necessity, using '
                                                          'the lowest adequate '
                                                          'contrast dose, and '
                                                          'optimizing hydration—not '
                                                          'dehydrating patients or '
                                                          'adding nephrotoxins.'}]},
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
                 'questions': {'easy': [{'question': 'Ottawa ankle rules help decide '
                                                     'need for?',
                                         'options': ['A) Radiographs after ankle '
                                                     'sprain when rules are positive',
                                                     'B) Immediate MRI for every ankle '
                                                     'sprain',
                                                     'C) Bone scan as first-line acute '
                                                     'imaging',
                                                     'D) No imaging pathway regardless '
                                                     'of inability to bear weight'],
                                         'answer': 'A) Radiographs after ankle sprain '
                                                   'when rules are positive',
                                         'explanation': 'Ottawa ankle rules use '
                                                        'tenderness and weight-bearing '
                                                        'ability to decide when '
                                                        'ankle/foot X-rays are needed '
                                                        'after sprain, reducing '
                                                        'unnecessary films while '
                                                        'catching clinically important '
                                                        'fractures.'},
                                        {'question': 'Colles fracture typically '
                                                     'follows?',
                                         'options': ['A) Direct blow causing isolated '
                                                     'scaphoid waist fracture only',
                                                     'B) FOOSH injury with distal '
                                                     'radius fracture and dorsal '
                                                     'angulation',
                                                     'C) Fall on a flexed wrist with '
                                                     'volar angulation (Smith pattern) '
                                                     'as the same lesion',
                                                     'D) Twisting injury producing '
                                                     'isolated medial malleolus '
                                                     'fracture'],
                                         'answer': 'B) FOOSH injury with distal radius '
                                                   'fracture and dorsal angulation',
                                         'explanation': 'A Colles fracture is a distal '
                                                        'radius fracture from fall on '
                                                        'an outstretched hand, '
                                                        'classically with dorsal '
                                                        'displacement/angulation of '
                                                        'the distal fragment. Smith '
                                                        'fractures angulate volarly; '
                                                        'scaphoid and ankle fractures '
                                                        'are different injuries.'},
                                        {'question': 'Open fracture needs?',
                                         'options': ['A) Delayed antibiotics until '
                                                     'after multiple days of '
                                                     'observation',
                                                     'B) Closed casting alone without '
                                                     'antibiotic coverage',
                                                     'C) Early antibiotics plus urgent '
                                                     'orthopedic management',
                                                     'D) Outpatient follow-up without '
                                                     'wound and fracture care'],
                                         'answer': 'C) Early antibiotics plus urgent '
                                                   'orthopedic management',
                                         'explanation': 'Open fractures communicate '
                                                        'with the environment and risk '
                                                        'deep infection and '
                                                        'osteomyelitis. Early IV '
                                                        'antibiotics, tetanus status, '
                                                        'and urgent surgical '
                                                        'debridement/fixation pathways '
                                                        'reduce infection and improve '
                                                        'outcomes.'}],
                               'medium': [{'question': 'Compartment syndrome key early '
                                                       'feature?',
                                           'options': ['A) Absent distal pulses as the '
                                                       'earliest and most sensitive '
                                                       'finding',
                                                       'B) Painless swelling without '
                                                       'tenderness',
                                                       'C) Isolated fever without limb '
                                                       'findings',
                                                       'D) Pain out of proportion and '
                                                       'pain on passive stretch'],
                                           'answer': 'D) Pain out of proportion and '
                                                     'pain on passive stretch',
                                           'explanation': 'Compartment syndrome '
                                                          'elevates intracompartmental '
                                                          'pressure, ischemicizing '
                                                          'muscle and nerve. Early '
                                                          'clues are severe pain out '
                                                          'of proportion and pain on '
                                                          'passive stretch; '
                                                          'pulselessness is a late '
                                                          'finding. Urgent fasciotomy '
                                                          'is required once '
                                                          'diagnosed.'},
                                          {'question': 'Fat embolism classic setting?',
                                           'options': ['A) After long-bone (or pelvic) '
                                                       'fracture',
                                                       'B) After uncomplicated distal '
                                                       'phalanx tuft fracture alone',
                                                       'C) After simple ankle sprain '
                                                       'without fracture',
                                                       'D) After elective soft-tissue '
                                                       'laceration repair alone'],
                                           'answer': 'A) After long-bone (or pelvic) '
                                                     'fracture',
                                           'explanation': 'Fat emboli classically '
                                                          'follow femoral or other '
                                                          'long-bone fractures (and '
                                                          'some orthopedic '
                                                          'procedures), presenting '
                                                          '24–72 hours later with '
                                                          'respiratory and neurologic '
                                                          'features ± petechiae.'},
                                          {'question': 'Septic arthritis urgency?',
                                           'options': ['A) Empiric oral antibiotics '
                                                       'for weeks without aspiration',
                                                       'B) Urgent joint aspiration for '
                                                       'culture then prompt '
                                                       'antibiotics',
                                                       'C) Watchful waiting until '
                                                       'cartilage is destroyed',
                                                       'D) Steroid injection before '
                                                       'excluding infection'],
                                           'answer': 'B) Urgent joint aspiration for '
                                                     'culture then prompt antibiotics',
                                           'explanation': 'Septic arthritis rapidly '
                                                          'destroys cartilage. Urgent '
                                                          'aspiration for Gram '
                                                          'stain/culture should '
                                                          'precede antibiotics when '
                                                          'feasible, then prompt IV '
                                                          'antibiotics and often '
                                                          'surgical drainage—steroids '
                                                          'and delay worsen joint '
                                                          'outcomes.'}],
                               'hard': [{'question': 'Salter-Harris injuries involve?',
                                         'options': ['A) Only the adult articular '
                                                     'cartilage surface without physis',
                                                     'B) Isolated muscle belly strain',
                                                     'C) The physis (growth plate)',
                                                     'D) Pure ligament sprain without '
                                                     'bony growth-plate involvement'],
                                         'answer': 'C) The physis (growth plate)',
                                         'explanation': 'Salter–Harris classification '
                                                        'describes fractures involving '
                                                        'the pediatric physis. Injury '
                                                        'pattern determines growth '
                                                        'disturbance risk and '
                                                        'management. Adult articular '
                                                        'injuries and soft-tissue '
                                                        'sprains are classified '
                                                        'differently.'},
                                        {'question': 'Cauda equina red flags include?',
                                         'options': ['A) Isolated mechanical low-back '
                                                     'pain without neurologic change',
                                                     'B) Unilateral ankle jerk '
                                                     'asymmetry alone without '
                                                     'sphincter signs',
                                                     'C) Chronic intermittent sciatica '
                                                     'without red flags',
                                                     'D) Saddle anesthesia with bowel '
                                                     'or bladder dysfunction'],
                                         'answer': 'D) Saddle anesthesia with bowel or '
                                                   'bladder dysfunction',
                                         'explanation': 'Cauda equina compression '
                                                        'produces saddle anesthesia, '
                                                        'sphincter dysfunction, and '
                                                        'often bilateral leg symptoms. '
                                                        'These red flags demand urgent '
                                                        'MRI and decompression to '
                                                        'preserve continence and '
                                                        'sexual function.'},
                                        {'question': 'Pathologic fracture suggests?',
                                         'options': ['A) Underlying bone weakness from '
                                                     'tumor, osteoporosis, or '
                                                     'metabolic bone disease',
                                                     'B) Normal bone subjected only to '
                                                     'high-energy trauma as the '
                                                     'definition',
                                                     'C) Isolated soft-tissue '
                                                     'contusion without fracture',
                                                     'D) Greenstick injury in a '
                                                     'healthy child as the pathologic '
                                                     'definition'],
                                         'answer': 'A) Underlying bone weakness from '
                                                   'tumor, osteoporosis, or metabolic '
                                                   'bone disease',
                                         'explanation': 'A pathologic fracture occurs '
                                                        'through bone weakened by '
                                                        'tumor, osteoporosis, '
                                                        'infection, or metabolic '
                                                        'disease, often after minimal '
                                                        'trauma. Recognizing it '
                                                        'prompts evaluation for the '
                                                        'underlying bone pathology.'}],
                               'extreme': [{'question': 'Necrotizing fasciitis clue?',
                                            'options': ['A) Mild localized cellulitis '
                                                        'improving on oral antibiotics',
                                                        'B) Pain out of proportion, '
                                                        'rapid spread, and systemic '
                                                        'toxicity',
                                                        'C) Chronic venous stasis '
                                                        'dermatitis without toxicity',
                                                        'D) Uncomplicated superficial '
                                                        'abrasion'],
                                            'answer': 'B) Pain out of proportion, '
                                                      'rapid spread, and systemic '
                                                      'toxicity',
                                            'explanation': 'Necrotizing fasciitis '
                                                           'features severe pain out '
                                                           'of proportion, rapid '
                                                           'progression, and systemic '
                                                           'toxicity, sometimes with '
                                                           'crepitus. It is a surgical '
                                                           'emergency requiring '
                                                           'immediate debridement—not '
                                                           'observation as simple '
                                                           'cellulitis.'},
                                           {'question': 'Pelvic binder indication '
                                                        'theme?',
                                            'options': ['A) Stable isolated pubic '
                                                        'ramus fracture without '
                                                        'hemodynamic concern',
                                                        'B) Acetabular fracture '
                                                        'already fully fixed in the OR',
                                                        'C) Unstable pelvic fracture '
                                                        'with concern for '
                                                        'life-threatening hemorrhage',
                                                        'D) Chronic pelvic deformity '
                                                        'without acute bleeding'],
                                            'answer': 'C) Unstable pelvic fracture '
                                                      'with concern for '
                                                      'life-threatening hemorrhage',
                                            'explanation': 'A pelvic binder '
                                                           'temporarily reduces pelvic '
                                                           'volume and can tamponade '
                                                           'venous/cancellous bleeding '
                                                           'in unstable pelvic ring '
                                                           'injuries during '
                                                           'resuscitation. It is not '
                                                           'needed for every minor '
                                                           'stable pelvic fracture.'},
                                           {'question': 'Rhabdomyolysis AKI risk from?',
                                            'options': ['A) Isolated hypercalcemia '
                                                        'without muscle necrosis',
                                                        'B) Simple dehydration without '
                                                        'rhabdomyolysis',
                                                        'C) Postrenal obstruction from '
                                                        'prostate enlargement alone',
                                                        'D) Myoglobinuria after crush '
                                                        'injury or extreme exertion'],
                                            'answer': 'D) Myoglobinuria after crush '
                                                      'injury or extreme exertion',
                                            'explanation': 'Rhabdomyolysis releases '
                                                           'myoglobin and potassium '
                                                           'from necrotic muscle; '
                                                           'myoglobin is nephrotoxic '
                                                           'and can cause AKI after '
                                                           'crush, immobilization, or '
                                                           'extreme exertion. '
                                                           'Aggressive IV fluids are '
                                                           'the mainstay of kidney '
                                                           'protection.'}]},
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
                 'questions': {'easy': [{'question': 'Honey-colored crusts suggest?',
                                         'options': ['A) Impetigo',
                                                     'B) Pemphigus vulgaris',
                                                     'C) Bullous pemphigoid',
                                                     'D) Discoid lupus erythematosus'],
                                         'answer': 'A) Impetigo',
                                         'explanation': 'Honey-colored crusts on '
                                                        'erosions, especially on the '
                                                        'face of children, are classic '
                                                        'for nonbullous impetigo from '
                                                        'Staphylococcus aureus or '
                                                        'Streptococcus pyogenes. '
                                                        'Autoimmune blistering '
                                                        'diseases and discoid lupus '
                                                        'have different morphologies '
                                                        'and demographics.'},
                                        {'question': 'ABCDE screens for?',
                                         'options': ['A) Seborrheic keratosis alone',
                                                     'B) Melanoma',
                                                     'C) Dermatofibroma alone',
                                                     'D) Lipoma alone'],
                                         'answer': 'B) Melanoma',
                                         'explanation': 'ABCDE (Asymmetry, Border '
                                                        'irregularity, Color '
                                                        'variegation, Diameter, '
                                                        'Evolution) screens pigmented '
                                                        'lesions for melanoma risk and '
                                                        'guides biopsy decisions. '
                                                        'Seborrheic keratoses, '
                                                        'dermatofibromas, and lipomas '
                                                        'have different clinical '
                                                        'signatures.'},
                                        {'question': 'Auspitz sign relates to?',
                                         'options': ['A) Atopic dermatitis',
                                                     'B) Lichen planus',
                                                     'C) Psoriasis',
                                                     'D) Nummular eczema without '
                                                     'Auspitz bleeding'],
                                         'answer': 'C) Psoriasis',
                                         'explanation': 'Auspitz sign is pinpoint '
                                                        'bleeding when psoriatic scale '
                                                        'is removed, reflecting '
                                                        'dilated dermal papillae under '
                                                        'thinned epidermis. Atopic '
                                                        'dermatitis, lichen planus, '
                                                        'and nummular eczema are '
                                                        'diagnosed by other '
                                                        'morphologic clues.'}],
                               'medium': [{'question': 'Scabies itch is worse?',
                                           'options': ['A) Facial pruritus triggered '
                                                       'by ultraviolet exposure '
                                                       '(polymorphous light eruption '
                                                       'pattern)',
                                                       'B) Cold-induced wheals of cold '
                                                       'urticaria on the trunk',
                                                       'C) Painless hypopigmented '
                                                       'macules of pityriasis '
                                                       'versicolor',
                                                       'D) At night, especially in '
                                                       'finger web spaces and other '
                                                       'burrow sites'],
                                           'answer': 'D) At night, especially in '
                                                     'finger web spaces and other '
                                                     'burrow sites',
                                           'explanation': 'Sarcoptes scabiei burrows '
                                                          'in stratum corneum; intense '
                                                          'nocturnal pruritus in webs, '
                                                          'wrists, and genitals is '
                                                          'characteristic. '
                                                          'Sun-triggered facial itch '
                                                          'and cold urticaria suggest '
                                                          'other diagnoses; '
                                                          'hypopigmented patches '
                                                          'suggest pityriasis '
                                                          'versicolor or vitiligo.'},
                                          {'question': 'Cellulitis features?',
                                           'options': ['A) Spreading erythema, warmth, '
                                                       'and tenderness of the skin and '
                                                       'soft tissue',
                                                       'B) Well-demarcated silvery '
                                                       'plaques on extensor surfaces',
                                                       'C) Annular plaque from '
                                                       'granuloma annulare without '
                                                       'cellulitis signs',
                                                       'D) Noninflammatory '
                                                       'subcutaneous lipoma'],
                                           'answer': 'A) Spreading erythema, warmth, '
                                                     'and tenderness of the skin and '
                                                     'soft tissue',
                                           'explanation': 'Cellulitis is bacterial '
                                                          'infection of dermis and '
                                                          'subcutaneous tissue '
                                                          'producing expanding '
                                                          'erythema, warmth, swelling, '
                                                          'and tenderness. Psoriasis '
                                                          'plaques, granuloma '
                                                          'annulare, and lipomas are '
                                                          'morphologically distinct.'},
                                          {'question': 'SJS/TEN are?',
                                           'options': ['A) Mild irritant contact '
                                                       'dermatitis only',
                                                       'B) Severe cutaneous adverse '
                                                       'drug reactions with epidermal '
                                                       'necrosis',
                                                       'C) Simple morbilliform drug '
                                                       'rash without necrosis',
                                                       'D) Chronic plaque psoriasis '
                                                       'exacerbation alone'],
                                           'answer': 'B) Severe cutaneous adverse drug '
                                                     'reactions with epidermal '
                                                     'necrosis',
                                           'explanation': 'Stevens–Johnson syndrome '
                                                          'and toxic epidermal '
                                                          'necrolysis are severe '
                                                          'drug-induced reactions with '
                                                          'widespread epidermal '
                                                          'necrosis and mucosal '
                                                          'involvement, carrying high '
                                                          'morbidity. Mild drug '
                                                          'exanthems and psoriasis '
                                                          'lack this necrolytic '
                                                          'mucocutaneous pattern.'}],
                               'hard': [{'question': 'Nikolsky sign can be positive '
                                                     'in?',
                                         'options': ['A) Uncomplicated urticaria '
                                                     'without epidermal detachment',
                                                     'B) Acne vulgaris',
                                                     'C) SJS/TEN and certain other '
                                                     'blistering diseases (e.g., '
                                                     'pemphigus)',
                                                     'D) Vitiligo'],
                                         'answer': 'C) SJS/TEN and certain other '
                                                   'blistering diseases (e.g., '
                                                   'pemphigus)',
                                         'explanation': 'Nikolsky sign—lateral '
                                                        'pressure causing sheet-like '
                                                        'epidermal separation—is '
                                                        'positive in TEN/SJS and in '
                                                        'pemphigus, reflecting loss of '
                                                        'keratinocyte adhesion. '
                                                        'Urticaria, acne, and vitiligo '
                                                        'do not show true Nikolsky '
                                                        'positivity.'},
                                        {'question': 'Erythema migrans suggests?',
                                         'options': ['A) Secondary syphilis as the '
                                                     'identical lesion name',
                                                     'B) Fixed drug eruption as the '
                                                     'usual EM cause',
                                                     'C) Erythema multiforme target '
                                                     'lesions as the same entity',
                                                     'D) Early Lyme disease (erythema '
                                                     'migrans)'],
                                         'answer': 'D) Early Lyme disease (erythema '
                                                   'migrans)',
                                         'explanation': 'Erythema migrans is the '
                                                        'expanding annular rash of '
                                                        'early Lyme borreliosis after '
                                                        'Ixodes tick bite. Erythema '
                                                        'multiforme shows targetoid '
                                                        'lesions often post-herpes; '
                                                        'syphilis and fixed drug '
                                                        'eruptions are different '
                                                        'morphologies and etiologies.'},
                                        {'question': 'Necrotizing infection vs simple '
                                                     'cellulitis clue?',
                                         'options': ['A) Extreme pain, crepitus, and '
                                                     'rapid clinical deterioration',
                                                     'B) Mild warmth responding '
                                                     'quickly to oral antibiotics',
                                                     'C) Chronic bilateral venous '
                                                     'stasis changes only',
                                                     'D) Localized folliculitis '
                                                     'without systemic signs'],
                                         'answer': 'A) Extreme pain, crepitus, and '
                                                   'rapid clinical deterioration',
                                         'explanation': 'Necrotizing soft-tissue '
                                                        'infection differs from simple '
                                                        'cellulitis by pain out of '
                                                        'proportion, rapid spread, '
                                                        'crepitus/gas, and early '
                                                        'sepsis. Suspicion mandates '
                                                        'urgent surgical exploration '
                                                        'rather than observation on '
                                                        'oral antibiotics alone.'}],
                               'extreme': [{'question': 'Purpura fulminans '
                                                        'association?',
                                            'options': ['A) Uncomplicated atopic '
                                                        'eczema flare',
                                                        'B) Severe sepsis, especially '
                                                        'meningococcemia',
                                                        'C) Mild viral exanthem '
                                                        'without shock',
                                                        'D) Localized contact '
                                                        'dermatitis'],
                                            'answer': 'B) Severe sepsis, especially '
                                                      'meningococcemia',
                                            'explanation': 'Purpura fulminans is acute '
                                                           'purpuric skin necrosis '
                                                           'from disseminated '
                                                           'intravascular coagulation '
                                                           'and dermal vascular '
                                                           'thrombosis, classically '
                                                           'with meningococcal sepsis. '
                                                           'It is a medical emergency '
                                                           'distinct from benign '
                                                           'eczematous or contact '
                                                           'eruptions.'},
                                           {'question': 'Calciphylaxis occurs mainly '
                                                        'in?',
                                            'options': ['A) Healthy adolescents '
                                                        'without metabolic disease',
                                                        'B) Patients with isolated '
                                                        'mild fatty liver alone',
                                                        'C) Patients with advanced '
                                                        'kidney disease (often '
                                                        'dialysis-dependent)',
                                                        'D) Children with '
                                                        'uncomplicated atopic '
                                                        'dermatitis'],
                                            'answer': 'C) Patients with advanced '
                                                      'kidney disease (often '
                                                      'dialysis-dependent)',
                                            'explanation': 'Calciphylaxis (calcific '
                                                           'uremic arteriolopathy) '
                                                           'causes painful ischemic '
                                                           'skin necrosis mainly in '
                                                           'end-stage kidney disease '
                                                           'with disordered '
                                                           'calcium–phosphate '
                                                           'metabolism. It is rare '
                                                           'outside advanced '
                                                           'CKD/dialysis contexts.'},
                                           {'question': 'Toxic shock associations '
                                                        'include?',
                                            'options': ['A) Primary herpes simplex '
                                                        'gingivostomatitis alone',
                                                        'B) Uncomplicated dermatophyte '
                                                        'infection',
                                                        'C) Drug-induced '
                                                        'photosensitivity alone',
                                                        'D) Staphylococcal or '
                                                        'streptococcal '
                                                        'exotoxin–mediated disease'],
                                            'answer': 'D) Staphylococcal or '
                                                      'streptococcal exotoxin–mediated '
                                                      'disease',
                                            'explanation': 'Toxic shock syndromes are '
                                                           'mediated by superantigen '
                                                           'toxins from S. aureus or '
                                                           'S. pyogenes, causing '
                                                           'fever, shock, multiorgan '
                                                           'failure, and diffuse '
                                                           'erythema. Antiviral, '
                                                           'antifungal, and '
                                                           'photosensitivity disorders '
                                                           'are different '
                                                           'mechanisms.'}]},
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
           'questions': {'easy': [{'question': 'Most common PPH cause?',
                                   'options': ['A) Uterine atony',
                                               'B) Retained products of conception as '
                                               'more common than atony',
                                               'C) Uterine inversion as the most '
                                               'frequent cause',
                                               'D) Coagulopathy as the single most '
                                               'common primary cause'],
                                   'answer': 'A) Uterine atony',
                                   'explanation': 'Uterine atony—failure of myometrial '
                                                  'contraction after delivery—is the '
                                                  'most common cause of postpartum '
                                                  'hemorrhage. Retained tissue, '
                                                  'trauma, inversion, and coagulopathy '
                                                  'are important but less frequent '
                                                  "primary causes; the '4 Ts' "
                                                  'framework still starts with tone.'},
                                  {'question': 'Ectopic risk rises with?',
                                   'options': ['A) Prior uncomplicated term vaginal '
                                               'birth alone',
                                               'B) Prior PID or other tubal damage',
                                               'C) Folic acid supplementation',
                                               'D) Blood group O as an independent '
                                               'major risk'],
                                   'answer': 'B) Prior PID or other tubal damage',
                                   'explanation': 'Ectopic pregnancy risk rises when '
                                                  'tubal architecture is damaged—prior '
                                                  'PID, tubal surgery, or prior '
                                                  'ectopic—impairing blastocyst '
                                                  'transport. Uncomplicated prior '
                                                  'birth, folate, and blood group are '
                                                  'not major ectopic risk drivers.'},
                                  {'question': 'Fetal heart by Doppler often from?',
                                   'options': ['A) At 4 weeks by Doppler in all '
                                               'pregnancies',
                                               'B) Only after 28 weeks',
                                               "C) Approximately 10–12 weeks' "
                                               'gestation',
                                               'D) Never before quickening at 20 '
                                               'weeks'],
                                   'answer': "C) Approximately 10–12 weeks' gestation",
                                   'explanation': 'Handheld Doppler commonly detects '
                                                  'fetal heart tones around 10–12 '
                                                  'weeks, depending on habitus and '
                                                  'equipment. Earlier detection '
                                                  'usually requires transvaginal '
                                                  'ultrasound; waiting until the third '
                                                  'trimester is unnecessary for '
                                                  'routine dating/viability checks.'}],
                         'medium': [{'question': 'Pre-eclampsia is HTN after 20 weeks '
                                                 'plus?',
                                     'options': ['A) Isolated edema without '
                                                 'hypertension',
                                                 'B) Gestational diabetes alone',
                                                 'C) Physiologic first-trimester '
                                                 'nausea alone',
                                                 'D) Proteinuria or end-organ '
                                                 'dysfunction features'],
                                     'answer': 'D) Proteinuria or end-organ '
                                               'dysfunction features',
                                     'explanation': 'Pre-eclampsia is new hypertension '
                                                    'after 20 weeks plus proteinuria '
                                                    'or maternal organ dysfunction '
                                                    '(renal, hepatic, neurologic, '
                                                    'hematologic) or uteroplacental '
                                                    'dysfunction. Edema alone is '
                                                    'nonspecific; GDM and early nausea '
                                                    'are separate conditions.'},
                                    {'question': 'Ectopic classic combo?',
                                     'options': ['A) Positive pregnancy test, empty '
                                                 'uterus on ultrasound, and pain or '
                                                 'bleeding',
                                                 'B) Negative hCG with intrauterine '
                                                 'pregnancy on scan',
                                                 'C) Intrauterine gestational sac with '
                                                 'fetal pole and no pain',
                                                 'D) Missed menses with closed cervix '
                                                 'and no ultrasound findings needed'],
                                     'answer': 'A) Positive pregnancy test, empty '
                                               'uterus on ultrasound, and pain or '
                                               'bleeding',
                                     'explanation': 'Ectopic pregnancy classically '
                                                    'combines a positive hCG, an empty '
                                                    'uterine cavity, and unilateral '
                                                    'pain or bleeding. An intrauterine '
                                                    'gestation makes ectopic unlikely '
                                                    '(except rare heterotopic '
                                                    'pregnancy). Early diagnosis '
                                                    'prevents rupture.'},
                                    {'question': 'Shoulder dystocia is?',
                                     'options': ['A) A normal second-stage variant '
                                                 'needing no maneuvers',
                                                 'B) An obstetric emergency when the '
                                                 'shoulders fail to deliver after the '
                                                 'head',
                                                 'C) Failure of placental separation '
                                                 'after 30 minutes as the same entity',
                                                 'D) Cord prolapse after membrane '
                                                 'rupture as the identical diagnosis'],
                                     'answer': 'B) An obstetric emergency when the '
                                               'shoulders fail to deliver after the '
                                               'head',
                                     'explanation': 'Shoulder dystocia is impaction of '
                                                    'the fetal shoulders after '
                                                    'delivery of the head, risking '
                                                    'hypoxia and brachial plexus '
                                                    'injury. It requires immediate '
                                                    'help and maneuvers (McRoberts, '
                                                    'suprapubic pressure)—not '
                                                    'expectant delay.'}],
                         'hard': [{'question': 'Magnesium sulfate in obstetrics is '
                                               'used for?',
                                   'options': ['A) First-line tocolysis for all '
                                               'preterm labor',
                                               'B) Routine induction agent at term for '
                                               'all women',
                                               'C) Seizure prophylaxis and treatment '
                                               'in pre-eclampsia/eclampsia',
                                               'D) Antibiotic prophylaxis for group B '
                                               'streptococcus'],
                                   'answer': 'C) Seizure prophylaxis and treatment in '
                                             'pre-eclampsia/eclampsia',
                                   'explanation': 'Magnesium sulfate is used to '
                                                  'prevent and treat eclamptic '
                                                  'seizures in pre-eclampsia with '
                                                  'severe features and eclampsia; it '
                                                  'also offers fetal neuroprotection '
                                                  'in selected preterm births. It is '
                                                  'not a routine induction agent or '
                                                  'GBS antibiotic.'},
                                  {'question': 'Placenta previa bleeding is typically?',
                                   'options': ['A) Painful bleeding with a hypertonic '
                                               'tender uterus (abruption pattern)',
                                               'B) Passage of tissue with cramping at '
                                               '8 weeks as the defining previa feature',
                                               'C) Amenorrhea without bleeding',
                                               'D) Painless vaginal bleeding'],
                                   'answer': 'D) Painless vaginal bleeding',
                                   'explanation': 'Placenta previa overlies the '
                                                  'cervical os; bleeding is typically '
                                                  'painless as the placenta shears '
                                                  'with lower-segment change. Painful '
                                                  'bleeding with uterine hypertonus '
                                                  'suggests abruption instead.'},
                                  {'question': 'HELLP relates to?',
                                   'options': ['A) Hemolysis, elevated liver enzymes, '
                                               'and low platelets',
                                               'B) Hyperemesis with normal liver '
                                               'enzymes and platelets',
                                               'C) Isolated gestational '
                                               'thrombocytopenia without hemolysis or '
                                               'liver injury',
                                               'D) Cholestasis of pregnancy with '
                                               'pruritus and bile acids alone'],
                                   'answer': 'A) Hemolysis, elevated liver enzymes, '
                                             'and low platelets',
                                   'explanation': 'HELLP syndrome (Hemolysis, Elevated '
                                                  'Liver enzymes, Low Platelets) is a '
                                                  'severe pre-eclampsia spectrum '
                                                  'disorder requiring urgent obstetric '
                                                  'management. Hyperemesis, isolated '
                                                  'gestational thrombocytopenia, and '
                                                  'cholestasis are distinct '
                                                  'entities.'}],
                         'extreme': [{'question': 'Amniotic fluid embolism theme?',
                                      'options': ['A) Gradual postpartum blues over '
                                                  'days without shock',
                                                  'B) Sudden cardiorespiratory '
                                                  'collapse and coagulopathy in labor '
                                                  'or immediate postpartum',
                                                  'C) Isolated retained placenta '
                                                  'without hemodynamic change',
                                                  'D) Mild transient hypotension after '
                                                  'epidural without hypoxia or DIC'],
                                      'answer': 'B) Sudden cardiorespiratory collapse '
                                                'and coagulopathy in labor or '
                                                'immediate postpartum',
                                      'explanation': 'Amniotic fluid embolism presents '
                                                     'with abrupt hypoxia, '
                                                     'hypotension/cardiovascular '
                                                     'collapse, and often disseminated '
                                                     'intravascular coagulation during '
                                                     'labor or immediately postpartum. '
                                                     'It is a clinical diagnosis '
                                                     'requiring immediate '
                                                     'resuscitation.'},
                                     {'question': 'Acute fatty liver of pregnancy '
                                                  'overlaps with?',
                                      'options': ['A) First-trimester hyperemesis '
                                                  'without liver synthetic failure',
                                                  'B) Uncomplicated gestational '
                                                  'thrombocytopenia alone',
                                                  'C) A late-pregnancy acute '
                                                  'liver-failure phenotype',
                                                  'D) Intrahepatic cholestasis with '
                                                  'pruritus but preserved synthetic '
                                                  'function as identical AFLP'],
                                      'answer': 'C) A late-pregnancy acute '
                                                'liver-failure phenotype',
                                      'explanation': 'Acute fatty liver of pregnancy '
                                                     'is a third-trimester '
                                                     'mitochondrial hepatopathy '
                                                     'presenting with liver failure, '
                                                     'coagulopathy, hypoglycemia, and '
                                                     'encephalopathy that overlaps '
                                                     'clinically with HELLP/severe '
                                                     'pre-eclampsia and requires '
                                                     'urgent delivery and supportive '
                                                     'care.'},
                                     {'question': 'Uterine rupture risk rises with?',
                                      'options': ['A) Primiparous spontaneous labor '
                                                  'with no uterine surgery',
                                                  'B) Elective repeat cesarean before '
                                                  'labor as the highest rupture '
                                                  'setting',
                                                  'C) Uncomplicated vacuum extraction '
                                                  'without scar as the main risk',
                                                  'D) Prior cesarean scar undergoing '
                                                  'labor'],
                                      'answer': 'D) Prior cesarean scar undergoing '
                                                'labor',
                                      'explanation': 'Uterine rupture risk is highest '
                                                     'with labor in a scarred uterus '
                                                     '(prior cesarean), especially '
                                                     'with induction or dysfunctional '
                                                     'labor. Unscarred primiparous '
                                                     'labor has much lower risk; '
                                                     'rupture presents with fetal '
                                                     'distress, loss of station, and '
                                                     'maternal shock.'}]},
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
                'questions': {'easy': [{'question': 'ORS is first-line for?',
                                        'options': ['A) Most dehydrating diarrheal '
                                                    'illnesses when the child can '
                                                    'still drink',
                                                    'B) All children with severe shock '
                                                    'as the only initial fluid '
                                                    'strategy',
                                                    'C) Isolated constipation without '
                                                    'fluid loss',
                                                    'D) Surgical abdomen with '
                                                    'peritonitis as preferred sole '
                                                    'therapy'],
                                        'answer': 'A) Most dehydrating diarrheal '
                                                  'illnesses when the child can still '
                                                  'drink',
                                        'explanation': 'Oral rehydration solution '
                                                       'replaces water and '
                                                       'electrolytes using '
                                                       'glucose–sodium cotransport and '
                                                       'is first-line for most '
                                                       'children with dehydrating '
                                                       'diarrhea who can drink. IV '
                                                       'fluids are needed for severe '
                                                       'shock or inability to tolerate '
                                                       'oral intake.'},
                                       {'question': 'MMR vaccine type?',
                                        'options': ['A) Inactivated whole-virus only',
                                                    'B) Live attenuated',
                                                    'C) Toxoid vaccine',
                                                    'D) Pure polysaccharide conjugate '
                                                    'identical to tetanus toxoid'],
                                        'answer': 'B) Live attenuated',
                                        'explanation': 'MMR is a live attenuated '
                                                       'vaccine and is generally '
                                                       'contraindicated in significant '
                                                       'immunocompromise and '
                                                       'pregnancy. Inactivated, '
                                                       'toxoid, and polysaccharide '
                                                       'vaccines are different '
                                                       'platforms used for other '
                                                       'pathogens.'},
                                       {'question': 'APGAR is done at?',
                                        'options': ['A) Only at 30 minutes after birth',
                                                    'B) Only at hospital discharge',
                                                    'C) 1 and 5 minutes of life '
                                                    '(commonly), with further scores '
                                                    'if needed',
                                                    'D) Once at conception dating '
                                                    'ultrasound'],
                                        'answer': 'C) 1 and 5 minutes of life '
                                                  '(commonly), with further scores if '
                                                  'needed',
                                        'explanation': 'The Apgar score assesses '
                                                       'appearance, pulse, grimace, '
                                                       'activity, and respiration at 1 '
                                                       'and 5 minutes to summarize '
                                                       'early transition; further '
                                                       'scores are recorded if the '
                                                       '5-minute score remains low. It '
                                                       'is not a discharge readiness '
                                                       'tool.'}],
                              'medium': [{'question': 'Kawasaki complication?',
                                          'options': ['A) Isolated mitral stenosis as '
                                                      'the classic sequela',
                                                      'B) Chronic interstitial lung '
                                                      'fibrosis as the main '
                                                      'complication',
                                                      'C) Avascular necrosis of the '
                                                      'femoral head as the defining '
                                                      'feature',
                                                      'D) Coronary artery aneurysms'],
                                          'answer': 'D) Coronary artery aneurysms',
                                          'explanation': 'Kawasaki disease is a '
                                                         'medium-vessel vasculitis of '
                                                         'childhood; coronary artery '
                                                         'aneurysms are the major '
                                                         'complication prevented by '
                                                         'timely IVIG. Cardiac '
                                                         'involvement—not mitral '
                                                         'stenosis, pulmonary '
                                                         'fibrosis, or femoral '
                                                         'AVN—drives follow-up '
                                                         'echocardiography.'},
                                         {'question': 'Fever in a neonate is?',
                                          'options': ['A) A serious infection until '
                                                      'proven otherwise',
                                                      'B) Always a benign viral '
                                                      'illness needing no evaluation',
                                                      'C) Routine teething without '
                                                      'workup in all neonates',
                                                      'D) Ignored if the infant still '
                                                      'feeds occasionally'],
                                          'answer': 'A) A serious infection until '
                                                    'proven otherwise',
                                          'explanation': 'Neonates have immature '
                                                         'immunity and can deteriorate '
                                                         'rapidly from bacterial '
                                                         'sepsis/meningitis. Fever in '
                                                         'this age group mandates '
                                                         'urgent full evaluation and '
                                                         'empiric therapy pathways—not '
                                                         'attribution to teething.'},
                                         {'question': 'Croup hallmark?',
                                          'options': ['A) Expiratory wheeze as the '
                                                      'sole hallmark without '
                                                      'upper-airway signs',
                                                      'B) Barking cough and '
                                                      'inspiratory stridor',
                                                      'C) Drooling and tripoding as '
                                                      'the typical croup posture',
                                                      'D) Productive lobar '
                                                      'consolidation as the defining '
                                                      'feature'],
                                          'answer': 'B) Barking cough and inspiratory '
                                                    'stridor',
                                          'explanation': 'Viral croup '
                                                         '(laryngotracheobronchitis) '
                                                         'produces subglottic edema '
                                                         'with a barking cough and '
                                                         'stridor, often after a viral '
                                                         'prodrome. Drooling/tripoding '
                                                         'suggests epiglottitis; '
                                                         'expiratory wheeze suggests '
                                                         'lower-airway disease such as '
                                                         'bronchiolitis or asthma.'}],
                              'hard': [{'question': 'Pyloric stenosis classic?',
                                        'options': ['A) Bilious vomiting from day one '
                                                    'of life',
                                                    'B) Chronic constipation starting '
                                                    'in adolescence',
                                                    'C) Projectile non-bilious '
                                                    'vomiting at about 2–8 weeks of '
                                                    'age',
                                                    'D) Painless rectal bleeding at 2 '
                                                    'years without vomiting'],
                                        'answer': 'C) Projectile non-bilious vomiting '
                                                  'at about 2–8 weeks of age',
                                        'explanation': 'Infantile hypertrophic pyloric '
                                                       'stenosis causes progressive '
                                                       'gastric outlet obstruction, '
                                                       'typically with projectile '
                                                       'non-bilious vomiting in weeks '
                                                       '2–8, visible peristalsis, and '
                                                       'a palpable olive. Bilious '
                                                       'emesis suggests more distal '
                                                       'obstruction.'},
                                       {'question': 'Intussusception stool?',
                                        'options': ['A) Acholic pale stools from '
                                                    'biliary atresia as the same '
                                                    'finding',
                                                    'B) Melena from duodenal ulcer as '
                                                    'the typical toddler pattern',
                                                    'C) Steatorrhea from pancreatic '
                                                    'insufficiency as the classic '
                                                    'intussusception stool',
                                                    'D) Redcurrant-jelly stool (a late '
                                                    'sign)'],
                                        'answer': 'D) Redcurrant-jelly stool (a late '
                                                  'sign)',
                                        'explanation': 'Intussusception may produce '
                                                       'currant-jelly stool from '
                                                       'ischemia and mucus late in the '
                                                       'course; earlier clues are '
                                                       'intermittent severe colic and '
                                                       'lethargy with a possible '
                                                       'sausage mass. Pale stools, '
                                                       'melena, and steatorrhea '
                                                       'indicate other diseases.'},
                                       {'question': 'Congenital adrenal hyperplasia '
                                                    'crisis in boys may show?',
                                        'options': ['A) Salt-wasting adrenal crisis '
                                                    'with shock, hyponatremia, and '
                                                    'hyperkalemia',
                                                    'B) Isolated hypertension without '
                                                    'electrolyte change',
                                                    'C) Cushingoid obesity from birth '
                                                    'without crisis',
                                                    'D) Hypoglycemia only without '
                                                    'mineralocorticoid features'],
                                        'answer': 'A) Salt-wasting adrenal crisis with '
                                                  'shock, hyponatremia, and '
                                                  'hyperkalemia',
                                        'explanation': 'In salt-wasting 21-hydroxylase '
                                                       'deficiency, boys lack '
                                                       'ambiguous genitalia and may '
                                                       'present in the first weeks '
                                                       'with vomiting, shock, '
                                                       'hyponatremia, and hyperkalemia '
                                                       'from aldosterone deficiency—an '
                                                       'endocrine emergency treated '
                                                       'with fluids, glucose, and '
                                                       'steroids.'}],
                              'extreme': [{'question': 'Ductal-dependent congenital '
                                                       'heart lesion presenting in '
                                                       'shock when the duct closes '
                                                       'needs?',
                                           'options': ['A) Indomethacin to close the '
                                                       'duct as first therapy in '
                                                       'ductal-dependent systemic flow',
                                                       'B) Prostaglandin E1 infusion '
                                                       'while resuscitating, under '
                                                       'specialty guidance',
                                                       'C) Fluid restriction alone '
                                                       'without ductal patency support',
                                                       'D) Outpatient cardiology '
                                                       'review in weeks without '
                                                       'prostaglandin'],
                                           'answer': 'B) Prostaglandin E1 infusion '
                                                     'while resuscitating, under '
                                                     'specialty guidance',
                                           'explanation': 'Ductal-dependent congenital '
                                                          'heart lesions present with '
                                                          'shock or cyanosis as the '
                                                          'ductus arteriosus closes. '
                                                          'PGE1 reopens/maintains '
                                                          'ductal flow while '
                                                          'resuscitation and urgent '
                                                          'cardiology/cardiac surgery '
                                                          'pathways proceed. '
                                                          'Indomethacin would close '
                                                          'the duct and worsen '
                                                          'systemic or pulmonary '
                                                          'flow.'},
                                          {'question': 'Non-accidental injury clue?',
                                           'options': ['A) Age-appropriate bruising on '
                                                       'shins in a cruising toddler '
                                                       'alone',
                                                       'B) Documented witnessed '
                                                       'accidental fall matching exam '
                                                       'findings',
                                                       'C) Injury inconsistent with '
                                                       'the history or developmental '
                                                       'stage',
                                                       'D) Isolated viral petechiae '
                                                       'with known enteroviral illness '
                                                       'and reassuring workup'],
                                           'answer': 'C) Injury inconsistent with the '
                                                     'history or developmental stage',
                                           'explanation': 'Non-accidental injury is '
                                                          'suggested when trauma is '
                                                          'inconsistent with history '
                                                          'or developmental capability '
                                                          '(e.g., femur fracture in a '
                                                          'nonambulatory infant), '
                                                          'patterned bruises, or '
                                                          'occult fractures. '
                                                          'Age-appropriate shin '
                                                          'bruises and consistent '
                                                          'accidental mechanisms are '
                                                          'less concerning.'},
                                          {'question': 'Acute epiglottitis classic '
                                                       'presentation (less common with '
                                                       'Hib vaccine)?',
                                           'options': ['A) Barking cough with mild '
                                                       'stridor managed as routine '
                                                       'croup at home',
                                                       'B) Bilateral expiratory wheeze '
                                                       'treated only with inhaled '
                                                       'bronchodilator',
                                                       'C) Simple viral rhinitis '
                                                       'without toxicity',
                                                       'D) Toxic appearance, drooling, '
                                                       'and tripoding—avoid agitating '
                                                       'the airway; obtain airway '
                                                       'expertise'],
                                           'answer': 'D) Toxic appearance, drooling, '
                                                     'and tripoding—avoid agitating '
                                                     'the airway; obtain airway '
                                                     'expertise',
                                           'explanation': 'Epiglottitis presents with '
                                                          'a toxic child, drooling, '
                                                          'and tripoding from '
                                                          'supraglottic swelling. '
                                                          'Airway examination that '
                                                          'agitates the child can '
                                                          'precipitate complete '
                                                          'obstruction; keep the child '
                                                          'calm and summon experienced '
                                                          'airway support. Hib '
                                                          'vaccination has made '
                                                          'classic epiglottitis '
                                                          'uncommon but not '
                                                          'extinct.'}]},
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
