"""Undergraduate nursing study content by specialty and difficulty."""
from __future__ import annotations

import random

from quiz_bank import DIFFICULTIES, DIFFICULTY_LABELS, LABEL_TO_DIFFICULTY

SPECIALTY_ORDER = ['fundamentals', 'med_surg', 'pediatrics', 'maternity', 'psychiatric', 'community', 'critical_care', 'pharm_nursing', 'ethics_leadership', 'geriatrics']

SPECIALTIES: dict[str, dict] = {'fundamentals': {'label': 'Fundamentals of Nursing',
                  'books': ['Fundamentals of Nursing — Potter & Perry',
                            "Kozier & Erb's Fundamentals of Nursing",
                            'Nursing diagnosis handbooks'],
                  'pdf_notes': ['ABC and safety come before routine tasks.',
                                'Two patient identifiers every medication/procedure.',
                                'Hand hygiene is the highest-yield infection control habit.',
                                'Reassess after interventions (pain, vitals, response).',
                                'Document factually; report near misses.'],
                  'questions': {'easy': [{'question': 'Vital signs typically include?',
                                          'options': ['A) Temperature, pulse, respiration, blood '
                                                      'pressure (± SpO2/pain)',
                                                      'B) Only urine output forever',
                                                      'C) Only weight only',
                                                      'D) Only ECG always'],
                                          'answer': 'A) Temperature, pulse, respiration, blood '
                                                    'pressure (± SpO2/pain)',
                                          'explanation': 'Core bedside assessment.'},
                                         {'question': 'Hand hygiene is primarily to?',
                                          'options': ['A) Reduce pathogen transmission',
                                                      'B) Replace sterile technique always',
                                                      'C) Only clean gloves forever',
                                                      'D) Only after discharge'],
                                          'answer': 'A) Reduce pathogen transmission',
                                          'explanation': 'Most effective infection-control '
                                                         'measure.'},
                                         {'question': 'Informed consent requires?',
                                          'options': ['A) Understanding of procedure, risks, '
                                                      'alternatives, voluntary agreement',
                                                      'B) Nurse signature only without explanation',
                                                      'C) Family coercion always',
                                                      'D) No documentation'],
                                          'answer': 'A) Understanding of procedure, risks, '
                                                    'alternatives, voluntary agreement',
                                          'explanation': 'Nurse often witnesses; provider '
                                                         'explains.'}],
                                'medium': [{'question': 'Best time to assess pain after IV opioid '
                                                        'roughly?',
                                            'options': ['A) At expected peak effect (often ~15–30 '
                                                        'min; follow policy/drug)',
                                                        'B) Only after 12 hours always',
                                                        'C) Never reassess',
                                                        'D) Only at discharge'],
                                            'answer': 'A) At expected peak effect (often ~15–30 '
                                                      'min; follow policy/drug)',
                                            'explanation': 'Reassess efficacy and adverse '
                                                           'effects.'},
                                           {'question': 'Fall risk interventions include?',
                                            'options': ['A) Call light in reach, non-slip '
                                                        'footwear, bed low, assist as needed',
                                                        'B) Keep bed highest always',
                                                        'C) Remove call light',
                                                        'D) Encourage rushing alone'],
                                            'answer': 'A) Call light in reach, non-slip footwear, '
                                                      'bed low, assist as needed',
                                            'explanation': 'Prevention is multifactorial.'},
                                           {'question': 'Standard precautions apply to?',
                                            'options': ['A) All patients',
                                                        'B) Only isolation rooms',
                                                        'C) Only surgical patients',
                                                        'D) Only febrile patients'],
                                            'answer': 'A) All patients',
                                            'explanation': 'Assume all blood/body fluids '
                                                           'potentially infectious.'}],
                                'hard': [{'question': 'A junior colleague asks for the single best '
                                                      'answer. Priority framework when multiple '
                                                      'needs compete? Beware of near-miss '
                                                      'distractors.',
                                          'options': ['A) Airway/breathing/circulation and safety '
                                                      'before routine tasks',
                                                      'B) Complete charting before airway',
                                                      'C) Only psychosocial first always',
                                                      'D) Ignore ABCs'],
                                          'answer': 'A) Airway/breathing/circulation and safety '
                                                    'before routine tasks',
                                          'explanation': 'Maslow/ABC triage thinking.'},
                                         {'question': 'A junior colleague asks for the single best '
                                                      'answer. Restraint use requires? Beware of '
                                                      'near-miss distractors.',
                                          'options': ['A) Least restrictive alternative, order, '
                                                      'monitoring, documentation',
                                                      'B) Convenience alone without assessment',
                                                      'C) Family demand only',
                                                      'D) No reassessment'],
                                          'answer': 'A) Least restrictive alternative, order, '
                                                    'monitoring, documentation',
                                          'explanation': 'Safety and ethics.'},
                                         {'question': 'A junior colleague asks for the single best '
                                                      'answer. Medication right that prevents '
                                                      'wrong patient? Beware of near-miss '
                                                      'distractors.',
                                          'options': ['A) Right patient (two identifiers)',
                                                      'B) Right room number alone always',
                                                      'C) Right bed color',
                                                      'D) Right roommate name'],
                                          'answer': 'A) Right patient (two identifiers)',
                                          'explanation': 'Two identifiers every time.'}],
                                'extreme': [{'question': 'In a high-stakes nursing scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? Unresponsive patient, no pulse '
                                                         '— first action? Avoid actions that could '
                                                         'harm if a critical risk remains open.',
                                             'options': ['A) Start CPR / call emergency response '
                                                         'per protocol',
                                                         'B) Wait for family consent only',
                                                         'C) Only document first',
                                                         'D) Leave to find chart'],
                                             'answer': 'A) Start CPR / call emergency response per '
                                                       'protocol',
                                             'explanation': 'CAB/CPR immediacy.'},
                                            {'question': 'In a high-stakes nursing scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? Suspected transfusion reaction '
                                                         'mid-transfusion? Avoid actions that '
                                                         'could harm if a critical risk remains '
                                                         'open.',
                                             'options': ['A) Stop transfusion, keep IV line with '
                                                         'NS, assess, notify provider/blood bank',
                                                         'B) Increase rate to finish',
                                                         'C) Ignore fever',
                                                         'D) Discard bag without notification'],
                                             'answer': 'A) Stop transfusion, keep IV line with NS, '
                                                       'assess, notify provider/blood bank',
                                             'explanation': 'Classic emergency nursing action.'},
                                            {'question': 'In a high-stakes nursing scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? Fire on unit — RACE theme '
                                                         'starts with? Avoid actions that could '
                                                         'harm if a critical risk remains open.',
                                             'options': ['A) Rescue patients in immediate danger '
                                                         '(then alarm/contain/extinguish as '
                                                         'trained)',
                                                         'B) Hide charts first',
                                                         'C) Finish meal trays',
                                                         'D) Ignore alarms'],
                                             'answer': 'A) Rescue patients in immediate danger '
                                                       '(then alarm/contain/extinguish as trained)',
                                             'explanation': 'Know facility fire plan.'}]},
                  'cases': {'easy': [{'title': 'New Admission Baseline',
                                      'stem': 'A newly admitted adult is alert; nurse prepares '
                                              'first assessment.',
                                      'question': 'Priority baseline?',
                                      'answer': 'ABC/vital signs + focused history and safety '
                                                'orientation.',
                                      'discussion': 'Establish baseline before interventions.',
                                      'book_hint': 'Fundamentals of Nursing — Potter & Perry / '
                                                   'Kozier'}],
                            'medium': [{'title': 'Post-op Hypotension',
                                        'stem': '1 hour after surgery BP drops; patient drowsy.',
                                        'question': 'First nursing actions theme?',
                                        'answer': 'ABC, call for help per protocol, assess '
                                                  'bleeding/volume, notify provider.',
                                        'discussion': 'Do not leave unstable patient unattended.',
                                        'book_hint': 'Fundamentals of Nursing — Potter & Perry / '
                                                     'Kozier'}],
                            'hard': [{'title': 'Confusion After Sedation',
                                      'stem': 'Elderly patient becomes newly confused after '
                                              'benzodiazepine.',
                                      'question': 'Nursing priority?',
                                      'answer': 'Safety, assess oxygenation/glucose/neuro, notify, '
                                                'avoid more sedatives blindly.',
                                      'discussion': 'Delirium workup themes.',
                                      'book_hint': 'Fundamentals of Nursing — Potter & Perry / '
                                                   'Kozier'}],
                            'extreme': [{'title': 'Airway Emergency',
                                         'stem': 'Patient develops stridor after medication; SpO2 '
                                                 'falling.',
                                         'question': 'Immediate priority?',
                                         'answer': 'Airway support, emergency response, prepare '
                                                   'for advanced airway, stop culprit if known.',
                                         'discussion': 'Do not delay for non-urgent tasks.',
                                         'book_hint': 'Fundamentals of Nursing — Potter & Perry / '
                                                      'Kozier'}]}},
 'med_surg': {'label': 'Medical-Surgical Nursing',
              'books': ['Medical-Surgical Nursing — Lewis',
                        'Ignatavicius Medical-Surgical Nursing',
                        'Pathophysiology primers'],
              'pdf_notes': ['Chest pain / dyspnea / new confusion = escalate early.',
                            'Know sepsis recognition cues on the ward.',
                            'Post-op: ABCs, bleeding, VTE prevention, pulmonary hygiene.',
                            'Interpret trends (weight, I&O, labs), not single values alone.',
                            'Patient teaching prevents readmissions.'],
              'questions': {'easy': [{'question': 'Chest pain suggesting ACS — first nursing '
                                                  'themes?',
                                      'options': ['A) ABC, ECG access, oxygen if indicated, notify '
                                                  'promptly',
                                                  'B) Encourage treadmill first',
                                                  'C) Only give antacid forever',
                                                  'D) Ignore radiating pain'],
                                      'answer': 'A) ABC, ECG access, oxygen if indicated, notify '
                                                'promptly',
                                      'explanation': 'Time-sensitive cardiac care.'},
                                     {'question': 'Post-op incentive spirometry aims to?',
                                      'options': ['A) Prevent atelectasis / promote lung expansion',
                                                  'B) Replace ambulation always',
                                                  'C) Only treat constipation',
                                                  'D) Only lower BP'],
                                      'answer': 'A) Prevent atelectasis / promote lung expansion',
                                      'explanation': 'Pulmonary hygiene.'},
                                     {'question': 'Hypoglycemia classic early signs?',
                                      'options': ['A) Sweating, tremor, confusion/hunger (vary)',
                                                  'B) Only hypertension always',
                                                  'C) Only bradycardia only',
                                                  'D) Only rash'],
                                      'answer': 'A) Sweating, tremor, confusion/hunger (vary)',
                                      'explanation': 'Treat promptly with protocol.'}],
                            'medium': [{'question': 'Heart failure weight gain overnight suggests?',
                                        'options': ['A) Fluid retention — assess and report',
                                                    'B) Always muscle only',
                                                    'C) Always irrelevant',
                                                    'D) Always improved nutrition only'],
                                        'answer': 'A) Fluid retention — assess and report',
                                        'explanation': 'Daily weights matter.'},
                                       {'question': 'NG tube placement confirmation gold standard?',
                                        'options': ['A) X-ray confirmation per policy before first '
                                                    'use',
                                                    'B) Air insufflation alone always adequate',
                                                    'C) Patient saying it feels fine only',
                                                    'D) No check needed'],
                                        'answer': 'A) X-ray confirmation per policy before first '
                                                  'use',
                                        'explanation': 'Aspiration prevention.'},
                                       {'question': 'DVT prevention includes?',
                                        'options': ['A) Early ambulation, prophylaxis as ordered, '
                                                    'leg exercises',
                                                    'B) Prolonged immobility encouragement',
                                                    'C) Crossing legs tightly always',
                                                    'D) Ignoring calf pain'],
                                        'answer': 'A) Early ambulation, prophylaxis as ordered, '
                                                  'leg exercises',
                                        'explanation': 'VTE risk is high post-op.'}],
                            'hard': [{'question': 'A junior colleague asks for the single best '
                                                  'answer. Sepsis early nursing recognition uses? '
                                                  'Beware of near-miss distractors.',
                                      'options': ['A) Infection + organ dysfunction signs '
                                                  '(fever/hypothermia, tachypnea, altered '
                                                  'mentation, etc.)',
                                                  'B) Waiting for hypotension only always',
                                                  'C) Only rash required',
                                                  'D) Ignoring lactate'],
                                      'answer': 'A) Infection + organ dysfunction signs '
                                                '(fever/hypothermia, tachypnea, altered mentation, '
                                                'etc.)',
                                      'explanation': 'Early recognition saves lives.'},
                                     {'question': 'A junior colleague asks for the single best '
                                                  'answer. COPD patient on high O2 becomes drowsy '
                                                  '— concern? Beware of near-miss distractors.',
                                      'options': ['A) CO2 retention / ventilatory failure risk — '
                                                  'assess ABG/notify',
                                                  'B) Always give more O2 blindly',
                                                  'C) Ignore SpO2',
                                                  'D) Force oral fluids only'],
                                      'answer': 'A) CO2 retention / ventilatory failure risk — '
                                                'assess ABG/notify',
                                      'explanation': 'Titrate O2 carefully.'},
                                     {'question': 'A junior colleague asks for the single best '
                                                  'answer. Post-thyroidectomy emergency concern? '
                                                  'Beware of near-miss distractors.',
                                      'options': ['A) Airway compromise / hematoma / hypocalcemia '
                                                  'themes',
                                                  'B) Only constipation',
                                                  'C) Only acne',
                                                  'D) Only myopia'],
                                      'answer': 'A) Airway compromise / hematoma / hypocalcemia '
                                                'themes',
                                      'explanation': 'Tracheostomy kit readiness themes.'}],
                            'extreme': [{'question': 'In a high-stakes nursing scenario with '
                                                     'incomplete data, which statement is MOST '
                                                     'correct? Anaphylaxis after IV antibiotic — '
                                                     'first drug theme? Avoid actions that could '
                                                     'harm if a critical risk remains open.',
                                         'options': ['A) Epinephrine IM per protocol + airway '
                                                     'support / stop infusion',
                                                     'B) Only oral antihistamine forever',
                                                     'C) Increase infusion rate',
                                                     'D) Wait and see 2 hours'],
                                         'answer': 'A) Epinephrine IM per protocol + airway '
                                                   'support / stop infusion',
                                         'explanation': 'Life-threatening emergency.'},
                                        {'question': 'In a high-stakes nursing scenario with '
                                                     'incomplete data, which statement is MOST '
                                                     'correct? Massive hemoptysis priority? Avoid '
                                                     'actions that could harm if a critical risk '
                                                     'remains open.',
                                         'options': ['A) Airway protection / position bleeding '
                                                     'side down if known, emergency help',
                                                     'B) Encourage coughing forcefully '
                                                     'unsupervised only',
                                                     'C) Only chart color',
                                                     'D) Leave for lunch'],
                                         'answer': 'A) Airway protection / position bleeding side '
                                                   'down if known, emergency help',
                                         'explanation': 'Airway first.'},
                                        {'question': 'In a high-stakes nursing scenario with '
                                                     'incomplete data, which statement is MOST '
                                                     'correct? Suspect compartment syndrome after '
                                                     'cast? Avoid actions that could harm if a '
                                                     'critical risk remains open.',
                                         'options': ['A) Pain out of proportion, pallor, '
                                                     'paresthesia — urgent notify; do not elevate '
                                                     'blindly alone as only action',
                                                     'B) Ignore escalating pain',
                                                     'C) Tighten cast more',
                                                     'D) Give only PRN sleep aid'],
                                         'answer': 'A) Pain out of proportion, pallor, paresthesia '
                                                   '— urgent notify; do not elevate blindly alone '
                                                   'as only action',
                                         'explanation': 'Limb-threatening.'}]},
              'cases': {'easy': [{'title': 'New Chest Pain',
                                  'stem': 'Ward patient reports crushing chest pain radiating to '
                                          'arm.',
                                  'question': 'Priority?',
                                  'answer': 'Stay with patient, ABC, call rapid response/ECG per '
                                            'protocol, notify provider.',
                                  'discussion': 'Do not leave for non-urgent tasks.',
                                  'book_hint': 'Medical-Surgical Nursing — Lewis / Ignatavicius'}],
                        'medium': [{'title': 'Rising Creatinine on ACEI',
                                    'stem': 'Patient on ACEI has rising creatinine and '
                                            'hyperkalemia.',
                                    'question': 'Nursing action theme?',
                                    'answer': 'Hold per protocol, notify provider, review '
                                              'meds/fluids, monitor ECG if K high.',
                                    'discussion': 'Do not ignore lab trends.',
                                    'book_hint': 'Medical-Surgical Nursing — Lewis / '
                                                 'Ignatavicius'}],
                        'hard': [{'title': 'Suspected Sepsis',
                                  'stem': 'Post-op day 2: fever, HR 120, RR 28, confused.',
                                  'question': 'Priority bundle theme?',
                                  'answer': 'Rapid assessment, cultures before antibiotics if '
                                            'possible without delay, fluids/abx per protocol, '
                                            'escalate.',
                                  'discussion': 'Surviving sepsis nursing role.',
                                  'book_hint': 'Medical-Surgical Nursing — Lewis / Ignatavicius'}],
                        'extreme': [{'title': 'PE Suspicion',
                                     'stem': 'Sudden dyspnea, chest pain, SpO2 84% after long bone '
                                             'surgery.',
                                     'question': 'Priority?',
                                     'answer': 'Oxygen/support ABC, rapid response, notify '
                                               'provider, prepare for workup; do not ambulate '
                                               'further.',
                                     'discussion': 'VTE emergency.',
                                     'book_hint': 'Medical-Surgical Nursing — Lewis / '
                                                  'Ignatavicius'}]}},
 'pediatrics': {'label': 'Pediatric Nursing',
                'books': ["Wong's Essentials of Pediatric Nursing",
                          'Pediatric nursing care plans',
                          'PALS provider resources'],
                'pdf_notes': ['Weight-based dosing with safe-range checks.',
                              'Fever in young infants is urgent until proven otherwise.',
                              'Use age-appropriate pain scales (FLACC, Wong-Baker).',
                              'Airway differences: do not agitate suspected epiglottitis.',
                              'Family-centered care and mandated reporting duties.'],
                'questions': {'easy': [{'question': 'Best IM site for young infants often?',
                                        'options': ['A) Vastus lateralis',
                                                    'B) Dorsogluteal always preferred in neonates',
                                                    'C) Deltoid only in newborns always',
                                                    'D) Foot pad'],
                                        'answer': 'A) Vastus lateralis',
                                        'explanation': 'Age-appropriate sites.'},
                                       {'question': 'Pediatric med dosing commonly based on?',
                                        'options': ['A) Weight (mg/kg) with safe range checks',
                                                    'B) Adult dose always',
                                                    'C) Hair color',
                                                    'D) Room number'],
                                        'answer': 'A) Weight (mg/kg) with safe range checks',
                                        'explanation': 'Double-check calculations.'},
                                       {'question': 'Fontanelle assessment is relevant in?',
                                        'options': ['A) Infants',
                                                    'B) Only elderly always',
                                                    'C) Only adolescents only',
                                                    'D) Only pregnancy'],
                                        'answer': 'A) Infants',
                                        'explanation': 'Hydration/ICP clues.'}],
                              'medium': [{'question': 'Dehydration signs in children include?',
                                          'options': ['A) Sunken eyes/fontanelle, dry mucosa, '
                                                      'decreased tears/urine, lethargy',
                                                      'B) Only hyperactivity always',
                                                      'C) Always moist mucosa only',
                                                      'D) Only adult BP cutoffs'],
                                          'answer': 'A) Sunken eyes/fontanelle, dry mucosa, '
                                                    'decreased tears/urine, lethargy',
                                          'explanation': 'Compare to baseline.'},
                                         {'question': 'FLACC scale is used for?',
                                          'options': ['A) Pain assessment in nonverbal/young '
                                                      'children',
                                                      'B) Only adult IQ',
                                                      'C) Only adult BMI',
                                                      'D) Only vision'],
                                          'answer': 'A) Pain assessment in nonverbal/young '
                                                    'children',
                                          'explanation': 'Behavioral pain tool.'},
                                         {'question': 'RSV bronchiolitis nursing focus?',
                                          'options': ['A) Supportive airway/oxygen/hydration; '
                                                      'isolation precautions as indicated',
                                                      'B) Routine antibiotics always cure RSV',
                                                      'C) Force feed solids only',
                                                      'D) Ignore SpO2'],
                                          'answer': 'A) Supportive airway/oxygen/hydration; '
                                                    'isolation precautions as indicated',
                                          'explanation': 'Viral supportive care.'}],
                              'hard': [{'question': 'A junior colleague asks for the single best '
                                                    'answer. Suspected child abuse reporting? '
                                                    'Beware of near-miss distractors.',
                                        'options': ['A) Nurses are mandated reporters — follow '
                                                    'law/policy',
                                                    'B) Only tell parents privately forever and '
                                                    'stop',
                                                    'C) Ignore bruises',
                                                    'D) Wait until discharge always'],
                                        'answer': 'A) Nurses are mandated reporters — follow '
                                                  'law/policy',
                                        'explanation': 'Protect the child.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Epiglottitis classic caution? Beware '
                                                    'of near-miss distractors.',
                                        'options': ['A) Do not agitate / avoid throat exam that '
                                                    'precipitates obstruction; airway readiness',
                                                    'B) Force tongue blade exam first always',
                                                    'C) Give oral fluids freely while distressed',
                                                    'D) Ignore drooling'],
                                        'answer': 'A) Do not agitate / avoid throat exam that '
                                                  'precipitates obstruction; airway readiness',
                                        'explanation': 'Airway emergency.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Kawasaki concern includes? Beware of '
                                                    'near-miss distractors.',
                                        'options': ['A) Coronary artery complications — follow '
                                                    'treatment protocols',
                                                    'B) Only dental caries',
                                                    'C) Only myopia',
                                                    'D) Only acne alone'],
                                        'answer': 'A) Coronary artery complications — follow '
                                                  'treatment protocols',
                                        'explanation': 'Fever + mucocutaneous signs themes.'}],
                              'extreme': [{'question': 'In a high-stakes nursing scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Pediatric cardiac arrest '
                                                       'compression depth theme? Avoid actions '
                                                       'that could harm if a critical risk remains '
                                                       'open.',
                                           'options': ['A) About 1/3 AP chest diameter; '
                                                       'high-quality CPR',
                                                       'B) Only 1 cm always',
                                                       'C) No compressions if parent present',
                                                       'D) Only abdominal thrusts forever'],
                                           'answer': 'A) About 1/3 AP chest diameter; high-quality '
                                                     'CPR',
                                           'explanation': 'PALS themes.'},
                                          {'question': 'In a high-stakes nursing scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Anaphylaxis in child after '
                                                       'peanut? Avoid actions that could harm if a '
                                                       'critical risk remains open.',
                                           'options': ['A) IM epinephrine promptly + emergency '
                                                       'activation',
                                                       'B) Wait for rash to spread fully',
                                                       'C) Only oral water',
                                                       'D) Induce vomiting'],
                                           'answer': 'A) IM epinephrine promptly + emergency '
                                                     'activation',
                                           'explanation': 'Do not delay epi.'},
                                          {'question': 'In a high-stakes nursing scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Suspected increased ICP in child '
                                                       'after trauma? Avoid actions that could '
                                                       'harm if a critical risk remains open.',
                                           'options': ['A) ABC, head midline, avoid hypotonic '
                                                       'fluids blindly, urgent notify/neurosurg '
                                                       'path',
                                                       'B) Trendelenburg always',
                                                       'C) Force oral hydration race',
                                                       'D) Ignore unequal pupils'],
                                           'answer': 'A) ABC, head midline, avoid hypotonic fluids '
                                                     'blindly, urgent notify/neurosurg path',
                                           'explanation': 'Neuro emergency.'}]},
                'cases': {'easy': [{'title': 'Febrile Infant',
                                    'stem': '6-week-old with fever 38.5°C; parents anxious.',
                                    'question': 'Nursing priority theme?',
                                    'answer': 'ABC, triage urgency, support workup — young infants '
                                              'need prompt evaluation.',
                                    'discussion': 'Do not dismiss fever in neonate/young infant.',
                                    'book_hint': "Wong's Essentials of Pediatric Nursing"}],
                          'medium': [{'title': 'Asthma Exacerbation',
                                      'stem': 'Child wheezing, speaking short phrases, SpO2 90%.',
                                      'question': 'Priority?',
                                      'answer': 'Oxygen/bronchodilator per protocol, calm '
                                                'positioning, escalate if severe.',
                                      'discussion': 'Status risk.',
                                      'book_hint': "Wong's Essentials of Pediatric Nursing"}],
                          'hard': [{'title': 'Croup vs Epiglottitis',
                                    'stem': 'Toddler with stridor; sitting forward, drooling, '
                                            'toxic.',
                                    'question': 'Concern?',
                                    'answer': 'Possible epiglottitis — minimize agitation, airway '
                                              'team, do not force exam.',
                                    'discussion': 'Differentiate from viral croup.',
                                    'book_hint': "Wong's Essentials of Pediatric Nursing"}],
                          'extreme': [{'title': 'Septic Shock Toddler',
                                       'stem': 'Toddler febrile, mottled, delayed CRT, lethargic.',
                                       'question': 'Priority?',
                                       'answer': 'ABC, oxygen, rapid IV/IO access, fluid bolus per '
                                                 'PALS/sepsis protocol, antibiotics, escalate.',
                                       'discussion': 'Minutes matter.',
                                       'book_hint': "Wong's Essentials of Pediatric Nursing"}]}},
 'maternity': {'label': 'Maternity / OB Nursing',
               'books': ["Maternity & Women's Health Care — Lowdermilk",
                         'Maternal-Newborn Nursing texts',
                         'Obstetric emergency protocols'],
               'pdf_notes': ['PPH: massage fundus, call help, follow hemorrhage bundle.',
                             'Preeclampsia danger signs need urgent escalation.',
                             'MgSO4 toxicity: stop drip, support RR, notify.',
                             'Cord prolapse: relieve pressure, emergent birth path.',
                             'Support bonding and newborn transition (APGAR, warmth).'],
               'questions': {'easy': [{'question': 'APGAR assesses newborn?',
                                       'options': ['A) Appearance, Pulse, Grimace, Activity, '
                                                   'Respiration',
                                                   'B) Only weight',
                                                   'C) Only maternal BP',
                                                   'D) Only cord length'],
                                       'answer': 'A) Appearance, Pulse, Grimace, Activity, '
                                                 'Respiration',
                                       'explanation': '1 and 5 minutes typically.'},
                                      {'question': 'Fundal massage after birth primarily for?',
                                       'options': ['A) Uterine atony / postpartum hemorrhage '
                                                   'control',
                                                   'B) Only breastfeeding latch forever',
                                                   'C) Only newborn bath',
                                                   'D) Only episiotomy stitch'],
                                       'answer': 'A) Uterine atony / postpartum hemorrhage control',
                                       'explanation': 'First-line nursing for boggy uterus.'},
                                      {'question': 'Rh-negative mother may need?',
                                       'options': ['A) Rh immune globulin when indicated',
                                                   'B) Always iron only',
                                                   'C) Always no blood product ever',
                                                   'D) Vitamin C only'],
                                       'answer': 'A) Rh immune globulin when indicated',
                                       'explanation': 'Prevent sensitization.'}],
                             'medium': [{'question': 'Preeclampsia danger signs include?',
                                         'options': ['A) Severe headache, visual changes, RUQ '
                                                     'pain, rising BP, proteinuria themes',
                                                     'B) Only mild ankle edema alone always benign '
                                                     'forever',
                                                     'C) Only heartburn always',
                                                     'D) Only stretch marks'],
                                         'answer': 'A) Severe headache, visual changes, RUQ pain, '
                                                   'rising BP, proteinuria themes',
                                         'explanation': 'Escalate promptly.'},
                                        {'question': 'Nonstress test reactive means roughly?',
                                         'options': ['A) Adequate fetal heart accelerations with '
                                                     'movement (criteria gestational-age '
                                                     'dependent)',
                                                     'B) Always decelerations only',
                                                     'C) Always flat line preferred',
                                                     'D) Maternal sleep only'],
                                         'answer': 'A) Adequate fetal heart accelerations with '
                                                   'movement (criteria gestational-age dependent)',
                                         'explanation': 'Fetal well-being screen.'},
                                        {'question': 'Mastitis teaching includes?',
                                         'options': ['A) Continue breastfeeding/pumping as '
                                                     'advised, antibiotics if prescribed, '
                                                     'supportive care',
                                                     'B) Abrupt weaning always required first',
                                                     'C) Ignore fever',
                                                     'D) Tight binding only'],
                                         'answer': 'A) Continue breastfeeding/pumping as advised, '
                                                   'antibiotics if prescribed, supportive care',
                                         'explanation': 'Emptying breast helps.'}],
                             'hard': [{'question': 'A junior colleague asks for the single best '
                                                   'answer. Shoulder dystocia nursing help? Beware '
                                                   'of near-miss distractors.',
                                       'options': ['A) McRoberts, suprapubic pressure (not '
                                                   'fundal), call for help',
                                                   'B) Fundal pressure first always',
                                                   'C) Leave room',
                                                   'D) Only chart'],
                                       'answer': 'A) McRoberts, suprapubic pressure (not fundal), '
                                                 'call for help',
                                       'explanation': 'HELPERR themes.'},
                                      {'question': 'A junior colleague asks for the single best '
                                                   'answer. Abruptio placentae classic? Beware of '
                                                   'near-miss distractors.',
                                       'options': ['A) Painful bleeding, uterine '
                                                   'tenderness/hypertonus, fetal distress risk',
                                                   'B) Painless bright bleeding always placenta '
                                                   'previa only',
                                                   'C) Always normal labor forever',
                                                   'D) Only UTI'],
                                       'answer': 'A) Painful bleeding, uterine '
                                                 'tenderness/hypertonus, fetal distress risk',
                                       'explanation': 'Emergency.'},
                                      {'question': 'A junior colleague asks for the single best '
                                                   'answer. Postpartum blues vs depression? Beware '
                                                   'of near-miss distractors.',
                                       'options': ['A) Blues brief/self-limited; depression '
                                                   'persistent and impairs function — screen/refer',
                                                   'B) Depression never occurs',
                                                   'C) Blues always psychosis',
                                                   'D) Ignore tearfulness always'],
                                       'answer': 'A) Blues brief/self-limited; depression '
                                                 'persistent and impairs function — screen/refer',
                                       'explanation': 'Mental health screening.'}],
                             'extreme': [{'question': 'In a high-stakes nursing scenario with '
                                                      'incomplete data, which statement is MOST '
                                                      'correct? Eclampsia priority after seizure? '
                                                      'Avoid actions that could harm if a critical '
                                                      'risk remains open.',
                                          'options': ['A) Airway/breathing, lateral position, '
                                                      'MgSO4 per protocol, protect from injury',
                                                      'B) Oral fluids immediately during seizure',
                                                      'C) Leave alone',
                                                      'D) Only document after hours'],
                                          'answer': 'A) Airway/breathing, lateral position, MgSO4 '
                                                    'per protocol, protect from injury',
                                          'explanation': 'Maternal-fetal emergency.'},
                                         {'question': 'In a high-stakes nursing scenario with '
                                                      'incomplete data, which statement is MOST '
                                                      'correct? Amniotic fluid embolism suspicion? '
                                                      'Avoid actions that could harm if a critical '
                                                      'risk remains open.',
                                          'options': ['A) Sudden hypoxia/hypotension/coagulopathy '
                                                      'in labor — emergency response',
                                                      'B) Routine ambulation first',
                                                      'C) Ignore dyspnea',
                                                      'D) Only antacid'],
                                          'answer': 'A) Sudden hypoxia/hypotension/coagulopathy in '
                                                    'labor — emergency response',
                                          'explanation': 'Catastrophic rarity — act fast.'},
                                         {'question': 'In a high-stakes nursing scenario with '
                                                      'incomplete data, which statement is MOST '
                                                      'correct? Uterine inversion recognition? '
                                                      'Avoid actions that could harm if a critical '
                                                      'risk remains open.',
                                          'options': ['A) Fundus prolapses; hemorrhage/shock — do '
                                                      'not remove placenta aggressively; emergency '
                                                      'help',
                                                      'B) Push fundal pressure harder blindly',
                                                      'C) Ignore',
                                                      'D) Oral oxytocin only'],
                                          'answer': 'A) Fundus prolapses; hemorrhage/shock — do '
                                                    'not remove placenta aggressively; emergency '
                                                    'help',
                                          'explanation': 'Obstetric emergency.'}]},
               'cases': {'easy': [{'title': 'Boggy Uterus',
                                   'stem': '1 hour PP: heavy lochia, fundus soft/boggy.',
                                   'question': 'First action?',
                                   'answer': 'Fundal massage, call for help, assess bladder, '
                                             'notify provider.',
                                   'discussion': 'PPH pathway.',
                                   'book_hint': "Maternity & Women's Health Care — Lowdermilk / "
                                                'Maternal-Newborn Nursing'}],
                         'medium': [{'title': 'Magnesium Sulfate',
                                     'stem': 'Preeclamptic on MgSO4 becomes drowsy with RR 10 and '
                                             'loss of reflexes.',
                                     'question': 'Concern?',
                                     'answer': 'Mg toxicity — stop infusion per protocol, support '
                                               'airway, notify, calcium gluconate readiness.',
                                     'discussion': 'Toxicity triage.',
                                     'book_hint': "Maternity & Women's Health Care — Lowdermilk / "
                                                  'Maternal-Newborn Nursing'}],
                         'hard': [{'title': 'PPH Unresponsive',
                                   'stem': 'Despite massage, bleeding continues; patient pale, '
                                           'tachycardic.',
                                   'question': 'Priority?',
                                   'answer': 'Activate hemorrhage protocol, large-bore IV, oxygen, '
                                             'uterotonics as ordered, prepare for higher care.',
                                   'discussion': 'Do not delay escalation.',
                                   'book_hint': "Maternity & Women's Health Care — Lowdermilk / "
                                                'Maternal-Newborn Nursing'}],
                         'extreme': [{'title': 'Cord Prolapse',
                                      'stem': 'ROM; cord visible; fetal bradycardia.',
                                      'question': 'Immediate action?',
                                      'answer': 'Relieve cord pressure (elevate presenting part), '
                                                'call for help, prepare emergent birth, do not '
                                                'push cord back routinely.',
                                      'discussion': 'Minutes to birth.',
                                      'book_hint': "Maternity & Women's Health Care — Lowdermilk / "
                                                   'Maternal-Newborn Nursing'}]}},
 'psychiatric': {'label': 'Psychiatric Nursing',
                 'books': ['Psychiatric-Mental Health Nursing — Videbeck',
                           'Townsend Psychiatric Mental Health Nursing',
                           'Crisis intervention guides'],
                 'pdf_notes': ['Ask directly about suicide; ensure safety first.',
                               'Therapeutic communication over arguing delusions.',
                               'Know lithium toxicity and alcohol withdrawal risks.',
                               'De-escalate early; restraints are last resort.',
                               'NMS and serotonin syndrome are emergencies.'],
                 'questions': {'easy': [{'question': 'Therapeutic communication emphasizes?',
                                         'options': ['A) Open-ended questions, empathy, '
                                                     'clarifying, nonjudgmental stance',
                                                     'B) Giving false reassurance always',
                                                     'C) Changing subject to nurse problems',
                                                     'D) Arguing delusions as debate sport'],
                                         'answer': 'A) Open-ended questions, empathy, clarifying, '
                                                   'nonjudgmental stance',
                                         'explanation': 'Build trust.'},
                                        {'question': 'Suicide risk assessment asks about?',
                                         'options': ['A) Ideation, plan, intent, means, protective '
                                                     'factors',
                                                     'B) Only favorite color',
                                                     'C) Only BMI',
                                                     'D) Avoiding the topic forever'],
                                         'answer': 'A) Ideation, plan, intent, means, protective '
                                                   'factors',
                                         'explanation': 'Direct questions are appropriate.'},
                                        {'question': 'SSRIs common early side effect theme?',
                                         'options': ['A) GI upset, headache, sleep changes; watch '
                                                     'activation/suicidality especially early',
                                                     'B) Immediate permanent cure day 1 always',
                                                     'C) Only purple urine always',
                                                     'D) No monitoring ever'],
                                         'answer': 'A) GI upset, headache, sleep changes; watch '
                                                   'activation/suicidality especially early',
                                         'explanation': 'Educate and follow up.'}],
                               'medium': [{'question': 'Lithium toxicity early signs?',
                                           'options': ['A) Nausea, tremor, ataxia, confusion — '
                                                       'hold and notify; check level',
                                                       'B) Ignore coarse tremor',
                                                       'C) Double next dose',
                                                       'D) Only give caffeine'],
                                           'answer': 'A) Nausea, tremor, ataxia, confusion — hold '
                                                     'and notify; check level',
                                           'explanation': 'Narrow therapeutic index.'},
                                          {'question': 'Alcohol withdrawal risk includes?',
                                           'options': ['A) Seizures / DTs — use CIWA and protocols',
                                                       'B) Always harmless forever',
                                                       'C) Only treats itself with coffee',
                                                       'D) Ignore tachycardia'],
                                           'answer': 'A) Seizures / DTs — use CIWA and protocols',
                                           'explanation': 'Medical emergency potential.'},
                                          {'question': 'Hallucination nursing response?',
                                           'options': ['A) Acknowledge experience without '
                                                       'reinforcing delusion; redirect to '
                                                       'reality/safety',
                                                       'B) Argue for hours to prove wrong',
                                                       'C) Agree the voices are real entities '
                                                       'always',
                                                       'D) Ignore safety cues'],
                                           'answer': 'A) Acknowledge experience without '
                                                     'reinforcing delusion; redirect to '
                                                     'reality/safety',
                                           'explanation': 'Reality orientation gently.'}],
                               'hard': [{'question': 'A junior colleague asks for the single best '
                                                     'answer. NMS vs serotonin syndrome clue '
                                                     'themes? Beware of near-miss distractors.',
                                         'options': ['A) NMS: rigidity/fever on antipsychotics; '
                                                     'SS: hyperreflexia/clonus on serotonergic '
                                                     'combos — both emergencies',
                                                     'B) Both always benign',
                                                     'C) Only dental issue',
                                                     'D) Ignore fever on antipsychotics'],
                                         'answer': 'A) NMS: rigidity/fever on antipsychotics; SS: '
                                                   'hyperreflexia/clonus on serotonergic combos — '
                                                   'both emergencies',
                                         'explanation': 'Stop offender, supportive care, notify.'},
                                        {'question': 'A junior colleague asks for the single best '
                                                     'answer. Involuntary hold criteria themes? '
                                                     'Beware of near-miss distractors.',
                                         'options': ['A) Danger to self/others or grave disability '
                                                     'per law',
                                                     'B) Nurse dislike of patient',
                                                     'C) Family convenience only',
                                                     'D) Missed appointment alone'],
                                         'answer': 'A) Danger to self/others or grave disability '
                                                   'per law',
                                         'explanation': 'Know local mental health law.'},
                                        {'question': 'A junior colleague asks for the single best '
                                                     'answer. Clozapine unique monitoring? Beware '
                                                     'of near-miss distractors.',
                                         'options': ['A) Agranulocytosis risk — CBC monitoring '
                                                     'mandatory',
                                                     'B) No labs ever',
                                                     'C) Only dental x-rays',
                                                     'D) Ignore sore throat/fever'],
                                         'answer': 'A) Agranulocytosis risk — CBC monitoring '
                                                   'mandatory',
                                         'explanation': 'Fever/sore throat = urgent.'}],
                               'extreme': [{'question': 'In a high-stakes nursing scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Active suicide attempt on unit? '
                                                        'Avoid actions that could harm if a '
                                                        'critical risk remains open.',
                                            'options': ['A) Ensure scene safety, call emergency '
                                                        'response, first aid/ABC, continuous '
                                                        'observation',
                                                        'B) Leave to finish charting first',
                                                        'C) Debate motives for 30 min before help',
                                                        'D) Remove observation'],
                                            'answer': 'A) Ensure scene safety, call emergency '
                                                      'response, first aid/ABC, continuous '
                                                      'observation',
                                            'explanation': 'Life over paperwork.'},
                                           {'question': 'In a high-stakes nursing scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Violent patient with weapon? '
                                                        'Avoid actions that could harm if a '
                                                        'critical risk remains open.',
                                            'options': ['A) Do not approach alone; secure '
                                                        'self/others, call security/emergency per '
                                                        'policy',
                                                        'B) Grab weapon barehanded always',
                                                        'C) Corner alone',
                                                        'D) Ignore'],
                                            'answer': 'A) Do not approach alone; secure '
                                                      'self/others, call security/emergency per '
                                                      'policy',
                                            'explanation': 'Staff safety enables patient safety.'},
                                           {'question': 'In a high-stakes nursing scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Neuroleptic malignant syndrome '
                                                        'priority? Avoid actions that could harm '
                                                        'if a critical risk remains open.',
                                            'options': ['A) Stop antipsychotic, supportive care, '
                                                        'escalate urgently',
                                                        'B) Give another dose of same drug',
                                                        'C) Only oral fluids race',
                                                        'D) Ignore rigidity/fever'],
                                            'answer': 'A) Stop antipsychotic, supportive care, '
                                                      'escalate urgently',
                                            'explanation': 'High mortality if missed.'}]},
                 'cases': {'easy': [{'title': 'New Suicidal Ideation',
                                     'stem': 'Patient says life is not worth living; has a plan.',
                                     'question': 'Priority?',
                                     'answer': 'Safety — 1:1/observation per policy, remove means, '
                                               'notify provider, do not leave alone.',
                                     'discussion': 'Never dismiss.',
                                     'book_hint': 'Psychiatric-Mental Health Nursing — Videbeck / '
                                                  'Townsend'}],
                           'medium': [{'title': 'Aggressive Escalation',
                                       'stem': 'Patient pacing, clenched fists, yelling.',
                                       'question': 'First approach?',
                                       'answer': 'Safety distance, calm voice, offer choices, call '
                                                 'assistance early; seclusion/restraint last '
                                                 'resort.',
                                       'discussion': 'De-escalation first.',
                                       'book_hint': 'Psychiatric-Mental Health Nursing — Videbeck '
                                                    '/ Townsend'}],
                           'hard': [{'title': 'Lithium + Dehydration',
                                     'stem': 'Patient on lithium with vomiting/diarrhea; coarse '
                                             'tremor.',
                                     'question': 'Action?',
                                     'answer': 'Hold lithium, assess, notify, obtain '
                                               'level/electrolytes, hydrate carefully.',
                                     'discussion': 'Toxicity risk rises with volume depletion.',
                                     'book_hint': 'Psychiatric-Mental Health Nursing — Videbeck / '
                                                  'Townsend'}],
                           'extreme': [{'title': 'Serotonin Syndrome',
                                        'stem': 'On SSRI + tramadol: agitation, hyperreflexia, '
                                                'fever, diarrhea.',
                                        'question': 'Priority?',
                                        'answer': 'Stop serotonergic agents, ABC/cooling support, '
                                                  'notify provider urgently.',
                                        'discussion': 'Do not add more serotonergic drugs.',
                                        'book_hint': 'Psychiatric-Mental Health Nursing — Videbeck '
                                                     '/ Townsend'}]}},
 'community': {'label': 'Community / Public Health',
               'books': ['Community/Public Health Nursing — Stanhope & Lancaster',
                         'Public health nursing texts',
                         'CDC immunization schedules'],
               'pdf_notes': ['Primary vs secondary vs tertiary prevention.',
                             'Social determinants drive outcomes.',
                             'Reportable diseases and outbreak notification paths.',
                             'Home-visit safety planning matters.',
                             'Disaster triage: greatest good for greatest number.'],
               'questions': {'easy': [{'question': 'Primary prevention example?',
                                       'options': ['A) Immunization / health education before '
                                                   'disease',
                                                   'B) Rehab after stroke only',
                                                   'C) Only ICU care',
                                                   'D) Only chemotherapy'],
                                       'answer': 'A) Immunization / health education before '
                                                 'disease',
                                       'explanation': 'Prevent occurrence.'},
                                      {'question': 'Secondary prevention example?',
                                       'options': ['A) Screening (e.g., BP, mammogram) for early '
                                                   'detection',
                                                   'B) Building wheelchair ramps only',
                                                   'C) Only hospice',
                                                   'D) Only surgery forever'],
                                       'answer': 'A) Screening (e.g., BP, mammogram) for early '
                                                 'detection',
                                       'explanation': 'Detect early.'},
                                      {'question': 'Herd immunity relates to?',
                                       'options': ['A) Enough immunized people protecting '
                                                   'vulnerable',
                                                   'B) Only one person vaccinated ever',
                                                   'C) Avoiding all vaccines always',
                                                   'D) Only hand gel'],
                                       'answer': 'A) Enough immunized people protecting vulnerable',
                                       'explanation': 'Community protection.'}],
                             'medium': [{'question': 'Social determinants of health include?',
                                         'options': ['A) Housing, income, education, food access, '
                                                     'environment',
                                                     'B) Only genetics forever alone',
                                                     'C) Only shoe size',
                                                     'D) Only favorite color'],
                                         'answer': 'A) Housing, income, education, food access, '
                                                   'environment',
                                         'explanation': 'Shape outcomes.'},
                                        {'question': 'TB airborne precautions need?',
                                         'options': ['A) N95/respirator + airborne room as '
                                                     'indicated',
                                                     'B) Surgical mask only always enough for '
                                                     'nurse entering airborne room',
                                                     'C) No mask',
                                                     'D) Only gloves forever'],
                                         'answer': 'A) N95/respirator + airborne room as indicated',
                                         'explanation': 'Know transmission-based precautions.'},
                                        {'question': 'Home visit safety includes?',
                                         'options': ['A) Situational awareness, share itinerary, '
                                                     'exit plan, respect culture',
                                                     'B) Ignore neighborhood risk',
                                                     'C) Enter dark unknown spaces alone always',
                                                     'D) Leave meds unlabeled'],
                                         'answer': 'A) Situational awareness, share itinerary, '
                                                   'exit plan, respect culture',
                                         'explanation': 'Safety first.'}],
                             'hard': [{'question': 'A junior colleague asks for the single best '
                                                   'answer. Upstream thinking in public health '
                                                   'means? Beware of near-miss distractors.',
                                       'options': ['A) Address root causes/policies, not only '
                                                   'individual downstream care',
                                                   'B) Only treat end-stage disease',
                                                   'C) Ignore housing',
                                                   'D) Only ICU metrics'],
                                       'answer': 'A) Address root causes/policies, not only '
                                                 'individual downstream care',
                                       'explanation': 'Prevention at systems level.'},
                                      {'question': 'A junior colleague asks for the single best '
                                                   'answer. Disaster triage START theme? Beware of '
                                                   'near-miss distractors.',
                                       'options': ['A) Do the most good for most people with '
                                                   'limited resources',
                                                   'B) Treat least injured first always',
                                                   'C) Ignore airway',
                                                   'D) One patient only forever'],
                                       'answer': 'A) Do the most good for most people with limited '
                                                 'resources',
                                       'explanation': 'Utilitarian disaster ethics.'},
                                      {'question': 'A junior colleague asks for the single best '
                                                   'answer. Vaccine hesitancy best nursing '
                                                   'approach? Beware of near-miss distractors.',
                                       'options': ['A) Motivational interviewing, listen, correct '
                                                   'myths respectfully with evidence',
                                                   'B) Shame and argue only',
                                                   'C) Refuse all discussion',
                                                   'D) Fake data'],
                                       'answer': 'A) Motivational interviewing, listen, correct '
                                                 'myths respectfully with evidence',
                                       'explanation': 'Trust building.'}],
                             'extreme': [{'question': 'In a high-stakes nursing scenario with '
                                                      'incomplete data, which statement is MOST '
                                                      'correct? Suspected bioterror inhalation '
                                                      'anthrax cluster? Avoid actions that could '
                                                      'harm if a critical risk remains open.',
                                          'options': ['A) Recognize, protect self, notify public '
                                                      'health/emergency immediately',
                                                      'B) Wait weeks to report',
                                                      'C) Tell patients to travel widely',
                                                      'D) Ignore'],
                                          'answer': 'A) Recognize, protect self, notify public '
                                                    'health/emergency immediately',
                                          'explanation': 'Reportable emergency.'},
                                         {'question': 'In a high-stakes nursing scenario with '
                                                      'incomplete data, which statement is MOST '
                                                      'correct? Needle stick after unknown source? '
                                                      'Avoid actions that could harm if a critical '
                                                      'risk remains open.',
                                          'options': ['A) Wash, report, evaluate source, follow '
                                                      'PEP policy ASAP',
                                                      'B) Ignore and finish shift only',
                                                      'C) Suck wound',
                                                      'D) Delay weeks'],
                                          'answer': 'A) Wash, report, evaluate source, follow PEP '
                                                    'policy ASAP',
                                          'explanation': 'Time-sensitive PEP.'},
                                         {'question': 'In a high-stakes nursing scenario with '
                                                      'incomplete data, which statement is MOST '
                                                      'correct? Quarantine vs isolation? Avoid '
                                                      'actions that could harm if a critical risk '
                                                      'remains open.',
                                          'options': ['A) Isolation: ill contagious; quarantine: '
                                                      'exposed potentially incubating — follow '
                                                      'public health orders',
                                                      'B) Same always meaning forever',
                                                      'C) Only for pets',
                                                      'D) Never used'],
                                          'answer': 'A) Isolation: ill contagious; quarantine: '
                                                    'exposed potentially incubating — follow '
                                                    'public health orders',
                                          'explanation': 'Know definitions.'}]},
               'cases': {'easy': [{'title': 'School Outbreak',
                                   'stem': 'Several students with measles-like rash; some '
                                           'unvaccinated.',
                                   'question': 'Nursing public health action?',
                                   'answer': 'Notify public health, isolate per guidance, identify '
                                             'contacts, support vaccination catch-up.',
                                   'discussion': 'Reportable disease pathways.',
                                   'book_hint': 'Community/Public Health Nursing — Stanhope & '
                                                'Lancaster'}],
                         'medium': [{'title': 'Hypertension Screening Fair',
                                     'stem': 'Community BP screening finds 180/110 asymptomatic '
                                             'adult.',
                                     'question': 'Action?',
                                     'answer': 'Retake, assess symptoms, urgent referral/ED if '
                                               'indicated; do not ignore.',
                                     'discussion': 'Severe HTN needs prompt care.',
                                     'book_hint': 'Community/Public Health Nursing — Stanhope & '
                                                  'Lancaster'}],
                         'hard': [{'title': 'Flood Shelter',
                                   'stem': 'Nurse in shelter; elderly with chest pain and dyspnea.',
                                   'question': 'Triage priority?',
                                   'answer': 'Immediate/red — cardiac emergency; activate EMS.',
                                   'discussion': 'Disaster still uses ABC priorities for '
                                                 'individuals.',
                                   'book_hint': 'Community/Public Health Nursing — Stanhope & '
                                                'Lancaster'}],
                         'extreme': [{'title': 'Measles Exposure',
                                      'stem': 'Unvaccinated pregnant nurse exposed to measles.',
                                      'question': 'Action?',
                                      'answer': 'Occupational health immediately; follow '
                                                'post-exposure protocol; work restrictions as '
                                                'advised.',
                                      'discussion': 'Protect nurse and patients.',
                                      'book_hint': 'Community/Public Health Nursing — Stanhope & '
                                                   'Lancaster'}]}},
 'critical_care': {'label': 'Critical Care Nursing',
                   'books': ['Critical Care Nursing — Urden',
                             'AACN Essentials of Critical Care Nursing',
                             'ACLS/PALS references'],
                   'pdf_notes': ['Treat the patient, not only the alarm (DOPE for vents).',
                                 'Shock: ABC, access, oxygen, protocolized care.',
                                 'Lung-protective ventilation themes in ARDS.',
                                 'Neuro: ICP precautions and clustering care wisely.',
                                 'High-alert drips need careful titration and double-checks.'],
                   'questions': {'easy': [{'question': 'Normal adult SpO2 target often roughly?',
                                           'options': ['A) Generally ≥94% unless COPD/target '
                                                       'ordered differently',
                                                       'B) Always 70%',
                                                       'C) Always 40%',
                                                       'D) Ignore SpO2'],
                                           'answer': 'A) Generally ≥94% unless COPD/target ordered '
                                                     'differently',
                                           'explanation': 'Follow ordered targets.'},
                                          {'question': 'Arterial line zeroing is done at?',
                                           'options': ['A) Phlebostatic axis (approx 4th ICS '
                                                       'midaxillary)',
                                                       'B) Top of head',
                                                       'C) Foot',
                                                       'D) IV pole random height'],
                                           'answer': 'A) Phlebostatic axis (approx 4th ICS '
                                                     'midaxillary)',
                                           'explanation': 'Accurate BP.'},
                                          {'question': 'VAP prevention bundle includes?',
                                           'options': ['A) HOB elevation, oral care, sedation '
                                                       'vacation themes as protocol',
                                                       'B) Keep flat always',
                                                       'C) Skip oral care',
                                                       'D) Never assess readiness to wean'],
                                           'answer': 'A) HOB elevation, oral care, sedation '
                                                     'vacation themes as protocol',
                                           'explanation': 'Bundle care.'}],
                                 'medium': [{'question': 'CVP roughly reflects?',
                                             'options': ['A) Right atrial pressure / preload '
                                                         'estimate',
                                                         'B) Only left ventricular EF always exact',
                                                         'C) Only urine color',
                                                         'D) Only temperature'],
                                             'answer': 'A) Right atrial pressure / preload '
                                                       'estimate',
                                             'explanation': 'Interpret with trends.'},
                                            {'question': 'Increased ICP nursing measures include?',
                                             'options': ['A) HOB elevation as ordered, head '
                                                         'midline, avoid clustering care, treat '
                                                         'pain/fever',
                                                         'B) Trendelenburg always',
                                                         'C) Force cough frequently',
                                                         'D) Hypotonic free water boluses blindly'],
                                             'answer': 'A) HOB elevation as ordered, head midline, '
                                                       'avoid clustering care, treat pain/fever',
                                             'explanation': 'Neuroprotective.'},
                                            {'question': 'Shock first nursing priorities?',
                                             'options': ['A) ABC, IV access, oxygen, identify '
                                                         'type, follow protocols',
                                                         'B) Oral diet first',
                                                         'C) Ambulate immediately',
                                                         'D) Ignore lactate'],
                                             'answer': 'A) ABC, IV access, oxygen, identify type, '
                                                       'follow protocols',
                                             'explanation': 'Minutes matter.'}],
                                 'hard': [{'question': 'A junior colleague asks for the single '
                                                       'best answer. ARDS ventilation theme? '
                                                       'Beware of near-miss distractors.',
                                           'options': ['A) Lung-protective low tidal volume '
                                                       'strategies',
                                                       'B) Very high TV always best',
                                                       'C) Ignore plateau pressures',
                                                       'D) No PEEP ever'],
                                           'answer': 'A) Lung-protective low tidal volume '
                                                     'strategies',
                                           'explanation': 'Reduce VILI.'},
                                          {'question': 'A junior colleague asks for the single '
                                                       'best answer. Cardiac tamponade classic? '
                                                       'Beware of near-miss distractors.',
                                           'options': ['A) Hypotension, JVD, muffled sounds / '
                                                       'pulsus — emergency',
                                                       'B) Only mild cough',
                                                       'C) Always benign',
                                                       'D) Only ankle edema'],
                                           'answer': 'A) Hypotension, JVD, muffled sounds / pulsus '
                                                     '— emergency',
                                           'explanation': 'Pericardiocentesis path.'},
                                          {'question': 'A junior colleague asks for the single '
                                                       'best answer. DKA nursing priorities? '
                                                       'Beware of near-miss distractors.',
                                           'options': ['A) Fluids, insulin protocol, electrolyte '
                                                       '(K+) monitoring',
                                                       'B) Stop all fluids forever',
                                                       'C) Only SQ insulin home dose blindly',
                                                       'D) Ignore K'],
                                           'answer': 'A) Fluids, insulin protocol, electrolyte '
                                                     '(K+) monitoring',
                                           'explanation': 'K before/while insulin carefully.'}],
                                 'extreme': [{'question': 'In a high-stakes nursing scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Pulseless VT/VF? Avoid '
                                                          'actions that could harm if a critical '
                                                          'risk remains open.',
                                              'options': ['A) Defibrillate + high-quality CPR per '
                                                          'ACLS',
                                                          'B) Only atropine forever first',
                                                          'C) Wait for family meeting first',
                                                          'D) No CPR if intubated'],
                                              'answer': 'A) Defibrillate + high-quality CPR per '
                                                        'ACLS',
                                              'explanation': 'Shockable rhythms.'},
                                             {'question': 'In a high-stakes nursing scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Massive transfusion '
                                                          'nursing priorities? Avoid actions that '
                                                          'could harm if a critical risk remains '
                                                          'open.',
                                              'options': ['A) ABC, large-bore access, warmer, '
                                                          'protocol ratios, watch '
                                                          'citrate/hypocalcemia/hyperK themes',
                                                          'B) Tiny 22G only forever',
                                                          'C) Cold blood rapid without monitoring',
                                                          'D) Ignore coagulopathy'],
                                              'answer': 'A) ABC, large-bore access, warmer, '
                                                        'protocol ratios, watch '
                                                        'citrate/hypocalcemia/hyperK themes',
                                              'explanation': 'Trauma/ICU hemorrhage.'},
                                             {'question': 'In a high-stakes nursing scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Brain death testing '
                                                          'nursing role? Avoid actions that could '
                                                          'harm if a critical risk remains open.',
                                              'options': ['A) Support protocol, family '
                                                          'communication with team, maintain donor '
                                                          'care if applicable',
                                                          'B) Declare alone without criteria',
                                                          'C) Stop all documentation',
                                                          'D) Argue with family alone'],
                                              'answer': 'A) Support protocol, family communication '
                                                        'with team, maintain donor care if '
                                                        'applicable',
                                              'explanation': 'Policy-driven.'}]},
                   'cases': {'easy': [{'title': 'Desaturation on Vent',
                                       'stem': 'Vent alarms; SpO2 falling.',
                                       'question': 'First actions?',
                                       'answer': 'Look at patient (not only alarm), bag if needed, '
                                                 'suction/check tube, call help.',
                                       'discussion': 'DOPE mnemonic themes.',
                                       'book_hint': 'Critical Care Nursing — Urden / AACN '
                                                    'essentials'}],
                             'medium': [{'title': 'Septic Shock Pressors',
                                         'stem': 'After fluids, MAP still low; norepinephrine '
                                                 'started.',
                                         'question': 'Nursing focus?',
                                         'answer': 'Titrate to MAP goal, monitor perfusion/urine, '
                                                   'watch extravasation, escalate.',
                                         'discussion': 'Surviving sepsis ICU role.',
                                         'book_hint': 'Critical Care Nursing — Urden / AACN '
                                                      'essentials'}],
                             'hard': [{'title': 'Rising Peak Pressures',
                                       'stem': 'Intubated patient; high peak pressures, unequal '
                                               'breath sounds suddenly.',
                                       'question': 'Concern?',
                                       'answer': 'Pneumothorax/DOPE — disconnect/bag, assess, '
                                                 'urgent CXR/needle decompression readiness.',
                                       'discussion': 'Life-threatening.',
                                       'book_hint': 'Critical Care Nursing — Urden / AACN '
                                                    'essentials'}],
                             'extreme': [{'title': 'Anaphylactic Shock ICU',
                                          'stem': 'IV contrast; sudden hypotension, wheeze, rash.',
                                          'question': 'Priority?',
                                          'answer': 'Stop infusion, epinephrine per protocol, '
                                                    'airway, fluids, call help.',
                                          'discussion': 'Seconds count.',
                                          'book_hint': 'Critical Care Nursing — Urden / AACN '
                                                       'essentials'}]}},
 'pharm_nursing': {'label': 'Pharmacology for Nurses',
                   'books': ["Lehne's Pharmacology for Nursing Care",
                             'Nursing pharmacology review books',
                             'High-alert medication policies'],
                   'pdf_notes': ['Rights of medication administration every time.',
                                 'Never IV push potassium.',
                                 'Independent double-checks for high-alert drugs.',
                                 'Know hold parameters (digoxin, antihypertensives, insulin).',
                                 'Teach anticoagulants, opioids, and insulin safety.'],
                   'questions': {'easy': [{'question': 'Five (plus) rights of medication include?',
                                           'options': ['A) Patient, drug, dose, route, time (+ '
                                                       'documentation/reason/response)',
                                                       'B) Right roommate guess',
                                                       'C) Right color of pill only',
                                                       'D) Right bed number alone'],
                                           'answer': 'A) Patient, drug, dose, route, time (+ '
                                                     'documentation/reason/response)',
                                           'explanation': 'Safety core.'},
                                          {'question': 'Before giving digoxin, nurse often checks?',
                                           'options': ['A) Apical pulse / hold parameters per '
                                                       'order',
                                                       'B) Only hair color',
                                                       'C) Only shoe size',
                                                       'D) Never pulse'],
                                           'answer': 'A) Apical pulse / hold parameters per order',
                                           'explanation': 'Bradycardia risk.'},
                                          {'question': 'IM injection angle typically?',
                                           'options': ['A) 90 degrees',
                                                       'B) 10 degrees always only',
                                                       'C) 180 degrees into bone',
                                                       'D) Parallel to skin forever'],
                                           'answer': 'A) 90 degrees',
                                           'explanation': 'Technique basics.'}],
                                 'medium': [{'question': 'Warfarin teaching includes?',
                                             'options': ['A) Consistent vitamin K intake, INR '
                                                         'monitoring, bleed precautions',
                                                         'B) Double dose if missed yesterday '
                                                         'always without advice',
                                                         'C) Ignore black stools',
                                                         'D) Take with mega vitamin K swings '
                                                         'daily'],
                                             'answer': 'A) Consistent vitamin K intake, INR '
                                                       'monitoring, bleed precautions',
                                             'explanation': 'Anticoag safety.'},
                                            {'question': 'IV push opioids require?',
                                             'options': ['A) Slow administration per policy, '
                                                         'monitor RR/sedation, naloxone readiness',
                                                         'B) Push as fast as possible always',
                                                         'C) No monitoring',
                                                         'D) Leave room immediately forever'],
                                             'answer': 'A) Slow administration per policy, monitor '
                                                       'RR/sedation, naloxone readiness',
                                             'explanation': 'Respiratory depression risk.'},
                                            {'question': 'Insulin mixing clear-to-cloudy theme?',
                                             'options': ['A) Draw clear (regular) before cloudy '
                                                         '(NPH) if mixing allowed',
                                                         'B) Shake NPH violently always preferred '
                                                         'over roll',
                                                         'C) Share pens between patients',
                                                         'D) Skip site rotation'],
                                             'answer': 'A) Draw clear (regular) before cloudy '
                                                       '(NPH) if mixing allowed',
                                             'explanation': 'Know institutional policy.'}],
                                 'hard': [{'question': 'A junior colleague asks for the single '
                                                       'best answer. High-alert meds include '
                                                       'examples like? Beware of near-miss '
                                                       'distractors.',
                                           'options': ['A) Insulin, anticoagulants, opioids, '
                                                       'concentrated electrolytes',
                                                       'B) Only multivitamins',
                                                       'C) Only topical lotion',
                                                       'D) Only normal saline bags always'],
                                           'answer': 'A) Insulin, anticoagulants, opioids, '
                                                     'concentrated electrolytes',
                                           'explanation': 'Independent double-checks.'},
                                          {'question': 'A junior colleague asks for the single '
                                                       'best answer. Vancomycin red man syndrome '
                                                       'related to? Beware of near-miss '
                                                       'distractors.',
                                           'options': ['A) Rapid infusion — slow rate; not true '
                                                       'IgE allergy always',
                                                       'B) Always anaphylaxis only forever',
                                                       'C) Ignore flushing',
                                                       'D) Speed up infusion'],
                                           'answer': 'A) Rapid infusion — slow rate; not true IgE '
                                                     'allergy always',
                                           'explanation': 'Rate-related.'},
                                          {'question': 'A junior colleague asks for the single '
                                                       'best answer. Potassium IV concentrated '
                                                       'must? Beware of near-miss distractors.',
                                           'options': ['A) Never IV push; dilute/infuse per policy '
                                                       'with monitoring',
                                                       'B) IV push undiluted always OK',
                                                       'C) Give IM potassium',
                                                       'D) Ignore rate'],
                                           'answer': 'A) Never IV push; dilute/infuse per policy '
                                                     'with monitoring',
                                           'explanation': 'Lethal if pushed.'}],
                                 'extreme': [{'question': 'In a high-stakes nursing scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Suspect malignant '
                                                          'hyperthermia after anesthesia trigger? '
                                                          'Avoid actions that could harm if a '
                                                          'critical risk remains open.',
                                              'options': ['A) Call MH protocol, dantrolene '
                                                          'readiness, stop triggers, cool/support',
                                                          'B) Give more succinylcholine',
                                                          'C) Ignore rising ETCO2/fever',
                                                          'D) Only oral fluids'],
                                              'answer': 'A) Call MH protocol, dantrolene '
                                                        'readiness, stop triggers, cool/support',
                                              'explanation': 'Crisis.'},
                                             {'question': 'In a high-stakes nursing scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Opioid overdose with RR '
                                                          '4? Avoid actions that could harm if a '
                                                          'critical risk remains open.',
                                              'options': ['A) Stimulate, support ventilation, '
                                                          'naloxone per protocol',
                                                          'B) More opioid',
                                                          'C) Leave alone to sleep it off',
                                                          'D) Only document later'],
                                              'answer': 'A) Stimulate, support ventilation, '
                                                        'naloxone per protocol',
                                              'explanation': 'ABC + antidote.'},
                                             {'question': 'In a high-stakes nursing scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Chemotherapy '
                                                          'extravasation? Avoid actions that could '
                                                          'harm if a critical risk remains open.',
                                              'options': ['A) Stop infusion, follow vesicant '
                                                          'protocol, do not ignore pain/swelling '
                                                          'at site',
                                                          'B) Increase rate',
                                                          'C) Ignore',
                                                          'D) Hot pack blindly for all agents'],
                                              'answer': 'A) Stop infusion, follow vesicant '
                                                        'protocol, do not ignore pain/swelling at '
                                                        'site',
                                              'explanation': 'Agent-specific protocols.'}]},
                   'cases': {'easy': [{'title': 'Allergy Bracelet',
                                       'stem': 'Patient allergic to penicillin; order for '
                                               'amoxicillin arrives.',
                                       'question': 'Action?',
                                       'answer': 'Hold, clarify with provider/pharmacy, do not '
                                                 'administer.',
                                       'discussion': 'Allergy safety.',
                                       'book_hint': 'Pharmacology: A Patient-Centered Nursing '
                                                    'Approach / Lehne'}],
                             'medium': [{'title': 'Wrong Dose Caught',
                                         'stem': 'Pharmacy sent 10× dose; nurse notices before '
                                                 'giving.',
                                         'question': 'Action?',
                                         'answer': 'Do not give; verify with pharmacy/provider; '
                                                   'report near miss.',
                                         'discussion': 'Second check saves lives.',
                                         'book_hint': 'Pharmacology: A Patient-Centered Nursing '
                                                      'Approach / Lehne'}],
                             'hard': [{'title': 'Heparin Infusion',
                                       'stem': 'aPTT supra-therapeutic; oozing IV sites.',
                                       'question': 'Action?',
                                       'answer': 'Hold/adjust per protocol, notify, assess '
                                                 'bleeding, prepare reversal if ordered.',
                                       'discussion': 'Anticoag emergency readiness.',
                                       'book_hint': 'Pharmacology: A Patient-Centered Nursing '
                                                    'Approach / Lehne'}],
                             'extreme': [{'title': 'Concentrated Electrolyte',
                                          'stem': 'New nurse about to IV push KCl from vial.',
                                          'question': 'Intervention?',
                                          'answer': 'Stop immediately — educate, report, follow '
                                                    'high-alert policy.',
                                          'discussion': 'Never IV push KCl.',
                                          'book_hint': 'Pharmacology: A Patient-Centered Nursing '
                                                       'Approach / Lehne'}]}},
 'ethics_leadership': {'label': 'Ethics & Leadership',
                       'books': ['Nursing Ethics texts',
                                 'Professional nursing practice books',
                                 'Facility policy / nurse practice act summaries'],
                       'pdf_notes': ['Autonomy, beneficence, nonmaleficence, justice.',
                                     'Confidentiality — no elevator or social media PHI.',
                                     'Advocate and use chain of command for safety.',
                                     'Refuse falsified documentation; report impaired practice.',
                                     'Incident reports improve systems.'],
                       'questions': {'easy': [{'question': 'Autonomy means?',
                                               'options': ["A) Respect patient's right to make "
                                                           'informed decisions',
                                                           'B) Nurse decides everything always',
                                                           'C) Hide all information',
                                                           'D) Force treatment always'],
                                               'answer': "A) Respect patient's right to make "
                                                         'informed decisions',
                                               'explanation': 'Core bioethics.'},
                                              {'question': 'Beneficence means?',
                                               'options': ['A) Act to benefit the patient',
                                                           'B) Do harm for convenience',
                                                           'C) Ignore needs',
                                                           'D) Only protect institution always'],
                                               'answer': 'A) Act to benefit the patient',
                                               'explanation': 'Do good.'},
                                              {'question': 'Confidentiality breach example?',
                                               'options': ['A) Discussing patient details in '
                                                           'elevator with strangers',
                                                           'B) Hand-off in private with care team',
                                                           'C) Charting accurately',
                                                           'D) Encrypted official communication'],
                                               'answer': 'A) Discussing patient details in '
                                                         'elevator with strangers',
                                               'explanation': 'HIPAA-like duties.'}],
                                     'medium': [{'question': 'Nonmaleficence means?',
                                                 'options': ['A) Do no harm',
                                                             'B) Always maximize billing',
                                                             'C) Hide errors',
                                                             'D) Ignore safety'],
                                                 'answer': 'A) Do no harm',
                                                 'explanation': 'Avoid harm.'},
                                                {'question': 'Justice in nursing relates to?',
                                                 'options': ['A) Fair allocation of care/resources',
                                                             'B) Prefer friends only',
                                                             'C) Skip poor patients',
                                                             'D) Only VIP care'],
                                                 'answer': 'A) Fair allocation of care/resources',
                                                 'explanation': 'Equity.'},
                                                {'question': 'Incident report purpose?',
                                                 'options': ['A) Quality improvement / risk '
                                                             'reduction — factual, not punitive '
                                                             'chart blame essay',
                                                             'B) Punish only',
                                                             'C) Copy into public social media',
                                                             'D) Skip facts'],
                                                 'answer': 'A) Quality improvement / risk '
                                                           'reduction — factual, not punitive '
                                                           'chart blame essay',
                                                 'explanation': 'Report near misses too.'}],
                                     'hard': [{'question': 'A junior colleague asks for the single '
                                                           'best answer. Advocacy means? Beware of '
                                                           'near-miss distractors.',
                                               'options': ['A) Speak/act to protect patient rights '
                                                           'and best interests',
                                                           'B) Silence when unsafe orders given',
                                                           'C) Prioritize convenience over safety',
                                                           'D) Hide information patient needs'],
                                               'answer': 'A) Speak/act to protect patient rights '
                                                         'and best interests',
                                               'explanation': 'Core professional duty.'},
                                              {'question': 'A junior colleague asks for the single '
                                                           'best answer. Informed consent nurse '
                                                           'role often? Beware of near-miss '
                                                           'distractors.',
                                               'options': ['A) Witness signature, verify '
                                                           'understanding, notify provider if '
                                                           'questions remain',
                                                           'B) Explain surgical risks instead of '
                                                           'surgeon always alone as only explainer',
                                                           'C) Force signing',
                                                           'D) Skip interpreter when needed'],
                                               'answer': 'A) Witness signature, verify '
                                                         'understanding, notify provider if '
                                                         'questions remain',
                                               'explanation': 'Communication access matters.'},
                                              {'question': 'A junior colleague asks for the single '
                                                           'best answer. Moral distress occurs '
                                                           'when? Beware of near-miss distractors.',
                                               'options': ['A) Nurse knows right action but '
                                                           'constrained from taking it',
                                                           'B) Always vacation joy',
                                                           'C) Only overtime pay issues',
                                                           'D) Never in nursing'],
                                               'answer': 'A) Nurse knows right action but '
                                                         'constrained from taking it',
                                               'explanation': 'Seek ethics support.'}],
                                     'extreme': [{'question': 'In a high-stakes nursing scenario '
                                                              'with incomplete data, which '
                                                              'statement is MOST correct? '
                                                              'Whistleblowing about ongoing '
                                                              'patient harm? Avoid actions that '
                                                              'could harm if a critical risk '
                                                              'remains open.',
                                                  'options': ['A) Report through required '
                                                              'channels; patient safety overrides '
                                                              'loyalty to cover-ups',
                                                              'B) Destroy evidence',
                                                              'C) Post PHI publicly',
                                                              'D) Ignore deaths'],
                                                  'answer': 'A) Report through required channels; '
                                                            'patient safety overrides loyalty to '
                                                            'cover-ups',
                                                  'explanation': 'Follow law/policy.'},
                                                 {'question': 'In a high-stakes nursing scenario '
                                                              'with incomplete data, which '
                                                              'statement is MOST correct? DNR '
                                                              'order conflict at bedside? Avoid '
                                                              'actions that could harm if a '
                                                              'critical risk remains open.',
                                                  'options': ['A) Clarify current valid order with '
                                                              'team; do not perform unwanted '
                                                              'resuscitation if valid DNR',
                                                              'B) Ignore DNR always',
                                                              'C) Hide order',
                                                              'D) Argue alone without chain of '
                                                              'command'],
                                                  'answer': 'A) Clarify current valid order with '
                                                            'team; do not perform unwanted '
                                                            'resuscitation if valid DNR',
                                                  'explanation': 'Know policy.'},
                                                 {'question': 'In a high-stakes nursing scenario '
                                                              'with incomplete data, which '
                                                              'statement is MOST correct? Social '
                                                              'media photo of patient? Avoid '
                                                              'actions that could harm if a '
                                                              'critical risk remains open.',
                                                  'options': ['A) Never — confidentiality/privacy '
                                                              'violation',
                                                              'B) OK if face blurred sometimes '
                                                              'without consent always',
                                                              'C) OK in stories',
                                                              'D) OK if funny'],
                                                  'answer': 'A) Never — confidentiality/privacy '
                                                            'violation',
                                                  'explanation': 'Professional boundaries.'}]},
                       'cases': {'easy': [{'title': 'Refusing Treatment',
                                           'stem': 'Alert competent adult refuses transfusion for '
                                                   'religious reasons.',
                                           'question': 'Nursing role?',
                                           'answer': 'Ensure informed refusal documented; respect '
                                                     'autonomy; notify team; support care within '
                                                     'limits.',
                                           'discussion': 'Do not coerce.',
                                           'book_hint': 'Nursing Ethics / Professional Nursing '
                                                        'practice texts'}],
                                 'medium': [{'title': 'Impaired Colleague',
                                             'stem': 'Smell alcohol on nurse starting shift.',
                                             'question': 'Action?',
                                             'answer': 'Follow policy — remove from patient care, '
                                                       'notify supervisor; patient safety first.',
                                             'discussion': 'Do not cover up.',
                                             'book_hint': 'Nursing Ethics / Professional Nursing '
                                                          'practice texts'}],
                                 'hard': [{'title': 'Unsafe Staffing',
                                           'stem': 'Assignment exceeds safe capacity with unstable '
                                                   'patients.',
                                           'question': 'Action?',
                                           'answer': 'Use chain of command, document concerns, '
                                                     'prioritize ABCs, do not abandon patients.',
                                           'discussion': 'Safe harbor/policy pathways vary by '
                                                         'region.',
                                           'book_hint': 'Nursing Ethics / Professional Nursing '
                                                        'practice texts'}],
                                 'extreme': [{'title': 'Falsified Documentation',
                                              'stem': 'Peer asks you to chart assessments they did '
                                                      'not perform.',
                                              'question': 'Response?',
                                              'answer': 'Refuse; report per policy; never falsify '
                                                        'records.',
                                              'discussion': 'Integrity and legal risk.',
                                              'book_hint': 'Nursing Ethics / Professional Nursing '
                                                           'practice texts'}]}},
 'geriatrics': {'label': 'Geriatric Nursing',
                'books': ['Gerontological Nursing — Touhy & Jett',
                          'Eliopoulos Gerontological Nursing',
                          'Beers Criteria summaries'],
                'pdf_notes': ['Infection may present as confusion without fever.',
                              'Polypharmacy and Beers Criteria awareness.',
                              'Delirium is acute — seek reversible causes.',
                              'Fall and pressure-injury prevention bundles.',
                              'Report suspected elder abuse.'],
                'questions': {'easy': [{'question': 'Common atypical infection sign in elderly?',
                                        'options': ['A) Confusion / falls / functional decline '
                                                    '(fever may be absent)',
                                                    'B) Only classic high fever always',
                                                    'C) Only sore throat always',
                                                    'D) Never changes mentation'],
                                        'answer': 'A) Confusion / falls / functional decline '
                                                  '(fever may be absent)',
                                        'explanation': 'Atypical presentations.'},
                                       {'question': 'Polypharmacy risk includes?',
                                        'options': ['A) Interactions, falls, ADRs',
                                                    'B) Only benefits forever',
                                                    'C) No need for med review',
                                                    'D) Always safe if OTC'],
                                        'answer': 'A) Interactions, falls, ADRs',
                                        'explanation': 'Brown-bag reviews help.'},
                                       {'question': 'Pressure injury prevention includes?',
                                        'options': ['A) Repositioning, skin care, nutrition, '
                                                    'pressure-relieving surfaces',
                                                    'B) Keep wet linen',
                                                    'C) Massage reddened bony areas hard always',
                                                    'D) Ignore mobility'],
                                        'answer': 'A) Repositioning, skin care, nutrition, '
                                                  'pressure-relieving surfaces',
                                        'explanation': 'Skin integrity.'}],
                              'medium': [{'question': 'Beers Criteria relate to?',
                                          'options': ['A) Potentially inappropriate medications in '
                                                      'older adults',
                                                      'B) Only pediatric dosing',
                                                      'C) Only veterinary meds',
                                                      'D) Only IV fluids'],
                                          'answer': 'A) Potentially inappropriate medications in '
                                                    'older adults',
                                          'explanation': 'Deprescribing awareness.'},
                                         {'question': 'Orthostatic hypotension nursing tip?',
                                          'options': ['A) Dangle, rise slowly, monitor BP '
                                                      'lying/standing',
                                                      'B) Jump out of bed fast always',
                                                      'C) Ignore dizziness',
                                                      'D) Fluid restrict always'],
                                          'answer': 'A) Dangle, rise slowly, monitor BP '
                                                    'lying/standing',
                                          'explanation': 'Fall prevention.'},
                                         {'question': 'Delirium vs dementia key?',
                                          'options': ['A) Delirium acute/fluctuating often '
                                                      'reversible cause; dementia chronic '
                                                      'progressive',
                                                      'B) Delirium always permanent',
                                                      'C) Dementia always starts in minutes',
                                                      'D) No difference'],
                                          'answer': 'A) Delirium acute/fluctuating often '
                                                    'reversible cause; dementia chronic '
                                                    'progressive',
                                          'explanation': 'Treat causes of delirium.'}],
                              'hard': [{'question': 'A junior colleague asks for the single best '
                                                    'answer. Elder abuse nurse duty? Beware of '
                                                    'near-miss distractors.',
                                        'options': ['A) Report suspected abuse per law/policy',
                                                    'B) Ignore bruises',
                                                    'C) Confront abuser alone unsafely always as '
                                                    'only step',
                                                    'D) Hide evidence'],
                                        'answer': 'A) Report suspected abuse per law/policy',
                                        'explanation': 'Mandatory reporting themes.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Restraint alternative for wander '
                                                    'risk? Beware of near-miss distractors.',
                                        'options': ['A) Supervision, alarms, toileting schedule, '
                                                    'meaningful activity — least restrictive',
                                                    'B) Tie to chair for convenience',
                                                    'C) Ignore elopement risk',
                                                    'D) Lock without assessment'],
                                        'answer': 'A) Supervision, alarms, toileting schedule, '
                                                  'meaningful activity — least restrictive',
                                        'explanation': 'Dignity + safety.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Heart failure in elderly nursing '
                                                    'weight tip? Beware of near-miss distractors.',
                                        'options': ['A) Same scale, same time, report gain per '
                                                    'parameters',
                                                    'B) Weigh weekly randomly clothed differently '
                                                    'always',
                                                    'C) Ignore 2 kg gain',
                                                    'D) Only estimate'],
                                        'answer': 'A) Same scale, same time, report gain per '
                                                  'parameters',
                                        'explanation': 'Fluid monitoring.'}],
                              'extreme': [{'question': 'In a high-stakes nursing scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Hip fracture post-fall priority? '
                                                       'Avoid actions that could harm if a '
                                                       'critical risk remains open.',
                                           'options': ['A) ABC, pain, immobilize as trained, '
                                                       'neurovascular checks, urgent ortho path',
                                                       'B) Force walk immediately',
                                                       'C) Ignore shortened rotated leg',
                                                       'D) Only give laxative'],
                                           'answer': 'A) ABC, pain, immobilize as trained, '
                                                     'neurovascular checks, urgent ortho path',
                                           'explanation': 'Common life-changing injury.'},
                                          {'question': 'In a high-stakes nursing scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Sepsis in frail elder may present '
                                                       'as? Avoid actions that could harm if a '
                                                       'critical risk remains open.',
                                           'options': ['A) Subtle confusion/weakness without high '
                                                       'fever — still urgent',
                                                       'B) Always classic fever only',
                                                       'C) Always well appearance',
                                                       'D) Never sepsis'],
                                           'answer': 'A) Subtle confusion/weakness without high '
                                                     'fever — still urgent',
                                           'explanation': 'Low threshold to escalate.'},
                                          {'question': 'In a high-stakes nursing scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Advance directive conflict at '
                                                       'EOL? Avoid actions that could harm if a '
                                                       'critical risk remains open.',
                                           'options': ['A) Follow valid patient wishes/legal '
                                                       'documents with ethics/team support',
                                                       'B) Nurse overrides alone always',
                                                       'C) Ignore proxy',
                                                       'D) Hide documents'],
                                           'answer': 'A) Follow valid patient wishes/legal '
                                                     'documents with ethics/team support',
                                           'explanation': 'Respect goals of care.'}]},
                'cases': {'easy': [{'title': 'New Confusion',
                                    'stem': '85-year-old newly confused; no fever noted.',
                                    'question': 'Priority differentials theme?',
                                    'answer': 'Infection, meds, hypoxia, electrolytes, pain, '
                                              'stroke — assess ABC and workup.',
                                    'discussion': 'Do not assume dementia only.',
                                    'book_hint': 'Gerontological Nursing — Touhy & Jett / '
                                                 'Eliopoulos'}],
                          'medium': [{'title': 'Fall at Night',
                                      'stem': 'Elderly patient found on floor; on benzos and '
                                              'antihypertensives.',
                                      'question': 'Actions?',
                                      'answer': 'ABC/injury assessment, notify, vitals, neuro '
                                                'check, review fall risk meds, do not move if '
                                                'injury suspected improperly.',
                                      'discussion': 'Post-fall protocol.',
                                      'book_hint': 'Gerontological Nursing — Touhy & Jett / '
                                                   'Eliopoulos'}],
                          'hard': [{'title': 'Digoxin Toxicity Clue',
                                    'stem': 'Elderly on digoxin: anorexia, visual changes, '
                                            'bradycardia.',
                                    'question': 'Action?',
                                    'answer': 'Hold digoxin, notify, check level/electrolytes.',
                                    'discussion': 'Narrow TI + renal aging.',
                                    'book_hint': 'Gerontological Nursing — Touhy & Jett / '
                                                 'Eliopoulos'}],
                          'extreme': [{'title': 'Suspected Elder Abuse',
                                       'stem': 'Nursing home resident with patterned bruises; '
                                               'fearful with one visitor.',
                                       'question': 'Action?',
                                       'answer': 'Ensure safety, report per mandatory laws, '
                                                 'document objectively, involve social work/APS as '
                                                 'required.',
                                       'discussion': 'Do not delay reporting.',
                                       'book_hint': 'Gerontological Nursing — Touhy & Jett / '
                                                    'Eliopoulos'}]}}}

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
        f"💡 {item['explanation']}\n\n"
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
        "🔬 *CharaNas Nursing Bot*\n"
        "Undergraduate Nursing\n\n"
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
