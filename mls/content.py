"""Undergraduate MLS study content by specialty and difficulty."""
from __future__ import annotations

import random

from quiz_bank import DIFFICULTIES, DIFFICULTY_LABELS, LABEL_TO_DIFFICULTY

SPECIALTY_ORDER = ['hematology', 'clinical_chemistry', 'medical_microbiology', 'immunology', 'blood_bank', 'histopathology', 'parasitology', 'molecular_diagnostics', 'lab_qa', 'urinalysis']

SPECIALTIES: dict[str, dict] = {'hematology': {'label': 'Hematology',
                'books': ['Clinical Hematology — Rodak',
                          "Hoffbrand's Essential Haematology",
                          'CLSI hematology method documents'],
                'pdf_notes': ['Always correlate CBC with smear morphology.',
                              'Microcytic anemia: iron deficiency vs thalassemia themes.',
                              'Blasts on smear = urgent hematology review.',
                              'PT/INR vs aPTT vs anti-Xa — know what each monitors.',
                              'Preanalytic errors (clotted/hemolyzed) invalidate many results.'],
                'questions': {'easy': [{'question': 'Normal adult male hemoglobin roughly?',
                                        'options': ['A) About 13–17 g/dL (lab-dependent)',
                                                    'B) 3 g/dL',
                                                    'C) 30 g/dL always',
                                                    'D) 0.5 g/dL'],
                                        'answer': 'A) About 13–17 g/dL (lab-dependent)',
                                        'explanation': 'Know local reference ranges.'},
                                       {'question': 'CBC primarily measures?',
                                        'options': ['A) Blood cell counts and indices',
                                                    'B) Only electrolytes',
                                                    'C) Only liver enzymes',
                                                    'D) Only blood gases'],
                                        'answer': 'A) Blood cell counts and indices',
                                        'explanation': 'Core hematology test.'},
                                       {'question': 'Anemia means?',
                                        'options': ['A) Low hemoglobin/RBC mass for age/sex',
                                                    'B) Always high WBC',
                                                    'C) Always high platelets',
                                                    'D) Always normal oxygen forever'],
                                        'answer': 'A) Low hemoglobin/RBC mass for age/sex',
                                        'explanation': 'Classify morphologically/kinetically.'}],
                              'medium': [{'question': 'Schistocytes suggest?',
                                          'options': ['A) Microangiopathic hemolysis',
                                                      'B) Only iron deficiency always',
                                                      'C) Only B12 deficiency only',
                                                      'D) Only artifact never pathology'],
                                          'answer': 'A) Microangiopathic hemolysis',
                                          'explanation': 'Think TTP/DIC/HUS contexts.'},
                                         {'question': 'Left shift means?',
                                          'options': ['A) Increased immature neutrophils',
                                                      'B) Only low lymphocytes always',
                                                      'C) Only eosinophilia only',
                                                      'D) Only basophilia only'],
                                          'answer': 'A) Increased immature neutrophils',
                                          'explanation': 'Infection/stress response.'},
                                         {'question': 'INR monitors?',
                                          'options': ['A) Warfarin / extrinsic pathway themes',
                                                      'B) Only heparin anti-Xa always exclusively',
                                                      'C) Only bleeding time only',
                                                      'D) Only D-dimer only'],
                                          'answer': 'A) Warfarin / extrinsic pathway themes',
                                          'explanation': 'PT/INR system.'}],
                              'hard': [{'question': 'A junior colleague asks for the single best '
                                                    'answer. PNH relates to? Beware of near-miss '
                                                    'distractors.',
                                        'options': ['A) Complement-mediated hemolysis due to '
                                                    'GPI-anchor defect',
                                                    'B) Only iron overload diet',
                                                    'C) Only folate excess',
                                                    'D) Only splenic sequestration only forever'],
                                        'answer': 'A) Complement-mediated hemolysis due to '
                                                  'GPI-anchor defect',
                                        'explanation': 'Flow cytometry diagnosis themes.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. AML vs ALL distinction uses? Beware '
                                                    'of near-miss distractors.',
                                        'options': ['A) Morphology + '
                                                    'cytochemistry/immunophenotype/genetics',
                                                    'B) Only patient age forever alone',
                                                    'C) Only Hb value alone',
                                                    'D) Only platelet count alone'],
                                        'answer': 'A) Morphology + '
                                                  'cytochemistry/immunophenotype/genetics',
                                        'explanation': 'WHO classification.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. HIT is? Beware of near-miss '
                                                    'distractors.',
                                        'options': ['A) Heparin-induced thrombocytopenia — immune, '
                                                    'thrombosis risk',
                                                    'B) Always benign platelet clumping only',
                                                    'C) Only iron deficiency',
                                                    'D) Only B12 deficiency'],
                                        'answer': 'A) Heparin-induced thrombocytopenia — immune, '
                                                  'thrombosis risk',
                                        'explanation': 'Stop heparin; use alternative '
                                                       'anticoagulation pathways.'}],
                              'extreme': [{'question': 'In a high-stakes laboratory scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? APML emergency risk? Avoid '
                                                       'actions that could harm if a critical risk '
                                                       'remains open.',
                                           'options': ['A) DIC / bleeding — urgent ATRA pathway '
                                                       'themes',
                                                       'B) Only mild iron deficiency',
                                                       'C) Only allergic rhinitis',
                                                       'D) Only dehydration'],
                                           'answer': 'A) DIC / bleeding — urgent ATRA pathway '
                                                     'themes',
                                           'explanation': 'Recognize promyelocytes/Auer rods '
                                                          'cues.'},
                                          {'question': 'In a high-stakes laboratory scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? TTP pentad classic teaching '
                                                       'includes? Avoid actions that could harm if '
                                                       'a critical risk remains open.',
                                           'options': ['A) MAHA, thrombocytopenia, neurologic '
                                                       'change (± renal/fever)',
                                                       'B) Only isolated neutropenia',
                                                       'C) Only polycythemia alone',
                                                       'D) Only eosinophilia'],
                                           'answer': 'A) MAHA, thrombocytopenia, neurologic change '
                                                     '(± renal/fever)',
                                           'explanation': 'ADAMTS13; plasma exchange themes.'},
                                          {'question': 'In a high-stakes laboratory scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Flow cytometry MRD aims to? Avoid '
                                                       'actions that could harm if a critical risk '
                                                       'remains open.',
                                           'options': ['A) Detect residual disease below '
                                                       'morphology threshold',
                                                       'B) Replace all coagulation tests',
                                                       'C) Measure only glucose',
                                                       'D) Only blood type'],
                                           'answer': 'A) Detect residual disease below morphology '
                                                     'threshold',
                                           'explanation': 'Treatment response monitoring.'}]},
                'cases': {'easy': [{'title': 'Fatigue + Low Hb',
                                    'stem': 'A young woman has fatigue; Hb 9.5 g/dL, MCV low.',
                                    'question': 'Likely anemia type theme?',
                                    'answer': 'Microcytic anemia — consider iron deficiency among '
                                              'differentials.',
                                    'discussion': 'Check iron studies/smear as indicated.',
                                    'book_hint': 'Clinical Hematology — Rodak / Hoffbrand'}],
                          'medium': [{'title': 'Fever + Blasts',
                                      'stem': 'CBC shows marked leukocytosis with circulating '
                                              'blasts and anemia/thrombocytopenia.',
                                      'question': 'Concern?',
                                      'answer': 'Acute leukemia until proven otherwise — urgent '
                                                'hematology workup.',
                                      'discussion': 'Do not delay smear review.',
                                      'book_hint': 'Clinical Hematology — Rodak / Hoffbrand'}],
                          'hard': [{'title': 'Post-Heparin Platelet Drop + Clot',
                                    'stem': 'Platelets fall by >50% after heparin; new thrombosis. '
                                            'Choose the safest high-yield next laboratory concept.',
                                    'question': 'Suspect?',
                                    'answer': 'HIT — discontinue heparin and manage per protocol.',
                                    'discussion': 'Do not just transfuse platelets routinely '
                                                  'without guidance.',
                                    'book_hint': 'Clinical Hematology — Rodak / Hoffbrand'}],
                          'extreme': [{'title': 'Schistocytes + Low Plt + Confusion',
                                       'stem': 'MAHA, thrombocytopenia, neurologic changes; coag '
                                               'relatively less DIC-like. Avoid reporting or '
                                               'actions that could harm if a critical quality risk '
                                               'remains open.',
                                       'question': 'Top concern?',
                                       'answer': 'TTP — urgent specialist therapy (exchange '
                                                 'pathways).',
                                       'discussion': 'Time-critical.',
                                       'book_hint': 'Clinical Hematology — Rodak / Hoffbrand'}]}},
 'clinical_chemistry': {'label': 'Clinical Chemistry',
                        'books': ['Tietz Fundamentals of Clinical Chemistry',
                                  'Clinical Chemistry — Bishop',
                                  'CLSI chemistry documents'],
                        'pdf_notes': ['Hemolysis falsely elevates K+ — reject/redraw when '
                                      'indicated.',
                                      'Know critical value notification pathways.',
                                      'Enzyme panels: pattern recognition > single numbers.',
                                      'Method interference and reference ranges are lab-specific.',
                                      'Preanalytic → analytic → postanalytic thinking prevents '
                                      'errors.'],
                        'questions': {'easy': [{'question': 'Electrolyte panel commonly includes?',
                                                'options': ['A) Na, K, Cl, bicarbonate themes',
                                                            'B) Only HbA1c',
                                                            'C) Only blood film',
                                                            'D) Only PT only'],
                                                'answer': 'A) Na, K, Cl, bicarbonate themes',
                                                'explanation': 'Basic metabolic themes.'},
                                               {'question': 'Creatinine mainly reflects?',
                                                'options': ['A) Kidney filtration function roughly',
                                                            'B) Only liver synthetic function '
                                                            'alone',
                                                            'C) Only muscle enzymes only forever',
                                                            'D) Only amylase only'],
                                                'answer': 'A) Kidney filtration function roughly',
                                                'explanation': 'eGFR derived.'},
                                               {'question': 'Hypoglycemia means?',
                                                'options': ['A) Low blood glucose',
                                                            'B) Always high glucose',
                                                            'C) Only high ketones without glucose '
                                                            'context',
                                                            'D) Only high Hb'],
                                                'answer': 'A) Low blood glucose',
                                                'explanation': 'Critical value pathways.'}],
                                      'medium': [{'question': 'AST/ALT pattern helps assess?',
                                                  'options': ['A) Hepatocellular injury',
                                                              'B) Only bone disease exclusively',
                                                              'C) Only hemolysis exclusively '
                                                              'forever',
                                                              'D) Only thyroid only'],
                                                  'answer': 'A) Hepatocellular injury',
                                                  'explanation': 'ALP/GGT more cholestatic '
                                                                 'themes.'},
                                                 {'question': 'Troponin rise suggests?',
                                                  'options': ['A) Myocardial injury',
                                                              'B) Only UTI',
                                                              'C) Only anemia',
                                                              'D) Only caries'],
                                                  'answer': 'A) Myocardial injury',
                                                  'explanation': 'Interpret with clinical ACS '
                                                                 'context.'},
                                                 {'question': 'HbA1c reflects?',
                                                  'options': ['A) Average glycemia over ~2–3 '
                                                              'months',
                                                              "B) Only today's glucose",
                                                              'C) Only urine glucose',
                                                              'D) Only insulin dose brand'],
                                                  'answer': 'A) Average glycemia over ~2–3 months',
                                                  'explanation': 'Diabetes monitoring.'}],
                                      'hard': [{'question': 'A junior colleague asks for the '
                                                            'single best answer. Osmolal gap '
                                                            'increases with? Beware of near-miss '
                                                            'distractors.',
                                                'options': ['A) Osmotically active toxins (e.g., '
                                                            'alcohols) among causes',
                                                            'B) Only normal saline always',
                                                            'C) Only oxygen therapy',
                                                            'D) Only vitamins'],
                                                'answer': 'A) Osmotically active toxins (e.g., '
                                                          'alcohols) among causes',
                                                'explanation': 'Toxic alcohol workup.'},
                                               {'question': 'A junior colleague asks for the '
                                                            'single best answer. Hook effect can '
                                                            'cause? Beware of near-miss '
                                                            'distractors.',
                                                'options': ['A) Falsely low immunoassay results at '
                                                            'very high analyte',
                                                            'B) Always accurate highs',
                                                            'C) Only color change of tubes',
                                                            'D) Only barcode errors'],
                                                'answer': 'A) Falsely low immunoassay results at '
                                                          'very high analyte',
                                                'explanation': 'Dilute and repeat.'},
                                               {'question': 'A junior colleague asks for the '
                                                            'single best answer. '
                                                            'Pseudohyponatremia classic with? '
                                                            'Beware of near-miss distractors.',
                                                'options': ['A) Severe '
                                                            'hyperlipidemia/hyperproteinemia '
                                                            '(older methods)',
                                                            'B) Always true low Na only',
                                                            'C) Only dehydration forever',
                                                            'D) Only SIADH always'],
                                                'answer': 'A) Severe '
                                                          'hyperlipidemia/hyperproteinemia (older '
                                                          'methods)',
                                                'explanation': 'Method-dependent.'}],
                                      'extreme': [{'question': 'In a high-stakes laboratory '
                                                               'scenario with incomplete data, '
                                                               'which statement is MOST correct? '
                                                               'Critical value policy requires? '
                                                               'Avoid actions that could harm if a '
                                                               'critical risk remains open.',
                                                   'options': ['A) Rapid clinician notification '
                                                               'and documentation',
                                                               'B) Filing only next week',
                                                               'C) Ignoring repeats',
                                                               'D) Only emailing patient directly '
                                                               'always'],
                                                   'answer': 'A) Rapid clinician notification and '
                                                             'documentation',
                                                   'explanation': 'Patient safety.'},
                                                  {'question': 'In a high-stakes laboratory '
                                                               'scenario with incomplete data, '
                                                               'which statement is MOST correct? '
                                                               'Delta check flags? Avoid actions '
                                                               'that could harm if a critical risk '
                                                               'remains open.',
                                                   'options': ['A) Implausible change vs prior '
                                                               'results',
                                                               'B) Only new patient names',
                                                               'C) Only tube color preferences',
                                                               'D) Only printer jams'],
                                                   'answer': 'A) Implausible change vs prior '
                                                             'results',
                                                   'explanation': 'Quality/error detection.'},
                                                  {'question': 'In a high-stakes laboratory '
                                                               'scenario with incomplete data, '
                                                               'which statement is MOST correct? '
                                                               'Blood gas preanalytics: air '
                                                               'bubbles cause? Avoid actions that '
                                                               'could harm if a critical risk '
                                                               'remains open.',
                                                   'options': ['A) Distorted pO2/pCO2',
                                                               'B) Better accuracy always',
                                                               'C) No effect ever',
                                                               'D) Only higher glucose'],
                                                   'answer': 'A) Distorted pO2/pCO2',
                                                   'explanation': 'Expel air; analyze promptly.'}]},
                        'cases': {'easy': [{'title': 'High K on Lab Call',
                                            'stem': 'Lab flags K 6.8 mmol/L.',
                                            'question': 'First lab/clinical check?',
                                            'answer': 'Rule out hemolysis/EDTA contamination; '
                                                      'inform clinician for ECG/treatment.',
                                            'discussion': 'Preanalytical errors common.',
                                            'book_hint': 'Tietz Textbook of Clinical Chemistry'}],
                                  'medium': [{'title': 'Jaundice Labs',
                                              'stem': 'High bilirubin with high ALP/GGT '
                                                      'predominance.',
                                              'question': 'Pattern?',
                                              'answer': 'Cholestatic/obstructive theme — correlate '
                                                        'imaging.',
                                              'discussion': 'vs hepatocellular AST/ALT dominant.',
                                              'book_hint': 'Tietz Textbook of Clinical Chemistry'}],
                                  'hard': [{'title': 'Very High hCG but Assay Low',
                                            'stem': 'Clinical molar pregnancy suspected; hCG '
                                                    'unexpectedly not sky-high. Choose the safest '
                                                    'high-yield next laboratory concept.',
                                            'question': 'Consider?',
                                            'answer': 'Hook effect — dilute specimen.',
                                            'discussion': 'Communicate with lab.',
                                            'book_hint': 'Tietz Textbook of Clinical Chemistry'}],
                                  'extreme': [{'title': 'Mismatch Glucose POCT vs Lab',
                                               'stem': 'Fingerstick 45 mg/dL; venous lab 110 mg/dL '
                                                       'in shocked patient. Avoid reporting or '
                                                       'actions that could harm if a critical '
                                                       'quality risk remains open.',
                                               'question': 'Concept?',
                                               'answer': 'POCT limitations in poor perfusion — '
                                                         'confirm critically with lab method.',
                                               'discussion': 'Treat patient, verify method.',
                                               'book_hint': 'Tietz Textbook of Clinical '
                                                            'Chemistry'}]}},
 'medical_microbiology': {'label': 'Medical Microbiology',
                          'books': ["Bailey & Scott's Diagnostic Microbiology",
                                    'CLSI M100',
                                    'Murray Medical Microbiology'],
                          'pdf_notes': ['Gram stain guides early therapy and culture workup.',
                                        'AST breakpoints are CLSI/EUCAST version-dependent.',
                                        'Blood culture contamination vs true bacteremia matters.',
                                        'Biosafety: never smell plates; escalate select agents '
                                        'correctly.',
                                        'Stewardship: report actionable MICs and resistance '
                                        'alerts.'],
                          'questions': {'easy': [{'question': 'Gram-positive organisms stain?',
                                                  'options': ['A) Purple/blue',
                                                              'B) Always pink only',
                                                              'C) Always colorless forever',
                                                              'D) Always acid-fast only'],
                                                  'answer': 'A) Purple/blue',
                                                  'explanation': 'Cell wall differences.'},
                                                 {'question': 'Blood culture indication theme?',
                                                  'options': ['A) Suspected bacteremia/sepsis',
                                                              'B) Only routine wellness',
                                                              'C) Only anemia workup alone',
                                                              'D) Only lipid panel'],
                                                  'answer': 'A) Suspected bacteremia/sepsis',
                                                  'explanation': 'Volume and timing matter.'},
                                                 {'question': 'Antibiotic susceptibility testing '
                                                              'guides?',
                                                  'options': ['A) Therapy choice',
                                                              'B) Only hospital food menus',
                                                              'C) Only bed assignment',
                                                              'D) Only billing codes alone'],
                                                  'answer': 'A) Therapy choice',
                                                  'explanation': 'Interpret with breakpoints.'}],
                                        'medium': [{'question': 'Acid-fast stain used for?',
                                                    'options': ['A) Mycobacteria',
                                                                'B) Only streptococci',
                                                                'C) Only Candida always only',
                                                                'D) Only viruses'],
                                                    'answer': 'A) Mycobacteria',
                                                    'explanation': 'TB workup.'},
                                                   {'question': 'Catalase-positive gram-positive '
                                                                'cocci suggest?',
                                                    'options': ['A) Staphylococci',
                                                                'B) Streptococci typically',
                                                                'C) Enterococci always catalase+++ '
                                                                'classic teaching opposite',
                                                                'D) Only Neisseria'],
                                                    'answer': 'A) Staphylococci',
                                                    'explanation': 'Strep usually '
                                                                   'catalase-negative.'},
                                                   {'question': 'CSF Gram stain urgency?',
                                                    'options': ['A) Critical for meningitis',
                                                                'B) Can wait days always',
                                                                'C) Only research interest',
                                                                'D) Never report'],
                                                    'answer': 'A) Critical for meningitis',
                                                    'explanation': 'Call critical positives.'}],
                                        'hard': [{'question': 'A junior colleague asks for the '
                                                              'single best answer. MRSA detected '
                                                              'by? Beware of near-miss '
                                                              'distractors.',
                                                  'options': ['A) Oxacillin/cefoxitin testing / '
                                                              'mecA themes',
                                                              'B) Only optochin',
                                                              'C) Only bile esculin',
                                                              'D) Only coagulase negative always'],
                                                  'answer': 'A) Oxacillin/cefoxitin testing / mecA '
                                                            'themes',
                                                  'explanation': 'Infection control implications.'},
                                                 {'question': 'A junior colleague asks for the '
                                                              'single best answer. Anaerobic '
                                                              'culture needs? Beware of near-miss '
                                                              'distractors.',
                                                  'options': ['A) Proper anaerobic '
                                                              'transport/conditions',
                                                              'B) Open air plates only',
                                                              'C) Fridge only forever',
                                                              'D) No media'],
                                                  'answer': 'A) Proper anaerobic '
                                                            'transport/conditions',
                                                  'explanation': 'Preanalytics crucial.'},
                                                 {'question': 'A junior colleague asks for the '
                                                              'single best answer. Blood culture '
                                                              'contamination clues? Beware of '
                                                              'near-miss distractors.',
                                                  'options': ['A) Skin flora in 1 of multiple sets',
                                                              'B) Same pathogen in all sets always '
                                                              'contamination',
                                                              'C) Never happens',
                                                              'D) Only fungal always true'],
                                                  'answer': 'A) Skin flora in 1 of multiple sets',
                                                  'explanation': 'Interpret clinically.'}],
                                        'extreme': [{'question': 'In a high-stakes laboratory '
                                                                 'scenario with incomplete data, '
                                                                 'which statement is MOST correct? '
                                                                 'Carbapenemase-producing '
                                                                 'Enterobacterales require? Avoid '
                                                                 'actions that could harm if a '
                                                                 'critical risk remains open.',
                                                     'options': ['A) Infection control + '
                                                                 'specialized testing/therapy '
                                                                 'stewardship',
                                                                 'B) Ignore resistance',
                                                                 'C) Always only amoxicillin',
                                                                 'D) No reporting'],
                                                     'answer': 'A) Infection control + specialized '
                                                               'testing/therapy stewardship',
                                                     'explanation': 'Public health threat.'},
                                                    {'question': 'In a high-stakes laboratory '
                                                                 'scenario with incomplete data, '
                                                                 'which statement is MOST correct? '
                                                                 'Biosafety for Neisseria '
                                                                 'meningitidis work? Avoid actions '
                                                                 'that could harm if a critical '
                                                                 'risk remains open.',
                                                     'options': ['A) Appropriate BSL practices; '
                                                                 'protect staff',
                                                                 'B) Open bench sniffing cultures',
                                                                 'C) No PPE ever',
                                                                 'D) Mouth pipetting'],
                                                     'answer': 'A) Appropriate BSL practices; '
                                                               'protect staff',
                                                     'explanation': 'Lab-acquired infection risk.'},
                                                    {'question': 'In a high-stakes laboratory '
                                                                 'scenario with incomplete data, '
                                                                 'which statement is MOST correct? '
                                                                 'MALDI-TOF identifies? Avoid '
                                                                 'actions that could harm if a '
                                                                 'critical risk remains open.',
                                                     'options': ['A) Organisms by protein mass '
                                                                 'spectra',
                                                                 'B) Only electrolytes',
                                                                 'C) Only Hb',
                                                                 'D) Only PT'],
                                                     'answer': 'A) Organisms by protein mass '
                                                               'spectra',
                                                     'explanation': 'Rapid ID technology.'}]},
                          'cases': {'easy': [{'title': 'UTI Culture',
                                              'stem': 'Dysuria; midstream urine culture growing E. '
                                                      'coli >10^5 CFU/mL.',
                                              'question': 'Interpretation theme?',
                                              'answer': 'Consistent with UTI if clinical match; '
                                                        'report susceptibilities.',
                                              'discussion': 'Contamination if mixed flora skin '
                                                            'organisms.',
                                              'book_hint': "Bailey & Scott's Diagnostic "
                                                           'Microbiology'}],
                                    'medium': [{'title': 'CSF Cloudy',
                                                'stem': 'Fever, neck stiffness; CSF WBC high, '
                                                        'Gram-negative diplococci.',
                                                'question': 'Likely?',
                                                'answer': 'Meningococcal meningitis theme — urgent '
                                                          'report/treatment coordination.',
                                                'discussion': 'Lab biosafety.',
                                                'book_hint': "Bailey & Scott's Diagnostic "
                                                             'Microbiology'}],
                                    'hard': [{'title': 'CoNS in One Bottle',
                                              'stem': 'One of four bottles grows '
                                                      'coagulase-negative staph in a non-device '
                                                      'patient. Choose the safest high-yield next '
                                                      'laboratory concept.',
                                              'question': 'Likely?',
                                              'answer': 'Possible contaminant — correlate '
                                                        'clinically; may not treat.',
                                              'discussion': 'Device patients differ.',
                                              'book_hint': "Bailey & Scott's Diagnostic "
                                                           'Microbiology'}],
                                    'extreme': [{'title': 'Possible Brucella on Bench',
                                                 'stem': 'Slow-growing gram-negative coccobacilli '
                                                         'from blood; history of farm exposure. '
                                                         'Avoid reporting or actions that could '
                                                         'harm if a critical quality risk remains '
                                                         'open.',
                                                 'question': 'Action?',
                                                 'answer': 'Stop aerosol-generating work; BSL '
                                                           'precautions; notify; rule out '
                                                           'Brucella.',
                                                 'discussion': 'Do not sniff plates.',
                                                 'book_hint': "Bailey & Scott's Diagnostic "
                                                              'Microbiology'}]}},
 'immunology': {'label': 'Immunology & Serology',
                'books': ['Clinical Immunology textbooks',
                          "Henry's Clinical Diagnosis",
                          'Assay package inserts / IFU'],
                'pdf_notes': ['Sensitivity vs specificity vs PPV/NPV depend on prevalence.',
                              'Syphilis algorithms: nontreponemal + treponemal confirmation '
                              'themes.',
                              'HIV testing follows staged algorithms — do not stop at one '
                              'reactive.',
                              'ANA patterns guide follow-up antibody panels.',
                              'Heterophile antibodies and cross-reactivity cause false results.'],
                'questions': {'easy': [{'question': 'ELISA detects?',
                                        'options': ['A) Antigen or antibody via enzyme-linked '
                                                    'assay',
                                                    'B) Only blood films',
                                                    'C) Only electrolytes',
                                                    'D) Only urine crystals'],
                                        'answer': 'A) Antigen or antibody via enzyme-linked assay',
                                        'explanation': 'Common serology platform.'},
                                       {'question': 'IgM generally indicates?',
                                        'options': ['A) Acute/recent response themes',
                                                    'B) Only lifelong remote immunity always',
                                                    'C) Only allergy only forever',
                                                    'D) Only transfusion reaction only'],
                                        'answer': 'A) Acute/recent response themes',
                                        'explanation': 'Context-dependent.'},
                                       {'question': 'Blood type ABO based on?',
                                        'options': ['A) RBC antigens / plasma isoagglutinins',
                                                    'B) Only RhD alone',
                                                    'C) Only HLA only',
                                                    'D) Only platelet antigens only'],
                                        'answer': 'A) RBC antigens / plasma isoagglutinins',
                                        'explanation': 'Fundamental serology.'}],
                              'medium': [{'question': 'ANA testing used in?',
                                          'options': ['A) Autoimmune disease workups',
                                                      'B) Only UTI',
                                                      'C) Only fracture healing',
                                                      'D) Only caries'],
                                          'answer': 'A) Autoimmune disease workups',
                                          'explanation': 'Pattern/titer interpretation.'},
                                         {'question': 'Window period means?',
                                          'options': ['A) Infection present but markers not yet '
                                                      'detectable',
                                                      'B) Always lifelong immunity',
                                                      'C) Assay never works',
                                                      'D) Only sample clotting'],
                                          'answer': 'A) Infection present but markers not yet '
                                                    'detectable',
                                          'explanation': 'Limit of serology/NAT relevance.'},
                                         {'question': 'Complement C3/C4 low in?',
                                          'options': ['A) Some immune complex diseases (e.g., '
                                                      'lupus nephritis themes)',
                                                      'B) Always healthy states only',
                                                      'C) Only dehydration',
                                                      'D) Only iron deficiency'],
                                          'answer': 'A) Some immune complex diseases (e.g., lupus '
                                                    'nephritis themes)',
                                          'explanation': 'Interpret with clinical.'}],
                              'hard': [{'question': 'A junior colleague asks for the single best '
                                                    'answer. Prozone/hook in serology causes? '
                                                    'Beware of near-miss distractors.',
                                        'options': ['A) False negative at antibody excess',
                                                    'B) Always true positive stronger',
                                                    'C) Only hemolysis',
                                                    'D) Only icterus'],
                                        'answer': 'A) False negative at antibody excess',
                                        'explanation': 'Dilute and repeat.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Flow cytometry immunophenotyping used '
                                                    'for? Beware of near-miss distractors.',
                                        'options': ['A) Leukemia/lymphoma characterization among '
                                                    'uses',
                                                    'B) Only Na measurement',
                                                    'C) Only culture',
                                                    'D) Only ESR only'],
                                        'answer': 'A) Leukemia/lymphoma characterization among '
                                                  'uses',
                                        'explanation': 'CD marker panels.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Rheumatoid factor can interfere with? '
                                                    'Beware of near-miss distractors.',
                                        'options': ['A) Some immunoassays',
                                                    'B) Never any assay',
                                                    'C) Only gram stains',
                                                    'D) Only microhematocrit'],
                                        'answer': 'A) Some immunoassays',
                                        'explanation': 'Know interferences.'}],
                              'extreme': [{'question': 'In a high-stakes laboratory scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Heterophile antibodies may cause? '
                                                       'Avoid actions that could harm if a '
                                                       'critical risk remains open.',
                                           'options': ['A) False immunoassay results',
                                                       'B) Perfect accuracy always',
                                                       'C) Only better cultures',
                                                       'D) Only higher Hb'],
                                           'answer': 'A) False immunoassay results',
                                           'explanation': 'Suspect when clinically discordant.'},
                                          {'question': 'In a high-stakes laboratory scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Quantiferon/IGRA interprets? '
                                                       'Avoid actions that could harm if a '
                                                       'critical risk remains open.',
                                           'options': ['A) TB infection immune response (not '
                                                       'active vs latent alone fully)',
                                                       'B) Active TB location always',
                                                       'C) Only BCG forever identical certainty',
                                                       'D) Only bacterial culture replacement '
                                                       'always'],
                                           'answer': 'A) TB infection immune response (not active '
                                                     'vs latent alone fully)',
                                           'explanation': 'Clinical correlation.'},
                                          {'question': 'In a high-stakes laboratory scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Cryoglobulin handling requires? '
                                                       'Avoid actions that could harm if a '
                                                       'critical risk remains open.',
                                           'options': ['A) Warm collection/transport protocols',
                                                       'B) Ice immediately always for all tests',
                                                       'C) Freeze-thaw repeatedly',
                                                       'D) No special handling'],
                                           'answer': 'A) Warm collection/transport protocols',
                                           'explanation': 'Preanalytics.'}]},
                'cases': {'easy': [{'title': 'HBsAg Positive Screen',
                                    'stem': 'Donor/patient HBsAg reactive.',
                                    'question': 'Next?',
                                    'answer': 'Confirm per algorithm; notify; do not release as '
                                              'negative.',
                                    'discussion': 'Viral marker algorithms.',
                                    'book_hint': "Clinical Immunology texts / Henry's Clinical "
                                                 'Diagnosis'}],
                          'medium': [{'title': 'HIV Ag/Ab Reactive',
                                      'stem': 'Screen reactive on automated assay.',
                                      'question': 'Lab next step?',
                                      'answer': 'Follow confirmatory algorithm / differentiation '
                                                'assay per guidelines.',
                                      'discussion': 'Never report final on single screen alone '
                                                    'where algorithm requires more.',
                                      'book_hint': "Clinical Immunology texts / Henry's Clinical "
                                                   'Diagnosis'}],
                          'hard': [{'title': 'Discordant Hepatitis Serology',
                                    'stem': 'Unusual HBsAg/anti-HBc pattern. Choose the safest '
                                            'high-yield next laboratory concept.',
                                    'question': 'Approach?',
                                    'answer': 'Repeat, review vaccine/infection history, use '
                                              'supplemental tests, consult specialist algorithm.',
                                    'discussion': 'Avoid overinterpretation.',
                                    'book_hint': "Clinical Immunology texts / Henry's Clinical "
                                                 'Diagnosis'}],
                          'extreme': [{'title': 'Assay Positive but Patient Well',
                                       'stem': 'Tumor marker extremely high; imaging negative; '
                                               'suspicion of interference. Avoid reporting or '
                                               'actions that could harm if a critical quality risk '
                                               'remains open.',
                                       'question': 'Actions?',
                                       'answer': 'Discuss interference workup (heterophile '
                                                 'blocking, dilutions, alternate method).',
                                       'discussion': 'Prevent unnecessary procedures.',
                                       'book_hint': "Clinical Immunology texts / Henry's Clinical "
                                                    'Diagnosis'}]}},
 'blood_bank': {'label': 'Blood Bank / Transfusion',
                'books': ['AABB Technical Manual',
                          'Blood Banking and Transfusion Medicine texts',
                          'Hospital blood bank SOPs'],
                'pdf_notes': ['ABO discrepancy must be resolved before routine transfusion.',
                              'Type & screen vs type & crossmatch — know indications.',
                              'Acute hemolytic reaction: stop transfusion, keep line open with '
                              'saline, notify BB.',
                              'Emergency release O-negative / group-specific protocols need '
                              'documentation.',
                              'Antibody ID panels before issuing antigen-negative units when '
                              'needed.'],
                'questions': {'easy': [{'question': 'Forward typing detects?',
                                        'options': ['A) RBC antigens',
                                                    'B) Only plasma antibodies forever only',
                                                    'C) Only Hb',
                                                    'D) Only WBC'],
                                        'answer': 'A) RBC antigens',
                                        'explanation': 'Reverse typing detects antibodies.'},
                                       {'question': 'Crossmatch checks?',
                                        'options': ['A) Compatibility between donor RBC and '
                                                    'recipient plasma',
                                                    'B) Only donor HIV only',
                                                    'C) Only platelet count',
                                                    'D) Only ESR'],
                                        'answer': 'A) Compatibility between donor RBC and '
                                                  'recipient plasma',
                                        'explanation': 'Pretransfusion testing.'},
                                       {'question': 'O negative often used as?',
                                        'options': ['A) Emergency uncrossmatched RBC in selected '
                                                    'protocols',
                                                    'B) Universal plasma always',
                                                    'C) Only platelet product',
                                                    'D) Only cryoprecipitate'],
                                        'answer': 'A) Emergency uncrossmatched RBC in selected '
                                                  'protocols',
                                        'explanation': 'Know local massive transfusion rules.'}],
                              'medium': [{'question': 'RhIg indicated for?',
                                          'options': ['A) RhD-negative mother at risk for anti-D '
                                                      'sensitization themes',
                                                      'B) All mothers always regardless of Rh',
                                                      'C) Only fathers',
                                                      'D) Only platelet donors always'],
                                          'answer': 'A) RhD-negative mother at risk for anti-D '
                                                    'sensitization themes',
                                          'explanation': 'Obstetric blood bank.'},
                                         {'question': 'Acute hemolytic reaction classic cause?',
                                          'options': ['A) ABO incompatibility',
                                                      'B) Only mild allergic always',
                                                      'C) Only citrate only',
                                                      'D) Only TACO only'],
                                          'answer': 'A) ABO incompatibility',
                                          'explanation': 'Stop transfusion; clerical check.'},
                                         {'question': 'DAT detects?',
                                          'options': ['A) In vivo coated RBCs',
                                                      'B) Only free plasma antibody always only',
                                                      'C) Only bacteria',
                                                      'D) Only glucose'],
                                          'answer': 'A) In vivo coated RBCs',
                                          'explanation': 'AIHA/HDFN/transfusion workups.'}],
                              'hard': [{'question': 'A junior colleague asks for the single best '
                                                    'answer. Antibody screen positive next? Beware '
                                                    'of near-miss distractors.',
                                        'options': ['A) Antibody identification panel',
                                                    'B) Ignore and issue anything',
                                                    'C) Only give platelets',
                                                    'D) Cancel blood bank forever'],
                                        'answer': 'A) Antibody identification panel',
                                        'explanation': 'Then antigen-negative units.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. TRALI vs TACO? Beware of near-miss '
                                                    'distractors.',
                                        'options': ['A) TRALI: permeability edema/immune; TACO: '
                                                    'hydrostatic overload',
                                                    'B) Identical always',
                                                    'C) Neither related to transfusion',
                                                    'D) Only allergic rash defines both'],
                                        'answer': 'A) TRALI: permeability edema/immune; TACO: '
                                                  'hydrostatic overload',
                                        'explanation': 'Different management cues.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Massive transfusion issues include? '
                                                    'Beware of near-miss distractors.',
                                        'options': ['A) Coagulopathy, hypothermia, hypocalcemia, '
                                                    'citrate',
                                                    'B) Only better clotting always',
                                                    'C) Only hyperglycemia only forever',
                                                    'D) No lab monitoring needed'],
                                        'answer': 'A) Coagulopathy, hypothermia, hypocalcemia, '
                                                  'citrate',
                                        'explanation': 'Ratio protocols / viscoelastic testing '
                                                       'themes.'}],
                              'extreme': [{'question': 'In a high-stakes laboratory scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Emergency release documentation '
                                                       'must? Avoid actions that could harm if a '
                                                       'critical risk remains open.',
                                           'options': ['A) Capture physician urgency '
                                                       'acknowledgment and follow-up testing',
                                                       'B) Skip all records',
                                                       'C) Change blood type quietly',
                                                       'D) Discard segments'],
                                           'answer': 'A) Capture physician urgency acknowledgment '
                                                     'and follow-up testing',
                                           'explanation': 'Regulatory/safety.'},
                                          {'question': 'In a high-stakes laboratory scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Warm AIHA crossmatch difficulty? '
                                                       'Avoid actions that could harm if a '
                                                       'critical risk remains open.',
                                           'options': ['A) Panagglutination; need special '
                                                       'techniques/least incompatible strategies '
                                                       'with clinical team',
                                                       'B) Always easy identical to normal',
                                                       'C) Never transfuse ever regardless of life '
                                                       'threat without discussion',
                                                       'D) Ignore antibody'],
                                           'answer': 'A) Panagglutination; need special '
                                                     'techniques/least incompatible strategies '
                                                     'with clinical team',
                                           'explanation': 'Coordinate hematology.'},
                                          {'question': 'In a high-stakes laboratory scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Bacterial contamination highest '
                                                       'risk historically with? Avoid actions that '
                                                       'could harm if a critical risk remains '
                                                       'open.',
                                           'options': ['A) Platelets (room temp storage)',
                                                       'B) Frozen plasma always higher than '
                                                       'platelets historically classic teaching '
                                                       'opposite',
                                                       'C) Washed RBCs only',
                                                       'D) Crystalloid'],
                                           'answer': 'A) Platelets (room temp storage)',
                                           'explanation': 'Visual checks + culture strategies.'}]},
                'cases': {'easy': [{'title': 'Pre-op Type and Screen',
                                    'stem': 'Patient needs elective surgery; type and screen '
                                            'ordered.',
                                    'question': 'Purpose?',
                                    'answer': 'Determine ABO/Rh and unexpected antibodies before '
                                              'transfusion need.',
                                    'discussion': 'Saves time if crossmatch needed.',
                                    'book_hint': 'Technical Manual — AABB'}],
                          'medium': [{'title': 'Fever During Transfusion',
                                      'stem': 'Fever/chills mid-RBC transfusion.',
                                      'question': 'Immediate action?',
                                      'answer': 'Stop transfusion, keep IV line, check clerical, '
                                                'notify blood bank, investigate per protocol.',
                                      'discussion': 'Rule out hemolytic/bacterial.',
                                      'book_hint': 'Technical Manual — AABB'}],
                          'hard': [{'title': 'Dyspnea + Hypoxemia Post Transfusion',
                                    'stem': 'Bilateral infiltrates, no hypertension; timing after '
                                            'plasma-rich product. Choose the safest high-yield '
                                            'next laboratory concept.',
                                    'question': 'Consider?',
                                    'answer': 'TRALI among differentials — supportive care; '
                                              'report.',
                                    'discussion': 'Distinguish from TACO.',
                                    'book_hint': 'Technical Manual — AABB'}],
                          'extreme': [{'title': 'Massive Bleed Uncrossmatched',
                                       'stem': 'Trauma exsanguinating; blood bank issues emergency '
                                               'O units then switches to type-specific. Avoid '
                                               'reporting or actions that could harm if a critical '
                                               'quality risk remains open.',
                                       'question': 'Key lab roles?',
                                       'answer': 'Rapid ABO, switch policies, MTP support, '
                                                 'communication, documentation.',
                                       'discussion': 'Prevent ABO errors under pressure.',
                                       'book_hint': 'Technical Manual — AABB'}]}},
 'histopathology': {'label': 'Histopathology',
                    'books': ["Bancroft's Theory and Practice of Histological Techniques",
                              'Histotechnology manuals',
                              'CAP histology checklists'],
                    'pdf_notes': ['Fixation time/type critically affect morphology and IHC.',
                                  'Tissue processing artifacts can mimic pathology.',
                                  'H&E is foundational; special stains answer specific questions.',
                                  'Frozen section has limits — communicate clearly with surgeon.',
                                  'Orientation, margins, and labeling prevent catastrophic '
                                  'mix-ups.'],
                    'questions': {'easy': [{'question': 'Formalin mainly used to?',
                                            'options': ['A) Fix tissues',
                                                        'B) Stain nuclei only',
                                                        'C) Culture bacteria',
                                                        'D) Measure glucose'],
                                            'answer': 'A) Fix tissues',
                                            'explanation': 'Preserve morphology.'},
                                           {'question': 'H&E stain shows?',
                                            'options': ['A) General tissue morphology',
                                                        'B) Only fat exclusively',
                                                        'C) Only organisms always only',
                                                        'D) Only iron only'],
                                            'answer': 'A) General tissue morphology',
                                            'explanation': 'Routine stain.'},
                                           {'question': 'Pap smear is a?',
                                            'options': ['A) Cytology screening test',
                                                        'B) Only blood culture',
                                                        'C) Only CBC',
                                                        'D) Only PT'],
                                            'answer': 'A) Cytology screening test',
                                            'explanation': 'Cervical screening themes.'}],
                                  'medium': [{'question': 'Immunohistochemistry detects?',
                                              'options': ['A) Antigens in tissue with antibodies',
                                                          'B) Only electrolytes in serum',
                                                          'C) Only urine SG',
                                                          'D) Only ESR'],
                                              'answer': 'A) Antigens in tissue with antibodies',
                                              'explanation': 'Diagnosis/classification.'},
                                             {'question': 'Frozen section purpose?',
                                              'options': ['A) Intraoperative rapid diagnosis',
                                                          'B) Permanent best morphology always '
                                                          'superior to paraffin forever for '
                                                          'everything',
                                                          'C) Only research posters',
                                                          'D) Only teaching without clinical use'],
                                              'answer': 'A) Intraoperative rapid diagnosis',
                                              'explanation': 'Limitations vs permanent.'},
                                             {'question': 'Cytopathology adequacy matters because?',
                                              'options': ['A) Insufficient cells → unsatisfactory '
                                                          'interpretation',
                                                          'B) Always diagnostic regardless',
                                                          'C) Volume never matters',
                                                          'D) Labels optional'],
                                              'answer': 'A) Insufficient cells → unsatisfactory '
                                                        'interpretation',
                                              'explanation': 'Bethesda-style reporting themes.'}],
                                  'hard': [{'question': 'A junior colleague asks for the single '
                                                        'best answer. Poor fixation artifact can? '
                                                        'Beware of near-miss distractors.',
                                            'options': ['A) Mimic/ obscure pathology',
                                                        'B) Improve IHC always',
                                                        'C) Never affect diagnosis',
                                                        'D) Only change barcode'],
                                            'answer': 'A) Mimic/ obscure pathology',
                                            'explanation': 'Preanalytics in AP.'},
                                           {'question': 'A junior colleague asks for the single '
                                                        'best answer. Special stain AFB used for? '
                                                        'Beware of near-miss distractors.',
                                            'options': ['A) Mycobacteria in tissue',
                                                        'B) Only glycogen only',
                                                        'C) Only collagen only',
                                                        'D) Only amyloid only'],
                                            'answer': 'A) Mycobacteria in tissue',
                                            'explanation': 'Correlate microbiology.'},
                                           {'question': 'A junior colleague asks for the single '
                                                        'best answer. Molecular tests on FFPE '
                                                        'need? Beware of near-miss distractors.',
                                            'options': ['A) Adequate tumor content/quality nucleic '
                                                        'acid',
                                                        'B) No pathologist input ever',
                                                        'C) Only wet tissue never fixed ever '
                                                        'exclusively',
                                                        'D) Random blocks without review'],
                                            'answer': 'A) Adequate tumor content/quality nucleic '
                                                      'acid',
                                            'explanation': 'Precision oncology pathway.'}],
                                  'extreme': [{'question': 'In a high-stakes laboratory scenario '
                                                           'with incomplete data, which statement '
                                                           'is MOST correct? Critical unexpected '
                                                           'malignancy in frozen? Avoid actions '
                                                           'that could harm if a critical risk '
                                                           'remains open.',
                                               'options': ['A) Immediate clear communication to '
                                                           'surgeon',
                                                           'B) Leave note tomorrow only',
                                                           'C) Change diagnosis silently later '
                                                           'without call',
                                                           'D) Discard slide'],
                                               'answer': 'A) Immediate clear communication to '
                                                         'surgeon',
                                               'explanation': 'Intraoperative impact.'},
                                              {'question': 'In a high-stakes laboratory scenario '
                                                           'with incomplete data, which statement '
                                                           'is MOST correct? Cytotech–pathologist '
                                                           'hierarchy ensures? Avoid actions that '
                                                           'could harm if a critical risk remains '
                                                           'open.',
                                               'options': ['A) Qualified review of abnormal '
                                                           'findings',
                                                           'B) No QA',
                                                           'C) Screening without standards',
                                                           'D) Ignoring ASCUS algorithms'],
                                               'answer': 'A) Qualified review of abnormal findings',
                                               'explanation': 'Quality systems.'},
                                              {'question': 'In a high-stakes laboratory scenario '
                                                           'with incomplete data, which statement '
                                                           'is MOST correct? Decalcification '
                                                           'overdone may? Avoid actions that could '
                                                           'harm if a critical risk remains open.',
                                               'options': ['A) Damage antigenicity/morphology',
                                                           'B) Always improve IHC',
                                                           'C) Never matter',
                                                           'D) Only help cultures'],
                                               'answer': 'A) Damage antigenicity/morphology',
                                               'explanation': 'Balance soft enough to cut vs '
                                                              'over-decal.'}]},
                    'cases': {'easy': [{'title': 'Biopsy in Formalin',
                                        'stem': 'Surgeon sends breast lump in formalin.',
                                        'question': 'Lab first steps?',
                                        'answer': 'Accession, gross, fix adequately, process to '
                                                  'paraffin.',
                                        'discussion': 'Labeling critical.',
                                        'book_hint': 'Robbins Basic Pathology / Bancroft histotech '
                                                     'themes'}],
                              'medium': [{'title': 'Frozen Section Margin',
                                          'stem': 'Surgeon asks if margin is clear during surgery.',
                                          'question': 'Role?',
                                          'answer': 'Rapid microscopic assessment; communicate '
                                                    'limitations.',
                                          'discussion': 'Defer final to permanent sections when '
                                                        'needed.',
                                          'book_hint': 'Robbins Basic Pathology / Bancroft '
                                                       'histotech themes'}],
                              'hard': [{'title': 'Unlabeled Specimen',
                                        'stem': 'Two specimens arrive; one unlabeled. Choose the '
                                                'safest high-yield next laboratory concept.',
                                        'question': 'Action?',
                                        'answer': 'Do not guess — resolve identity per policy '
                                                  'before processing.',
                                        'discussion': 'Patient safety.',
                                        'book_hint': 'Robbins Basic Pathology / Bancroft histotech '
                                                     'themes'}],
                              'extreme': [{'title': 'Mismatch Clinical vs Histology Site',
                                           'stem': 'Label says left lobe; surgeon says right. '
                                                   'Avoid reporting or actions that could harm if '
                                                   'a critical quality risk remains open.',
                                           'question': 'Response?',
                                           'answer': 'Stop, verify with clinical team before '
                                                     'sign-out; amend accessioning if resolved.',
                                           'discussion': 'Never assume.',
                                           'book_hint': 'Robbins Basic Pathology / Bancroft '
                                                        'histotech themes'}]}},
 'parasitology': {'label': 'Parasitology',
                  'books': ['CDC DPDx',
                            'Clinical Parasitology textbooks',
                            'WHO parasitology guides'],
                  'pdf_notes': ['Thick vs thin smears serve different malaria goals.',
                                'O&P timing and preservatives affect recovery.',
                                'Know morphologic keys for common protozoa/helminths.',
                                'Travel/exposure history guides test selection.',
                                'Strongyloides risk before immunosuppression — screen when '
                                'indicated.'],
                  'questions': {'easy': [{'question': 'Stool O&P looks for?',
                                          'options': ['A) Ova and parasites',
                                                      'B) Only bacteria always only',
                                                      'C) Only viruses',
                                                      'D) Only occult blood only'],
                                          'answer': 'A) Ova and parasites',
                                          'explanation': 'Concentration/permanent stains.'},
                                         {'question': 'Malaria diagnosed commonly by?',
                                          'options': ['A) Blood films (thick/thin)',
                                                      'B) Only urine dipstick',
                                                      'C) Only chest x-ray',
                                                      'D) Only ECG'],
                                          'answer': 'A) Blood films (thick/thin)',
                                          'explanation': 'Species identification matters.'},
                                         {'question': 'Enterobius best sampled by?',
                                          'options': ['A) Perianal tape test',
                                                      'B) Only blood culture',
                                                      'C) Only throat swab',
                                                      'D) Only CSF'],
                                          'answer': 'A) Perianal tape test',
                                          'explanation': 'Pinworm.'}],
                                'medium': [{'question': 'Giardia trophozoites seen in?',
                                            'options': ['A) Stool (or duodenal) specimens',
                                                        'B) Only blood',
                                                        'C) Only sputum always',
                                                        'D) Only CSF always'],
                                            'answer': 'A) Stool (or duodenal) specimens',
                                            'explanation': 'Antigen/NAAT also used.'},
                                           {'question': 'E. histolytica concern?',
                                            'options': ['A) Invasive amebiasis; distinguish from '
                                                        'nonpathogenic amebae',
                                                        'B) Always harmless commensals identical',
                                                        'C) Only skin flora',
                                                        'D) Only contaminants never pathogenic'],
                                            'answer': 'A) Invasive amebiasis; distinguish from '
                                                      'nonpathogenic amebae',
                                            'explanation': 'Careful ID.'},
                                           {'question': 'Ziehl-Neelsen modified may help detect?',
                                            'options': ['A) Cryptosporidium oocysts among uses',
                                                        'B) Only staphylococci',
                                                        'C) Only yeast always better gram',
                                                        'D) Only mycobacteria exclusively never '
                                                        'crypto'],
                                            'answer': 'A) Cryptosporidium oocysts among uses',
                                            'explanation': 'Acid-fast parasites.'}],
                                'hard': [{'question': 'A junior colleague asks for the single best '
                                                      'answer. Babesia vs malaria on film? Beware '
                                                      'of near-miss distractors.',
                                          'options': ['A) Babesia may show Maltese cross; no '
                                                      'travel sometimes; different Rx',
                                                      'B) Identical always',
                                                      'C) Babesia only in stool',
                                                      'D) Malaria only in urine'],
                                          'answer': 'A) Babesia may show Maltese cross; no travel '
                                                    'sometimes; different Rx',
                                          'explanation': 'Tick exposure.'},
                                         {'question': 'A junior colleague asks for the single best '
                                                      'answer. Hydatid disease caution in lab? '
                                                      'Beware of near-miss distractors.',
                                          'options': ['A) Avoid spilling cystic fluid; anaphylaxis '
                                                      'risk themes',
                                                      'B) Open on bench casually',
                                                      'C) No PPE',
                                                      'D) Culture anaerobically only concern'],
                                          'answer': 'A) Avoid spilling cystic fluid; anaphylaxis '
                                                    'risk themes',
                                          'explanation': 'Surgical pathology coordination.'},
                                         {'question': 'A junior colleague asks for the single best '
                                                      'answer. Concentration methods increase? '
                                                      'Beware of near-miss distractors.',
                                          'options': ['A) Sensitivity for ova/cysts',
                                                      'B) Specificity to 100% always',
                                                      'C) Only turnaround slower without benefit',
                                                      'D) No use'],
                                          'answer': 'A) Sensitivity for ova/cysts',
                                          'explanation': 'Formalin-ethyl acetate etc.'}],
                                'extreme': [{'question': 'In a high-stakes laboratory scenario '
                                                         'with incomplete data, which statement is '
                                                         'MOST correct? Leishmania amastigotes '
                                                         'found in? Avoid actions that could harm '
                                                         'if a critical risk remains open.',
                                             'options': ['A) Macrophages in tissue/bone marrow '
                                                         'themes',
                                                         'B) Only peripheral thin film always easy '
                                                         'like malaria exclusively',
                                                         'C) Only urine crystals',
                                                         'D) Only gram stain of throat'],
                                             'answer': 'A) Macrophages in tissue/bone marrow '
                                                       'themes',
                                             'explanation': 'Specialist centers.'},
                                            {'question': 'In a high-stakes laboratory scenario '
                                                         'with incomplete data, which statement is '
                                                         'MOST correct? Automated malaria '
                                                         'analyzers still need? Avoid actions that '
                                                         'could harm if a critical risk remains '
                                                         'open.',
                                             'options': ['A) Expert smear review for '
                                                         'speciation/confirmation pathways',
                                                         'B) No human review ever',
                                                         'C) Only app selfie',
                                                         'D) Discard films'],
                                             'answer': 'A) Expert smear review for '
                                                       'speciation/confirmation pathways',
                                             'explanation': 'Critical speciation.'},
                                            {'question': 'In a high-stakes laboratory scenario '
                                                         'with incomplete data, which statement is '
                                                         'MOST correct? Formalin stool vials '
                                                         'hazard? Avoid actions that could harm if '
                                                         'a critical risk remains open.',
                                             'options': ['A) Chemical exposure; handle per SDS',
                                                         'B) Drinkable preservative',
                                                         'C) No labeling needed',
                                                         'D) Store with food'],
                                             'answer': 'A) Chemical exposure; handle per SDS',
                                             'explanation': 'Lab safety.'}]},
                  'cases': {'easy': [{'title': 'Travel Fever',
                                      'stem': 'Fever after travel to endemic area; order malaria '
                                              'smears.',
                                      'question': 'Lab urgency?',
                                      'answer': 'Stat thick/thin films; notify positives.',
                                      'discussion': 'Repeat smears if high suspicion.',
                                      'book_hint': 'Diagnostic Medical Parasitology — Garcia'}],
                            'medium': [{'title': 'Chronic Diarrhea HIV',
                                        'stem': 'Acid-fast oocysts in stool.',
                                        'question': 'Likely?',
                                        'answer': 'Cryptosporidium — report; supportive/ID care.',
                                        'discussion': 'Infection control in waterborne outbreaks.',
                                        'book_hint': 'Diagnostic Medical Parasitology — Garcia'}],
                            'hard': [{'title': 'Blood Film Ring Forms No Travel',
                                      'stem': 'Northeast US, fever, hemolysis; rings on smear. '
                                              'Choose the safest high-yield next laboratory '
                                              'concept.',
                                      'question': 'Consider?',
                                      'answer': 'Babesia — confirm; notify clinician.',
                                      'discussion': 'Co-infection/tick history.',
                                      'book_hint': 'Diagnostic Medical Parasitology — Garcia'}],
                            'extreme': [{'title': 'Possible Echinococcus Cyst Fluid',
                                         'stem': 'Aspiration fluid sent unexpectedly. Avoid '
                                                 'reporting or actions that could harm if a '
                                                 'critical quality risk remains open.',
                                         'question': 'Lab action?',
                                         'answer': 'Handle as hazardous; communicate; specialized '
                                                   'testing pathways; protect staff.',
                                         'discussion': 'Do not centrifuge casually without '
                                                       'precautions.',
                                         'book_hint': 'Diagnostic Medical Parasitology — '
                                                      'Garcia'}]}},
 'molecular_diagnostics': {'label': 'Molecular Diagnostics',
                           'books': ['Molecular Diagnostics textbooks',
                                     'CAP molecular pathology checklists',
                                     'Assay IFUs'],
                           'pdf_notes': ['Contamination control (unidirectional workflow) is '
                                         'non-negotiable.',
                                         'Internal controls detect inhibition and process failure.',
                                         'CT near cutoff needs defined repeat/confirm policy.',
                                         'NAAT often preferred over culture for some STIs.',
                                         'Result interpretation must include analytic '
                                         'limitations.'],
                           'questions': {'easy': [{'question': 'PCR amplifies?',
                                                   'options': ['A) Target nucleic acid',
                                                               'B) Only proteins always',
                                                               'C) Only lipids',
                                                               'D) Only glucose'],
                                                   'answer': 'A) Target nucleic acid',
                                                   'explanation': 'Core molecular method.'},
                                                  {'question': 'Contamination control in PCR '
                                                               'includes?',
                                                   'options': ['A) Separate areas/ unidirectional '
                                                               'workflow / controls',
                                                               'B) Open amplicons everywhere',
                                                               'C) No negative controls',
                                                               'D) Reuse tips with amplicon '
                                                               'freely'],
                                                   'answer': 'A) Separate areas/ unidirectional '
                                                             'workflow / controls',
                                                   'explanation': 'False positives risk.'},
                                                  {'question': 'Viral load assays monitor?',
                                                   'options': ['A) Quantity of virus nucleic acid',
                                                               'B) Only bacterial colonies on '
                                                               'plate only',
                                                               'C) Only HbA1c',
                                                               'D) Only urine color'],
                                                   'answer': 'A) Quantity of virus nucleic acid',
                                                   'explanation': 'HIV/HCV etc.'}],
                                         'medium': [{'question': 'Ct value roughly relates to?',
                                                     'options': ['A) Inverse of target amount '
                                                                 '(method-dependent)',
                                                                 'B) Always exact organism count '
                                                                 'identical across platforms',
                                                                 'C) Only cycle of moon',
                                                                 'D) Only reagent lot letter'],
                                                     'answer': 'A) Inverse of target amount '
                                                               '(method-dependent)',
                                                     'explanation': 'Interpret cautiously.'},
                                                    {'question': 'Internal control failure '
                                                                 'suggests?',
                                                     'options': ['A) Inhibition/extraction problem',
                                                                 'B) Perfect run',
                                                                 'C) Always true negative',
                                                                 'D) Ignore'],
                                                     'answer': 'A) Inhibition/extraction problem',
                                                     'explanation': 'Repeat/recollect.'},
                                                    {'question': 'Genotyping may guide?',
                                                     'options': ['A) Therapy (e.g., '
                                                                 'resistance/pharmacogenetics)',
                                                                 'B) Only room assignment',
                                                                 'C) Only meal choice',
                                                                 'D) Only parking'],
                                                     'answer': 'A) Therapy (e.g., '
                                                               'resistance/pharmacogenetics)',
                                                     'explanation': 'Precision medicine.'}],
                                         'hard': [{'question': 'A junior colleague asks for the '
                                                               'single best answer. NGS panels '
                                                               'need? Beware of near-miss '
                                                               'distractors.',
                                                   'options': ['A) Bioinformatic pipelines + '
                                                               'quality metrics + interpretation',
                                                               'B) Only naked eye bands forever',
                                                               'C) No controls',
                                                               'D) Random variant calling without '
                                                               'QA'],
                                                   'answer': 'A) Bioinformatic pipelines + quality '
                                                             'metrics + interpretation',
                                                   'explanation': 'Complex validation.'},
                                                  {'question': 'A junior colleague asks for the '
                                                               'single best answer. Minimal '
                                                               'residual disease PCR detects? '
                                                               'Beware of near-miss distractors.',
                                                   'options': ['A) Very low level residual target',
                                                               'B) Only gross disease visible on '
                                                               'smear always same sensitivity',
                                                               'C) Only chemistry panels',
                                                               'D) Only cultures'],
                                                   'answer': 'A) Very low level residual target',
                                                   'explanation': 'Hematologic malignancy '
                                                                  'monitoring.'},
                                                  {'question': 'A junior colleague asks for the '
                                                               'single best answer. Sample swap '
                                                               'detection uses? Beware of '
                                                               'near-miss distractors.',
                                                   'options': ['A) Identity checks / barcodes / '
                                                               'sometimes genetic ID strategies',
                                                               'B) Guessing',
                                                               'C) Ignoring names',
                                                               'D) Mixing tubes to save time'],
                                                   'answer': 'A) Identity checks / barcodes / '
                                                             'sometimes genetic ID strategies',
                                                   'explanation': 'Fatal error prevention.'}],
                                         'extreme': [{'question': 'In a high-stakes laboratory '
                                                                  'scenario with incomplete data, '
                                                                  'which statement is MOST '
                                                                  'correct? Laboratory-developed '
                                                                  'tests require? Avoid actions '
                                                                  'that could harm if a critical '
                                                                  'risk remains open.',
                                                      'options': ['A) Validation/verification per '
                                                                  'regulations before clinical use',
                                                                  'B) No documentation',
                                                                  'C) Launch without performance '
                                                                  'characteristics',
                                                                  'D) Only vendor brochure'],
                                                      'answer': 'A) Validation/verification per '
                                                                'regulations before clinical use',
                                                      'explanation': 'CLIA/CAP themes.'},
                                                     {'question': 'In a high-stakes laboratory '
                                                                  'scenario with incomplete data, '
                                                                  'which statement is MOST '
                                                                  'correct? Amplicon contamination '
                                                                  'outbreak presents as? Avoid '
                                                                  'actions that could harm if a '
                                                                  'critical risk remains open.',
                                                      'options': ['A) Unexpected positives '
                                                                  'clustering',
                                                                  'B) Perfect specificity always',
                                                                  'C) Only reagent shortages',
                                                                  'D) Only slower TAT'],
                                                      'answer': 'A) Unexpected positives '
                                                                'clustering',
                                                      'explanation': 'Stop, clean, root-cause.'},
                                                     {'question': 'In a high-stakes laboratory '
                                                                  'scenario with incomplete data, '
                                                                  'which statement is MOST '
                                                                  'correct? Cell-free DNA assays '
                                                                  'challenges include? Avoid '
                                                                  'actions that could harm if a '
                                                                  'critical risk remains open.',
                                                      'options': ['A) Low analyte, fragmentation, '
                                                                  'preanalytics',
                                                                  'B) Always trivial easy like '
                                                                  'glucose',
                                                                  'C) No need for controls',
                                                                  'D) Room temperature months '
                                                                  'always fine'],
                                                      'answer': 'A) Low analyte, fragmentation, '
                                                                'preanalytics',
                                                      'explanation': 'Special handling.'}]},
                           'cases': {'easy': [{'title': 'COVID/Flu NAAT Order',
                                               'stem': 'Respiratory NAAT requested.',
                                               'question': 'Preanalytic key?',
                                               'answer': 'Correct swab/transport, labeling, avoid '
                                                         'contamination.',
                                               'discussion': 'Invalid if poor collection.',
                                               'book_hint': 'Molecular Diagnostics texts / CAP '
                                                            'molecular themes'}],
                                     'medium': [{'title': 'Inhibited PCR',
                                                 'stem': 'Patient negative but IC fails.',
                                                 'question': 'Report?',
                                                 'answer': 'Invalid/inhibited — do not call true '
                                                           'negative; repeat.',
                                                 'discussion': 'Communicate.',
                                                 'book_hint': 'Molecular Diagnostics texts / CAP '
                                                              'molecular themes'}],
                                     'hard': [{'title': 'Unexpected Mutation Report',
                                               'stem': 'Pathogenic variant reported but clinical '
                                                       'mismatch. Choose the safest high-yield '
                                                       'next laboratory concept.',
                                               'question': 'Steps?',
                                               'answer': 'Confirm identity, review IGV/reads, '
                                                         'orthogonal method, amend if needed.',
                                               'discussion': 'Patient impact huge.',
                                               'book_hint': 'Molecular Diagnostics texts / CAP '
                                                            'molecular themes'}],
                                     'extreme': [{'title': 'Wave of Weak Positives',
                                                  'stem': 'Sudden rise in low-positive NAAT '
                                                          'results after renovation near PCR room. '
                                                          'Avoid reporting or actions that could '
                                                          'harm if a critical quality risk remains '
                                                          'open.',
                                                  'question': 'Suspect?',
                                                  'answer': 'Contamination — halt reporting, '
                                                            'investigate environment/workflow, '
                                                            'notify clinicians about possible '
                                                            'false positives.',
                                                  'discussion': 'Quality crisis management.',
                                                  'book_hint': 'Molecular Diagnostics texts / CAP '
                                                               'molecular themes'}]}},
 'lab_qa': {'label': 'Lab QA & Safety',
            'books': ['ISO 15189 overview materials',
                      'CLSI quality documents',
                      'Biosafety in Microbiological and Biomedical Laboratories'],
            'pdf_notes': ['Do not release patient results when QC is out of control.',
                          'Westgard rules help detect random vs systematic error.',
                          'Needle-stick: wash, report, evaluate source, follow PEP policy.',
                          'Document corrective actions and verify before resuming testing.',
                          'Quality is a system: people, methods, reagents, equipment, IT.'],
            'questions': {'easy': [{'question': 'QA means?',
                                    'options': ['A) Quality assurance — systems to ensure reliable '
                                                'results',
                                                'B) Quick assay only',
                                                'C) Quiet area only',
                                                'D) Quarterly absence'],
                                    'answer': 'A) Quality assurance — systems to ensure reliable '
                                              'results',
                                    'explanation': 'Beyond single QC points.'},
                                   {'question': 'QC monitors?',
                                    'options': ['A) Method performance over time',
                                                'B) Only staff birthdays',
                                                'C) Only paint color',
                                                'D) Only lunch breaks'],
                                    'answer': 'A) Method performance over time',
                                    'explanation': 'Levey-Jennings themes.'},
                                   {'question': 'SOP stands for?',
                                    'options': ['A) Standard operating procedure',
                                                'B) Special optional print',
                                                'C) Serum only processing',
                                                'D) Shift overtime pay'],
                                    'answer': 'A) Standard operating procedure',
                                    'explanation': 'Follow written methods.'}],
                          'medium': [{'question': 'Westgard rules help detect?',
                                      'options': ['A) Random/systematic error patterns',
                                                  'B) Only staffing needs',
                                                  'C) Only inventory of gloves',
                                                  'D) Only temperature of break room'],
                                      'answer': 'A) Random/systematic error patterns',
                                      'explanation': 'Multirule QC.'},
                                     {'question': 'Proficiency testing evaluates?',
                                      'options': ['A) Laboratory accuracy vs external unknowns',
                                                  'B) Only typing speed',
                                                  'C) Only parking skills',
                                                  'D) Only phone etiquette'],
                                      'answer': 'A) Laboratory accuracy vs external unknowns',
                                      'explanation': 'Accreditation requirement.'},
                                     {'question': 'Critical results require?',
                                      'options': ['A) Timely notification and '
                                                  'read-back/documentation',
                                                  'B) Batching next month',
                                                  'C) No records',
                                                  'D) Texting only the patient'],
                                      'answer': 'A) Timely notification and '
                                                'read-back/documentation',
                                      'explanation': 'Patient safety.'}],
                          'hard': [{'question': 'A junior colleague asks for the single best '
                                                'answer. Root cause analysis after error aims to? '
                                                'Beware of near-miss distractors.',
                                    'options': ['A) Fix system causes not only blame individuals',
                                                'B) Punish only and stop',
                                                'C) Hide the event',
                                                'D) Change result without review'],
                                    'answer': 'A) Fix system causes not only blame individuals',
                                    'explanation': 'Just culture balance.'},
                                   {'question': 'A junior colleague asks for the single best '
                                                'answer. Document control ensures? Beware of '
                                                'near-miss distractors.',
                                    'options': ['A) Only current approved SOPs in use',
                                                'B) Mixed obsolete versions everywhere',
                                                'C) No version numbers',
                                                'D) Sticky notes replace SOPs'],
                                    'answer': 'A) Only current approved SOPs in use',
                                    'explanation': 'ISO/CAP themes.'},
                                   {'question': 'A junior colleague asks for the single best '
                                                'answer. Risk management in labs includes? Beware '
                                                'of near-miss distractors.',
                                    'options': ['A) Identifying failure modes and mitigations',
                                                'B) Ignoring near misses',
                                                'C) No incident reports',
                                                'D) Skipping training'],
                                    'answer': 'A) Identifying failure modes and mitigations',
                                    'explanation': 'Proactive safety.'}],
                          'extreme': [{'question': 'In a high-stakes laboratory scenario with '
                                                   'incomplete data, which statement is MOST '
                                                   'correct? Accreditation nonconformance demands? '
                                                   'Avoid actions that could harm if a critical '
                                                   'risk remains open.',
                                       'options': ['A) Corrective/preventive action with evidence',
                                                   'B) Ignore surveyor',
                                                   'C) Verbal promise only forever',
                                                   'D) Delete records'],
                                       'answer': 'A) Corrective/preventive action with evidence',
                                       'explanation': 'Close the loop.'},
                                      {'question': 'In a high-stakes laboratory scenario with '
                                                   'incomplete data, which statement is MOST '
                                                   'correct? LIS downtime procedure must? Avoid '
                                                   'actions that could harm if a critical risk '
                                                   'remains open.',
                                       'options': ['A) Maintain safe manual '
                                                   'reporting/identification',
                                                   'B) Stop all care without backup',
                                                   'C) Invent results',
                                                   'D) Skip identifiers'],
                                       'answer': 'A) Maintain safe manual reporting/identification',
                                       'explanation': 'Business continuity.'},
                                      {'question': 'In a high-stakes laboratory scenario with '
                                                   'incomplete data, which statement is MOST '
                                                   'correct? Ethical reflex: altered QC to pass? '
                                                   'Avoid actions that could harm if a critical '
                                                   'risk remains open.',
                                       'options': ['A) Fraud — never; report integrity concerns',
                                                   'B) Acceptable shortcut',
                                                   'C) Expected nightly',
                                                   'D) Manager bonus method'],
                                       'answer': 'A) Fraud — never; report integrity concerns',
                                       'explanation': 'Professional ethics.'}]},
            'cases': {'easy': [{'title': 'QC Out of Range',
                                'stem': 'Daily QC fails.',
                                'question': 'Action?',
                                'answer': 'Do not report patient results until resolved per SOP.',
                                'discussion': 'Troubleshoot then document.',
                                'book_hint': 'Clinical Laboratory Management / CAP accreditation '
                                             'themes'}],
                      'medium': [{'title': 'PT Unsatisfactory',
                                  'stem': 'Proficiency testing fails for glucose.',
                                  'question': 'Next?',
                                  'answer': 'Investigate, corrective action, possible patient '
                                            'impact assessment.',
                                  'discussion': 'Document thoroughly.',
                                  'book_hint': 'Clinical Laboratory Management / CAP accreditation '
                                               'themes'}],
                      'hard': [{'title': 'Wrong Blood in Tube Event',
                                'stem': 'WBIT discovered after delta check. Choose the safest '
                                        'high-yield next laboratory concept.',
                                'question': 'Response?',
                                'answer': 'Recall results, recollect, RCA, notify clinicians, '
                                          'systemic barcode/ID fixes.',
                                'discussion': 'High-harm event.',
                                'book_hint': 'Clinical Laboratory Management / CAP accreditation '
                                             'themes'}],
                      'extreme': [{'title': 'Systemic QC Falsification Allegation',
                                   'stem': 'Staff report that failing QC was rewritten as passing. '
                                           'Avoid reporting or actions that could harm if a '
                                           'critical quality risk remains open.',
                                   'question': 'Leadership action?',
                                   'answer': 'Immediate investigation, protect patients (result '
                                             'review), protect reporters, regulatory notification '
                                             'as required.',
                                   'discussion': 'Integrity crisis.',
                                   'book_hint': 'Clinical Laboratory Management / CAP '
                                                'accreditation themes'}]}},
 'urinalysis': {'label': 'Urinalysis & Body Fluids',
                'books': ['Urinalysis and Body Fluids — Strasinger',
                          'Clinical microscopy manuals',
                          'CLSI body fluid documents'],
                'pdf_notes': ['Correlate dipstick with microscopy.',
                              'RBC casts suggest glomerular disease themes.',
                              'CSF: cell count, differential, culture, and timing matter.',
                              'Crystal ID: polarization distinguishes MSU vs CPPD themes.',
                              'Proper collection (midstream, timed) reduces false positives.'],
                'questions': {'easy': [{'question': 'Urine dipstick blood may detect?',
                                        'options': ['A) Hematuria/hemoglobinuria/myoglobinuria '
                                                    'themes',
                                                    'B) Only glucose always',
                                                    'C) Only ketones only',
                                                    'D) Only bacteria species always'],
                                        'answer': 'A) Hematuria/hemoglobinuria/myoglobinuria '
                                                  'themes',
                                        'explanation': 'Microscopy differentiates intact RBCs.'},
                                       {'question': 'Specific gravity estimates?',
                                        'options': ['A) Urine concentration',
                                                    'B) Only color preference',
                                                    'C) Only odor',
                                                    'D) Only volume alone without concentration'],
                                        'answer': 'A) Urine concentration',
                                        'explanation': 'Hydration/renal concentrating.'},
                                       {'question': 'CSF tube order typically?',
                                        'options': ['A) Chemistry/micro/heme allocations per '
                                                    'protocol',
                                                    'B) Random any order always fine',
                                                    'C) Only one tube ever allowed worldwide',
                                                    'D) No labeling'],
                                        'answer': 'A) Chemistry/micro/heme allocations per '
                                                  'protocol',
                                        'explanation': 'Follow local SOP.'}],
                              'medium': [{'question': 'RBC casts suggest?',
                                          'options': ['A) Glomerular disease',
                                                      'B) Always contamination only',
                                                      'C) Only lower UTI exclusively',
                                                      'D) Only crystals only'],
                                          'answer': 'A) Glomerular disease',
                                          'explanation': 'Microscopy skill.'},
                                         {'question': 'Oval fat bodies associate with?',
                                          'options': ['A) Nephrotic syndrome themes',
                                                      'B) Only diabetes insipidus only',
                                                      'C) Only dehydration only',
                                                      'D) Only contamination ink'],
                                          'answer': 'A) Nephrotic syndrome themes',
                                          'explanation': 'Maltese cross under polarized light.'},
                                         {'question': 'Synovial fluid crystals: needle strongly '
                                                      'birefringent negative?',
                                          'options': ['A) Monosodium urate (gout) themes',
                                                      'B) Always CPPD exclusively',
                                                      'C) Always cholesterol only',
                                                      'D) Always starch'],
                                          'answer': 'A) Monosodium urate (gout) themes',
                                          'explanation': 'Compensated polarized microscopy.'}],
                              'hard': [{'question': 'A junior colleague asks for the single best '
                                                    'answer. Xanthochromia in CSF suggests? Beware '
                                                    'of near-miss distractors.',
                                        'options': ['A) Subarachnoid hemorrhage (after excluding '
                                                    'artifact)',
                                                    'B) Always traumatic tap only forever',
                                                    'C) Always bacterial meningitis only',
                                                    'D) Always normal'],
                                        'answer': 'A) Subarachnoid hemorrhage (after excluding '
                                                  'artifact)',
                                        'explanation': 'Timing/spectrophotometry themes.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Myoglobin vs hemoglobin on dipstick? '
                                                    'Beware of near-miss distractors.',
                                        'options': ['A) Both may read blood positive; '
                                                    'clinical/plasma clues differ',
                                                    'B) Dipstick distinguishes perfectly always',
                                                    'C) Neither ever positive',
                                                    'D) Only WBC detected'],
                                        'answer': 'A) Both may read blood positive; '
                                                  'clinical/plasma clues differ',
                                        'explanation': 'Clear plasma favors myoglobin themes.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Transudate vs exudate uses? Beware of '
                                                    'near-miss distractors.',
                                        'options': ["A) Light's criteria themes for pleural fluid",
                                                    'B) Only color forever',
                                                    'C) Only patient age',
                                                    'D) Only tube number'],
                                        'answer': "A) Light's criteria themes for pleural fluid",
                                        'explanation': 'Chemistry on fluid vs serum.'}],
                              'extreme': [{'question': 'In a high-stakes laboratory scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Body fluid cell counts on '
                                                       'automated analyzers need? Avoid actions '
                                                       'that could harm if a critical risk remains '
                                                       'open.',
                                           'options': ['A) Validation and smear review for '
                                                       'atypical cells',
                                                       'B) Blind trust without flags',
                                                       'C) No clot checks',
                                                       'D) Sharing syringes'],
                                           'answer': 'A) Validation and smear review for atypical '
                                                     'cells',
                                           'explanation': 'Malignancy detection.'},
                                          {'question': 'In a high-stakes laboratory scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Critical CSF findings require? '
                                                       'Avoid actions that could harm if a '
                                                       'critical risk remains open.',
                                           'options': ['A) Immediate clinician notification',
                                                       'B) Batch next week',
                                                       'C) Only mailed letter',
                                                       'D) No documentation'],
                                           'answer': 'A) Immediate clinician notification',
                                           'explanation': 'Meningitis/SAH.'},
                                          {'question': 'In a high-stakes laboratory scenario with '
                                                       'incomplete data, which statement is MOST '
                                                       'correct? Contaminated clean-catch clues? '
                                                       'Avoid actions that could harm if a '
                                                       'critical risk remains open.',
                                           'options': ['A) Squamous epithelial cells many + mixed '
                                                       'flora',
                                                       'B) Pure single uropathogen always '
                                                       'contamination',
                                                       'C) No epithelials ever means always '
                                                       'contamination',
                                                       'D) Labels optional'],
                                           'answer': 'A) Squamous epithelial cells many + mixed '
                                                     'flora',
                                           'explanation': 'Recollect counseling.'}]},
                'cases': {'easy': [{'title': 'Dipstick Nitrite Positive',
                                    'stem': 'Dysuria; nitrite+/LE+.',
                                    'question': 'Suggests?',
                                    'answer': 'Possible UTI — correlate culture.',
                                    'discussion': 'Not all organisms reduce nitrate.',
                                    'book_hint': 'Urinalysis and Body Fluids — Strasinger'}],
                          'medium': [{'title': 'Tea-Colored Urine + RBC Casts',
                                      'stem': 'Hypertension, edema.',
                                      'question': 'Point to?',
                                      'answer': 'Glomerulonephritis workup — report casts clearly.',
                                      'discussion': 'Urgent clinical correlation.',
                                      'book_hint': 'Urinalysis and Body Fluids — Strasinger'}],
                          'hard': [{'title': 'Traumatic Tap vs SAH',
                                    'stem': 'CSF bloody; question xanthochromia. Choose the safest '
                                            'high-yield next laboratory concept.',
                                    'question': 'Approach?',
                                    'answer': 'Compare tubes, centrifuge supernatant, timing since '
                                              'onset; communicate uncertainty.',
                                    'discussion': 'Do not overcall.',
                                    'book_hint': 'Urinalysis and Body Fluids — Strasinger'}],
                          'extreme': [{'title': 'Unexpected Malignant Cells in Fluid',
                                       'stem': 'Cytotech sees atypical cells in pleural fluid '
                                               'count specimen. Avoid reporting or actions that '
                                               'could harm if a critical quality risk remains '
                                               'open.',
                                       'question': 'Action?',
                                       'answer': 'Flag for pathologist/cytology review urgently; '
                                                 'notify clinical team per policy.',
                                       'discussion': "Do not release as 'normal count' only.",
                                       'book_hint': 'Urinalysis and Body Fluids — Strasinger'}]}}}


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
    return (
        f"📘 *Short MCQ — {specialty_label_text}*\n"
        f"Difficulty: *{diff}*\n\n"
        f"{item['question']}\n\n"
        f"_Tap an answer button below._"
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
        "🔬 *CharaNas MLS Bot*\n"
        "Undergraduate Medical Laboratory Science\n\n"
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
