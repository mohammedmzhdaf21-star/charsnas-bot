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
                                          'options': ['A) Daily weight, intake/output, and bowel '
                                                      'pattern only',
                                                      'B) Temperature, pulse, respiration, blood '
                                                      'pressure (± SpO2/pain)',
                                                      'C) Continuous ECG monitoring without other '
                                                      'bedside measures',
                                                      'D) Pupil size and Glasgow Coma Scale alone'],
                                          'answer': 'B) Temperature, pulse, respiration, blood '
                                                    'pressure (± SpO2/pain)',
                                          'explanation': 'Vital signs index thermoregulation, '
                                                         'cardiac output, ventilation, and '
                                                         'vascular tone. Temperature, pulse, '
                                                         'respiration, and blood pressure—often '
                                                         'with SpO2 and pain—form the baseline '
                                                         'nurses use to detect deterioration; '
                                                         'trends matter more than single values '
                                                         'because compensation can mask illness.',
                                          'choice_explanations': {'A': 'Weight and I&O inform '
                                                                       'fluid balance but do not '
                                                                       'measure thermoregulation, '
                                                                       'cardiac output, '
                                                                       'ventilation, or vascular '
                                                                       'tone that define classic '
                                                                       'vital signs.',
                                                                  'B': 'Temperature, pulse, '
                                                                       'respiration, and blood '
                                                                       'pressure (± SpO2/pain) '
                                                                       'directly reflect the core '
                                                                       'physiologic signals nurses '
                                                                       'trend for early '
                                                                       'deterioration.',
                                                                  'C': 'ECG tracks rhythm and rate '
                                                                       'but does not replace '
                                                                       'temperature, '
                                                                       'blood-pressure, or '
                                                                       'respiratory assessment as '
                                                                       'the standard vital-sign '
                                                                       'set.',
                                                                  'D': 'Pupils and GCS assess '
                                                                       'neurologic status; they '
                                                                       'complement but do not '
                                                                       'substitute for '
                                                                       'cardiopulmonary and '
                                                                       'thermoregulatory vital '
                                                                       'signs.'}},
                                         {'question': 'Why is hand hygiene considered the '
                                                      'highest-yield routine infection-control '
                                                      'practice in direct patient care?',
                                          'options': ['A) It replaces sterile technique for all '
                                                      'invasive procedures',
                                                      'B) It eliminates any need for gloves during '
                                                      'wound care',
                                                      'C) It reduces transient flora that drives '
                                                      'cross-transmission',
                                                      'D) It is required only during discharge '
                                                      'teaching sessions'],
                                          'answer': 'C) It reduces transient flora that drives '
                                                    'cross-transmission',
                                          'explanation': 'Transient microorganisms on hands are a '
                                                         'major vehicle for healthcare-associated '
                                                         'infection. Hand hygiene mechanically and '
                                                         'chemically lowers microbial load before '
                                                         'and after contact, interrupting '
                                                         'cross-transmission. Gloves are an '
                                                         'adjunct, not a substitute, because hands '
                                                         'and glove surfaces still become '
                                                         'contaminated.',
                                          'choice_explanations': {'A': 'Sterile technique protects '
                                                                       'invasive fields; hand '
                                                                       'hygiene reduces hand flora '
                                                                       'but does not replace '
                                                                       'asepsis for sterile '
                                                                       'procedures.',
                                                                  'B': 'Gloves are barriers during '
                                                                       'wound care, yet '
                                                                       'contamination still '
                                                                       'occurs; hygiene is '
                                                                       'required before donning '
                                                                       'and after removing gloves.',
                                                                  'C': 'Reducing transient hand '
                                                                       'flora interrupts the most '
                                                                       'common pathway of '
                                                                       'contact-mediated pathogen '
                                                                       'transfer between patients '
                                                                       'and surfaces.',
                                                                  'D': 'Transmission risk exists '
                                                                       'throughout care '
                                                                       'encounters, not only at '
                                                                       'discharge; limiting '
                                                                       'hygiene to teaching leaves '
                                                                       'ongoing contact risk '
                                                                       'unaddressed.'}},
                                         {'question': 'Which elements are required for valid '
                                                      'informed consent before an invasive '
                                                      'procedure?',
                                          'options': ['A) Nurse signature alone without explaining '
                                                      'the procedure to the patient',
                                                      'B) Family agreement even when a capacitated '
                                                      'patient refuses',
                                                      'C) Verbal assent without documenting risks '
                                                      'or alternatives',
                                                      'D) Understanding of procedure, risks, '
                                                      'alternatives, and voluntary agreement'],
                                          'answer': 'D) Understanding of procedure, risks, '
                                                    'alternatives, and voluntary agreement',
                                          'explanation': 'Informed consent requires that a '
                                                         'capacitated patient understand the '
                                                         'nature of the procedure, material risks '
                                                         'and benefits, and reasonable '
                                                         'alternatives, then agree voluntarily '
                                                         'without coercion. The proceduralist '
                                                         'obtains consent; the nurse verifies '
                                                         'understanding, witnesses, and advocates '
                                                         'if doubts arise.',
                                          'choice_explanations': {'A': 'A signature without '
                                                                       'disclosure does not '
                                                                       'demonstrate understanding '
                                                                       'of risks, benefits, or '
                                                                       'alternatives.',
                                                                  'B': 'A capacitated adult’s '
                                                                       'refusal overrides family '
                                                                       'preference; autonomy is '
                                                                       'not transferred to '
                                                                       'relatives by default.',
                                                                  'C': 'Undocumented verbal assent '
                                                                       'fails to show that '
                                                                       'material risks and '
                                                                       'alternatives were '
                                                                       'discussed and understood.',
                                                                  'D': 'Understanding plus '
                                                                       'voluntary agreement after '
                                                                       'disclosure of procedure, '
                                                                       'risks, and alternatives '
                                                                       'defines valid informed '
                                                                       'consent.'}}],
                                'medium': [{'question': 'About 20 minutes after an IV opioid, the '
                                                        'patient rates pain 8/10 and is newly '
                                                        'drowsy with RR 9. What is the best '
                                                        'immediate nursing judgment?',
                                            'options': ['A) Hold further opioid, stimulate '
                                                        'respiration, assess sedation/SpO2, and '
                                                        'notify the provider',
                                                        'B) Give the next scheduled opioid dose '
                                                        'early because pain remains high',
                                                        'C) Document the score only and reassess '
                                                        'at the next routine vital-sign time',
                                                        'D) Apply a heating pad as the sole '
                                                        'intervention without respiratory '
                                                        'assessment'],
                                            'answer': 'A) Hold further opioid, stimulate '
                                                      'respiration, assess sedation/SpO2, and '
                                                      'notify the provider',
                                            'explanation': 'High pain with new opioid-related '
                                                           'sedation and hypoventilation signals '
                                                           'analgesic effect overlapping with '
                                                           'respiratory depression. The priority '
                                                           'is to protect ventilation—stimulate, '
                                                           'support airway/oxygenation as needed, '
                                                           'withhold further opioid, and '
                                                           'escalate—rather than escalating '
                                                           'analgesia blindly.',
                                            'choice_explanations': {'A': 'Holding opioid while '
                                                                         'assessing '
                                                                         'sedation/ventilation and '
                                                                         'notifying the provider '
                                                                         'addresses both pain '
                                                                         'context and '
                                                                         'life-threatening '
                                                                         'respiratory depression.',
                                                                    'B': 'Giving more opioid when '
                                                                         'RR is already 9 can '
                                                                         'deepen hypoventilation '
                                                                         'and precipitate arrest.',
                                                                    'C': 'Waiting for routine '
                                                                         'vitals delays '
                                                                         'recognition of '
                                                                         'progressive respiratory '
                                                                         'depression after a '
                                                                         'recent IV opioid.',
                                                                    'D': 'A heating pad does not '
                                                                         'reverse opioid-mediated '
                                                                         'respiratory depression '
                                                                         'and skips mandatory '
                                                                         'airway assessment.'}},
                                           {'question': 'An ambulatory older adult scores high on '
                                                        'fall risk and needs to toilet at night. '
                                                        'Which intervention best applies '
                                                        'fall-prevention principles?',
                                            'options': ['A) Keep all side rails up and lights off '
                                                        'to encourage sleep',
                                                        'B) Place the call light in reach, use '
                                                        'nonslip footwear, and clear the path to a '
                                                        'nearby toilet',
                                                        'C) Withhold diuretics indefinitely so '
                                                        'nighttime toileting never occurs',
                                                        'D) Restrain the patient in a chair '
                                                        'whenever staff are busy'],
                                            'answer': 'B) Place the call light in reach, use '
                                                      'nonslip footwear, and clear the path to a '
                                                      'nearby toilet',
                                            'explanation': 'Fall prevention targets modifiable '
                                                           'hazards: ensure the patient can call '
                                                           'for help, wear stable footwear, and '
                                                           'navigate a clear, lighted path. '
                                                           'Restraints and darkness increase '
                                                           'injury risk; medication changes '
                                                           'require orders and clinical judgment, '
                                                           'not unilateral indefinite withholding.',
                                            'choice_explanations': {'A': 'Full side rails and '
                                                                         'darkness increase '
                                                                         'entrapment and fall '
                                                                         'injury risk rather than '
                                                                         'preventing falls.',
                                                                    'B': 'Call access, nonslip '
                                                                         'footwear, and a clear '
                                                                         'toileting path reduce '
                                                                         'environmental and '
                                                                         'assistance-related fall '
                                                                         'risk.',
                                                                    'C': 'Stopping diuretics '
                                                                         'without an order can '
                                                                         'worsen heart failure or '
                                                                         'hypertension and is not '
                                                                         'a first-line fall '
                                                                         'intervention.',
                                                                    'D': 'Restraints are a last '
                                                                         'resort with specific '
                                                                         'orders; they increase '
                                                                         'agitation and injury '
                                                                         'risk when used for '
                                                                         'staffing convenience.'}},
                                           {'question': 'You enter a room to draw blood on a '
                                                        'patient with unknown infection status. '
                                                        'Which statement correctly applies '
                                                        'standard precautions?',
                                            'options': ['A) Standard precautions are used only '
                                                        'after culture results confirm a pathogen',
                                                        'B) Gowns and N95s are required for every '
                                                        'blood draw regardless of splash risk',
                                                        'C) Assume all blood and body fluids are '
                                                        'potentially infectious and use '
                                                        'appropriate barriers',
                                                        'D) Hand hygiene is unnecessary if gloves '
                                                        'will be worn for the entire procedure'],
                                            'answer': 'C) Assume all blood and body fluids are '
                                                      'potentially infectious and use appropriate '
                                                      'barriers',
                                            'explanation': 'Standard precautions treat all blood '
                                                           'and body fluids as potentially '
                                                           'infectious. Barrier selection is based '
                                                           'on anticipated exposure; gloves plus '
                                                           'hand hygiene are baseline for '
                                                           'phlebotomy, with face/eye protection '
                                                           'if splash is likely. Waiting for '
                                                           'cultures leaves staff unprotected '
                                                           'during the highest-risk period.',
                                            'choice_explanations': {'A': 'Transmission risk exists '
                                                                         'before cultures return; '
                                                                         'standard precautions '
                                                                         'apply to all patients.',
                                                                    'B': 'N95s are for airborne '
                                                                         'risks; routine '
                                                                         'phlebotomy needs gloves '
                                                                         'and splash protection '
                                                                         'only when indicated.',
                                                                    'C': 'Treating all blood/body '
                                                                         'fluids as infectious and '
                                                                         'matching barriers to '
                                                                         'exposure is the '
                                                                         'definition of standard '
                                                                         'precautions.',
                                                                    'D': 'Gloves do not replace '
                                                                         'hand hygiene; hands are '
                                                                         'contaminated during '
                                                                         'glove removal and '
                                                                         'between tasks.'}}],
                                'hard': [{'question': 'You are caring for four patients: one with '
                                                      'new stridor after IV contrast, one '
                                                      'requesting PRN oral analgesic, one due for '
                                                      'routine dressing change, and one asking for '
                                                      'water. Using priority frameworks, which '
                                                      'patient do you assess first?',
                                          'options': ['A) The patient requesting water to prevent '
                                                      'dehydration',
                                                      'B) The patient due for a scheduled dressing '
                                                      'change',
                                                      'C) The patient requesting PRN oral pain '
                                                      'medication',
                                                      'D) The patient with new stridor after IV '
                                                      'contrast'],
                                          'answer': 'D) The patient with new stridor after IV '
                                                    'contrast',
                                          'explanation': 'Airway compromise after contrast '
                                                         'suggests evolving anaphylaxis or airway '
                                                         'edema and outranks comfort and routine '
                                                         'tasks. ABC and acute physiologic threat '
                                                         'determine priority; analgesia, '
                                                         'hydration, and dressings are important '
                                                         'but deferrable when an airway emergency '
                                                         'is unfolding.',
                                          'choice_explanations': {'A': 'Thirst is a '
                                                                       'comfort/hydration need and '
                                                                       'does not outrank acute '
                                                                       'airway threat.',
                                                                  'B': 'A routine dressing change '
                                                                       'is time-sensitive for '
                                                                       'wound care but not '
                                                                       'immediately '
                                                                       'life-threatening.',
                                                                  'C': 'Pain requires timely '
                                                                       'treatment yet is lower '
                                                                       'priority than new stridor '
                                                                       'indicating airway risk.',
                                                                  'D': 'New stridor after contrast '
                                                                       'signals possible airway '
                                                                       'edema/anaphylaxis—the '
                                                                       'highest ABC priority.'}},
                                         {'question': 'A confused patient repeatedly tries to pull '
                                                      'a central line. Soft wrist restraints are '
                                                      'ordered. Which nursing action is required '
                                                      'for safe, lawful restraint use?',
                                          'options': ['A) Apply restraints, then assess '
                                                      'circulation, sensation, and need for '
                                                      'release at required intervals; attempt '
                                                      'least-restrictive alternatives',
                                                      'B) Tie restraints to the side rails tightly '
                                                      'so the patient cannot move either arm at '
                                                      'all',
                                                      'C) Leave restraints on continuously without '
                                                      'documentation until discharge',
                                                      'D) Have family apply restraints whenever '
                                                      'staff leave the room'],
                                          'answer': 'A) Apply restraints, then assess circulation, '
                                                    'sensation, and need for release at required '
                                                    'intervals; attempt least-restrictive '
                                                    'alternatives',
                                          'explanation': 'Restraints require an order, '
                                                         'least-restrictive alternatives first, '
                                                         'correct application, and frequent '
                                                         'circulatory/skin/behavioral reassessment '
                                                         'with timed release opportunities. '
                                                         'Securing to rails, continuous '
                                                         'unmonitored use, and delegating '
                                                         'application to family violate safety and '
                                                         'regulatory standards.',
                                          'choice_explanations': {'A': 'Interval neurovascular '
                                                                       'checks, release trials, '
                                                                       'and least-restrictive '
                                                                       'alternatives are mandatory '
                                                                       'for safe restraint use.',
                                                                  'B': 'Tight immobilization to '
                                                                       'side rails risks '
                                                                       'neurovascular injury and '
                                                                       'is improper restraint '
                                                                       'technique.',
                                                                  'C': 'Continuous use without '
                                                                       'reassessment and '
                                                                       'documentation violates '
                                                                       'restraint standards of '
                                                                       'care.',
                                                                  'D': 'Restraint application and '
                                                                       'monitoring are nursing '
                                                                       'responsibilities and '
                                                                       'cannot be handed to '
                                                                       'family.'}},
                                         {'question': 'Two patients share a room. You bring oral '
                                                      'digoxin for Bed A, but the roommate answers '
                                                      'to the name when you call it from the '
                                                      'doorway. Which action best prevents a '
                                                      'wrong-patient medication error?',
                                          'options': ['A) Give the dose because the roommate '
                                                      'seemed to recognize the name',
                                                      'B) Verify two unique identifiers at the '
                                                      'bedside with the labeled medication against '
                                                      'the MAR before administering',
                                                      'C) Ask which bed usually gets digoxin and '
                                                      'administer based on bed location',
                                                      'D) Leave the cup on the overbed table and '
                                                      'ask whoever needs digoxin to take it'],
                                          'answer': 'B) Verify two unique identifiers at the '
                                                    'bedside with the labeled medication against '
                                                    'the MAR before administering',
                                          'explanation': 'Wrong-patient errors occur when identity '
                                                         'is not verified at the point of '
                                                         'administration. Two unique identifiers '
                                                         '(e.g., name and DOB/MRN) must match the '
                                                         'MAR and labeled drug at the bedside. '
                                                         'Room/bed location and doorway name '
                                                         'checks are unreliable when patients '
                                                         'share spaces or have similar names.',
                                          'choice_explanations': {'A': 'A verbal response from the '
                                                                       'wrong person in a shared '
                                                                       'room is a classic '
                                                                       'near-miss pathway for '
                                                                       'wrong-patient dosing.',
                                                                  'B': 'Bedside dual-identifier '
                                                                       'check against the MAR '
                                                                       'links the ordered digoxin '
                                                                       'to the intended recipient '
                                                                       'before the dose is given.',
                                                                  'C': 'Bed location is not a '
                                                                       'unique identifier and '
                                                                       'changes with transfers, so '
                                                                       'it cannot prevent '
                                                                       'wrong-patient errors.',
                                                                  'D': 'Unattended medication cups '
                                                                       'allow self-administration '
                                                                       'by the wrong patient and '
                                                                       'lose chain-of-custody '
                                                                       'control.'}}],
                                'extreme': [{'question': 'You find an unresponsive adult on the '
                                                         'floor with no palpable pulse and agonal '
                                                         'gasps. A visitor insists you wait for '
                                                         'the family to consent before touching '
                                                         'the patient. The charge nurse is on '
                                                         'another unit, and the paper code status '
                                                         'sheet is not in the binder. What is the '
                                                         'immediate priority action?',
                                             'options': ['A) Leave to retrieve the paper chart and '
                                                         'confirm code status before any '
                                                         'compressions',
                                                         'B) Document a full narrative note, then '
                                                         'return to begin CPR',
                                                         'C) Start high-quality CPR and activate '
                                                         'the emergency response per protocol '
                                                         'while code status is clarified in '
                                                         'parallel',
                                                         'D) Obtain written family consent before '
                                                         'initiating compressions'],
                                             'answer': 'C) Start high-quality CPR and activate the '
                                                       'emergency response per protocol while code '
                                                       'status is clarified in parallel',
                                             'explanation': 'Pulseless unresponsiveness with '
                                                            'agonal breathing indicates '
                                                            'circulatory arrest. Unless a valid '
                                                            'DNR is known and verified, immediate '
                                                            'CPR and emergency activation are '
                                                            'required; ischemic time drives '
                                                            'neurologic outcome. Chart retrieval, '
                                                            'documentation, and consent delays are '
                                                            'inappropriate when arrest is '
                                                            'witnessed and code status is unknown.',
                                             'choice_explanations': {'A': 'Leaving a pulseless '
                                                                          'patient to find '
                                                                          'paperwork abandons '
                                                                          'circulation support '
                                                                          'during the most '
                                                                          'time-critical minutes.',
                                                                     'B': 'Documentation cannot '
                                                                          'restore coronary or '
                                                                          'cerebral perfusion and '
                                                                          'must not precede CPR.',
                                                                     'C': 'Starting CPR and '
                                                                          'activating the '
                                                                          'emergency team '
                                                                          'immediately maximizes '
                                                                          'perfusion while code '
                                                                          'status is rapidly '
                                                                          'clarified.',
                                                                     'D': 'Implied consent for '
                                                                          'emergency resuscitation '
                                                                          'applies when a valid '
                                                                          'refusal of CPR is not '
                                                                          'established; waiting '
                                                                          'for family consent '
                                                                          'costs brain minutes.'}},
                                            {'question': 'Fifteen minutes into a packed RBC '
                                                         'transfusion, the patient develops fever, '
                                                         'back pain, and hypotension. The primary '
                                                         'nurse is off the floor; the blood bank '
                                                         'phone is busy; and a colleague suggests '
                                                         '“finish the unit so none is wasted.” '
                                                         'What is the correct priority sequence?',
                                             'options': ['A) Increase the rate to finish the unit '
                                                         'quickly, then call the provider',
                                                         'B) Continue at the current rate and '
                                                         'recheck vitals in one hour',
                                                         'C) Discard the bag in regular trash so '
                                                         'the reaction cannot be investigated',
                                                         'D) Stop the transfusion, maintain IV '
                                                         'access with normal saline, assess ABCs, '
                                                         'and notify the provider and blood bank'],
                                             'answer': 'D) Stop the transfusion, maintain IV '
                                                       'access with normal saline, assess ABCs, '
                                                       'and notify the provider and blood bank',
                                             'explanation': 'Acute hemolytic or septic transfusion '
                                                            'reactions can progress within '
                                                            'minutes. Stopping the implicated unit '
                                                            'limits further antigen/bacterial '
                                                            'exposure while saline keeps venous '
                                                            'access for resuscitation. Provider '
                                                            'and blood bank notification enables '
                                                            'workup and product quarantine. '
                                                            'Continuing or discarding the bag '
                                                            'worsens injury or destroys evidence.',
                                             'choice_explanations': {'A': 'Faster infusion '
                                                                          'delivers more '
                                                                          'incompatible blood or '
                                                                          'contaminants and '
                                                                          'accelerates hemolysis '
                                                                          'or shock.',
                                                                     'B': 'Waiting an hour allows '
                                                                          'ongoing '
                                                                          'immune/inflammatory '
                                                                          'injury during an acute '
                                                                          'reaction.',
                                                                     'C': 'Discarding the unit '
                                                                          'eliminates evidence '
                                                                          'needed for clerical '
                                                                          'check, culture, and '
                                                                          'hemovigilance.',
                                                                     'D': 'Immediate cessation, '
                                                                          'saline IV access, ABC '
                                                                          'assessment, and dual '
                                                                          'notification are the '
                                                                          'standard acute-reaction '
                                                                          'response.'}},
                                            {'question': 'Smoke is coming from an electrical '
                                                         'outlet behind an occupied bed. The '
                                                         'patient is alert on 2 L oxygen by nasal '
                                                         'cannula; visitors are in the room; and a '
                                                         'medication cart partially blocks the '
                                                         'doorway. Applying RACE, what is your '
                                                         'first action?',
                                             'options': ['A) Rescue the patient to a safe area, '
                                                         'removing oxygen from the fire source as '
                                                         'you move',
                                                         'B) Pull the fire alarm only after you '
                                                         'finish charting the event',
                                                         'C) Stay to fight the fire with a blanket '
                                                         'before moving anyone',
                                                         'D) Close the door and leave the patient '
                                                         'inside to contain smoke'],
                                             'answer': 'A) Rescue the patient to a safe area, '
                                                       'removing oxygen from the fire source as '
                                                       'you move',
                                             'explanation': 'RACE begins with Rescue of anyone in '
                                                            'immediate danger. An alert patient '
                                                            'beside an electrical fire on oxygen '
                                                            'must be moved from the '
                                                            'ignition/oxygen-enriched environment '
                                                            'before Alarm/Contain/Extinguish '
                                                            'steps. Blocking exits and delaying '
                                                            'evacuation increase burn and '
                                                            'inhalation injury risk.',
                                             'choice_explanations': {'A': 'Immediate rescue from '
                                                                          'the fire/oxygen hazard '
                                                                          'is the first RACE '
                                                                          'action for an '
                                                                          'endangered occupant.',
                                                                     'B': 'Alarm follows rescue of '
                                                                          'those in immediate '
                                                                          'danger; charting never '
                                                                          'precedes evacuation.',
                                                                     'C': 'Attempting '
                                                                          'extinguishment before '
                                                                          'rescue leaves the '
                                                                          'patient exposed to '
                                                                          'flame and toxic smoke.',
                                                                     'D': 'Containment is after '
                                                                          'rescue; leaving the '
                                                                          'patient in the '
                                                                          'smoke-filled room '
                                                                          'violates RACE '
                                                                          'order.'}}]},
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
                                                  'D) Apply heat to the chest and reassess '
                                                  'tomorrow'],
                                      'answer': 'B) ABCs, oxygen as indicated, ECG, and rapid '
                                                'notification of the provider',
                                      'explanation': 'Symptoms suggesting ACS require immediate '
                                                     'airway/breathing/circulation support, ECG to '
                                                     'detect STEMI, and rapid escalation for '
                                                     'reperfusion pathways. Delaying assessment '
                                                     'for meals, ambulation, or local heat risks '
                                                     'missing time-critical ischemia.',
                                      'choice_explanations': {'A': 'Ambulation increases '
                                                                   'myocardial demand during '
                                                                   'possible coronary occlusion.',
                                                              'B': 'Stabilizing ABCs, obtaining '
                                                                   'ECG, and notifying the '
                                                                   'provider enable timely ACS '
                                                                   'recognition and treatment.',
                                                              'C': 'Oral intake delays evaluation '
                                                                   'and is unsafe if procedural '
                                                                   'sedation or emergent '
                                                                   'catheterization is needed.',
                                                              'D': 'Heat does not treat coronary '
                                                                   'ischemia and postpones ECG '
                                                                   'diagnosis.'}},
                                     {'question': 'Why is incentive spirometry emphasized after '
                                                  'abdominal surgery?',
                                      'options': ['A) It primarily lowers blood pressure through '
                                                  'vagal stimulation',
                                                  'B) It replaces the need for early ambulation '
                                                  'entirely',
                                                  'C) It promotes alveolar expansion and helps '
                                                  'prevent postoperative atelectasis/pneumonia',
                                                  'D) It is used only to exercise arm muscles '
                                                  'after incision'],
                                      'answer': 'C) It promotes alveolar expansion and helps '
                                                'prevent postoperative atelectasis/pneumonia',
                                      'explanation': 'Shallow breathing after anesthesia and '
                                                     'abdominal pain predisposes to atelectasis. '
                                                     'Incentive spirometry encourages sustained '
                                                     'maximal inspiration, re-expanding alveoli '
                                                     'and reducing pulmonary complication risk '
                                                     'when combined with mobilization and pain '
                                                     'control.',
                                      'choice_explanations': {'A': 'Incentive spirometry targets '
                                                                   'lung expansion, not '
                                                                   'blood-pressure reduction.',
                                                              'B': 'Ambulation remains essential; '
                                                                   'spirometry complements but '
                                                                   'does not replace mobilization.',
                                                              'C': 'Sustained inspiration '
                                                                   're-expands alveoli and is a '
                                                                   'core atelectasis-prevention '
                                                                   'strategy.',
                                                              'D': 'The device trains inspiratory '
                                                                   'effort, not arm muscle '
                                                                   'strength.'}},
                                     {'question': 'Which early findings most classically suggest '
                                                  'hypoglycemia in an alert diabetic patient?',
                                      'options': ['A) Polyuria, polydipsia, and fruity breath '
                                                  'alone',
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
                                                     'rescue before seizure or coma. Osmotic '
                                                     'hyperglycemia symptoms and cholestatic signs '
                                                     'point elsewhere.',
                                      'choice_explanations': {'A': 'Polyuria, polydipsia, and '
                                                                   'ketotic breath suggest '
                                                                   'hyperglycemia/DKA, not '
                                                                   'hypoglycemia.',
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
                                                    'B) Expected muscle gain from one night of '
                                                    'bedrest',
                                                    'C) Adequate diuresis and readiness for '
                                                    'discharge teaching only',
                                                    'D) Dehydration from excessive fluid '
                                                    'restriction'],
                                        'answer': 'A) Worsening fluid retention requiring '
                                                  'assessment of volume status and provider '
                                                  'notification',
                                        'explanation': 'Rapid overnight weight gain with orthopnea '
                                                       'reflects increasing '
                                                       'intravascular/interstitial volume in heart '
                                                       'failure. Nurses trend daily weights as an '
                                                       'early congestion marker and escalate for '
                                                       'possible diuretic adjustment before frank '
                                                       'pulmonary edema develops.',
                                        'choice_explanations': {'A': 'Acute weight gain plus '
                                                                     'orthopnea signals congesting '
                                                                     'heart failure needing volume '
                                                                     'reassessment and escalation.',
                                                                'B': 'Muscle mass does not '
                                                                     'increase overnight; '
                                                                     'kilogram-scale gains are '
                                                                     'fluid.',
                                                                'C': 'Orthopnea and weight gain '
                                                                     'contradict adequate '
                                                                     'diuresis.',
                                                                'D': 'Dehydration causes weight '
                                                                     'loss, not rapid gain with '
                                                                     'orthopnea.'}},
                                       {'question': 'After blind NG tube insertion for feeding, '
                                                    'which confirmation method is the gold '
                                                    'standard before first use?',
                                        'options': ['A) Auscultating air insufflation over the '
                                                    'stomach alone',
                                                    'B) Radiographic verification of tip position '
                                                    'per protocol',
                                                    'C) Assuming correct placement if the patient '
                                                    'does not cough',
                                                    'D) Checking that the external tube length '
                                                    'looks unchanged from another patient'],
                                        'answer': 'B) Radiographic verification of tip position '
                                                  'per protocol',
                                        'explanation': 'Radiographic confirmation is the accepted '
                                                       'gold standard before initiating feedings '
                                                       'because auscultation and absence of cough '
                                                       'miss respiratory placements. Incorrect NG '
                                                       'position risks aspiration pneumonia and '
                                                       'death.',
                                        'choice_explanations': {'A': 'Air auscultation cannot '
                                                                     'reliably distinguish gastric '
                                                                     'from pulmonary placement.',
                                                                'B': 'X-ray confirmation verifies '
                                                                     'tip location before feeding, '
                                                                     'preventing unrecognized '
                                                                     'bronchial placement.',
                                                                'C': 'Patients may not cough with '
                                                                     'pulmonary placement, '
                                                                     'especially if sedated.',
                                                                'D': 'External length from another '
                                                                     'patient is irrelevant to '
                                                                     'this patient’s anatomy.'}},
                                       {'question': 'Which nursing plan best applies '
                                                    'evidence-based prevention of '
                                                    'hospital-acquired DVT in a postoperative '
                                                    'adult?',
                                        'options': ['A) Encourage prolonged bedrest to protect the '
                                                    'incision',
                                                    'B) Massage calves vigorously every hour to '
                                                    '“break up clots”',
                                                    'C) Early ambulation, anticoagulation as '
                                                    'ordered, and mechanical prophylaxis when '
                                                    'indicated',
                                                    'D) Restrict fluids severely to thicken venous '
                                                    'return'],
                                        'answer': 'C) Early ambulation, anticoagulation as '
                                                  'ordered, and mechanical prophylaxis when '
                                                  'indicated',
                                        'explanation': 'Venous stasis, endothelial injury, and '
                                                       'hypercoagulability drive postoperative '
                                                       'DVT. Early ambulation, ordered '
                                                       'pharmacologic prophylaxis, and mechanical '
                                                       'devices reduce stasis and thrombus '
                                                       'formation. Bedrest, calf massage of '
                                                       'possible clots, and intentional '
                                                       'hemoconcentration increase risk.',
                                        'choice_explanations': {'A': 'Immobility worsens venous '
                                                                     'stasis, the opposite of DVT '
                                                                     'prevention.',
                                                                'B': 'Massaging a potential deep '
                                                                     'vein thrombus can embolize '
                                                                     'clot to the lungs.',
                                                                'C': 'Ambulation plus '
                                                                     'pharmacologic/mechanical '
                                                                     'prophylaxis targets the '
                                                                     'major preventable DVT '
                                                                     'pathway.',
                                                                'D': 'Dehydration increases '
                                                                     'viscosity and thrombotic '
                                                                     'risk.'}}],
                            'hard': [{'question': 'On postoperative day 2, a patient has fever '
                                                  '38.9°C, HR 122, RR 28, BP 88/50, and new '
                                                  'confusion. Lactate is pending. What is the '
                                                  'priority nursing recognition and action theme?',
                                      'options': ['A) Treat as expected postoperative fever and '
                                                  'ambulate in the hallway',
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
                                                     'recognition, ABC support, cultures before '
                                                     'antibiotics when feasible, lactate, fluids '
                                                     'per protocol, and rapid escalation improve '
                                                     'survival; attributing findings to “normal” '
                                                     'postop changes delays care.',
                                      'choice_explanations': {'A': 'Hypotension and confusion are '
                                                                   'not benign expected fever; '
                                                                   'they suggest organ '
                                                                   'hypoperfusion.',
                                                              'B': 'New confusion with abnormal '
                                                                   'vitals is delirium of acute '
                                                                   'illness until proven '
                                                                   'otherwise, not routine '
                                                                   'sundowning.',
                                                              'C': 'Systemic hypoperfusion '
                                                                   'outranks isolated wound care; '
                                                                   'source control follows '
                                                                   'resuscitation.',
                                                              'D': 'Multi-cue sepsis/shock '
                                                                   'recognition with ABC support '
                                                                   'and urgent escalation matches '
                                                                   'Surviving Sepsis priorities.'}},
                                     {'question': 'A COPD patient on high-flow oxygen becomes '
                                                  'increasingly drowsy with rising PaCO2 on ABG. '
                                                  'What is the main nursing concern?',
                                      'options': ['A) Oxygen-related CO2 retention/hypoventilation '
                                                  'requiring reassessment of O2 target and '
                                                  'ventilatory status',
                                                  'B) Expected sedation from improved oxygenation '
                                                  'that needs no follow-up',
                                                  'C) Hyperactive delirium that should be treated '
                                                  'with a benzodiazepine first',
                                                  'D) Pure metabolic alkalosis unrelated to oxygen '
                                                  'therapy'],
                                      'answer': 'A) Oxygen-related CO2 retention/hypoventilation '
                                                'requiring reassessment of O2 target and '
                                                'ventilatory status',
                                      'explanation': 'Some COPD patients lose hypoxic drive or '
                                                     'worsen V/Q mismatch on excessive oxygen, '
                                                     'producing CO2 narcosis. Drowsiness with '
                                                     'rising PaCO2 mandates lowering oxygen toward '
                                                     'SpO2 targets (~88–92% when appropriate), '
                                                     'supporting ventilation, and escalating—not '
                                                     'ignoring sedation or adding respiratory '
                                                     'depressants.',
                                      'choice_explanations': {'A': 'Drowsiness plus rising PaCO2 '
                                                                   'on high O2 signals CO2 '
                                                                   'retention needing O2 titration '
                                                                   'and ventilatory support.',
                                                              'B': 'Progressive drowsiness with '
                                                                   'hypercapnia is dangerous, not '
                                                                   'a benign effect of oxygen.',
                                                              'C': 'Benzodiazepines further '
                                                                   'depress ventilation in '
                                                                   'hypercapnic COPD.',
                                                              'D': 'The vignette describes '
                                                                   'ventilatory failure with CO2 '
                                                                   'rise, not primary metabolic '
                                                                   'alkalosis.'}},
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
                                                  'D) Hypocalcemia tetany as the only possible '
                                                  'cause, so give oral calcium and leave'],
                                      'answer': 'B) Airway compression from hematoma/edema '
                                                'requiring immediate airway support and surgical '
                                                'notification',
                                      'explanation': 'Neck hematoma or edema after thyroidectomy '
                                                     'can rapidly obstruct the airway. Stridor, '
                                                     'tightness, and desaturation demand immediate '
                                                     'airway management and surgeon notification '
                                                     'for possible evacuation. Delaying for '
                                                     'reassurance or treating only hypocalcemia '
                                                     'misses a surgical airway emergency (though '
                                                     'hypocalcemia remains a later concern).',
                                      'choice_explanations': {'A': 'Stridor and desaturation are '
                                                                   'not routine sore throat and '
                                                                   'can progress to complete '
                                                                   'obstruction.',
                                                              'B': 'Airway compression from '
                                                                   'postoperative hematoma/edema '
                                                                   'is the life-threatening '
                                                                   'priority.',
                                                              'C': 'Anxiety coaching without '
                                                                   'airway assessment ignores '
                                                                   'objective stridor and hypoxia.',
                                                              'D': 'Hypocalcemia usually presents '
                                                                   'later with '
                                                                   'tetany/paresthesias; acute '
                                                                   'stridor points first to '
                                                                   'mechanical airway threat.'}}],
                            'extreme': [{'question': 'Two minutes after starting IV ceftriaxone, a '
                                                     'patient develops urticaria, wheezing, BP '
                                                     '70/40, and a sense of doom. The provider’s '
                                                     'phone goes to voicemail. An order set on the '
                                                     'chart lists “diphenhydramine 25 mg PO PRN '
                                                     'itch.” What is the first drug/action '
                                                     'priority?',
                                         'options': ['A) Give the PRN oral diphenhydramine and '
                                                     'continue the antibiotic infusion',
                                                     'B) Place the patient supine without '
                                                     'epinephrine because BP is already low',
                                                     'C) Stop the infusion and give intramuscular '
                                                     'epinephrine per anaphylaxis protocol while '
                                                     'activating emergency response',
                                                     'D) Start a fluid bolus only and defer '
                                                     'epinephrine until allergy testing is done'],
                                         'answer': 'C) Stop the infusion and give intramuscular '
                                                   'epinephrine per anaphylaxis protocol while '
                                                   'activating emergency response',
                                         'explanation': 'This is anaphylactic shock from IV '
                                                        'antibiotic. Immediate cessation of the '
                                                        'antigen and IM epinephrine are '
                                                        'first-line; epinephrine treats '
                                                        'vasodilation and bronchoconstriction. '
                                                        'Oral antihistamine alone, withholding '
                                                        'epinephrine for hypotension myths, or '
                                                        'waiting for testing are dangerous delays.',
                                         'choice_explanations': {'A': 'Oral antihistamine does not '
                                                                      'reverse anaphylactic shock, '
                                                                      'and continuing the drug '
                                                                      'worsens antigen exposure.',
                                                                 'B': 'Hypotension is an '
                                                                      'indication for epinephrine '
                                                                      'in anaphylaxis, not a '
                                                                      'reason to withhold it.',
                                                                 'C': 'Stopping the drug and '
                                                                      'giving IM epinephrine while '
                                                                      'calling for help is the '
                                                                      'evidence-based first '
                                                                      'response.',
                                                                 'D': 'Fluids support BP but do '
                                                                      'not replace epinephrine as '
                                                                      'the disease-modifying first '
                                                                      'drug.'}},
                                        {'question': 'A patient with known lung cancer suddenly '
                                                     'coughs up large volumes of bright red blood, '
                                                     'SpO2 82% on room air, and becomes pale and '
                                                     'anxious. Radiology wants him transported now '
                                                     'for a non-urgent staging CT. What is the '
                                                     'nursing priority?',
                                         'options': ['A) Send for CT immediately to identify the '
                                                     'bleeding vessel before any airway support',
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
                                         'explanation': 'Massive hemoptysis threatens airway '
                                                        'patency and gas exchange before the '
                                                        'source is imaged. Priorities are airway '
                                                        'protection, oxygen, positioning (often '
                                                        'bleeding-side down when known), '
                                                        'hemodynamic support, and emergency '
                                                        'escalation. Non-urgent CT and ambulation '
                                                        'increase aspiration and hypoxic risk.',
                                         'choice_explanations': {'A': 'Unstable hemoptysis '
                                                                      'patients need '
                                                                      'airway/resuscitation first; '
                                                                      'non-urgent CT can wait.',
                                                                 'B': 'Oral fluids do not restore '
                                                                      'circulating volume and risk '
                                                                      'aspiration during active '
                                                                      'bleeding.',
                                                                 'C': 'Ambulation worsens bleeding '
                                                                      'and hypoxia during massive '
                                                                      'hemoptysis.',
                                                                 'D': 'Airway/oxygen support and '
                                                                      'rapid response while '
                                                                      'holding non-urgent '
                                                                      'transport address the '
                                                                      'immediate lethal threat.'}},
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
                                                     'B) Accept the explanation and max out '
                                                     'opioids without further assessment',
                                                     'C) Elevate the limb above the heart '
                                                     'continuously and ignore stretch pain',
                                                     'D) Remove the cast yourself immediately '
                                                     'without notifying the provider or surgeon'],
                                         'answer': 'A) Escalate urgently for compartment syndrome '
                                                   'evaluation; pulses can remain until late',
                                         'explanation': 'Compartment syndrome is a clinical '
                                                        'diagnosis: pain out of proportion, pain '
                                                        'on passive stretch, and sensory changes '
                                                        'are early cues. Distal pulses often '
                                                        'persist until late ischemia. Nurses must '
                                                        'escalate despite false reassurance from '
                                                        'palpable pulses; opioids alone mask '
                                                        'progression toward irreversible '
                                                        'muscle/nerve injury.',
                                         'choice_explanations': {'A': 'Multi-cue findings with '
                                                                      'preserved pulses still '
                                                                      'warrant urgent surgical '
                                                                      'evaluation for fasciotomy '
                                                                      'timing.',
                                                                 'B': 'More opioid without '
                                                                      'escalation allows '
                                                                      'compartment pressure injury '
                                                                      'to progress.',
                                                                 'C': 'Extreme elevation can '
                                                                      'reduce arterial perfusion; '
                                                                      'stretch pain is a red flag, '
                                                                      'not to be ignored.',
                                                                 'D': 'Cast bivalving may be '
                                                                      'ordered, but unilateral '
                                                                      'removal without the team '
                                                                      'can be unsafe; urgent '
                                                                      'notification is '
                                                                      'required.'}}]},
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
                                        'options': ['A) Dorsogluteal muscle to avoid the sciatic '
                                                    'nerve',
                                                    'B) Vastus lateralis (anterolateral thigh)',
                                                    'C) Deltoid only, regardless of muscle mass',
                                                    'D) Ventrogluteal site exclusively in early '
                                                    'infancy'],
                                        'answer': 'B) Vastus lateralis (anterolateral thigh)',
                                        'explanation': 'In young infants the vastus lateralis has '
                                                       'adequate muscle mass and avoids major '
                                                       'nerves and vessels used in other sites. '
                                                       'Deltoid mass is often insufficient early '
                                                       'on; dorsogluteal injections risk sciatic '
                                                       'injury and are avoided.',
                                        'choice_explanations': {'A': 'Dorsogluteal injections risk '
                                                                     'sciatic nerve injury and are '
                                                                     'not preferred in infants.',
                                                                'B': 'The anterolateral thigh '
                                                                     '(vastus lateralis) is the '
                                                                     'recommended IM site for '
                                                                     'young infants.',
                                                                'C': 'Infant deltoid mass is often '
                                                                     'inadequate for safe IM '
                                                                     'injection.',
                                                                'D': 'Ventrogluteal use is more '
                                                                     'common in older '
                                                                     'children/adults once '
                                                                     'landmarks and mass allow.'}},
                                       {'question': 'Pediatric medication doses are most commonly '
                                                    'calculated using which patient factor?',
                                        'options': ['A) Adult standard dose cut in half for all '
                                                    'ages',
                                                    'B) Shoe size as a surrogate for maturity',
                                                    'C) Body weight (and sometimes body surface '
                                                    'area)',
                                                    'D) Room number to standardize unit dosing'],
                                        'answer': 'C) Body weight (and sometimes body surface '
                                                  'area)',
                                        'explanation': 'Children’s pharmacokinetics scale '
                                                       'primarily with body size; weight-based '
                                                       '(mg/kg) and sometimes BSA-based dosing '
                                                       'prevent under- and overdosing. Adult '
                                                       'half-doses, shoe size, and room number '
                                                       'have no pharmacologic basis.',
                                        'choice_explanations': {'A': 'Halving adult doses ignores '
                                                                     'wide pediatric weight ranges '
                                                                     'and can cause toxicity or '
                                                                     'failure.',
                                                                'B': 'Shoe size does not determine '
                                                                     'volume of distribution or '
                                                                     'clearance.',
                                                                'C': 'Weight-based (and sometimes '
                                                                     'BSA) dosing matches '
                                                                     'developmental '
                                                                     'pharmacokinetics.',
                                                                'D': 'Room number is unrelated to '
                                                                     'dose requirements.'}},
                                       {'question': 'Anterior fontanelle assessment is clinically '
                                                    'most relevant in which pediatric age group?',
                                        'options': ['A) Only adolescents after growth-plate '
                                                    'closure',
                                                    'B) Only adults with chronic headache',
                                                    'C) Only neonates in the first 24 hours of '
                                                    'life',
                                                    'D) Infants while the fontanelle remains '
                                                    'patent (typically through early infancy)'],
                                        'answer': 'D) Infants while the fontanelle remains patent '
                                                  '(typically through early infancy)',
                                        'explanation': 'The anterior fontanelle remains open in '
                                                       'infancy and provides a window on '
                                                       'intracranial pressure and hydration '
                                                       '(bulging vs sunken). After closure, it is '
                                                       'no longer available as an assessment '
                                                       'landmark.',
                                        'choice_explanations': {'A': 'Adolescent cranial sutures '
                                                                     'are closed; fontanelle '
                                                                     'assessment is not '
                                                                     'applicable.',
                                                                'B': 'Adults lack a patent '
                                                                     'fontanelle for this '
                                                                     'assessment.',
                                                                'C': 'Assessment matters '
                                                                     'throughout infancy while the '
                                                                     'fontanelle is open, not only '
                                                                     'day one.',
                                                                'D': 'Patent fontanelles in '
                                                                     'infants allow pressure and '
                                                                     'hydration cues until '
                                                                     'closure.'}}],
                              'medium': [{'question': 'A toddler with gastroenteritis has sunken '
                                                      'eyes, absent tears, dry mucous membranes, '
                                                      'and delayed capillary refill. What do these '
                                                      'signs indicate?',
                                          'options': ['A) Moderate to severe dehydration requiring '
                                                      'urgent fluid assessment and escalation',
                                                      'B) Adequate hydration because the child is '
                                                      'still crying intermittently',
                                                      'C) Isolated allergic rhinitis unrelated to '
                                                      'volume status',
                                                      'D) Overhydration from excess free water'],
                                          'answer': 'A) Moderate to severe dehydration requiring '
                                                    'urgent fluid assessment and escalation',
                                          'explanation': 'Sunken eyes, absent tears, dry mucosa, '
                                                         'and delayed CRT are classic dehydration '
                                                         'signs reflecting volume loss and '
                                                         'impaired perfusion. Pediatric patients '
                                                         'decompensate quickly; nurses escalate '
                                                         'for oral/IV rehydration based on '
                                                         'severity rather than waiting for '
                                                         'complete anuria.',
                                          'choice_explanations': {'A': 'Combined mucosal and '
                                                                       'perfusion signs indicate '
                                                                       'clinically important '
                                                                       'dehydration needing urgent '
                                                                       'management.',
                                                                  'B': 'Intermittent crying does '
                                                                       'not negate objective '
                                                                       'dehydration signs.',
                                                                  'C': 'These findings reflect '
                                                                       'volume status, not primary '
                                                                       'rhinitis.',
                                                                  'D': 'Overhydration would not '
                                                                       'produce sunken eyes and '
                                                                       'delayed CRT.'}},
                                         {'question': 'When is the FLACC pain scale the most '
                                                      'appropriate choice?',
                                          'options': ['A) Only for verbal adults who can use a '
                                                      '0–10 numeric rating',
                                                      'B) For infants/young children who cannot '
                                                      'self-report pain reliably',
                                                      'C) As a substitute for vital signs in '
                                                      'septic shock',
                                                      'D) Only postoperatively in patients with '
                                                      'epidurals'],
                                          'answer': 'B) For infants/young children who cannot '
                                                    'self-report pain reliably',
                                          'explanation': 'FLACC scores Face, Legs, Activity, Cry, '
                                                         'and Consolability—behavioral cues used '
                                                         'when children cannot self-report. '
                                                         'Numeric scales suit verbal older '
                                                         'patients; FLACC does not replace '
                                                         'hemodynamic assessment in shock.',
                                          'choice_explanations': {'A': 'Verbal adults should use '
                                                                       'self-report scales, not '
                                                                       'FLACC.',
                                                                  'B': 'FLACC is designed for '
                                                                       'preverbal or '
                                                                       'non-self-reporting young '
                                                                       'children.',
                                                                  'C': 'Pain scales complement but '
                                                                       'do not replace ABC/sepsis '
                                                                       'assessment.',
                                                                  'D': 'FLACC is not limited to '
                                                                       'epidural patients; it is '
                                                                       'an age/ability-based '
                                                                       'tool.'}},
                                         {'question': 'Nursing care for an infant with RSV '
                                                      'bronchiolitis should primarily focus on '
                                                      'which priorities?',
                                          'options': ['A) Forcing oral feeds despite marked '
                                                      'tachypnea',
                                                      'B) Routine chest physiotherapy as the '
                                                      'mainstay for all cases',
                                                      'C) Airway support, hydration as tolerated, '
                                                      'oxygen/monitoring, and infection control',
                                                      'D) Immediate antibiotics for all viral '
                                                      'bronchiolitis'],
                                          'answer': 'C) Airway support, hydration as tolerated, '
                                                    'oxygen/monitoring, and infection control',
                                          'explanation': 'RSV bronchiolitis care is supportive: '
                                                         'maintain airway and oxygenation, '
                                                         'carefully manage fluids, monitor for '
                                                         'apnea/respiratory failure, and use '
                                                         'contact precautions. Antibiotics treat '
                                                         'bacterial coinfection only; aggressive '
                                                         'feeding during severe work of breathing '
                                                         'risks aspiration.',
                                          'choice_explanations': {'A': 'Forced oral feeding with '
                                                                       'high work of breathing '
                                                                       'risks aspiration and '
                                                                       'fatigue.',
                                                                  'B': 'Routine CPT is not '
                                                                       'standard for all RSV '
                                                                       'bronchiolitis and may '
                                                                       'increase distress.',
                                                                  'C': 'Supportive '
                                                                       'airway/oxygen/hydration '
                                                                       'care with isolation '
                                                                       'precautions matches '
                                                                       'evidence-based RSV '
                                                                       'nursing.',
                                                                  'D': 'RSV is viral; antibiotics '
                                                                       'are not routinely '
                                                                       'indicated without '
                                                                       'bacterial infection.'}}],
                              'hard': [{'question': 'A toddler has patterned burns and a changing '
                                                    'caregiver story. The child is hemodynamically '
                                                    'stable. What is the nurse’s legal and ethical '
                                                    'obligation?',
                                        'options': ['A) Confront the caregiver aggressively in the '
                                                    'waiting room before documenting',
                                                    'B) Wait until absolute proof is obtained in '
                                                    'court before telling anyone',
                                                    'C) Discharge home quickly to avoid involving '
                                                    'social services',
                                                    'D) Report suspected abuse per mandatory '
                                                    'reporting laws and ensure immediate safety'],
                                        'answer': 'D) Report suspected abuse per mandatory '
                                                  'reporting laws and ensure immediate safety',
                                        'explanation': 'Nurses are mandatory reporters: reasonable '
                                                       'suspicion of abuse triggers reporting and '
                                                       'protection, not courtroom-level proof. '
                                                       'Patterned burns with inconsistent history '
                                                       'warrant report and safety planning while '
                                                       'medical care continues. Confrontation that '
                                                       'escalates risk or premature discharge is '
                                                       'unsafe.',
                                        'choice_explanations': {'A': 'Hostile confrontation can '
                                                                     'increase danger and '
                                                                     'compromise investigation; '
                                                                     'report through proper '
                                                                     'channels.',
                                                                'B': 'The reporting threshold is '
                                                                     'reasonable suspicion, not '
                                                                     'judicial certainty.',
                                                                'C': 'Discharging to a potentially '
                                                                     'unsafe home violates the '
                                                                     'duty to protect.',
                                                                'D': 'Mandatory reporting plus '
                                                                     'ensuring safety is the '
                                                                     'required nursing response.'}},
                                       {'question': 'A 3-year-old sits forward, drools, and has '
                                                    'stridor with high fever. The caregiver asks '
                                                    'you to look in the throat with a tongue '
                                                    'blade. What is the correct caution?',
                                        'options': ['A) Do not agitate or instrument the airway; '
                                                    'keep the child calm and prepare for emergency '
                                                    'airway management',
                                                    'B) Force the child supine and examine the '
                                                    'pharynx immediately',
                                                    'C) Give a throat lozenge and discharge if '
                                                    'SpO2 is briefly 94%',
                                                    'D) Perform blind finger sweeps to clear '
                                                    'secretions'],
                                        'answer': 'A) Do not agitate or instrument the airway; '
                                                  'keep the child calm and prepare for emergency '
                                                  'airway management',
                                        'explanation': 'Tripod posture, drooling, and stridor '
                                                       'suggest epiglottitis or critical '
                                                       'upper-airway obstruction. Stimulating the '
                                                       'airway can cause complete obstruction. '
                                                       'Keep the child calm in a preferred '
                                                       'position, give oxygen as tolerated, and '
                                                       'prepare for controlled airway management '
                                                       'with specialists.',
                                        'choice_explanations': {'A': 'Avoiding '
                                                                     'agitation/instrumentation '
                                                                     'while preparing advanced '
                                                                     'airway support is the key '
                                                                     'safety principle.',
                                                                'B': 'Forcing supine examination '
                                                                     'can precipitate total airway '
                                                                     'loss.',
                                                                'C': 'This presentation is a '
                                                                     'life-threatening emergency, '
                                                                     'not a dischargeable sore '
                                                                     'throat.',
                                                                'D': 'Blind finger sweeps can push '
                                                                     'obstruction deeper and '
                                                                     'provoke spasm.'}},
                                       {'question': 'A child treated for Kawasaki disease is '
                                                    'irritable with persistent fever and a new '
                                                    'gallop. Which complication concern should '
                                                    'guide nursing surveillance?',
                                        'options': ['A) Isolated otitis media as the only sequela '
                                                    'of concern',
                                                    'B) Coronary artery aneurysms and myocardial '
                                                    'ischemia/dysfunction',
                                                    'C) Simple viral exanthem without cardiac '
                                                    'follow-up',
                                                    'D) Guaranteed immunity to all future '
                                                    'streptococcal disease'],
                                        'answer': 'B) Coronary artery aneurysms and myocardial '
                                                  'ischemia/dysfunction',
                                        'explanation': 'Kawasaki disease can cause coronary '
                                                       'arteritis and aneurysms, risking ischemia, '
                                                       'infarction, and ventricular dysfunction. '
                                                       'Persistent fever and new gallop heighten '
                                                       'concern for ongoing inflammation/cardiac '
                                                       'involvement, mandating monitoring, '
                                                       'IVIG/aspirin per protocol, and cardiology '
                                                       'follow-up—not dismissal as a simple rash.',
                                        'choice_explanations': {'A': 'Otitis is not the defining '
                                                                     'serious sequela of Kawasaki '
                                                                     'disease.',
                                                                'B': 'Coronary aneurysms and '
                                                                     'cardiac dysfunction are the '
                                                                     'critical complications '
                                                                     'nurses watch for.',
                                                                'C': 'Cardiac surveillance is '
                                                                     'mandatory; this is not a '
                                                                     'benign viral exanthem.',
                                                                'D': 'Kawasaki treatment does not '
                                                                     'confer streptococcal '
                                                                     'immunity.'}}],
                              'extreme': [{'question': 'A 6-year-old becomes unresponsive and '
                                                       'pulseless in the playroom after '
                                                       'progressive respiratory distress. An AED '
                                                       'is being attached; a parent is screaming '
                                                       'to “give adult shocks now.” Using '
                                                       'pediatric BLS principles, what compression '
                                                       'approach should you prioritize while the '
                                                       'team prepares defibrillation?',
                                           'options': ['A) Compress at adult depth of at least 5 '
                                                       'inches on the xiphoid to be “sure”',
                                                       'B) Deliver only rescue breaths without '
                                                       'compressions until a physician arrives',
                                                       'C) Start high-quality CPR with chest '
                                                       'compressions to about one-third AP chest '
                                                       'depth (≈5 cm in children) and allow full '
                                                       'recoil',
                                                       'D) Wait for a pulse check every 5 seconds '
                                                       'before any compression'],
                                           'answer': 'C) Start high-quality CPR with chest '
                                                     'compressions to about one-third AP chest '
                                                     'depth (≈5 cm in children) and allow full '
                                                     'recoil',
                                           'explanation': 'Pediatric cardiac arrest is often '
                                                          'hypoxic; immediate high-quality '
                                                          'compressions with age-appropriate depth '
                                                          '(~⅓ AP diameter), full recoil, and '
                                                          'minimal interruptions improve coronary '
                                                          'perfusion while AED/defibrillation is '
                                                          'prepared. Excessive depth risks injury; '
                                                          'pulse-check delays and breath-only '
                                                          'approaches worsen ischemic time.',
                                           'choice_explanations': {'A': 'Excessive depth and '
                                                                        'xiphoid pressure risk '
                                                                        'trauma and are not '
                                                                        'pediatric technique.',
                                                                   'B': 'Compressions are '
                                                                        'essential once pulseless; '
                                                                        'breaths alone do not '
                                                                        'circulate blood.',
                                                                   'C': 'Age-appropriate depth '
                                                                        'with full recoil is the '
                                                                        'pediatric BLS compression '
                                                                        'standard.',
                                                                   'D': 'Frequent prolonged pulse '
                                                                        'checks interrupt '
                                                                        'perfusion; minimize '
                                                                        'pauses.'}},
                                          {'question': 'A school-age child with a known peanut '
                                                       'allergy eats a cookie at a party, then '
                                                       'develops facial swelling, wheeze, and BP '
                                                       '78/40. The parent’s epinephrine '
                                                       'auto-injector is available, but a '
                                                       'volunteer insists you “wait for EMS so you '
                                                       'don’t get in trouble.” What should you do?',
                                           'options': ['A) Wait for EMS arrival before any '
                                                       'medication',
                                                       'B) Give oral diphenhydramine only and '
                                                       'observe in the hallway',
                                                       'C) Have the child walk briskly to “work '
                                                       'off” the reaction',
                                                       'D) Give epinephrine IM via auto-injector '
                                                       'immediately and activate emergency '
                                                       'services'],
                                           'answer': 'D) Give epinephrine IM via auto-injector '
                                                     'immediately and activate emergency services',
                                           'explanation': 'Anaphylaxis with respiratory and '
                                                          'hypotensive features requires immediate '
                                                          'IM epinephrine; delay increases '
                                                          'fatality. Antihistamines are adjuncts '
                                                          'only. EMS should be activated '
                                                          'concurrently, not as a reason to '
                                                          'withhold first-line epinephrine already '
                                                          'in hand.',
                                           'choice_explanations': {'A': 'Waiting for EMS before '
                                                                        'epinephrine is a common '
                                                                        'fatal delay in '
                                                                        'anaphylaxis.',
                                                                   'B': 'Antihistamines do not '
                                                                        'reverse airway edema or '
                                                                        'shock.',
                                                                   'C': 'Exercise worsens '
                                                                        'distribution of allergen '
                                                                        'and shock.',
                                                                   'D': 'Immediate IM epinephrine '
                                                                        'plus EMS activation is '
                                                                        'the correct priority '
                                                                        'sequence.'}},
                                          {'question': 'After a high-speed MVC, a child is drowsy '
                                                       'with unequal pupils, HR 58, and BP 150/95. '
                                                       'The cervical collar is in place. A '
                                                       'colleague wants to flex the neck for a '
                                                       '“better airway look” and start hypotonic '
                                                       'free-water fluids wide open. What is the '
                                                       'priority nursing approach?',
                                           'options': ['A) Protect airway/C-spine, avoid hypotonic '
                                                       'fluids, elevate head of bed if permitted, '
                                                       'and escalate for rising ICP/herniation '
                                                       'signs',
                                                       'B) Flex the neck aggressively to improve '
                                                       'the view without precautions',
                                                       'C) Give free-water boluses to lower sodium '
                                                       'rapidly',
                                                       'D) Remove the collar because bradycardia '
                                                       'proves the spine is fine'],
                                           'answer': 'A) Protect airway/C-spine, avoid hypotonic '
                                                     'fluids, elevate head of bed if permitted, '
                                                     'and escalate for rising ICP/herniation signs',
                                           'explanation': 'Bradycardia with hypertension and '
                                                          'unequal pupils suggests Cushing '
                                                          'physiology and possible herniation '
                                                          'after trauma. Priorities are airway '
                                                          'with C-spine protection, '
                                                          'normoxia/normocapnia goals per '
                                                          'protocol, avoiding hypotonic fluids '
                                                          'that worsen cerebral edema, head '
                                                          'elevation if approved, and emergent '
                                                          'neurosurgical escalation.',
                                           'choice_explanations': {'A': 'C-spine/airway protection '
                                                                        'and ICP-minded care with '
                                                                        'urgent escalation match '
                                                                        'traumatic brain injury '
                                                                        'priorities.',
                                                                   'B': 'Neck flexion without '
                                                                        'stabilization risks cord '
                                                                        'injury and does not treat '
                                                                        'herniation.',
                                                                   'C': 'Hypotonic free water can '
                                                                        'worsen cerebral edema.',
                                                                   'D': 'Bradycardia here is a '
                                                                        'late ICP sign, not proof '
                                                                        'the spine is '
                                                                        'uninjured.'}}]},
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
                                       'options': ['A) Long-term intelligence quotient at age 5',
                                                   'B) Immediate cardiopulmonary and neuromuscular '
                                                   'transition at 1 and 5 minutes',
                                                   'C) Maternal blood type compatibility only',
                                                   'D) Exact gestational age in weeks'],
                                       'answer': 'B) Immediate cardiopulmonary and neuromuscular '
                                                 'transition at 1 and 5 minutes',
                                       'explanation': 'APGAR evaluates Appearance, Pulse, Grimace, '
                                                      'Activity, and Respiration to summarize the '
                                                      'newborn’s immediate adaptation and need for '
                                                      'resuscitation support. It is not an IQ '
                                                      'test, blood-type assay, or dating tool.',
                                       'choice_explanations': {'A': 'APGAR does not predict '
                                                                    'long-term intelligence.',
                                                               'B': 'It scores immediate '
                                                                    'transition and guides early '
                                                                    'resuscitation needs at 1 and '
                                                                    '5 minutes.',
                                                               'C': 'Blood type is a separate '
                                                                    'maternal–neonatal lab issue.',
                                                               'D': 'Gestational age uses other '
                                                                    'dating methods, not APGAR.'}},
                                      {'question': 'Why is fundal massage performed in the '
                                                   'immediate postpartum period when the uterus is '
                                                   'boggy?',
                                       'options': ['A) To induce lactation within seconds',
                                                   'B) To replace the need for quantifying blood '
                                                   'loss',
                                                   'C) To stimulate uterine contraction and reduce '
                                                   'postpartum hemorrhage from atony',
                                                   'D) To confirm placental pathology under the '
                                                   'microscope'],
                                       'answer': 'C) To stimulate uterine contraction and reduce '
                                                 'postpartum hemorrhage from atony',
                                       'explanation': 'Uterine atony is a leading cause of '
                                                      'postpartum hemorrhage. Fundal massage '
                                                      'stimulates myometrial contraction, '
                                                      'compressing vessels at the placental site. '
                                                      'It complements uterotonics and does not '
                                                      'replace blood-loss assessment or lactation '
                                                      'physiology.',
                                       'choice_explanations': {'A': 'Massage does not instantly '
                                                                    'induce lactation.',
                                                               'B': 'Blood loss still must be '
                                                                    'quantified; massage treats '
                                                                    'atony.',
                                                               'C': 'Contraction from massage '
                                                                    'reduces bleeding from an '
                                                                    'atonic uterus.',
                                                               'D': 'Massage is a clinical '
                                                                    'intervention, not a pathology '
                                                                    'technique.'}},
                                      {'question': 'An Rh-negative mother delivers an Rh-positive '
                                                   'newborn. Which postpartum intervention may she '
                                                   'need?',
                                       'options': ['A) High-dose vitamin K to the mother instead '
                                                   'of the newborn',
                                                   'B) Immediate hysterectomy for sensitization '
                                                   'prevention',
                                                   'C) No blood-product counseling of any kind',
                                                   'D) Rh(D) immune globulin (RhoGAM) as indicated '
                                                   'to prevent sensitization'],
                                       'answer': 'D) Rh(D) immune globulin (RhoGAM) as indicated '
                                                 'to prevent sensitization',
                                       'explanation': 'RhIG given when indicated prevents maternal '
                                                      'anti-D formation after exposure to '
                                                      'Rh-positive fetal cells, protecting future '
                                                      'pregnancies from hemolytic disease. It is '
                                                      'not replaced by vitamin K, surgery, or '
                                                      'omission of counseling.',
                                       'choice_explanations': {'A': 'Vitamin K is for newborn '
                                                                    'hemorrhagic disease '
                                                                    'prevention, not maternal Rh '
                                                                    'sensitization.',
                                                               'B': 'Hysterectomy is not the '
                                                                    'prophylaxis for Rh '
                                                                    'incompatibility.',
                                                               'C': 'Counseling about RhIG timing '
                                                                    'and indications is essential.',
                                                               'D': 'RhIG prevents '
                                                                    'alloimmunization in eligible '
                                                                    'Rh-negative mothers.'}}],
                             'medium': [{'question': 'Which cluster best represents danger signs '
                                                     'of worsening preeclampsia that require '
                                                     'urgent escalation?',
                                         'options': ['A) Severe headache, visual changes, '
                                                     'epigastric pain, and rising BP',
                                                     'B) Isolated mild ankle edema without other '
                                                     'findings in late pregnancy',
                                                     'C) Fetal quickening reported for the first '
                                                     'time at 20 weeks',
                                                     'D) Leukorrhea without itching in the second '
                                                     'trimester'],
                                         'answer': 'A) Severe headache, visual changes, epigastric '
                                                   'pain, and rising BP',
                                         'explanation': 'Severe features of preeclampsia include '
                                                        'neurologic symptoms (headache, visual '
                                                        'changes), right-upper-quadrant/epigastric '
                                                        'pain (hepatic capsule stretch), and '
                                                        'severe hypertension—harbingers of '
                                                        'eclampsia and organ injury. Mild '
                                                        'dependent edema alone is common and less '
                                                        'specific.',
                                         'choice_explanations': {'A': 'This symptom cluster '
                                                                      'signals severe features '
                                                                      'needing urgent evaluation '
                                                                      'and seizure precautions.',
                                                                 'B': 'Mild dependent edema alone '
                                                                      'is common in late pregnancy '
                                                                      'and not by itself a severe '
                                                                      'feature.',
                                                                 'C': 'Quickening is expected '
                                                                      'fetal movement, not a '
                                                                      'preeclampsia danger sign.',
                                                                 'D': 'Normal leukorrhea without '
                                                                      'infection signs is not a '
                                                                      'preeclampsia warning.'}},
                                        {'question': 'A nonstress test is reported as reactive. '
                                                     'What does this roughly indicate?',
                                         'options': ['A) Immediate cesarean is mandatory '
                                                     'regardless of other findings',
                                                     'B) Adequate fetal heart-rate accelerations '
                                                     'with movement, suggesting fetal well-being '
                                                     'in that window',
                                                     'C) Confirmed fetal demise',
                                                     'D) Need to stop all maternal oral intake '
                                                     'permanently'],
                                         'answer': 'B) Adequate fetal heart-rate accelerations '
                                                   'with movement, suggesting fetal well-being in '
                                                   'that window',
                                         'explanation': 'A reactive NST shows accelerations '
                                                        'associated with fetal movement, '
                                                        'reflecting intact autonomic and '
                                                        'oxygenation status during the test '
                                                        'period. It is reassuring but not an '
                                                        'automatic surgical indication, nor '
                                                        'evidence of demise.',
                                         'choice_explanations': {'A': 'Reactive NST is reassuring, '
                                                                      'not an automatic cesarean '
                                                                      'trigger.',
                                                                 'B': 'Accelerations with movement '
                                                                      'indicate fetal well-being '
                                                                      'during the testing window.',
                                                                 'C': 'Demise would lack a normal '
                                                                      'reactive pattern.',
                                                                 'D': 'NST result alone does not '
                                                                      'dictate lifelong NPO '
                                                                      'status.'}},
                                        {'question': 'Teaching for a breastfeeding parent with '
                                                     'mastitis should include which point?',
                                         'options': ['A) Abruptly stop breastfeeding on the '
                                                     'affected side permanently',
                                                     'B) Apply ice only and never empty the breast',
                                                     'C) Continue frequent emptying (feed/pump), '
                                                     'use comfort measures, and take antibiotics '
                                                     'if prescribed',
                                                     'D) Ignore fever because mastitis is always '
                                                     'self-limited without treatment'],
                                         'answer': 'C) Continue frequent emptying (feed/pump), use '
                                                   'comfort measures, and take antibiotics if '
                                                   'prescribed',
                                         'explanation': 'Mastitis management includes continued '
                                                        'milk removal, supportive care, and '
                                                        'antibiotics when indicated. Abrupt '
                                                        'weaning worsens engorgement and '
                                                        'infection; leaving milk stagnant promotes '
                                                        'bacterial growth.',
                                         'choice_explanations': {'A': 'Continued emptying aids '
                                                                      'resolution; abrupt '
                                                                      'cessation worsens stasis.',
                                                                 'B': 'Emptying is therapeutic; '
                                                                      'ice alone without removal '
                                                                      'is insufficient.',
                                                                 'C': 'Frequent emptying plus '
                                                                      'prescribed '
                                                                      'antibiotics/supportive care '
                                                                      'is standard teaching.',
                                                                 'D': 'Fever with mastitis often '
                                                                      'needs evaluation and '
                                                                      'possible antibiotics.'}}],
                             'hard': [{'question': 'During delivery, the head delivers but the '
                                                   'shoulders do not follow; the turtle sign is '
                                                   'present. Which nursing actions help the team '
                                                   'manage shoulder dystocia?',
                                       'options': ['A) Apply fundal pressure as the first and only '
                                                   'maneuver',
                                                   'B) Pull harder on the head without calling for '
                                                   'help',
                                                   'C) Have the mother stand and walk to deliver '
                                                   'the shoulders',
                                                   'D) Call for help, note the time, assist with '
                                                   'McRoberts/suprapubic pressure as directed, and '
                                                   'avoid fundal pressure'],
                                       'answer': 'D) Call for help, note the time, assist with '
                                                 'McRoberts/suprapubic pressure as directed, and '
                                                 'avoid fundal pressure',
                                       'explanation': 'Shoulder dystocia is an obstetric '
                                                      'emergency. Nurses activate help, track '
                                                      'time, and assist with McRoberts positioning '
                                                      'and suprapubic pressure. Fundal pressure '
                                                      'worsens impaction and is contraindicated; '
                                                      'forceful traction risks brachial plexus '
                                                      'injury.',
                                       'choice_explanations': {'A': 'Fundal pressure increases '
                                                                    'shoulder impaction and is '
                                                                    'contraindicated.',
                                                               'B': 'Excessive traction risks '
                                                                    'nerve injury; help and proper '
                                                                    'maneuvers are required.',
                                                               'C': 'Ambulation is impossible and '
                                                                    'unsafe mid-dystocia.',
                                                               'D': 'Help, timing, McRoberts, and '
                                                                    'suprapubic pressure are the '
                                                                    'correct assistive '
                                                                    'priorities.'}},
                                      {'question': 'A pregnant patient at 34 weeks has sudden dark '
                                                   'vaginal bleeding, rigid board-like abdomen, '
                                                   'and severe pain with fetal bradycardia. Which '
                                                   'condition fits this classic pattern?',
                                       'options': ['A) Placental abruption until proven otherwise',
                                                   'B) Bloody show of early latent labor only',
                                                   'C) Uncomplicated placenta previa with painless '
                                                   'bright bleeding exclusively',
                                                   'D) Normal Braxton Hicks with mucus plug only'],
                                       'answer': 'A) Placental abruption until proven otherwise',
                                       'explanation': 'Painful dark bleeding, uterine '
                                                      'rigidity/tenderness, and fetal distress '
                                                      'classic for abruption—premature placental '
                                                      'separation compromising maternal–fetal '
                                                      'perfusion. Previa is typically painless '
                                                      'bright bleeding; bloody show is lighter and '
                                                      'not associated with a board-like uterus.',
                                       'choice_explanations': {'A': 'Painful bleeding with a rigid '
                                                                    'uterus and fetal compromise '
                                                                    'is the abruption pattern.',
                                                               'B': 'Bloody show lacks board-like '
                                                                    'rigidity and severe fetal '
                                                                    'bradycardia of this degree.',
                                                               'C': 'Previa is usually painless; '
                                                                    'rigidity and severe pain '
                                                                    'point to abruption.',
                                                               'D': 'Braxton Hicks are '
                                                                    'intermittent tightenings '
                                                                    'without hemorrhage and fetal '
                                                                    'bradycardia.'}},
                                      {'question': 'How do postpartum blues typically differ from '
                                                   'postpartum depression in nursing assessment?',
                                       'options': ['A) Blues always include psychosis and require '
                                                   'immediate involuntary hold',
                                                   'B) Blues are transient tearfulness/mood '
                                                   'lability peaking early; depression is more '
                                                   'persistent with functional impairment',
                                                   'C) Depression never occurs after day 3, so '
                                                   'late symptoms can be ignored',
                                                   'D) Blues require lifelong antipsychotic '
                                                   'therapy by definition'],
                                       'answer': 'B) Blues are transient tearfulness/mood lability '
                                                 'peaking early; depression is more persistent '
                                                 'with functional impairment',
                                       'explanation': 'Postpartum blues are common, brief mood '
                                                      'swings in the first days. Postpartum '
                                                      'depression lasts longer, impairs function, '
                                                      'and may include hopelessness or suicidal '
                                                      'ideation needing treatment. Psychosis is a '
                                                      'separate emergency. Timing alone does not '
                                                      'make late symptoms safe to ignore.',
                                       'choice_explanations': {'A': 'Psychosis is not a feature of '
                                                                    'blues; it is a psychiatric '
                                                                    'emergency of its own.',
                                                               'B': 'Duration and functional '
                                                                    'impact distinguish blues from '
                                                                    'depression.',
                                                               'C': 'Depression can present later '
                                                                    'and must not be dismissed by '
                                                                    'calendar day.',
                                                               'D': 'Blues are self-limited and do '
                                                                    'not mandate '
                                                                    'antipsychotics.'}}],
                             'extreme': [{'question': 'Immediately after a generalized eclamptic '
                                                      'seizure, the patient is still pregnant at '
                                                      '37 weeks, SpO2 is 88% on room air, and the '
                                                      'uterus is contracting. Magnesium sulfate is '
                                                      'ordered but not yet started; a family '
                                                      'member demands immediate discharge against '
                                                      'advice. What is the nursing priority '
                                                      'sequence?',
                                          'options': ['A) Discharge home with oral acetaminophen '
                                                      'for headache',
                                                      'B) Begin oxytocin augmentation before '
                                                      'airway support',
                                                      'C) Protect airway/oxygenation, place in '
                                                      'lateral position, prevent injury, start '
                                                      'magnesium per protocol, and escalate '
                                                      'obstetric care',
                                                      'D) Withhold magnesium because seizures have '
                                                      'already occurred'],
                                          'answer': 'C) Protect airway/oxygenation, place in '
                                                    'lateral position, prevent injury, start '
                                                    'magnesium per protocol, and escalate '
                                                    'obstetric care',
                                          'explanation': 'Post-ictal eclampsia care prioritizes '
                                                         'airway, oxygenation, lateral '
                                                         'positioning, injury prevention, and '
                                                         'magnesium sulfate to prevent recurrent '
                                                         'seizures while preparing definitive '
                                                         'obstetric management. Discharge is '
                                                         'unsafe; magnesium is indicated after as '
                                                         'well as before seizures; oxytocin is not '
                                                         'the first step over ABCs.',
                                          'choice_explanations': {'A': 'Eclampsia requires '
                                                                       'inpatient stabilization, '
                                                                       'not discharge.',
                                                                  'B': 'Airway and seizure control '
                                                                       'precede labor augmentation '
                                                                       'decisions.',
                                                                  'C': 'ABC support plus magnesium '
                                                                       'and obstetric escalation '
                                                                       'is the evidence-based '
                                                                       'priority cluster.',
                                                                  'D': 'Magnesium remains '
                                                                       'first-line to prevent '
                                                                       'recurrent eclamptic '
                                                                       'seizures.'}},
                                         {'question': 'During labor, a multipara suddenly develops '
                                                      'dyspnea, hypotension, and DIC-range '
                                                      'bleeding from IV sites after membrane '
                                                      'rupture. The anesthetist suspects amniotic '
                                                      'fluid embolism. Fetal heart tracing shows '
                                                      'prolonged bradycardia. What should nursing '
                                                      'priorities emphasize?',
                                          'options': ['A) Encourage ambulation to improve venous '
                                                      'return',
                                                      'B) Give a full meal to prevent hypoglycemia',
                                                      'C) Focus only on collecting cord blood for '
                                                      'banking before calling help',
                                                      'D) Support ABCs/resuscitation, activate '
                                                      'massive hemorrhage/rapid response pathways, '
                                                      'and prepare for emergency delivery per '
                                                      'team'],
                                          'answer': 'D) Support ABCs/resuscitation, activate '
                                                    'massive hemorrhage/rapid response pathways, '
                                                    'and prepare for emergency delivery per team',
                                          'explanation': 'Amniotic fluid embolism presents with '
                                                         'sudden cardiorespiratory collapse and '
                                                         'coagulopathy. Survival depends on '
                                                         'aggressive airway/hemodynamic support, '
                                                         'hemorrhage resuscitation, and expedited '
                                                         'delivery when indicated—not ambulation, '
                                                         'feeding, or delaying help for '
                                                         'nonessential tasks.',
                                          'choice_explanations': {'A': 'Ambulation is impossible '
                                                                       'and harmful in shock/DIC.',
                                                                  'B': 'Oral intake is '
                                                                       'contraindicated in a '
                                                                       'crashing laboring patient.',
                                                                  'C': 'Cord banking must not '
                                                                       'delay maternal '
                                                                       'resuscitation.',
                                                                  'D': 'ABC support, hemorrhage '
                                                                       'activation, and readiness '
                                                                       'for emergency delivery '
                                                                       'address the multi-system '
                                                                       'crisis.'}},
                                         {'question': 'After a difficult third stage, a mass '
                                                      'protrudes at the introitus, the fundus '
                                                      'cannot be palpated abdominally, and '
                                                      'hemorrhage is heavy. A junior clinician '
                                                      'orders fundal oxytocin IM “into the uterus” '
                                                      'through the mass. What is the correct '
                                                      'recognition and response?',
                                          'options': ['A) Suspect uterine inversion; stop '
                                                      'inappropriate uterotonic into the inverted '
                                                      'fundus, support ABCs, and call for '
                                                      'immediate obstetric replacement help',
                                                      'B) Massage the protruding mass vigorously '
                                                      'as if it were a boggy fundus',
                                                      'C) Pull on the cord again to deliver more '
                                                      'placenta',
                                                      'D) Ignore bleeding because inversion is a '
                                                      'normal variant'],
                                          'answer': 'A) Suspect uterine inversion; stop '
                                                    'inappropriate uterotonic into the inverted '
                                                    'fundus, support ABCs, and call for immediate '
                                                    'obstetric replacement help',
                                          'explanation': 'Missing abdominal fundus with a vaginal '
                                                         'mass and hemorrhage indicates uterine '
                                                         'inversion—a rare hemorrhagic emergency. '
                                                         'Oxytocin into an inverted uterus before '
                                                         'replacement can tighten the cervix and '
                                                         'trap the uterus. Nurses support '
                                                         'resuscitation and emergent replacement '
                                                         'by the obstetric team; further traction '
                                                         'worsens inversion.',
                                          'choice_explanations': {'A': 'Recognition, withholding '
                                                                       'premature uterotonic into '
                                                                       'the inverted organ, and '
                                                                       'emergent help are correct.',
                                                                  'B': 'Massaging an inverted '
                                                                       'uterus is not standard '
                                                                       'atony massage and may '
                                                                       'worsen injury.',
                                                                  'C': 'Additional cord traction '
                                                                       'can deepen inversion.',
                                                                  'D': 'Inversion is a '
                                                                       'life-threatening '
                                                                       'emergency, not a normal '
                                                                       'variant.'}}]},
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
                                         'options': ['A) Giving false reassurance to end the '
                                                     'conversation quickly',
                                                     'B) Using empathy, open-ended questions, and '
                                                     'clarifying without judgment',
                                                     'C) Changing the subject whenever emotion '
                                                     'appears',
                                                     'D) Sharing detailed personal problems to '
                                                     'equalize roles'],
                                         'answer': 'B) Using empathy, open-ended questions, and '
                                                   'clarifying without judgment',
                                         'explanation': 'Therapeutic communication builds trust '
                                                        'through empathy, clarification, and '
                                                        'nonjudgmental exploration. False '
                                                        'reassurance, topic changes that shut down '
                                                        'feeling, and blurred boundaries undermine '
                                                        'the therapeutic alliance.',
                                         'choice_explanations': {'A': 'False reassurance dismisses '
                                                                      'emotion and blocks '
                                                                      'assessment of risk and '
                                                                      'meaning.',
                                                                 'B': 'Empathy and open '
                                                                      'clarification are core '
                                                                      'therapeutic communication '
                                                                      'skills.',
                                                                 'C': 'Avoiding emotion prevents '
                                                                      'understanding and alliance.',
                                                                 'D': 'Over-sharing personal '
                                                                      'problems shifts focus and '
                                                                      'blurs professional '
                                                                      'boundaries.'}},
                                        {'question': 'What must a suicide risk assessment '
                                                     'specifically explore beyond general sadness?',
                                         'options': ['A) Preferred cafeteria foods only',
                                                     'B) Favorite television shows this week',
                                                     'C) Ideation, plan, intent, means, and '
                                                     'protective factors',
                                                     'D) Only whether the patient smiles during '
                                                     'interview'],
                                         'answer': 'C) Ideation, plan, intent, means, and '
                                                   'protective factors',
                                         'explanation': 'Suicide assessment asks about ideation, '
                                                        'plan specificity, intent, access to '
                                                        'means, and protective factors. Surface '
                                                        'mood cues or unrelated preferences do not '
                                                        'quantify near-term risk.',
                                         'choice_explanations': {'A': 'Food preference is '
                                                                      'unrelated to suicide risk '
                                                                      'stratification.',
                                                                 'B': 'Media preferences do not '
                                                                      'replace plan/intent/means '
                                                                      'assessment.',
                                                                 'C': 'Ideation–plan–intent–means '
                                                                      'plus protectors is the '
                                                                      'required risk framework.',
                                                                 'D': 'Affect alone is an '
                                                                      'unreliable indicator of '
                                                                      'suicide risk.'}},
                                        {'question': 'Which early side-effect theme is commonly '
                                                     'taught for SSRIs in the first weeks?',
                                         'options': ['A) Immediate complete remission of all '
                                                     'symptoms by day one',
                                                     'B) Guaranteed absence of any sexual or GI '
                                                     'effects',
                                                     'C) Need to stop the drug after one dose if '
                                                     'mood is unchanged',
                                                     'D) Possible GI upset, headache, sleep '
                                                     'change, and transient anxiety/activation'],
                                         'answer': 'D) Possible GI upset, headache, sleep change, '
                                                   'and transient anxiety/activation',
                                         'explanation': 'SSRIs often cause early GI symptoms, '
                                                        'headache, sleep disturbance, and '
                                                        'sometimes activation before '
                                                        'antidepressant benefit emerges over '
                                                        'weeks. Patients need anticipatory '
                                                        'guidance rather than expecting instant '
                                                        'cure or stopping prematurely without '
                                                        'clinical advice.',
                                         'choice_explanations': {'A': 'Therapeutic effect is '
                                                                      'delayed; day-one remission '
                                                                      'is not expected.',
                                                                 'B': 'Sexual and GI effects are '
                                                                      'relatively common and '
                                                                      'should be discussed.',
                                                                 'C': 'Stopping after one '
                                                                      'unchanged-mood dose ignores '
                                                                      'expected latency of '
                                                                      'benefit.',
                                                                 'D': 'Early somatic/activation '
                                                                      'effects are the common '
                                                                      'teaching points for SSRI '
                                                                      'initiation.'}}],
                               'medium': [{'question': 'A patient on lithium develops nausea, '
                                                       'vomiting, diarrhea, and coarse tremor '
                                                       'after a viral illness with poor intake. '
                                                       'What should the nurse suspect?',
                                           'options': ['A) Possible lithium toxicity precipitated '
                                                       'by volume depletion; hold dose and '
                                                       'escalate',
                                                       'B) Normal lithium effect that always '
                                                       'includes coarse tremor and vomiting',
                                                       'C) Need to double the next lithium dose to '
                                                       '“catch up”',
                                                       'D) Allergic rhinitis unrelated to lithium '
                                                       'levels'],
                                           'answer': 'A) Possible lithium toxicity precipitated by '
                                                     'volume depletion; hold dose and escalate',
                                           'explanation': 'Dehydration and sodium loss reduce '
                                                          'lithium clearance and raise levels. GI '
                                                          'losses plus coarse tremor are toxicity '
                                                          'cues. The dose should be held pending '
                                                          'levels and medical evaluation—not '
                                                          'increased.',
                                           'choice_explanations': {'A': 'Illness-related volume '
                                                                        'loss with GI symptoms and '
                                                                        'coarse tremor suggests '
                                                                        'toxicity needing hold and '
                                                                        'escalation.',
                                                                   'B': 'Coarse tremor with '
                                                                        'vomiting is not a benign '
                                                                        '“normal” effect.',
                                                                   'C': 'Doubling the dose worsens '
                                                                        'potential toxicity.',
                                                                   'D': 'These symptoms align with '
                                                                        'lithium toxicity, not '
                                                                        'rhinitis.'}},
                                          {'question': 'Which complication is a major nursing '
                                                       'surveillance priority in acute alcohol '
                                                       'withdrawal?',
                                           'options': ['A) Guaranteed absence of autonomic '
                                                       'hyperactivity',
                                                       'B) Seizures and delirium tremens with '
                                                       'autonomic instability',
                                                       'C) Only mild thirst without vital-sign '
                                                       'changes',
                                                       'D) Immediate lifelong immunity to alcohol '
                                                       'after one detox'],
                                           'answer': 'B) Seizures and delirium tremens with '
                                                     'autonomic instability',
                                           'explanation': 'Alcohol withdrawal can progress to '
                                                          'seizures and DTs with tachycardia, '
                                                          'hypertension, fever, and altered '
                                                          'mentation. Nurses use protocols (e.g., '
                                                          'CIWA), seizure precautions, and ordered '
                                                          'benzodiazepines. Detox does not confer '
                                                          'immunity to future use.',
                                           'choice_explanations': {'A': 'Autonomic hyperactivity '
                                                                        'is common in withdrawal, '
                                                                        'not absent.',
                                                                   'B': 'Seizures and DTs are the '
                                                                        'high-morbidity '
                                                                        'complications requiring '
                                                                        'vigilance.',
                                                                   'C': 'Mild thirst understates '
                                                                        'the risk of severe '
                                                                        'withdrawal.',
                                                                   'D': 'Detox does not create '
                                                                        'lasting immunity to '
                                                                        'alcohol use disorder.'}},
                                          {'question': 'A patient with schizophrenia says, “The '
                                                       'voices tell me the food is poisoned.” What '
                                                       'is the best initial nursing response '
                                                       'theme?',
                                           'options': ['A) Argue that the voices are imaginary '
                                                       'until the patient agrees',
                                                       'B) Laugh to show the idea is silly',
                                                       'C) Acknowledge the experience, reinforce '
                                                       'reality gently, and assess safety without '
                                                       'debating the delusion as a fact contest',
                                                       'D) Agree the food is poisoned and discard '
                                                       'all unit meals'],
                                           'answer': 'C) Acknowledge the experience, reinforce '
                                                     'reality gently, and assess safety without '
                                                     'debating the delusion as a fact contest',
                                           'explanation': 'Therapeutic responses acknowledge the '
                                                          'patient’s perceptual experience, avoid '
                                                          'hostile confrontation of fixed '
                                                          'delusions, reinforce reality, and '
                                                          'assess for command '
                                                          'hallucinations/safety. Colluding with '
                                                          'the delusion or ridicule damages trust '
                                                          'and assessment.',
                                           'choice_explanations': {'A': 'Arguing rarely '
                                                                        'extinguishes delusions '
                                                                        'and increases agitation.',
                                                                   'B': 'Ridicule shames the '
                                                                        'patient and ruptures '
                                                                        'alliance.',
                                                                   'C': 'Acknowledgment plus '
                                                                        'gentle reality '
                                                                        'orientation and safety '
                                                                        'assessment is best '
                                                                        'practice.',
                                                                   'D': 'Agreeing with the '
                                                                        'delusion reinforces false '
                                                                        'belief and disrupts '
                                                                        'nutrition care.'}}],
                               'hard': [{'question': 'A patient on a high-potency antipsychotic '
                                                     'develops lead-pipe rigidity, very high '
                                                     'fever, and fluctuating consciousness. '
                                                     'Another patient on an SSRI plus tramadol is '
                                                     'agitated, hyperreflexic, and '
                                                     'clonus-positive. Which clue themes correctly '
                                                     'separate NMS from serotonin syndrome?',
                                         'options': ['A) Both are identical and treated with the '
                                                     'same first antidote always',
                                                     'B) NMS is always caused by SSRIs; serotonin '
                                                     'syndrome is always caused by haloperidol '
                                                     'alone',
                                                     'C) Fever never occurs in either syndrome',
                                                     'D) NMS: rigidity/bradyreflexia after '
                                                     'antipsychotics; serotonin syndrome: '
                                                     'hyperreflexia/clonus after serotonergic '
                                                     'drugs'],
                                         'answer': 'D) NMS: rigidity/bradyreflexia after '
                                                   'antipsychotics; serotonin syndrome: '
                                                   'hyperreflexia/clonus after serotonergic drugs',
                                         'explanation': 'NMS is an antipsychotic-related '
                                                        'idiosyncratic reaction with severe '
                                                        'rigidity and hyporeflexia. Serotonin '
                                                        'syndrome from serotonergic agents '
                                                        'features hyperreflexia and clonus. '
                                                        'Distinguishing guides whether to stop '
                                                        'antipsychotics/cool/support vs stop '
                                                        'serotonergic agents and manage '
                                                        'neuromuscular irritability.',
                                         'choice_explanations': {'A': 'Mechanisms and exam clues '
                                                                      'differ; treatments are not '
                                                                      'identical.',
                                                                 'B': 'NMS links to '
                                                                      'antipsychotics; serotonin '
                                                                      'syndrome to serotonergic '
                                                                      'combinations—roles reversed '
                                                                      'here are wrong.',
                                                                 'C': 'Fever can occur in both and '
                                                                      'is clinically important.',
                                                                 'D': 'Rigidity vs '
                                                                      'hyperreflexia/clonus plus '
                                                                      'drug class correctly '
                                                                      'differentiates NMS from '
                                                                      'serotonin syndrome.'}},
                                        {'question': 'Which situation best meets typical criteria '
                                                     'themes for emergency involuntary psychiatric '
                                                     'hold?',
                                         'options': ['A) Imminent danger to self/others or grave '
                                                     'disability from mental illness when the '
                                                     'person refuses voluntary safe care',
                                                     'B) Family embarrassment about a diagnosis '
                                                     'without safety risk',
                                                     'C) Missed outpatient appointment alone',
                                                     'D) Patient request for elective career '
                                                     'counseling'],
                                         'answer': 'A) Imminent danger to self/others or grave '
                                                   'disability from mental illness when the person '
                                                   'refuses voluntary safe care',
                                         'explanation': 'Involuntary holds are justified when '
                                                        'mental illness produces imminent risk of '
                                                        'harm to self/others or inability to meet '
                                                        'basic needs, and less restrictive '
                                                        'voluntary options are not feasible. '
                                                        'Embarrassment, missed appointments, or '
                                                        'elective counseling do not meet hold '
                                                        'criteria.',
                                         'choice_explanations': {'A': 'Danger or grave disability '
                                                                      'with refusal of voluntary '
                                                                      'safe care is the classic '
                                                                      'hold threshold theme.',
                                                                 'B': 'Family discomfort without '
                                                                      'safety risk is not a legal '
                                                                      'hold criterion.',
                                                                 'C': 'Missed appointments need '
                                                                      'outreach, not automatic '
                                                                      'involuntary confinement.',
                                                                 'D': 'Career counseling is not an '
                                                                      'emergency detention '
                                                                      'indication.'}},
                                        {'question': 'Why does clozapine require unique '
                                                     'nursing/pharmacy monitoring compared with '
                                                     'many other antipsychotics?',
                                         'options': ['A) It never causes metabolic effects, so no '
                                                     'labs are needed',
                                                     'B) Risk of agranulocytosis/neutropenia '
                                                     'requiring scheduled absolute neutrophil '
                                                     'count monitoring',
                                                     'C) It is available only as a one-time '
                                                     'lifetime dose',
                                                     'D) It has no cholinergic or seizure-risk '
                                                     'considerations'],
                                         'answer': 'B) Risk of agranulocytosis/neutropenia '
                                                   'requiring scheduled absolute neutrophil count '
                                                   'monitoring',
                                         'explanation': 'Clozapine’s boxed risk of severe '
                                                        'neutropenia mandates REMS-style ANC '
                                                        'monitoring before and during therapy. It '
                                                        'also carries metabolic, myocarditis, '
                                                        'seizure, and sialorrhea risks—so “no labs '
                                                        'needed” is false.',
                                         'choice_explanations': {'A': 'Clozapine has significant '
                                                                      'metabolic and hematologic '
                                                                      'risks requiring monitoring.',
                                                                 'B': 'ANC monitoring for '
                                                                      'agranulocytosis risk is the '
                                                                      'distinctive safety '
                                                                      'requirement.',
                                                                 'C': 'Clozapine is ongoing '
                                                                      'therapy, not a single '
                                                                      'lifetime dose.',
                                                                 'D': 'Seizure risk and other '
                                                                      'adverse effects are '
                                                                      'clinically relevant.'}}],
                               'extreme': [{'question': 'On a locked unit, a patient is found in '
                                                        'the bathroom with a sheet ligature around '
                                                        'the neck, cyanotic but with a weak pulse. '
                                                        'Another patient is yelling for PRN '
                                                        'lorazepam at the desk, and a new '
                                                        'admission needs orientation. What is your '
                                                        'immediate priority?',
                                            'options': ['A) Finish the new-admission tour before '
                                                        'returning to the bathroom',
                                                        'B) Bring oral lorazepam to the yelling '
                                                        'patient first to restore unit calm',
                                                        'C) Call for help, release the ligature, '
                                                        'initiate rescue breathing/CPR as needed, '
                                                        'and secure the environment',
                                                        'D) Leave the patient to find the paper '
                                                        'incident form before intervening'],
                                            'answer': 'C) Call for help, release the ligature, '
                                                      'initiate rescue breathing/CPR as needed, '
                                                      'and secure the environment',
                                            'explanation': 'An active hanging/ligature attempt is '
                                                           'an airway and circulatory emergency. '
                                                           'Simultaneous help, ligature release, '
                                                           'and BLS take absolute priority over '
                                                           'admissions and PRN requests. '
                                                           'Documentation follows stabilization.',
                                            'choice_explanations': {'A': 'Orientation tasks never '
                                                                         'outrank an active '
                                                                         'asphyxiation emergency.',
                                                                    'B': 'Agitation at the desk is '
                                                                         'secondary to a cyanotic '
                                                                         'ligature victim.',
                                                                    'C': 'Help, airway rescue, and '
                                                                         'environmental security '
                                                                         'are the immediate '
                                                                         'life-saving sequence.',
                                                                    'D': 'Forms cannot restore '
                                                                         'oxygenation; intervene '
                                                                         'first.'}},
                                           {'question': 'A visitor becomes violent, brandishes a '
                                                        'knife, and blocks the exit while '
                                                        'demanding a patient’s discharge. Staff '
                                                        'personal alarms are available; the '
                                                        'patient is hiding in the bathroom. What '
                                                        'is the correct priority?',
                                            'options': ['A) Attempt to physically disarm the '
                                                        'visitor alone to show confidence',
                                                        'B) Negotiate discharge paperwork under '
                                                        'threat to “de-escalate”',
                                                        'C) Ignore the weapon and continue '
                                                        'medication pass in the hallway',
                                                        'D) Ensure staff/patient safety: activate '
                                                        'emergency security response, '
                                                        'evacuate/shelter others, and do not '
                                                        'approach the weapon alone'],
                                            'answer': 'D) Ensure staff/patient safety: activate '
                                                      'emergency security response, '
                                                      'evacuate/shelter others, and do not '
                                                      'approach the weapon alone',
                                            'explanation': 'Weaponized violence is a '
                                                           'security/law-enforcement emergency. '
                                                           'Priorities are protecting patients and '
                                                           'staff, activating trained responders, '
                                                           'and avoiding lone disarmament. '
                                                           'Capitulating to threats or continuing '
                                                           'routine care in the strike zone '
                                                           'increases casualties.',
                                            'choice_explanations': {'A': 'Lone disarmament of a '
                                                                         'knife-wielding person '
                                                                         'risks severe injury.',
                                                                    'B': 'Clinical decisions under '
                                                                         'threat are coerced and '
                                                                         'unsafe.',
                                                                    'C': 'Continuing hallway care '
                                                                         'exposes more people to '
                                                                         'the weapon.',
                                                                    'D': 'Emergency activation, '
                                                                         'shelter/evacuation, and '
                                                                         'avoiding solo '
                                                                         'confrontation are '
                                                                         'correct.'}},
                                           {'question': 'A patient on high-dose haloperidol '
                                                        'develops temperature 41°C, lead-pipe '
                                                        'rigidity, BP instability, and rising CK. '
                                                        'The covering provider texts “give another '
                                                        'IM haloperidol for agitation.” What '
                                                        'should you do?',
                                            'options': ['A) Hold further antipsychotics, support '
                                                        'ABCs/cooling, notify the provider of '
                                                        'suspected NMS, and seek urgent medical '
                                                        'treatment',
                                                        'B) Give the additional IM haloperidol as '
                                                        'texted without assessment',
                                                        'C) Cover with heavy blankets to “sweat '
                                                        'out” the fever',
                                                        'D) Force ambulation to loosen the '
                                                        'rigidity'],
                                            'answer': 'A) Hold further antipsychotics, support '
                                                      'ABCs/cooling, notify the provider of '
                                                      'suspected NMS, and seek urgent medical '
                                                      'treatment',
                                            'explanation': 'This presentation is classic '
                                                           'neuroleptic malignant syndrome. '
                                                           'Continuing dopamine blockade worsens '
                                                           'the syndrome. Nurses hold '
                                                           'antipsychotics, escalate, and support '
                                                           'airway, circulation, and cooling while '
                                                           'definitive care (e.g., ICU, possible '
                                                           'dantrolene/bromocriptine per protocol) '
                                                           'is arranged.',
                                            'choice_explanations': {'A': 'Holding antipsychotics '
                                                                         'and urgent '
                                                                         'supportive/medical '
                                                                         'escalation is the '
                                                                         'correct NMS response.',
                                                                    'B': 'More haloperidol '
                                                                         'intensifies NMS.',
                                                                    'C': 'Heavy bundling impairs '
                                                                         'heat loss in '
                                                                         'life-threatening '
                                                                         'hyperthermia.',
                                                                    'D': 'Forced ambulation is '
                                                                         'unsafe with severe '
                                                                         'rigidity and autonomic '
                                                                         'instability.'}}]},
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
                                                   'C) Insulin teaching after diabetes diagnosis',
                                                   'D) Hospice care for terminal cancer'],
                                       'answer': 'B) Community influenza immunization before flu '
                                                 'season',
                                       'explanation': 'Primary prevention averts disease before '
                                                      'onset—immunization is classic. Rehab after '
                                                      'MI and insulin teaching after diagnosis are '
                                                      'secondary/tertiary; hospice is '
                                                      'tertiary/comfort care.',
                                       'choice_explanations': {'A': 'Post-MI rehab prevents '
                                                                    'complications of existing '
                                                                    'disease (tertiary).',
                                                               'B': 'Vaccination before exposure '
                                                                    'prevents disease onset '
                                                                    '(primary).',
                                                               'C': 'Teaching after diagnosis '
                                                                    'manages existing disease.',
                                                               'D': 'Hospice addresses advanced '
                                                                    'disease, not primary '
                                                                    'prevention.'}},
                                      {'question': 'Which activity best exemplifies secondary '
                                                   'prevention?',
                                       'options': ['A) Building safe bike lanes citywide',
                                                   'B) Seat-belt legislation campaigns only',
                                                   'C) Blood-pressure screening to detect '
                                                   'hypertension early',
                                                   'D) Long-term stroke rehabilitation therapy'],
                                       'answer': 'C) Blood-pressure screening to detect '
                                                 'hypertension early',
                                       'explanation': 'Secondary prevention detects disease early '
                                                      'through screening so treatment can begin '
                                                      'before advanced complications. '
                                                      'Environmental safety laws are primary; '
                                                      'rehabilitation after stroke is tertiary.',
                                       'choice_explanations': {'A': 'Bike-lane engineering is '
                                                                    'primary prevention of injury.',
                                                               'B': 'Seat-belt campaigns primarily '
                                                                    'prevent injury '
                                                                    'occurrence/severity at the '
                                                                    'primary level.',
                                                               'C': 'BP screening finds '
                                                                    'asymptomatic hypertension '
                                                                    'early—secondary prevention.',
                                                               'D': 'Rehab after stroke is '
                                                                    'tertiary prevention.'}},
                                      {'question': 'Herd immunity most directly relates to which '
                                                   'public-health concept?',
                                       'options': ['A) Individual hand preference in a population',
                                                   'B) Hospital bed count alone without '
                                                   'transmission dynamics',
                                                   'C) Only vector control without vaccines',
                                                   'D) Indirect protection of susceptible persons '
                                                   'when enough of the population is immune'],
                                       'answer': 'D) Indirect protection of susceptible persons '
                                                 'when enough of the population is immune',
                                       'explanation': 'Herd immunity occurs when sufficient '
                                                      'population immunity (often via vaccination) '
                                                      'lowers transmission enough to protect those '
                                                      'who remain susceptible. It is a '
                                                      'transmission-dynamics concept, not bed '
                                                      'inventory or handedness.',
                                       'choice_explanations': {'A': 'Handedness is unrelated to '
                                                                    'infectious herd effects.',
                                                               'B': 'Bed capacity does not define '
                                                                    'herd immunity.',
                                                               'C': 'Vector control helps some '
                                                                    'diseases but is not the '
                                                                    'definition of herd immunity.',
                                                               'D': 'Indirect protection via high '
                                                                    'population immunity is the '
                                                                    'herd-immunity concept.'}}],
                             'medium': [{'question': 'Which factors are included among social '
                                                     'determinants of health that community nurses '
                                                     'assess?',
                                         'options': ['A) Housing, education, income, food access, '
                                                     'and neighborhood safety',
                                                     'B) Only genetic polymorphisms with no '
                                                     'environmental context',
                                                     'C) Favorite sports team affiliation alone',
                                                     'D) Shoe brand preference as the main health '
                                                     'driver'],
                                         'answer': 'A) Housing, education, income, food access, '
                                                   'and neighborhood safety',
                                         'explanation': 'Social determinants—conditions in which '
                                                        'people live, learn, work, and '
                                                        'age—strongly shape health outcomes. '
                                                        'Housing, education, income, food, and '
                                                        'safety are core domains; consumer '
                                                        'preferences and genes alone do not '
                                                        'capture this framework.',
                                         'choice_explanations': {'A': 'These structural living '
                                                                      'conditions are classic '
                                                                      'social determinants nurses '
                                                                      'assess in community '
                                                                      'practice.',
                                                                 'B': 'Genetics matter but do not '
                                                                      'replace '
                                                                      'social-environmental '
                                                                      'determinants.',
                                                                 'C': 'Sports fandom is not a '
                                                                      'standard SDOH domain.',
                                                                 'D': 'Brand preference is not a '
                                                                      'primary SDOH construct.'}},
                                        {'question': 'A client with pulmonary tuberculosis needs '
                                                     'community/home isolation teaching. Which '
                                                     'precaution theme is required for infectious '
                                                     'TB?',
                                         'options': ['A) Contact gown only without respiratory '
                                                     'protection considerations',
                                                     'B) Airborne precautions with appropriate '
                                                     'respirator use and ventilation guidance',
                                                     'C) Droplet surgical mask only for all TB '
                                                     'forms without assessment',
                                                     'D) No precautions once the client feels '
                                                     'subjectively better for one hour'],
                                         'answer': 'B) Airborne precautions with appropriate '
                                                   'respirator use and ventilation guidance',
                                         'explanation': 'Infectious pulmonary TB requires airborne '
                                                        'precautions—N95/respirator use by '
                                                        'caregivers and ventilation/isolation '
                                                        'strategies—until noninfectious criteria '
                                                        'are met. Feeling better briefly does not '
                                                        'clear transmissibility.',
                                         'choice_explanations': {'A': 'Contact barriers alone do '
                                                                      'not stop airborne droplet '
                                                                      'nuclei.',
                                                                 'B': 'Airborne precautions with '
                                                                      'respirators/ventilation are '
                                                                      'required for infectious '
                                                                      'pulmonary TB.',
                                                                 'C': 'Standard surgical masks are '
                                                                      'insufficient for airborne '
                                                                      'TB nuclei in many care '
                                                                      'settings.',
                                                                 'D': 'Subjective improvement does '
                                                                      'not equal noninfectious '
                                                                      'status.'}},
                                        {'question': 'Before a home health visit in an unfamiliar '
                                                     'neighborhood, which safety practice should '
                                                     'the nurse include?',
                                         'options': ['A) Keep visit plans secret from the agency '
                                                     'so nobody knows the location',
                                                     'B) Enter immediately if yelling is heard, '
                                                     'without calling for backup',
                                                     'C) Share schedule with the agency, carry a '
                                                     'charged phone, assess exit routes, and leave '
                                                     'if the environment is unsafe',
                                                     'D) Leave valuables visible in the car to '
                                                     'retrieve later during the visit'],
                                         'answer': 'C) Share schedule with the agency, carry a '
                                                   'charged phone, assess exit routes, and leave '
                                                   'if the environment is unsafe',
                                         'explanation': 'Home-visit safety includes agency '
                                                        'awareness of schedule/location, '
                                                        'communication devices, environmental '
                                                        'scanning, and willingness to leave when '
                                                        'threatened. Secrecy, reckless entry into '
                                                        'violence, and visible valuables increase '
                                                        'risk.',
                                         'choice_explanations': {'A': 'The agency must know '
                                                                      'location/timing for '
                                                                      'check-in and emergency '
                                                                      'response.',
                                                                 'B': 'Entering an active violent '
                                                                      'scene alone is unsafe.',
                                                                 'C': 'Communication, exit '
                                                                      'planning, and leaving when '
                                                                      'unsafe are core home-visit '
                                                                      'safety practices.',
                                                                 'D': 'Visible valuables invite '
                                                                      'theft and delay egress.'}}],
                             'hard': [{'question': 'What does “upstream thinking” mean when a '
                                                   'community nurse plans interventions for '
                                                   'childhood asthma hospitalizations?',
                                       'options': ['A) Focus only on rescue inhalers after each '
                                                   'ICU admission',
                                                   'B) Limit care to charting readmission rates '
                                                   'without action',
                                                   'C) Treat only the last child who was intubated',
                                                   'D) Address root causes such as housing mold, '
                                                   'air quality, and access to controller therapy '
                                                   'before crises'],
                                       'answer': 'D) Address root causes such as housing mold, air '
                                                 'quality, and access to controller therapy before '
                                                 'crises',
                                       'explanation': 'Upstream approaches modify social and '
                                                      'environmental root causes that generate '
                                                      'disease burden, rather than only responding '
                                                      'after acute decompensation. For asthma, '
                                                      'housing quality, triggers, and controller '
                                                      'access are upstream levers.',
                                       'choice_explanations': {'A': 'Rescue-only focus is '
                                                                    'downstream crisis care.',
                                                               'B': 'Measurement without '
                                                                    'intervention does not change '
                                                                    'outcomes.',
                                                               'C': 'Caring for one severe case '
                                                                    'alone ignores population '
                                                                    'drivers.',
                                                               'D': 'Root-cause environmental and '
                                                                    'access interventions '
                                                                    'exemplify upstream '
                                                                    'thinking.'}},
                                      {'question': 'In a mass-casualty incident using START '
                                                   'triage, which principle guides tagging?',
                                       'options': ['A) Expectant/minor/delayed/immediate '
                                                   'categories based on respiration, perfusion, '
                                                   'and mentation—not first-come-first-served',
                                                   'B) Treat VIP adults before all children '
                                                   'regardless of injuries',
                                                   'C) Ignore airway because scene care is only '
                                                   'for fractures',
                                                   'D) Spend unlimited time on each victim before '
                                                   'moving on'],
                                       'answer': 'A) Expectant/minor/delayed/immediate categories '
                                                 'based on respiration, perfusion, and '
                                                 'mentation—not first-come-first-served',
                                       'explanation': 'START triage rapidly sorts victims by '
                                                      'simple physiologic cues into immediate, '
                                                      'delayed, minor, or expectant categories to '
                                                      'do the greatest good for the greatest '
                                                      'number. Social status and unlimited '
                                                      'one-patient focus violate MCI ethics.',
                                       'choice_explanations': {'A': 'Physiologic '
                                                                    'categorization—not arrival '
                                                                    'order—defines START.',
                                                               'B': 'VIP status is not a START '
                                                                    'criterion.',
                                                               'C': 'Respiration/airway is a core '
                                                                    'START assessment node.',
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
                                                   'D) Document nothing about the conversation'],
                                       'answer': 'B) Use motivational, respectful dialogue; '
                                                 'address specific concerns with evidence; and '
                                                 'keep the door open for future acceptance',
                                       'explanation': 'Vaccine hesitancy responds best to '
                                                      'nonjudgmental listening, tailored evidence, '
                                                      'and relationship continuity. Ridicule and '
                                                      'care refusal deepen mistrust; undocumented '
                                                      'counseling misses a safety and legal '
                                                      'record.',
                                       'choice_explanations': {'A': 'Mockery increases resistance '
                                                                    'and damages alliance.',
                                                               'B': 'Respectful, concern-specific '
                                                                    'counseling with ongoing '
                                                                    'engagement is best practice.',
                                                               'C': 'Withholding unrelated '
                                                                    'essential care is unethical '
                                                                    'coercion.',
                                                               'D': 'Counseling and refusal must '
                                                                    'be documented.'}}],
                             'extreme': [{'question': 'Several postal workers from one facility '
                                                      'present with fever, cough, and mediastinal '
                                                      'widening on chest imaging after handling '
                                                      'dusty mail. Media are calling; a supervisor '
                                                      'wants them sent home with azithromycin '
                                                      'only. What should the public-health nursing '
                                                      'response prioritize?',
                                          'options': ['A) Reassure media that bacterial pneumonia '
                                                      'is always community MRSA',
                                                      'B) Send everyone home without reporting '
                                                      'because publicity is inconvenient',
                                                      'C) Treat as possible inhalational '
                                                      'anthrax/bioterror cluster: urgent '
                                                      'public-health notification, isolation/PPE '
                                                      'guidance, and coordinated '
                                                      'prophylaxis/treatment pathways',
                                                      'D) Start airborne measles precautions only '
                                                      'and stop investigation'],
                                          'answer': 'C) Treat as possible inhalational '
                                                    'anthrax/bioterror cluster: urgent '
                                                    'public-health notification, isolation/PPE '
                                                    'guidance, and coordinated '
                                                    'prophylaxis/treatment pathways',
                                          'explanation': 'Occupational cluster with mediastinal '
                                                         'widening after mail exposure raises '
                                                         'inhalational anthrax/bioterror concern. '
                                                         'Nurses escalate to public health, use '
                                                         'appropriate PPE, and follow '
                                                         'chemoprophylaxis/treatment protocols—not '
                                                         'casual discharge or wrong-pathogen '
                                                         'assumptions.',
                                          'choice_explanations': {'A': 'Mediastinal widening in '
                                                                       'this context is a classic '
                                                                       'anthrax clue, not routine '
                                                                       'MRSA pneumonia messaging.',
                                                                  'B': 'Failure to report a '
                                                                       'potential bioterror '
                                                                       'cluster endangers the '
                                                                       'community.',
                                                                  'C': 'Notification, PPE, and '
                                                                       'coordinated anthrax '
                                                                       'pathways are the correct '
                                                                       'multi-agency response.',
                                                                  'D': 'Measles precautions alone '
                                                                       'miss anthrax evaluation '
                                                                       'and prophylaxis needs.'}},
                                         {'question': 'After a needlestick from an unknown-source '
                                                      'needle in a community clinic, bleeding is '
                                                      'encouraged at the site and soap-and-water '
                                                      'washing is done. The source patient left '
                                                      'without labs. What is the correct next '
                                                      'priority cluster?',
                                          'options': ['A) Ignore the injury if the wound looks '
                                                      'small',
                                                      'B) Apply a tight arterial tourniquet for 6 '
                                                      'hours',
                                                      'C) Finish the shift without reporting to '
                                                      'avoid paperwork',
                                                      'D) Report immediately, seek urgent '
                                                      'employee-health/ED evaluation for baseline '
                                                      'labs and possible post-exposure prophylaxis '
                                                      'timing'],
                                          'answer': 'D) Report immediately, seek urgent '
                                                    'employee-health/ED evaluation for baseline '
                                                    'labs and possible post-exposure prophylaxis '
                                                    'timing',
                                          'explanation': 'Bloodborne pathogen exposures require '
                                                         'immediate reporting and timely risk '
                                                         'assessment for HIV/HBV/HCV PEP '
                                                         'decisions. First aid is necessary but '
                                                         'not sufficient; tourniquets and '
                                                         'nonreporting increase harm.',
                                          'choice_explanations': {'A': 'Wound size does not '
                                                                       'eliminate bloodborne '
                                                                       'infection risk.',
                                                                  'B': 'Prolonged tourniquets '
                                                                       'cause ischemic injury and '
                                                                       'are not exposure first '
                                                                       'aid.',
                                                                  'C': 'Delayed reporting can miss '
                                                                       'PEP windows.',
                                                                  'D': 'Immediate report plus '
                                                                       'urgent PEP/lab evaluation '
                                                                       'is required after '
                                                                       'unknown-source '
                                                                       'needlestick.'}},
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
                                                      'B) Quarantine and isolation are identical '
                                                      'legal terms with no difference',
                                                      'C) Isolation applies only to plants; '
                                                      'quarantine only to animals',
                                                      'D) Neither strategy is ever used in '
                                                      'outbreak control'],
                                          'answer': 'A) Isolation separates people with contagious '
                                                    'infection; quarantine restricts exposed well '
                                                    'persons who may become infectious',
                                          'explanation': 'Isolation restricts known infectious '
                                                         'cases; quarantine restricts exposed '
                                                         'susceptible persons during incubation. '
                                                         'Accurate terminology guides who stays '
                                                         'home, who needs airborne rooms, and '
                                                         'occupational restrictions—especially for '
                                                         'nonimmune pregnant staff after measles '
                                                         'exposure.',
                                          'choice_explanations': {'A': 'This is the correct '
                                                                       'operational distinction '
                                                                       'used in outbreak control.',
                                                                  'B': 'Conflating the terms '
                                                                       'causes incorrect '
                                                                       'restrictions and '
                                                                       'messaging.',
                                                                  'C': 'Both apply to human '
                                                                       'public-health practice.',
                                                                  'D': 'Both are foundational '
                                                                       'outbreak tools.'}}]},
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
                                           'options': ['A) Always keep SpO2 at exactly 100% with '
                                                       'maximal FiO2',
                                                       'B) Approximately 94–98% (or per ordered '
                                                       'disease-specific targets)',
                                                       'C) SpO2 of 70% is acceptable if the '
                                                       'patient is talking',
                                                       'D) Oxygen saturation goals are never '
                                                       'individualized'],
                                           'answer': 'B) Approximately 94–98% (or per ordered '
                                                     'disease-specific targets)',
                                           'explanation': 'Many guidelines target roughly 94–98% '
                                                          'for acutely ill adults, with lower '
                                                          'targets (e.g., 88–92%) for some COPD '
                                                          'patients. Forcing 100% with excess '
                                                          'oxygen can be harmful; 70% is unsafe.',
                                           'choice_explanations': {'A': 'Unnecessary hyperoxia can '
                                                                        'cause harm; 100% is not a '
                                                                        'universal goal.',
                                                                   'B': '≈94–98% (or ordered '
                                                                        'disease-specific ranges) '
                                                                        'is a common adult target '
                                                                        'theme.',
                                                                   'C': 'SpO2 70% indicates '
                                                                        'critical hypoxemia.',
                                                                   'D': 'Targets are often '
                                                                        'individualized (e.g., '
                                                                        'COPD).'}},
                                          {'question': 'Where is an arterial line typically '
                                                       'zeroed/leveled for accurate pressure '
                                                       'monitoring?',
                                           'options': ['A) At the patient’s knee regardless of '
                                                       'position',
                                                       'B) At the IV fluid bag spike',
                                                       'C) At the phlebostatic axis (approx. 4th '
                                                       'ICS, midaxillary line)',
                                                       'D) At the top of the ventilator circuit '
                                                       'only'],
                                           'answer': 'C) At the phlebostatic axis (approx. 4th '
                                                     'ICS, midaxillary line)',
                                           'explanation': 'Leveling the transducer at the '
                                                          'phlebostatic axis references pressures '
                                                          'to the right atrium. Wrong leveling '
                                                          'produces falsely high or low readings '
                                                          'that misguide vasopressor and volume '
                                                          'decisions.',
                                           'choice_explanations': {'A': 'Knee leveling does not '
                                                                        'reference atrial level.',
                                                                   'B': 'The bag spike is not the '
                                                                        'anatomic reference point.',
                                                                   'C': 'Phlebostatic axis '
                                                                        'leveling is the standard '
                                                                        'for arterial/CVP '
                                                                        'referencing.',
                                                                   'D': 'Ventilator circuit height '
                                                                        'is unrelated to arterial '
                                                                        'transducer leveling.'}},
                                          {'question': 'Which intervention is part of a typical '
                                                       'ventilator-associated pneumonia (VAP) '
                                                       'prevention bundle?',
                                           'options': ['A) Keeping the head of bed flat at all '
                                                       'times',
                                                       'B) Avoiding oral care to reduce secretions',
                                                       'C) Breaking circuit daily without '
                                                       'indication for “freshness”',
                                                       'D) Head-of-bed elevation, oral care with '
                                                       'antiseptic, and sedation/weaning reviews '
                                                       'as protocolled'],
                                           'answer': 'D) Head-of-bed elevation, oral care with '
                                                     'antiseptic, and sedation/weaning reviews as '
                                                     'protocolled',
                                           'explanation': 'VAP bundles reduce aspiration and '
                                                          'biofilm risk via HOB elevation, oral '
                                                          'antiseptic care, subglottic suction '
                                                          'when available, and daily '
                                                          'sedation/spontaneous breathing '
                                                          'assessments. Flat positioning and '
                                                          'neglected oral care increase VAP risk.',
                                           'choice_explanations': {'A': 'Flat positioning '
                                                                        'increases aspiration '
                                                                        'risk.',
                                                                   'B': 'Oral care is a key VAP '
                                                                        'prevention element.',
                                                                   'C': 'Unnecessary circuit '
                                                                        'breaks increase '
                                                                        'contamination risk.',
                                                                   'D': 'HOB elevation, oral care, '
                                                                        'and sedation/weaning '
                                                                        'practices are core bundle '
                                                                        'elements.'}}],
                                 'medium': [{'question': 'Central venous pressure (CVP) most '
                                                         'closely reflects which physiologic '
                                                         'concept at the bedside?',
                                             'options': ['A) Right-heart preload / right atrial '
                                                         'pressure trend (with interpretation '
                                                         'limits)',
                                                         'B) Exact left-ventricular ejection '
                                                         'fraction percentage',
                                                         'C) Serum potassium concentration',
                                                         'D) Pupil reactivity score'],
                                             'answer': 'A) Right-heart preload / right atrial '
                                                       'pressure trend (with interpretation '
                                                       'limits)',
                                             'explanation': 'CVP approximates right atrial '
                                                            'pressure and is used as a crude '
                                                            'right-sided preload trend, '
                                                            'interpreted with exams, fluids, and '
                                                            'other hemodynamics. It does not equal '
                                                            'LVEF, potassium, or neurologic '
                                                            'scores.',
                                             'choice_explanations': {'A': 'CVP trends right atrial '
                                                                          'pressure/preload with '
                                                                          'known limitations.',
                                                                     'B': 'LVEF requires imaging, '
                                                                          'not CVP alone.',
                                                                     'C': 'Electrolytes are lab '
                                                                          'values, not CVP.',
                                                                     'D': 'Pupils are neurologic '
                                                                          'findings unrelated to '
                                                                          'CVP meaning.'}},
                                            {'question': 'Which nursing measures help manage '
                                                         'increased intracranial pressure?',
                                             'options': ['A) Cluster noxious care, keep neck '
                                                         'flexed, and hypotonic free-water boluses',
                                                         'B) Neutral head alignment, HOB elevation '
                                                         'if ordered, controlled '
                                                         'ventilation/oxygenation, and minimize '
                                                         'clustering of stimuli',
                                                         'C) Force coughing and Valsalva '
                                                         'frequently to “clear pressure”',
                                                         'D) Place in Trendelenburg continuously'],
                                             'answer': 'B) Neutral head alignment, HOB elevation '
                                                       'if ordered, controlled '
                                                       'ventilation/oxygenation, and minimize '
                                                       'clustering of stimuli',
                                             'explanation': 'ICP care maintains cerebral venous '
                                                            'drainage (neutral neck, HOB elevation '
                                                            'as ordered), avoids '
                                                            'hypoxemia/hypercapnia extremes per '
                                                            'goals, and limits stimulatory '
                                                            'clustering. Flexion, Trendelenburg, '
                                                            'hypotonic fluids, and forced Valsalva '
                                                            'raise ICP.',
                                             'choice_explanations': {'A': 'Neck flexion and '
                                                                          'hypotonic fluids worsen '
                                                                          'cerebral edema/ICP.',
                                                                     'B': 'Alignment, ordered HOB '
                                                                          'elevation, gas-exchange '
                                                                          'control, and stimulus '
                                                                          'control lower ICP risk.',
                                                                     'C': 'Coughing/Valsalva '
                                                                          'transiently spike ICP.',
                                                                     'D': 'Trendelenburg increases '
                                                                          'cerebral venous '
                                                                          'pressure.'}},
                                            {'question': 'In undifferentiated shock, what are the '
                                                         'first nursing priorities?',
                                             'options': ['A) Wait for a definitive etiology before '
                                                         'any oxygen or IV access',
                                                         'B) Focus only on giving oral fluids in '
                                                         'hypotensive patients',
                                                         'C) Support ABCs, obtain IV access, '
                                                         'monitor perfusion, and escalate while '
                                                         'etiology is pursued',
                                                         'D) Place the patient in a chair and '
                                                         'ambulate vigorously'],
                                             'answer': 'C) Support ABCs, obtain IV access, monitor '
                                                       'perfusion, and escalate while etiology is '
                                                       'pursued',
                                             'explanation': 'Shock care begins with airway, '
                                                            'breathing, circulation support, '
                                                            'access, and perfusion monitoring '
                                                            'while identifying hypovolemic, '
                                                            'distributive, cardiogenic, or '
                                                            'obstructive causes. Delaying '
                                                            'oxygen/access for perfect diagnosis '
                                                            'worsens ischemia.',
                                             'choice_explanations': {'A': 'Resuscitation and '
                                                                          'diagnosis proceed in '
                                                                          'parallel.',
                                                                     'B': 'Oral fluids are '
                                                                          'inappropriate in many '
                                                                          'shocked patients.',
                                                                     'C': 'ABC support plus access '
                                                                          'and escalation is the '
                                                                          'correct first priority '
                                                                          'set.',
                                                                     'D': 'Ambulation is '
                                                                          'contraindicated in '
                                                                          'shock.'}}],
                                 'hard': [{'question': 'An intubated ARDS patient has refractory '
                                                       'hypoxemia. Which ventilation theme aligns '
                                                       'with lung-protective strategy?',
                                           'options': ['A) Very large tidal volumes to “pop open” '
                                                       'all alveoli regardless of plateau pressure',
                                                       'B) Zero PEEP in all ARDS cases',
                                                       'C) Permissive hyperoxia at FiO2 1.0 '
                                                       'indefinitely without review',
                                                       'D) Low tidal volumes (~6 mL/kg PBW), '
                                                       'plateau-pressure limits, and PEEP/FiO2 '
                                                       'titration per protocol'],
                                           'answer': 'D) Low tidal volumes (~6 mL/kg PBW), '
                                                     'plateau-pressure limits, and PEEP/FiO2 '
                                                     'titration per protocol',
                                           'explanation': 'ARDSNet-style protection uses ~6 mL/kg '
                                                          'predicted body weight tidal volumes, '
                                                          'plateau-pressure limits, and PEEP/FiO2 '
                                                          'tables to reduce volutrauma while '
                                                          'supporting oxygenation. Oversized '
                                                          'volumes and ignoring PEEP worsen lung '
                                                          'injury.',
                                           'choice_explanations': {'A': 'Large tidal volumes drive '
                                                                        'ventilator-induced lung '
                                                                        'injury.',
                                                                   'B': 'PEEP is used thoughtfully '
                                                                        'in ARDS to maintain '
                                                                        'recruitment.',
                                                                   'C': 'Prolonged unnecessary '
                                                                        'FiO2 1.0 risks oxygen '
                                                                        'toxicity; titrate.',
                                                                   'D': 'Low Vt, Pplat limits, and '
                                                                        'PEEP/FiO2 protocols '
                                                                        'define lung protection.'}},
                                          {'question': 'After blunt chest trauma, a patient has '
                                                       'muffled heart sounds, JVD, and hypotension '
                                                       'with electrical activity on the monitor. '
                                                       'What classic condition should you suspect?',
                                           'options': ['A) Cardiac tamponade (Beck’s triad '
                                                       'pattern) requiring urgent escalation',
                                                       'B) Simple anxiety attack without '
                                                       'hemodynamic meaning',
                                                       'C) Uncomplicated dehydration alone',
                                                       'D) Hyperthyroidism storm as the first '
                                                       'explanation'],
                                           'answer': 'A) Cardiac tamponade (Beck’s triad pattern) '
                                                     'requiring urgent escalation',
                                           'explanation': 'Beck’s triad—hypotension, JVD, muffled '
                                                          'sounds—suggests tamponade physiology '
                                                          'where pericardial blood impairs '
                                                          'filling. Pulseless electrical activity '
                                                          'can ensue. This is an obstructive shock '
                                                          'emergency needing immediate escalation, '
                                                          'not reassurance.',
                                           'choice_explanations': {'A': 'Muffled sounds, JVD, and '
                                                                        'hypotension classic for '
                                                                        'tamponade needing urgent '
                                                                        'action.',
                                                                   'B': 'Objective shock signs are '
                                                                        'not explained by anxiety.',
                                                                   'C': 'Dehydration alone does '
                                                                        'not muffle heart sounds.',
                                                                   'D': 'Thyroid storm has a '
                                                                        'different constellation; '
                                                                        'trauma points to '
                                                                        'tamponade first.'}},
                                          {'question': 'In DKA, which nursing priority cluster is '
                                                       'most accurate while insulin and fluids are '
                                                       'ordered?',
                                           'options': ['A) Stop all potassium monitoring because '
                                                       'insulin raises potassium',
                                                       'B) Airway/hemodynamic support, fluid '
                                                       'resuscitation as ordered, insulin therapy, '
                                                       'and close electrolyte (especially '
                                                       'potassium) monitoring',
                                                       'C) Give subcutaneous insulin only and '
                                                       'encourage sugary drinks',
                                                       'D) Ignore mental-status changes because '
                                                       'they are expected and harmless'],
                                           'answer': 'B) Airway/hemodynamic support, fluid '
                                                     'resuscitation as ordered, insulin therapy, '
                                                     'and close electrolyte (especially potassium) '
                                                     'monitoring',
                                           'explanation': 'DKA care prioritizes ABCs, volume '
                                                          'replacement, insulin to stop '
                                                          'ketogenesis, and electrolyte '
                                                          'management—potassium often falls with '
                                                          'insulin and must be watched. Oral sugar '
                                                          'and neglected mentation assessment are '
                                                          'dangerous.',
                                           'choice_explanations': {'A': 'Insulin drives potassium '
                                                                        'intracellularly; '
                                                                        'monitoring/replacement '
                                                                        'are critical.',
                                                                   'B': 'Fluids, insulin, and '
                                                                        'electrolyte/ABC vigilance '
                                                                        'are the DKA nursing '
                                                                        'pillars.',
                                                                   'C': 'DKA usually needs IV '
                                                                        'insulin/fluids, not '
                                                                        'sugary drinks.',
                                                                   'D': 'Altered mentation can '
                                                                        'signal worsening '
                                                                        'acidosis/hypoperfusion '
                                                                        'and airway risk.'}}],
                                 'extreme': [{'question': 'You are alone at the bedside when the '
                                                          'monitor shows pulseless ventricular '
                                                          'tachycardia; the patient is '
                                                          'unresponsive. A family member forbids '
                                                          'you to shock “until the priest '
                                                          'arrives,” and the defibrillator pads '
                                                          'are in the drawer. What is the correct '
                                                          'immediate action sequence?',
                                              'options': ['A) Wait for clergy before any '
                                                          'intervention',
                                                          'B) Check a blood pressure cuff cycle '
                                                          'before compressions',
                                                          'C) Start CPR, apply pads, defibrillate '
                                                          'as indicated for pulseless VT/VF, and '
                                                          'activate the code team',
                                                          'D) Give a fluid bolus as the sole '
                                                          'therapy for pulseless VT'],
                                              'answer': 'C) Start CPR, apply pads, defibrillate as '
                                                        'indicated for pulseless VT/VF, and '
                                                        'activate the code team',
                                              'explanation': 'Pulseless VT/VF is a shockable '
                                                             'arrest rhythm. Immediate CPR and '
                                                             'defibrillation, with code-team '
                                                             'activation, are mandatory. Family '
                                                             'preference cannot override emergency '
                                                             'resuscitation absent a valid DNR; '
                                                             'fluids do not treat VF/pVT.',
                                              'choice_explanations': {'A': 'Delaying '
                                                                           'defibrillation for '
                                                                           'clergy arrival costs '
                                                                           'survival.',
                                                                      'B': 'Pulse/responsiveness '
                                                                           'already establish '
                                                                           'arrest; long cuff '
                                                                           'cycles delay CPR.',
                                                                      'C': 'CPR plus '
                                                                           'defibrillation for '
                                                                           'shockable rhythms is '
                                                                           'ACLS first-line care.',
                                                                      'D': 'Volume alone does not '
                                                                           'terminate pulseless '
                                                                           'VT/VF.'}},
                                             {'question': 'A trauma patient in hemorrhagic shock '
                                                          'is receiving a massive transfusion. '
                                                          'Temperature is 34.8°C, ionized calcium '
                                                          'is low, and oozing worsens. Which '
                                                          'priority cluster is most appropriate?',
                                              'options': ['A) Stop all blood products and give '
                                                          'only hypotonic free water',
                                                          'B) Accept hypothermia as inevitable and '
                                                          'withhold warming devices',
                                                          'C) Give unmatched products from '
                                                          'unlabeled syringes to save time',
                                                          'D) Warm the patient/products, replace '
                                                          'calcium as ordered, follow MTP ratios, '
                                                          'and preserve transfusion safety checks '
                                                          'while escalating coagulopathy care'],
                                              'answer': 'D) Warm the patient/products, replace '
                                                        'calcium as ordered, follow MTP ratios, '
                                                        'and preserve transfusion safety checks '
                                                        'while escalating coagulopathy care',
                                              'explanation': 'Massive transfusion must counter the '
                                                             'lethal triad while preserving blood '
                                                             'safety. Warming, calcium repletion '
                                                             'for citrate effect, balanced product '
                                                             'ratios, coagulopathy management, and '
                                                             'continued product verification are '
                                                             'concurrent priorities.',
                                              'choice_explanations': {'A': 'Stopping blood for '
                                                                           'free water worsens '
                                                                           'hemorrhage and '
                                                                           'hyponatremia risk.',
                                                                      'B': 'Hypothermia '
                                                                           'intensifies '
                                                                           'coagulopathy and '
                                                                           'should be actively '
                                                                           'corrected.',
                                                                      'C': 'Unlabeled products '
                                                                           'risk fatal ABO '
                                                                           'incompatibility.',
                                                                      'D': 'Warming, calcium, MTP '
                                                                           'ratios, and safety '
                                                                           'checks together '
                                                                           'address bleeding '
                                                                           'physiology and prevent '
                                                                           'transfusion error.'}},
                                             {'question': 'The team is preparing clinical '
                                                          'brain-death testing on an ICU patient. '
                                                          'A junior nurse plans to give a sedative '
                                                          'bolus “so the exam is calm,” and family '
                                                          'asks what nursing’s role is. What '
                                                          'should you do?',
                                              'options': ['A) Clarify that confounding '
                                                          'sedation/metabolic issues must be '
                                                          'absent; support family, maintain '
                                                          'physiologic stability, and assist the '
                                                          'declared protocol—do not sedate before '
                                                          'testing',
                                                          'B) Give extra propofol to guarantee '
                                                          'unresponsiveness for the exam',
                                                          'C) Tell family brain-death testing is '
                                                          'optional entertainment',
                                                          'D) Stop all blood-pressure support so '
                                                          'the exam is “more realistic”'],
                                              'answer': 'A) Clarify that confounding '
                                                        'sedation/metabolic issues must be absent; '
                                                        'support family, maintain physiologic '
                                                        'stability, and assist the declared '
                                                        'protocol—do not sedate before testing',
                                              'explanation': 'Brain-death determination requires '
                                                             'absence of confounders such as '
                                                             'recent sedation, hypothermia, and '
                                                             'severe metabolic derangements. '
                                                             'Nursing maintains stability, '
                                                             'educates/supports family, and '
                                                             'assists the protocol—not deepening '
                                                             'sedation or withdrawing needed '
                                                             'support to fake findings.',
                                              'choice_explanations': {'A': 'Avoiding sedative '
                                                                           'confounders and '
                                                                           'supporting '
                                                                           'protocol/family is the '
                                                                           'correct nursing role.',
                                                                      'B': 'Sedation invalidates '
                                                                           'the neurologic exam.',
                                                                      'C': 'Testing is a solemn '
                                                                           'clinical/legal '
                                                                           'determination, not '
                                                                           'entertainment.',
                                                                      'D': 'Induced instability is '
                                                                           'unethical and '
                                                                           'confounds '
                                                                           'assessment.'}}]},
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
                                           'options': ['A) Only billing mistakes on the hospital '
                                                       'invoice',
                                                       'B) Wrong patient, drug, dose, route, time '
                                                       '(and related rights such as '
                                                       'documentation/reason)',
                                                       'C) Exclusive prevention of dietary tray '
                                                       'mix-ups',
                                                       'D) Errors related only to visitor visiting '
                                                       'hours'],
                                           'answer': 'B) Wrong patient, drug, dose, route, time '
                                                     '(and related rights such as '
                                                     'documentation/reason)',
                                           'explanation': 'Medication rights systematize identity, '
                                                          'drug, dose, route, time, documentation, '
                                                          'and reason checks to interrupt common '
                                                          'administration error pathways. They are '
                                                          'clinical safety tools, not billing or '
                                                          'visitor policies.',
                                           'choice_explanations': {'A': 'Rights target clinical '
                                                                        'administration safety, '
                                                                        'not invoices.',
                                                                   'B': 'Patient/drug/dose/route/time '
                                                                        '(plus related rights) '
                                                                        'prevent core med errors.',
                                                                   'C': 'Dietary trays are a '
                                                                        'different safety domain.',
                                                                   'D': 'Visiting hours are '
                                                                        'unrelated to med-rights '
                                                                        'framework.'}},
                                          {'question': 'Before giving digoxin, which assessment is '
                                                       'most classically required?',
                                           'options': ['A) Pupil size only',
                                                       'B) Stool occult blood only',
                                                       'C) Apical pulse (and review of '
                                                       'potassium/digoxin-toxicity cues per '
                                                       'protocol)',
                                                       'D) Audiometry in every adult before each '
                                                       'dose'],
                                           'answer': 'C) Apical pulse (and review of '
                                                     'potassium/digoxin-toxicity cues per '
                                                     'protocol)',
                                           'explanation': 'Digoxin slows conduction; apical rate '
                                                          'below hold parameters and hypokalemia '
                                                          'raise toxicity/bradyarrhythmia risk. '
                                                          'Nurses check apical pulse and relevant '
                                                          'labs/symptoms before administration.',
                                           'choice_explanations': {'A': 'Pupils are not the '
                                                                        'primary digoxin hold '
                                                                        'parameter.',
                                                                   'B': 'Occult blood is not the '
                                                                        'classic pre-digoxin '
                                                                        'check.',
                                                                   'C': 'Apical pulse plus '
                                                                        'potassium/toxicity '
                                                                        'surveillance is the '
                                                                        'standard nursing check.',
                                                                   'D': 'Hearing tests are not '
                                                                        'required before each '
                                                                        'digoxin dose.'}},
                                          {'question': 'What needle angle is typically used for a '
                                                       'standard intramuscular injection?',
                                           'options': ['A) 10° into the dermis only',
                                                       'B) 45° into subcutaneous fat only as the '
                                                       'IM standard',
                                                       'C) 0° parallel to skin for all IM vaccines',
                                                       'D) 90° into muscle (unless a specific '
                                                       'alternative technique is indicated)'],
                                           'answer': 'D) 90° into muscle (unless a specific '
                                                     'alternative technique is indicated)',
                                           'explanation': 'IM injections are generally delivered '
                                                          'at 90° to deposit medication in muscle. '
                                                          'Intradermal uses ~10–15°; subcutaneous '
                                                          'often 45–90° depending on '
                                                          'needle/fold—not the IM default.',
                                           'choice_explanations': {'A': '≈10–15° is intradermal '
                                                                        'technique.',
                                                                   'B': '45° is a common '
                                                                        'subcutaneous angle, not '
                                                                        'the IM standard.',
                                                                   'C': 'Parallel-to-skin '
                                                                        'technique is not IM '
                                                                        'administration.',
                                                                   'D': '90° IM angle targets '
                                                                        'muscle for intended '
                                                                        'absorption.'}}],
                                 'medium': [{'question': 'Which teaching point is essential for a '
                                                         'patient newly started on warfarin?',
                                             'options': ['A) Report unusual bleeding/bruising, '
                                                         'keep INR monitoring, and maintain '
                                                         'consistent vitamin K intake',
                                                         'B) Double doses after any missed tablet '
                                                         'without advice',
                                                         'C) Stop warfarin if a headache occurs '
                                                         'and never tell the clinician',
                                                         'D) Take NSAIDs freely because they '
                                                         'protect the stomach on warfarin'],
                                             'answer': 'A) Report unusual bleeding/bruising, keep '
                                                       'INR monitoring, and maintain consistent '
                                                       'vitamin K intake',
                                             'explanation': 'Warfarin’s narrow index requires INR '
                                                            'surveillance, bleeding precautions, '
                                                            'and consistent vitamin K intake. Dose '
                                                            'self-doubling, silent stops, and '
                                                            'NSAIDs raise thrombosis or bleed '
                                                            'risk.',
                                             'choice_explanations': {'A': 'Bleeding awareness, INR '
                                                                          'follow-up, and vitamin '
                                                                          'K consistency are core '
                                                                          'warfarin teaching.',
                                                                     'B': 'Unadvised double dosing '
                                                                          'can cause '
                                                                          'life-threatening '
                                                                          'hemorrhage.',
                                                                     'C': 'Unreported cessation '
                                                                          'risks stroke/VTE; '
                                                                          'clinicians must know.',
                                                                     'D': 'NSAIDs increase '
                                                                          'bleeding risk with '
                                                                          'warfarin.'}},
                                            {'question': 'When giving an IV push opioid, which '
                                                         'nursing requirement is most important?',
                                             'options': ['A) Push as fast as possible to finish '
                                                         'rounds sooner',
                                                         'B) Administer at the recommended rate '
                                                         'while monitoring sedation and '
                                                         'respiratory status',
                                                         'C) Leave the patient alone for one hour '
                                                         'without reassessment',
                                                         'D) Mix with unknown leftover syringe '
                                                         'contents to avoid waste'],
                                             'answer': 'B) Administer at the recommended rate '
                                                       'while monitoring sedation and respiratory '
                                                       'status',
                                             'explanation': 'IV opioids can cause rapid '
                                                            'respiratory depression. Correct push '
                                                            'rates and close sedation/RR/SpO2 '
                                                            'monitoring reduce overdose risk. '
                                                            'Speed-pushing, neglectful '
                                                            'observation, and syringe pooling are '
                                                            'unsafe.',
                                             'choice_explanations': {'A': 'Rapid push spikes '
                                                                          'CNS/respiratory '
                                                                          'depression risk.',
                                                                     'B': 'Rate control plus '
                                                                          'respiratory/sedation '
                                                                          'monitoring is '
                                                                          'mandatory.',
                                                                     'C': 'Reassessment after IV '
                                                                          'opioids is required for '
                                                                          'safety.',
                                                                     'D': 'Unidentified syringe '
                                                                          'mixing risks dosing and '
                                                                          'contamination errors.'}},
                                            {'question': 'When mixing regular (clear) and NPH '
                                                         '(cloudy) insulin in one syringe, which '
                                                         'theme is correct?',
                                             'options': ['A) Draw cloudy before clear always, '
                                                         'without air steps',
                                                         'B) Shake NPH violently until foam '
                                                         'appears',
                                                         'C) Inject air into NPH then regular, '
                                                         'draw regular (clear) first, then '
                                                         'NPH—avoid contaminating the regular vial',
                                                         'D) Use the same needle to pierce '
                                                         'multiple patient vials interchangeably'],
                                             'answer': 'C) Inject air into NPH then regular, draw '
                                                       'regular (clear) first, then NPH—avoid '
                                                       'contaminating the regular vial',
                                             'explanation': 'Clear-before-cloudy drawing after '
                                                            'appropriate air injection prevents '
                                                            'regular-insulin vial contamination '
                                                            'with NPH. Foaming from violent '
                                                            'shaking and sharing needles across '
                                                            'vials are unsafe.',
                                             'choice_explanations': {'A': 'Drawing cloudy first '
                                                                          'contaminates the '
                                                                          'regular vial.',
                                                                     'B': 'Violent shaking creates '
                                                                          'foam and dosing '
                                                                          'inaccuracy; roll/gentle '
                                                                          'mix per teaching.',
                                                                     'C': 'Air steps then '
                                                                          'clear-before-cloudy '
                                                                          'preserves regular vial '
                                                                          'integrity.',
                                                                     'D': 'Multi-patient vial '
                                                                          'needle sharing risks '
                                                                          'contamination.'}}],
                                 'hard': [{'question': 'Which medications are classic high-alert '
                                                       'examples requiring extra nursing '
                                                       'safeguards?',
                                           'options': ['A) Bulk laxatives only, with no other '
                                                       'categories',
                                                       'B) Topical emollients exclusively',
                                                       'C) Multivitamins as the sole high-alert '
                                                       'class',
                                                       'D) Insulin, anticoagulants, opioids, and '
                                                       'concentrated electrolytes'],
                                           'answer': 'D) Insulin, anticoagulants, opioids, and '
                                                     'concentrated electrolytes',
                                           'explanation': 'High-alert drugs cause severe harm when '
                                                          'misused—insulin, anticoagulants, '
                                                          'opioids, and concentrated electrolytes '
                                                          'head most lists. Independent '
                                                          'double-checks and smart-pump libraries '
                                                          'are common safeguards.',
                                           'choice_explanations': {'A': 'Laxatives are not the '
                                                                        'defining high-alert '
                                                                        'group.',
                                                                   'B': 'Emollients lack the '
                                                                        'catastrophic harm profile '
                                                                        'of high-alert meds.',
                                                                   'C': 'Multivitamins are not '
                                                                        'classic high-alert '
                                                                        'agents.',
                                                                   'D': 'Insulin, anticoagulants, '
                                                                        'opioids, and concentrated '
                                                                        'electrolytes are '
                                                                        'prototypical high-alert '
                                                                        'meds.'}},
                                          {'question': 'Vancomycin “red man syndrome” is most '
                                                       'related to which administration issue?',
                                           'options': ['A) Too-rapid infusion causing '
                                                       'histamine-release flushing/hypotension',
                                                       'B) Giving the dose intramuscularly into '
                                                       'the deltoid only',
                                                       'C) Mixing with lactulose for synergy',
                                                       'D) Taking vancomycin with grapefruit juice '
                                                       'exclusively'],
                                           'answer': 'A) Too-rapid infusion causing '
                                                     'histamine-release flushing/hypotension',
                                           'explanation': 'Rapid vancomycin infusion triggers '
                                                          'mast-cell histamine release with '
                                                          'flushing, rash, and possible '
                                                          'hypotension. Slowing the infusion rate '
                                                          '(and antihistamines per protocol) '
                                                          'manages it; it is rate-related, not an '
                                                          'IM or grapefruit phenomenon.',
                                           'choice_explanations': {'A': 'Rate-related histamine '
                                                                        'release explains red man '
                                                                        'syndrome.',
                                                                   'B': 'Vancomycin is typically '
                                                                        'IV; IM deltoid is not the '
                                                                        'red-man mechanism.',
                                                                   'C': 'Lactulose mixing is '
                                                                        'unrelated.',
                                                                   'D': 'Grapefruit interactions '
                                                                        'are not the classic '
                                                                        'red-man cause.'}},
                                          {'question': 'Why must concentrated IV potassium never '
                                                       'be given as an undiluted IV push?',
                                           'options': ['A) Because potassium tastes bitter if '
                                                       'pushed',
                                                       'B) Because undiluted IV push can cause '
                                                       'fatal dysrhythmias; it requires diluted, '
                                                       'pump-controlled infusion per policy',
                                                       'C) Because potassium only works orally',
                                                       'D) Because pumps are never used for '
                                                       'electrolytes'],
                                           'answer': 'B) Because undiluted IV push can cause fatal '
                                                     'dysrhythmias; it requires diluted, '
                                                     'pump-controlled infusion per policy',
                                           'explanation': 'Bolus concentrated KCl can cause '
                                                          'immediate cardiac arrest. Policies '
                                                          'require dilution, maximum rates, pump '
                                                          'control, and often central access for '
                                                          'higher concentrations—never IV push '
                                                          'from a vial.',
                                           'choice_explanations': {'A': 'Taste is irrelevant to IV '
                                                                        'cardiac toxicity.',
                                                                   'B': 'Fatal dysrhythmia risk '
                                                                        'mandates diluted, '
                                                                        'rate-controlled infusion.',
                                                                   'C': 'IV potassium is used when '
                                                                        'oral route is inadequate, '
                                                                        'but safely infused.',
                                                                   'D': 'Pumps are specifically '
                                                                        'used to control potassium '
                                                                        'infusion rates.'}}],
                                 'extreme': [{'question': 'Minutes after succinylcholine, a '
                                                          'surgical patient develops ETCO2 rise, '
                                                          'jaw rigidity, temperature climbing '
                                                          'through 39°C, and mixed acidosis. The '
                                                          'anesthesia tech suggests “just give '
                                                          'more inhalational agent.” What should '
                                                          'the nurse anticipate as the priority '
                                                          'treatment pathway?',
                                              'options': ['A) Continue triggering agents and cover '
                                                          'with warm blankets',
                                                          'B) Treat as anxiety and give midazolam '
                                                          'only',
                                                          'C) Call malignant hyperthermia '
                                                          'response: stop triggers, hyperventilate '
                                                          'with 100% O2, give dantrolene per '
                                                          'protocol, cool, and support ABCs',
                                                          'D) Give IV potassium push to treat '
                                                          'presumed hypokalemia only'],
                                              'answer': 'C) Call malignant hyperthermia response: '
                                                        'stop triggers, hyperventilate with 100% '
                                                        'O2, give dantrolene per protocol, cool, '
                                                        'and support ABCs',
                                              'explanation': 'Rising CO2, rigidity, and '
                                                             'hyperthermia after a trigger '
                                                             'anesthetic indicate malignant '
                                                             'hyperthermia—a hypermetabolic '
                                                             'crisis. Stop triggers, call for '
                                                             'help/MH cart, give dantrolene, '
                                                             'hyperventilate with oxygen, cool, '
                                                             'and manage electrolytes/ABCs. More '
                                                             'trigger agent is contraindicated.',
                                              'choice_explanations': {'A': 'Continuing triggers '
                                                                           'and warming worsens '
                                                                           'MH.',
                                                                      'B': 'Midazolam does not '
                                                                           'treat MH '
                                                                           'pathophysiology.',
                                                                      'C': 'Trigger cessation, '
                                                                           'dantrolene, cooling, '
                                                                           'and ABC support are '
                                                                           'the MH pathway.',
                                                                      'D': 'MH often involves '
                                                                           'hyperkalemia; blind '
                                                                           'KCl push can be '
                                                                           'lethal.'}},
                                             {'question': 'A postoperative patient on a PCA has RR '
                                                          '4, pinpoint pupils, SpO2 82%, and is '
                                                          'barely arousable. A visitor says the '
                                                          'patient “needs another click for pain.” '
                                                          'What is the priority action?',
                                              'options': ['A) Encourage the visitor to press the '
                                                          'PCA button repeatedly',
                                                          'B) Document and reassess after lunch',
                                                          'C) Increase the PCA basal rate to '
                                                          'overcome tolerance',
                                                          'D) Support airway/ventilation, stop '
                                                          'opioid input, give naloxone per '
                                                          'protocol, and activate rapid response'],
                                              'answer': 'D) Support airway/ventilation, stop '
                                                        'opioid input, give naloxone per protocol, '
                                                        'and activate rapid response',
                                              'explanation': 'This is opioid-induced respiratory '
                                                             'depression/overdose. Priorities are '
                                                             'airway, oxygenation/ventilation, '
                                                             'stopping further opioid, and '
                                                             'naloxone with rapid-response '
                                                             'activation. PCA by proxy and dose '
                                                             'escalation are dangerous.',
                                              'choice_explanations': {'A': 'PCA by proxy can kill '
                                                                           'a sedated patient.',
                                                                      'B': 'RR 4 with hypoxia '
                                                                           'needs immediate '
                                                                           'intervention, not '
                                                                           'delayed reassessment.',
                                                                      'C': 'Increasing basal '
                                                                           'opioid worsens '
                                                                           'hypoventilation.',
                                                                      'D': 'Airway support, '
                                                                           'naloxone, and stopping '
                                                                           'opioid are the correct '
                                                                           'overdose response.'}},
                                             {'question': 'During peripheral chemotherapy '
                                                          'infusion, the patient reports burning; '
                                                          'the site is swollen and cool, and no '
                                                          'blood return is obtained. The protocol '
                                                          'labels the drug a vesicant. What should '
                                                          'you do?',
                                              'options': ['A) Stop the infusion, aspirate residual '
                                                          'per protocol, mark the site, notify the '
                                                          'provider/pharmacy, and follow '
                                                          'antidote/extravasation standing '
                                                          'orders—do not flush blindly',
                                                          'B) Speed the infusion to finish before '
                                                          'swelling worsens',
                                                          'C) Apply a tight arterial tourniquet '
                                                          'above the site for hours',
                                                          'D) Ignore burning because vesicants '
                                                          'never injure tissue'],
                                              'answer': 'A) Stop the infusion, aspirate residual '
                                                        'per protocol, mark the site, notify the '
                                                        'provider/pharmacy, and follow '
                                                        'antidote/extravasation standing orders—do '
                                                        'not flush blindly',
                                              'explanation': 'Vesicant extravasation can cause '
                                                             'severe tissue necrosis. Immediate '
                                                             'stop, limited aspiration per '
                                                             'protocol, avoiding forceful flush, '
                                                             'escalation, and antidote/thermal '
                                                             'measures specific to the agent are '
                                                             'required.',
                                              'choice_explanations': {'A': 'Stop–aspirate–notify–antidote '
                                                                           'sequence matches '
                                                                           'extravasation '
                                                                           'standards.',
                                                                      'B': 'Faster infusion '
                                                                           'increases extravasated '
                                                                           'volume and injury.',
                                                                      'C': 'Prolonged tourniquets '
                                                                           'cause ischemia and do '
                                                                           'not treat '
                                                                           'extravasation.',
                                                                      'D': 'Vesicants are defined '
                                                                           'by their '
                                                                           'tissue-destroying '
                                                                           'potential.'}}]},
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
                                               'options': ['A) Staff may decide all treatments '
                                                           'without patient input',
                                                           'B) Respect for a capacitated person’s '
                                                           'right to make informed choices about '
                                                           'their care',
                                                           'C) Always doing whatever the family '
                                                           'demands',
                                                           'D) Keeping patients uninformed to '
                                                           'reduce anxiety'],
                                               'answer': 'B) Respect for a capacitated person’s '
                                                         'right to make informed choices about '
                                                         'their care',
                                               'explanation': 'Autonomy respects informed '
                                                              'self-determination by capacitated '
                                                              'patients. Paternalistic secrecy, '
                                                              'staff unilateralism, and automatic '
                                                              'family override (when the patient '
                                                              'has capacity) violate autonomy.',
                                               'choice_explanations': {'A': 'Excluding the patient '
                                                                            'negates autonomy.',
                                                                       'B': 'Informed '
                                                                            'self-determination is '
                                                                            'the definition of '
                                                                            'autonomy.',
                                                                       'C': 'Family demands do not '
                                                                            'automatically replace '
                                                                            'a capacitated '
                                                                            'patient’s choices.',
                                                                       'D': 'Withholding '
                                                                            'information blocks '
                                                                            'informed choice.'}},
                                              {'question': 'Beneficence in nursing ethics most '
                                                           'nearly means?',
                                               'options': ['A) Avoiding all treatments even when '
                                                           'clearly helpful',
                                                           'B) Maximizing billable procedures '
                                                           'regardless of benefit',
                                                           'C) Acting to promote the patient’s '
                                                           'good and well-being',
                                                           'D) Following only personal '
                                                           'convenience'],
                                               'answer': 'C) Acting to promote the patient’s good '
                                                         'and well-being',
                                               'explanation': 'Beneficence is the obligation to '
                                                              'benefit the patient—promoting '
                                                              'health and welfare. It is balanced '
                                                              'with autonomy and nonmaleficence, '
                                                              'not equated with profit or '
                                                              'convenience.',
                                               'choice_explanations': {'A': 'Withholding helpful '
                                                                            'indicated care '
                                                                            'contradicts '
                                                                            'beneficence.',
                                                                       'B': 'Profit-driven excess '
                                                                            'is not beneficence.',
                                                                       'C': 'Promoting patient '
                                                                            'good is beneficence.',
                                                                       'D': 'Convenience is not an '
                                                                            'ethical principle of '
                                                                            'beneficence.'}},
                                              {'question': 'Which situation is a confidentiality '
                                                           'breach?',
                                               'options': ['A) Hand-off report to the oncoming '
                                                           'nurse in a private area',
                                                           'B) Sharing need-to-know details with '
                                                           'the interprofessional care team',
                                                           'C) Documenting objectively in the '
                                                           'legal medical record',
                                                           'D) Discussing identifiable patient '
                                                           'details with friends in an elevator'],
                                               'answer': 'D) Discussing identifiable patient '
                                                         'details with friends in an elevator',
                                               'explanation': 'Confidentiality limits PHI to '
                                                              'need-to-know care contexts. '
                                                              'Elevator gossip with friends is a '
                                                              'classic breach; private handoffs, '
                                                              'team communication, and record '
                                                              'documentation are legitimate uses.',
                                               'choice_explanations': {'A': 'Private clinical '
                                                                            'handoff is '
                                                                            'appropriate '
                                                                            'information sharing.',
                                                                       'B': 'Care-team '
                                                                            'need-to-know sharing '
                                                                            'supports treatment.',
                                                                       'C': 'Accurate '
                                                                            'documentation is a '
                                                                            'required '
                                                                            'legal/clinical '
                                                                            'function.',
                                                                       'D': 'Non-care gossip with '
                                                                            'identifiers violates '
                                                                            'confidentiality.'}}],
                                     'medium': [{'question': 'Nonmaleficence most directly '
                                                             'obligates the nurse to do which?',
                                                 'options': ['A) Avoid causing unjustified harm '
                                                             'and minimize risk in care',
                                                             'B) Guarantee every outcome will be '
                                                             'perfect',
                                                             'C) Refuse to report errors so nobody '
                                                             'is upset',
                                                             'D) Prioritize institutional image '
                                                             'over patient safety'],
                                                 'answer': 'A) Avoid causing unjustified harm and '
                                                           'minimize risk in care',
                                                 'explanation': 'Nonmaleficence—“do no '
                                                                'harm”—requires avoiding '
                                                                'unjustified injury and reducing '
                                                                'foreseeable risk. It does not '
                                                                'demand perfection myths or '
                                                                'concealment of errors that could '
                                                                'harm others.',
                                                 'choice_explanations': {'A': 'Minimizing '
                                                                              'unjustified harm is '
                                                                              'the core of '
                                                                              'nonmaleficence.',
                                                                         'B': 'Ethics does not '
                                                                              'require impossible '
                                                                              'outcome guarantees.',
                                                                         'C': 'Hiding errors '
                                                                              'increases harm '
                                                                              'potential.',
                                                                         'D': 'Image over safety '
                                                                              'violates '
                                                                              'nonmaleficence and '
                                                                              'fidelity.'}},
                                                {'question': 'Justice as a nursing ethical '
                                                             'principle primarily concerns which '
                                                             'issue?',
                                                 'options': ['A) Giving VIP patients unlimited '
                                                             'unequal access by default',
                                                             'B) Fair allocation of resources and '
                                                             'equitable treatment without unjust '
                                                             'discrimination',
                                                             'C) Ignoring marginalized '
                                                             'populations’ barriers',
                                                             'D) Using lottery only for meal tray '
                                                             'colors'],
                                                 'answer': 'B) Fair allocation of resources and '
                                                           'equitable treatment without unjust '
                                                           'discrimination',
                                                 'explanation': 'Justice addresses fairness in '
                                                                'distribution of care and '
                                                                'resources and opposition to '
                                                                'unjust discrimination. VIP '
                                                                'favoritism and ignoring '
                                                                'disparities contradict justice.',
                                                 'choice_explanations': {'A': 'Unjust VIP '
                                                                              'preference violates '
                                                                              'justice.',
                                                                         'B': 'Fair, '
                                                                              'nondiscriminatory '
                                                                              'allocation is the '
                                                                              'justice principle.',
                                                                         'C': 'Ignoring barriers '
                                                                              'perpetuates '
                                                                              'inequity.',
                                                                         'D': 'Tray-color '
                                                                              'lotteries '
                                                                              'trivialize the '
                                                                              'principle.'}},
                                                {'question': 'What is the primary purpose of an '
                                                             'incident (occurrence) report?',
                                                 'options': ['A) Punish staff publicly in the '
                                                             'newspaper',
                                                             'B) Create gossip material for break '
                                                             'rooms',
                                                             'C) Document events for system '
                                                             'learning and risk reduction '
                                                             '(quality/safety), separate from '
                                                             'blame-focused charting',
                                                             'D) Replace the need for any clinical '
                                                             'documentation in the record'],
                                                 'answer': 'C) Document events for system learning '
                                                           'and risk reduction (quality/safety), '
                                                           'separate from blame-focused charting',
                                                 'explanation': 'Incident reports feed '
                                                                'institutional safety learning and '
                                                                'risk management. They are not '
                                                                'publicity tools or substitutes '
                                                                'for factual clinical charting, '
                                                                'nor are they meant for gossip.',
                                                 'choice_explanations': {'A': 'Public punishment '
                                                                              'is not the purpose '
                                                                              'of incident '
                                                                              'reporting.',
                                                                         'B': 'Gossip misuse '
                                                                              'undermines just '
                                                                              'culture.',
                                                                         'C': 'System learning and '
                                                                              'risk reduction are '
                                                                              'the primary aims.',
                                                                         'D': 'The medical record '
                                                                              'still needs factual '
                                                                              'clinical '
                                                                              'documentation.'}}],
                                     'hard': [{'question': 'Advocacy in nursing leadership most '
                                                           'accurately means which action?',
                                               'options': ['A) Remaining silent when unsafe orders '
                                                           'endanger patients',
                                                           'B) Prioritizing personal overtime pay '
                                                           'above all patient needs',
                                                           'C) Supporting only popular colleagues’ '
                                                           'preferences',
                                                           'D) Speaking and acting to protect '
                                                           'patients’ rights, safety, and best '
                                                           'interests—including challenging unsafe '
                                                           'practices'],
                                               'answer': 'D) Speaking and acting to protect '
                                                         'patients’ rights, safety, and best '
                                                         'interests—including challenging unsafe '
                                                         'practices',
                                               'explanation': 'Advocacy elevates patient rights '
                                                              'and safety, including escalating '
                                                              'concerns about unsafe care. Silence '
                                                              'in the face of harm and '
                                                              'self-interest over patients '
                                                              'contradict advocacy.',
                                               'choice_explanations': {'A': 'Silence with known '
                                                                            'danger abandons '
                                                                            'advocacy.',
                                                                       'B': 'Personal pay is not '
                                                                            'the definition of '
                                                                            'patient advocacy.',
                                                                       'C': 'Popularity contests '
                                                                            'are not advocacy.',
                                                                       'D': 'Protecting '
                                                                            'rights/safety, '
                                                                            'including challenging '
                                                                            'unsafe practice, '
                                                                            'defines advocacy.'}},
                                              {'question': 'What is the nurse’s usual role related '
                                                           'to informed consent?',
                                               'options': ['A) Witness signature, verify '
                                                           'understanding, and advocate if the '
                                                           'patient seems unclear—while the '
                                                           'provider obtains consent for the '
                                                           'procedure',
                                                           'B) Personally perform the surgeon’s '
                                                           'risk disclosure as the sole consenting '
                                                           'party in all hospitals',
                                                           'C) Forge a signature if the patient is '
                                                           'asleep to keep the OR on time',
                                                           'D) Ignore questions because consent is '
                                                           '“already done”'],
                                               'answer': 'A) Witness signature, verify '
                                                         'understanding, and advocate if the '
                                                         'patient seems unclear—while the provider '
                                                         'obtains consent for the procedure',
                                               'explanation': 'The proceduralist discloses '
                                                              'risks/benefits/alternatives. Nurses '
                                                              'commonly witness, confirm '
                                                              'understanding, and stop the process '
                                                              'to seek clarification if '
                                                              'comprehension is lacking. Forgery '
                                                              'and ignoring questions are '
                                                              'unethical and illegal.',
                                               'choice_explanations': {'A': 'Witnessing, verifying '
                                                                            'understanding, and '
                                                                            'advocating for '
                                                                            'clarity match the '
                                                                            'nursing consent role.',
                                                                       'B': 'Primary disclosure '
                                                                            'belongs to the '
                                                                            'provider performing '
                                                                            'the procedure.',
                                                                       'C': 'Forgery is fraud and '
                                                                            'assault risk.',
                                                                       'D': 'Unanswered questions '
                                                                            'invalidate meaningful '
                                                                            'consent.'}},
                                              {'question': 'Moral distress occurs when nurses '
                                                           'experience which situation?',
                                               'options': ['A) They lack any ethical opinions '
                                                           'whatsoever',
                                                           'B) They know the ethically appropriate '
                                                           'action but institutional or other '
                                                           'barriers prevent taking it',
                                                           'C) They always get what they want '
                                                           'administratively',
                                                           'D) They have unlimited resources and '
                                                           'no conflicting duties'],
                                               'answer': 'B) They know the ethically appropriate '
                                                         'action but institutional or other '
                                                         'barriers prevent taking it',
                                               'explanation': 'Moral distress arises when '
                                                              'clinicians know the right course '
                                                              'but constraints block action, '
                                                              'producing guilt and burnout. It is '
                                                              'not absence of ethics or unlimited '
                                                              'ease.',
                                               'choice_explanations': {'A': 'Moral distress '
                                                                            'presupposes an '
                                                                            'ethical judgment, not '
                                                                            'a vacuum of values.',
                                                                       'B': 'Knowing the right act '
                                                                            'yet being blocked '
                                                                            'defines moral '
                                                                            'distress.',
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
                                                              'B) Alter charts to hide the falls',
                                                              'C) Escalate through '
                                                              'whistleblowing/higher reporting '
                                                              'channels as protected '
                                                              'patient-safety disclosure when '
                                                              'internal routes fail and harm '
                                                              'continues',
                                                              'D) Blame the injured patients for '
                                                              'getting out of bed'],
                                                  'answer': 'C) Escalate through '
                                                            'whistleblowing/higher reporting '
                                                            'channels as protected patient-safety '
                                                            'disclosure when internal routes fail '
                                                            'and harm continues',
                                                  'explanation': 'When internal reporting fails '
                                                                 'and patients keep being harmed, '
                                                                 'nurses may escalate to higher '
                                                                 'authorities '
                                                                 '(regulatory/accreditation) under '
                                                                 'whistleblower protections. '
                                                                 'Silence, chart alteration, and '
                                                                 'victim-blaming violate fidelity '
                                                                 'and nonmaleficence.',
                                                  'choice_explanations': {'A': 'Career fear does '
                                                                               'not justify '
                                                                               'ongoing '
                                                                               'preventable '
                                                                               'patient harm.',
                                                                          'B': 'Falsifying records '
                                                                               'is illegal and '
                                                                               'unethical.',
                                                                          'C': 'Protected '
                                                                               'escalation after '
                                                                               'failed internal '
                                                                               'routes is '
                                                                               'appropriate when '
                                                                               'harm persists.',
                                                                          'D': 'Blaming patients '
                                                                               'ignores a known '
                                                                               'system hazard.'}},
                                                 {'question': 'A capacitated patient with a valid '
                                                              'DNR develops ventricular '
                                                              'fibrillation. A resident orders '
                                                              '“just this one shock for the '
                                                              'family.” The spouse is screaming to '
                                                              '“do everything.” What should you '
                                                              'do?',
                                                  'options': ['A) Shock immediately because the '
                                                              'resident outranks the patient’s '
                                                              'written wishes',
                                                              'B) Hide the DNR form so nobody is '
                                                              'upset',
                                                              'C) Start a full code without '
                                                              'discussion to avoid conflict',
                                                              'D) Uphold the valid DNR, '
                                                              'communicate clearly with the '
                                                              'team/family, and refuse '
                                                              'interventions the patient '
                                                              'declined—seek ethics/supervisor '
                                                              'support if conflict persists'],
                                                  'answer': 'D) Uphold the valid DNR, communicate '
                                                            'clearly with the team/family, and '
                                                            'refuse interventions the patient '
                                                            'declined—seek ethics/supervisor '
                                                            'support if conflict persists',
                                                  'explanation': 'A valid DNR reflecting a '
                                                                 'capacitated patient’s wishes '
                                                                 'governs, even under family or '
                                                                 'hierarchical pressure. Nurses '
                                                                 'advocate for those wishes, '
                                                                 'clarify orders, and escalate '
                                                                 'conflicts through chain of '
                                                                 'command/ethics—not secretly '
                                                                 'discarding advance decisions.',
                                                  'choice_explanations': {'A': 'Unlawful/unethical '
                                                                               'to override a '
                                                                               'valid DNR for '
                                                                               'hierarchy alone.',
                                                                          'B': 'Concealing the DNR '
                                                                               'violates honesty '
                                                                               'and patient '
                                                                               'rights.',
                                                                          'C': 'Full code against '
                                                                               'DNR is '
                                                                               'battery/ethics '
                                                                               'breach.',
                                                                          'D': 'Honoring the DNR '
                                                                               'with clear '
                                                                               'communication and '
                                                                               'escalation support '
                                                                               'is correct.'}},
                                                 {'question': 'A coworker posts a recognizable '
                                                              'photo of your confused patient on '
                                                              'social media “for education,” with '
                                                              'room number visible. The patient '
                                                              'did not consent. What is your '
                                                              'obligation?',
                                                  'options': ['A) Report the privacy breach per '
                                                              'policy, support mitigation, and do '
                                                              'not reshare the image',
                                                              'B) Like and repost to show unit '
                                                              'camaraderie',
                                                              'C) Download the photo for your '
                                                              'personal scrapbook',
                                                              'D) Ignore it because social media '
                                                              'is always allowed for PHI'],
                                                  'answer': 'A) Report the privacy breach per '
                                                            'policy, support mitigation, and do '
                                                            'not reshare the image',
                                                  'explanation': 'Identifiable patient images '
                                                                 'without authorization are '
                                                                 'HIPAA/privacy violations. Nurses '
                                                                 'must report, help contain the '
                                                                 'breach, and avoid further '
                                                                 'dissemination. Social media is '
                                                                 'not a lawful PHI channel.',
                                                  'choice_explanations': {'A': 'Reporting and '
                                                                               'containment '
                                                                               'without resharing '
                                                                               'fulfill privacy '
                                                                               'duties.',
                                                                          'B': 'Reposting '
                                                                               'multiplies the '
                                                                               'breach.',
                                                                          'C': 'Personal copies '
                                                                               'extend '
                                                                               'unauthorized use '
                                                                               'of PHI.',
                                                                          'D': 'Social media is '
                                                                               'not an approved '
                                                                               'PHI disclosure '
                                                                               'path.'}}]},
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
                                                    'C) Always a productive cough with clear focal '
                                                    'findings',
                                                    'D) Guaranteed leukocytosis above 20,000 in '
                                                    'all cases'],
                                        'answer': 'B) New or worsening confusion/falls with or '
                                                  'without fever',
                                        'explanation': 'Older adults often present with delirium, '
                                                       'falls, or functional decline rather than '
                                                       'classic fever and localizing signs. Normal '
                                                       'temperature does not rule out serious '
                                                       'infection.',
                                        'choice_explanations': {'A': 'Fever may be blunted or '
                                                                     'absent in elders.',
                                                                'B': 'Acute confusion/falls are '
                                                                     'classic atypical infection '
                                                                     'cues.',
                                                                'C': 'Many infections lack '
                                                                     'textbook respiratory '
                                                                     'findings.',
                                                                'D': 'Leukocytosis is not '
                                                                     'guaranteed; '
                                                                     'immunocomosenescence blunts '
                                                                     'responses.'}},
                                       {'question': 'Polypharmacy in geriatrics most increases '
                                                    'which risk?',
                                        'options': ['A) Improved adherence automatically with more '
                                                    'pills',
                                                    'B) Complete immunity to adverse drug events',
                                                    'C) Drug interactions, falls, cognitive '
                                                    'impairment, and adherence problems',
                                                    'D) Guaranteed better outcomes with every '
                                                    'added medication'],
                                        'answer': 'C) Drug interactions, falls, cognitive '
                                                  'impairment, and adherence problems',
                                        'explanation': 'Multiple medications raise interaction, '
                                                       'fall, delirium, and nonadherence risks. '
                                                       'Deprescribing review is a geriatric '
                                                       'nursing priority—not celebrating pill '
                                                       'count.',
                                        'choice_explanations': {'A': 'More pills often worsen '
                                                                     'adherence.',
                                                                'B': 'ADE risk rises with regimen '
                                                                     'complexity.',
                                                                'C': 'Interactions, falls, '
                                                                     'cognition, and adherence '
                                                                     'harms define polypharmacy '
                                                                     'risk.',
                                                                'D': 'Added drugs without '
                                                                     'indication can harm more '
                                                                     'than help.'}},
                                       {'question': 'Which nursing actions help prevent pressure '
                                                    'injuries in immobile older adults?',
                                        'options': ['A) Keep the head of bed at 90° continuously '
                                                    'without shifts',
                                                    'B) Massage reddened bony prominences '
                                                    'vigorously',
                                                    'C) Use a donut ring pillow under the sacrum '
                                                    'at all times',
                                                    'D) Reposition regularly, optimize '
                                                    'nutrition/moisture, and use '
                                                    'pressure-redistributing surfaces'],
                                        'answer': 'D) Reposition regularly, optimize '
                                                  'nutrition/moisture, and use '
                                                  'pressure-redistributing surfaces',
                                        'explanation': 'Pressure-injury prevention combines '
                                                       'turning schedules, skin moisture '
                                                       'management, nutrition, and support '
                                                       'surfaces. Massaging damaged tissue, donut '
                                                       'devices, and constant high Fowler’s '
                                                       'without offloading increase injury risk.',
                                        'choice_explanations': {'A': 'Constant high Fowler’s '
                                                                     'increases shear/pressure on '
                                                                     'the sacrum.',
                                                                'B': 'Massaging reddened areas can '
                                                                     'deepen tissue injury.',
                                                                'C': 'Donut rings focus pressure '
                                                                     'at edges and are '
                                                                     'discouraged.',
                                                                'D': 'Repositioning, '
                                                                     'nutrition/moisture care, and '
                                                                     'support surfaces are '
                                                                     'prevention pillars.'}}],
                              'medium': [{'question': 'What do the Beers Criteria help clinicians '
                                                      'evaluate in older adults?',
                                          'options': ['A) Potentially inappropriate medications '
                                                      'that carry heightened risk in the elderly',
                                                      'B) Exact shoe sizes for fall mats',
                                                      'C) Only surgical instrument sterilization '
                                                      'methods',
                                                      'D) Preferred television volume levels on '
                                                      'units'],
                                          'answer': 'A) Potentially inappropriate medications that '
                                                    'carry heightened risk in the elderly',
                                          'explanation': 'Beers Criteria list medications that are '
                                                         'potentially inappropriate in older '
                                                         'adults due to adverse-effect profiles. '
                                                         'Nurses use them in med reconciliation '
                                                         'conversations—not for unrelated '
                                                         'environmental trivia.',
                                          'choice_explanations': {'A': 'Identifying high-risk/PIM '
                                                                       'drugs in elders is the '
                                                                       'Beers purpose.',
                                                                  'B': 'Shoe size is unrelated.',
                                                                  'C': 'Sterilization is an '
                                                                       'infection-control domain.',
                                                                  'D': 'TV volume is not a Beers '
                                                                       'domain.'}},
                                         {'question': 'When helping an older adult with '
                                                      'orthostatic hypotension stand, which '
                                                      'nursing tip is best?',
                                          'options': ['A) Stand abruptly from supine in one second',
                                                      'B) Dangle at the bedside, rise slowly, and '
                                                      'wait for dizziness to resolve before '
                                                      'walking',
                                                      'C) Hold all fluids permanently without '
                                                      'orders',
                                                      'D) Encourage hot baths immediately before '
                                                      'standing'],
                                          'answer': 'B) Dangle at the bedside, rise slowly, and '
                                                    'wait for dizziness to resolve before walking',
                                          'explanation': 'Orthostatic precautions use staged '
                                                         'position changes to allow baroreceptor '
                                                         'compensation. Sudden standing, '
                                                         'dehydration, and vasodilation from hot '
                                                         'baths provoke syncope and falls.',
                                          'choice_explanations': {'A': 'Abrupt standing '
                                                                       'precipitates orthostatic '
                                                                       'syncope.',
                                                                  'B': 'Slow staged rising is the '
                                                                       'correct orthostatic '
                                                                       'technique.',
                                                                  'C': 'Unordered fluid '
                                                                       'withholding may worsen '
                                                                       'orthostasis.',
                                                                  'D': 'Heat causes vasodilation '
                                                                       'that worsens '
                                                                       'hypotension.'}},
                                         {'question': 'Which feature best helps distinguish '
                                                      'delirium from dementia at the bedside?',
                                          'options': ['A) Delirium is always chronic over years '
                                                      'without fluctuation',
                                                      'B) Dementia always starts in minutes after '
                                                      'a UTI',
                                                      'C) Delirium is acute/fluctuating and often '
                                                      'reversible with treatable causes; dementia '
                                                      'is acquired progressive cognitive decline',
                                                      'D) They are identical terms with no '
                                                      'clinical difference'],
                                          'answer': 'C) Delirium is acute/fluctuating and often '
                                                    'reversible with treatable causes; dementia is '
                                                    'acquired progressive cognitive decline',
                                          'explanation': 'Delirium is an acute, fluctuating '
                                                         'attention/awareness disturbance often '
                                                         'due to infection, meds, or metabolic '
                                                         'insult—and potentially reversible. '
                                                         'Dementia is a chronic progressive '
                                                         'decline. Mislabeling delirium as '
                                                         'dementia delays life-saving workup.',
                                          'choice_explanations': {'A': 'Chronic nonfluctuating '
                                                                       'course describes dementia '
                                                                       'more than delirium.',
                                                                  'B': 'Minutes-to-hours onset '
                                                                       'after illness suggests '
                                                                       'delirium, not dementia '
                                                                       'onset.',
                                                                  'C': 'Acute fluctuating vs '
                                                                       'chronic progressive is the '
                                                                       'key distinction.',
                                                                  'D': 'The distinction drives '
                                                                       'urgent medical '
                                                                       'evaluation.'}}],
                              'hard': [{'question': 'If a nurse suspects elder abuse in a '
                                                    'long-term care resident, what is the duty?',
                                        'options': ['A) Keep it private to protect the facility’s '
                                                    'reputation',
                                                    'B) Confront the suspected abuser alone in a '
                                                    'secluded area without a plan',
                                                    'C) Wait for photographic proof beyond any '
                                                    'doubt before acting',
                                                    'D) Ensure safety and report per mandatory '
                                                    'elder-abuse reporting laws'],
                                        'answer': 'D) Ensure safety and report per mandatory '
                                                  'elder-abuse reporting laws',
                                        'explanation': 'Nurses are mandatory reporters of '
                                                       'suspected elder abuse. Reasonable '
                                                       'suspicion triggers reporting and '
                                                       'protective action; facility reputation and '
                                                       'solitary confrontation are inappropriate.',
                                        'choice_explanations': {'A': 'Reputation does not override '
                                                                     'mandated reporting.',
                                                                'B': 'Lone confrontation can '
                                                                     'escalate danger and spoil '
                                                                     'investigations.',
                                                                'C': 'Suspicion, not courtroom '
                                                                     'proof, is the reporting '
                                                                     'threshold.',
                                                                'D': 'Safety plus mandatory '
                                                                     'reporting is the required '
                                                                     'response.'}},
                                       {'question': 'For an older adult with dementia who wanders, '
                                                    'which approach is a preferred restraint '
                                                    'alternative?',
                                        'options': ['A) Supervised ambulation, door alarms, '
                                                    'meaningful activities, and environmental '
                                                    'modification before restraints',
                                                    'B) Immediate four-point leather restraints on '
                                                    'admission',
                                                    'C) Chemical sedation as first-line for all '
                                                    'wanderers without assessment',
                                                    'D) Locking the person in a dark closet'],
                                        'answer': 'A) Supervised ambulation, door alarms, '
                                                  'meaningful activities, and environmental '
                                                  'modification before restraints',
                                        'explanation': 'Least-restrictive dementia care uses '
                                                       'supervision, alarms, activities, and '
                                                       'environment before restraints. Restraints '
                                                       'and punitive confinement increase injury '
                                                       'and trauma; chemical restraint without '
                                                       'assessment is inappropriate first-line '
                                                       'care.',
                                        'choice_explanations': {'A': 'Nonpharmacologic, '
                                                                     'least-restrictive strategies '
                                                                     'are preferred wander '
                                                                     'management.',
                                                                'B': 'Restraints are last resort '
                                                                     'with strict criteria, not '
                                                                     'admission defaults.',
                                                                'C': 'Sedation without assessment '
                                                                     'risks delirium and falls.',
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
                                                    'D) Weight is unrelated to volume status in '
                                                    'HF'],
                                        'answer': 'B) Sudden gains often signal fluid retention '
                                                  'needing early intervention before frank '
                                                  'decompensation',
                                        'explanation': 'Rapid weight gain is an early congestion '
                                                       'marker in HF, prompting diet/diuretic '
                                                       'reassessment. It complements—not '
                                                       'replaces—symptom and exam assessment.',
                                        'choice_explanations': {'A': 'Overnight kilogram gains are '
                                                                     'fluid, not muscle.',
                                                                'B': 'Early fluid detection '
                                                                     'enables intervention before '
                                                                     'hospitalization.',
                                                                'C': 'Symptoms and exam remain '
                                                                     'essential alongside weights.',
                                                                'D': 'Weight is a practical volume '
                                                                     'proxy in HF.'}}],
                              'extreme': [{'question': 'An 88-year-old with osteoporosis is found '
                                                       'on the floor after a fall, reporting '
                                                       'severe hip pain and external rotation of '
                                                       'the leg. She is on anticoagulants; BP is '
                                                       '88/50; and a family member demands she '
                                                       'stand to “walk it off” before imaging. '
                                                       'What is the priority?',
                                           'options': ['A) Force ambulation to prevent stiffness',
                                                       'B) Give a NSAID cocktail and discharge '
                                                       'home immediately',
                                                       'C) Immobilize/support the limb, treat '
                                                       'shock, hold unsafe movement, escalate for '
                                                       'fracture/bleeding evaluation, and keep NPO '
                                                       'for possible surgery',
                                                       'D) Remove anticoagulation charts so '
                                                       'surgery is simpler later'],
                                           'answer': 'C) Immobilize/support the limb, treat shock, '
                                                     'hold unsafe movement, escalate for '
                                                     'fracture/bleeding evaluation, and keep NPO '
                                                     'for possible surgery',
                                           'explanation': 'Shortened externally rotated leg after '
                                                          'fall suggests hip fracture. '
                                                          'Anticoagulation plus hypotension raise '
                                                          'hemorrhage concern. Priorities: '
                                                          'immobilize, ABC/shock care, no '
                                                          'weight-bearing, urgent evaluation—not '
                                                          'ambulation or chart destruction.',
                                           'choice_explanations': {'A': 'Ambulation can worsen '
                                                                        'fracture displacement and '
                                                                        'bleeding.',
                                                                   'B': 'NSAIDs plus premature '
                                                                        'discharge ignore '
                                                                        'fracture/shock risk.',
                                                                   'C': 'Immobilization, shock '
                                                                        'care, and surgical workup '
                                                                        'readiness are correct.',
                                                                   'D': 'Hiding anticoagulation '
                                                                        'endangers perioperative '
                                                                        'safety.'}},
                                          {'question': 'A frail nursing-home resident develops new '
                                                       'lethargy, anorexia, and falls without '
                                                       'fever. Urine is foul; BP drops to 80/40; '
                                                       'lactate is rising. Staff say “old people '
                                                       'get confused—just watch.” What should you '
                                                       'do?',
                                           'options': ['A) Agree and defer vitals until tomorrow',
                                                       'B) Encourage vigorous exercise testing now',
                                                       'C) Give a large oral water challenge while '
                                                       'supine hypotension persists',
                                                       'D) Recognize possible sepsis with atypical '
                                                       'signs, support ABCs, obtain cultures/labs '
                                                       'per protocol, and escalate urgently '
                                                       'despite lack of high fever'],
                                           'answer': 'D) Recognize possible sepsis with atypical '
                                                     'signs, support ABCs, obtain cultures/labs '
                                                     'per protocol, and escalate urgently despite '
                                                     'lack of high fever',
                                           'explanation': 'Frail elders often show sepsis as '
                                                          'delirium, falls, and anorexia without '
                                                          'high fever. Hypotension and rising '
                                                          'lactate indicate hypoperfusion '
                                                          'requiring sepsis pathways—not watchful '
                                                          'neglect.',
                                           'choice_explanations': {'A': 'Deferring assessment '
                                                                        'during hypotension is '
                                                                        'dangerous.',
                                                                   'B': 'Exercise testing is '
                                                                        'contraindicated in shock.',
                                                                   'C': 'Oral fluid challenges are '
                                                                        'unsafe in hypotensive '
                                                                        'possible sepsis without '
                                                                        'IV access/plan.',
                                                                   'D': 'Atypical sepsis '
                                                                        'recognition with ABC '
                                                                        'support and escalation is '
                                                                        'required.'}},
                                          {'question': 'At end of life, a capacitated older '
                                                       'adult’s advance directive declines '
                                                       'intubation. The adult child demands “full '
                                                       'code for guilt reasons,” and a covering '
                                                       'resident writes intubation orders. The '
                                                       'patient remains alert and refuses. What is '
                                                       'the correct nursing action?',
                                           'options': ['A) Uphold the patient’s directive and '
                                                       'current refusal; escalate to '
                                                       'attending/ethics/chain of command; do not '
                                                       'intubate against capacitated refusal',
                                                       'B) Hide the advance directive and proceed '
                                                       'to intubation',
                                                       'C) Tell the patient autonomy no longer '
                                                       'applies after age 80',
                                                       'D) Follow the child’s demands because '
                                                       'family always outranks the patient'],
                                           'answer': 'A) Uphold the patient’s directive and '
                                                     'current refusal; escalate to '
                                                     'attending/ethics/chain of command; do not '
                                                     'intubate against capacitated refusal',
                                           'explanation': 'Capacitated patients’ contemporaneous '
                                                          'refusals and valid advance directives '
                                                          'prevail over conflicting family guilt '
                                                          'and erroneous orders. Nurses refuse '
                                                          'unsafe/unwanted intubation and escalate '
                                                          'through leadership/ethics for order '
                                                          'correction.',
                                           'choice_explanations': {'A': 'Honoring capacitated '
                                                                        'refusal/directive with '
                                                                        'escalation is ethically '
                                                                        'and legally required.',
                                                                   'B': 'Concealing directives to '
                                                                        'force intubation violates '
                                                                        'autonomy and law.',
                                                                   'C': 'Age does not erase '
                                                                        'autonomy.',
                                                                   'D': 'Family preference does '
                                                                        'not outrank a capacitated '
                                                                        'patient’s decision.'}}]},
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
