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
                                          'options': ['A) Daily weight, intake/output, and bowel '
                                                      'pattern only',
                                                      'B) Temperature, pulse, respiration, blood '
                                                      'pressure (± SpO2/pain)',
                                                      'C) Only continuous ECG monitoring without '
                                                      'other measures',
                                                      'D) Pupil size and Glasgow Coma Scale alone'],
                                          'answer': 'B) Temperature, pulse, respiration, blood '
                                                    'pressure (± SpO2/pain)',
                                          'explanation': 'Vital signs reflect core physiologic '
                                                         'functions of thermoregulation, cardiac '
                                                         'output, ventilatory status, and vascular '
                                                         'tone. Temperature, pulse, respiration, '
                                                         'and blood pressure—often with SpO2 and '
                                                         'pain—form the baseline data nurses use '
                                                         'to detect early deterioration. Trends '
                                                         'over time are more informative than '
                                                         'isolated values because compensatory '
                                                         'mechanisms can temporarily mask '
                                                         'illness.'},
                                         {'question': 'Hand hygiene is primarily to?',
                                          'options': ['A) Replace sterile technique for all '
                                                      'invasive procedures',
                                                      'B) Eliminate the need for gloves during '
                                                      'wound care',
                                                      'C) Reduce pathogen transmission',
                                                      'D) Be performed only at discharge teaching'],
                                          'answer': 'C) Reduce pathogen transmission',
                                          'explanation': 'Transient microorganisms on the hands '
                                                         'are a major vehicle for '
                                                         'healthcare-associated infection. Hand '
                                                         'hygiene mechanically and chemically '
                                                         'reduces microbial load before and after '
                                                         'patient contact, interrupting '
                                                         'cross-transmission. Gloves do not '
                                                         'replace hand hygiene because '
                                                         'contamination of hands and glove '
                                                         'surfaces still occurs during care.'},
                                         {'question': 'Informed consent requires?',
                                          'options': ['A) Nurse signature alone without patient '
                                                      'explanation',
                                                      'B) Family agreement even if the patient '
                                                      'refuses',
                                                      'C) Verbal assent without documenting the '
                                                      'discussion',
                                                      'D) Understanding of procedure, risks, '
                                                      'alternatives, voluntary agreement'],
                                          'answer': 'D) Understanding of procedure, risks, '
                                                    'alternatives, voluntary agreement',
                                          'explanation': 'Informed consent is valid only when the '
                                                         'patient understands the nature of the '
                                                         'procedure, its material risks and '
                                                         'benefits, and reasonable alternatives, '
                                                         'and then agrees voluntarily without '
                                                         'coercion. The provider performing the '
                                                         'procedure retains responsibility for '
                                                         'disclosure; the nurse commonly witnesses '
                                                         'the signature and advocates if '
                                                         'comprehension appears incomplete. '
                                                         'Documentation preserves the ethical and '
                                                         'legal record of that process.'}],
                                'medium': [{'question': 'Best time to assess pain after IV opioid '
                                                        'roughly?',
                                            'options': ['A) At expected peak effect (often ~15–30 '
                                                        'min; follow policy/drug)',
                                                        'B) Only after 4–6 hours for all IV '
                                                        'opioids',
                                                        'C) Immediately before the next scheduled '
                                                        'oral dose only',
                                                        'D) Once at discharge when completing the '
                                                        'pain summary'],
                                            'answer': 'A) At expected peak effect (often ~15–30 '
                                                      'min; follow policy/drug)',
                                            'explanation': 'Intravenous opioids reach peak plasma '
                                                           'and central nervous system effect '
                                                           'relatively quickly, often within about '
                                                           '15–30 minutes depending on the agent '
                                                           'and patient factors. Reassessment at '
                                                           'that interval evaluates analgesic '
                                                           'efficacy and detects adverse effects '
                                                           'such as respiratory depression, '
                                                           'sedation, and hypotension. Ongoing '
                                                           'titration depends on both subjective '
                                                           'pain report and objective vital-sign '
                                                           'changes.'},
                                           {'question': 'Fall risk interventions include?',
                                            'options': ['A) Keep the bed in the highest position '
                                                        'for easier transfers',
                                                        'B) Call light in reach, non-slip '
                                                        'footwear, bed low, assist as needed',
                                                        'C) Remove assistive devices so the '
                                                        'patient walks independently sooner',
                                                        'D) Encourage unassisted toileting at '
                                                        'night to build confidence'],
                                            'answer': 'B) Call light in reach, non-slip footwear, '
                                                      'bed low, assist as needed',
                                            'explanation': 'Falls result from interacting '
                                                           'intrinsic factors (gait instability, '
                                                           'orthostasis, cognition, medications) '
                                                           'and extrinsic hazards (bed height, '
                                                           'footwear, unreachable call light). '
                                                           'Multifactorial prevention lowers fall '
                                                           'energy and frequency by keeping the '
                                                           'bed low, ensuring non-slip footwear, '
                                                           'placing the call light within reach, '
                                                           'and matching assistance to mobility '
                                                           'status. These measures reduce injury '
                                                           'risk without unnecessarily restricting '
                                                           'autonomy.'},
                                           {'question': 'Standard precautions apply to?',
                                            'options': ['A) Only patients in isolation rooms',
                                                        'B) Only surgical or immunocompromised '
                                                        'patients',
                                                        'C) All patients',
                                                        'D) Only patients with documented fever or '
                                                        'known infection'],
                                            'answer': 'C) All patients',
                                            'explanation': 'Standard precautions assume that blood '
                                                           'and body fluids from every patient may '
                                                           'contain bloodborne pathogens, '
                                                           'regardless of known diagnosis. '
                                                           'Consistent use of hand hygiene, '
                                                           'appropriate PPE, safe sharps handling, '
                                                           'and environmental cleaning protects '
                                                           'both patients and staff. '
                                                           'Transmission-based precautions are '
                                                           'added when a specific pathogen’s route '
                                                           'requires additional barriers.'}],
                                'hard': [{'question': 'Priority framework when multiple needs '
                                                      'compete?',
                                          'options': ['A) Complete all documentation before '
                                                      'addressing airway concerns',
                                                      'B) Address psychosocial needs before '
                                                      'physiologic threats',
                                                      'C) Finish routine hygiene tasks before '
                                                      'safety hazards',
                                                      'D) Airway/breathing/circulation and safety '
                                                      'before routine tasks'],
                                          'answer': 'D) Airway/breathing/circulation and safety '
                                                    'before routine tasks',
                                          'explanation': 'When multiple needs compete, threats to '
                                                         'airway patency, oxygenation, and '
                                                         'circulation produce the most immediate '
                                                         'risk of hypoxic brain injury and cardiac '
                                                         'arrest. Safety hazards that can cause '
                                                         'sudden harm (e.g., active bleeding, '
                                                         'falls from instability) likewise outrank '
                                                         'routine comfort or documentation tasks. '
                                                         'This physiologic hierarchy mirrors ABC '
                                                         'triage and Maslow’s prioritization of '
                                                         'survival needs.'},
                                         {'question': 'Restraint use requires?',
                                          'options': ['A) Least restrictive alternative, order, '
                                                      'monitoring, documentation',
                                                      'B) Application based on staff convenience '
                                                      'during busy shifts',
                                                      'C) Family request alone without clinical '
                                                      'assessment',
                                                      'D) Continuous use without scheduled '
                                                      'reassessment'],
                                          'answer': 'A) Least restrictive alternative, order, '
                                                    'monitoring, documentation',
                                          'explanation': 'Physical restraints can cause pressure '
                                                         'injury, circulatory compromise, '
                                                         'aspiration, psychological trauma, and '
                                                         'even death if misused. Ethical and '
                                                         'regulatory standards therefore require '
                                                         'the least restrictive effective '
                                                         'alternative, a time-limited order, '
                                                         'frequent monitoring, and clear '
                                                         'documentation of indication and '
                                                         'reassessment. Restraint is a controlled '
                                                         'safety intervention, not a convenience '
                                                         'measure.'},
                                         {'question': 'Medication right that prevents wrong '
                                                      'patient?',
                                          'options': ['A) Right room number as the sole identifier',
                                                      'B) Right patient (two identifiers)',
                                                      'C) Right bed location confirmed by staff '
                                                      'memory',
                                                      'D) Right roommate name verified verbally'],
                                          'answer': 'B) Right patient (two identifiers)',
                                          'explanation': 'Wrong-patient medication errors occur '
                                                         'when identity verification fails at the '
                                                         'point of administration. Using two '
                                                         'unique identifiers (such as name and '
                                                         'date of birth or medical record number) '
                                                         'links the ordered drug to the correct '
                                                         'person before the dose is given. This '
                                                         'right-patient check is foundational '
                                                         'because subsequent rights cannot correct '
                                                         'an identity mismatch.'}],
                                'extreme': [{'question': 'Unresponsive patient, no pulse — first '
                                                         'action?',
                                             'options': ['A) Obtain family consent before starting '
                                                         'compressions',
                                                         'B) Document a full note, then return to '
                                                         'start CPR',
                                                         'C) Start CPR / call emergency response '
                                                         'per protocol',
                                                         'D) Leave the room briefly to retrieve '
                                                         'the paper chart'],
                                             'answer': 'C) Start CPR / call emergency response per '
                                                       'protocol',
                                             'explanation': 'Pulseless unresponsiveness indicates '
                                                            'abrupt cessation of effective cardiac '
                                                            'output and cerebral perfusion. '
                                                            'Immediate high-quality CPR and '
                                                            'activation of the emergency response '
                                                            'restore circulation while advanced '
                                                            'interventions are prepared. Delaying '
                                                            'compressions for nonessential tasks '
                                                            'prolongs ischemic time and worsens '
                                                            'neurologic outcome.'},
                                            {'question': 'Suspected transfusion reaction '
                                                         'mid-transfusion?',
                                             'options': ['A) Increase the infusion rate to finish '
                                                         'the unit faster',
                                                         'B) Continue the transfusion and recheck '
                                                         'vitals in one hour',
                                                         'C) Discard the bag immediately without '
                                                         'notifying blood bank',
                                                         'D) Stop transfusion, keep IV line with '
                                                         'NS, assess, notify provider/blood bank'],
                                             'answer': 'D) Stop transfusion, keep IV line with NS, '
                                                       'assess, notify provider/blood bank',
                                             'explanation': 'Acute transfusion reactions may '
                                                            'involve hemolysis, anaphylaxis, '
                                                            'TRALI, or bacterial contamination, '
                                                            'all of which can progress rapidly '
                                                            'once antigen–antibody or inflammatory '
                                                            'cascades are underway. Stopping the '
                                                            'transfusion immediately limits '
                                                            'further exposure to the implicated '
                                                            'unit while maintaining IV access with '
                                                            'normal saline for resuscitation and '
                                                            'medication delivery. Concurrent '
                                                            'assessment and notification of the '
                                                            'provider and blood bank enable '
                                                            'laboratory workup and definitive '
                                                            'treatment.'},
                                            {'question': 'Fire on unit — RACE theme starts with?',
                                             'options': ['A) Rescue patients in immediate danger '
                                                         '(then alarm/contain/extinguish as '
                                                         'trained)',
                                                         'B) Secure charts and computers before '
                                                         'moving anyone',
                                                         'C) Finish distributing meal trays, then '
                                                         'investigate the alarm',
                                                         'D) Silence alarms first to reduce panic '
                                                         'on the unit'],
                                             'answer': 'A) Rescue patients in immediate danger '
                                                       '(then alarm/contain/extinguish as trained)',
                                             'explanation': 'In a unit fire, patients in the '
                                                            'immediate zone of danger face smoke '
                                                            'inhalation, thermal injury, and '
                                                            'hypoxia within minutes. The RACE '
                                                            'sequence begins with Rescue of those '
                                                            'at imminent risk, then Alarm, '
                                                            'Contain, and Extinguish/Evacuate as '
                                                            'trained, because human life takes '
                                                            'precedence over property. '
                                                            'Facility-specific fire plans '
                                                            'operationalize this sequence for '
                                                            'local exits and equipment.'}]},
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
                                      'options': ['A) Encourage ambulation on a treadmill to test '
                                                  'exertional pain',
                                                  'B) ABC, ECG access, oxygen if indicated, notify '
                                                  'promptly',
                                                  'C) Give an antacid first and observe for one '
                                                  'hour',
                                                  'D) Defer evaluation if pain radiates to the arm '
                                                  'or jaw'],
                                      'answer': 'B) ABC, ECG access, oxygen if indicated, notify '
                                                'promptly',
                                      'explanation': 'Acute coronary syndromes reflect myocardial '
                                                     'ischemia from plaque rupture, thrombosis, or '
                                                     'supply–demand mismatch, with rapidly '
                                                     'progressive myocyte necrosis. Early ECG '
                                                     'acquisition, ABC support, oxygen when '
                                                     'hypoxemic, and prompt team notification '
                                                     'shorten ischemic time and guide reperfusion '
                                                     'decisions. Nursing actions focus on '
                                                     'continuous monitoring for arrhythmias and '
                                                     'hemodynamic instability while preparing for '
                                                     'urgent therapy.'},
                                     {'question': 'Post-op incentive spirometry aims to?',
                                      'options': ['A) Replace the need for early ambulation after '
                                                  'surgery',
                                                  'B) Primarily relieve postoperative constipation',
                                                  'C) Prevent atelectasis / promote lung expansion',
                                                  'D) Lower blood pressure through vagal '
                                                  'stimulation'],
                                      'answer': 'C) Prevent atelectasis / promote lung expansion',
                                      'explanation': 'Postoperative shallow breathing and '
                                                     'diaphragmatic splinting promote alveolar '
                                                     'collapse (atelectasis), impairing gas '
                                                     'exchange and predisposing to pneumonia. '
                                                     'Incentive spirometry encourages sustained '
                                                     'maximal inspiration that re-expands alveoli '
                                                     'and mobilizes secretions. Combined with '
                                                     'early mobilization and coughing, it is a '
                                                     'core pulmonary hygiene strategy after '
                                                     'surgery.'},
                                     {'question': 'Hypoglycemia classic early signs?',
                                      'options': ['A) Hypertension and bradycardia as the earliest '
                                                  'cluster',
                                                  'B) Isolated pruritic rash without autonomic '
                                                  'signs',
                                                  'C) Polyuria and polydipsia as acute warning '
                                                  'signs',
                                                  'D) Sweating, tremor, confusion/hunger (vary)'],
                                      'answer': 'D) Sweating, tremor, confusion/hunger (vary)',
                                      'explanation': 'Neuroglycopenia and autonomic '
                                                     'counter-regulation produce the classic early '
                                                     'hypoglycemia cluster of diaphoresis, tremor, '
                                                     'hunger, and confusion as glucose delivery to '
                                                     'the brain falls. Prompt carbohydrate '
                                                     'replacement per protocol restores plasma '
                                                     'glucose before seizures or loss of '
                                                     'consciousness occur. Nurses also reassess '
                                                     'after treatment because rebound '
                                                     'hyperglycemia or recurrent hypoglycemia may '
                                                     'follow.'}],
                            'medium': [{'question': 'Heart failure weight gain overnight suggests?',
                                        'options': ['A) Fluid retention — assess and report',
                                                    'B) Expected muscle gain from bedrest recovery',
                                                    'C) Improved nutrition without fluid status '
                                                    'change',
                                                    'D) Measurement error that never requires '
                                                    'reporting'],
                                        'answer': 'A) Fluid retention — assess and report',
                                        'explanation': 'In heart failure, elevated venous '
                                                       'pressures and reduced renal perfusion '
                                                       'activate neurohormonal pathways that '
                                                       'promote sodium and water retention. '
                                                       'Overnight weight gain is therefore a '
                                                       'sensitive bedside marker of accumulating '
                                                       'intravascular and interstitial fluid '
                                                       'before frank pulmonary edema appears. '
                                                       'Reporting significant gains allows earlier '
                                                       'diuretic adjustment and congestion '
                                                       'assessment.'},
                                       {'question': 'NG tube placement confirmation gold standard?',
                                        'options': ['A) Air insufflation with auscultation alone '
                                                    'before first use',
                                                    'B) X-ray confirmation per policy before first '
                                                    'use',
                                                    "C) Patient report that the tube 'feels fine' "
                                                    'in the nose',
                                                    'D) Immediate feeding if gastric aspirate '
                                                    'looks clear'],
                                        'answer': 'B) X-ray confirmation per policy before first '
                                                  'use',
                                        'explanation': 'Blind nasogastric tube placement can '
                                                       'inadvertently enter the airway; feeding or '
                                                       'medication into a misplaced tube causes '
                                                       'chemical pneumonitis and aspiration '
                                                       'pneumonia. Radiographic confirmation per '
                                                       'policy before first use is the gold '
                                                       'standard because bedside cues alone are '
                                                       'insufficiently reliable. Correct placement '
                                                       'protects the airway–GI barrier during '
                                                       'enteral therapy.'},
                                       {'question': 'DVT prevention includes?',
                                        'options': ['A) Prolonged bedrest to protect surgical '
                                                    'incisions',
                                                    'B) Crossing legs tightly to improve venous '
                                                    'return',
                                                    'C) Early ambulation, prophylaxis as ordered, '
                                                    'leg exercises',
                                                    'D) Deferring calf pain assessment until '
                                                    'discharge'],
                                        'answer': 'C) Early ambulation, prophylaxis as ordered, '
                                                  'leg exercises',
                                        'explanation': 'Venous stasis, endothelial injury, and '
                                                       'hypercoagulability (Virchow’s triad) '
                                                       'intensify after surgery, raising deep-vein '
                                                       'thrombosis and pulmonary embolism risk. '
                                                       'Early ambulation, prescribed pharmacologic '
                                                       'prophylaxis, and leg exercises augment '
                                                       'venous return and blunt clot formation. '
                                                       'Nursing surveillance for calf pain, '
                                                       'swelling, and sudden dyspnea supports '
                                                       'timely escalation.'}],
                            'hard': [{'question': 'Sepsis early nursing recognition uses?',
                                      'options': ['A) Waiting for hypotension before considering '
                                                  'sepsis',
                                                  'B) Presence of a rash as the required '
                                                  'diagnostic clue',
                                                  'C) Normal mentation ruling out organ '
                                                  'dysfunction',
                                                  'D) Infection + organ dysfunction signs '
                                                  '(fever/hypothermia, tachypnea, altered '
                                                  'mentation, etc.)'],
                                      'answer': 'D) Infection + organ dysfunction signs '
                                                '(fever/hypothermia, tachypnea, altered mentation, '
                                                'etc.)',
                                      'explanation': 'Sepsis is life-threatening organ dysfunction '
                                                     'driven by a dysregulated host response to '
                                                     'infection, with microvascular leak, '
                                                     'vasodilation, and impaired tissue oxygen '
                                                     'use. Early clues include fever or '
                                                     'hypothermia, tachypnea, altered mentation, '
                                                     'and other signs of organ stress alongside a '
                                                     'suspected infectious source. Recognition at '
                                                     'this stage enables rapid fluids, cultures, '
                                                     'antimicrobials, and source control that '
                                                     'reduce mortality.'},
                                     {'question': 'COPD patient on high O2 becomes drowsy — '
                                                  'concern?',
                                      'options': ['A) CO2 retention / ventilatory failure risk — '
                                                  'assess ABG/notify',
                                                  'B) Need for still higher FiO2 without further '
                                                  'assessment',
                                                  'C) Expected sedation from oxygen that needs no '
                                                  'follow-up',
                                                  'D) Dehydration only — push oral fluids '
                                                  'aggressively'],
                                      'answer': 'A) CO2 retention / ventilatory failure risk — '
                                                'assess ABG/notify',
                                      'explanation': 'In some patients with advanced COPD, chronic '
                                                     'hypercapnia shifts ventilatory drive and '
                                                     'high uncontrolled oxygen can worsen V/Q '
                                                     'mismatch and CO2 retention, producing '
                                                     'progressive drowsiness and respiratory '
                                                     'acidosis. Nursing concern centers on '
                                                     'assessing ventilation, obtaining ABGs as '
                                                     'indicated, and notifying the provider rather '
                                                     'than assuming oxygen is always benign. '
                                                     'Oxygen is titrated to ordered saturation '
                                                     'targets while supporting work of breathing.'},
                                     {'question': 'Post-thyroidectomy emergency concern?',
                                      'options': ['A) Constipation from opioid analgesia as the '
                                                  'main emergency',
                                                  'B) Airway compromise / hematoma / hypocalcemia '
                                                  'themes',
                                                  'C) Delayed acneiform rash as the urgent airway '
                                                  'threat',
                                                  'D) Refractive vision change without airway '
                                                  'concern'],
                                      'answer': 'B) Airway compromise / hematoma / hypocalcemia '
                                                'themes',
                                      'explanation': 'After thyroidectomy, hematoma in a closed '
                                                     'neck space can rapidly compress the trachea, '
                                                     'and inadvertent parathyroid injury may cause '
                                                     'acute hypocalcemia with laryngospasm. Both '
                                                     'pathways threaten airway patency within '
                                                     'hours of surgery. Emergency airway equipment '
                                                     'readiness and vigilant monitoring for '
                                                     'stridor, neck swelling, and tetany reflect '
                                                     'this anatomy-driven risk.'}],
                            'extreme': [{'question': 'Anaphylaxis after IV antibiotic — first drug '
                                                     'theme?',
                                         'options': ['A) Oral antihistamine alone while continuing '
                                                     'the infusion',
                                                     'B) Increase the antibiotic rate after a '
                                                     'brief pause',
                                                     'C) Epinephrine IM per protocol + airway '
                                                     'support / stop infusion',
                                                     'D) Observe for two hours before giving any '
                                                     'medication'],
                                         'answer': 'C) Epinephrine IM per protocol + airway '
                                                   'support / stop infusion',
                                         'explanation': 'Anaphylaxis is an acute systemic '
                                                        'hypersensitivity reaction with mast-cell '
                                                        'mediator release causing bronchospasm, '
                                                        'laryngeal edema, and distributive shock. '
                                                        'Intramuscular epinephrine is first-line '
                                                        'because it reverses vasodilation, reduces '
                                                        'mucosal edema, and supports cardiac '
                                                        'output while the offending infusion is '
                                                        'stopped. Airway support and emergency '
                                                        'activation proceed in parallel because '
                                                        'progression can be minutes.'},
                                        {'question': 'Massive hemoptysis priority?',
                                         'options': ['A) Encourage forceful coughing without '
                                                     'supervision',
                                                     'B) Document sputum color and continue '
                                                     'routine care',
                                                     'C) Position the bleeding lung up to improve '
                                                     'drainage',
                                                     'D) Airway protection / position bleeding '
                                                     'side down if known, emergency help'],
                                         'answer': 'D) Airway protection / position bleeding side '
                                                   'down if known, emergency help',
                                         'explanation': 'Massive hemoptysis threatens asphyxiation '
                                                        'more immediately than exsanguination '
                                                        'because blood in the airways obstructs '
                                                        'alveolar ventilation. Priority nursing '
                                                        'actions protect the airway and, when the '
                                                        'bleeding side is known, position that '
                                                        'lung dependent to spare the contralateral '
                                                        'lung. Emergency help is summoned while '
                                                        'oxygenation and suction readiness are '
                                                        'maintained.'},
                                        {'question': 'Suspect compartment syndrome after cast?',
                                         'options': ['A) Pain out of proportion, pallor, '
                                                     'paresthesia — urgent notify; do not elevate '
                                                     'blindly alone as only action',
                                                     'B) Ignore escalating pain if distal pulses '
                                                     'are still palpable',
                                                     'C) Tighten the cast to reduce swelling '
                                                     'sensation',
                                                     'D) Treat with a sleep aid and reassess in '
                                                     'the morning'],
                                         'answer': 'A) Pain out of proportion, pallor, paresthesia '
                                                   '— urgent notify; do not elevate blindly alone '
                                                   'as only action',
                                         'explanation': 'Compartment syndrome occurs when rising '
                                                        'pressure within a fascial compartment '
                                                        'occludes capillary perfusion, producing '
                                                        'ischemic muscle and nerve injury. Pain '
                                                        'out of proportion, paresthesia, and '
                                                        'pallor are early ischemic warnings that '
                                                        'demand urgent surgical evaluation. '
                                                        'Casting or elevation alone without '
                                                        'escalation can delay fasciotomy and '
                                                        'result in irreversible limb loss.'}]},
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
                                        'options': ['A) Dorsogluteal site as first choice in '
                                                    'neonates',
                                                    'B) Vastus lateralis',
                                                    'C) Deltoid muscle for all newborns',
                                                    'D) Plantar foot pad for routine vaccines'],
                                        'answer': 'B) Vastus lateralis',
                                        'explanation': 'In young infants the vastus lateralis '
                                                       'provides a sufficiently large, '
                                                       'well-perfused muscle mass away from major '
                                                       'nerves and vessels used for ambulation '
                                                       'later in development. The dorsogluteal '
                                                       'site is avoided because of sciatic nerve '
                                                       'proximity and immature muscle bulk. '
                                                       'Age-appropriate site selection therefore '
                                                       'balances absorption with injury '
                                                       'prevention.'},
                                       {'question': 'Pediatric med dosing commonly based on?',
                                        'options': ['A) Matching the standard adult tablet dose',
                                                    'B) Patient hair color and estimated age only',
                                                    'C) Weight (mg/kg) with safe range checks',
                                                    'D) Room number–based unit stock vials'],
                                        'answer': 'C) Weight (mg/kg) with safe range checks',
                                        'explanation': 'Children’s body composition and immature '
                                                       'organ clearance make '
                                                       'milligram-per-kilogram dosing the standard '
                                                       'for most pediatric medications. '
                                                       'Weight-based calculation with safe-range '
                                                       'verification reduces both underdosing and '
                                                       'toxic overdose. Independent double-checks '
                                                       'are especially important for high-alert '
                                                       'agents such as insulin and opioids.'},
                                       {'question': 'Fontanelle assessment is relevant in?',
                                        'options': ['A) Only older adults with dementia',
                                                    'B) Only adolescents during growth spurts',
                                                    'C) Only pregnant patients in third trimester',
                                                    'D) Infants'],
                                        'answer': 'D) Infants',
                                        'explanation': 'The anterior fontanelle remains patent in '
                                                       'infancy and transmits changes in '
                                                       'intracranial volume and hydration status '
                                                       'to the examiner’s fingertips. A sunken '
                                                       'fontanelle suggests volume depletion, '
                                                       'whereas tense bulging may indicate '
                                                       'elevated intracranial pressure or '
                                                       'meningitis-related inflammation. '
                                                       'Fontanelle assessment is therefore '
                                                       'clinically relevant primarily while these '
                                                       'sutures remain open.'}],
                              'medium': [{'question': 'Dehydration signs in children include?',
                                          'options': ['A) Sunken eyes/fontanelle, dry mucosa, '
                                                      'decreased tears/urine, lethargy',
                                                      'B) Persistent hyperactivity with moist '
                                                      'mucous membranes',
                                                      'C) Adult blood-pressure cutoffs applied '
                                                      'unchanged',
                                                      'D) Increased tears and frequent large wet '
                                                      'diapers'],
                                          'answer': 'A) Sunken eyes/fontanelle, dry mucosa, '
                                                    'decreased tears/urine, lethargy',
                                          'explanation': 'Children have higher proportional water '
                                                         'content and faster turnover, so '
                                                         'gastrointestinal or febrile losses '
                                                         'quickly shrink intravascular volume. '
                                                         'Sunken eyes or fontanelle, dry mucosa, '
                                                         'decreased tears and urine, and lethargy '
                                                         'reflect progressive dehydration and '
                                                         'impaired perfusion. Comparing these '
                                                         'findings with the child’s baseline '
                                                         'distinguishes acute deterioration from '
                                                         'chronic habitus.'},
                                         {'question': 'FLACC scale is used for?',
                                          'options': ['A) Developmental milestone scoring in '
                                                      'toddlers',
                                                      'B) Pain assessment in nonverbal/young '
                                                      'children',
                                                      'C) Respiratory distress grading in '
                                                      'bronchiolitis only',
                                                      'D) Nutritional status screening in '
                                                      'adolescents'],
                                          'answer': 'B) Pain assessment in nonverbal/young '
                                                    'children',
                                          'explanation': 'Young and nonverbal children cannot '
                                                         'reliably self-report pain intensity, so '
                                                         'validated observational tools are '
                                                         'required. The FLACC scale scores Face, '
                                                         'Legs, Activity, Cry, and Consolability '
                                                         'as behavioral correlates of nociception. '
                                                         'Structured scoring guides analgesic '
                                                         'titration when self-report scales are '
                                                         'developmentally inappropriate.'},
                                         {'question': 'RSV bronchiolitis nursing focus?',
                                          'options': ['A) Immediate antibiotics for all suspected '
                                                      'viral cases',
                                                      'B) Chest physiotherapy as the sole required '
                                                      'intervention',
                                                      'C) Supportive airway/oxygen/hydration; '
                                                      'isolation precautions as indicated',
                                                      'D) Fluid restriction even with poor oral '
                                                      'intake'],
                                          'answer': 'C) Supportive airway/oxygen/hydration; '
                                                    'isolation precautions as indicated',
                                          'explanation': 'RSV bronchiolitis inflames small '
                                                         'airways, producing edema, mucus '
                                                         'plugging, and air trapping that increase '
                                                         'work of breathing and impair feeding. '
                                                         'Nursing care is primarily '
                                                         'supportive—oxygenation, airway clearance '
                                                         'as indicated, and hydration—while '
                                                         'droplet/contact precautions limit '
                                                         'nosocomial spread. Most infants improve '
                                                         'with time as inflammation resolves; '
                                                         'antivirals are not routine for typical '
                                                         'disease.'}],
                              'hard': [{'question': 'Suspected child abuse reporting?',
                                        'options': ['A) Confirm abuse in court before any report '
                                                    'is filed',
                                                    'B) Notify only the attending if parents '
                                                    'request privacy',
                                                    'C) Document suspicions but delay reporting '
                                                    'pending proof',
                                                    'D) Nurses are mandated reporters — follow '
                                                    'law/policy'],
                                        'answer': 'D) Nurses are mandated reporters — follow '
                                                  'law/policy',
                                        'explanation': 'Child maltreatment produces preventable '
                                                       'injury and developmental harm; statutes '
                                                       'designate nurses as mandated reporters so '
                                                       'protection does not depend on certainty of '
                                                       'guilt. Reporting suspected abuse per law '
                                                       'and policy initiates investigation and '
                                                       'safety planning by appropriate '
                                                       'authorities. The nurse’s clinical duty is '
                                                       'to document objectively and secure the '
                                                       'child’s immediate safety.'},
                                       {'question': 'Epiglottitis classic caution?',
                                        'options': ['A) Do not agitate / avoid throat exam that '
                                                    'precipitates obstruction; airway readiness',
                                                    'B) Force a thorough throat exam to visualize '
                                                    'the epiglottis',
                                                    'C) Place supine and stimulate crying for a '
                                                    'better airway view',
                                                    'D) Give oral fluids first to assess '
                                                    'swallowing safely'],
                                        'answer': 'A) Do not agitate / avoid throat exam that '
                                                  'precipitates obstruction; airway readiness',
                                        'explanation': 'Epiglottitis causes rapidly progressive '
                                                       'inflammation of the supraglottic '
                                                       'structures that can culminate in complete '
                                                       'airway obstruction. Agitation, forced '
                                                       'throat examination, or supine positioning '
                                                       'may precipitate sudden occlusion. Nursing '
                                                       'priorities are calm airway readiness, '
                                                       'avoidance of invasive oral inspection, and '
                                                       'emergent advanced-airway support in a '
                                                       'controlled setting.'},
                                       {'question': 'Kawasaki concern includes?',
                                        'options': ['A) Isolated otitis media as the primary '
                                                    'long-term risk',
                                                    'B) Coronary artery complications — follow '
                                                    'treatment protocols',
                                                    'C) Simple viral exanthem requiring '
                                                    'observation only',
                                                    'D) Transient limp that never needs cardiac '
                                                    'follow-up'],
                                        'answer': 'B) Coronary artery complications — follow '
                                                  'treatment protocols',
                                        'explanation': 'Kawasaki disease is a medium-vessel '
                                                       'vasculitis; coronary artery inflammation '
                                                       'can lead to aneurysms, thrombosis, and '
                                                       'myocardial ischemia if untreated. Fever '
                                                       'with mucocutaneous signs prompts '
                                                       'protocolized therapy (commonly IVIG and '
                                                       'aspirin as ordered) to blunt vasculitis. '
                                                       'Cardiac surveillance is integral because '
                                                       'coronary complications drive long-term '
                                                       'morbidity.'}],
                              'extreme': [{'question': 'Pediatric cardiac arrest compression depth '
                                                       'theme?',
                                           'options': ['A) Full adult 5 cm depth regardless of '
                                                       'child size',
                                                       'B) Shallow compressions to avoid rib '
                                                       'injury exclusively',
                                                       'C) About 1/3 AP chest diameter; '
                                                       'high-quality CPR',
                                                       'D) Compressions only after advanced airway '
                                                       'placement'],
                                           'answer': 'C) About 1/3 AP chest diameter; high-quality '
                                                     'CPR',
                                           'explanation': 'Pediatric cardiac arrest is usually '
                                                          'hypoxic–ischemic; coronary and cerebral '
                                                          'perfusion during CPR depend on adequate '
                                                          'compression depth and full recoil. '
                                                          'Compressing about one-third of the '
                                                          'anteroposterior chest diameter '
                                                          'generates the stroke volume needed '
                                                          'without excessive trauma. High-quality '
                                                          'CPR per PALS principles is the '
                                                          'physiologic bridge to return of '
                                                          'spontaneous circulation.'},
                                          {'question': 'Anaphylaxis in child after peanut?',
                                           'options': ['A) Oral antihistamine and observe at home '
                                                       'first',
                                                       'B) Nebulized albuterol as the initial '
                                                       'priority drug',
                                                       'C) IV epinephrine only after loss of '
                                                       'pulses',
                                                       'D) IM epinephrine promptly + emergency '
                                                       'activation'],
                                           'answer': 'D) IM epinephrine promptly + emergency '
                                                     'activation',
                                           'explanation': 'Food-triggered anaphylaxis in children '
                                                          'can progress from urticaria to '
                                                          'bronchospasm and distributive shock '
                                                          'within minutes via IgE-mediated '
                                                          'mediator release. Intramuscular '
                                                          'epinephrine promptly stabilizes '
                                                          'mast-cell effects on airway and '
                                                          'vasculature and must not be delayed for '
                                                          'antihistamines alone. Emergency '
                                                          'activation ensures airway expertise and '
                                                          'monitoring for biphasic recurrence.'},
                                          {'question': 'Suspected increased ICP in child after '
                                                       'trauma?',
                                           'options': ['A) ABC, head midline, avoid hypotonic '
                                                       'fluids blindly, urgent notify/neurosurg '
                                                       'path',
                                                       'B) Trendelenburg positioning to improve '
                                                       'cerebral perfusion',
                                                       'C) Rapid free-water boluses to lower serum '
                                                       'sodium quickly',
                                                       'D) Cluster all nursing care to minimize '
                                                       'monitoring interruptions'],
                                           'answer': 'A) ABC, head midline, avoid hypotonic fluids '
                                                     'blindly, urgent notify/neurosurg path',
                                           'explanation': 'After trauma, rising intracranial '
                                                          'pressure reduces cerebral perfusion '
                                                          'pressure (CPP = MAP − ICP) and risks '
                                                          'herniation. Keeping the head midline, '
                                                          'supporting ABCs, and avoiding hypotonic '
                                                          'fluids that worsen cerebral edema are '
                                                          'nursing measures that protect '
                                                          'autoregulation while neurosurgical '
                                                          'pathways are activated. Urgent '
                                                          'notification matches the narrow window '
                                                          'before irreversible secondary brain '
                                                          'injury.'}]},
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
                                       'options': ['A) Airway, perfusion, glucose, activity, '
                                                   'reflexes only',
                                                   'B) Appearance, Pulse, Grimace, Activity, '
                                                   'Respiration',
                                                   'C) Apnea episodes, posture, grasp, alertness, '
                                                   'rooting',
                                                   'D) Albumin, platelets, glucose, acid–base, '
                                                   'respirations'],
                                       'answer': 'B) Appearance, Pulse, Grimace, Activity, '
                                                 'Respiration',
                                       'explanation': 'The APGAR score quantifies newborn '
                                                      'cardiopulmonary adaptation by scoring '
                                                      'Appearance, Pulse, Grimace, Activity, and '
                                                      'Respiration. Assessments at 1 and 5 minutes '
                                                      'capture immediate transition and response '
                                                      'to resuscitation, guiding whether ongoing '
                                                      'support is needed. It is a physiologic '
                                                      'snapshot, not a long-term developmental '
                                                      'predictor.'},
                                      {'question': 'Fundal massage after birth primarily for?',
                                       'options': ['A) Stimulate newborn breathing exclusively',
                                                   'B) Reduce afterpains without affecting '
                                                   'bleeding',
                                                   'C) Uterine atony / postpartum hemorrhage '
                                                   'control',
                                                   'D) Promote lactation by emptying milk ducts'],
                                       'answer': 'C) Uterine atony / postpartum hemorrhage control',
                                       'explanation': 'After placental delivery, uterine atony '
                                                      'leaves spiral arteries unconstricted, '
                                                      'producing potentially massive postpartum '
                                                      'hemorrhage. Fundal massage stimulates '
                                                      'myometrial contraction that mechanically '
                                                      'tamponades these vessels. It is first-line '
                                                      'nursing management for a boggy uterus while '
                                                      'uterotonic medications and escalation '
                                                      'proceed.'},
                                      {'question': 'Rh-negative mother may need?',
                                       'options': ['A) Oxytocin infusion for every Rh-negative '
                                                   'mother',
                                                   'B) Magnesium sulfate solely based on Rh status',
                                                   'C) Broad-spectrum antibiotics for Rh '
                                                   'incompatibility',
                                                   'D) Rh immune globulin when indicated'],
                                       'answer': 'D) Rh immune globulin when indicated',
                                       'explanation': 'RhD-negative mothers can form '
                                                      'alloantibodies if exposed to RhD-positive '
                                                      'fetal red cells, risking hemolytic disease '
                                                      'in subsequent pregnancies. Rh immune '
                                                      'globulin provides passive antibody that '
                                                      'clears fetal antigen before maternal '
                                                      'sensitization occurs. Administration when '
                                                      'indicated interrupts this immunologic '
                                                      'cascade.'}],
                             'medium': [{'question': 'Preeclampsia danger signs include?',
                                         'options': ['A) Severe headache, visual changes, RUQ '
                                                     'pain, rising BP, proteinuria themes',
                                                     'B) Painless bright-red bleeding with a soft '
                                                     'nontender uterus only',
                                                     'C) Isolated dependent edema without BP or '
                                                     'symptom changes',
                                                     'D) Early satiety and heartburn without '
                                                     'neurologic symptoms'],
                                         'answer': 'A) Severe headache, visual changes, RUQ pain, '
                                                   'rising BP, proteinuria themes',
                                         'explanation': 'Preeclampsia features systemic '
                                                        'endothelial dysfunction with hypertension '
                                                        'and organ ischemia affecting brain, '
                                                        'liver, and kidneys. Severe headache, '
                                                        'visual changes, right-upper-quadrant '
                                                        'pain, rising blood pressure, and '
                                                        'proteinuria signal worsening vasospasm '
                                                        'and impending eclampsia or HELLP '
                                                        'progression. Prompt escalation enables '
                                                        'magnesium sulfate seizure prophylaxis and '
                                                        'delivery planning.'},
                                        {'question': 'Nonstress test reactive means roughly?',
                                         'options': ['A) Absent accelerations with a flat tracing '
                                                     'for hours',
                                                     'B) Adequate fetal heart accelerations with '
                                                     'movement (criteria gestational-age '
                                                     'dependent)',
                                                     'C) Late decelerations after every '
                                                     'contraction as reassurance',
                                                     'D) Maternal tachycardia alone confirming '
                                                     'fetal well-being'],
                                         'answer': 'B) Adequate fetal heart accelerations with '
                                                   'movement (criteria gestational-age dependent)',
                                         'explanation': 'A reactive nonstress test demonstrates '
                                                        'fetal heart-rate accelerations coupled '
                                                        'with movement, reflecting an intact '
                                                        'autonomic and myocardial oxygen supply. '
                                                        'Gestational-age–dependent criteria define '
                                                        'adequacy of that acceleratory pattern. '
                                                        'Reactivity is therefore used as a bedside '
                                                        'screen of current fetal well-being.'},
                                        {'question': 'Mastitis teaching includes?',
                                         'options': ['A) Stop breastfeeding until antibiotics are '
                                                     'finished',
                                                     'B) Apply ice only and avoid emptying the '
                                                     'breast',
                                                     'C) Continue breastfeeding/pumping as '
                                                     'advised, antibiotics if prescribed, '
                                                     'supportive care',
                                                     'D) Wean abruptly to prevent milk stasis '
                                                     'permanently'],
                                         'answer': 'C) Continue breastfeeding/pumping as advised, '
                                                   'antibiotics if prescribed, supportive care',
                                         'explanation': 'Lactational mastitis usually arises when '
                                                        'milk stasis and nipple trauma allow '
                                                        'bacterial entry into engorged ducts and '
                                                        'parenchyma. Continued breastfeeding or '
                                                        'pumping empties the breast, reduces '
                                                        'intraductal pressure, and aids antibiotic '
                                                        'delivery into infected tissue when '
                                                        'prescribed. Supportive care addresses '
                                                        'pain and inflammation while maintaining '
                                                        'milk flow.'}],
                             'hard': [{'question': 'Shoulder dystocia nursing help?',
                                       'options': ['A) Apply strong fundal pressure as the first '
                                                   'maneuver',
                                                   'B) Pull the fetal head firmly to free the '
                                                   'shoulder',
                                                   'C) Have the mother stand and push without '
                                                   'assistance',
                                                   'D) McRoberts, suprapubic pressure (not '
                                                   'fundal), call for help'],
                                       'answer': 'D) McRoberts, suprapubic pressure (not fundal), '
                                                 'call for help',
                                       'explanation': 'Shoulder dystocia traps the anterior '
                                                      'shoulder behind the pubic symphysis after '
                                                      'the head delivers, compressing the fetal '
                                                      'neck and delaying chest expansion. '
                                                      'McRoberts maneuver straightens the sacrum '
                                                      'and flattens the lumbar lordosis, while '
                                                      'directed suprapubic pressure adducts the '
                                                      'fetal shoulder; fundal pressure is avoided '
                                                      'because it worsens impaction. Immediate '
                                                      'help mobilization shortens the hypoxic '
                                                      'interval.'},
                                      {'question': 'Abruptio placentae classic?',
                                       'options': ['A) Painful bleeding, uterine '
                                                   'tenderness/hypertonus, fetal distress risk',
                                                   'B) Painless bleeding with a soft relaxed '
                                                   'uterus and reassuring FHTs',
                                                   'C) Clear fluid leak without pain or uterine '
                                                   'tone change',
                                                   'D) Low backache only after epidural placement'],
                                       'answer': 'A) Painful bleeding, uterine '
                                                 'tenderness/hypertonus, fetal distress risk',
                                       'explanation': 'Placental abruption is premature separation '
                                                      'of the placenta with maternal hemorrhage '
                                                      'into the decidual interface, producing '
                                                      'painful bleeding, uterine hypertonus, and '
                                                      'acute fetal hypoxia. Compromised '
                                                      'uteroplacental perfusion can rapidly cause '
                                                      'fetal distress and maternal coagulopathy. '
                                                      'Recognition as an obstetric emergency '
                                                      'drives continuous monitoring and expedited '
                                                      'delivery readiness.'},
                                      {'question': 'Postpartum blues vs depression?',
                                       'options': ['A) Blues lasting months with inability to care '
                                                   'for the infant',
                                                   'B) Blues brief/self-limited; depression '
                                                   'persistent and impairs function — screen/refer',
                                                   'C) Depression that always resolves by '
                                                   'postpartum day three',
                                                   'D) Blues requiring immediate involuntary '
                                                   'psychiatric hold'],
                                       'answer': 'B) Blues brief/self-limited; depression '
                                                 'persistent and impairs function — screen/refer',
                                       'explanation': 'Postpartum blues are transient mood '
                                                      'lability linked to hormonal shifts and '
                                                      'sleep loss, typically peaking within two '
                                                      'weeks without major functional collapse. '
                                                      'Postpartum depression persists, impairs '
                                                      'bonding and self-care, and carries suicide '
                                                      'risk, requiring screening and referral. '
                                                      'Differentiating duration and functional '
                                                      'impact guides whether reassurance or active '
                                                      'mental-health intervention is '
                                                      'appropriate.'}],
                             'extreme': [{'question': 'Eclampsia priority after seizure?',
                                          'options': ['A) Oral fluids and ambulation immediately '
                                                      'after the seizure',
                                                      'B) High-dose oxytocin as the first '
                                                      'antiseizure priority',
                                                      'C) Airway/breathing, lateral position, '
                                                      'MgSO4 per protocol, protect from injury',
                                                      'D) Trendelenburg and fundal massage during '
                                                      'the convulsion'],
                                          'answer': 'C) Airway/breathing, lateral position, MgSO4 '
                                                    'per protocol, protect from injury',
                                          'explanation': 'Eclamptic seizures threaten maternal '
                                                         'aspiration, hypoxemia, and trauma while '
                                                         'uteroplacental perfusion falls during '
                                                         'convulsive apnea. Lateral positioning '
                                                         'protects the airway, injury precautions '
                                                         'limit secondary trauma, and magnesium '
                                                         'sulfate per protocol raises the seizure '
                                                         'threshold by stabilizing neuronal '
                                                         'membranes. Maternal ABC stabilization is '
                                                         'the immediate prerequisite to fetal '
                                                         'resuscitation planning.'},
                                         {'question': 'Amniotic fluid embolism suspicion?',
                                          'options': ['A) Expected epidural side effect managed '
                                                      'with fluids only',
                                                      'B) Mild anxiety attack treated with '
                                                      'reassurance alone',
                                                      'C) Routine postpartum hemorrhage without '
                                                      'respiratory change',
                                                      'D) Sudden hypoxia/hypotension/coagulopathy '
                                                      'in labor — emergency response'],
                                          'answer': 'D) Sudden hypoxia/hypotension/coagulopathy in '
                                                    'labor — emergency response',
                                          'explanation': 'Amniotic fluid embolism is a rare '
                                                         'anaphylactoid response to amniotic '
                                                         'antigens entering the maternal '
                                                         'circulation, triggering sudden hypoxia, '
                                                         'cardiovascular collapse, and consumptive '
                                                         'coagulopathy during labor or immediately '
                                                         'postpartum. The syndrome behaves like '
                                                         'combined distributive/cardiogenic shock '
                                                         'plus DIC. Immediate emergency response '
                                                         'focuses on oxygenation, circulatory '
                                                         'support, and correction of hemorrhage.'},
                                         {'question': 'Uterine inversion recognition?',
                                          'options': ['A) Fundus prolapses; hemorrhage/shock — do '
                                                      'not remove placenta aggressively; emergency '
                                                      'help',
                                                      'B) Continue vigorous cord traction to '
                                                      'deliver the placenta faster',
                                                      'C) Give methylergonovine before recognizing '
                                                      'uterine position',
                                                      'D) Encourage maternal pushing to reduce the '
                                                      'inverted fundus'],
                                          'answer': 'A) Fundus prolapses; hemorrhage/shock — do '
                                                    'not remove placenta aggressively; emergency '
                                                    'help',
                                          'explanation': 'Uterine inversion is prolapse of the '
                                                         'fundus through the cervix, often '
                                                         'associated with excessive cord traction '
                                                         'or fundal pressure, producing profound '
                                                         'hemorrhage and vasovagal shock. '
                                                         'Aggressive attempts to remove an '
                                                         'attached placenta can worsen inversion '
                                                         'and bleeding. Emergency obstetric help '
                                                         'is required for prompt uterine '
                                                         'replacement and resuscitation.'}]},
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
                                         'options': ['A) Closed yes/no questions and rapid '
                                                     'advice-giving',
                                                     'B) Open-ended questions, empathy, '
                                                     'clarifying, nonjudgmental stance',
                                                     'C) Confronting delusions until the patient '
                                                     'agrees',
                                                     'D) Sharing personal opinions to build '
                                                     'rapport quickly'],
                                         'answer': 'B) Open-ended questions, empathy, clarifying, '
                                                   'nonjudgmental stance',
                                         'explanation': 'Therapeutic communication uses open-ended '
                                                        'questions, clarification, and empathic, '
                                                        'nonjudgmental presence to elicit the '
                                                        'patient’s internal experience without '
                                                        'imposing the nurse’s agenda. This stance '
                                                        'lowers defensive arousal and builds the '
                                                        'trust needed for accurate assessment and '
                                                        'collaborative care. Technique serves '
                                                        'relationship, which in turn enables '
                                                        'safety planning and treatment adherence.'},
                                        {'question': 'Suicide risk assessment asks about?',
                                         'options': ['A) Only family history without current '
                                                     'ideation',
                                                     'B) Sleep pattern alone as a sufficient '
                                                     'screen',
                                                     'C) Ideation, plan, intent, means, protective '
                                                     'factors',
                                                     'D) Appetite changes without safety '
                                                     'assessment'],
                                         'answer': 'C) Ideation, plan, intent, means, protective '
                                                   'factors',
                                         'explanation': 'Suicide risk is a dynamic clinical state '
                                                        'defined by ideation, planning, intent, '
                                                        'access to means, and the balance of '
                                                        'protective factors. Direct questioning '
                                                        'does not implant the idea; it clarifies '
                                                        'imminent danger so observation level and '
                                                        'means restriction can be matched to risk. '
                                                        'Incomplete assessment leaves lethal plans '
                                                        'unrecognized.'},
                                        {'question': 'SSRIs common early side effect theme?',
                                         'options': ['A) Immediate agranulocytosis in the first 24 '
                                                     'hours for all SSRIs',
                                                     'B) Severe hypertension as the most common '
                                                     'early effect',
                                                     'C) Complete absence of side effects after '
                                                     'the first dose',
                                                     'D) GI upset, headache, sleep changes; watch '
                                                     'activation/suicidality especially early'],
                                         'answer': 'D) GI upset, headache, sleep changes; watch '
                                                   'activation/suicidality especially early',
                                         'explanation': 'SSRIs increase serotonergic tone and '
                                                        'commonly cause early gastrointestinal '
                                                        'upset, headache, and sleep disturbance as '
                                                        'receptors adapt. A subset of patients, '
                                                        'especially early in treatment or after '
                                                        'dose changes, may experience activation '
                                                        'or heightened suicidal ideation requiring '
                                                        'close follow-up. Education prepares '
                                                        'patients to report these effects rather '
                                                        'than abruptly stopping therapy without '
                                                        'guidance.'}],
                               'medium': [{'question': 'Lithium toxicity early signs?',
                                           'options': ['A) Nausea, tremor, ataxia, confusion — '
                                                       'hold and notify; check level',
                                                       'B) Isolated dry mouth that never warrants '
                                                       'holding the dose',
                                                       'C) Improved mood confirming a therapeutic '
                                                       'level always',
                                                       'D) Mild thirst only, continue dose and '
                                                       'recheck in one month'],
                                           'answer': 'A) Nausea, tremor, ataxia, confusion — hold '
                                                     'and notify; check level',
                                           'explanation': 'Lithium has a narrow therapeutic index; '
                                                          'rising levels impair cerebellar and '
                                                          'cortical function, producing nausea, '
                                                          'coarse tremor, ataxia, and confusion as '
                                                          'early toxicity. Holding the dose and '
                                                          'obtaining a serum level prevent '
                                                          'progression to seizures and renal '
                                                          'injury. Volume depletion and drug '
                                                          'interactions that reduce clearance '
                                                          'amplify this risk.'},
                                          {'question': 'Alcohol withdrawal risk includes?',
                                           'options': ['A) Guaranteed safe outpatient detox '
                                                       'without monitoring',
                                                       'B) Seizures / DTs — use CIWA and protocols',
                                                       'C) Hypoglycemia exclusively without '
                                                       'autonomic signs',
                                                       'D) Only mild insomnia that never '
                                                       'progresses'],
                                           'answer': 'B) Seizures / DTs — use CIWA and protocols',
                                           'explanation': 'Abrupt cessation of chronic alcohol '
                                                          'intake removes GABA facilitation and '
                                                          'unmasks glutamate excess, producing '
                                                          'autonomic hyperactivity, seizures, and '
                                                          'potentially delirium tremens. '
                                                          'CIWA-guided benzodiazepine protocols '
                                                          'treat this hyperexcitable state and '
                                                          'reduce mortality. Withdrawal is '
                                                          'therefore managed as a medical '
                                                          'emergency risk, not solely a behavioral '
                                                          'issue.'},
                                          {'question': 'Hallucination nursing response?',
                                           'options': ['A) Argue until the patient admits the '
                                                       'voice is imaginary',
                                                       'B) Agree that the hallucination is '
                                                       'objectively real',
                                                       'C) Acknowledge experience without '
                                                       'reinforcing delusion; redirect to '
                                                       'reality/safety',
                                                       'D) Ignore the report and change the '
                                                       'subject abruptly'],
                                           'answer': 'C) Acknowledge experience without '
                                                     'reinforcing delusion; redirect to '
                                                     'reality/safety',
                                           'explanation': 'Hallucinations are percepts without '
                                                          'external stimuli generated by '
                                                          'disordered sensory processing; arguing '
                                                          'that they are “not real” often '
                                                          'increases distress without '
                                                          'extinguishing the experience. '
                                                          'Acknowledging the patient’s experience '
                                                          'while gently redirecting to shared '
                                                          'reality and safety maintains alliance '
                                                          'and reduces escalation. The nursing '
                                                          'goal is containment and orientation, '
                                                          'not debate.'}],
                               'hard': [{'question': 'NMS vs serotonin syndrome clue themes?',
                                         'options': ['A) Both are mild and observed outpatient '
                                                     'without holding meds',
                                                     'B) Serotonin syndrome always presents with '
                                                     'lead-pipe rigidity only',
                                                     'C) NMS is treated by increasing the '
                                                     'antipsychotic dose',
                                                     'D) NMS: rigidity/fever on antipsychotics; '
                                                     'SS: hyperreflexia/clonus on serotonergic '
                                                     'combos — both emergencies'],
                                         'answer': 'D) NMS: rigidity/fever on antipsychotics; SS: '
                                                   'hyperreflexia/clonus on serotonergic combos — '
                                                   'both emergencies',
                                         'explanation': 'Neuroleptic malignant syndrome is a '
                                                        'hypodopaminergic crisis with lead-pipe '
                                                        'rigidity, hyperthermia, and autonomic '
                                                        'instability after antipsychotics, whereas '
                                                        'serotonin syndrome features neuromuscular '
                                                        'hyperreflexia and clonus from excess '
                                                        'serotonergic activity. Both produce '
                                                        'life-threatening hyperthermia and organ '
                                                        'failure if unrecognized. Immediate '
                                                        'discontinuation of the offending agents '
                                                        'and intensive supportive care are '
                                                        'required in either case.'},
                                        {'question': 'Involuntary hold criteria themes?',
                                         'options': ['A) Danger to self/others or grave disability '
                                                     'per law',
                                                     'B) Patient disagreement with the treatment '
                                                     'plan alone',
                                                     'C) Family preference without clinical risk '
                                                     'criteria',
                                                     'D) Missed outpatient appointment without '
                                                     'safety concerns'],
                                         'answer': 'A) Danger to self/others or grave disability '
                                                   'per law',
                                         'explanation': 'Involuntary psychiatric holds exist when '
                                                        'mental illness creates imminent danger to '
                                                        'self or others, or grave disability that '
                                                        'prevents meeting basic needs, as defined '
                                                        'by statute. The criterion balances '
                                                        'liberty against the state’s interest in '
                                                        'preventing foreseeable harm. Nurses must '
                                                        'apply local legal standards when '
                                                        'initiating or supporting emergency '
                                                        'detention.'},
                                        {'question': 'Clozapine unique monitoring?',
                                         'options': ['A) Only liver enzymes every five years',
                                                     'B) Agranulocytosis risk — CBC monitoring '
                                                     'mandatory',
                                                     'C) No laboratory monitoring once therapy '
                                                     'starts',
                                                     'D) Serum lithium levels as the primary '
                                                     'clozapine check'],
                                         'answer': 'B) Agranulocytosis risk — CBC monitoring '
                                                   'mandatory',
                                         'explanation': 'Clozapine can cause idiosyncratic '
                                                        'agranulocytosis, abruptly collapsing '
                                                        'neutrophil defenses and permitting '
                                                        'overwhelming infection. Mandatory CBC '
                                                        'monitoring detects neutropenia before '
                                                        'sepsis develops. Fever or sore throat in '
                                                        'a clozapine-treated patient is treated as '
                                                        'a hematologic emergency until counts are '
                                                        'known.'}],
                               'extreme': [{'question': 'Active suicide attempt on unit?',
                                            'options': ['A) Leave the patient alone to preserve '
                                                        'privacy first',
                                                        'B) Negotiate for 30 minutes before '
                                                        'calling for help',
                                                        'C) Ensure scene safety, call emergency '
                                                        'response, first aid/ABC, continuous '
                                                        'observation',
                                                        'D) Document only and wait for the next '
                                                        'shift handoff'],
                                            'answer': 'C) Ensure scene safety, call emergency '
                                                      'response, first aid/ABC, continuous '
                                                      'observation',
                                            'explanation': 'An active suicide attempt on the unit '
                                                           'produces ongoing tissue injury, airway '
                                                           'compromise, or hemorrhage that '
                                                           'outranks administrative tasks. Scene '
                                                           'safety, emergency activation, and '
                                                           'ABC/first aid address immediate '
                                                           'physiologic threat while continuous '
                                                           'observation prevents a second attempt. '
                                                           'Rapid medical stabilization is the '
                                                           'prerequisite to psychiatric '
                                                           'containment.'},
                                           {'question': 'Violent patient with weapon?',
                                            'options': ['A) Approach alone to remove the weapon '
                                                        'quickly',
                                                        'B) Attempt physical takedown without '
                                                        'calling security',
                                                        'C) Corner the patient to prevent escape '
                                                        'routes',
                                                        'D) Do not approach alone; secure '
                                                        'self/others, call security/emergency per '
                                                        'policy'],
                                            'answer': 'D) Do not approach alone; secure '
                                                      'self/others, call security/emergency per '
                                                      'policy',
                                            'explanation': 'A weaponized violent patient can '
                                                           'injure staff and other patients before '
                                                           'therapeutic engagement is possible. '
                                                           'Not approaching alone and summoning '
                                                           'security per policy preserve the '
                                                           'responders who must later provide '
                                                           'care. Environmental control and '
                                                           'distance reduce assault risk while '
                                                           'de-escalation resources assemble.'},
                                           {'question': 'Neuroleptic malignant syndrome priority?',
                                            'options': ['A) Stop antipsychotic, supportive care, '
                                                        'escalate urgently',
                                                        'B) Give another antipsychotic dose to '
                                                        'treat rigidity',
                                                        'C) Apply heating blankets as the first '
                                                        'intervention',
                                                        'D) Discharge home with oral antipyretics '
                                                        'only'],
                                            'answer': 'A) Stop antipsychotic, supportive care, '
                                                      'escalate urgently',
                                            'explanation': 'Neuroleptic malignant syndrome drives '
                                                           'rigid hypermetabolism, rhabdomyolysis, '
                                                           'and autonomic collapse with high '
                                                           'untreated mortality. Stopping the '
                                                           'antipsychotic removes the dopaminergic '
                                                           'blockade precipitant while cooling, '
                                                           'hydration, and urgent medical '
                                                           'escalation treat the systemic crisis. '
                                                           'Early recognition is decisive because '
                                                           'progression can be fulminant.'}]},
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
                                       'options': ['A) Cardiac rehabilitation after myocardial '
                                                   'infarction',
                                                   'B) Immunization / health education before '
                                                   'disease',
                                                   'C) Chemotherapy for diagnosed cancer',
                                                   'D) Stroke rehab to restore lost function'],
                                       'answer': 'B) Immunization / health education before '
                                                 'disease',
                                       'explanation': 'Primary prevention interrupts disease '
                                                      'before pathophysiology begins by reducing '
                                                      'exposure or enhancing host resistance. '
                                                      'Immunization primes adaptive immunity, and '
                                                      'health education modifies risk behaviors '
                                                      'prior to clinical illness. These strategies '
                                                      'lower incidence at the population level '
                                                      'rather than treating established disease.'},
                                      {'question': 'Secondary prevention example?',
                                       'options': ['A) Seat-belt education before any injury '
                                                   'occurs',
                                                   'B) Building codes that prevent lead exposure',
                                                   'C) Screening (e.g., BP, mammogram) for early '
                                                   'detection',
                                                   'D) Hospice care for end-stage illness'],
                                       'answer': 'C) Screening (e.g., BP, mammogram) for early '
                                                 'detection',
                                       'explanation': 'Secondary prevention identifies pathologic '
                                                      'processes in a preclinical or early '
                                                      'clinical stage when intervention can alter '
                                                      'natural history. Screening tests such as '
                                                      'blood-pressure measurement and mammography '
                                                      'detect hypertension or malignancy before '
                                                      'advanced organ damage. Early detection '
                                                      'improves the likelihood that treatment will '
                                                      'be less invasive and more effective.'},
                                      {'question': 'Herd immunity relates to?',
                                       'options': ['A) Natural immunity from one recovered person '
                                                   'only',
                                                   'B) Antibiotic prophylaxis for an entire city',
                                                   'C) Quarantine of all healthy vaccinated people',
                                                   'D) Enough immunized people protecting '
                                                   'vulnerable'],
                                       'answer': 'D) Enough immunized people protecting vulnerable',
                                       'explanation': 'Herd immunity arises when a sufficient '
                                                      'proportion of a population is immune, '
                                                      'shrinking chains of transmission so that '
                                                      'susceptible individuals—including those who '
                                                      'cannot be vaccinated—are indirectly '
                                                      'protected. Community-level immune coverage '
                                                      'therefore functions as a barrier around '
                                                      'vulnerable hosts. Outbreak risk rises when '
                                                      'that coverage falls below pathogen-specific '
                                                      'thresholds.'}],
                             'medium': [{'question': 'Social determinants of health include?',
                                         'options': ['A) Housing, income, education, food access, '
                                                     'environment',
                                                     'B) Only genetic polymorphisms unrelated to '
                                                     'living conditions',
                                                     'C) Hospital bed count as the sole community '
                                                     'factor',
                                                     'D) Nurse staffing ratios inside one ICU '
                                                     'exclusively'],
                                         'answer': 'A) Housing, income, education, food access, '
                                                   'environment',
                                         'explanation': 'Health outcomes are shaped not only by '
                                                        'individual biology but by upstream '
                                                        'conditions—housing, income, education, '
                                                        'food access, and environment—that '
                                                        'structure exposure, stress, and access to '
                                                        'care. These social determinants influence '
                                                        'inflammation, nutrition, infection risk, '
                                                        'and chronic disease trajectories across '
                                                        'the life course. Community nursing '
                                                        'assessment therefore includes the '
                                                        'conditions in which people live and '
                                                        'work.'},
                                        {'question': 'TB airborne precautions need?',
                                         'options': ['A) Surgical mask and standard room only',
                                                     'B) N95/respirator + airborne room as '
                                                     'indicated',
                                                     'C) Contact gown without respiratory '
                                                     'protection',
                                                     'D) No PPE if the patient is afebrile'],
                                         'answer': 'B) N95/respirator + airborne room as indicated',
                                         'explanation': 'Mycobacterium tuberculosis is transmitted '
                                                        'by airborne droplet nuclei that remain '
                                                        'suspended and can be inhaled into '
                                                        'alveoli. Airborne precautions—N95 or '
                                                        'higher respirator and an '
                                                        'airborne-infection isolation room—reduce '
                                                        'inhalation dose for healthcare workers '
                                                        'and other patients. Transmission-based '
                                                        'precautions are matched to this aerosol '
                                                        'route rather than to contact alone.'},
                                        {'question': 'Home visit safety includes?',
                                         'options': ['A) Arrive unannounced without sharing '
                                                     'location',
                                                     'B) Ignore exit routes to appear culturally '
                                                     'humble',
                                                     'C) Situational awareness, share itinerary, '
                                                     'exit plan, respect culture',
                                                     'D) Enter any dwelling alone after dark '
                                                     'without check-in'],
                                         'answer': 'C) Situational awareness, share itinerary, '
                                                   'exit plan, respect culture',
                                         'explanation': 'Home visiting places the nurse in '
                                                        'uncontrolled environments where '
                                                        'aggression, animals, structural hazards, '
                                                        'or isolation can impede escape. '
                                                        'Situational awareness, shared '
                                                        'itineraries, and an exit plan mitigate '
                                                        'those risks while culturally respectful '
                                                        'engagement sustains therapeutic access. '
                                                        'Clinician safety is a precondition for '
                                                        'safe patient care in the community.'}],
                             'hard': [{'question': 'Upstream thinking in public health means?',
                                       'options': ['A) Focus only on individual downstream clinic '
                                                   'visits',
                                                   'B) Treat complications after disease is '
                                                   'established only',
                                                   'C) Avoid policy work and stay solely at the '
                                                   'bedside',
                                                   'D) Address root causes/policies, not only '
                                                   'individual downstream care'],
                                       'answer': 'D) Address root causes/policies, not only '
                                                 'individual downstream care',
                                       'explanation': 'Upstream public-health thinking targets the '
                                                      'policies, environments, and economic '
                                                      'structures that generate disease, rather '
                                                      'than only treating individuals after '
                                                      'illness appears. Addressing root '
                                                      'causes—such as housing, sanitation, or '
                                                      'tobacco regulation—prevents larger numbers '
                                                      'of cases than downstream clinical care '
                                                      'alone. Systems-level prevention is '
                                                      'therefore a core community-nursing '
                                                      'orientation.'},
                                      {'question': 'Disaster triage START theme?',
                                       'options': ['A) Do the most good for most people with '
                                                   'limited resources',
                                                   'B) Provide unlimited care to every victim '
                                                   'equally regardless of resources',
                                                   'C) Treat the least injured first to clear the '
                                                   'scene faster',
                                                   'D) Delay triage until specialists arrive for '
                                                   'every patient'],
                                       'answer': 'A) Do the most good for most people with limited '
                                                 'resources',
                                       'explanation': 'In mass-casualty disasters, immediate needs '
                                                      'exceed available personnel and supplies, so '
                                                      'triage allocates scarce resources to '
                                                      'maximize lives saved. START-type systems '
                                                      'rapidly categorize casualties by '
                                                      'survivability with timely intervention. '
                                                      'This utilitarian frame differs from '
                                                      'everyday intensive care of each individual '
                                                      'regardless of opportunity cost.'},
                                      {'question': 'Vaccine hesitancy best nursing approach?',
                                       'options': ['A) Dismiss concerns and mandate vaccination '
                                                   'without dialogue',
                                                   'B) Motivational interviewing, listen, correct '
                                                   'myths respectfully with evidence',
                                                   'C) Provide only printed material and end the '
                                                   'visit',
                                                   'D) Shame hesitant parents to force compliance'],
                                       'answer': 'B) Motivational interviewing, listen, correct '
                                                 'myths respectfully with evidence',
                                       'explanation': 'Vaccine hesitancy often reflects mistrust, '
                                                      'prior experience, and misinformation rather '
                                                      'than simple knowledge deficits. '
                                                      'Motivational interviewing elicits concerns, '
                                                      'affirms autonomy, and offers evidence '
                                                      'without confrontation, which is more '
                                                      'effective than coercive correction alone. '
                                                      'Trusting dialogue increases the likelihood '
                                                      'of informed acceptance over time.'}],
                             'extreme': [{'question': 'Suspected bioterror inhalation anthrax '
                                                      'cluster?',
                                          'options': ['A) Wait for culture confirmation before any '
                                                      'notification',
                                                      'B) Post details on social media to warn '
                                                      'neighbors first',
                                                      'C) Recognize, protect self, notify public '
                                                      'health/emergency immediately',
                                                      'D) Send exposed staff home without '
                                                      'reporting channels'],
                                          'answer': 'C) Recognize, protect self, notify public '
                                                    'health/emergency immediately',
                                          'explanation': 'Inhalation anthrax presents with severe '
                                                         'febrile respiratory illness and widened '
                                                         'mediastinum after aerosol exposure and '
                                                         'may signal intentional release when '
                                                         'clustered. Self-protection, rapid '
                                                         'clinical recognition, and immediate '
                                                         'public-health notification enable '
                                                         'antibiotic prophylaxis for exposed '
                                                         'cohorts and environmental control. Delay '
                                                         'allows continued exposure and missed '
                                                         'outbreak containment.'},
                                         {'question': 'Needle stick after unknown source?',
                                          'options': ['A) Squeeze the wound and delay reporting '
                                                      'until next shift',
                                                      'B) Ignore if the source patient looks '
                                                      'healthy',
                                                      'C) Apply lotion only and continue the '
                                                      'workday',
                                                      'D) Wash, report, evaluate source, follow '
                                                      'PEP policy ASAP'],
                                          'answer': 'D) Wash, report, evaluate source, follow PEP '
                                                    'policy ASAP',
                                          'explanation': 'Percutaneous exposure to blood can '
                                                         'transmit HIV, hepatitis B, and hepatitis '
                                                         'C; viral inoculum begins replication '
                                                         'quickly after inoculation. Immediate '
                                                         'washing, exposure reporting, source '
                                                         'evaluation, and post-exposure '
                                                         'prophylaxis per policy reduce infection '
                                                         'probability in a time-sensitive window. '
                                                         'Occupational health pathways exist '
                                                         'specifically for this biologic urgency.'},
                                         {'question': 'Quarantine vs isolation?',
                                          'options': ['A) Isolation: ill contagious; quarantine: '
                                                      'exposed potentially incubating — follow '
                                                      'public health orders',
                                                      'B) Isolation and quarantine are identical '
                                                      'terms in public health',
                                                      'C) Quarantine applies only to confirmed ill '
                                                      'contagious patients',
                                                      'D) Isolation is used solely for '
                                                      'noninfectious mental-health holds'],
                                          'answer': 'A) Isolation: ill contagious; quarantine: '
                                                    'exposed potentially incubating — follow '
                                                    'public health orders',
                                          'explanation': 'Isolation separates persons who are '
                                                         'already ill and contagious to stop '
                                                         'ongoing shedding to others, whereas '
                                                         'quarantine restricts movement of '
                                                         'asymptomatic exposed persons who may be '
                                                         'incubating infection. Public-health '
                                                         'orders operationalize these definitions '
                                                         'based on transmissibility and incubation '
                                                         'period. Accurate use of terms ensures '
                                                         'the correct population receives the '
                                                         'correct restriction.'}]},
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
                                           'options': ['A) Always keep SpO2 at 100% for every '
                                                       'adult',
                                                       'B) Generally ≥94% unless COPD/target '
                                                       'ordered differently',
                                                       'C) Accept SpO2 of 80% as normal in all '
                                                       'adults',
                                                       'D) Oxygen targets are irrelevant if the '
                                                       'patient is talking'],
                                           'answer': 'B) Generally ≥94% unless COPD/target ordered '
                                                     'differently',
                                           'explanation': 'Arterial oxygen saturation reflects '
                                                          'hemoglobin oxygen binding and, in most '
                                                          'adults without chronic hypercapnia, '
                                                          'targets of roughly ≥94% balance tissue '
                                                          'oxygen delivery against oxygen '
                                                          'toxicity. Patients with COPD or '
                                                          'specific orders may require lower '
                                                          'targets to avoid worsening hypercapnia. '
                                                          'SpO2 goals are therefore individualized '
                                                          'to pathophysiology and written '
                                                          'parameters.'},
                                          {'question': 'Arterial line zeroing is done at?',
                                           'options': ['A) At the top of the IV pole for '
                                                       'convenience',
                                                       "B) At the patient's wrist regardless of "
                                                       'position',
                                                       'C) Phlebostatic axis (approx 4th ICS '
                                                       'midaxillary)',
                                                       'D) At the ear lobe to approximate arterial '
                                                       'pressure'],
                                           'answer': 'C) Phlebostatic axis (approx 4th ICS '
                                                     'midaxillary)',
                                           'explanation': 'Arterial pressure transduction measures '
                                                          'hydrostatic pressure relative to a '
                                                          'reference level; the phlebostatic axis '
                                                          '(approximately the 4th intercostal '
                                                          'space at the midaxillary line) '
                                                          'approximates the right atrium. Zeroing '
                                                          'and leveling at this point remove '
                                                          'atmospheric and hydrostatic error so '
                                                          'displayed values reflect true '
                                                          'intravascular pressure. Incorrect '
                                                          'leveling systematically falsely '
                                                          'elevates or lowers readings.'},
                                          {'question': 'VAP prevention bundle includes?',
                                           'options': ['A) Keep the head of bed flat at all times',
                                                       'B) Avoid oral care to reduce gagging risk',
                                                       'C) Deep continuous sedation without '
                                                       'interruption forever',
                                                       'D) HOB elevation, oral care, sedation '
                                                       'vacation themes as protocol'],
                                           'answer': 'D) HOB elevation, oral care, sedation '
                                                     'vacation themes as protocol',
                                           'explanation': 'Ventilator-associated pneumonia follows '
                                                          'microaspiration of oropharyngeal '
                                                          'pathogens around the endotracheal tube '
                                                          'into dependent lung segments. Bundle '
                                                          'elements—head-of-bed elevation, oral '
                                                          'care, and sedation interruption as '
                                                          'protocolized—reduce aspiration risk and '
                                                          'facilitate liberation assessment. '
                                                          'Consistent bundle adherence lowers VAP '
                                                          'incidence in ventilated patients.'}],
                                 'medium': [{'question': 'CVP roughly reflects?',
                                             'options': ['A) Right atrial pressure / preload '
                                                         'estimate',
                                                         'B) Left ventricular ejection fraction '
                                                         'directly',
                                                         'C) Coronary artery stenosis severity',
                                                         'D) Systemic vascular resistance alone'],
                                             'answer': 'A) Right atrial pressure / preload '
                                                       'estimate',
                                             'explanation': 'Central venous pressure approximates '
                                                            'right atrial pressure and thus '
                                                            'estimates right-ventricular preload '
                                                            'under many clinical conditions. '
                                                            'Interpretation requires trends and '
                                                            'clinical context because positive '
                                                            'pressure ventilation, tricuspid '
                                                            'disease, and abdominal hypertension '
                                                            'alter the absolute number. Nurses use '
                                                            'CVP as one component of hemodynamic '
                                                            'assessment, not a standalone volume '
                                                            'verdict.'},
                                            {'question': 'Increased ICP nursing measures include?',
                                             'options': ['A) Cluster all care and keep the head '
                                                         'flexed sharply',
                                                         'B) HOB elevation as ordered, head '
                                                         'midline, avoid clustering care, treat '
                                                         'pain/fever',
                                                         'C) Trendelenburg and frequent coughing '
                                                         'exercises',
                                                         'D) Hypotonic free-water boluses to lower '
                                                         'ICP quickly'],
                                             'answer': 'B) HOB elevation as ordered, head midline, '
                                                       'avoid clustering care, treat pain/fever',
                                             'explanation': 'Intracranial pressure rises when '
                                                            'intracranial volume exceeds '
                                                            'compensatory CSF and venous shifts, '
                                                            'reducing cerebral perfusion. '
                                                            'Head-of-bed elevation as ordered, '
                                                            'head midline alignment, avoidance of '
                                                            'clustered noxious care, and control '
                                                            'of pain and fever limit venous '
                                                            'congestion and metabolic demand that '
                                                            'further elevate ICP. These nursing '
                                                            'measures are neuroprotective adjuncts '
                                                            'while definitive therapy proceeds.'},
                                            {'question': 'Shock first nursing priorities?',
                                             'options': ['A) Oral fluids only until the cause is '
                                                         'proven',
                                                         'B) Delay oxygen until laboratory results '
                                                         'return',
                                                         'C) ABC, IV access, oxygen, identify '
                                                         'type, follow protocols',
                                                         'D) Vasopressors before any airway or '
                                                         'breathing support'],
                                             'answer': 'C) ABC, IV access, oxygen, identify type, '
                                                       'follow protocols',
                                             'explanation': 'Shock is acute circulatory failure '
                                                            'with inadequate cellular oxygen '
                                                            'delivery or utilization, progressing '
                                                            'within minutes to lactic acidosis and '
                                                            'organ failure. Immediate '
                                                            'priorities—airway/breathing, oxygen, '
                                                            'vascular access, and '
                                                            'syndrome-specific protocols—restore '
                                                            'DO2 while the shock phenotype '
                                                            '(hypovolemic, distributive, '
                                                            'cardiogenic, obstructive) is '
                                                            'identified. Time to resuscitation '
                                                            'correlates with survival.'}],
                                 'hard': [{'question': 'ARDS ventilation theme?',
                                           'options': ['A) High tidal volumes to maximize minute '
                                                       'ventilation always',
                                                       'B) Zero PEEP for all ARDS patients',
                                                       'C) Unrestricted plateau pressures without '
                                                       'monitoring',
                                                       'D) Lung-protective low tidal volume '
                                                       'strategies'],
                                           'answer': 'D) Lung-protective low tidal volume '
                                                     'strategies',
                                           'explanation': 'ARDS features diffuse '
                                                          'alveolar-capillary injury with '
                                                          'noncardiogenic edema and stiff lungs '
                                                          'prone to overdistension injury. '
                                                          'Lung-protective ventilation with low '
                                                          'tidal volumes reduces volutrauma and '
                                                          'biotrauma that perpetuate cytokine '
                                                          'release and multiorgan failure. The '
                                                          'strategy accepts permissive hypercapnia '
                                                          'when needed to limit ventilator-induced '
                                                          'lung injury.'},
                                          {'question': 'Cardiac tamponade classic?',
                                           'options': ['A) Hypotension, JVD, muffled sounds / '
                                                       'pulsus — emergency',
                                                       'B) Hypertension with bounding pulses as '
                                                       'the classic triad',
                                                       'C) Isolated fever without hemodynamic '
                                                       'change',
                                                       'D) Clear lung sounds ruling out '
                                                       'pericardial disease'],
                                           'answer': 'A) Hypotension, JVD, muffled sounds / pulsus '
                                                     '— emergency',
                                           'explanation': 'Cardiac tamponade occurs when '
                                                          'pericardial fluid under pressure '
                                                          'equalizes diastolic filling pressures, '
                                                          'collapsing right-heart chambers and '
                                                          'cutting stroke volume. Classic '
                                                          'findings—hypotension, jugular venous '
                                                          'distention, muffled heart sounds, and '
                                                          'pulsus paradoxus—reflect obstructive '
                                                          'shock physiology. Emergent pericardial '
                                                          'decompression is required to restore '
                                                          'venous return.'},
                                          {'question': 'DKA nursing priorities?',
                                           'options': ['A) Fluid restriction and no insulin until '
                                                       'acidosis resolves',
                                                       'B) Fluids, insulin protocol, electrolyte '
                                                       '(K+) monitoring',
                                                       'C) Oral sulfonylurea as first-line ICU '
                                                       'therapy',
                                                       'D) Sodium bicarbonate push before any '
                                                       'fluid resuscitation always'],
                                           'answer': 'B) Fluids, insulin protocol, electrolyte '
                                                     '(K+) monitoring',
                                           'explanation': 'Diabetic ketoacidosis combines insulin '
                                                          'deficiency with counter-regulatory '
                                                          'hormone excess, driving hyperglycemia, '
                                                          'osmotic diuresis, and ketoacidosis with '
                                                          'total-body potassium depletion despite '
                                                          'variable serum K+. Fluid resuscitation, '
                                                          'protocolized insulin, and close '
                                                          'electrolyte monitoring correct the '
                                                          'metabolic spiral. Potassium must be '
                                                          'watched carefully because insulin '
                                                          'shifts K+ intracellularly and can '
                                                          'precipitate dangerous hypokalemia.'}],
                                 'extreme': [{'question': 'Pulseless VT/VF?',
                                              'options': ['A) Synchronized cardioversion at low '
                                                          'energy only without CPR',
                                                          'B) Antiarrhythmic infusion before any '
                                                          'defibrillation attempt',
                                                          'C) Defibrillate + high-quality CPR per '
                                                          'ACLS',
                                                          'D) Observe for spontaneous conversion '
                                                          'without intervention'],
                                              'answer': 'C) Defibrillate + high-quality CPR per '
                                                        'ACLS',
                                              'explanation': 'Pulseless ventricular tachycardia '
                                                             'and ventricular fibrillation produce '
                                                             'no effective stroke volume because '
                                                             'organized ventricular ejection '
                                                             'ceases. Defibrillation stuns the '
                                                             'myocardium to allow organized '
                                                             'pacemakers to resume, while '
                                                             'high-quality CPR maintains coronary '
                                                             'and cerebral perfusion between '
                                                             'shocks. ACLS pairs these '
                                                             'interventions because neither alone '
                                                             'reliably restores circulation.'},
                                             {'question': 'Massive transfusion nursing priorities?',
                                              'options': ['A) Single small-bore IV and '
                                                          'ambient-temperature products only',
                                                          'B) Delay access until type and cross '
                                                          'are fully complete in hemorrhage',
                                                          'C) Ignore electrolyte shifts during '
                                                          'rapid transfusion',
                                                          'D) ABC, large-bore access, warmer, '
                                                          'protocol ratios, watch '
                                                          'citrate/hypocalcemia/hyperK themes'],
                                              'answer': 'D) ABC, large-bore access, warmer, '
                                                        'protocol ratios, watch '
                                                        'citrate/hypocalcemia/hyperK themes',
                                              'explanation': 'Massive hemorrhage depletes '
                                                             'oxygen-carrying capacity and '
                                                             'clotting factors; resuscitation with '
                                                             'large-bore access, blood warmers, '
                                                             'and balanced product ratios '
                                                             'addresses hypovolemic shock and '
                                                             'trauma-induced coagulopathy. Citrate '
                                                             'in stored blood can bind calcium, '
                                                             'and cell lysis plus tissue injury '
                                                             'can raise potassium—both requiring '
                                                             'surveillance. Nursing priorities '
                                                             'integrate ABC support with '
                                                             'protocolized transfusion '
                                                             'physiology.'},
                                             {'question': 'Brain death testing nursing role?',
                                              'options': ['A) Support protocol, family '
                                                          'communication with team, maintain donor '
                                                          'care if applicable',
                                                          'B) Declare death independently without '
                                                          'institutional protocol',
                                                          'C) Stop all communication with family '
                                                          'during testing',
                                                          'D) Withhold ordered supportive care '
                                                          'that maintains organ perfusion for '
                                                          'donation pathways'],
                                              'answer': 'A) Support protocol, family communication '
                                                        'with team, maintain donor care if '
                                                        'applicable',
                                              'explanation': 'Brain-death determination follows '
                                                             'strict neurologic protocols '
                                                             'demonstrating irreversible cessation '
                                                             'of brain function, including '
                                                             'brainstem reflexes, under conditions '
                                                             'that exclude confounders. Nursing '
                                                             'roles include supporting testing '
                                                             'logistics, maintaining physiologic '
                                                             'stability for potential donation, '
                                                             'and facilitating transparent family '
                                                             'communication with the team. '
                                                             'Practice is policy-governed because '
                                                             'the diagnosis carries immediate '
                                                             'end-of-life and transplant '
                                                             'implications.'}]},
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
                                           'options': ['A) Patient preference, favorite color, '
                                                       'meal time only',
                                                       'B) Patient, drug, dose, route, time (+ '
                                                       'documentation/reason/response)',
                                                       'C) Room number, nurse name, shift, and '
                                                       'unit stock only',
                                                       'D) Manufacturer, lot number, and pharmacy '
                                                       'courier only'],
                                           'answer': 'B) Patient, drug, dose, route, time (+ '
                                                     'documentation/reason/response)',
                                           'explanation': 'Medication errors arise when any link '
                                                          'between the ordered therapy and the '
                                                          'administered product fails—wrong '
                                                          'patient, drug, dose, route, or time. '
                                                          'The rights framework operationalizes '
                                                          'independent verification at the bedside '
                                                          'before the patient is exposed to '
                                                          'pharmacologic effect. Documentation, '
                                                          'indication, and response complete the '
                                                          'safety loop after administration.'},
                                          {'question': 'Before giving digoxin, nurse often checks?',
                                           'options': ['A) Capillary blood glucose exclusively '
                                                       'before every dose',
                                                       'B) Serum potassium only, ignoring heart '
                                                       'rate',
                                                       'C) Apical pulse / hold parameters per '
                                                       'order',
                                                       'D) Orthostatic BP without assessing heart '
                                                       'rate'],
                                           'answer': 'C) Apical pulse / hold parameters per order',
                                           'explanation': 'Digoxin increases vagal tone and slows '
                                                          'atrioventricular conduction while '
                                                          'augmenting contractility; excess effect '
                                                          'produces symptomatic bradycardia and '
                                                          'arrhythmias. Checking the apical pulse '
                                                          'against hold parameters identifies '
                                                          'patients already at conduction risk '
                                                          'before an additional dose. Renal '
                                                          'impairment and electrolyte shifts '
                                                          'further narrow its therapeutic margin.'},
                                          {'question': 'IM injection angle typically?',
                                           'options': ['A) 15 degrees for all intramuscular '
                                                       'injections',
                                                       'B) 45 degrees as the standard IM angle',
                                                       'C) 5 degrees intradermal technique for IM '
                                                       'drugs',
                                                       'D) 90 degrees'],
                                           'answer': 'D) 90 degrees',
                                           'explanation': 'Intramuscular injection deposits '
                                                          'medication into highly vascular '
                                                          'skeletal muscle for relatively rapid '
                                                          'absorption. A 90-degree angle ensures '
                                                          'the needle traverses subcutaneous '
                                                          'tissue into muscle rather than '
                                                          'lingering in fat, where absorption is '
                                                          'slower and irritation may increase. '
                                                          'Correct angle is therefore a '
                                                          'determinant of intended '
                                                          'pharmacokinetics.'}],
                                 'medium': [{'question': 'Warfarin teaching includes?',
                                             'options': ['A) Consistent vitamin K intake, INR '
                                                         'monitoring, bleed precautions',
                                                         'B) Double vitamin K foods on days INR is '
                                                         'checked only',
                                                         'C) Stop INR checks once the dose feels '
                                                         'stable',
                                                         'D) Use razors freely and ignore unusual '
                                                         'bruising'],
                                             'answer': 'A) Consistent vitamin K intake, INR '
                                                       'monitoring, bleed precautions',
                                             'explanation': 'Warfarin inhibits vitamin K–dependent '
                                                            'clotting-factor synthesis, so dietary '
                                                            'vitamin K fluctuations alter INR and '
                                                            'bleeding or thrombosis risk. '
                                                            'Consistent intake, scheduled INR '
                                                            'monitoring, and bleed precautions '
                                                            'align everyday behavior with this '
                                                            'narrow therapeutic anticoagulation. '
                                                            'Patients need to recognize that '
                                                            'antibiotics, illness, and drug '
                                                            'interactions can abruptly change '
                                                            'warfarin effect.'},
                                            {'question': 'IV push opioids require?',
                                             'options': ['A) Rapid bolus without respiratory '
                                                         'monitoring',
                                                         'B) Slow administration per policy, '
                                                         'monitor RR/sedation, naloxone readiness',
                                                         'C) No need for sedation or RR checks '
                                                         'after IV opioids',
                                                         'D) Give with other CNS depressants to '
                                                         'enhance effect freely'],
                                             'answer': 'B) Slow administration per policy, monitor '
                                                       'RR/sedation, naloxone readiness',
                                             'explanation': 'Opioids agonize μ-receptors in the '
                                                            'brainstem respiratory centers, '
                                                            'depressing minute ventilation and '
                                                            'bluntng hypoxic drive in a '
                                                            'dose-dependent manner. Slow IV push '
                                                            'per policy and monitoring of '
                                                            'respiratory rate and sedation detect '
                                                            'early narcosis, while naloxone '
                                                            'readiness provides competitive '
                                                            'reversal if apnea develops. '
                                                            'Concurrent CNS depressants amplify '
                                                            'this risk.'},
                                            {'question': 'Insulin mixing clear-to-cloudy theme?',
                                             'options': ['A) Draw cloudy (NPH) before clear '
                                                         '(regular) always',
                                                         'B) Shake both vials vigorously until '
                                                         'foamy',
                                                         'C) Draw clear (regular) before cloudy '
                                                         '(NPH) if mixing allowed',
                                                         'D) Mix long-acting glargine with NPH in '
                                                         'one syringe routinely'],
                                             'answer': 'C) Draw clear (regular) before cloudy '
                                                       '(NPH) if mixing allowed',
                                             'explanation': 'When regular (clear) insulin is mixed '
                                                            'with NPH (cloudy), drawing the clear '
                                                            'insulin first prevents contamination '
                                                            'of the short-acting vial with '
                                                            'intermediate-acting suspension that '
                                                            'would alter future doses. The '
                                                            'sequence preserves the integrity of '
                                                            'each formulation when mixing is '
                                                            'allowed. Institutional policy still '
                                                            'governs whether mixing is permitted '
                                                            'for a given product.'}],
                                 'hard': [{'question': 'High-alert meds include examples like?',
                                           'options': ['A) Multivitamins and topical emollients '
                                                       'only',
                                                       'B) Normal saline flushes exclusively',
                                                       'C) Oral stool softeners as highest alert '
                                                       'class',
                                                       'D) Insulin, anticoagulants, opioids, '
                                                       'concentrated electrolytes'],
                                           'answer': 'D) Insulin, anticoagulants, opioids, '
                                                     'concentrated electrolytes',
                                           'explanation': 'High-alert medications—including '
                                                          'insulin, anticoagulants, opioids, and '
                                                          'concentrated electrolytes—have a '
                                                          'heightened risk of causing significant '
                                                          'patient harm when used in error because '
                                                          'of steep dose–response curves or '
                                                          'irreversible effects. Independent '
                                                          'double-checks add a second cognitive '
                                                          'verification before administration. '
                                                          'Layered safeguards acknowledge that '
                                                          'these agents leave little margin for '
                                                          'recovery from mistakes.'},
                                          {'question': 'Vancomycin red man syndrome related to?',
                                           'options': ['A) Rapid infusion — slow rate; not true '
                                                       'IgE allergy always',
                                                       'B) Mandatory lifelong ban on vancomycin '
                                                       'after any flush',
                                                       'C) Need to increase the infusion rate when '
                                                       'flushing appears',
                                                       'D) Proof of IgE allergy in every red-man '
                                                       'presentation'],
                                           'answer': 'A) Rapid infusion — slow rate; not true IgE '
                                                     'allergy always',
                                           'explanation': 'Vancomycin can trigger rate-related '
                                                          'mast-cell degranulation (red man '
                                                          'syndrome) with flushing, rash, and '
                                                          'hypotension that is distinct from '
                                                          'IgE-mediated allergy in many cases. '
                                                          'Slowing the infusion reduces histamine '
                                                          'release without necessarily requiring '
                                                          'permanent drug abandonment. Recognizing '
                                                          'the mechanism guides rate adjustment '
                                                          'versus true hypersensitivity workup.'},
                                          {'question': 'Potassium IV concentrated must?',
                                           'options': ['A) Give undiluted as a rapid IV push for '
                                                       'convenience',
                                                       'B) Never IV push; dilute/infuse per policy '
                                                       'with monitoring',
                                                       'C) Mix with undiluted calcium in the same '
                                                       'syringe',
                                                       'D) Infuse without cardiac monitoring '
                                                       'regardless of rate'],
                                           'answer': 'B) Never IV push; dilute/infuse per policy '
                                                     'with monitoring',
                                           'explanation': 'Intravenous potassium directly elevates '
                                                          'extracellular K+, which can abolish the '
                                                          'myocardial resting membrane gradient '
                                                          'and precipitate asystole or ventricular '
                                                          'fibrillation if delivered as a '
                                                          'concentrated push. Policy-mandated '
                                                          'dilution and controlled infusion with '
                                                          'cardiac monitoring limit the rate of '
                                                          'serum rise. Concentrated potassium is '
                                                          'therefore never given IV push.'}],
                                 'extreme': [{'question': 'Suspect malignant hyperthermia after '
                                                          'anesthesia trigger?',
                                              'options': ['A) Continue triggering agents while '
                                                          'giving antipyretics only',
                                                          'B) Apply warming blankets as the '
                                                          'primary treatment',
                                                          'C) Call MH protocol, dantrolene '
                                                          'readiness, stop triggers, cool/support',
                                                          'D) Discharge to PACU without notifying '
                                                          'anesthesia'],
                                              'answer': 'C) Call MH protocol, dantrolene '
                                                        'readiness, stop triggers, cool/support',
                                              'explanation': 'Malignant hyperthermia is a '
                                                             'pharmacogenetic ryanodine-receptor '
                                                             'crisis in skeletal muscle triggered '
                                                             'by certain anesthetics and '
                                                             'succinylcholine, causing '
                                                             'uncontrolled calcium release, '
                                                             'rigidity, hypercarbia, and '
                                                             'hyperthermia. Stopping triggers, '
                                                             'giving dantrolene to inhibit calcium '
                                                             'release, and active cooling '
                                                             'interrupt the hypermetabolic '
                                                             'cascade. MH protocol activation is '
                                                             'time-critical because rhabdomyolysis '
                                                             'and hyperkalemia progress rapidly.'},
                                             {'question': 'Opioid overdose with RR 4?',
                                              'options': ['A) Give additional opioid to reverse '
                                                          'paradoxical breathing',
                                                          'B) Wait for spontaneous improvement '
                                                          'without airway support',
                                                          'C) Oral naloxone only while leaving the '
                                                          'patient unmonitored',
                                                          'D) Stimulate, support ventilation, '
                                                          'naloxone per protocol'],
                                              'answer': 'D) Stimulate, support ventilation, '
                                                        'naloxone per protocol',
                                              'explanation': 'Severe opioid overdose produces '
                                                             'μ-receptor–mediated respiratory '
                                                             'arrest with hypoxemia and '
                                                             'hypercapnia; a respiratory rate of 4 '
                                                             'signals imminent hypoxic injury. '
                                                             'Stimulation and assisted ventilation '
                                                             'restore gas exchange while naloxone '
                                                             'competitively displaces opioid from '
                                                             'receptors. ABC support and antidote '
                                                             'are paired because naloxone onset is '
                                                             'not instantaneous and '
                                                             'renarcotization may occur.'},
                                             {'question': 'Chemotherapy extravasation?',
                                              'options': ['A) Stop infusion, follow vesicant '
                                                          'protocol, do not ignore pain/swelling '
                                                          'at site',
                                                          'B) Increase the rate to clear the line '
                                                          'faster',
                                                          'C) Apply heat and continue the vesicant '
                                                          'infusion',
                                                          'D) Document later without interrupting '
                                                          'the infusion'],
                                              'answer': 'A) Stop infusion, follow vesicant '
                                                        'protocol, do not ignore pain/swelling at '
                                                        'site',
                                              'explanation': 'Vesicant chemotherapy extravasated '
                                                             'into subcutaneous tissue causes '
                                                             'prolonged local DNA damage, '
                                                             'necrosis, and ulceration. Stopping '
                                                             'the infusion limits further '
                                                             'extravasation volume; agent-specific '
                                                             'antidotes, aspiration, and cold or '
                                                             'heat per protocol then modify tissue '
                                                             'injury. Pain or swelling at the site '
                                                             'is an early warning that must not be '
                                                             'dismissed.'}]},
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
                                               'options': ['A) Doing whatever the care team '
                                                           'prefers without discussion',
                                                           "B) Respect patient's right to make "
                                                           'informed decisions',
                                                           'C) Withholding information to avoid '
                                                           'patient worry always',
                                                           'D) Family decisions overriding a '
                                                           "capacitated patient's refusal"],
                                               'answer': "B) Respect patient's right to make "
                                                         'informed decisions',
                                               'explanation': 'Autonomy is the ethical principle '
                                                              'that competent persons have moral '
                                                              'authority over decisions affecting '
                                                              'their own bodies and lives. '
                                                              'Respecting informed choices—even '
                                                              'when clinicians disagree—affirms '
                                                              'the patient as the primary '
                                                              'decision-maker. Nursing practice '
                                                              'operationalizes autonomy through '
                                                              'informed consent, refusal support, '
                                                              'and avoidance of coercion.'},
                                              {'question': 'Beneficence means?',
                                               'options': ['A) Avoiding all interventions that '
                                                           'carry any risk',
                                                           'B) Distributing scarce resources by '
                                                           'ability to pay only',
                                                           'C) Act to benefit the patient',
                                                           'D) Keeping secrets that harm the care '
                                                           'plan'],
                                               'answer': 'C) Act to benefit the patient',
                                               'explanation': 'Beneficence obligates clinicians to '
                                                              'act in ways that promote the '
                                                              'patient’s health interests and '
                                                              'well-being, weighing benefits of '
                                                              'interventions against burdens. It '
                                                              'underpins proactive care such as '
                                                              'pain relief, fall prevention, and '
                                                              'timely escalation of deterioration. '
                                                              'Beneficent action is guided by the '
                                                              'patient’s values, not solely by '
                                                              'technical possibility.'},
                                              {'question': 'Confidentiality breach example?',
                                               'options': ['A) Hand-off report in a private '
                                                           'conference room',
                                                           'B) Encrypted EHR messaging among the '
                                                           'care team',
                                                           'C) Teaching with de-identified case '
                                                           'details in class',
                                                           'D) Discussing patient details in '
                                                           'elevator with strangers'],
                                               'answer': 'D) Discussing patient details in '
                                                         'elevator with strangers',
                                               'explanation': 'Confidentiality protects private '
                                                              'health information so patients can '
                                                              'disclose sensitive data needed for '
                                                              'accurate diagnosis without social '
                                                              'harm. Discussing identifiable '
                                                              'details in public spaces such as '
                                                              'elevators exposes protected health '
                                                              'information to bystanders and '
                                                              'erodes trust. Professional privacy '
                                                              'duties exist to preserve that '
                                                              'therapeutic disclosure '
                                                              'relationship.'}],
                                     'medium': [{'question': 'Nonmaleficence means?',
                                                 'options': ['A) Do no harm',
                                                             'B) Maximize billing for the '
                                                             'institution',
                                                             'C) Prioritize staff convenience over '
                                                             'safety',
                                                             'D) Guarantee cure regardless of '
                                                             'risk'],
                                                 'answer': 'A) Do no harm',
                                                 'explanation': 'Nonmaleficence requires that '
                                                                'caregivers avoid causing '
                                                                'unnecessary harm and minimize the '
                                                                'harms inherent in necessary '
                                                                'interventions. It constrains '
                                                                'risky procedures, inappropriate '
                                                                'restraints, and negligent '
                                                                'omissions that foreseeably injure '
                                                                'patients. Balancing '
                                                                'nonmaleficence with beneficence '
                                                                'is central to proportional '
                                                                'clinical judgment.'},
                                                {'question': 'Justice in nursing relates to?',
                                                 'options': ['A) Giving identical interventions to '
                                                             'every patient always',
                                                             'B) Fair allocation of care/resources',
                                                             'C) Favoring patients who are easiest '
                                                             'to care for',
                                                             'D) Ignoring disparities in access to '
                                                             'services'],
                                                 'answer': 'B) Fair allocation of care/resources',
                                                 'explanation': 'Justice in healthcare ethics '
                                                                'concerns fairness in the '
                                                                'distribution of nursing '
                                                                'attention, scarce resources, and '
                                                                'respect across patients without '
                                                                'arbitrary discrimination. '
                                                                'Equitable allocation means '
                                                                'clinically comparable needs '
                                                                'receive comparable priority. '
                                                                'Structural bias and preferential '
                                                                'treatment violate this '
                                                                'distributive obligation.'},
                                                {'question': 'Incident report purpose?',
                                                 'options': ['A) A punitive essay blaming the '
                                                             'individual nurse in the chart',
                                                             'B) A substitute for notifying the '
                                                             'provider of harm',
                                                             'C) Quality improvement / risk '
                                                             'reduction — factual, not punitive '
                                                             'chart blame essay',
                                                             'D) A public social-media summary of '
                                                             'the event'],
                                                 'answer': 'C) Quality improvement / risk '
                                                           'reduction — factual, not punitive '
                                                           'chart blame essay',
                                                 'explanation': 'Incident reports capture adverse '
                                                                'events and near misses as data '
                                                                'for system learning—process '
                                                                'redesign, equipment fixes, and '
                                                                'training—rather than as vehicles '
                                                                'for personal blame essays in the '
                                                                'medical record. Including near '
                                                                'misses reveals latent failures '
                                                                'before harm reaches the patient. '
                                                                'Just-culture reporting '
                                                                'strengthens prevention science at '
                                                                'the unit and organizational '
                                                                'level.'}],
                                     'hard': [{'question': 'Advocacy means?',
                                               'options': ["A) Protect the institution's "
                                                           'reputation over patient rights',
                                                           'B) Remain silent when unsafe practices '
                                                           'continue',
                                                           'C) Follow orders that clearly violate '
                                                           'patient safety without question',
                                                           'D) Speak/act to protect patient rights '
                                                           'and best interests'],
                                               'answer': 'D) Speak/act to protect patient rights '
                                                         'and best interests',
                                               'explanation': 'Advocacy is the professional '
                                                              'obligation to amplify the patient’s '
                                                              'rights, preferences, and best '
                                                              'interests when illness, hierarchy, '
                                                              'or systems create vulnerability. '
                                                              'Speaking up about unsafe conditions '
                                                              'or unanswered questions protects '
                                                              'those who cannot effectively '
                                                              'protect themselves. It is a core '
                                                              'nursing duty grounded in both '
                                                              'ethics and standards of practice.'},
                                              {'question': 'Informed consent nurse role often?',
                                               'options': ['A) Witness signature, verify '
                                                           'understanding, notify provider if '
                                                           'questions remain',
                                                           'B) Independently explain surgical '
                                                           'risks in place of the surgeon always',
                                                           'C) Obtain consent even when the '
                                                           'patient clearly does not understand',
                                                           'D) Skip witnessing if the family says '
                                                           'the patient agrees'],
                                               'answer': 'A) Witness signature, verify '
                                                         'understanding, notify provider if '
                                                         'questions remain',
                                               'explanation': 'Informed consent requires '
                                                              'comprehension; the nurse who '
                                                              'witnesses a signature also verifies '
                                                              'that the patient understands and '
                                                              'that lingering questions reach the '
                                                              'responsible provider. Language '
                                                              'access, sensory supports, and '
                                                              'unhurried clarification are part of '
                                                              'that communicative duty. Without '
                                                              'understanding, a signature does not '
                                                              'constitute meaningful consent.'},
                                              {'question': 'Moral distress occurs when?',
                                               'options': ['A) Feeling sad after a long shift '
                                                           'without ethical conflict',
                                                           'B) Nurse knows right action but '
                                                           'constrained from taking it',
                                                           'C) Simple disagreement about '
                                                           'lunch-break timing',
                                                           'D) Confidence that all institutional '
                                                           'policies are perfect'],
                                               'answer': 'B) Nurse knows right action but '
                                                         'constrained from taking it',
                                               'explanation': 'Moral distress arises when the '
                                                              'nurse can identify the ethically '
                                                              'appropriate action yet '
                                                              'institutional constraints, '
                                                              'conflicting orders, or power '
                                                              'structures block that action. The '
                                                              'resulting cognitive–emotional '
                                                              'conflict is associated with burnout '
                                                              'and silence about safety concerns. '
                                                              'Ethics consultation and '
                                                              'organizational support are '
                                                              'appropriate responses to relieve '
                                                              'the constraint, not merely to '
                                                              'advise endurance.'}],
                                     'extreme': [{'question': 'Whistleblowing about ongoing '
                                                              'patient harm?',
                                                  'options': ['A) Stay silent to protect '
                                                              'colleagues from scrutiny',
                                                              'B) Alter records to hide ongoing '
                                                              'unsafe practice',
                                                              'C) Report through required '
                                                              'channels; patient safety overrides '
                                                              'loyalty to cover-ups',
                                                              'D) Post accusations publicly before '
                                                              'using internal channels'],
                                                  'answer': 'C) Report through required channels; '
                                                            'patient safety overrides loyalty to '
                                                            'cover-ups',
                                                  'explanation': 'When ongoing practices cause '
                                                                 'patient harm, loyalty to '
                                                                 'colleagues or institutions '
                                                                 'cannot ethically outweigh the '
                                                                 'duty to protect those patients. '
                                                                 'Whistleblowing through required '
                                                                 'channels activates oversight '
                                                                 'mechanisms designed to stop '
                                                                 'preventable injury. Patient '
                                                                 'safety is the overriding '
                                                                 'professional interest in such '
                                                                 'conflicts.'},
                                                 {'question': 'DNR order conflict at bedside?',
                                                  'options': ['A) Start full CPR despite a '
                                                              'verified valid DNR',
                                                              'B) Ignore the order and ask only '
                                                              'the newest nurse',
                                                              'C) Hide the DNR document from the '
                                                              'responding team',
                                                              'D) Clarify current valid order with '
                                                              'team; do not perform unwanted '
                                                              'resuscitation if valid DNR'],
                                                  'answer': 'D) Clarify current valid order with '
                                                            'team; do not perform unwanted '
                                                            'resuscitation if valid DNR',
                                                  'explanation': 'A valid do-not-resuscitate order '
                                                                 'documents a decision to forgo '
                                                                 'CPR based on patient (or '
                                                                 'surrogate) values and medical '
                                                                 'judgment; performing unwanted '
                                                                 'resuscitation violates both '
                                                                 'autonomy and nonmaleficence. '
                                                                 'Bedside conflict is resolved by '
                                                                 'clarifying the current valid '
                                                                 'order with the care team and '
                                                                 'chain of command. Policy '
                                                                 'existence does not replace '
                                                                 'verifying which order is '
                                                                 'active.'},
                                                 {'question': 'Social media photo of patient?',
                                                  'options': ['A) Never — confidentiality/privacy '
                                                              'violation',
                                                              "B) Allowed if the patient's face is "
                                                              'only partially visible',
                                                              'C) Acceptable with friends-only '
                                                              'social media settings',
                                                              'D) Fine if posted after discharge '
                                                              'without consent'],
                                                  'answer': 'A) Never — confidentiality/privacy '
                                                            'violation',
                                                  'explanation': 'Photographs of patients shared '
                                                                 'on social media disclose '
                                                                 'identifiable health encounters '
                                                                 'outside the care relationship '
                                                                 'and authorized channels. Even '
                                                                 'partial identifiers or clinical '
                                                                 'context can violate privacy '
                                                                 'regulations and professional '
                                                                 'boundaries. Such posting is '
                                                                 'prohibited because '
                                                                 'confidentiality does not end at '
                                                                 'the hospital door.'}]},
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
                                        'options': ['A) High spiking fever as the only reliable '
                                                    'early clue',
                                                    'B) Confusion / falls / functional decline '
                                                    '(fever may be absent)',
                                                    'C) Classic localized pain identical to '
                                                    'younger adults always',
                                                    'D) Leukocytosis required before any concern '
                                                    'for infection'],
                                        'answer': 'B) Confusion / falls / functional decline '
                                                  '(fever may be absent)',
                                        'explanation': 'Older adults often mount blunted febrile '
                                                       'and local inflammatory responses because '
                                                       'of immunosenescence and altered '
                                                       'thermoregulation, so infection may present '
                                                       'as new confusion, falls, or functional '
                                                       'decline instead of high fever. Recognizing '
                                                       'atypical syndromes prevents delayed '
                                                       'antibiotics and sepsis progression. '
                                                       'Mental-status change is therefore treated '
                                                       'as a potential medical red flag.'},
                                       {'question': 'Polypharmacy risk includes?',
                                        'options': ['A) Improved adherence without adverse-effect '
                                                    'risk',
                                                    'B) Guaranteed better outcomes with more '
                                                    'medications',
                                                    'C) Interactions, falls, ADRs',
                                                    'D) Elimination of the need for medication '
                                                    'review'],
                                        'answer': 'C) Interactions, falls, ADRs',
                                        'explanation': 'Polypharmacy increases pharmacokinetic and '
                                                       'pharmacodynamic interactions, '
                                                       'anticholinergic burden, sedation, and '
                                                       'orthostasis, elevating falls and adverse '
                                                       'drug reaction rates. Age-related declines '
                                                       'in renal and hepatic clearance amplify '
                                                       'exposure to many agents. Medication '
                                                       'reconciliation and review reduce '
                                                       'cumulative toxicity while preserving '
                                                       'necessary therapy.'},
                                       {'question': 'Pressure injury prevention includes?',
                                        'options': ['A) Keep patients in one position to protect '
                                                    'surgical sites',
                                                    'B) Massage reddened bony areas vigorously '
                                                    'each hour',
                                                    'C) Restrict protein to reduce metabolic '
                                                    'demand',
                                                    'D) Repositioning, skin care, nutrition, '
                                                    'pressure-relieving surfaces'],
                                        'answer': 'D) Repositioning, skin care, nutrition, '
                                                  'pressure-relieving surfaces',
                                        'explanation': 'Pressure injuries develop when sustained '
                                                       'interface pressure and shear occlude '
                                                       'capillary flow over bony prominences, '
                                                       'producing ischemia and tissue necrosis. '
                                                       'Repositioning, moisture management, '
                                                       'nutrition adequate for repair, and '
                                                       'pressure-relieving surfaces restore '
                                                       'perfusion and tissue tolerance. Prevention '
                                                       'targets the mechanical and metabolic '
                                                       'drivers of skin breakdown.'}],
                              'medium': [{'question': 'Beers Criteria relate to?',
                                          'options': ['A) Potentially inappropriate medications in '
                                                      'older adults',
                                                      'B) Preferred antibiotics for pediatric '
                                                      'otitis only',
                                                      'C) Surgical antibiotic prophylaxis timing '
                                                      'exclusively',
                                                      'D) IV fluid selection in trauma '
                                                      'resuscitation only'],
                                          'answer': 'A) Potentially inappropriate medications in '
                                                    'older adults',
                                          'explanation': 'Beers Criteria catalog medications whose '
                                                         'risks—falls, delirium, bleeding, '
                                                         'anticholinergic effects—often outweigh '
                                                         'benefits in older adults given altered '
                                                         'physiology. Awareness of these '
                                                         'potentially inappropriate medications '
                                                         'supports safer prescribing and '
                                                         'deprescribing conversations. The list is '
                                                         'a clinical risk tool, not a pediatric or '
                                                         'veterinary dosing reference.'},
                                         {'question': 'Orthostatic hypotension nursing tip?',
                                          'options': ['A) Stand quickly and walk immediately after '
                                                      'lying flat',
                                                      'B) Dangle, rise slowly, monitor BP '
                                                      'lying/standing',
                                                      'C) Ignore dizziness if systolic BP is over '
                                                      '100',
                                                      'D) Hold all antihypertensives permanently '
                                                      'without review'],
                                          'answer': 'B) Dangle, rise slowly, monitor BP '
                                                    'lying/standing',
                                          'explanation': 'Orthostatic hypotension reflects '
                                                         'impaired baroreflex and vascular tone '
                                                         'with pooling of blood in the lower '
                                                         'extremities on standing, transiently '
                                                         'cutting cerebral perfusion. Dangling, '
                                                         'slow position changes, and '
                                                         'lying-to-standing blood-pressure '
                                                         'measurement detect and mitigate syncope '
                                                         'risk. Fall prevention follows directly '
                                                         'from this postural circulatory '
                                                         'physiology.'},
                                         {'question': 'Delirium vs dementia key?',
                                          'options': ['A) Delirium is always chronic and '
                                                      'irreversible',
                                                      'B) Dementia fluctuates hourly with acute '
                                                      'illness only',
                                                      'C) Delirium acute/fluctuating often '
                                                      'reversible cause; dementia chronic '
                                                      'progressive',
                                                      'D) Both conditions are identical in onset '
                                                      'and course'],
                                          'answer': 'C) Delirium acute/fluctuating often '
                                                    'reversible cause; dementia chronic '
                                                    'progressive',
                                          'explanation': 'Delirium is an acute, fluctuating '
                                                         'disturbance of attention and awareness '
                                                         'usually driven by a reversible medical '
                                                         'precipitant, whereas dementia is a '
                                                         'chronic progressive neurocognitive '
                                                         'decline. Distinguishing them matters '
                                                         'because delirium demands urgent search '
                                                         'for infection, hypoxia, medications, and '
                                                         'metabolic causes. Treating precipitants '
                                                         'can restore baseline cognition.'}],
                              'hard': [{'question': 'Elder abuse nurse duty?',
                                        'options': ['A) Confront the caregiver publicly before any '
                                                    'report',
                                                    'B) Wait for definitive proof before any '
                                                    'notification',
                                                    'C) Document only and never escalate outside '
                                                    'the unit',
                                                    'D) Report suspected abuse per law/policy'],
                                        'answer': 'D) Report suspected abuse per law/policy',
                                        'explanation': 'Elder abuse—physical, emotional, '
                                                       'financial, or neglect—exploits dependency '
                                                       'and produces preventable morbidity and '
                                                       'mortality. Nurses are typically mandated '
                                                       'reporters so that adult protective and '
                                                       'legal systems can intervene when suspicion '
                                                       'arises. Objective documentation and '
                                                       'reporting per law protect the older adult '
                                                       'when self-advocacy is compromised.'},
                                       {'question': 'Restraint alternative for wander risk?',
                                        'options': ['A) Supervision, alarms, toileting schedule, '
                                                    'meaningful activity — least restrictive',
                                                    'B) Immediate four-point restraints for any '
                                                    'wandering risk',
                                                    'C) Sedation to keep the patient in bed all '
                                                    'day',
                                                    'D) Locked seclusion without attempting '
                                                    'alternatives'],
                                        'answer': 'A) Supervision, alarms, toileting schedule, '
                                                  'meaningful activity — least restrictive',
                                        'explanation': 'Wandering risk often reflects unmet needs, '
                                                       'disorientation, or akathisia rather than '
                                                       'willful noncompliance; restraints add '
                                                       'injury, deconditioning, and dignity loss. '
                                                       'Least-restrictive '
                                                       'alternatives—supervision, alarms, '
                                                       'scheduled toileting, and meaningful '
                                                       'activity—address causes while preserving '
                                                       'mobility. Safety planning should escalate '
                                                       'restrictiveness only as clinical necessity '
                                                       'demands.'},
                                       {'question': 'Heart failure in elderly nursing weight tip?',
                                        'options': ['A) Weigh at random times on different scales '
                                                    'without reporting',
                                                    'B) Same scale, same time, report gain per '
                                                    'parameters',
                                                    'C) Ignore a 3-pound overnight gain if the '
                                                    'patient feels fine',
                                                    'D) Restrict weighing to monthly clinic visits '
                                                    'only'],
                                        'answer': 'B) Same scale, same time, report gain per '
                                                  'parameters',
                                        'explanation': 'In elderly patients with heart failure, '
                                                       'daily weights on the same scale at the '
                                                       'same time detect early sodium and water '
                                                       'retention before pulmonary edema is '
                                                       'obvious. Reporting gains that exceed '
                                                       'parameters allows timely diuretic '
                                                       'adjustment. Consistent technique reduces '
                                                       'noise so true preload changes are '
                                                       'visible.'}],
                              'extreme': [{'question': 'Hip fracture post-fall priority?',
                                           'options': ['A) Ambulate immediately to prevent '
                                                       'pneumonia before imaging',
                                                       'B) Give a full meal before pain control '
                                                       'and immobilization',
                                                       'C) ABC, pain, immobilize as trained, '
                                                       'neurovascular checks, urgent ortho path',
                                                       'D) Remove the cervical collar early to '
                                                       'improve comfort first'],
                                           'answer': 'C) ABC, pain, immobilize as trained, '
                                                     'neurovascular checks, urgent ortho path',
                                           'explanation': 'Hip fracture after a fall commonly '
                                                          'produces occult blood loss, severe '
                                                          'pain-related hypoventilation, and '
                                                          'neurovascular compromise of the limb, '
                                                          'with high subsequent morbidity in frail '
                                                          'elders. ABC assessment, analgesia, '
                                                          'proper immobilization, and '
                                                          'neurovascular checks stabilize the '
                                                          'patient while urgent orthopedic care is '
                                                          'arranged. Early physiologic support '
                                                          'influences both survival and functional '
                                                          'recovery.'},
                                          {'question': 'Sepsis in frail elder may present as?',
                                           'options': ['A) High fever must be present before '
                                                       'sepsis is considered',
                                                       'B) Confusion can be dismissed as normal '
                                                       'aging',
                                                       'C) Weakness without fever never warrants '
                                                       'urgent workup',
                                                       'D) Subtle confusion/weakness without high '
                                                       'fever — still urgent'],
                                           'answer': 'D) Subtle confusion/weakness without high '
                                                     'fever — still urgent',
                                           'explanation': 'Frailty and immunosenescence blunt '
                                                          'classic febrile responses, so sepsis in '
                                                          'older adults may appear only as subtle '
                                                          'confusion, weakness, or functional '
                                                          'collapse without high fever. The same '
                                                          'dysregulated infection physiology still '
                                                          'progresses to shock and organ failure. '
                                                          'A low threshold for urgent evaluation '
                                                          'prevents under-triage of '
                                                          'life-threatening infection.'},
                                          {'question': 'Advance directive conflict at EOL?',
                                           'options': ['A) Follow valid patient wishes/legal '
                                                       'documents with ethics/team support',
                                                       'B) Let the loudest family member override '
                                                       'valid directives',
                                                       'C) Ignore advance directives if staff '
                                                       'disagree personally',
                                                       'D) Start all aggressive interventions '
                                                       'despite a clear refusal document'],
                                           'answer': 'A) Follow valid patient wishes/legal '
                                                     'documents with ethics/team support',
                                           'explanation': 'Valid advance directives and legally '
                                                          'designated proxies express the '
                                                          'patient’s autonomous goals when the '
                                                          'patient can no longer speak. When '
                                                          'conflict arises at end of life, ethics '
                                                          'and interdisciplinary support help '
                                                          'interpret documents and reconcile '
                                                          'family distress with those known '
                                                          'wishes. Care then follows the patient’s '
                                                          'values rather than clinician or family '
                                                          'preference alone.'}]},
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
        "🔬 *CharaNas Nursing*\n"
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
