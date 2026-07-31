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
                  'questions': {'easy': [{'question': 'Which set of measurements constitutes the '
                                                      'core vital-sign assessment used to trend '
                                                      'early physiologic change?',
                                          'options': ['A) Temperature, pulse, respiration, blood '
                                                      'pressure (± SpO2/pain)',
                                                      'B) Daily weight, intake/output, and focused '
                                                      'pain score without cardiopulmonary vitals',
                                                      'C) Continuous ECG monitoring alone without '
                                                      'temperature or blood pressure',
                                                      'D) Pupil size and Glasgow Coma Scale as the '
                                                      'only trending measures'],
                                          'answer': 'A) Temperature, pulse, respiration, blood '
                                                    'pressure (± SpO2/pain)',
                                          'explanation': 'Vital signs index thermoregulation, '
                                                         'cardiac output, ventilation, and '
                                                         'vascular tone. Temperature, pulse, '
                                                         'respiration, and blood pressure—often '
                                                         'with SpO2 and pain—form the baseline '
                                                         'nurses use to detect deterioration; '
                                                         'trends matter more than single values '
                                                         'because compensation can mask illness.',
                                          'choice_explanations': {'A': 'These measures directly '
                                                                       'reflect the core '
                                                                       'physiologic signals nurses '
                                                                       'trend for early '
                                                                       'deterioration.',
                                                                  'B': 'Weight, I&O, and pain '
                                                                       'inform fluid and comfort '
                                                                       'status but omit the '
                                                                       'cardiopulmonary/thermoregulatory '
                                                                       'set that defines classic '
                                                                       'vital signs—easy to '
                                                                       'confuse with “assessment.”',
                                                                  'C': 'ECG tracks rhythm but does '
                                                                       'not replace temperature, '
                                                                       'blood pressure, or '
                                                                       'respiratory assessment as '
                                                                       'the standard vital-sign '
                                                                       'set.',
                                                                  'D': 'Pupils and GCS assess '
                                                                       'neurologic status; they '
                                                                       'complement but do not '
                                                                       'substitute for vital '
                                                                       'signs.'}},
                                         {'question': 'Why is hand hygiene considered the '
                                                      'highest-yield routine infection-control '
                                                      'practice in direct patient care?',
                                          'options': ['A) It replaces sterile technique for all '
                                                      'invasive procedures',
                                                      'B) It reduces transient flora that drives '
                                                      'cross-transmission between contacts',
                                                      'C) It eliminates any need for gloves during '
                                                      'wound care',
                                                      'D) It is most important after invasive '
                                                      'procedures, so routine contact hygiene can '
                                                      'be brief'],
                                          'answer': 'B) It reduces transient flora that drives '
                                                    'cross-transmission between contacts',
                                          'explanation': 'Transient microorganisms on hands are a '
                                                         'major vehicle for healthcare-associated '
                                                         'infection. Hand hygiene lowers microbial '
                                                         'load before and after contact, '
                                                         'interrupting cross-transmission. Gloves '
                                                         'are an adjunct, not a substitute.',
                                          'choice_explanations': {'A': 'Sterile technique protects '
                                                                       'invasive fields; hand '
                                                                       'hygiene does not replace '
                                                                       'asepsis for sterile '
                                                                       'procedures.',
                                                                  'B': 'Reducing transient hand '
                                                                       'flora interrupts the most '
                                                                       'common pathway of '
                                                                       'contact-mediated pathogen '
                                                                       'transfer.',
                                                                  'C': 'Gloves are barriers, yet '
                                                                       'contamination still '
                                                                       'occurs; hygiene is '
                                                                       'required before donning '
                                                                       'and after removing gloves.',
                                                                  'D': 'Prioritizing hygiene '
                                                                       'mainly after invasive work '
                                                                       'underestimates routine '
                                                                       'contact transmission—the '
                                                                       'overlapping “when it '
                                                                       'matters most” '
                                                                       'distractor.'}},
                                         {'question': 'Which elements are required for valid '
                                                      'informed consent before an invasive '
                                                      'procedure?',
                                          'options': ['A) Verbal assent without documenting risks '
                                                      'or alternatives',
                                                      'B) A signed consent form plus family verbal '
                                                      'approval when the patient seems hesitant',
                                                      'C) Understanding of procedure, risks, '
                                                      'alternatives, and voluntary agreement',
                                                      'D) Nurse signature alone without explaining '
                                                      'the procedure to the patient'],
                                          'answer': 'C) Understanding of procedure, risks, '
                                                    'alternatives, and voluntary agreement',
                                          'explanation': 'Informed consent requires that a '
                                                         'capacitated patient understand the '
                                                         'procedure, material risks and benefits, '
                                                         'and reasonable alternatives, then agree '
                                                         'voluntarily. The proceduralist obtains '
                                                         'consent; the nurse verifies '
                                                         'understanding and advocates if doubts '
                                                         'arise.',
                                          'choice_explanations': {'A': 'Undocumented verbal assent '
                                                                       'fails to show that '
                                                                       'material risks and '
                                                                       'alternatives were '
                                                                       'discussed and understood.',
                                                                  'B': 'A signature with family '
                                                                       'approval when the patient '
                                                                       'hesitates looks like '
                                                                       '“consent complete” but may '
                                                                       'mask inadequate '
                                                                       'understanding or '
                                                                       'coercion—classic '
                                                                       'near-miss.',
                                                                  'C': 'Understanding plus '
                                                                       'voluntary agreement after '
                                                                       'disclosure of procedure, '
                                                                       'risks, and alternatives is '
                                                                       'required.',
                                                                  'D': 'A signature without '
                                                                       'disclosure does not '
                                                                       'demonstrate understanding '
                                                                       'of risks, benefits, or '
                                                                       'alternatives.'}}],
                                'medium': [{'question': 'About 20 minutes after an IV opioid, the '
                                                        'patient rates pain 8/10 and is newly '
                                                        'drowsy with RR 9. What is the best '
                                                        'immediate nursing judgment?',
                                            'options': ['A) Reassess pain at the opioid peak and '
                                                        'give a non-opioid adjuvant while '
                                                        'continuing the current opioid plan',
                                                        'B) Give the next scheduled opioid dose '
                                                        'early because pain remains high',
                                                        'C) Document the score only and reassess '
                                                        'at the next routine vital-sign time',
                                                        'D) Hold further opioid, stimulate '
                                                        'respiration, assess sedation/SpO2, and '
                                                        'notify the provider'],
                                            'answer': 'D) Hold further opioid, stimulate '
                                                      'respiration, assess sedation/SpO2, and '
                                                      'notify the provider',
                                            'explanation': 'High pain with new opioid-related '
                                                           'sedation and hypoventilation signals '
                                                           'analgesic effect overlapping with '
                                                           'respiratory depression. Protect '
                                                           'ventilation first—stimulate, support '
                                                           'airway/oxygenation, hold opioid, and '
                                                           'escalate—before chasing pain scores '
                                                           'alone.',
                                            'choice_explanations': {'A': 'Peak-effect pain '
                                                                         'reassessment with an '
                                                                         'adjuvant is usually good '
                                                                         'practice, but continuing '
                                                                         'the opioid plan when RR '
                                                                         'is 9 ignores acute '
                                                                         'respiratory '
                                                                         'depression—priority '
                                                                         'cousin that creates '
                                                                         'doubt.',
                                                                    'B': 'Giving more opioid when '
                                                                         'RR is already 9 can '
                                                                         'deepen hypoventilation '
                                                                         'and precipitate arrest.',
                                                                    'C': 'Waiting for routine '
                                                                         'vitals delays '
                                                                         'recognition of '
                                                                         'progressive respiratory '
                                                                         'depression.',
                                                                    'D': 'Holding opioid while '
                                                                         'assessing '
                                                                         'sedation/ventilation and '
                                                                         'notifying the provider '
                                                                         'addresses the '
                                                                         'life-threatening risk.'}},
                                           {'question': 'An ambulatory older adult scores high on '
                                                        'fall risk and needs to toilet at night. '
                                                        'Which intervention best applies '
                                                        'fall-prevention principles?',
                                            'options': ['A) Place the call light in reach, use '
                                                        'nonslip footwear, and clear the path to a '
                                                        'nearby toilet',
                                                        'B) Keep the bed in mid-high position with '
                                                        'side rails up so toileting requires a '
                                                        'call for full lift assist',
                                                        'C) Withhold diuretics indefinitely so '
                                                        'nighttime toileting never occurs',
                                                        'D) Restrain the patient in a chair '
                                                        'whenever staff are busy'],
                                            'answer': 'A) Place the call light in reach, use '
                                                      'nonslip footwear, and clear the path to a '
                                                      'nearby toilet',
                                            'explanation': 'Fall prevention targets modifiable '
                                                           'hazards: ensure the patient can call '
                                                           'for help, wear stable footwear, and '
                                                           'navigate a clear path. Restraints and '
                                                           'poorly planned barriers can increase '
                                                           'injury risk.',
                                            'choice_explanations': {'A': 'Call access, nonslip '
                                                                         'footwear, and a clear '
                                                                         'toileting path reduce '
                                                                         'environmental and '
                                                                         'mobility fall risk.',
                                                                    'B': 'High bed/rails “for '
                                                                         'safety” sounds '
                                                                         'protective but increases '
                                                                         'fall-from-height and '
                                                                         'entrapment risk—common '
                                                                         'priority near-miss.',
                                                                    'C': 'Stopping diuretics '
                                                                         'without an order can '
                                                                         'worsen heart failure or '
                                                                         'hypertension and does '
                                                                         'not replace fall '
                                                                         'precautions.',
                                                                    'D': 'Restraints are a last '
                                                                         'resort with specific '
                                                                         'orders; they increase '
                                                                         'agitation and injury '
                                                                         'risk.'}},
                                           {'question': 'You enter a room to draw blood on a '
                                                        'patient with unknown infection status. '
                                                        'Which statement correctly applies '
                                                        'standard precautions?',
                                            'options': ['A) Standard precautions are used only '
                                                        'after culture results confirm a pathogen',
                                                        'B) Assume all blood and body fluids are '
                                                        'potentially infectious and use '
                                                        'appropriate barriers',
                                                        'C) Hand hygiene is unnecessary if gloves '
                                                        'will be worn for the entire procedure',
                                                        'D) Use gloves for the draw, then decide '
                                                        'on gown/mask only if the patient later '
                                                        'reports a known infection'],
                                            'answer': 'B) Assume all blood and body fluids are '
                                                      'potentially infectious and use appropriate '
                                                      'barriers',
                                            'explanation': 'Standard precautions treat all blood '
                                                           'and body fluids as potentially '
                                                           'infectious. Barrier selection is based '
                                                           'on anticipated exposure; gloves plus '
                                                           'hand hygiene are baseline for '
                                                           'phlebotomy.',
                                            'choice_explanations': {'A': 'Transmission risk exists '
                                                                         'before cultures return; '
                                                                         'standard precautions '
                                                                         'apply to all patients.',
                                                                    'B': 'Treating all blood/body '
                                                                         'fluids as infectious and '
                                                                         'matching barriers to '
                                                                         'exposure is the '
                                                                         'definition of standard '
                                                                         'precautions.',
                                                                    'C': 'Gloves do not replace '
                                                                         'hand hygiene; hands are '
                                                                         'contaminated during '
                                                                         'glove removal.',
                                                                    'D': 'Waiting to escalate '
                                                                         'barriers until infection '
                                                                         'is known confuses '
                                                                         'standard with '
                                                                         'transmission-based '
                                                                         'precautions—close '
                                                                         'assessment cousin.'}}],
                                'hard': [{'question': 'You are caring for four patients: one with '
                                                      'new stridor after IV contrast, one '
                                                      'requesting PRN oral analgesic, one due for '
                                                      'routine dressing change, and one asking for '
                                                      'water. Using priority frameworks, which '
                                                      'patient do you assess first?',
                                          'options': ['A) The patient requesting water to prevent '
                                                      'dehydration',
                                                      'B) The patient requesting PRN oral pain '
                                                      'medication who rates pain 9/10',
                                                      'C) The patient with new stridor after IV '
                                                      'contrast',
                                                      'D) The patient due for a scheduled dressing '
                                                      'change'],
                                          'answer': 'C) The patient with new stridor after IV '
                                                    'contrast',
                                          'explanation': 'Airway compromise after contrast '
                                                         'suggests evolving anaphylaxis or airway '
                                                         'edema and outranks comfort and routine '
                                                         'tasks. ABC and acute physiologic threat '
                                                         'determine priority.',
                                          'choice_explanations': {'A': 'Thirst is a '
                                                                       'comfort/hydration need and '
                                                                       'does not outrank acute '
                                                                       'airway threat.',
                                                                  'B': 'Severe pain is a '
                                                                       'legitimate urgent need and '
                                                                       'competes for attention, '
                                                                       'but it does not outrank '
                                                                       'new stridor—classic '
                                                                       'priority near-miss.',
                                                                  'C': 'New stridor after contrast '
                                                                       'signals possible airway '
                                                                       'edema/anaphylaxis—the '
                                                                       'highest acute threat.',
                                                                  'D': 'A routine dressing change '
                                                                       'is time-sensitive for '
                                                                       'wound care but not '
                                                                       'immediately '
                                                                       'life-threatening.'}},
                                         {'question': 'A confused patient repeatedly tries to pull '
                                                      'a central line. Soft wrist restraints are '
                                                      'ordered. Which nursing action is required '
                                                      'for safe, lawful restraint use?',
                                          'options': ['A) Apply restraints promptly to protect the '
                                                      'line, then complete a full head-to-toe '
                                                      'assessment before the first release trial',
                                                      'B) Tie restraints to the side rails tightly '
                                                      'so the patient cannot move either arm at '
                                                      'all',
                                                      'C) Leave restraints on continuously without '
                                                      'documentation until discharge',
                                                      'D) Apply restraints, then assess '
                                                      'circulation, sensation, and need for '
                                                      'release at required intervals; attempt '
                                                      'least-restrictive alternatives'],
                                          'answer': 'D) Apply restraints, then assess circulation, '
                                                    'sensation, and need for release at required '
                                                    'intervals; attempt least-restrictive '
                                                    'alternatives',
                                          'explanation': 'Restraints require an order, '
                                                         'least-restrictive alternatives first, '
                                                         'correct application, and frequent '
                                                         'circulatory/skin/behavioral reassessment '
                                                         'with timed release opportunities.',
                                          'choice_explanations': {'A': 'Protecting the line first '
                                                                       'then delaying release '
                                                                       'checks for a “complete '
                                                                       'assessment” sounds '
                                                                       'thorough but violates '
                                                                       'timed restraint '
                                                                       'monitoring—assessment '
                                                                       'cousin near-miss.',
                                                                  'B': 'Tight immobilization to '
                                                                       'side rails risks '
                                                                       'neurovascular injury and '
                                                                       'is improper technique.',
                                                                  'C': 'Continuous use without '
                                                                       'reassessment and '
                                                                       'documentation violates '
                                                                       'restraint standards.',
                                                                  'D': 'Interval neurovascular '
                                                                       'checks, release trials, '
                                                                       'and least-restrictive '
                                                                       'alternatives are required '
                                                                       'for safe lawful use.'}},
                                         {'question': 'Two patients share a room. You bring oral '
                                                      'digoxin for Bed A, but the roommate answers '
                                                      'to the name when you call it from the '
                                                      'doorway. Which action best prevents a '
                                                      'wrong-patient medication error?',
                                          'options': ['A) Verify two unique identifiers at the '
                                                      'bedside with the labeled medication against '
                                                      'the MAR before administering',
                                                      'B) Ask the answering roommate to state date '
                                                      'of birth, then give digoxin if it matches '
                                                      'the MAR',
                                                      'C) Give the dose because the roommate '
                                                      'seemed to recognize the name',
                                                      'D) Ask which bed usually gets digoxin and '
                                                      'administer based on bed location'],
                                          'answer': 'A) Verify two unique identifiers at the '
                                                    'bedside with the labeled medication against '
                                                    'the MAR before administering',
                                          'explanation': 'Wrong-patient errors occur when identity '
                                                         'is not verified at the point of '
                                                         'administration. Two unique identifiers '
                                                         'must match the MAR and labeled drug at '
                                                         'the bedside for the correct patient.',
                                          'choice_explanations': {'A': 'Bedside dual-identifier '
                                                                       'check against the MAR '
                                                                       'links the ordered digoxin '
                                                                       'to the intended patient.',
                                                                  'B': 'DOB from whoever answers '
                                                                       'is a near-miss “identifier '
                                                                       'check” that still fails to '
                                                                       'confirm you are speaking '
                                                                       'to Bed A.',
                                                                  'C': 'A verbal name response '
                                                                       'from the wrong person in a '
                                                                       'shared room is a classic '
                                                                       'error pathway.',
                                                                  'D': 'Bed location is not a '
                                                                       'unique identifier and '
                                                                       'changes with transfers.'}}],
                                'extreme': [{'question': 'You find an unresponsive adult on the '
                                                         'floor with no palpable pulse and agonal '
                                                         'gasps. A visitor insists you wait for '
                                                         'the family to consent before touching '
                                                         'the patient. The charge nurse is on '
                                                         'another unit, and the paper code status '
                                                         'sheet is not in the binder. What is the '
                                                         'immediate priority action?',
                                             'options': ['A) Obtain written family consent before '
                                                         'initiating compressions',
                                                         'B) Start high-quality CPR and activate '
                                                         'the emergency response per protocol '
                                                         'while code status is clarified in '
                                                         'parallel',
                                                         'C) Document a full narrative note, then '
                                                         'return to begin CPR',
                                                         'D) Quickly check the chart for code '
                                                         'status at the desk, then return to begin '
                                                         'compressions if full code'],
                                             'answer': 'B) Start high-quality CPR and activate the '
                                                       'emergency response per protocol while code '
                                                       'status is clarified in parallel',
                                             'explanation': 'Unresponsive, pulseless adults need '
                                                            'immediate CPR. Implied consent covers '
                                                            'emergency resuscitation while code '
                                                            'status is clarified without delaying '
                                                            'compressions.',
                                             'choice_explanations': {'A': 'Written family consent '
                                                                          'is not required before '
                                                                          'emergency CPR in this '
                                                                          'scenario.',
                                                                     'B': 'Immediate CPR plus '
                                                                          'emergency activation is '
                                                                          'the priority; status '
                                                                          'clarification proceeds '
                                                                          'in parallel.',
                                                                     'C': 'Documentation never '
                                                                          'precedes compressions '
                                                                          'in cardiac arrest.',
                                                                     'D': 'Chart verification of '
                                                                          'code status is '
                                                                          'important but leaving a '
                                                                          'pulseless patient to '
                                                                          'retrieve it first is a '
                                                                          'deadly near-miss '
                                                                          'priority error.'}},
                                            {'question': 'Fifteen minutes into a packed RBC '
                                                         'transfusion, the patient develops fever, '
                                                         'back pain, and hypotension. The primary '
                                                         'nurse is off the floor; the blood bank '
                                                         'phone is busy; and a colleague suggests '
                                                         '“finish the unit so none is wasted.” '
                                                         'What is the correct priority sequence?',
                                             'options': ['A) Discard the bag in regular trash so '
                                                         'the reaction cannot be investigated',
                                                         'B) Slow the transfusion markedly, give '
                                                         'antipyretic per protocol, and continue '
                                                         'close vital-sign monitoring',
                                                         'C) Stop the transfusion, maintain IV '
                                                         'access with normal saline, assess ABCs, '
                                                         'and notify the provider/blood bank',
                                                         'D) Increase the rate to finish the unit '
                                                         'quickly, then call the provider'],
                                             'answer': 'C) Stop the transfusion, maintain IV '
                                                       'access with normal saline, assess ABCs, '
                                                       'and notify the provider/blood bank',
                                             'explanation': 'Fever, back pain, and hypotension '
                                                            'during transfusion suggest acute '
                                                            'hemolytic or serious reaction. Stop '
                                                            'the blood, keep IV access with NS, '
                                                            'support ABCs, and notify '
                                                            'provider/blood bank—do not continue '
                                                            'the culprit product.',
                                             'choice_explanations': {'A': 'Discarding evidence '
                                                                          'prevents investigation '
                                                                          'and is unsafe.',
                                                                     'B': 'Slowing and treating '
                                                                          'fever can be '
                                                                          'appropriate for mild '
                                                                          'febrile reactions, but '
                                                                          'hypotension and back '
                                                                          'pain demand '
                                                                          'stopping—not '
                                                                          'titrating—the '
                                                                          'transfusion.',
                                                                     'C': 'Stopping the '
                                                                          'transfusion and '
                                                                          'maintaining saline '
                                                                          'access while escalating '
                                                                          'is the required first '
                                                                          'response.',
                                                                     'D': 'Speeding the unit '
                                                                          'worsens antigen '
                                                                          'exposure during a '
                                                                          'suspected reaction.'}},
                                            {'question': 'Smoke is coming from an electrical '
                                                         'outlet behind an occupied bed. The '
                                                         'patient is alert on 2 L oxygen by nasal '
                                                         'cannula; visitors are in the room; and a '
                                                         'medication cart partially blocks the '
                                                         'doorway. Applying RACE, what is your '
                                                         'first action?',
                                             'options': ['A) Shut off the oxygen at the wall '
                                                         'first, then decide whether the patient '
                                                         'can stay during extinguisher use',
                                                         'B) Pull the fire alarm only after you '
                                                         'finish charting the event',
                                                         'C) Close the door and leave the patient '
                                                         'inside to contain smoke',
                                                         'D) Rescue the patient to a safe area, '
                                                         'removing oxygen from the fire source as '
                                                         'you move'],
                                             'answer': 'D) Rescue the patient to a safe area, '
                                                       'removing oxygen from the fire source as '
                                                       'you move',
                                             'explanation': 'RACE prioritizes Rescue of those in '
                                                            'danger, then Alarm, Contain, '
                                                            'Extinguish/Evacuate. Oxygen feeds '
                                                            'fire; move the patient from the '
                                                            'ignition source promptly.',
                                             'choice_explanations': {'A': 'Oxygen shutoff is '
                                                                          'relevant but delaying '
                                                                          'rescue to fight/contain '
                                                                          'at the bedside is a '
                                                                          'near-miss sequencing '
                                                                          'error.',
                                                                     'B': 'Charting before '
                                                                          'alarm/rescue delays '
                                                                          'life-saving response.',
                                                                     'C': 'Leaving an alert '
                                                                          'patient in a smoking '
                                                                          'room abandons rescue.',
                                                                     'D': 'Rescuing the patient '
                                                                          'away from the outlet '
                                                                          'fire while managing '
                                                                          'oxygen follows '
                                                                          'RACE.'}}]},
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
              'questions': {'easy': [{'question': 'A patient reports new crushing substernal pain '
                                                  'radiating to the left arm. What is the first '
                                                  'nursing priority theme?',
                                      'options': ['A) Encourage ambulation to distract from pain',
                                                  'B) ABCs, oxygen as indicated, ECG, and rapid '
                                                  'notification of the provider',
                                                  'C) Give a full meal tray before any assessment',
                                                  'D) Obtain a full pain history and give ordered '
                                                  'PRN nitroglycerin before any ECG'],
                                      'answer': 'B) ABCs, oxygen as indicated, ECG, and rapid '
                                                'notification of the provider',
                                      'explanation': 'Symptoms suggesting ACS require immediate '
                                                     'ABC support, ECG to detect STEMI, and rapid '
                                                     'escalation. Delaying ECG for extended '
                                                     'history or comfort measures risks missing '
                                                     'time-critical ischemia.',
                                      'choice_explanations': {'A': 'Ambulation increases '
                                                                   'myocardial demand during '
                                                                   'possible coronary occlusion.',
                                                              'B': 'Stabilizing ABCs, obtaining '
                                                                   'ECG, and notifying the '
                                                                   'provider enable timely ACS '
                                                                   'response.',
                                                              'C': 'Oral intake delays evaluation '
                                                                   'and is unsafe if emergent '
                                                                   'procedures are needed.',
                                                              'D': 'Pain history and nitro are '
                                                                   'part of ACS care but must not '
                                                                   'delay ECG/escalation—classic '
                                                                   'priority near-miss.'}},
                                     {'question': 'Why is incentive spirometry emphasized after '
                                                  'abdominal surgery?',
                                      'options': ['A) It replaces the need for early ambulation '
                                                  'entirely',
                                                  'B) It is prioritized mainly to strengthen '
                                                  'accessory muscles so coughing is unnecessary',
                                                  'C) It promotes alveolar expansion and helps '
                                                  'prevent postoperative atelectasis/pneumonia',
                                                  'D) It primarily lowers blood pressure through '
                                                  'vagal stimulation'],
                                      'answer': 'C) It promotes alveolar expansion and helps '
                                                'prevent postoperative atelectasis/pneumonia',
                                      'explanation': 'Shallow breathing after anesthesia and '
                                                     'abdominal pain predisposes to atelectasis. '
                                                     'Incentive spirometry encourages sustained '
                                                     'maximal inspiration, re-expanding alveoli '
                                                     'and reducing pulmonary complications '
                                                     'alongside mobilization.',
                                      'choice_explanations': {'A': 'Ambulation remains essential; '
                                                                   'spirometry complements but '
                                                                   'does not replace mobility.',
                                                              'B': 'Muscle/cough framing is '
                                                                   'related pulmonary hygiene '
                                                                   'thinking but misstates the '
                                                                   'primary mechanism and wrongly '
                                                                   'dismisses coughing.',
                                                              'C': 'Sustained inspiration '
                                                                   're-expands alveoli and is a '
                                                                   'core atelectasis-prevention '
                                                                   'strategy.',
                                                              'D': 'Incentive spirometry targets '
                                                                   'lung expansion, not '
                                                                   'blood-pressure reduction.'}},
                                     {'question': 'Which early findings most classically suggest '
                                                  'hypoglycemia in an alert diabetic patient?',
                                      'options': ['A) Polyuria, polydipsia, and new blurred vision '
                                                  'suggesting glucose imbalance',
                                                  'B) Painless jaundice with clay-colored stools',
                                                  'C) Isolated ankle edema without autonomic '
                                                  'symptoms',
                                                  'D) Diaphoresis, tremor, tachycardia, hunger, '
                                                  'and confusion'],
                                      'answer': 'D) Diaphoresis, tremor, tachycardia, hunger, and '
                                                'confusion',
                                      'explanation': 'Neuroglycopenic and autonomic responses to '
                                                     'low glucose produce sweating, tremor, '
                                                     'palpitations, hunger, and altered mentation. '
                                                     'Recognizing these cues allows rapid glucose '
                                                     'rescue before seizure or coma.',
                                      'choice_explanations': {'A': 'Polyuria/polydipsia/blurred '
                                                                   'vision suggest '
                                                                   'hyperglycemia—glucose-imbalance '
                                                                   'cousin that creates doubt.',
                                                              'B': 'Painless jaundice suggests '
                                                                   'biliary/hepatic disease, not '
                                                                   'low glucose.',
                                                              'C': 'Isolated edema is not an early '
                                                                   'hypoglycemia signature.',
                                                              'D': 'Autonomic and neuroglycopenic '
                                                                   'signs are the classic early '
                                                                   'hypoglycemia pattern.'}}],
                            'medium': [{'question': 'A patient with heart failure gains 2.5 kg '
                                                    'overnight and reports orthopnea. What does '
                                                    'this finding most likely indicate?',
                                        'options': ['A) Worsening fluid retention requiring '
                                                    'assessment of volume status and provider '
                                                    'notification',
                                                    'B) Possible inadequate pain control causing '
                                                    'shallow breathing that should be treated '
                                                    'before volume assessment',
                                                    'C) Expected muscle gain from one night of '
                                                    'bedrest',
                                                    'D) Adequate diuresis and readiness for '
                                                    'discharge teaching only'],
                                        'answer': 'A) Worsening fluid retention requiring '
                                                  'assessment of volume status and provider '
                                                  'notification',
                                        'explanation': 'Rapid overnight weight gain with orthopnea '
                                                       'reflects increasing volume in heart '
                                                       'failure. Nurses trend daily weights as an '
                                                       'early congestion marker and escalate for '
                                                       'possible diuretic adjustment.',
                                        'choice_explanations': {'A': 'Acute weight gain plus '
                                                                     'orthopnea signals congesting '
                                                                     'heart failure needing volume '
                                                                     'assessment and notification.',
                                                                'B': 'Pain-related shallow '
                                                                     'breathing is a real '
                                                                     'postoperative concern but '
                                                                     'does not explain 2.5 kg '
                                                                     'overnight gain with '
                                                                     'orthopnea—assessment '
                                                                     'near-miss.',
                                                                'C': 'Muscle mass does not '
                                                                     'increase overnight; '
                                                                     'kilogram-scale gains are '
                                                                     'fluid.',
                                                                'D': 'Orthopnea and weight gain '
                                                                     'contradict adequate '
                                                                     'diuresis.'}},
                                       {'question': 'After blind NG tube insertion for feeding, '
                                                    'which confirmation method is the gold '
                                                    'standard before first use?',
                                        'options': ['A) Assuming correct placement if the patient '
                                                    'does not cough during insertion',
                                                    'B) Radiographic verification of tip position '
                                                    'per protocol before first use',
                                                    'C) Checking that the external tube length '
                                                    'looks unchanged from another patient',
                                                    'D) pH testing of aspirate plus air '
                                                    'auscultation over the stomach if the external '
                                                    'marking is unchanged'],
                                        'answer': 'B) Radiographic verification of tip position '
                                                  'per protocol before first use',
                                        'explanation': 'Radiographic confirmation is the accepted '
                                                       'gold standard before initiating feedings '
                                                       'because bedside checks can miss '
                                                       'respiratory placements. Incorrect NG '
                                                       'position risks aspiration pneumonia.',
                                        'choice_explanations': {'A': 'Patients may not cough with '
                                                                     'pulmonary placement, '
                                                                     'especially if sedated.',
                                                                'B': 'X-ray confirmation verifies '
                                                                     'tip location before feeding, '
                                                                     'preventing unrecognized '
                                                                     'pulmonary placement.',
                                                                'C': 'External length from another '
                                                                     'patient is irrelevant to '
                                                                     'this patient’s anatomy.',
                                                                'D': 'pH plus auscultation are '
                                                                     'common bedside checks and '
                                                                     'sound confirmatory, but they '
                                                                     'are not the gold standard '
                                                                     'before first use.'}},
                                       {'question': 'Which nursing plan best applies '
                                                    'evidence-based prevention of '
                                                    'hospital-acquired DVT in a postoperative '
                                                    'adult?',
                                        'options': ['A) Massage calves vigorously every hour to '
                                                    '“break up clots”',
                                                    'B) Antiembolism stockings alone while keeping '
                                                    'the patient on bedrest until the incision is '
                                                    'fully healed',
                                                    'C) Early ambulation, anticoagulation as '
                                                    'ordered, and mechanical prophylaxis when '
                                                    'indicated',
                                                    'D) Encourage prolonged bedrest to protect the '
                                                    'incision'],
                                        'answer': 'C) Early ambulation, anticoagulation as '
                                                  'ordered, and mechanical prophylaxis when '
                                                  'indicated',
                                        'explanation': 'Venous stasis, endothelial injury, and '
                                                       'hypercoagulability drive postoperative '
                                                       'DVT. Early ambulation, ordered '
                                                       'pharmacologic prophylaxis, and mechanical '
                                                       'devices reduce risk.',
                                        'choice_explanations': {'A': 'Massaging a potential deep '
                                                                     'vein thrombus can embolize '
                                                                     'clot to the lungs.',
                                                                'B': 'Stockings without ambulation '
                                                                     'are incomplete '
                                                                     'prophylaxis—mechanical '
                                                                     'cousin that creates false '
                                                                     'reassurance.',
                                                                'C': 'Ambulation plus '
                                                                     'pharmacologic/mechanical '
                                                                     'prophylaxis targets the '
                                                                     'major preventable factors.',
                                                                'D': 'Immobility worsens venous '
                                                                     'stasis, the opposite of DVT '
                                                                     'prevention.'}}],
                            'hard': [{'question': 'On postoperative day 2, a patient has fever '
                                                  '38.9°C, HR 122, RR 28, BP 88/50, and new '
                                                  'confusion. Lactate is pending. What is the '
                                                  'priority nursing recognition and action theme?',
                                      'options': ['A) Treat fever and tachycardia as expected '
                                                  'day-2 inflammation; recheck vitals in an hour '
                                                  'if BP stays near baseline',
                                                  'B) Attribute confusion to sundowning and defer '
                                                  'vital-sign reassessment',
                                                  'C) Focus only on wound packing because '
                                                  'infection must be localized',
                                                  'D) Recognize possible sepsis/shock, support '
                                                  'ABCs, obtain cultures/labs per protocol, and '
                                                  'escalate urgently'],
                                      'answer': 'D) Recognize possible sepsis/shock, support ABCs, '
                                                'obtain cultures/labs per protocol, and escalate '
                                                'urgently',
                                      'explanation': 'Tachycardia, tachypnea, hypotension, fever, '
                                                     'and acute confusion after surgery indicate '
                                                     'possible sepsis with hypoperfusion. Early '
                                                     'recognition, ABC support, cultures/labs, and '
                                                     'escalation are required.',
                                      'choice_explanations': {'A': '“Expected postoperative fever” '
                                                                   'is a dangerous near-miss when '
                                                                   'hypotension and confusion are '
                                                                   'present.',
                                                              'B': 'New confusion with abnormal '
                                                                   'vitals is delirium of acute '
                                                                   'illness until proven '
                                                                   'otherwise.',
                                                              'C': 'Systemic hypoperfusion '
                                                                   'outranks isolated wound care; '
                                                                   'source control follows '
                                                                   'resuscitation.',
                                                              'D': 'Multi-cue sepsis/shock '
                                                                   'recognition with ABC support '
                                                                   'and urgent escalation matches '
                                                                   'priority frameworks.'}},
                                     {'question': 'A COPD patient on high-flow oxygen becomes '
                                                  'increasingly drowsy with rising PaCO2 on ABG. '
                                                  'What is the main nursing concern?',
                                      'options': ['A) Oxygen-related CO2 retention/hypoventilation '
                                                  'requiring reassessment of O2 target and '
                                                  'ventilatory status',
                                                  'B) Progressive fatigue from work of breathing '
                                                  'that should be treated mainly with incentive '
                                                  'spirometry coaching',
                                                  'C) Expected sedation from improved oxygenation '
                                                  'that needs no follow-up',
                                                  'D) Hyperactive delirium that should be treated '
                                                  'with a benzodiazepine first'],
                                      'answer': 'A) Oxygen-related CO2 retention/hypoventilation '
                                                'requiring reassessment of O2 target and '
                                                'ventilatory status',
                                      'explanation': 'Some COPD patients worsen V/Q mismatch or '
                                                     'retain CO2 on excessive oxygen, producing '
                                                     'narcosis. Drowsiness with rising PaCO2 '
                                                     'mandates titration toward SpO2 targets and '
                                                     'ventilatory support assessment.',
                                      'choice_explanations': {'A': 'Drowsiness plus rising PaCO2 '
                                                                   'on high O2 signals CO2 '
                                                                   'retention needing O2 titration '
                                                                   'and ventilatory reassessment.',
                                                              'B': 'Work-of-breathing fatigue is '
                                                                   'related respiratory assessment '
                                                                   'thinking but misses '
                                                                   'oxygen-driven hypercapnia as '
                                                                   'the key concern.',
                                                              'C': 'Progressive drowsiness with '
                                                                   'hypercapnia is dangerous, not '
                                                                   'a benign effect of oxygen.',
                                                              'D': 'Benzodiazepines further '
                                                                   'depress ventilation in '
                                                                   'hypercapnic COPD.'}},
                                     {'question': 'Four hours after thyroidectomy, the patient '
                                                  'reports neck tightness, has stridor, and SpO2 '
                                                  'is falling. What is the priority concern?',
                                      'options': ['A) Expected sore throat that can wait until '
                                                  'morning rounds',
                                                  'B) Airway compression from hematoma/edema '
                                                  'requiring immediate airway support and surgical '
                                                  'notification',
                                                  'C) Anxiety alone; coach slow breathing without '
                                                  'assessing the neck',
                                                  'D) Early hypocalcemia after parathyroid '
                                                  'disturbance causing neuromuscular '
                                                  'irritability—give calcium and observe'],
                                      'answer': 'B) Airway compression from hematoma/edema '
                                                'requiring immediate airway support and surgical '
                                                'notification',
                                      'explanation': 'Neck hematoma or edema after thyroidectomy '
                                                     'can rapidly obstruct the airway. Stridor, '
                                                     'tightness, and desaturation demand immediate '
                                                     'airway management and surgeon notification.',
                                      'choice_explanations': {'A': 'Stridor and desaturation are '
                                                                   'not routine sore throat.',
                                                              'B': 'Airway compression from '
                                                                   'postoperative hematoma/edema '
                                                                   'is the life-threatening '
                                                                   'priority.',
                                                              'C': 'Anxiety coaching without '
                                                                   'airway assessment ignores '
                                                                   'objective stridor and hypoxia.',
                                                              'D': 'Hypocalcemia is a real '
                                                                   'post-thyroidectomy '
                                                                   'complication (assessment '
                                                                   'cousin) but usually later with '
                                                                   'tetany/paresthesias—not acute '
                                                                   'stridor and falling SpO2 hours '
                                                                   'after surgery.'}}],
                            'extreme': [{'question': 'Two minutes after starting IV ceftriaxone, a '
                                                     'patient develops urticaria, wheezing, BP '
                                                     '70/40, and a sense of doom. The provider’s '
                                                     'phone goes to voicemail. An order set on the '
                                                     'chart lists “diphenhydramine 25 mg PO PRN '
                                                     'itch.” What is the first drug/action '
                                                     'priority?',
                                         'options': ['A) Start a fluid bolus only and defer '
                                                     'epinephrine until allergy testing is done',
                                                     'B) Stop the infusion, give IV '
                                                     'diphenhydramine and fluids first, and '
                                                     'reserve epinephrine if wheeze persists',
                                                     'C) Stop the infusion and give intramuscular '
                                                     'epinephrine per anaphylaxis protocol while '
                                                     'activating emergency response',
                                                     'D) Give the PRN oral diphenhydramine and '
                                                     'continue the antibiotic infusion'],
                                         'answer': 'C) Stop the infusion and give intramuscular '
                                                   'epinephrine per anaphylaxis protocol while '
                                                   'activating emergency response',
                                         'explanation': 'Urticaria, wheezing, hypotension, and '
                                                        'doom after IV antibiotic indicate '
                                                        'anaphylaxis. Stop the trigger and give IM '
                                                        'epinephrine promptly while activating '
                                                        'help—antihistamines are adjuncts, not '
                                                        'first-line for shock.',
                                         'choice_explanations': {'A': 'Deferring epinephrine for '
                                                                      'testing during hypotension '
                                                                      'is dangerous.',
                                                                 'B': 'Antihistamine-and-fluids-first '
                                                                      'is a common near-miss that '
                                                                      'delays epinephrine in '
                                                                      'anaphylactic shock.',
                                                                 'C': 'Stopping the drug and '
                                                                      'giving IM epinephrine with '
                                                                      'emergency activation is '
                                                                      'first-line anaphylaxis '
                                                                      'care.',
                                                                 'D': 'Continuing the antigen '
                                                                      'while giving oral '
                                                                      'antihistamine worsens '
                                                                      'anaphylaxis.'}},
                                        {'question': 'A patient with known lung cancer suddenly '
                                                     'coughs up large volumes of bright red blood, '
                                                     'SpO2 82% on room air, and becomes pale and '
                                                     'anxious. Radiology wants him transported now '
                                                     'for a non-urgent staging CT. What is the '
                                                     'nursing priority?',
                                         'options': ['A) Obtain urgent imaging to localize '
                                                     'bleeding while applying oxygen by nasal '
                                                     'cannula en route',
                                                     'B) Encourage oral fluids to “replace” blood '
                                                     'loss',
                                                     'C) Have the patient ambulate to reduce clot '
                                                     'formation in the airways',
                                                     'D) Protect the airway/oxygenation, position '
                                                     'for drainage as trained, activate rapid '
                                                     'response, and defer non-urgent transport'],
                                         'answer': 'D) Protect the airway/oxygenation, position '
                                                   'for drainage as trained, activate rapid '
                                                   'response, and defer non-urgent transport',
                                         'explanation': 'Massive hemoptysis with hypoxemia is an '
                                                        'airway emergency. Stabilize '
                                                        'oxygenation/airway and escalate before '
                                                        'diagnostic transport.',
                                         'choice_explanations': {'A': 'Imaging is diagnostically '
                                                                      'tempting but sending an '
                                                                      'unstable bleeding patient '
                                                                      'to CT first is a classic '
                                                                      'priority near-miss.',
                                                                 'B': 'Oral fluids do not treat '
                                                                      'airway hemorrhage or '
                                                                      'hypoxia.',
                                                                 'C': 'Ambulation increases oxygen '
                                                                      'demand and aspiration/bleed '
                                                                      'risk.',
                                                                 'D': 'Airway/oxygenation '
                                                                      'protection with rapid '
                                                                      'response outranks immediate '
                                                                      'CT.'}},
                                        {'question': 'Six hours after cast application for a '
                                                     'tibial fracture, the patient reports severe '
                                                     'pain unrelieved by opioids, numbness in the '
                                                     'toes, and pain on passive stretch. Pedal '
                                                     'pulses are still Dopplerable. The on-call '
                                                     'provider says “pulses are present, so it '
                                                     'cannot be compartment syndrome—give more '
                                                     'morphine.” What should you do?',
                                         'options': ['A) Escalate urgently for compartment '
                                                     'syndrome evaluation; pulses can remain until '
                                                     'late',
                                                     'B) Elevate the casted limb, ice the site, '
                                                     'and increase analgesia while monitoring '
                                                     'pulses hourly',
                                                     'C) Accept max opioids without further '
                                                     'neurovascular assessment',
                                                     'D) Remove the cast yourself immediately '
                                                     'without notifying the provider or surgeon'],
                                         'answer': 'A) Escalate urgently for compartment syndrome '
                                                   'evaluation; pulses can remain until late',
                                         'explanation': 'Severe pain out of proportion, passive '
                                                        'stretch pain, and numbness after casting '
                                                        'suggest compartment syndrome. Pulses may '
                                                        'persist until late; urgent surgical '
                                                        'evaluation is required.',
                                         'choice_explanations': {'A': 'Urgent escalation for '
                                                                      'compartment syndrome is '
                                                                      'required even if pulses are '
                                                                      'present.',
                                                                 'B': 'Elevation/ice/analgesia is '
                                                                      'usual cast care and sounds '
                                                                      'reasonable, but pain out of '
                                                                      'proportion with stretch '
                                                                      'pain needs immediate '
                                                                      'escalation—not routine '
                                                                      'comfort measures alone.',
                                                                 'C': 'Masking pain with opioids '
                                                                      'without reassessment delays '
                                                                      'diagnosis.',
                                                                 'D': 'Unauthorized cast removal '
                                                                      'can injure tissue; notify '
                                                                      'surgical team for timed '
                                                                      'intervention.'}}]},
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
                'questions': {'easy': [{'question': 'For a healthy 2-month-old needing an '
                                                    'intramuscular vaccine, which site is '
                                                    'generally preferred?',
                                        'options': ['A) Deltoid only, regardless of muscle mass',
                                                    'B) Ventrogluteal site if landmarks feel clear '
                                                    'on a chubby infant',
                                                    'C) Vastus lateralis (anterolateral thigh)',
                                                    'D) Dorsogluteal muscle to avoid the sciatic '
                                                    'nerve'],
                                        'answer': 'C) Vastus lateralis (anterolateral thigh)',
                                        'explanation': 'In young infants the vastus lateralis has '
                                                       'adequate muscle mass and avoids major '
                                                       'nerves and vessels. Deltoid mass is often '
                                                       'insufficient early on; dorsogluteal '
                                                       'injections risk sciatic injury.',
                                        'choice_explanations': {'A': 'Infant deltoid mass is often '
                                                                     'inadequate for safe IM '
                                                                     'injection.',
                                                                'B': 'Ventrogluteal can be used in '
                                                                     'older children/adults and '
                                                                     'may seem “safer,” but it is '
                                                                     'not the preferred '
                                                                     'early-infancy default.',
                                                                'C': 'The anterolateral thigh '
                                                                     '(vastus lateralis) is the '
                                                                     'recommended IM site for '
                                                                     'young infants.',
                                                                'D': 'Dorsogluteal injections risk '
                                                                     'sciatic nerve injury and are '
                                                                     'not preferred in infants.'}},
                                       {'question': 'Pediatric medication doses are most commonly '
                                                    'calculated using which patient factor?',
                                        'options': ['A) Age in years rounded to the nearest adult '
                                                    'fraction (e.g., half-dose at age 8)',
                                                    'B) Shoe size as a surrogate for maturity',
                                                    'C) Room number to standardize unit dosing',
                                                    'D) Body weight (and sometimes body surface '
                                                    'area)'],
                                        'answer': 'D) Body weight (and sometimes body surface '
                                                  'area)',
                                        'explanation': 'Children’s pharmacokinetics scale '
                                                       'primarily with body size; weight-based '
                                                       '(mg/kg) and sometimes BSA-based dosing '
                                                       'prevent under- and overdosing.',
                                        'choice_explanations': {'A': 'Age-based adult fractions '
                                                                     'are a common bedside '
                                                                     'shortcut and create dosing '
                                                                     'doubt, but they ignore wide '
                                                                     'weight ranges at the same '
                                                                     'age.',
                                                                'B': 'Shoe size does not determine '
                                                                     'volume of distribution or '
                                                                     'clearance.',
                                                                'C': 'Room number is unrelated to '
                                                                     'dose requirements.',
                                                                'D': 'Weight-based (and sometimes '
                                                                     'BSA) dosing matches '
                                                                     'developmental '
                                                                     'pharmacokinetics.'}},
                                       {'question': 'Anterior fontanelle assessment is clinically '
                                                    'most relevant in which pediatric age group?',
                                        'options': ['A) Infants while the fontanelle remains '
                                                    'patent (typically through early infancy)',
                                                    'B) Any child under 5 years whenever '
                                                    'intracranial pressure might be elevated',
                                                    'C) Only adolescents after growth-plate '
                                                    'closure',
                                                    'D) Only neonates in the first 24 hours of '
                                                    'life'],
                                        'answer': 'A) Infants while the fontanelle remains patent '
                                                  '(typically through early infancy)',
                                        'explanation': 'The anterior fontanelle remains open in '
                                                       'infancy and provides a window on '
                                                       'intracranial pressure and hydration. After '
                                                       'closure, it is no longer available as an '
                                                       'assessment landmark.',
                                        'choice_explanations': {'A': 'Patent fontanelles in '
                                                                     'infants allow pressure and '
                                                                     'hydration cues until '
                                                                     'closure.',
                                                                'B': 'Extending fontanelle '
                                                                     'assessment to all young '
                                                                     'children sounds reasonable '
                                                                     'for ICP concern but is '
                                                                     'anatomically wrong after '
                                                                     'closure—assessment '
                                                                     'near-miss.',
                                                                'C': 'Adolescent cranial sutures '
                                                                     'are closed; fontanelle '
                                                                     'assessment is not '
                                                                     'applicable.',
                                                                'D': 'Assessment matters '
                                                                     'throughout infancy while the '
                                                                     'fontanelle is open, not only '
                                                                     'day one of life.'}}],
                              'medium': [{'question': 'A toddler with gastroenteritis has sunken '
                                                      'eyes, absent tears, dry mucous membranes, '
                                                      'and delayed capillary refill. What do these '
                                                      'signs indicate?',
                                          'options': ['A) Isolated allergic rhinitis unrelated to '
                                                      'volume status',
                                                      'B) Moderate to severe dehydration requiring '
                                                      'urgent fluid assessment and escalation',
                                                      'C) Overhydration from excess free water',
                                                      'D) Mild dehydration manageable with '
                                                      'continued oral challenge because the child '
                                                      'still cries at times'],
                                          'answer': 'B) Moderate to severe dehydration requiring '
                                                    'urgent fluid assessment and escalation',
                                          'explanation': 'Sunken eyes, absent tears, dry mucosa, '
                                                         'and delayed CRT are classic dehydration '
                                                         'signs reflecting volume loss and '
                                                         'impaired perfusion. Pediatric patients '
                                                         'decompensate quickly; escalate for '
                                                         'oral/IV rehydration.',
                                          'choice_explanations': {'A': 'These findings reflect '
                                                                       'volume status, not primary '
                                                                       'rhinitis.',
                                                                  'B': 'Combined mucosal and '
                                                                       'perfusion signs indicate '
                                                                       'clinically important '
                                                                       'dehydration needing urgent '
                                                                       'fluid assessment.',
                                                                  'C': 'Overhydration would not '
                                                                       'produce sunken eyes and '
                                                                       'delayed CRT.',
                                                                  'D': 'Intermittent crying can '
                                                                       'mislead caregivers toward '
                                                                       '“mild” status—overlapping '
                                                                       'hydration assessment '
                                                                       'near-miss.'}},
                                         {'question': 'When is the FLACC pain scale the most '
                                                      'appropriate choice?',
                                          'options': ['A) Only postoperatively in patients with '
                                                      'epidurals',
                                                      'B) For any hospitalized child when vital '
                                                      'signs are abnormal, as a shock-severity '
                                                      'tool',
                                                      'C) For infants/young children who cannot '
                                                      'self-report pain reliably',
                                                      'D) Only for verbal adults who can use a '
                                                      '0–10 numeric rating'],
                                          'answer': 'C) For infants/young children who cannot '
                                                    'self-report pain reliably',
                                          'explanation': 'FLACC scores Face, Legs, Activity, Cry, '
                                                         'and Consolability—behavioral cues used '
                                                         'when children cannot self-report. It '
                                                         'complements but does not replace '
                                                         'hemodynamic assessment.',
                                          'choice_explanations': {'A': 'FLACC is not limited to '
                                                                       'epidural patients; it is '
                                                                       'an age/ability-based tool.',
                                                                  'B': 'Using FLACC as a shock '
                                                                       'tool when vitals are '
                                                                       'abnormal confuses pain '
                                                                       'assessment with perfusion '
                                                                       'triage—cousin near-miss.',
                                                                  'C': 'FLACC is designed for '
                                                                       'preverbal or '
                                                                       'non-self-reporting young '
                                                                       'children.',
                                                                  'D': 'Verbal adults should use '
                                                                       'self-report scales, not '
                                                                       'FLACC.'}},
                                         {'question': 'Nursing care for an infant with RSV '
                                                      'bronchiolitis should primarily focus on '
                                                      'which priorities?',
                                          'options': ['A) Scheduled chest physiotherapy and forced '
                                                      'oral feeds to maintain calories despite '
                                                      'tachypnea',
                                                      'B) Immediate antibiotics for all viral '
                                                      'bronchiolitis',
                                                      'C) Allowing parents to skip isolation if '
                                                      'the child appears playful',
                                                      'D) Airway support, hydration as tolerated, '
                                                      'oxygen/monitoring, and infection control'],
                                          'answer': 'D) Airway support, hydration as tolerated, '
                                                    'oxygen/monitoring, and infection control',
                                          'explanation': 'RSV bronchiolitis care is supportive: '
                                                         'maintain airway and oxygenation, '
                                                         'carefully manage fluids, monitor for '
                                                         'apnea/respiratory failure, and use '
                                                         'contact precautions. Antibiotics treat '
                                                         'bacterial coinfection only.',
                                          'choice_explanations': {'A': 'CPT plus forced feeds '
                                                                       'sounds like active '
                                                                       '“respiratory care” but can '
                                                                       'increase distress and '
                                                                       'aspiration risk—priority '
                                                                       'near-miss.',
                                                                  'B': 'RSV is viral; antibiotics '
                                                                       'are not routinely '
                                                                       'indicated without '
                                                                       'bacterial infection.',
                                                                  'C': 'Playfulness does not '
                                                                       'remove transmission '
                                                                       'precautions.',
                                                                  'D': 'Supportive '
                                                                       'airway/oxygen/hydration '
                                                                       'care with isolation '
                                                                       'precautions matches '
                                                                       'evidence-based '
                                                                       'priorities.'}}],
                              'hard': [{'question': 'A toddler has patterned burns and a changing '
                                                    'caregiver story. The child is hemodynamically '
                                                    'stable. What is the nurse’s legal and ethical '
                                                    'obligation?',
                                        'options': ['A) Report suspected abuse per mandatory '
                                                    'reporting laws and ensure immediate safety',
                                                    'B) Complete a detailed forensic photo series '
                                                    'and confront caregivers for consistency '
                                                    'before reporting',
                                                    'C) Wait until absolute proof is obtained in '
                                                    'court before telling anyone',
                                                    'D) Discharge home quickly to avoid involving '
                                                    'social services'],
                                        'answer': 'A) Report suspected abuse per mandatory '
                                                  'reporting laws and ensure immediate safety',
                                        'explanation': 'Nurses are mandatory reporters: reasonable '
                                                       'suspicion of abuse triggers reporting and '
                                                       'protection, not courtroom-level proof. '
                                                       'Patterned burns with inconsistent history '
                                                       'warrant report and safety planning.',
                                        'choice_explanations': {'A': 'Mandatory reporting plus '
                                                                     'ensuring safety is the '
                                                                     'required nursing response.',
                                                                'B': 'Gathering more “proof” and '
                                                                     'confronting caregivers '
                                                                     'delays protection and can '
                                                                     'contaminate '
                                                                     'investigation—assessment '
                                                                     'cousin near-miss.',
                                                                'C': 'The reporting threshold is '
                                                                     'reasonable suspicion, not '
                                                                     'judicial certainty.',
                                                                'D': 'Discharging to a potentially '
                                                                     'unsafe home violates the '
                                                                     'duty to protect.'}},
                                       {'question': 'A 3-year-old sits forward, drools, and has '
                                                    'stridor with high fever. The caregiver asks '
                                                    'you to look in the throat with a tongue '
                                                    'blade. What is the correct caution?',
                                        'options': ['A) Force the child supine and examine the '
                                                    'pharynx immediately',
                                                    'B) Do not agitate or instrument the airway; '
                                                    'keep the child calm and prepare for emergency '
                                                    'airway management',
                                                    'C) Give a throat lozenge and discharge if '
                                                    'SpO2 is briefly 94%',
                                                    'D) Inspect the throat gently with a tongue '
                                                    'blade while the child remains upright to '
                                                    'confirm epiglottitis'],
                                        'answer': 'B) Do not agitate or instrument the airway; '
                                                  'keep the child calm and prepare for emergency '
                                                  'airway management',
                                        'explanation': 'Tripod posture, drooling, and stridor '
                                                       'suggest epiglottitis or critical '
                                                       'upper-airway obstruction. Stimulating the '
                                                       'airway can cause complete obstruction. '
                                                       'Keep the child calm and prepare for '
                                                       'advanced airway support.',
                                        'choice_explanations': {'A': 'Forcing supine examination '
                                                                     'can precipitate total airway '
                                                                     'loss.',
                                                                'B': 'Avoiding '
                                                                     'agitation/instrumentation '
                                                                     'while preparing advanced '
                                                                     'airway support is the '
                                                                     'correct caution.',
                                                                'C': 'This presentation is a '
                                                                     'life-threatening emergency, '
                                                                     'not a dischargeable sore '
                                                                     'throat.',
                                                                'D': 'A “gentle upright look” '
                                                                     'still instruments/agitates a '
                                                                     'critical airway—dangerous '
                                                                     'near-miss assessment urge.'}},
                                       {'question': 'A child treated for Kawasaki disease is '
                                                    'irritable with persistent fever and a new '
                                                    'gallop. Which complication concern should '
                                                    'guide nursing surveillance?',
                                        'options': ['A) Guaranteed immunity to all future '
                                                    'streptococcal disease',
                                                    'B) Persistent febrile illness with '
                                                    'dehydration risk as the main surveillance '
                                                    'focus',
                                                    'C) Coronary artery aneurysms and myocardial '
                                                    'ischemia/dysfunction',
                                                    'D) Isolated otitis media as the only sequela '
                                                    'of concern'],
                                        'answer': 'C) Coronary artery aneurysms and myocardial '
                                                  'ischemia/dysfunction',
                                        'explanation': 'Kawasaki disease can cause coronary '
                                                       'arteritis and aneurysms, risking ischemia, '
                                                       'infarction, and ventricular dysfunction. '
                                                       'Persistent fever and new gallop heighten '
                                                       'concern for cardiac complications.',
                                        'choice_explanations': {'A': 'Kawasaki treatment does not '
                                                                     'confer streptococcal '
                                                                     'immunity.',
                                                                'B': 'Fever/dehydration vigilance '
                                                                     'is appropriate supportive '
                                                                     'care but misses the defining '
                                                                     'cardiac '
                                                                     'complication—assessment '
                                                                     'near-miss.',
                                                                'C': 'Coronary aneurysms and '
                                                                     'cardiac dysfunction are the '
                                                                     'critical complications '
                                                                     'nurses watch for.',
                                                                'D': 'Otitis is not the defining '
                                                                     'serious sequela of Kawasaki '
                                                                     'disease.'}}],
                              'extreme': [{'question': 'A 6-year-old becomes unresponsive and '
                                                       'pulseless in the playroom after '
                                                       'progressive respiratory distress. An AED '
                                                       'is being attached; a parent is screaming '
                                                       'to “give adult shocks now.” Using '
                                                       'pediatric BLS principles, what compression '
                                                       'approach should you prioritize while the '
                                                       'team prepares defibrillation?',
                                           'options': ['A) Focus on rescue breaths first for a few '
                                                       'minutes because the arrest was respiratory '
                                                       'in origin, then start compressions',
                                                       'B) Compress at adult depth of at least 5 '
                                                       'inches on the xiphoid to be “sure”',
                                                       'C) Wait for a pulse check every 5 seconds '
                                                       'before any compression',
                                                       'D) Start high-quality CPR with chest '
                                                       'compressions to about one-third AP chest '
                                                       'depth (≈5 cm in children) and allow full '
                                                       'recoil'],
                                           'answer': 'D) Start high-quality CPR with chest '
                                                     'compressions to about one-third AP chest '
                                                     'depth (≈5 cm in children) and allow full '
                                                     'recoil',
                                           'explanation': 'Pulseless children need immediate '
                                                          'high-quality CPR. Even when respiratory '
                                                          'failure precedes arrest, current '
                                                          'pediatric BLS emphasizes starting '
                                                          'compressions with ventilations rather '
                                                          'than delaying for breaths-only care.',
                                           'choice_explanations': {'A': 'Respiratory-origin arrest '
                                                                        'tempts a breaths-first '
                                                                        'delay—priority near-miss '
                                                                        'that postpones '
                                                                        'compressions.',
                                                                   'B': 'Adult-depth xiphoid '
                                                                        'compressions risk injury '
                                                                        'and ineffective '
                                                                        'technique.',
                                                                   'C': 'Frequent prolonged pulse '
                                                                        'checks interrupt '
                                                                        'perfusion.',
                                                                   'D': 'Age-appropriate '
                                                                        'compression depth with '
                                                                        'high-quality CPR is the '
                                                                        'correct immediate '
                                                                        'action.'}},
                                          {'question': 'A school-age child with a known peanut '
                                                       'allergy eats a cookie at a party, then '
                                                       'develops facial swelling, wheeze, and BP '
                                                       '78/40. The parent’s epinephrine '
                                                       'auto-injector is available, but a '
                                                       'volunteer insists you “wait for EMS so you '
                                                       'don’t get in trouble.” What should you do?',
                                           'options': ['A) Give epinephrine IM via auto-injector '
                                                       'immediately and activate emergency '
                                                       'services',
                                                       'B) Give oral antihistamine and inhaled '
                                                       'bronchodilator first while waiting to see '
                                                       'if BP improves',
                                                       'C) Wait for EMS arrival before any '
                                                       'medication',
                                                       'D) Have the child walk briskly to “work '
                                                       'off” the reaction'],
                                           'answer': 'A) Give epinephrine IM via auto-injector '
                                                     'immediately and activate emergency services',
                                           'explanation': 'Facial swelling, wheeze, and '
                                                          'hypotension after peanut exposure are '
                                                          'anaphylaxis. IM epinephrine is '
                                                          'first-line and should not be delayed '
                                                          'for antihistamines or EMS arrival.',
                                           'choice_explanations': {'A': 'Immediate IM epinephrine '
                                                                        'plus emergency activation '
                                                                        'is first-line anaphylaxis '
                                                                        'care.',
                                                                   'B': 'Antihistamine/bronchodilator-first '
                                                                        'is a common near-miss '
                                                                        'that delays epinephrine '
                                                                        'in anaphylactic shock.',
                                                                   'C': 'Waiting for EMS delays '
                                                                        'the definitive first '
                                                                        'drug.',
                                                                   'D': 'Ambulation worsens shock '
                                                                        'and hypoxia.'}},
                                          {'question': 'After a high-speed MVC, a child is drowsy '
                                                       'with unequal pupils, HR 58, and BP 150/95. '
                                                       'The cervical collar is in place. A '
                                                       'colleague wants to flex the neck for a '
                                                       '“better airway look” and start hypotonic '
                                                       'free-water fluids wide open. What is the '
                                                       'priority nursing approach?',
                                           'options': ['A) Give free-water boluses to lower sodium '
                                                       'rapidly',
                                                       'B) Protect airway/C-spine, avoid hypotonic '
                                                       'fluids, elevate head of bed if permitted, '
                                                       'and escalate for rising ICP',
                                                       'C) Remove the collar because bradycardia '
                                                       'proves the spine is fine',
                                                       'D) Perform a focused neurologic exam '
                                                       'including neck flexion to localize the '
                                                       'lesion before calling neurosurgery'],
                                           'answer': 'B) Protect airway/C-spine, avoid hypotonic '
                                                     'fluids, elevate head of bed if permitted, '
                                                     'and escalate for rising ICP',
                                           'explanation': 'Unequal pupils, bradycardia, and '
                                                          'hypertension after trauma suggest '
                                                          'rising ICP with herniation risk. '
                                                          'Maintain C-spine precautions, support '
                                                          'airway, avoid hypotonic free water, and '
                                                          'escalate—do not flex the neck.',
                                           'choice_explanations': {'A': 'Free-water boluses can '
                                                                        'worsen cerebral edema.',
                                                                   'B': 'Airway/C-spine protection '
                                                                        'with ICP-minded care and '
                                                                        'escalation is the '
                                                                        'priority cluster.',
                                                                   'C': 'Bradycardia in this '
                                                                        'pattern is a Cushing '
                                                                        'clue, not proof the spine '
                                                                        'is uninjured.',
                                                                   'D': 'A complete neuro exam '
                                                                        'with neck flexion sounds '
                                                                        'assessment-rigorous but '
                                                                        'risks cord injury and ICP '
                                                                        'spikes—near-miss.'}}]},
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
               'questions': {'easy': [{'question': 'What does the APGAR score primarily assess in '
                                                   'the newborn?',
                                       'options': ['A) Overall newborn wellness used to predict '
                                                   'long-term developmental outcomes',
                                                   'B) Maternal blood type compatibility only',
                                                   'C) Exact gestational age in weeks',
                                                   'D) Immediate cardiopulmonary and neuromuscular '
                                                   'transition at 1 and 5 minutes'],
                                       'answer': 'D) Immediate cardiopulmonary and neuromuscular '
                                                 'transition at 1 and 5 minutes',
                                       'explanation': 'APGAR evaluates Appearance, Pulse, Grimace, '
                                                      'Activity, and Respiration to summarize '
                                                      'immediate adaptation and need for '
                                                      'resuscitation support. It is not a '
                                                      'long-term outcome predictor or dating tool.',
                                       'choice_explanations': {'A': 'Treating APGAR as a broad '
                                                                    'wellness/long-term predictor '
                                                                    'is a common '
                                                                    'misunderstanding—assessment '
                                                                    'cousin near-miss.',
                                                               'B': 'Blood type is a separate '
                                                                    'maternal–neonatal lab issue.',
                                                               'C': 'Gestational age uses other '
                                                                    'dating methods, not APGAR.',
                                                               'D': 'It scores immediate '
                                                                    'transition and guides early '
                                                                    'resuscitation needs at 1 and '
                                                                    '5 minutes.'}},
                                      {'question': 'Why is fundal massage performed in the '
                                                   'immediate postpartum period when the uterus is '
                                                   'boggy?',
                                       'options': ['A) To stimulate uterine contraction and reduce '
                                                   'postpartum hemorrhage from atony',
                                                   'B) To express clots and assess lochia amount '
                                                   'before deciding whether the fundus needs '
                                                   'firming',
                                                   'C) To induce lactation within seconds',
                                                   'D) To replace the need for quantifying blood '
                                                   'loss'],
                                       'answer': 'A) To stimulate uterine contraction and reduce '
                                                 'postpartum hemorrhage from atony',
                                       'explanation': 'Uterine atony is a leading cause of '
                                                      'postpartum hemorrhage. Fundal massage '
                                                      'stimulates myometrial contraction, '
                                                      'compressing vessels at the placental site. '
                                                      'It complements—not replaces—quantified '
                                                      'blood-loss assessment and uterotonics.',
                                       'choice_explanations': {'A': 'Contraction from massage '
                                                                    'reduces bleeding from an '
                                                                    'atonic uterus.',
                                                               'B': 'Assessing lochia/clots is '
                                                                    'important but delaying '
                                                                    'firming massage of a boggy '
                                                                    'fundus is a priority '
                                                                    'near-miss.',
                                                               'C': 'Massage does not instantly '
                                                                    'induce lactation.',
                                                               'D': 'Blood loss still must be '
                                                                    'quantified; massage treats '
                                                                    'atony.'}},
                                      {'question': 'An Rh-negative mother delivers an Rh-positive '
                                                   'newborn. Which postpartum intervention may she '
                                                   'need?',
                                       'options': ['A) High-dose vitamin K to the mother instead '
                                                   'of the newborn',
                                                   'B) Rh(D) immune globulin (RhoGAM) as indicated '
                                                   'to prevent sensitization',
                                                   'C) Immediate hysterectomy for sensitization '
                                                   'prevention',
                                                   'D) Type and crossmatch the mother for possible '
                                                   'delayed transfusion if titers rise later'],
                                       'answer': 'B) Rh(D) immune globulin (RhoGAM) as indicated '
                                                 'to prevent sensitization',
                                       'explanation': 'RhIG given when indicated prevents maternal '
                                                      'anti-D formation after exposure to '
                                                      'Rh-positive fetal cells, protecting future '
                                                      'pregnancies from hemolytic disease.',
                                       'choice_explanations': {'A': 'Vitamin K is for newborn '
                                                                    'hemorrhagic disease '
                                                                    'prevention, not maternal Rh '
                                                                    'sensitization.',
                                                               'B': 'RhIG prevents '
                                                                    'alloimmunization in eligible '
                                                                    'Rh-negative mothers.',
                                                               'C': 'Hysterectomy is not the '
                                                                    'prophylaxis for Rh '
                                                                    'incompatibility.',
                                                               'D': 'Blood-bank readiness is '
                                                                    'related Rh care thinking but '
                                                                    'is not the indicated '
                                                                    'postpartum sensitization '
                                                                    'prevention.'}}],
                             'medium': [{'question': 'Which cluster best represents danger signs '
                                                     'of worsening preeclampsia that require '
                                                     'urgent escalation?',
                                         'options': ['A) Leukorrhea without itching in the second '
                                                     'trimester',
                                                     'B) New dependent edema and mild headache '
                                                     'after a long day of standing',
                                                     'C) Severe headache, visual changes, '
                                                     'epigastric pain, and rising BP',
                                                     'D) Fetal quickening reported for the first '
                                                     'time at 20 weeks'],
                                         'answer': 'C) Severe headache, visual changes, epigastric '
                                                   'pain, and rising BP',
                                         'explanation': 'Severe features of preeclampsia include '
                                                        'neurologic symptoms, epigastric/RUQ pain, '
                                                        'and severe hypertension—harbingers of '
                                                        'eclampsia and organ injury needing urgent '
                                                        'escalation.',
                                         'choice_explanations': {'A': 'Normal leukorrhea without '
                                                                      'infection signs is not a '
                                                                      'preeclampsia warning.',
                                                                 'B': 'Edema with mild headache is '
                                                                      'common overlapping '
                                                                      'preeclampsia assessment '
                                                                      'territory and creates '
                                                                      'doubt, but alone lacks '
                                                                      'severe-feature urgency.',
                                                                 'C': 'This symptom cluster '
                                                                      'signals severe features '
                                                                      'needing urgent evaluation '
                                                                      'and seizure precautions.',
                                                                 'D': 'Quickening is expected '
                                                                      'fetal movement, not a '
                                                                      'preeclampsia danger sign.'}},
                                        {'question': 'A nonstress test is reported as reactive. '
                                                     'What does this roughly indicate?',
                                         'options': ['A) A reassuring test that rules out the need '
                                                     'for further fetal surveillance this '
                                                     'pregnancy',
                                                     'B) Immediate cesarean is mandatory '
                                                     'regardless of other findings',
                                                     'C) Confirmed fetal demise',
                                                     'D) Adequate fetal heart-rate accelerations '
                                                     'with movement, suggesting fetal well-being '
                                                     'in that window'],
                                         'answer': 'D) Adequate fetal heart-rate accelerations '
                                                   'with movement, suggesting fetal well-being in '
                                                   'that window',
                                         'explanation': 'A reactive NST shows accelerations '
                                                        'associated with fetal movement, '
                                                        'reflecting intact autonomic and '
                                                        'oxygenation status during the test '
                                                        'period. It is reassuring for that window, '
                                                        'not a permanent clearance.',
                                         'choice_explanations': {'A': 'Over-reading a reactive NST '
                                                                      'as ending all surveillance '
                                                                      'is an assessment near-miss.',
                                                                 'B': 'Reactive NST is reassuring, '
                                                                      'not an automatic cesarean '
                                                                      'trigger.',
                                                                 'C': 'Demise would lack a normal '
                                                                      'reactive pattern.',
                                                                 'D': 'Accelerations with movement '
                                                                      'indicate fetal well-being '
                                                                      'during the testing '
                                                                      'window.'}},
                                        {'question': 'Teaching for a breastfeeding parent with '
                                                     'mastitis should include which point?',
                                         'options': ['A) Continue frequent emptying (feed/pump), '
                                                     'use comfort measures, and take antibiotics '
                                                     'if prescribed',
                                                     'B) Rest the affected breast for 24 hours, '
                                                     'then resume feeding only if fever resolves',
                                                     'C) Abruptly stop breastfeeding on the '
                                                     'affected side permanently',
                                                     'D) Ignore fever because mastitis is always '
                                                     'self-limited without treatment'],
                                         'answer': 'A) Continue frequent emptying (feed/pump), use '
                                                   'comfort measures, and take antibiotics if '
                                                   'prescribed',
                                         'explanation': 'Mastitis management includes continued '
                                                        'milk removal, supportive care, and '
                                                        'antibiotics when indicated. Abrupt '
                                                        'weaning or prolonged “resting” the breast '
                                                        'worsens stasis.',
                                         'choice_explanations': {'A': 'Frequent emptying plus '
                                                                      'prescribed '
                                                                      'antibiotics/supportive care '
                                                                      'is standard teaching.',
                                                                 'B': 'Resting the breast until '
                                                                      'fever resolves sounds '
                                                                      'soothing but worsens milk '
                                                                      'stasis—near-miss.',
                                                                 'C': 'Continued emptying aids '
                                                                      'resolution; abrupt '
                                                                      'cessation worsens stasis.',
                                                                 'D': 'Fever with mastitis often '
                                                                      'needs evaluation and '
                                                                      'possible antibiotics.'}}],
                             'hard': [{'question': 'During delivery, the head delivers but the '
                                                   'shoulders do not follow; the turtle sign is '
                                                   'present. Which nursing actions help the team '
                                                   'manage shoulder dystocia?',
                                       'options': ['A) Pull harder on the head without calling for '
                                                   'help',
                                                   'B) Call for help, note the time, assist with '
                                                   'McRoberts/suprapubic pressure as directed, and '
                                                   'avoid fundal pressure',
                                                   'C) Have the mother stand and walk to deliver '
                                                   'the shoulders',
                                                   'D) Apply strong fundal pressure while traction '
                                                   'is increased to deliver the anterior shoulder '
                                                   'quickly'],
                                       'answer': 'B) Call for help, note the time, assist with '
                                                 'McRoberts/suprapubic pressure as directed, and '
                                                 'avoid fundal pressure',
                                       'explanation': 'Shoulder dystocia is an obstetric '
                                                      'emergency. Nurses activate help, track '
                                                      'time, and assist with McRoberts and '
                                                      'suprapubic pressure. Fundal pressure '
                                                      'worsens impaction and is contraindicated.',
                                       'choice_explanations': {'A': 'Excessive traction risks '
                                                                    'nerve injury; help and proper '
                                                                    'maneuvers are required.',
                                                               'B': 'Help, timing, McRoberts, and '
                                                                    'suprapubic pressure are the '
                                                                    'correct assistive priorities.',
                                                               'C': 'Ambulation is impossible and '
                                                                    'unsafe mid-dystocia.',
                                                               'D': 'Fundal pressure with traction '
                                                                    'is a dangerous instinctive '
                                                                    'near-miss that worsens '
                                                                    'impaction.'}},
                                      {'question': 'A pregnant patient at 34 weeks has sudden dark '
                                                   'vaginal bleeding, rigid board-like abdomen, '
                                                   'and severe pain with fetal bradycardia. Which '
                                                   'condition fits this classic pattern?',
                                       'options': ['A) Normal Braxton Hicks with mucus plug only',
                                                   'B) Placenta previa with labor pain from '
                                                   'contractions causing the bleeding appearance',
                                                   'C) Placental abruption until proven otherwise',
                                                   'D) Bloody show of early latent labor only'],
                                       'answer': 'C) Placental abruption until proven otherwise',
                                       'explanation': 'Painful dark bleeding, uterine '
                                                      'rigidity/tenderness, and fetal distress '
                                                      'classic for abruption. Previa is typically '
                                                      'painless bright bleeding without a '
                                                      'board-like uterus.',
                                       'choice_explanations': {'A': 'Braxton Hicks are '
                                                                    'intermittent tightenings '
                                                                    'without hemorrhage and fetal '
                                                                    'bradycardia.',
                                                               'B': 'Previa is the classic '
                                                                    'bleeding differential '
                                                                    '(assessment cousin) but '
                                                                    'painless bright bleeding '
                                                                    'lacks this rigid, painful '
                                                                    'picture.',
                                                               'C': 'Painful bleeding with a rigid '
                                                                    'uterus and fetal compromise '
                                                                    'is the abruption pattern.',
                                                               'D': 'Bloody show lacks board-like '
                                                                    'rigidity and severe fetal '
                                                                    'bradycardia of this degree.'}},
                                      {'question': 'How do postpartum blues typically differ from '
                                                   'postpartum depression in nursing assessment?',
                                       'options': ['A) Blues and depression are distinguished '
                                                   'mainly by whether EPDS screening was done on '
                                                   'postpartum day 1',
                                                   'B) Blues always include psychosis and require '
                                                   'immediate involuntary hold',
                                                   'C) Depression never occurs after day 3, so '
                                                   'late symptoms can be ignored',
                                                   'D) Blues are transient tearfulness/mood '
                                                   'lability peaking early; depression is more '
                                                   'persistent with functional impairment'],
                                       'answer': 'D) Blues are transient tearfulness/mood lability '
                                                 'peaking early; depression is more persistent '
                                                 'with functional impairment',
                                       'explanation': 'Postpartum blues are common, brief mood '
                                                      'swings in the first days. Postpartum '
                                                      'depression lasts longer, impairs function, '
                                                      'and may include hopelessness or suicidal '
                                                      'ideation needing treatment.',
                                       'choice_explanations': {'A': 'Screening timing matters but '
                                                                    'does not itself define the '
                                                                    'clinical '
                                                                    'distinction—assessment '
                                                                    'near-miss.',
                                                               'B': 'Psychosis is not a feature of '
                                                                    'blues; it is a psychiatric '
                                                                    'emergency of its own.',
                                                               'C': 'Depression can present later '
                                                                    'and must not be dismissed by '
                                                                    'calendar day.',
                                                               'D': 'Duration and functional '
                                                                    'impact distinguish blues from '
                                                                    'depression.'}}],
                             'extreme': [{'question': 'Immediately after a generalized eclamptic '
                                                      'seizure, the patient is still pregnant at '
                                                      '37 weeks, SpO2 is 88% on room air, and the '
                                                      'uterus is contracting. Magnesium sulfate is '
                                                      'ordered but not yet started; a family '
                                                      'member demands immediate discharge against '
                                                      'advice. What is the nursing priority '
                                                      'sequence?',
                                          'options': ['A) Protect airway/oxygenation, place in '
                                                      'lateral position, prevent injury, start '
                                                      'magnesium per protocol, and escalate',
                                                      'B) Focus first on continuous fetal '
                                                      'monitoring and prepare the OR while '
                                                      'oxygenation is briefly checked',
                                                      'C) Begin oxytocin augmentation before '
                                                      'airway support',
                                                      'D) Withhold magnesium because seizures have '
                                                      'already occurred'],
                                          'answer': 'A) Protect airway/oxygenation, place in '
                                                    'lateral position, prevent injury, start '
                                                    'magnesium per protocol, and escalate',
                                          'explanation': 'After eclamptic seizure, maternal '
                                                         'airway/oxygenation and injury prevention '
                                                         'come first, with magnesium to control '
                                                         'seizure activity and urgent obstetric '
                                                         'escalation. Fetal assessment follows '
                                                         'maternal stabilization.',
                                          'choice_explanations': {'A': 'Maternal ABC/safety plus '
                                                                       'magnesium and escalation '
                                                                       'is the immediate cluster.',
                                                                  'B': 'Fetal monitoring/OR prep '
                                                                       'are urgent obstetric next '
                                                                       'steps but must not outrank '
                                                                       'maternal airway—priority '
                                                                       'near-miss.',
                                                                  'C': 'Oxytocin before airway '
                                                                       'support ignores maternal '
                                                                       'hypoxemia.',
                                                                  'D': 'Magnesium is indicated to '
                                                                       'control eclamptic seizure '
                                                                       'activity and prevent '
                                                                       'recurrence.'}},
                                         {'question': 'During labor, a multipara suddenly develops '
                                                      'dyspnea, hypotension, and DIC-range '
                                                      'bleeding from IV sites after membrane '
                                                      'rupture. The anesthetist suspects amniotic '
                                                      'fluid embolism. Fetal heart tracing shows '
                                                      'prolonged bradycardia. What should nursing '
                                                      'priorities emphasize?',
                                          'options': ['A) Encourage ambulation to improve venous '
                                                      'return',
                                                      'B) Support ABCs/resuscitation, activate '
                                                      'massive hemorrhage/rapid response pathways, '
                                                      'and prepare for coagulopathy care',
                                                      'C) Give a full meal to prevent hypoglycemia',
                                                      'D) Priority collect labs and cord gases to '
                                                      'confirm AFE before activating the '
                                                      'hemorrhage protocol'],
                                          'answer': 'B) Support ABCs/resuscitation, activate '
                                                    'massive hemorrhage/rapid response pathways, '
                                                    'and prepare for coagulopathy care',
                                          'explanation': 'Sudden dyspnea, hypotension, and DIC '
                                                         'after rupture suggest amniotic fluid '
                                                         'embolism. Resuscitate, activate massive '
                                                         'hemorrhage pathways, and treat '
                                                         'coagulopathy—do not delay for '
                                                         'confirmatory labs.',
                                          'choice_explanations': {'A': 'Ambulation is '
                                                                       'contraindicated in '
                                                                       'shock/DIC.',
                                                                  'B': 'ABC support with massive '
                                                                       'hemorrhage/rapid response '
                                                                       'activation is the '
                                                                       'priority.',
                                                                  'C': 'Oral intake is unsafe in a '
                                                                       'crashing peripartum '
                                                                       'patient.',
                                                                  'D': 'Lab confirmation before '
                                                                       'protocol activation is a '
                                                                       'diagnostic near-miss '
                                                                       'during collapse.'}},
                                         {'question': 'After a difficult third stage, a mass '
                                                      'protrudes at the introitus, the fundus '
                                                      'cannot be palpated abdominally, and '
                                                      'hemorrhage is heavy. A junior clinician '
                                                      'orders fundal oxytocin IM “into the uterus” '
                                                      'through the mass. What is the correct '
                                                      'recognition and response?',
                                          'options': ['A) Ignore bleeding because inversion is a '
                                                      'normal variant',
                                                      'B) Massage the protruding mass firmly like '
                                                      'atony while giving the ordered uterotonic '
                                                      'to firm the uterus',
                                                      'C) Suspect uterine inversion; stop '
                                                      'inappropriate uterotonic into the inverted '
                                                      'fundus, support ABCs, and prepare for rapid '
                                                      'replacement',
                                                      'D) Pull on the cord again to deliver more '
                                                      'placenta'],
                                          'answer': 'C) Suspect uterine inversion; stop '
                                                    'inappropriate uterotonic into the inverted '
                                                    'fundus, support ABCs, and prepare for rapid '
                                                    'replacement',
                                          'explanation': 'A protruding mass with nonpalpable '
                                                         'abdominal fundus and hemorrhage suggests '
                                                         'uterine inversion. Uterotonics into an '
                                                         'inverted uterus and fundal-style massage '
                                                         'are contraindicated until replacement.',
                                          'choice_explanations': {'A': 'Inversion with hemorrhage '
                                                                       'is an obstetric emergency, '
                                                                       'not normal.',
                                                                  'B': 'Treating the mass as boggy '
                                                                       'atony is the classic '
                                                                       'dangerous near-miss.',
                                                                  'C': 'Recognizing inversion, '
                                                                       'stopping harmful '
                                                                       'uterotonic/massage, and '
                                                                       'preparing for replacement '
                                                                       'is correct.',
                                                                  'D': 'Further cord traction can '
                                                                       'worsen inversion.'}}]},
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
                 'questions': {'easy': [{'question': 'Which approach best reflects therapeutic '
                                                     'communication in psychiatric nursing?',
                                         'options': ['A) Using empathy, open-ended questions, and '
                                                     'clarifying without judgment',
                                                     'B) Offering hopeful reassurance and advice '
                                                     'to quickly reduce the patient’s distress',
                                                     'C) Changing the subject whenever emotion '
                                                     'appears',
                                                     'D) Sharing detailed personal problems to '
                                                     'equalize roles'],
                                         'answer': 'A) Using empathy, open-ended questions, and '
                                                   'clarifying without judgment',
                                         'explanation': 'Therapeutic communication builds trust '
                                                        'through empathy, clarification, and '
                                                        'nonjudgmental exploration. False '
                                                        'reassurance, topic changes that shut down '
                                                        'feeling, and blurred boundaries undermine '
                                                        'the alliance.',
                                         'choice_explanations': {'A': 'Empathy and open '
                                                                      'clarification are core '
                                                                      'therapeutic communication '
                                                                      'skills.',
                                                                 'B': 'Reassurance/advice can feel '
                                                                      'caring but often blocks '
                                                                      'exploration—communication '
                                                                      'near-miss.',
                                                                 'C': 'Avoiding emotion prevents '
                                                                      'understanding and alliance.',
                                                                 'D': 'Over-sharing personal '
                                                                      'problems shifts focus and '
                                                                      'blurs professional '
                                                                      'boundaries.'}},
                                        {'question': 'What must a suicide risk assessment '
                                                     'specifically explore beyond general sadness?',
                                         'options': ['A) Preferred cafeteria foods only',
                                                     'B) Ideation, plan, intent, means, and '
                                                     'protective factors',
                                                     'C) Only whether the patient smiles during '
                                                     'interview',
                                                     'D) Mood severity and whether the patient '
                                                     'appears tearful or withdrawn today'],
                                         'answer': 'B) Ideation, plan, intent, means, and '
                                                   'protective factors',
                                         'explanation': 'Suicide assessment asks about ideation, '
                                                        'plan specificity, intent, access to '
                                                        'means, and protective factors. Surface '
                                                        'mood cues alone do not quantify near-term '
                                                        'risk.',
                                         'choice_explanations': {'A': 'Food preference is '
                                                                      'unrelated to suicide risk '
                                                                      'stratification.',
                                                                 'B': 'Ideation–plan–intent–means '
                                                                      'plus protectors is the '
                                                                      'required risk framework.',
                                                                 'C': 'Affect alone is an '
                                                                      'unreliable indicator of '
                                                                      'suicide risk.',
                                                                 'D': 'Mood/affect assessment is '
                                                                      'related mental-status work '
                                                                      'but is insufficient for '
                                                                      'suicide risk '
                                                                      'stratification—near-miss.'}},
                                        {'question': 'Which early side-effect theme is commonly '
                                                     'taught for SSRIs in the first weeks?',
                                         'options': ['A) Need to stop the drug after one dose if '
                                                     'mood is unchanged',
                                                     'B) Early improvement in energy before mood '
                                                     'lifts, so suicide risk can be disregarded '
                                                     'after week one',
                                                     'C) Possible GI upset, headache, sleep '
                                                     'change, and transient anxiety/activation',
                                                     'D) Immediate complete remission of all '
                                                     'symptoms by day one'],
                                         'answer': 'C) Possible GI upset, headache, sleep change, '
                                                   'and transient anxiety/activation',
                                         'explanation': 'SSRIs often cause early GI symptoms, '
                                                        'headache, sleep disturbance, and '
                                                        'sometimes activation before '
                                                        'antidepressant benefit emerges over '
                                                        'weeks. Energy may improve before '
                                                        'mood—suicide vigilance continues.',
                                         'choice_explanations': {'A': 'Stopping after one '
                                                                      'unchanged-mood dose ignores '
                                                                      'expected latency of '
                                                                      'benefit.',
                                                                 'B': 'Energy-before-mood is a '
                                                                      'real teaching point but '
                                                                      'dismissing suicide risk is '
                                                                      'a dangerous near-miss.',
                                                                 'C': 'Early somatic/activation '
                                                                      'effects are the common '
                                                                      'teaching points for SSRI '
                                                                      'initiation.',
                                                                 'D': 'Therapeutic effect is '
                                                                      'delayed; day-one remission '
                                                                      'is not expected.'}}],
                               'medium': [{'question': 'A patient on lithium develops nausea, '
                                                       'vomiting, diarrhea, and coarse tremor '
                                                       'after a viral illness with poor intake. '
                                                       'What should the nurse suspect?',
                                           'options': ['A) Expected GI viral illness; continue '
                                                       'lithium with antiemetics and push oral '
                                                       'fluids',
                                                       'B) Need to double the next lithium dose to '
                                                       '“catch up”',
                                                       'C) Allergic rhinitis unrelated to lithium '
                                                       'levels',
                                                       'D) Possible lithium toxicity precipitated '
                                                       'by volume depletion; hold dose and '
                                                       'escalate'],
                                           'answer': 'D) Possible lithium toxicity precipitated by '
                                                     'volume depletion; hold dose and escalate',
                                           'explanation': 'Dehydration and sodium loss reduce '
                                                          'lithium clearance and raise levels. GI '
                                                          'losses plus coarse tremor are toxicity '
                                                          'cues. Hold the dose pending levels and '
                                                          'medical evaluation.',
                                           'choice_explanations': {'A': 'Continuing lithium '
                                                                        'through gastroenteritis '
                                                                        'with “hydration” sounds '
                                                                        'supportive but risks '
                                                                        'worsening '
                                                                        'toxicity—near-miss.',
                                                                   'B': 'Doubling the dose worsens '
                                                                        'potential toxicity.',
                                                                   'C': 'These symptoms align with '
                                                                        'lithium toxicity, not '
                                                                        'rhinitis.',
                                                                   'D': 'Illness-related volume '
                                                                        'loss with GI symptoms and '
                                                                        'coarse tremor suggests '
                                                                        'toxicity needing hold and '
                                                                        'escalation.'}},
                                          {'question': 'Which complication is a major nursing '
                                                       'surveillance priority in acute alcohol '
                                                       'withdrawal?',
                                           'options': ['A) Seizures and delirium tremens with '
                                                       'autonomic instability',
                                                       'B) Rebound anxiety and insomnia that '
                                                       'should be managed mainly with education '
                                                       'and observation',
                                                       'C) Guaranteed absence of autonomic '
                                                       'hyperactivity',
                                                       'D) Immediate lifelong immunity to alcohol '
                                                       'after one detox'],
                                           'answer': 'A) Seizures and delirium tremens with '
                                                     'autonomic instability',
                                           'explanation': 'Alcohol withdrawal can progress to '
                                                          'seizures and DTs with tachycardia, '
                                                          'hypertension, fever, and altered '
                                                          'mentation. Nurses use protocols (e.g., '
                                                          'CIWA), seizure precautions, and ordered '
                                                          'benzodiazepines.',
                                           'choice_explanations': {'A': 'Seizures and DTs are the '
                                                                        'high-morbidity '
                                                                        'complications requiring '
                                                                        'vigilance.',
                                                                   'B': 'Anxiety/insomnia are '
                                                                        'early withdrawal features '
                                                                        'and create doubt, but '
                                                                        'minimizing to observation '
                                                                        'misses seizure/DT risk.',
                                                                   'C': 'Autonomic hyperactivity '
                                                                        'is common in withdrawal, '
                                                                        'not absent.',
                                                                   'D': 'Detox does not create '
                                                                        'lasting immunity to '
                                                                        'alcohol use disorder.'}},
                                          {'question': 'A patient with schizophrenia says, “The '
                                                       'voices tell me the food is poisoned.” What '
                                                       'is the best initial nursing response '
                                                       'theme?',
                                           'options': ['A) Argue that the voices are imaginary '
                                                       'until the patient agrees',
                                                       'B) Acknowledge the experience, reinforce '
                                                       'reality gently, and assess safety without '
                                                       'debating the delusion as a fact contest',
                                                       'C) Agree the food is poisoned and discard '
                                                       'all unit meals',
                                                       'D) Redirect to unit activities after a '
                                                       'brief reality statement without asking '
                                                       'about command content'],
                                           'answer': 'B) Acknowledge the experience, reinforce '
                                                     'reality gently, and assess safety without '
                                                     'debating the delusion as a fact contest',
                                           'explanation': 'Therapeutic responses acknowledge the '
                                                          'patient’s experience, avoid hostile '
                                                          'confrontation of fixed delusions, '
                                                          'reinforce reality, and assess for '
                                                          'command hallucinations/safety.',
                                           'choice_explanations': {'A': 'Arguing rarely '
                                                                        'extinguishes delusions '
                                                                        'and increases agitation.',
                                                                   'B': 'Acknowledgment plus '
                                                                        'gentle reality '
                                                                        'orientation and safety '
                                                                        'assessment is best '
                                                                        'practice.',
                                                                   'C': 'Agreeing with the '
                                                                        'delusion reinforces false '
                                                                        'belief and disrupts '
                                                                        'nutrition care.',
                                                                   'D': 'Quick redirect without '
                                                                        'assessing command/safety '
                                                                        'content is a common '
                                                                        'incomplete near-miss.'}}],
                               'hard': [{'question': 'A patient on a high-potency antipsychotic '
                                                     'develops lead-pipe rigidity, very high '
                                                     'fever, and fluctuating consciousness. '
                                                     'Another patient on an SSRI plus tramadol is '
                                                     'agitated, hyperreflexic, and '
                                                     'clonus-positive. Which clue themes correctly '
                                                     'separate NMS from serotonin syndrome?',
                                         'options': ['A) Fever never occurs in either syndrome',
                                                     'B) Both present with fever and altered '
                                                     'mentation, so drug class history is optional '
                                                     'if cooling is started',
                                                     'C) NMS: rigidity/bradyreflexia after '
                                                     'antipsychotics; serotonin syndrome: '
                                                     'hyperreflexia/clonus after serotonergic '
                                                     'drugs',
                                                     'D) NMS is always caused by SSRIs; serotonin '
                                                     'syndrome is always caused by haloperidol '
                                                     'alone'],
                                         'answer': 'C) NMS: rigidity/bradyreflexia after '
                                                   'antipsychotics; serotonin syndrome: '
                                                   'hyperreflexia/clonus after serotonergic drugs',
                                         'explanation': 'NMS is an antipsychotic-related reaction '
                                                        'with severe rigidity and hyporeflexia. '
                                                        'Serotonin syndrome from serotonergic '
                                                        'agents features hyperreflexia and clonus. '
                                                        'Distinguishing guides treatment.',
                                         'choice_explanations': {'A': 'Fever can occur in both and '
                                                                      'is clinically important.',
                                                                 'B': 'Shared fever/mentation '
                                                                      'findings are real overlap; '
                                                                      'skipping drug/reflex clues '
                                                                      'is the assessment '
                                                                      'near-miss.',
                                                                 'C': 'Rigidity vs '
                                                                      'hyperreflexia/clonus plus '
                                                                      'drug class correctly '
                                                                      'differentiates NMS from '
                                                                      'serotonin syndrome.',
                                                                 'D': 'NMS links to '
                                                                      'antipsychotics; serotonin '
                                                                      'syndrome to serotonergic '
                                                                      'combinations—roles reversed '
                                                                      'here.'}},
                                        {'question': 'Which situation best meets typical criteria '
                                                     'themes for emergency involuntary psychiatric '
                                                     'hold?',
                                         'options': ['A) Severe psychiatric symptoms with poor '
                                                     'insight even when the person accepts '
                                                     'voluntary admission',
                                                     'B) Family embarrassment about a diagnosis '
                                                     'without safety risk',
                                                     'C) Missed outpatient appointment alone',
                                                     'D) Imminent danger to self/others or grave '
                                                     'disability from mental illness when the '
                                                     'person refuses voluntary safe care'],
                                         'answer': 'D) Imminent danger to self/others or grave '
                                                   'disability from mental illness when the person '
                                                   'refuses voluntary safe care',
                                         'explanation': 'Involuntary holds are justified when '
                                                        'mental illness produces imminent risk of '
                                                        'harm to self/others or inability to meet '
                                                        'basic needs, and less restrictive '
                                                        'voluntary options are not feasible.',
                                         'choice_explanations': {'A': 'Severe symptoms/poor '
                                                                      'insight matter clinically '
                                                                      'but voluntary acceptance '
                                                                      'usually precludes '
                                                                      'involuntary hold—near-miss.',
                                                                 'B': 'Family discomfort without '
                                                                      'safety risk is not a legal '
                                                                      'hold criterion.',
                                                                 'C': 'Missed appointments need '
                                                                      'outreach, not automatic '
                                                                      'involuntary confinement.',
                                                                 'D': 'Danger or grave disability '
                                                                      'with refusal of voluntary '
                                                                      'safe care is the classic '
                                                                      'hold theme.'}},
                                        {'question': 'Why does clozapine require unique '
                                                     'nursing/pharmacy monitoring compared with '
                                                     'many other antipsychotics?',
                                         'options': ['A) Risk of agranulocytosis/neutropenia '
                                                     'requiring scheduled absolute neutrophil '
                                                     'count monitoring',
                                                     'B) Metabolic syndrome risk requiring only '
                                                     'weight and glucose checks without '
                                                     'hematologic labs',
                                                     'C) It never causes metabolic effects, so no '
                                                     'labs are needed',
                                                     'D) It is available only as a one-time '
                                                     'lifetime dose'],
                                         'answer': 'A) Risk of agranulocytosis/neutropenia '
                                                   'requiring scheduled absolute neutrophil count '
                                                   'monitoring',
                                         'explanation': 'Clozapine’s boxed risk of severe '
                                                        'neutropenia mandates ANC monitoring '
                                                        'before and during therapy. It also '
                                                        'carries metabolic and other risks—so '
                                                        '“metabolic only” monitoring is '
                                                        'incomplete.',
                                         'choice_explanations': {'A': 'ANC monitoring for '
                                                                      'agranulocytosis risk is the '
                                                                      'distinctive safety '
                                                                      'requirement.',
                                                                 'B': 'Metabolic monitoring is '
                                                                      'needed but is not the '
                                                                      'unique clozapine '
                                                                      'requirement—near-miss.',
                                                                 'C': 'Clozapine has significant '
                                                                      'metabolic and hematologic '
                                                                      'risks requiring monitoring.',
                                                                 'D': 'Clozapine is ongoing '
                                                                      'therapy, not a single '
                                                                      'lifetime dose.'}}],
                               'extreme': [{'question': 'On a locked unit, a patient is found in '
                                                        'the bathroom with a sheet ligature around '
                                                        'the neck, cyanotic but with a weak pulse. '
                                                        'Another patient is yelling for PRN '
                                                        'lorazepam at the desk, and a new '
                                                        'admission needs orientation. What is your '
                                                        'immediate priority?',
                                            'options': ['A) Bring oral lorazepam to the yelling '
                                                        'patient first to restore unit calm',
                                                        'B) Call for help, release the ligature, '
                                                        'initiate rescue breathing/CPR as needed, '
                                                        'and secure the environment',
                                                        'C) Leave the patient to find the paper '
                                                        'incident form before intervening',
                                                        'D) Call for help and assess '
                                                        'responsiveness thoroughly before removing '
                                                        'the sheet to preserve the scene'],
                                            'answer': 'B) Call for help, release the ligature, '
                                                      'initiate rescue breathing/CPR as needed, '
                                                      'and secure the environment',
                                            'explanation': 'Ligature cyanosis with a weak pulse is '
                                                           'an immediate airway/circulation '
                                                           'emergency. Release the ligature and '
                                                           'resuscitate while calling for help; '
                                                           'scene preservation never delays '
                                                           'rescue.',
                                            'choice_explanations': {'A': 'PRN for another patient '
                                                                         'does not outrank an '
                                                                         'active hanging.',
                                                                    'B': 'Help, ligature release, '
                                                                         'and resuscitation are '
                                                                         'the life-saving '
                                                                         'sequence.',
                                                                    'C': 'Documentation never '
                                                                         'precedes rescue.',
                                                                    'D': 'Assessment-before-removal '
                                                                         'to “preserve the scene” '
                                                                         'is a deadly near-miss '
                                                                         'priority error.'}},
                                           {'question': 'A visitor becomes violent, brandishes a '
                                                        'knife, and blocks the exit while '
                                                        'demanding a patient’s discharge. Staff '
                                                        'personal alarms are available; the '
                                                        'patient is hiding in the bathroom. What '
                                                        'is the correct priority?',
                                            'options': ['A) Ignore the weapon and continue '
                                                        'medication pass in the hallway',
                                                        'B) Use therapeutic communication to '
                                                        'negotiate while slowly moving closer to '
                                                        'take the knife',
                                                        'C) Ensure staff/patient safety: activate '
                                                        'emergency security response, '
                                                        'evacuate/shelter others, and do not '
                                                        'attempt solo disarmament',
                                                        'D) Negotiate discharge paperwork under '
                                                        'threat to “de-escalate”'],
                                            'answer': 'C) Ensure staff/patient safety: activate '
                                                      'emergency security response, '
                                                      'evacuate/shelter others, and do not attempt '
                                                      'solo disarmament',
                                            'explanation': 'An armed visitor blocking exit is a '
                                                           'security emergency. Protect people, '
                                                           'activate trained responders, and avoid '
                                                           'solo disarmament or coerced clinical '
                                                           'decisions.',
                                            'choice_explanations': {'A': 'Continuing med pass '
                                                                         'ignores an active weapon '
                                                                         'threat.',
                                                                    'B': 'Talking while closing '
                                                                         'distance sounds '
                                                                         'de-escalatory but risks '
                                                                         'solo confrontation with '
                                                                         'a weapon—near-miss.',
                                                                    'C': 'Security activation, '
                                                                         'evacuation/shelter, and '
                                                                         'no solo disarmament '
                                                                         'protect life.',
                                                                    'D': 'Clinical decisions under '
                                                                         'threat are coerced and '
                                                                         'unsafe.'}},
                                           {'question': 'A patient on high-dose haloperidol '
                                                        'develops temperature 41°C, lead-pipe '
                                                        'rigidity, BP instability, and rising CK. '
                                                        'The covering provider texts “give another '
                                                        'IM haloperidol for agitation.” What '
                                                        'should you do?',
                                            'options': ['A) Give acetaminophen and IV fluids for '
                                                        'fever first, then reconsider the extra '
                                                        'haloperidol if rigidity persists',
                                                        'B) Give the additional IM haloperidol as '
                                                        'texted without assessment',
                                                        'C) Cover with heavy blankets to “sweat '
                                                        'out” the fever',
                                                        'D) Hold further antipsychotics, support '
                                                        'ABCs/cooling, notify the provider of '
                                                        'suspected NMS, and seek higher-level '
                                                        'orders'],
                                            'answer': 'D) Hold further antipsychotics, support '
                                                      'ABCs/cooling, notify the provider of '
                                                      'suspected NMS, and seek higher-level orders',
                                            'explanation': 'High fever, lead-pipe rigidity, '
                                                           'autonomic instability, and rising CK '
                                                           'after antipsychotics suggest NMS. Stop '
                                                           'dopamine blockers, support '
                                                           'ABCs/cooling, and escalate—do not give '
                                                           'more antipsychotic.',
                                            'choice_explanations': {'A': 'Treating fever '
                                                                         'supportively before '
                                                                         'stopping the culprit '
                                                                         'antipsychotic is a '
                                                                         'dangerous near-miss.',
                                                                    'B': 'More haloperidol can '
                                                                         'worsen NMS.',
                                                                    'C': 'Heavy bundling worsens '
                                                                         'hyperthermia.',
                                                                    'D': 'Holding antipsychotics '
                                                                         'with ABC/cooling support '
                                                                         'and NMS notification is '
                                                                         'required.'}}]},
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
               'questions': {'easy': [{'question': 'Which activity is the best example of primary '
                                                   'prevention?',
                                       'options': ['A) Cardiac rehabilitation after myocardial '
                                                   'infarction',
                                                   'B) Community influenza immunization before flu '
                                                   'season',
                                                   'C) Hospice care for terminal cancer',
                                                   'D) Blood-pressure screening fair to find '
                                                   'undiagnosed hypertension early'],
                                       'answer': 'B) Community influenza immunization before flu '
                                                 'season',
                                       'explanation': 'Primary prevention averts disease before '
                                                      'onset—immunization is classic. Screening is '
                                                      'secondary; rehab after MI and hospice are '
                                                      'tertiary/comfort care.',
                                       'choice_explanations': {'A': 'Post-MI rehab prevents '
                                                                    'complications of existing '
                                                                    'disease (tertiary).',
                                                               'B': 'Vaccination before exposure '
                                                                    'prevents disease onset '
                                                                    '(primary).',
                                                               'C': 'Hospice addresses advanced '
                                                                    'disease, not primary '
                                                                    'prevention.',
                                                               'D': 'BP screening is valuable '
                                                                    'prevention but is secondary '
                                                                    '(early detection)—classic '
                                                                    'level near-miss.'}},
                                      {'question': 'Which activity best exemplifies secondary '
                                                   'prevention?',
                                       'options': ['A) Long-term stroke rehabilitation therapy',
                                                   'B) Community influenza immunization before flu '
                                                   'season',
                                                   'C) Blood-pressure screening to detect '
                                                   'hypertension early',
                                                   'D) Building safe bike lanes citywide'],
                                       'answer': 'C) Blood-pressure screening to detect '
                                                 'hypertension early',
                                       'explanation': 'Secondary prevention detects disease early '
                                                      'through screening so treatment can begin '
                                                      'before advanced complications. Immunization '
                                                      'and environmental safety are primary; '
                                                      'rehabilitation after stroke is tertiary.',
                                       'choice_explanations': {'A': 'Rehab after stroke is '
                                                                    'tertiary prevention.',
                                                               'B': 'Immunization is primary '
                                                                    'prevention and is the most '
                                                                    'common level '
                                                                    'mix-up—near-miss.',
                                                               'C': 'BP screening finds '
                                                                    'asymptomatic hypertension '
                                                                    'early—secondary prevention.',
                                                               'D': 'Bike-lane engineering is '
                                                                    'primary prevention of '
                                                                    'injury.'}},
                                      {'question': 'Herd immunity most directly relates to which '
                                                   'public-health concept?',
                                       'options': ['A) Direct protection only of vaccinated '
                                                   'individuals, without community transmission '
                                                   'effects',
                                                   'B) Hospital bed count alone without '
                                                   'transmission dynamics',
                                                   'C) Individual hand preference in a population',
                                                   'D) Indirect protection of susceptible persons '
                                                   'when enough of the population is immune'],
                                       'answer': 'D) Indirect protection of susceptible persons '
                                                 'when enough of the population is immune',
                                       'explanation': 'Herd immunity occurs when sufficient '
                                                      'population immunity lowers transmission '
                                                      'enough to protect those who remain '
                                                      'susceptible. It is more than individual '
                                                      'vaccine protection alone.',
                                       'choice_explanations': {'A': 'Individual direct protection '
                                                                    'is related but '
                                                                    'incomplete—definition '
                                                                    'near-miss.',
                                                               'B': 'Bed capacity does not define '
                                                                    'herd immunity.',
                                                               'C': 'Handedness is unrelated to '
                                                                    'infectious herd effects.',
                                                               'D': 'Indirect protection via high '
                                                                    'population immunity is the '
                                                                    'herd-immunity concept.'}}],
                             'medium': [{'question': 'Which factors are included among social '
                                                     'determinants of health that community nurses '
                                                     'assess?',
                                         'options': ['A) Housing, education, income, food access, '
                                                     'and neighborhood safety',
                                                     'B) Health behaviors such as diet and '
                                                     'exercise as the primary determinants, with '
                                                     'limited social context',
                                                     'C) Only genetic polymorphisms with no '
                                                     'environmental context',
                                                     'D) Favorite sports team affiliation alone'],
                                         'answer': 'A) Housing, education, income, food access, '
                                                   'and neighborhood safety',
                                         'explanation': 'Social determinants—conditions in which '
                                                        'people live, learn, work, and '
                                                        'age—strongly shape health outcomes. '
                                                        'Housing, education, income, food, and '
                                                        'safety are core domains.',
                                         'choice_explanations': {'A': 'These structural living '
                                                                      'conditions are classic '
                                                                      'social determinants nurses '
                                                                      'assess.',
                                                                 'B': 'Behaviors matter but are '
                                                                      'not the full SDOH '
                                                                      'framework—assessment '
                                                                      'near-miss.',
                                                                 'C': 'Genetics matter but do not '
                                                                      'replace '
                                                                      'social-environmental '
                                                                      'determinants.',
                                                                 'D': 'Sports fandom is not a '
                                                                      'standard SDOH domain.'}},
                                        {'question': 'A client with pulmonary tuberculosis needs '
                                                     'community/home isolation teaching. Which '
                                                     'precaution theme is required for infectious '
                                                     'TB?',
                                         'options': ['A) Contact gown only without respiratory '
                                                     'protection considerations',
                                                     'B) Airborne precautions with appropriate '
                                                     'respirator use and ventilation guidance',
                                                     'C) No precautions once the client feels '
                                                     'subjectively better for one hour',
                                                     'D) Droplet precautions with surgical mask '
                                                     'for close contact if the client covers '
                                                     'coughs'],
                                         'answer': 'B) Airborne precautions with appropriate '
                                                   'respirator use and ventilation guidance',
                                         'explanation': 'Infectious pulmonary TB requires airborne '
                                                        'precautions—N95/respirator use and '
                                                        'ventilation/isolation strategies—until '
                                                        'noninfectious criteria are met.',
                                         'choice_explanations': {'A': 'Contact barriers alone do '
                                                                      'not stop airborne droplet '
                                                                      'nuclei.',
                                                                 'B': 'Airborne precautions with '
                                                                      'respirators/ventilation are '
                                                                      'required for infectious '
                                                                      'pulmonary TB.',
                                                                 'C': 'Subjective improvement does '
                                                                      'not equal noninfectious '
                                                                      'status.',
                                                                 'D': 'Droplet/surgical-mask '
                                                                      'thinking is a common TB '
                                                                      'precaution near-miss.'}},
                                        {'question': 'Before a home health visit in an unfamiliar '
                                                     'neighborhood, which safety practice should '
                                                     'the nurse include?',
                                         'options': ['A) Enter immediately if yelling is heard, '
                                                     'without calling for backup',
                                                     'B) Complete the clinical assessment quickly '
                                                     'if tension rises, then leave after '
                                                     'documenting in the home',
                                                     'C) Share schedule with the agency, carry a '
                                                     'charged phone, assess exit routes, and leave '
                                                     'if the environment is unsafe',
                                                     'D) Keep visit plans secret from the agency '
                                                     'so nobody knows the location'],
                                         'answer': 'C) Share schedule with the agency, carry a '
                                                   'charged phone, assess exit routes, and leave '
                                                   'if the environment is unsafe',
                                         'explanation': 'Home-visit safety includes agency '
                                                        'awareness of schedule/location, '
                                                        'communication devices, environmental '
                                                        'scanning, and willingness to leave when '
                                                        'threatened.',
                                         'choice_explanations': {'A': 'Entering an active violent '
                                                                      'scene alone is unsafe.',
                                                                 'B': 'Finishing '
                                                                      'assessment/documentation in '
                                                                      'an escalating home sounds '
                                                                      'duty-focused but delays '
                                                                      'egress—near-miss.',
                                                                 'C': 'Communication, exit '
                                                                      'planning, and leaving when '
                                                                      'unsafe are core home-visit '
                                                                      'safety practices.',
                                                                 'D': 'The agency must know '
                                                                      'location/timing for '
                                                                      'check-in and emergency '
                                                                      'response.'}}],
                             'hard': [{'question': 'What does “upstream thinking” mean when a '
                                                   'community nurse plans interventions for '
                                                   'childhood asthma hospitalizations?',
                                       'options': ['A) Improve ED asthma pathways and inhaler '
                                                   'teaching after each hospitalization as the '
                                                   'main plan',
                                                   'B) Focus only on rescue inhalers after each '
                                                   'ICU admission',
                                                   'C) Limit care to charting readmission rates '
                                                   'without action',
                                                   'D) Address root causes such as housing mold, '
                                                   'air quality, and access to controller therapy '
                                                   'before crises'],
                                       'answer': 'D) Address root causes such as housing mold, air '
                                                 'quality, and access to controller therapy before '
                                                 'crises',
                                       'explanation': 'Upstream approaches modify social and '
                                                      'environmental root causes that generate '
                                                      'disease burden, rather than only responding '
                                                      'after acute decompensation.',
                                       'choice_explanations': {'A': 'Strengthening post-hospital '
                                                                    'pathways is valuable but '
                                                                    'remains more '
                                                                    'downstream—near-miss.',
                                                               'B': 'Rescue-only focus is '
                                                                    'downstream crisis care.',
                                                               'C': 'Measurement without '
                                                                    'intervention does not change '
                                                                    'outcomes.',
                                                               'D': 'Root-cause environmental and '
                                                                    'access interventions '
                                                                    'exemplify upstream '
                                                                    'thinking.'}},
                                      {'question': 'In a mass-casualty incident using START '
                                                   'triage, which principle guides tagging?',
                                       'options': ['A) Expectant/minor/delayed/immediate '
                                                   'categories based on respiration, perfusion, '
                                                   'and mentation—not first-come-first-served',
                                                   'B) Treat the most verbally distressed victims '
                                                   'first because pain indicates immediacy',
                                                   'C) Treat VIP adults before all children '
                                                   'regardless of injuries',
                                                   'D) Spend unlimited time on each victim before '
                                                   'moving on'],
                                       'answer': 'A) Expectant/minor/delayed/immediate categories '
                                                 'based on respiration, perfusion, and '
                                                 'mentation—not first-come-first-served',
                                       'explanation': 'START triage rapidly sorts victims by '
                                                      'simple physiologic cues into immediate, '
                                                      'delayed, minor, or expectant categories to '
                                                      'do the greatest good for the greatest '
                                                      'number.',
                                       'choice_explanations': {'A': 'Physiologic '
                                                                    'categorization—not arrival '
                                                                    'order—defines START.',
                                                               'B': 'Distress/pain-first triage is '
                                                                    'an intuitive near-miss that '
                                                                    'ignores START physiology '
                                                                    'nodes.',
                                                               'C': 'VIP status is not a START '
                                                                    'criterion.',
                                                               'D': 'Rapid sorting requires time '
                                                                    'discipline across many '
                                                                    'victims.'}},
                                      {'question': 'A parent refuses childhood vaccines due to '
                                                   'social-media fears. What is the best nursing '
                                                   'approach?',
                                       'options': ['A) Mock the parent’s concerns in a group class',
                                                   'B) Use motivational, respectful dialogue; '
                                                   'address specific concerns with evidence; and '
                                                   'keep the door open for future acceptance',
                                                   'C) Refuse all other pediatric care until '
                                                   'vaccines are given',
                                                   'D) Provide a dense facts sheet and require a '
                                                   'same-visit decision so the child leaves '
                                                   'vaccinated'],
                                       'answer': 'B) Use motivational, respectful dialogue; '
                                                 'address specific concerns with evidence; and '
                                                 'keep the door open for future acceptance',
                                       'explanation': 'Vaccine hesitancy responds best to '
                                                      'nonjudgmental listening, tailored evidence, '
                                                      'and relationship continuity. Pressure '
                                                      'tactics and ridicule deepen mistrust.',
                                       'choice_explanations': {'A': 'Mockery increases resistance '
                                                                    'and damages alliance.',
                                                               'B': 'Respectful, concern-specific '
                                                                    'counseling with ongoing '
                                                                    'engagement is best practice.',
                                                               'C': 'Withholding unrelated '
                                                                    'essential care is unethical '
                                                                    'coercion.',
                                                               'D': 'Information dump with forced '
                                                                    'same-day decision is a common '
                                                                    'ineffective near-miss.'}}],
                             'extreme': [{'question': 'Several postal workers from one facility '
                                                      'present with fever, cough, and mediastinal '
                                                      'widening on chest imaging after handling '
                                                      'dusty mail. Media are calling; a supervisor '
                                                      'wants them sent home with azithromycin '
                                                      'only. What should the public-health nursing '
                                                      'response prioritize?',
                                          'options': ['A) Send everyone home without reporting '
                                                      'because publicity is inconvenient',
                                                      'B) Treat empirically for community '
                                                      'pneumonia first and notify public health '
                                                      'only if cultures later confirm anthrax',
                                                      'C) Treat as possible inhalational '
                                                      'anthrax/bioterror cluster: urgent '
                                                      'public-health notification, isolation/PPE '
                                                      'per protocol, and coordinated messaging',
                                                      'D) Reassure media that bacterial pneumonia '
                                                      'is always community MRSA'],
                                          'answer': 'C) Treat as possible inhalational '
                                                    'anthrax/bioterror cluster: urgent '
                                                    'public-health notification, isolation/PPE per '
                                                    'protocol, and coordinated messaging',
                                          'explanation': 'Clustered febrile illness with '
                                                         'mediastinal widening after dusty mail '
                                                         'handling raises inhalational '
                                                         'anthrax/bioterror concern. Immediate '
                                                         'public-health notification and '
                                                         'protective measures are required—not '
                                                         'waiting for final cultures.',
                                          'choice_explanations': {'A': 'Sending exposed ill '
                                                                       'workers home without '
                                                                       'reporting endangers the '
                                                                       'public.',
                                                                  'B': 'Empiric pneumonia care '
                                                                       'without early '
                                                                       'public-health alert is a '
                                                                       'dangerous delay near-miss.',
                                                                  'C': 'Urgent public-health '
                                                                       'notification with '
                                                                       'isolation/PPE and '
                                                                       'coordinated response '
                                                                       'matches bioterror cluster '
                                                                       'care.',
                                                                  'D': 'Media reassurance without '
                                                                       'investigation is '
                                                                       'inappropriate.'}},
                                         {'question': 'After a needlestick from an unknown-source '
                                                      'needle in a community clinic, bleeding is '
                                                      'encouraged at the site and soap-and-water '
                                                      'washing is done. The source patient left '
                                                      'without labs. What is the correct next '
                                                      'priority cluster?',
                                          'options': ['A) Wash thoroughly, document in a personal '
                                                      'notebook, and seek evaluation next business '
                                                      'day if the source seems low risk',
                                                      'B) Ignore the injury if the wound looks '
                                                      'small',
                                                      'C) Apply a tight arterial tourniquet for 6 '
                                                      'hours',
                                                      'D) Report immediately, seek urgent '
                                                      'employee-health/ED evaluation for baseline '
                                                      'labs and possible post-exposure '
                                                      'prophylaxis'],
                                          'answer': 'D) Report immediately, seek urgent '
                                                    'employee-health/ED evaluation for baseline '
                                                    'labs and possible post-exposure prophylaxis',
                                          'explanation': 'Needlestick exposures need immediate '
                                                         'reporting and urgent evaluation for '
                                                         'baseline testing and time-sensitive PEP '
                                                         'decisions. Delaying to the next day can '
                                                         'miss optimal prophylaxis windows.',
                                          'choice_explanations': {'A': 'Self-documentation with '
                                                                       'delayed evaluation is a '
                                                                       'common occupational '
                                                                       'near-miss.',
                                                                  'B': 'Wound size does not '
                                                                       'determine bloodborne '
                                                                       'pathogen risk.',
                                                                  'C': 'Arterial tourniquets are '
                                                                       'not appropriate '
                                                                       'needlestick first aid.',
                                                                  'D': 'Immediate report plus '
                                                                       'urgent evaluation for '
                                                                       'labs/PEP is required.'}},
                                         {'question': 'During a measles outbreak, an unvaccinated '
                                                      'pregnant nurse without immunity is exposed, '
                                                      'while a separate TB client needs airborne '
                                                      'isolation teaching. Leadership asks you to '
                                                      '“use quarantine and isolation '
                                                      'interchangeably in the press release.” What '
                                                      'distinction should guide your practice and '
                                                      'messaging?',
                                          'options': ['A) Isolation separates people with '
                                                      'contagious infection; quarantine restricts '
                                                      'exposed well persons who may become '
                                                      'infectious',
                                                      'B) Quarantine is used for confirmed measles '
                                                      'cases; isolation is only for exposed staff '
                                                      'awaiting titers',
                                                      'C) Quarantine and isolation are identical '
                                                      'legal terms with no difference',
                                                      'D) Neither strategy is ever used in '
                                                      'outbreak control'],
                                          'answer': 'A) Isolation separates people with contagious '
                                                    'infection; quarantine restricts exposed well '
                                                    'persons who may become infectious',
                                          'explanation': 'Isolation applies to people known or '
                                                         'suspected to be infectious; quarantine '
                                                         'restricts movement of exposed '
                                                         'asymptomatic persons during the '
                                                         'incubation period. Mixing the terms '
                                                         'confuses outbreak control.',
                                          'choice_explanations': {'A': 'Infectious vs exposed-well '
                                                                       'distinction correctly '
                                                                       'separates isolation from '
                                                                       'quarantine.',
                                                                  'B': 'Swapping the terms is a '
                                                                       'classic definition '
                                                                       'near-miss.',
                                                                  'C': 'The terms are not '
                                                                       'identical.',
                                                                  'D': 'Both strategies are used '
                                                                       'in outbreak control.'}}]},
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
                   'questions': {'easy': [{'question': 'For many acutely ill adults without '
                                                       'COPD-specific targets, which SpO2 range is '
                                                       'commonly used as a general oxygenation '
                                                       'goal?',
                                           'options': ['A) SpO2 of 70% is acceptable if the '
                                                       'patient is talking',
                                                       'B) Approximately 88–92% for all acutely '
                                                       'ill adults to avoid oxygen toxicity',
                                                       'C) Approximately 94–98% (or per ordered '
                                                       'disease-specific targets)',
                                                       'D) Always keep SpO2 at exactly 100% with '
                                                       'maximal FiO2'],
                                           'answer': 'C) Approximately 94–98% (or per ordered '
                                                     'disease-specific targets)',
                                           'explanation': 'Many guidelines target roughly 94–98% '
                                                          'for acutely ill adults, with lower '
                                                          'targets (e.g., 88–92%) for some COPD '
                                                          'patients. Forcing 100% with excess '
                                                          'oxygen can be harmful.',
                                           'choice_explanations': {'A': 'SpO2 70% indicates '
                                                                        'critical hypoxemia.',
                                                                   'B': '88–92% is a real '
                                                                        'COPD-related target '
                                                                        'wrongly generalized to '
                                                                        'all adults—near-miss.',
                                                                   'C': '≈94–98% (or ordered '
                                                                        'disease-specific ranges) '
                                                                        'is a common adult target '
                                                                        'theme.',
                                                                   'D': 'Unnecessary hyperoxia can '
                                                                        'cause harm; 100% is not a '
                                                                        'universal goal.'}},
                                          {'question': 'Where is an arterial line typically '
                                                       'zeroed/leveled for accurate pressure '
                                                       'monitoring?',
                                           'options': ['A) At the catheter insertion site so the '
                                                       'transducer matches the arterial puncture '
                                                       'level',
                                                       'B) At the patient’s knee regardless of '
                                                       'position',
                                                       'C) At the IV fluid bag spike',
                                                       'D) At the phlebostatic axis (approx. 4th '
                                                       'ICS, midaxillary line)'],
                                           'answer': 'D) At the phlebostatic axis (approx. 4th '
                                                     'ICS, midaxillary line)',
                                           'explanation': 'Leveling the transducer at the '
                                                          'phlebostatic axis references pressures '
                                                          'to the right atrium. Wrong leveling '
                                                          'produces falsely high or low readings '
                                                          'that misguide therapy.',
                                           'choice_explanations': {'A': 'Leveling to the insertion '
                                                                        'site is a believable '
                                                                        'setup error—assessment '
                                                                        'near-miss.',
                                                                   'B': 'Knee leveling does not '
                                                                        'reference atrial level.',
                                                                   'C': 'The bag spike is not the '
                                                                        'anatomic reference point.',
                                                                   'D': 'Phlebostatic axis '
                                                                        'leveling is the standard '
                                                                        'for arterial/CVP '
                                                                        'referencing.'}},
                                          {'question': 'Which intervention is part of a typical '
                                                       'ventilator-associated pneumonia (VAP) '
                                                       'prevention bundle?',
                                           'options': ['A) Head-of-bed elevation, oral care with '
                                                       'antiseptic, and sedation/weaning reviews '
                                                       'as protocolled',
                                                       'B) Daily circuit changes and keeping the '
                                                       'head of bed flat to reduce pressure injury '
                                                       'risk',
                                                       'C) Avoiding oral care to reduce secretions',
                                                       'D) Breaking circuit daily without '
                                                       'indication for “freshness”'],
                                           'answer': 'A) Head-of-bed elevation, oral care with '
                                                     'antiseptic, and sedation/weaning reviews as '
                                                     'protocolled',
                                           'explanation': 'VAP bundles reduce aspiration and '
                                                          'biofilm risk via HOB elevation, oral '
                                                          'antiseptic care, and daily '
                                                          'sedation/spontaneous breathing '
                                                          'assessments.',
                                           'choice_explanations': {'A': 'HOB elevation, oral care, '
                                                                        'and sedation/weaning '
                                                                        'practices are core bundle '
                                                                        'elements.',
                                                                   'B': 'Circuit changes plus flat '
                                                                        'HOB mixes '
                                                                        'infection-control myths '
                                                                        'with skin '
                                                                        'priorities—near-miss '
                                                                        'against VAP evidence.',
                                                                   'C': 'Oral care is a key VAP '
                                                                        'prevention element.',
                                                                   'D': 'Unnecessary circuit '
                                                                        'breaks increase '
                                                                        'contamination risk.'}}],
                                 'medium': [{'question': 'Central venous pressure (CVP) most '
                                                         'closely reflects which physiologic '
                                                         'concept at the bedside?',
                                             'options': ['A) Serum potassium concentration',
                                                         'B) Right-heart preload / right atrial '
                                                         'pressure trend (with interpretation '
                                                         'limits)',
                                                         'C) Pupil reactivity score',
                                                         'D) Left-ventricular end-diastolic volume '
                                                         'as a precise standalone '
                                                         'fluid-responsiveness number'],
                                             'answer': 'B) Right-heart preload / right atrial '
                                                       'pressure trend (with interpretation '
                                                       'limits)',
                                             'explanation': 'CVP approximates right atrial '
                                                            'pressure and is used as a crude '
                                                            'right-sided preload trend, '
                                                            'interpreted with exam and other '
                                                            'hemodynamics. It is not a precise LV '
                                                            'volume or fluid-responsiveness '
                                                            'guarantee.',
                                             'choice_explanations': {'A': 'Electrolytes are lab '
                                                                          'values, not CVP.',
                                                                     'B': 'CVP trends right atrial '
                                                                          'pressure/preload with '
                                                                          'known limitations.',
                                                                     'C': 'Pupils are neurologic '
                                                                          'findings unrelated to '
                                                                          'CVP meaning.',
                                                                     'D': 'Equating CVP with '
                                                                          'precise LV '
                                                                          'preload/fluid '
                                                                          'responsiveness is a '
                                                                          'common hemodynamic '
                                                                          'near-miss.'}},
                                            {'question': 'Which nursing measures help manage '
                                                         'increased intracranial pressure?',
                                             'options': ['A) Place in Trendelenburg continuously',
                                                         'B) Cluster complete nursing care into '
                                                         'long sessions so the patient can rest '
                                                         'undisturbed for hours afterward',
                                                         'C) Neutral head alignment, HOB elevation '
                                                         'if ordered, controlled '
                                                         'ventilation/oxygenation, and minimize '
                                                         'clustering of stimuli',
                                                         'D) Force coughing and Valsalva '
                                                         'frequently to “clear pressure”'],
                                             'answer': 'C) Neutral head alignment, HOB elevation '
                                                       'if ordered, controlled '
                                                       'ventilation/oxygenation, and minimize '
                                                       'clustering of stimuli',
                                             'explanation': 'ICP care maintains cerebral venous '
                                                            'drainage (neutral neck, HOB elevation '
                                                            'as ordered), avoids gas-exchange '
                                                            'extremes per goals, and limits '
                                                            'stimulatory clustering. Long '
                                                            'clustered noxious care can spike ICP.',
                                             'choice_explanations': {'A': 'Trendelenburg increases '
                                                                          'cerebral venous '
                                                                          'pressure.',
                                                                     'B': 'Clustering care for '
                                                                          'later rest sounds '
                                                                          'considerate but can '
                                                                          'cause prolonged ICP '
                                                                          'surges—near-miss.',
                                                                     'C': 'Alignment, ordered HOB '
                                                                          'elevation, gas-exchange '
                                                                          'control, and stimulus '
                                                                          'control lower ICP risk.',
                                                                     'D': 'Coughing/Valsalva '
                                                                          'transiently spike '
                                                                          'ICP.'}},
                                            {'question': 'In undifferentiated shock, what are the '
                                                         'first nursing priorities?',
                                             'options': ['A) Identify the exact shock subtype with '
                                                         'full diagnostics before oxygen, access, '
                                                         'or fluids',
                                                         'B) Focus only on giving oral fluids in '
                                                         'hypotensive patients',
                                                         'C) Place the patient in a chair and '
                                                         'ambulate vigorously',
                                                         'D) Support ABCs, obtain IV access, '
                                                         'monitor perfusion, and escalate while '
                                                         'etiology is pursued'],
                                             'answer': 'D) Support ABCs, obtain IV access, monitor '
                                                       'perfusion, and escalate while etiology is '
                                                       'pursued',
                                             'explanation': 'Shock care begins with airway, '
                                                            'breathing, circulation support, '
                                                            'access, and perfusion monitoring '
                                                            'while identifying the cause. '
                                                            'Resuscitation and diagnosis proceed '
                                                            'in parallel.',
                                             'choice_explanations': {'A': 'Subtype-first '
                                                                          'diagnostic delay is a '
                                                                          'classic shock '
                                                                          'near-miss.',
                                                                     'B': 'Oral fluids are '
                                                                          'inappropriate in many '
                                                                          'shocked patients.',
                                                                     'C': 'Ambulation is '
                                                                          'contraindicated in '
                                                                          'shock.',
                                                                     'D': 'ABC support plus access '
                                                                          'and escalation is the '
                                                                          'correct first priority '
                                                                          'set.'}}],
                                 'hard': [{'question': 'An intubated ARDS patient has refractory '
                                                       'hypoxemia. Which ventilation theme aligns '
                                                       'with lung-protective strategy?',
                                           'options': ['A) Low tidal volumes (~6 mL/kg PBW), '
                                                       'plateau-pressure limits, and PEEP/FiO2 '
                                                       'titration per protocol',
                                                       'B) Higher tidal volumes temporarily to '
                                                       'correct hypercapnia quickly, then return '
                                                       'to protective settings',
                                                       'C) Very large tidal volumes to “pop open” '
                                                       'all alveoli regardless of plateau pressure',
                                                       'D) Zero PEEP in all ARDS cases'],
                                           'answer': 'A) Low tidal volumes (~6 mL/kg PBW), '
                                                     'plateau-pressure limits, and PEEP/FiO2 '
                                                     'titration per protocol',
                                           'explanation': 'ARDSNet-style protection uses ~6 mL/kg '
                                                          'predicted body weight tidal volumes, '
                                                          'plateau-pressure limits, and PEEP/FiO2 '
                                                          'tables. Permissive hypercapnia is often '
                                                          'accepted rather than abandoning low Vt.',
                                           'choice_explanations': {'A': 'Low Vt, Pplat limits, and '
                                                                        'PEEP/FiO2 protocols '
                                                                        'define lung protection.',
                                                                   'B': 'Raising Vt to fix CO2 is '
                                                                        'a tempting near-miss that '
                                                                        'increases VILI risk.',
                                                                   'C': 'Large tidal volumes drive '
                                                                        'ventilator-induced lung '
                                                                        'injury.',
                                                                   'D': 'PEEP is used thoughtfully '
                                                                        'in ARDS to maintain '
                                                                        'recruitment.'}},
                                          {'question': 'After blunt chest trauma, a patient has '
                                                       'muffled heart sounds, JVD, and hypotension '
                                                       'with electrical activity on the monitor. '
                                                       'What classic condition should you suspect?',
                                           'options': ['A) Simple anxiety attack without '
                                                       'hemodynamic meaning',
                                                       'B) Cardiac tamponade (Beck’s triad '
                                                       'pattern) requiring urgent escalation',
                                                       'C) Uncomplicated dehydration alone',
                                                       'D) Tension pneumothorax as the first '
                                                       'explanation for hypotension with JVD after '
                                                       'chest trauma'],
                                           'answer': 'B) Cardiac tamponade (Beck’s triad pattern) '
                                                     'requiring urgent escalation',
                                           'explanation': 'Beck’s triad—hypotension, JVD, muffled '
                                                          'sounds—suggests tamponade physiology. '
                                                          'Tension pneumothorax is an important '
                                                          'trauma cousin but typically has '
                                                          'unilateral breath-sound loss/tracheal '
                                                          'deviation rather than muffled '
                                                          'heartsounds as the hallmark.',
                                           'choice_explanations': {'A': 'Objective shock signs are '
                                                                        'not explained by anxiety.',
                                                                   'B': 'Muffled sounds, JVD, and '
                                                                        'hypotension classic for '
                                                                        'tamponade needing urgent '
                                                                        'action.',
                                                                   'C': 'Dehydration alone does '
                                                                        'not muffle heart sounds.',
                                                                   'D': 'Tension pneumothorax is '
                                                                        'the key obstructive-shock '
                                                                        'differential—priority/assessment '
                                                                        'near-miss.'}},
                                          {'question': 'In DKA, which nursing priority cluster is '
                                                       'most accurate while insulin and fluids are '
                                                       'ordered?',
                                           'options': ['A) Give subcutaneous insulin only and '
                                                       'encourage sugary drinks',
                                                       'B) Start insulin promptly and bolus '
                                                       'potassium only after the anion gap fully '
                                                       'closes',
                                                       'C) Airway/hemodynamic support, fluid '
                                                       'resuscitation as ordered, insulin therapy, '
                                                       'and close electrolyte (especially '
                                                       'potassium) monitoring',
                                                       'D) Stop all potassium monitoring because '
                                                       'insulin raises potassium'],
                                           'answer': 'C) Airway/hemodynamic support, fluid '
                                                     'resuscitation as ordered, insulin therapy, '
                                                     'and close electrolyte (especially potassium) '
                                                     'monitoring',
                                           'explanation': 'DKA care prioritizes ABCs, volume '
                                                          'replacement, insulin to stop '
                                                          'ketogenesis, and electrolyte '
                                                          'management—potassium often falls with '
                                                          'insulin and must be watched throughout, '
                                                          'not only after gap closure.',
                                           'choice_explanations': {'A': 'DKA usually needs IV '
                                                                        'insulin/fluids, not '
                                                                        'sugary drinks.',
                                                                   'B': 'Delaying potassium '
                                                                        'attention until gap '
                                                                        'closure misunderstands '
                                                                        'early K shifts—near-miss.',
                                                                   'C': 'Fluids, insulin, and '
                                                                        'electrolyte/ABC vigilance '
                                                                        'are the DKA nursing '
                                                                        'pillars.',
                                                                   'D': 'Insulin drives potassium '
                                                                        'intracellularly; '
                                                                        'monitoring/replacement '
                                                                        'are critical.'}}],
                                 'extreme': [{'question': 'You are alone at the bedside when the '
                                                          'monitor shows pulseless ventricular '
                                                          'tachycardia; the patient is '
                                                          'unresponsive. A family member forbids '
                                                          'you to shock “until the priest '
                                                          'arrives,” and the defibrillator pads '
                                                          'are in the drawer. What is the correct '
                                                          'immediate action sequence?',
                                              'options': ['A) Confirm asystole vs artifact with a '
                                                          'pulse check lasting a full minute '
                                                          'before shocking',
                                                          'B) Wait for clergy before any '
                                                          'intervention',
                                                          'C) Give a fluid bolus as the sole '
                                                          'therapy for pulseless VT',
                                                          'D) Start CPR, apply pads, defibrillate '
                                                          'as indicated for pulseless VT/VF, and '
                                                          'activate the code team'],
                                              'answer': 'D) Start CPR, apply pads, defibrillate as '
                                                        'indicated for pulseless VT/VF, and '
                                                        'activate the code team',
                                              'explanation': 'Pulseless VT is a shockable arrest '
                                                             'rhythm. Immediate CPR and '
                                                             'defibrillation save lives; prolonged '
                                                             'pulse checks and non-emergent delays '
                                                             'are harmful. Family objections do '
                                                             'not override emergency implied '
                                                             'consent when no DNR is established.',
                                              'choice_explanations': {'A': 'Over-long rhythm/pulse '
                                                                           'confirmation delays '
                                                                           'defibrillation—near-miss.',
                                                                      'B': 'Clergy presence is not '
                                                                           'a prerequisite for '
                                                                           'defibrillation.',
                                                                      'C': 'Fluids alone do not '
                                                                           'treat pulseless VT.',
                                                                      'D': 'CPR plus '
                                                                           'defibrillation for '
                                                                           'pulseless VT/VF with '
                                                                           'code activation is '
                                                                           'required.'}},
                                             {'question': 'A trauma patient in hemorrhagic shock '
                                                          'is receiving a massive transfusion. '
                                                          'Temperature is 34.8°C, ionized calcium '
                                                          'is low, and oozing worsens. Which '
                                                          'priority cluster is most appropriate?',
                                              'options': ['A) Warm the patient/products, replace '
                                                          'calcium as ordered, follow MTP ratios, '
                                                          'and preserve transfusion safety checks',
                                                          'B) Prioritize speed by giving products '
                                                          'wide open while deferring warming and '
                                                          'calcium until bleeding slows',
                                                          'C) Stop all blood products and give '
                                                          'only hypotonic free water',
                                                          'D) Give unmatched products from '
                                                          'unlabeled syringes to save time'],
                                              'answer': 'A) Warm the patient/products, replace '
                                                        'calcium as ordered, follow MTP ratios, '
                                                        'and preserve transfusion safety checks',
                                              'explanation': 'Massive transfusion complications '
                                                             'include hypothermia, hypocalcemia, '
                                                             'and coagulopathy. Warming, calcium '
                                                             'replacement, balanced ratios, and '
                                                             'identification checks proceed with '
                                                             'resuscitation—not after.',
                                              'choice_explanations': {'A': 'Warming, calcium, MTP '
                                                                           'ratios, and safety '
                                                                           'checks address lethal '
                                                                           'triad drivers.',
                                                                      'B': 'Speed-over-warming/calcium '
                                                                           'is a common MTP '
                                                                           'near-miss that worsens '
                                                                           'coagulopathy.',
                                                                      'C': 'Stopping blood for '
                                                                           'hypotonic water is '
                                                                           'wrong in hemorrhagic '
                                                                           'shock.',
                                                                      'D': 'Unlabeled unmatched '
                                                                           'products create '
                                                                           'catastrophic error '
                                                                           'risk.'}},
                                             {'question': 'The team is preparing clinical '
                                                          'brain-death testing on an ICU patient. '
                                                          'A junior nurse plans to give a sedative '
                                                          'bolus “so the exam is calm,” and family '
                                                          'asks what nursing’s role is. What '
                                                          'should you do?',
                                              'options': ['A) Give extra propofol to guarantee '
                                                          'unresponsiveness for the exam',
                                                          'B) Clarify that confounding '
                                                          'sedation/metabolic issues must be '
                                                          'absent; support family, maintain '
                                                          'physiology per protocol, and escalate '
                                                          'concerns about the planned sedative',
                                                          'C) Tell family brain-death testing is '
                                                          'optional entertainment',
                                                          'D) Lighten sedation just enough for the '
                                                          'exam but give a small anxiolytic so the '
                                                          'family sees a peaceful face'],
                                              'answer': 'B) Clarify that confounding '
                                                        'sedation/metabolic issues must be absent; '
                                                        'support family, maintain physiology per '
                                                        'protocol, and escalate concerns about the '
                                                        'planned sedative',
                                              'explanation': 'Brain-death determination requires '
                                                             'absence of confounders such as '
                                                             'residual sedation. Nurses advocate '
                                                             'for valid testing conditions, '
                                                             'physiologic support per protocol, '
                                                             'and truthful family communication.',
                                              'choice_explanations': {'A': 'Extra propofol '
                                                                           'invalidates neurologic '
                                                                           'testing.',
                                                                      'B': 'Removing confounders, '
                                                                           'supporting family, and '
                                                                           'escalating unsafe exam '
                                                                           'plans is correct.',
                                                                      'C': 'Brain-death evaluation '
                                                                           'is a solemn '
                                                                           'clinical/legal '
                                                                           'process, not '
                                                                           'entertainment.',
                                                                      'D': 'Any sedative for '
                                                                           'appearance during '
                                                                           'brain-death testing '
                                                                           'confounds the '
                                                                           'exam—near-miss.'}}]},
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
                   'questions': {'easy': [{'question': 'The “rights” of medication administration '
                                                       'primarily exist to prevent which type of '
                                                       'error?',
                                           'options': ['A) Mainly wrong-time errors, since other '
                                                       'checks are handled by pharmacy barcoding '
                                                       'alone',
                                                       'B) Only billing mistakes on the hospital '
                                                       'invoice',
                                                       'C) Errors related only to visitor visiting '
                                                       'hours',
                                                       'D) Wrong patient, drug, dose, route, time '
                                                       '(and related rights such as '
                                                       'documentation/reason)'],
                                           'answer': 'D) Wrong patient, drug, dose, route, time '
                                                     '(and related rights such as '
                                                     'documentation/reason)',
                                           'explanation': 'Medication rights systematize identity, '
                                                          'drug, dose, route, time, documentation, '
                                                          'and reason checks to interrupt common '
                                                          'administration error pathways.',
                                           'choice_explanations': {'A': 'Narrowing rights to '
                                                                        'timing because pharmacy '
                                                                        'technology “covers the '
                                                                        'rest” is a safety '
                                                                        'near-miss.',
                                                                   'B': 'Rights target clinical '
                                                                        'administration safety, '
                                                                        'not invoices.',
                                                                   'C': 'Visiting hours are '
                                                                        'unrelated to med-rights '
                                                                        'framework.',
                                                                   'D': 'Patient/drug/dose/route/time '
                                                                        '(plus related rights) '
                                                                        'prevent core med '
                                                                        'errors.'}},
                                          {'question': 'Before giving digoxin, which assessment is '
                                                       'most classically required?',
                                           'options': ['A) Apical pulse (and review of '
                                                       'potassium/digoxin-toxicity cues per '
                                                       'protocol)',
                                                       'B) Radial pulse rate alone, because '
                                                       'peripheral rate equals apical rate for '
                                                       'hold parameters',
                                                       'C) Pupil size only',
                                                       'D) Stool occult blood only'],
                                           'answer': 'A) Apical pulse (and review of '
                                                     'potassium/digoxin-toxicity cues per '
                                                     'protocol)',
                                           'explanation': 'Digoxin slows conduction; apical rate '
                                                          'below hold parameters and hypokalemia '
                                                          'raise toxicity/bradyarrhythmia risk. '
                                                          'Nurses check apical pulse and relevant '
                                                          'labs/symptoms before administration.',
                                           'choice_explanations': {'A': 'Apical pulse plus '
                                                                        'potassium/toxicity '
                                                                        'surveillance is the '
                                                                        'standard nursing check.',
                                                                   'B': 'Radial-only counting '
                                                                        'misses pulse deficits and '
                                                                        'is a classic assessment '
                                                                        'near-miss.',
                                                                   'C': 'Pupils are not the '
                                                                        'primary digoxin hold '
                                                                        'parameter.',
                                                                   'D': 'Occult blood is not the '
                                                                        'classic pre-digoxin '
                                                                        'check.'}},
                                          {'question': 'What needle angle is typically used for a '
                                                       'standard intramuscular injection?',
                                           'options': ['A) 10° into the dermis only',
                                                       'B) 90° into muscle (unless a specific '
                                                       'alternative technique is indicated)',
                                                       'C) 0° parallel to skin for all IM vaccines',
                                                       'D) 45° with a skinfold, using the same '
                                                       'angle taught for subcutaneous injections'],
                                           'answer': 'B) 90° into muscle (unless a specific '
                                                     'alternative technique is indicated)',
                                           'explanation': 'IM injections are generally delivered '
                                                          'at 90° to deposit medication in muscle. '
                                                          'Intradermal uses ~10–15°; subcutaneous '
                                                          'often 45–90° depending on '
                                                          'needle/fold—not the IM default.',
                                           'choice_explanations': {'A': '≈10–15° is intradermal '
                                                                        'technique.',
                                                                   'B': '90° IM angle targets '
                                                                        'muscle for intended '
                                                                        'absorption.',
                                                                   'C': 'Parallel-to-skin '
                                                                        'technique is not IM '
                                                                        'administration.',
                                                                   'D': '45° with skinfold '
                                                                        'confuses IM with '
                                                                        'subcutaneous '
                                                                        'technique—near-miss.'}}],
                                 'medium': [{'question': 'Which teaching point is essential for a '
                                                         'patient newly started on warfarin?',
                                             'options': ['A) Take NSAIDs freely because they '
                                                         'protect the stomach on warfarin',
                                                         'B) Avoid all green vegetables '
                                                         'permanently and skip INR checks if no '
                                                         'bleeding is visible',
                                                         'C) Report unusual bleeding/bruising, '
                                                         'keep INR monitoring, and maintain '
                                                         'consistent vitamin K intake',
                                                         'D) Double doses after any missed tablet '
                                                         'without advice'],
                                             'answer': 'C) Report unusual bleeding/bruising, keep '
                                                       'INR monitoring, and maintain consistent '
                                                       'vitamin K intake',
                                             'explanation': 'Warfarin’s narrow index requires INR '
                                                            'surveillance, bleeding precautions, '
                                                            'and consistent vitamin K intake—not '
                                                            'total elimination of greens or '
                                                            'skipping labs when asymptomatic.',
                                             'choice_explanations': {'A': 'NSAIDs increase '
                                                                          'bleeding risk with '
                                                                          'warfarin.',
                                                                     'B': 'Zero-vitamin-K plus '
                                                                          'symptom-only monitoring '
                                                                          'is a common teaching '
                                                                          'near-miss.',
                                                                     'C': 'Bleeding awareness, INR '
                                                                          'follow-up, and vitamin '
                                                                          'K consistency are core '
                                                                          'warfarin teaching.',
                                                                     'D': 'Unadvised double dosing '
                                                                          'can cause '
                                                                          'life-threatening '
                                                                          'hemorrhage.'}},
                                            {'question': 'When giving an IV push opioid, which '
                                                         'nursing requirement is most important?',
                                             'options': ['A) Give the push promptly, then leave '
                                                         'pulse oximetry in place and return after '
                                                         'other meds',
                                                         'B) Push as fast as possible to finish '
                                                         'rounds sooner',
                                                         'C) Mix with unknown leftover syringe '
                                                         'contents to avoid waste',
                                                         'D) Administer at the recommended rate '
                                                         'while monitoring sedation and '
                                                         'respiratory status'],
                                             'answer': 'D) Administer at the recommended rate '
                                                       'while monitoring sedation and respiratory '
                                                       'status',
                                             'explanation': 'IV opioids can cause rapid '
                                                            'respiratory depression. Correct push '
                                                            'rates and close sedation/RR/SpO2 '
                                                            'monitoring reduce overdose risk. '
                                                            'Leaving the patient after a rapid '
                                                            'push is unsafe.',
                                             'choice_explanations': {'A': 'Monitor-on-and-leave '
                                                                          'after a prompt push is '
                                                                          'a supervision '
                                                                          'near-miss.',
                                                                     'B': 'Rapid push spikes '
                                                                          'CNS/respiratory '
                                                                          'depression risk.',
                                                                     'C': 'Unidentified syringe '
                                                                          'mixing risks dosing and '
                                                                          'contamination errors.',
                                                                     'D': 'Rate control plus '
                                                                          'respiratory/sedation '
                                                                          'monitoring is '
                                                                          'mandatory.'}},
                                            {'question': 'When mixing regular (clear) and NPH '
                                                         '(cloudy) insulin in one syringe, which '
                                                         'theme is correct?',
                                             'options': ['A) Inject air into NPH then regular, '
                                                         'draw regular (clear) first, then '
                                                         'NPH—avoid contaminating the regular vial',
                                                         'B) Draw NPH first if it is the larger '
                                                         'dose, then regular, to reduce mixing '
                                                         'error in the syringe',
                                                         'C) Shake NPH violently until foam '
                                                         'appears',
                                                         'D) Use the same needle to pierce '
                                                         'multiple patient vials interchangeably'],
                                             'answer': 'A) Inject air into NPH then regular, draw '
                                                       'regular (clear) first, then NPH—avoid '
                                                       'contaminating the regular vial',
                                             'explanation': 'Clear-before-cloudy drawing after '
                                                            'appropriate air injection prevents '
                                                            'regular-insulin vial contamination '
                                                            'with NPH.',
                                             'choice_explanations': {'A': 'Air steps then '
                                                                          'clear-before-cloudy '
                                                                          'preserves regular vial '
                                                                          'integrity.',
                                                                     'B': 'Larger-dose-first logic '
                                                                          'sounds practical but '
                                                                          'contaminates the clear '
                                                                          'vial—near-miss.',
                                                                     'C': 'Violent shaking creates '
                                                                          'foam and dosing '
                                                                          'inaccuracy; roll/gentle '
                                                                          'mix per teaching.',
                                                                     'D': 'Multi-patient vial '
                                                                          'needle sharing risks '
                                                                          'contamination.'}}],
                                 'hard': [{'question': 'Which medications are classic high-alert '
                                                       'examples requiring extra nursing '
                                                       'safeguards?',
                                           'options': ['A) Bulk laxatives only, with no other '
                                                       'categories',
                                                       'B) Insulin, anticoagulants, opioids, and '
                                                       'concentrated electrolytes',
                                                       'C) Topical emollients exclusively',
                                                       'D) Antibiotics and antiemetics, because '
                                                       'allergic reactions are the main high-alert '
                                                       'pathway'],
                                           'answer': 'B) Insulin, anticoagulants, opioids, and '
                                                     'concentrated electrolytes',
                                           'explanation': 'High-alert drugs cause severe harm when '
                                                          'misused—insulin, anticoagulants, '
                                                          'opioids, and concentrated electrolytes '
                                                          'head most lists. Allergy-prone drugs '
                                                          'need caution but are not the classic '
                                                          'high-alert set.',
                                           'choice_explanations': {'A': 'Laxatives are not the '
                                                                        'defining high-alert '
                                                                        'group.',
                                                                   'B': 'Insulin, anticoagulants, '
                                                                        'opioids, and concentrated '
                                                                        'electrolytes are '
                                                                        'prototypical high-alert '
                                                                        'classes.',
                                                                   'C': 'Emollients lack the '
                                                                        'catastrophic harm profile '
                                                                        'of high-alert meds.',
                                                                   'D': 'Allergy-focused '
                                                                        'antibiotic/antiemetic '
                                                                        'framing is a related '
                                                                        'safety near-miss, not the '
                                                                        'high-alert definition.'}},
                                          {'question': 'Vancomycin “red man syndrome” is most '
                                                       'related to which administration issue?',
                                           'options': ['A) Taking vancomycin with grapefruit juice '
                                                       'exclusively',
                                                       'B) IgE-mediated anaphylaxis that always '
                                                       'requires lifelong vancomycin avoidance '
                                                       'after one flush',
                                                       'C) Too-rapid infusion causing '
                                                       'histamine-release flushing/hypotension',
                                                       'D) Giving the dose intramuscularly into '
                                                       'the deltoid only'],
                                           'answer': 'C) Too-rapid infusion causing '
                                                     'histamine-release flushing/hypotension',
                                           'explanation': 'Rapid vancomycin infusion triggers '
                                                          'mast-cell histamine release with '
                                                          'flushing, rash, and possible '
                                                          'hypotension. Slowing the infusion '
                                                          'manages red man syndrome; it is '
                                                          'rate-related and distinct from true '
                                                          'anaphylaxis, though severe reactions '
                                                          'still need urgent care.',
                                           'choice_explanations': {'A': 'Grapefruit interactions '
                                                                        'are not the classic '
                                                                        'red-man cause.',
                                                                   'B': 'Labeling every flush as '
                                                                        'anaphylaxis requiring '
                                                                        'permanent avoidance is a '
                                                                        'differential near-miss.',
                                                                   'C': 'Rate-related histamine '
                                                                        'release explains red man '
                                                                        'syndrome.',
                                                                   'D': 'Vancomycin is typically '
                                                                        'IV; IM deltoid is not the '
                                                                        'red-man mechanism.'}},
                                          {'question': 'Why must concentrated IV potassium never '
                                                       'be given as an undiluted IV push?',
                                           'options': ['A) Because peripheral IV potassium is '
                                                       'acceptable as a slow push if continuous '
                                                       'ECG is monitored',
                                                       'B) Because potassium tastes bitter if '
                                                       'pushed',
                                                       'C) Because potassium only works orally',
                                                       'D) Because undiluted IV push can cause '
                                                       'fatal dysrhythmias; it requires diluted, '
                                                       'pump-controlled infusion per policy'],
                                           'answer': 'D) Because undiluted IV push can cause fatal '
                                                     'dysrhythmias; it requires diluted, '
                                                     'pump-controlled infusion per policy',
                                           'explanation': 'Bolus concentrated KCl can cause '
                                                          'immediate cardiac arrest. Policies '
                                                          'require dilution, maximum rates, pump '
                                                          'control, and often central access for '
                                                          'higher concentrations—never undiluted '
                                                          'IV push.',
                                           'choice_explanations': {'A': '“Slow push with ECG” '
                                                                        'still violates '
                                                                        'push/concentrate '
                                                                        'rules—dangerous '
                                                                        'near-miss.',
                                                                   'B': 'Taste is irrelevant to IV '
                                                                        'cardiac toxicity.',
                                                                   'C': 'IV potassium is used when '
                                                                        'oral route is inadequate, '
                                                                        'but safely infused.',
                                                                   'D': 'Fatal dysrhythmia risk '
                                                                        'mandates diluted, '
                                                                        'rate-controlled '
                                                                        'infusion.'}}],
                                 'extreme': [{'question': 'Minutes after succinylcholine, a '
                                                          'surgical patient develops ETCO2 rise, '
                                                          'jaw rigidity, temperature climbing '
                                                          'through 39°C, and mixed acidosis. The '
                                                          'anesthesia tech suggests “just give '
                                                          'more inhalational agent.” What should '
                                                          'the nurse anticipate as the priority '
                                                          'treatment pathway?',
                                              'options': ['A) Call malignant hyperthermia '
                                                          'response: stop triggers, hyperventilate '
                                                          'with 100% O2, give dantrolene, and cool',
                                                          'B) Treat as sepsis-related fever: '
                                                          'cultures, broad antibiotics, and '
                                                          'antipyretics while surgery continues',
                                                          'C) Continue triggering agents and cover '
                                                          'with warm blankets',
                                                          'D) Treat as anxiety and give midazolam '
                                                          'only'],
                                              'answer': 'A) Call malignant hyperthermia response: '
                                                        'stop triggers, hyperventilate with 100% '
                                                        'O2, give dantrolene, and cool',
                                              'explanation': 'Rising ETCO2, jaw rigidity, and '
                                                             'escalating temperature after '
                                                             'succinylcholine suggest malignant '
                                                             'hyperthermia. Stop triggers, give '
                                                             'dantrolene, hyperventilate with 100% '
                                                             'O2, and cool—do not treat as '
                                                             'ordinary fever.',
                                              'choice_explanations': {'A': 'MH protocol with '
                                                                           'dantrolene and trigger '
                                                                           'cessation is required.',
                                                                      'B': 'Intraoperative fever '
                                                                           'workup for sepsis '
                                                                           'delays MH-specific '
                                                                           'therapy—near-miss.',
                                                                      'C': 'Continuing triggers '
                                                                           'and warming worsens '
                                                                           'MH.',
                                                                      'D': 'Anxiolysis does not '
                                                                           'treat MH '
                                                                           'hypermetabolism.'}},
                                             {'question': 'A postoperative patient on a PCA has RR '
                                                          '4, pinpoint pupils, SpO2 82%, and is '
                                                          'barely arousable. A visitor says the '
                                                          'patient “needs another click for pain.” '
                                                          'What is the priority action?',
                                              'options': ['A) Encourage the visitor to press the '
                                                          'PCA button repeatedly',
                                                          'B) Support airway/ventilation, stop '
                                                          'opioid input, give naloxone per '
                                                          'protocol, and activate rapid response',
                                                          'C) Increase the PCA basal rate to '
                                                          'overcome tolerance',
                                                          'D) Stimulate the patient and reduce the '
                                                          'PCA dose, holding naloxone unless apnea '
                                                          'persists another 10 minutes'],
                                              'answer': 'B) Support airway/ventilation, stop '
                                                        'opioid input, give naloxone per protocol, '
                                                        'and activate rapid response',
                                              'explanation': 'RR 4, pinpoint pupils, hypoxia, and '
                                                             'unresponsiveness indicate '
                                                             'opioid-induced respiratory '
                                                             'depression. Support ventilation, '
                                                             'stop opioid input, and give naloxone '
                                                             'while activating help.',
                                              'choice_explanations': {'A': 'Visitor PCA presses '
                                                                           'worsen overdose.',
                                                                      'B': 'Airway/ventilation '
                                                                           'support with naloxone '
                                                                           'and rapid response is '
                                                                           'the priority.',
                                                                      'C': 'Increasing basal '
                                                                           'opioid deepens '
                                                                           'hypoventilation.',
                                                                      'D': 'Stimulate-and-wait '
                                                                           'before naloxone is a '
                                                                           'common delay near-miss '
                                                                           'in severe '
                                                                           'depression.'}},
                                             {'question': 'During peripheral chemotherapy '
                                                          'infusion, the patient reports burning; '
                                                          'the site is swollen and cool, and no '
                                                          'blood return is obtained. The protocol '
                                                          'labels the drug a vesicant. What should '
                                                          'you do?',
                                              'options': ['A) Apply a tight arterial tourniquet '
                                                          'above the site for hours',
                                                          'B) Pause briefly, restart at a slower '
                                                          'rate if swelling seems stable, and warm '
                                                          'the site',
                                                          'C) Stop the infusion, aspirate residual '
                                                          'per protocol, mark the site, notify the '
                                                          'provider/pharmacy, and follow vesicant '
                                                          'extravasation orders',
                                                          'D) Speed the infusion to finish before '
                                                          'swelling worsens'],
                                              'answer': 'C) Stop the infusion, aspirate residual '
                                                        'per protocol, mark the site, notify the '
                                                        'provider/pharmacy, and follow vesicant '
                                                        'extravasation orders',
                                              'explanation': 'Burning, swelling, coolness, and no '
                                                             'blood return during vesicant '
                                                             'infusion suggest extravasation. '
                                                             'Stop, aspirate per protocol, mark, '
                                                             'notify, and use drug-specific '
                                                             'antidote/thermal measures—do not '
                                                             'restart.',
                                              'choice_explanations': {'A': 'Arterial tourniquets '
                                                                           'are not extravasation '
                                                                           'first aid.',
                                                                      'B': 'Slow-restart with '
                                                                           'warmth is a harmful '
                                                                           'near-miss for many '
                                                                           'vesicants.',
                                                                      'C': 'Stop–aspirate–mark–notify–protocol '
                                                                           'care is required for '
                                                                           'vesicant '
                                                                           'extravasation.',
                                                                      'D': 'Speeding infusion '
                                                                           'increases '
                                                                           'extravasation '
                                                                           'injury.'}}]},
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
                       'questions': {'easy': [{'question': 'In healthcare ethics, autonomy '
                                                           'primarily means which idea?',
                                               'options': ['A) Respect for a capacitated person’s '
                                                           'right to make informed choices about '
                                                           'their care',
                                                           'B) Doing what clinicians judge best '
                                                           'for the patient when the choice seems '
                                                           'unwise',
                                                           'C) Staff may decide all treatments '
                                                           'without patient input',
                                                           'D) Keeping patients uninformed to '
                                                           'reduce anxiety'],
                                               'answer': 'A) Respect for a capacitated person’s '
                                                         'right to make informed choices about '
                                                         'their care',
                                               'explanation': 'Autonomy respects informed '
                                                              'self-determination by capacitated '
                                                              'patients. Beneficent paternalism '
                                                              'that overrides capacitated choices '
                                                              'is a related but distinct ethical '
                                                              'tension.',
                                               'choice_explanations': {'A': 'Informed '
                                                                            'self-determination is '
                                                                            'the definition of '
                                                                            'autonomy.',
                                                                       'B': 'Clinician-judged '
                                                                            '“best interest” '
                                                                            'override is '
                                                                            'beneficence/paternalism—ethical '
                                                                            'near-miss for '
                                                                            'autonomy.',
                                                                       'C': 'Excluding the patient '
                                                                            'negates autonomy.',
                                                                       'D': 'Withholding '
                                                                            'information blocks '
                                                                            'informed choice.'}},
                                              {'question': 'Beneficence in nursing ethics most '
                                                           'nearly means?',
                                               'options': ['A) Maximizing billable procedures '
                                                           'regardless of benefit',
                                                           'B) Acting to promote the patient’s '
                                                           'good and well-being',
                                                           'C) Following only personal convenience',
                                                           'D) Avoiding harm first, even if that '
                                                           'means withholding beneficial indicated '
                                                           'treatments'],
                                               'answer': 'B) Acting to promote the patient’s good '
                                                         'and well-being',
                                               'explanation': 'Beneficence is the obligation to '
                                                              'benefit the patient—promoting '
                                                              'health and welfare. It is balanced '
                                                              'with autonomy and nonmaleficence, '
                                                              'not identical to “do no harm” '
                                                              'alone.',
                                               'choice_explanations': {'A': 'Profit-driven excess '
                                                                            'is not beneficence.',
                                                                       'B': 'Promoting patient '
                                                                            'good is beneficence.',
                                                                       'C': 'Convenience is not an '
                                                                            'ethical principle of '
                                                                            'beneficence.',
                                                                       'D': 'Equating beneficence '
                                                                            'with '
                                                                            'nonmaleficence-only '
                                                                            'is a principle '
                                                                            'near-miss.'}},
                                              {'question': 'Which situation is a confidentiality '
                                                           'breach?',
                                               'options': ['A) Sharing need-to-know details with '
                                                           'the interprofessional care team',
                                                           'B) Giving a shift hand-off at the '
                                                           'nursing station where visitors might '
                                                           'overhear details',
                                                           'C) Discussing identifiable patient '
                                                           'details with friends in an elevator',
                                                           'D) Hand-off report to the oncoming '
                                                           'nurse in a private area'],
                                               'answer': 'C) Discussing identifiable patient '
                                                         'details with friends in an elevator',
                                               'explanation': 'Confidentiality limits PHI to '
                                                              'need-to-know care contexts. '
                                                              'Elevator gossip is a clear breach; '
                                                              'station handoffs with possible '
                                                              'overhearing are privacy risks but '
                                                              'still clinical handoff—often tested '
                                                              'as the overlapping concern.',
                                               'choice_explanations': {'A': 'Care-team '
                                                                            'need-to-know sharing '
                                                                            'supports treatment.',
                                                                       'B': 'Clinical handoff in a '
                                                                            'semi-public station '
                                                                            'is a privacy '
                                                                            'near-miss that still '
                                                                            'differs from social '
                                                                            'gossip.',
                                                                       'C': 'Non-care gossip with '
                                                                            'identifiers violates '
                                                                            'confidentiality.',
                                                                       'D': 'Private clinical '
                                                                            'handoff is '
                                                                            'appropriate '
                                                                            'information '
                                                                            'sharing.'}}],
                                     'medium': [{'question': 'Nonmaleficence most directly '
                                                             'obligates the nurse to do which?',
                                                 'options': ['A) Promote good outcomes '
                                                             'aggressively even when the '
                                                             'intervention adds significant '
                                                             'preventable risk',
                                                             'B) Guarantee every outcome will be '
                                                             'perfect',
                                                             'C) Refuse to report errors so nobody '
                                                             'is upset',
                                                             'D) Avoid causing unjustified harm '
                                                             'and minimize risk in care'],
                                                 'answer': 'D) Avoid causing unjustified harm and '
                                                           'minimize risk in care',
                                                 'explanation': 'Nonmaleficence—“do no '
                                                                'harm”—requires avoiding '
                                                                'unjustified injury and reducing '
                                                                'foreseeable risk. Aggressive '
                                                                'benefit-seeking without risk '
                                                                'regard confuses beneficence with '
                                                                'nonmaleficence.',
                                                 'choice_explanations': {'A': 'Benefit-at-any-risk '
                                                                              'thinking is the '
                                                                              'beneficence/nonmaleficence '
                                                                              'near-miss.',
                                                                         'B': 'Ethics does not '
                                                                              'require impossible '
                                                                              'outcome guarantees.',
                                                                         'C': 'Hiding errors '
                                                                              'increases harm '
                                                                              'potential.',
                                                                         'D': 'Minimizing '
                                                                              'unjustified harm is '
                                                                              'the core of '
                                                                              'nonmaleficence.'}},
                                                {'question': 'Justice as a nursing ethical '
                                                             'principle primarily concerns which '
                                                             'issue?',
                                                 'options': ['A) Fair allocation of resources and '
                                                             'equitable treatment without unjust '
                                                             'discrimination',
                                                             'B) Treating every patient with '
                                                             'identical resources regardless of '
                                                             'clinical need or acuity',
                                                             'C) Giving VIP patients unlimited '
                                                             'unequal access by default',
                                                             'D) Ignoring marginalized '
                                                             'populations’ barriers'],
                                                 'answer': 'A) Fair allocation of resources and '
                                                           'equitable treatment without unjust '
                                                           'discrimination',
                                                 'explanation': 'Justice addresses fairness in '
                                                                'distribution of care and '
                                                                'resources and opposition to '
                                                                'unjust discrimination. Equal '
                                                                'shares regardless of need is '
                                                                'sameness, not equity.',
                                                 'choice_explanations': {'A': 'Fair, '
                                                                              'nondiscriminatory '
                                                                              'allocation is the '
                                                                              'justice principle.',
                                                                         'B': 'Identical '
                                                                              'allocation ignoring '
                                                                              'acuity confuses '
                                                                              'equality with '
                                                                              'equity—near-miss.',
                                                                         'C': 'Unjust VIP '
                                                                              'preference violates '
                                                                              'justice.',
                                                                         'D': 'Ignoring barriers '
                                                                              'perpetuates '
                                                                              'inequity.'}},
                                                {'question': 'What is the primary purpose of an '
                                                             'incident (occurrence) report?',
                                                 'options': ['A) Punish staff publicly in the '
                                                             'newspaper',
                                                             'B) Document events for system '
                                                             'learning and risk reduction '
                                                             '(quality/safety), separate from '
                                                             'blame-focused charting',
                                                             'C) Replace the need for any clinical '
                                                             'documentation in the record',
                                                             'D) Create a detailed narrative in '
                                                             'the medical record that assigns '
                                                             'individual blame for later '
                                                             'discipline'],
                                                 'answer': 'B) Document events for system learning '
                                                           'and risk reduction (quality/safety), '
                                                           'separate from blame-focused charting',
                                                 'explanation': 'Incident reports feed '
                                                                'institutional safety learning and '
                                                                'risk management. They are not '
                                                                'substitutes for factual clinical '
                                                                'charting and should not be used '
                                                                'primarily as blame vehicles in '
                                                                'the record.',
                                                 'choice_explanations': {'A': 'Public punishment '
                                                                              'is not the purpose '
                                                                              'of incident '
                                                                              'reporting.',
                                                                         'B': 'System learning and '
                                                                              'risk reduction are '
                                                                              'the primary aims.',
                                                                         'C': 'The medical record '
                                                                              'still needs factual '
                                                                              'clinical '
                                                                              'documentation.',
                                                                         'D': 'Blame-focused '
                                                                              'charting conflates '
                                                                              'incident reporting '
                                                                              'with punitive '
                                                                              'documentation—near-miss.'}}],
                                     'hard': [{'question': 'Advocacy in nursing leadership most '
                                                           'accurately means which action?',
                                               'options': ['A) Prioritizing personal overtime pay '
                                                           'above all patient needs',
                                                           'B) Supporting the care team’s harmony '
                                                           'by raising safety concerns only after '
                                                           'consensus is certain',
                                                           'C) Speaking and acting to protect '
                                                           'patients’ rights, safety, and best '
                                                           'interests—including challenging unsafe '
                                                           'practices',
                                                           'D) Remaining silent when unsafe orders '
                                                           'endanger patients'],
                                               'answer': 'C) Speaking and acting to protect '
                                                         'patients’ rights, safety, and best '
                                                         'interests—including challenging unsafe '
                                                         'practices',
                                               'explanation': 'Advocacy elevates patient rights '
                                                              'and safety, including escalating '
                                                              'concerns about unsafe care. Waiting '
                                                              'for perfect consensus can delay '
                                                              'protection.',
                                               'choice_explanations': {'A': 'Personal pay is not '
                                                                            'the definition of '
                                                                            'patient advocacy.',
                                                                       'B': 'Harmony-first delayed '
                                                                            'escalation is an '
                                                                            'advocacy near-miss.',
                                                                       'C': 'Protecting '
                                                                            'rights/safety, '
                                                                            'including challenging '
                                                                            'unsafe practice, '
                                                                            'defines advocacy.',
                                                                       'D': 'Silence with known '
                                                                            'danger abandons '
                                                                            'advocacy.'}},
                                              {'question': 'What is the nurse’s usual role related '
                                                           'to informed consent?',
                                               'options': ['A) Explain surgical risks in detail '
                                                           'yourself so consent is complete before '
                                                           'the provider arrives',
                                                           'B) Forge a signature if the patient is '
                                                           'asleep to keep the OR on time',
                                                           'C) Ignore questions because consent is '
                                                           '“already done”',
                                                           'D) Witness signature, verify '
                                                           'understanding, and advocate if the '
                                                           'patient seems unclear—while the '
                                                           'provider obtains consent for the '
                                                           'procedure'],
                                               'answer': 'D) Witness signature, verify '
                                                         'understanding, and advocate if the '
                                                         'patient seems unclear—while the provider '
                                                         'obtains consent for the procedure',
                                               'explanation': 'The proceduralist discloses '
                                                              'risks/benefits/alternatives. Nurses '
                                                              'commonly witness, confirm '
                                                              'understanding, and stop the process '
                                                              'to seek clarification if '
                                                              'comprehension is lacking—not '
                                                              'replace the provider’s disclosure '
                                                              'role.',
                                               'choice_explanations': {'A': 'Nurse-led full risk '
                                                                            'disclosure as sole '
                                                                            'consenting act is a '
                                                                            'role near-miss.',
                                                                       'B': 'Forgery is fraud and '
                                                                            'assault risk.',
                                                                       'C': 'Unanswered questions '
                                                                            'invalidate meaningful '
                                                                            'consent.',
                                                                       'D': 'Witnessing, verifying '
                                                                            'understanding, and '
                                                                            'advocating for '
                                                                            'clarity match the '
                                                                            'nursing role.'}},
                                              {'question': 'Moral distress occurs when nurses '
                                                           'experience which situation?',
                                               'options': ['A) They know the ethically appropriate '
                                                           'action but institutional or other '
                                                           'barriers prevent taking it',
                                                           'B) They are uncertain which ethical '
                                                           'principle applies and need more '
                                                           'education before deciding',
                                                           'C) They always get what they want '
                                                           'administratively',
                                                           'D) They have unlimited resources and '
                                                           'no conflicting duties'],
                                               'answer': 'A) They know the ethically appropriate '
                                                         'action but institutional or other '
                                                         'barriers prevent taking it',
                                               'explanation': 'Moral distress arises when '
                                                              'clinicians know the right course '
                                                              'but constraints block action. Moral '
                                                              'uncertainty (not knowing what is '
                                                              'right) is related but distinct.',
                                               'choice_explanations': {'A': 'Knowing the right act '
                                                                            'yet being blocked '
                                                                            'defines moral '
                                                                            'distress.',
                                                                       'B': 'Moral uncertainty '
                                                                            'about which principle '
                                                                            'applies is the '
                                                                            'conceptual near-miss.',
                                                                       'C': 'Getting one’s way '
                                                                            'administratively is '
                                                                            'not moral distress.',
                                                                       'D': 'Unlimited resources '
                                                                            'without conflict do '
                                                                            'not produce distress '
                                                                            'of this type.'}}],
                                     'extreme': [{'question': 'You repeatedly report that a broken '
                                                              'bed-exit alarm contributed to '
                                                              'falls; leadership takes no action, '
                                                              'and another serious injury occurs. '
                                                              'A colleague warns that further '
                                                              'reporting will “hurt your career.” '
                                                              'What is the ethically grounded next '
                                                              'step theme?',
                                                  'options': ['A) Stay silent to protect '
                                                              'promotions',
                                                              'B) Escalate through '
                                                              'whistleblowing/higher reporting '
                                                              'channels as protected '
                                                              'patient-safety disclosure when '
                                                              'internal fixes fail',
                                                              'C) Alter charts to hide the falls',
                                                              'D) Keep documenting locally and '
                                                              'wait for the next committee cycle '
                                                              'before any external escalation'],
                                                  'answer': 'B) Escalate through '
                                                            'whistleblowing/higher reporting '
                                                            'channels as protected patient-safety '
                                                            'disclosure when internal fixes fail',
                                                  'explanation': 'Persistent uncorrected hazards '
                                                                 'after repeated reports may '
                                                                 'require protected '
                                                                 'escalation/whistleblowing. '
                                                                 'Endless local waiting while '
                                                                 'patients are injured is '
                                                                 'inadequate.',
                                                  'choice_explanations': {'A': 'Silence protects '
                                                                               'careers, not '
                                                                               'patients.',
                                                                          'B': 'Protected '
                                                                               'higher-channel '
                                                                               'escalation is '
                                                                               'appropriate after '
                                                                               'failed internal '
                                                                               'response.',
                                                                          'C': 'Chart alteration '
                                                                               'is fraudulent and '
                                                                               'unsafe.',
                                                                          'D': 'Committee-cycle '
                                                                               'waiting after '
                                                                               'repeated harm is a '
                                                                               'delay near-miss.'}},
                                                 {'question': 'A capacitated patient with a valid '
                                                              'DNR develops ventricular '
                                                              'fibrillation. A resident orders '
                                                              '“just this one shock for the '
                                                              'family.” The spouse is screaming to '
                                                              '“do everything.” What should you '
                                                              'do?',
                                                  'options': ['A) Hide the DNR form so nobody is '
                                                              'upset',
                                                              'B) Provide a brief shock now for '
                                                              'family coping, then reinstate the '
                                                              'DNR afterward',
                                                              'C) Uphold the valid DNR, '
                                                              'communicate clearly with the '
                                                              'team/family, and refuse '
                                                              'interventions the patient declined',
                                                              'D) Shock immediately because the '
                                                              'resident outranks the patient’s '
                                                              'written wishes'],
                                                  'answer': 'C) Uphold the valid DNR, communicate '
                                                            'clearly with the team/family, and '
                                                            'refuse interventions the patient '
                                                            'declined',
                                                  'explanation': 'A valid DNR reflects capacitated '
                                                                 'patient wishes and must be '
                                                                 'honored despite family distress '
                                                                 'or hierarchical pressure. “One '
                                                                 'shock for the family” violates '
                                                                 'the directive.',
                                                  'choice_explanations': {'A': 'Hiding the DNR is '
                                                                               'dishonest and '
                                                                               'unsafe.',
                                                                          'B': 'Temporary '
                                                                               'suspension “for '
                                                                               'the family” is a '
                                                                               'common ethical '
                                                                               'near-miss.',
                                                                          'C': 'Upholding the DNR '
                                                                               'with clear '
                                                                               'communication is '
                                                                               'required.',
                                                                          'D': 'Resident orders '
                                                                               'cannot override a '
                                                                               'valid DNR.'}},
                                                 {'question': 'A coworker posts a recognizable '
                                                              'photo of your confused patient on '
                                                              'social media “for education,” with '
                                                              'room number visible. The patient '
                                                              'did not consent. What is your '
                                                              'obligation?',
                                                  'options': ['A) Ask the coworker to delete the '
                                                              'post and consider the matter closed '
                                                              'without reporting',
                                                              'B) Like and repost to show unit '
                                                              'camaraderie',
                                                              'C) Ignore it because social media '
                                                              'is always allowed for PHI',
                                                              'D) Report the privacy breach per '
                                                              'policy, support mitigation, and do '
                                                              'not reshare the image'],
                                                  'answer': 'D) Report the privacy breach per '
                                                            'policy, support mitigation, and do '
                                                            'not reshare the image',
                                                  'explanation': 'Posting identifiable patient '
                                                                 'images without consent is a '
                                                                 'privacy breach. Reporting and '
                                                                 'mitigation are required; '
                                                                 'informal delete-only responses '
                                                                 'often fail institutional/legal '
                                                                 'obligations.',
                                                  'choice_explanations': {'A': 'Delete-without-reporting '
                                                                               'is a common '
                                                                               'incomplete '
                                                                               'near-miss.',
                                                                          'B': 'Reposting spreads '
                                                                               'the breach.',
                                                                          'C': 'Social media is '
                                                                               'not a permitted '
                                                                               'PHI channel '
                                                                               'without '
                                                                               'authorization.',
                                                                          'D': 'Reporting, '
                                                                               'mitigation, and '
                                                                               'not resharing meet '
                                                                               'privacy '
                                                                               'duties.'}}]},
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
                'questions': {'easy': [{'question': 'Which presentation is a common atypical sign '
                                                    'of infection in older adults?',
                                        'options': ['A) High spiking fever in every infection '
                                                    'without exception',
                                                    'B) New or worsening confusion/falls with or '
                                                    'without fever',
                                                    'C) Guaranteed leukocytosis above 20,000 in '
                                                    'all cases',
                                                    'D) Low-grade temperature elevation with clear '
                                                    'localizing symptoms in every case'],
                                        'answer': 'B) New or worsening confusion/falls with or '
                                                  'without fever',
                                        'explanation': 'Older adults often present with delirium, '
                                                       'falls, or functional decline rather than '
                                                       'classic fever and localizing signs. Normal '
                                                       'or minimal temperature does not rule out '
                                                       'serious infection.',
                                        'choice_explanations': {'A': 'Fever may be blunted or '
                                                                     'absent in elders.',
                                                                'B': 'Acute confusion/falls are '
                                                                     'classic atypical infection '
                                                                     'cues.',
                                                                'C': 'Leukocytosis is not '
                                                                     'guaranteed; immunosenescence '
                                                                     'blunts responses.',
                                                                'D': 'Expecting even low-grade '
                                                                     'fever plus localizing signs '
                                                                     'misses afebrile '
                                                                     'presentations—assessment '
                                                                     'near-miss.'}},
                                       {'question': 'Polypharmacy in geriatrics most increases '
                                                    'which risk?',
                                        'options': ['A) Complete immunity to adverse drug events',
                                                    'B) Milder adverse effects because older '
                                                    'adults have slower metabolism of all drugs',
                                                    'C) Drug interactions, falls, cognitive '
                                                    'impairment, and adherence problems',
                                                    'D) Improved adherence automatically with more '
                                                    'pills'],
                                        'answer': 'C) Drug interactions, falls, cognitive '
                                                  'impairment, and adherence problems',
                                        'explanation': 'Multiple medications raise interaction, '
                                                       'fall, delirium, and nonadherence risks. '
                                                       'Slower metabolism can increase—not '
                                                       'decrease—adverse-effect risk.',
                                        'choice_explanations': {'A': 'ADE risk rises with regimen '
                                                                     'complexity.',
                                                                'B': 'Assuming milder ADEs from '
                                                                     'slower metabolism is a '
                                                                     'pharmacokinetics near-miss.',
                                                                'C': 'Interactions, falls, '
                                                                     'cognition, and adherence '
                                                                     'harms define polypharmacy '
                                                                     'risk.',
                                                                'D': 'More pills often worsen '
                                                                     'adherence.'}},
                                       {'question': 'Which nursing actions help prevent pressure '
                                                    'injuries in immobile older adults?',
                                        'options': ['A) Massage reddened areas gently and keep HOB '
                                                    'high to improve comfort and skin blood flow',
                                                    'B) Use a donut ring pillow under the sacrum '
                                                    'at all times',
                                                    'C) Keep the head of bed at 90° continuously '
                                                    'without shifts',
                                                    'D) Reposition regularly, optimize '
                                                    'nutrition/moisture, and use '
                                                    'pressure-redistributing surfaces'],
                                        'answer': 'D) Reposition regularly, optimize '
                                                  'nutrition/moisture, and use '
                                                  'pressure-redistributing surfaces',
                                        'explanation': 'Pressure-injury prevention combines '
                                                       'turning schedules, skin moisture '
                                                       'management, nutrition, and support '
                                                       'surfaces. Massaging damaged tissue and '
                                                       'constant high Fowler’s without offloading '
                                                       'increase injury risk.',
                                        'choice_explanations': {'A': 'Massage plus high HOB is '
                                                                     'outdated/harmful “skin care” '
                                                                     'near-miss.',
                                                                'B': 'Donut rings focus pressure '
                                                                     'at edges and are '
                                                                     'discouraged.',
                                                                'C': 'Constant high Fowler’s '
                                                                     'increases shear/pressure on '
                                                                     'the sacrum.',
                                                                'D': 'Repositioning, '
                                                                     'nutrition/moisture care, and '
                                                                     'support surfaces are '
                                                                     'prevention pillars.'}}],
                              'medium': [{'question': 'What do the Beers Criteria help clinicians '
                                                      'evaluate in older adults?',
                                          'options': ['A) Potentially inappropriate medications '
                                                      'that carry heightened risk in the elderly',
                                                      'B) Drug–drug interactions only, without '
                                                      'considering age-related adverse-effect risk '
                                                      'of single agents',
                                                      'C) Exact shoe sizes for fall mats',
                                                      'D) Only surgical instrument sterilization '
                                                      'methods'],
                                          'answer': 'A) Potentially inappropriate medications that '
                                                    'carry heightened risk in the elderly',
                                          'explanation': 'Beers Criteria list medications that are '
                                                         'potentially inappropriate in older '
                                                         'adults due to adverse-effect profiles. '
                                                         'Interaction checking is related '
                                                         'medication safety but is not what Beers '
                                                         'primarily catalogs.',
                                          'choice_explanations': {'A': 'Identifying high-risk/PIM '
                                                                       'drugs in elders is the '
                                                                       'Beers purpose.',
                                                                  'B': 'Interaction-only framing '
                                                                       'is a medication-safety '
                                                                       'near-miss for Beers.',
                                                                  'C': 'Shoe size is unrelated.',
                                                                  'D': 'Sterilization is an '
                                                                       'infection-control '
                                                                       'domain.'}},
                                         {'question': 'When helping an older adult with '
                                                      'orthostatic hypotension stand, which '
                                                      'nursing tip is best?',
                                          'options': ['A) Stand abruptly from supine in one second',
                                                      'B) Dangle at the bedside, rise slowly, and '
                                                      'wait for dizziness to resolve before '
                                                      'walking',
                                                      'C) Encourage hot baths immediately before '
                                                      'standing',
                                                      'D) Apply compression stockings and stand '
                                                      'promptly so blood pressure adapts faster'],
                                          'answer': 'B) Dangle at the bedside, rise slowly, and '
                                                    'wait for dizziness to resolve before walking',
                                          'explanation': 'Orthostatic precautions use staged '
                                                         'position changes to allow baroreceptor '
                                                         'compensation. Stockings may help select '
                                                         'patients but do not justify abrupt '
                                                         'standing.',
                                          'choice_explanations': {'A': 'Abrupt standing '
                                                                       'precipitates orthostatic '
                                                                       'syncope.',
                                                                  'B': 'Slow staged rising is the '
                                                                       'correct orthostatic '
                                                                       'technique.',
                                                                  'C': 'Heat causes vasodilation '
                                                                       'that worsens hypotension.',
                                                                  'D': 'Stockings plus prompt '
                                                                       'standing mixes a helpful '
                                                                       'adjunct with unsafe '
                                                                       'timing—near-miss.'}},
                                         {'question': 'Which feature best helps distinguish '
                                                      'delirium from dementia at the bedside?',
                                          'options': ['A) They are identical terms with no '
                                                      'clinical difference',
                                                      'B) Delirium is simply worsening dementia, '
                                                      'so the workup can focus on redirection '
                                                      'techniques alone',
                                                      'C) Delirium is acute/fluctuating and often '
                                                      'reversible with treatable causes; dementia '
                                                      'is acquired progressive cognitive decline',
                                                      'D) Delirium is always chronic over years '
                                                      'without fluctuation'],
                                          'answer': 'C) Delirium is acute/fluctuating and often '
                                                    'reversible with treatable causes; dementia is '
                                                    'acquired progressive cognitive decline',
                                          'explanation': 'Delirium is an acute, fluctuating '
                                                         'attention/awareness disturbance often '
                                                         'due to infection, meds, or metabolic '
                                                         'insult—and potentially reversible. '
                                                         'Dementia is a chronic progressive '
                                                         'decline. Mislabeling delirium as '
                                                         'dementia delays urgent evaluation.',
                                          'choice_explanations': {'A': 'The distinction drives '
                                                                       'urgent medical evaluation.',
                                                                  'B': 'Treating delirium as '
                                                                       'dementia progression only '
                                                                       'is a high-stakes '
                                                                       'assessment near-miss.',
                                                                  'C': 'Acute fluctuating vs '
                                                                       'chronic progressive is the '
                                                                       'key distinction.',
                                                                  'D': 'Chronic nonfluctuating '
                                                                       'course describes dementia '
                                                                       'more than delirium.'}}],
                              'hard': [{'question': 'If a nurse suspects elder abuse in a '
                                                    'long-term care resident, what is the duty?',
                                        'options': ['A) Gather more collateral history and '
                                                    'photographs over several shifts before '
                                                    'involving outsiders',
                                                    'B) Keep it private to protect the facility’s '
                                                    'reputation',
                                                    'C) Confront the suspected abuser alone in a '
                                                    'secluded area without a plan',
                                                    'D) Ensure safety and report per mandatory '
                                                    'elder-abuse reporting laws'],
                                        'answer': 'D) Ensure safety and report per mandatory '
                                                  'elder-abuse reporting laws',
                                        'explanation': 'Nurses are mandatory reporters of '
                                                       'suspected elder abuse. Reasonable '
                                                       'suspicion triggers reporting and '
                                                       'protective action; delaying for perfect '
                                                       'documentation endangers the elder.',
                                        'choice_explanations': {'A': 'Extended private '
                                                                     'evidence-gathering before '
                                                                     'reporting is a protection '
                                                                     'near-miss.',
                                                                'B': 'Reputation does not override '
                                                                     'mandated reporting.',
                                                                'C': 'Lone confrontation can '
                                                                     'escalate danger and spoil '
                                                                     'investigations.',
                                                                'D': 'Safety plus mandatory '
                                                                     'reporting is the required '
                                                                     'response.'}},
                                       {'question': 'For an older adult with dementia who wanders, '
                                                    'which approach is a preferred restraint '
                                                    'alternative?',
                                        'options': ['A) Supervised ambulation, door alarms, '
                                                    'meaningful activities, and environmental '
                                                    'modification before restraints',
                                                    'B) Move the resident nearer the nurses’ '
                                                    'station and use PRN sedation if wandering '
                                                    'continues after dark',
                                                    'C) Immediate four-point leather restraints on '
                                                    'admission',
                                                    'D) Locking the person in a dark closet'],
                                        'answer': 'A) Supervised ambulation, door alarms, '
                                                  'meaningful activities, and environmental '
                                                  'modification before restraints',
                                        'explanation': 'Least-restrictive dementia care uses '
                                                       'supervision, alarms, activities, and '
                                                       'environment before restraints. Early '
                                                       'chemical restraint for wandering is not '
                                                       'first-line.',
                                        'choice_explanations': {'A': 'Nonpharmacologic, '
                                                                     'least-restrictive strategies '
                                                                     'are preferred wander '
                                                                     'management.',
                                                                'B': 'Station proximity plus PRN '
                                                                     'sedation mixes a good '
                                                                     'environmental idea with '
                                                                     'chemical restraint '
                                                                     'near-miss.',
                                                                'C': 'Restraints are last resort '
                                                                     'with strict criteria, not '
                                                                     'admission defaults.',
                                                                'D': 'Confinement in a closet is '
                                                                     'abusive and illegal.'}},
                                       {'question': 'Why do nurses emphasize daily weights in '
                                                    'older adults with heart failure?',
                                        'options': ['A) Weights detect muscle hypertrophy '
                                                    'overnight from exercise',
                                                    'B) Sudden gains often signal fluid retention '
                                                    'needing early intervention before frank '
                                                    'decompensation',
                                                    'C) Daily weights replace the need for any '
                                                    'symptom assessment',
                                                    'D) Daily weights mainly verify nutritional '
                                                    'status, so small gains can wait until the '
                                                    'weekly clinic visit'],
                                        'answer': 'B) Sudden gains often signal fluid retention '
                                                  'needing early intervention before frank '
                                                  'decompensation',
                                        'explanation': 'Rapid weight gain is an early congestion '
                                                       'marker in HF, prompting diet/diuretic '
                                                       'reassessment. Interpreting gains only as '
                                                       'nutrition delays congestion care.',
                                        'choice_explanations': {'A': 'Overnight kilogram gains are '
                                                                     'fluid, not muscle.',
                                                                'B': 'Early fluid detection '
                                                                     'enables intervention before '
                                                                     'hospitalization.',
                                                                'C': 'Symptoms and exam remain '
                                                                     'essential alongside weights.',
                                                                'D': 'Nutrition-only '
                                                                     'interpretation of daily '
                                                                     'weights is an assessment '
                                                                     'near-miss in HF.'}}],
                              'extreme': [{'question': 'An 88-year-old with osteoporosis is found '
                                                       'on the floor after a fall, reporting '
                                                       'severe hip pain and external rotation of '
                                                       'the leg. She is on anticoagulants; BP is '
                                                       '88/50; and a family member demands she '
                                                       'stand to “walk it off” before imaging. '
                                                       'What is the priority?',
                                           'options': ['A) Give a NSAID cocktail and discharge '
                                                       'home immediately',
                                                       'B) Log-roll carefully onto a chair for '
                                                       'comfort while awaiting X-ray if BP is near '
                                                       'baseline',
                                                       'C) Immobilize/support the limb, treat '
                                                       'shock, hold unsafe movement, escalate for '
                                                       'fracture/bleeding evaluation',
                                                       'D) Force ambulation to prevent stiffness'],
                                           'answer': 'C) Immobilize/support the limb, treat shock, '
                                                     'hold unsafe movement, escalate for '
                                                     'fracture/bleeding evaluation',
                                           'explanation': 'Hip fracture signs with anticoagulant '
                                                          'use and hypotension suggest fracture '
                                                          'plus bleeding/shock risk. Immobilize, '
                                                          'support circulation, and escalate—do '
                                                          'not mobilize for comfort.',
                                           'choice_explanations': {'A': 'NSAID discharge ignores '
                                                                        'fracture, shock, and '
                                                                        'bleed risk.',
                                                                   'B': 'Early chair transfer for '
                                                                        'comfort is a mobility '
                                                                        'near-miss with '
                                                                        'fracture/shock.',
                                                                   'C': 'Immobilization, shock '
                                                                        'care, and urgent '
                                                                        'escalation protect life '
                                                                        'and limb.',
                                                                   'D': 'Forcing ambulation can '
                                                                        'worsen fracture '
                                                                        'displacement and '
                                                                        'bleeding.'}},
                                          {'question': 'A frail nursing-home resident develops new '
                                                       'lethargy, anorexia, and falls without '
                                                       'fever. Urine is foul; BP drops to 80/40; '
                                                       'lactate is rising. Staff say “old people '
                                                       'get confused—just watch.” What should you '
                                                       'do?',
                                           'options': ['A) Treat presumed UTI with oral '
                                                       'antibiotics on the unit while monitoring '
                                                       'for fever before escalating',
                                                       'B) Agree and defer vitals until tomorrow',
                                                       'C) Encourage vigorous exercise testing now',
                                                       'D) Recognize possible sepsis with atypical '
                                                       'signs, support ABCs, obtain cultures/labs '
                                                       'per protocol, and escalate urgently'],
                                           'answer': 'D) Recognize possible sepsis with atypical '
                                                     'signs, support ABCs, obtain cultures/labs '
                                                     'per protocol, and escalate urgently',
                                           'explanation': 'New lethargy, anorexia, falls, foul '
                                                          'urine, hypotension, and rising lactate '
                                                          'suggest sepsis with atypical geriatric '
                                                          'onset. ABC support and urgent '
                                                          'escalation outrank watchful oral '
                                                          'treatment alone.',
                                           'choice_explanations': {'A': 'Unit oral UTI treatment '
                                                                        'while awaiting fever is a '
                                                                        'dangerous under-triage '
                                                                        'near-miss when shock cues '
                                                                        'exist.',
                                                                   'B': 'Deferring vitals ignores '
                                                                        'evolving shock.',
                                                                   'C': 'Exercise testing is '
                                                                        'contraindicated in '
                                                                        'hypotensive sepsis.',
                                                                   'D': 'Atypical sepsis '
                                                                        'recognition with ABC '
                                                                        'support and urgent '
                                                                        'escalation is required.'}},
                                          {'question': 'At end of life, a capacitated older '
                                                       'adult’s advance directive declines '
                                                       'intubation. The adult child demands “full '
                                                       'code for guilt reasons,” and a covering '
                                                       'resident writes intubation orders. The '
                                                       'patient remains alert and refuses. What is '
                                                       'the correct nursing action?',
                                           'options': ['A) Uphold the patient’s directive and '
                                                       'current refusal; escalate to '
                                                       'attending/ethics/chain of command as '
                                                       'needed',
                                                       'B) Facilitate a family meeting first and '
                                                       'follow the child’s preference if the '
                                                       'meeting runs long near arrest',
                                                       'C) Hide the advance directive and proceed '
                                                       'to intubation',
                                                       'D) Tell the patient autonomy no longer '
                                                       'applies after age 80'],
                                           'answer': 'A) Uphold the patient’s directive and '
                                                     'current refusal; escalate to '
                                                     'attending/ethics/chain of command as needed',
                                           'explanation': 'Capacitated patient directives and '
                                                          'current refusals outrank family '
                                                          'guilt-driven demands. Escalate '
                                                          'conflicts; do not intubate against '
                                                          'valid wishes while “waiting out” a '
                                                          'meeting.',
                                           'choice_explanations': {'A': 'Upholding the directive '
                                                                        'with appropriate '
                                                                        'escalation is required.',
                                                                   'B': 'Family-meeting delay that '
                                                                        'defaults to the child’s '
                                                                        'wishes is an ethics '
                                                                        'near-miss.',
                                                                   'C': 'Hiding the directive is '
                                                                        'fraudulent.',
                                                                   'D': 'Age does not erase '
                                                                        'autonomy.'}}]},
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



# Load expanded MCQ banks (100 unique questions per specialty) when available.
from pathlib import Path as _BankPath
import importlib.util as _ilu

def _load_apply_question_banks():
    for candidate in (
        _BankPath(__file__).resolve().parent / "bank_loader.py",
        _BankPath(__file__).resolve().parent.parent / "bank_loader.py",
    ):
        if candidate.exists():
            spec = _ilu.spec_from_file_location("_charanas_bank_loader", candidate)
            mod = _ilu.module_from_spec(spec)
            assert spec.loader is not None
            spec.loader.exec_module(mod)
            return mod.apply_question_banks
    raise ImportError("bank_loader.py not found")

_apply_question_banks = _load_apply_question_banks()
_apply_question_banks(SPECIALTIES, _BankPath(__file__).resolve().parent / "question_banks")


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
