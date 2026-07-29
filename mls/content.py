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
                                        'explanation': 'Adult male hemoglobin reference intervals are typically about 13–17 g/dL, though exact cutoffs vary by laboratory, altitude, and method. Hemoglobin concentration reflects circulating oxygen-carrying capacity and is interpreted with hematocrit and red-cell indices. Sex- and age-specific intervals from the reporting laboratory define the interpretive reference.'},
                                       {'question': 'CBC primarily measures?',
                                        'options': ['A) Blood cell counts and indices',
                                                    'B) Only electrolytes',
                                                    'C) Only liver enzymes',
                                                    'D) Only blood gases'],
                                        'answer': 'A) Blood cell counts and indices',
                                        'explanation': 'A complete blood count (CBC) quantifies leukocytes, erythrocytes, and platelets and reports red-cell indices such as MCV, MCH, and MCHC. Automated analyzers also provide leukocyte differentials and flags that prompt smear review. The CBC is the foundational screening test in hematology for anemia, infection, and cytopenias.'},
                                       {'question': 'Anemia means?',
                                        'options': ['A) Low hemoglobin/RBC mass for age/sex',
                                                    'B) Always high WBC',
                                                    'C) Always high platelets',
                                                    'D) Always normal oxygen forever'],
                                        'answer': 'A) Low hemoglobin/RBC mass for age/sex',
                                        'explanation': 'Anemia is a reduction in hemoglobin concentration or red-cell mass below the reference interval for age and sex. It may result from decreased production, increased destruction, or blood loss. Morphologic (MCV-based) and kinetic approaches guide the subsequent laboratory workup.'}],
                              'medium': [{'question': 'Schistocytes suggest?',
                                          'options': ['A) Microangiopathic hemolysis',
                                                      'B) Only iron deficiency always',
                                                      'C) Only B12 deficiency only',
                                                      'D) Only artifact never pathology'],
                                          'answer': 'A) Microangiopathic hemolysis',
                                          'explanation': 'Schistocytes are fragmented red cells formed when erythrocytes are sheared by fibrin strands or abnormal vasculature. Their presence supports microangiopathic hemolytic anemia (MAHA), as seen in TTP, HUS, DIC, and mechanical valve injury. Correlation with LDH, haptoglobin, bilirubin, and platelet count refines the differential.'},
                                         {'question': 'Left shift means?',
                                          'options': ['A) Increased immature neutrophils',
                                                      'B) Only low lymphocytes always',
                                                      'C) Only eosinophilia only',
                                                      'D) Only basophilia only'],
                                          'answer': 'A) Increased immature neutrophils',
                                          'explanation': 'A left shift denotes increased circulating immature neutrophils such as bands and earlier myeloid forms. It commonly accompanies acute bacterial infection, inflammation, or physiologic stress with accelerated marrow release. Marked left shift with dysplasia or blasts requires morphologic review to exclude myeloid malignancy.'},
                                         {'question': 'INR monitors?',
                                          'options': ['A) Warfarin / extrinsic pathway themes',
                                                      'B) Only heparin anti-Xa always exclusively',
                                                      'C) Only bleeding time only',
                                                      'D) Only D-dimer only'],
                                          'answer': 'A) Warfarin / extrinsic pathway themes',
                                          'explanation': 'The international normalized ratio (INR) standardizes the prothrombin time (PT) across thromboplastin reagents. PT/INR primarily assesses the extrinsic and common coagulation pathways and is used to monitor vitamin K antagonist (warfarin) therapy. Results are interpreted with the therapeutic target appropriate to the clinical indication.'}],
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
                                        'explanation': 'Paroxysmal nocturnal hemoglobinuria (PNH) arises from acquired PIGA mutations that impair GPI-anchor synthesis, depleting complement-regulatory proteins CD55 and CD59 on blood cells. Unopposed complement activity produces intravascular hemolysis and contributes to thrombosis risk. High-sensitivity flow cytometry for GPI-deficient clones is the diagnostic method of choice.'},
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
                                        'explanation': 'Acute myeloid leukemia (AML) and acute lymphoblastic leukemia (ALL) cannot be reliably separated by age or blood counts alone. Distinction relies on blast morphology, cytochemistry when used, multiparameter immunophenotyping, and genetic/cytogenetic findings under WHO/ICC frameworks. Accurate lineage assignment directs induction therapy and risk stratification.'},
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
                                        'explanation': 'Heparin-induced thrombocytopenia (HIT) is an immune-mediated disorder in which antibodies against platelet factor 4–heparin complexes activate platelets. Paradoxically, patients develop thrombocytopenia with a high risk of arterial and venous thrombosis. Laboratory evaluation may include immunoassay and functional assays, and heparin must be discontinued with alternative anticoagulation.'}],
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
                                           'explanation': 'Acute promyelocytic leukemia (APML/APL) is driven by PML::RARA and characteristically presents with coagulopathy and DIC-related bleeding. Early recognition of abnormal promyelocytes, often with Auer rods, warrants urgent initiation of all-trans retinoic acid (ATRA)–based therapy. Delayed treatment markedly increases early hemorrhagic mortality.'},
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
                                           'explanation': 'Thrombotic thrombocytopenic purpura (TTP) classically features microangiopathic hemolytic anemia and thrombocytopenia, often with neurologic findings; fever and renal involvement may occur. Severe ADAMTS13 deficiency allows uncleaved ultra-large von Willebrand multimers to drive platelet microthrombi. Prompt plasma exchange is disease-modifying therapy.'},
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
                                           'explanation': 'Minimal residual disease (MRD) assessment by multiparameter flow cytometry detects leukemic cells below the threshold of morphologic remission. Sensitive MRD monitoring informs treatment response, risk stratification, and need for therapy intensification. Assay design requires disease-specific antigen aberrant phenotypes and validated sensitivity limits.'}]},
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
                                                'explanation': 'A routine electrolyte panel typically measures sodium, potassium, chloride, and bicarbonate (total CO2), reflecting extracellular fluid composition and acid–base balance. These analytes are central to evaluating dehydration, renal disorders, and metabolic disturbances. Interpretation requires awareness of preanalytic factors such as hemolysis affecting potassium.'},
                                               {'question': 'Creatinine mainly reflects?',
                                                'options': ['A) Kidney filtration function roughly',
                                                            'B) Only liver synthetic function '
                                                            'alone',
                                                            'C) Only muscle enzymes only forever',
                                                            'D) Only amylase only'],
                                                'answer': 'A) Kidney filtration function roughly',
                                                'explanation': 'Serum creatinine is produced from muscle creatine metabolism and is cleared primarily by glomerular filtration. Rising creatinine generally indicates reduced glomerular filtration rate, though levels also depend on muscle mass, age, sex, and some drugs. Estimated GFR equations convert creatinine into a more physiologically interpretable filtration index.'},
                                               {'question': 'Hypoglycemia means?',
                                                'options': ['A) Low blood glucose',
                                                            'B) Always high glucose',
                                                            'C) Only high ketones without glucose '
                                                            'context',
                                                            'D) Only high Hb'],
                                                'answer': 'A) Low blood glucose',
                                                'explanation': 'Hypoglycemia denotes abnormally low plasma glucose and can cause neuroglycopenic and autonomic symptoms. Critical hypoglycemia is a medical emergency requiring rapid confirmation and treatment. Laboratory practice includes critical-value notification and investigation of causes ranging from insulin excess to hepatic failure and adrenal insufficiency.'}],
                                      'medium': [{'question': 'AST/ALT pattern helps assess?',
                                                  'options': ['A) Hepatocellular injury',
                                                              'B) Only bone disease exclusively',
                                                              'C) Only hemolysis exclusively '
                                                              'forever',
                                                              'D) Only thyroid only'],
                                                  'answer': 'A) Hepatocellular injury',
                                                  'explanation': 'Aspartate and alanine aminotransferases (AST and ALT) are cytosolic enzymes released with hepatocyte injury. Elevations with an hepatocellular pattern support hepatitis, ischemic injury, or toxin-mediated damage. In contrast, ALP and GGT elevations more often reflect cholestasis or biliary obstruction.'},
                                                 {'question': 'Troponin rise suggests?',
                                                  'options': ['A) Myocardial injury',
                                                              'B) Only UTI',
                                                              'C) Only anemia',
                                                              'D) Only caries'],
                                                  'answer': 'A) Myocardial injury',
                                                  'explanation': 'Cardiac troponins I and T are regulatory proteins released into blood after cardiomyocyte necrosis or injury. Serial rises and/or falls above the assay-specific 99th percentile support myocardial injury and, with clinical criteria, acute myocardial infarction. High-sensitivity assays detect earlier and smaller elevations but require clinical correlation.'},
                                                 {'question': 'HbA1c reflects?',
                                                  'options': ['A) Average glycemia over ~2–3 '
                                                              'months',
                                                              "B) Only today's glucose",
                                                              'C) Only urine glucose',
                                                              'D) Only insulin dose brand'],
                                                  'answer': 'A) Average glycemia over ~2–3 months',
                                                  'explanation': 'Hemoglobin A1c forms by nonenzymatic glycation of hemoglobin and reflects average glycemia over approximately the preceding 2–3 months, corresponding to erythrocyte lifespan. It is used for diabetes diagnosis and long-term glycemic monitoring when conditions affecting red-cell turnover are absent. Method-specific NGSP/IFCC standardization underpins comparability.'}],
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
                                                'explanation': 'The osmolal gap is the difference between measured serum osmolality and osmolality calculated from sodium, glucose, and urea. An elevated gap suggests unmeasured osmotically active solutes such as methanol, ethylene glycol, or isopropanol. Toxic-alcohol evaluation pairs the gap with anion gap, blood gases, and specific analyte assays.'},
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
                                                'explanation': 'The high-dose hook (prozone-like) effect in sandwich immunoassays occurs when extremely high antigen concentrations saturate capture and detection antibodies, preventing sandwich formation. The reported result can be falsely low or normal despite massive analyte excess. Dilution of the specimen restores linearity and reveals the true high concentration.'},
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
                                                'explanation': 'Pseudohyponatremia is an artifactual low sodium reported by indirect potentiometry when marked hyperlipidemia or hyperproteinemia expands the non-aqueous plasma fraction. Direct ion-selective electrode methods that measure activity in the undiluted aqueous phase are largely unaffected. Recognizing method dependence prevents inappropriate hypotonic fluid therapy.'}],
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
                                                   'explanation': 'Critical laboratory values identify results that may indicate life-threatening conditions requiring immediate clinical action. Laboratory policy mandates rapid clinician notification, read-back verification, and documentation of the communication. Timely reporting is a core patient-safety and accreditation requirement.'},
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
                                                   'explanation': 'Delta checks compare a current result with a patient’s recent prior values to detect implausible analytic or identity errors. Large unexpected changes may indicate specimen mix-up, IV contamination, or instrument malfunction rather than true physiology. Investigation before release protects against reporting erroneous results.'},
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
                                                   'explanation': 'Air bubbles in arterial blood-gas syringes allow gas exchange that can falsely raise pO2 toward ambient air and alter pCO2. Delayed analysis permits ongoing cellular metabolism that consumes oxygen and generates CO2. Specimens should be carefully debubbled, mixed, and analyzed promptly under anaerobic conditions.'}]},
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
                                                  'explanation': 'Gram-positive bacteria retain crystal violet–iodine complex within a thick peptidoglycan cell wall and appear purple/blue after decolorization and safranin counterstain. Gram-negative organisms lose the primary stain and take up the pink/red counterstain because of their thinner peptidoglycan and outer membrane. Gram morphology guides initial empiric interpretation and workup.'},
                                                 {'question': 'Blood culture indication theme?',
                                                  'options': ['A) Suspected bacteremia/sepsis',
                                                              'B) Only routine wellness',
                                                              'C) Only anemia workup alone',
                                                              'D) Only lipid panel'],
                                                  'answer': 'A) Suspected bacteremia/sepsis',
                                                  'explanation': 'Blood cultures are indicated when bacteremia or sepsis is suspected clinically. Adequate blood volume per bottle and collection of multiple sets before antibiotics maximize sensitivity and help distinguish true pathogens from contaminants. Timing relative to fever spikes is less critical than volume and aseptic technique.'},
                                                 {'question': 'Antibiotic susceptibility testing '
                                                              'guides?',
                                                  'options': ['A) Therapy choice',
                                                              'B) Only hospital food menus',
                                                              'C) Only bed assignment',
                                                              'D) Only billing codes alone'],
                                                  'answer': 'A) Therapy choice',
                                                  'explanation': 'Antimicrobial susceptibility testing determines whether an isolate is inhibited by achievable drug concentrations. Interpretive breakpoints from standards organizations convert MICs or zone sizes into susceptible, intermediate, or resistant categories. Results guide targeted therapy and antimicrobial stewardship.'}],
                                        'medium': [{'question': 'Acid-fast stain used for?',
                                                    'options': ['A) Mycobacteria',
                                                                'B) Only streptococci',
                                                                'C) Only Candida always only',
                                                                'D) Only viruses'],
                                                    'answer': 'A) Mycobacteria',
                                                    'explanation': 'Acid-fast stains such as Ziehl–Neelsen or fluorochrome auramine exploit mycolic acid–rich cell walls that resist acid-alcohol decolorization. Mycobacteria, including Mycobacterium tuberculosis complex, appear acid-fast and are central targets of this method. Positive smears accelerate airborne precautions and confirmatory culture or molecular testing.'},
                                                   {'question': 'Catalase-positive gram-positive '
                                                                'cocci suggest?',
                                                    'options': ['A) Staphylococci',
                                                                'B) Streptococci typically',
                                                                'C) Enterococci always catalase+++ '
                                                                'classic teaching opposite',
                                                                'D) Only Neisseria'],
                                                    'answer': 'A) Staphylococci',
                                                    'explanation': 'Catalase decomposes hydrogen peroxide to water and oxygen; bubbling indicates a positive reaction. Among gram-positive cocci, staphylococci are typically catalase-positive, whereas streptococci and enterococci are catalase-negative. This rapid test is an early branch point in the identification algorithm.'},
                                                   {'question': 'CSF Gram stain urgency?',
                                                    'options': ['A) Critical for meningitis',
                                                                'B) Can wait days always',
                                                                'C) Only research interest',
                                                                'D) Never report'],
                                                    'answer': 'A) Critical for meningitis',
                                                    'explanation': 'CSF Gram stain is a time-critical test in suspected bacterial meningitis because early morphologic clues can guide empiric therapy. Detection of organisms or marked neutrophilic pleocytosis warrants immediate clinician notification. Culture, antigen, and molecular assays complement but do not replace urgent smear review.'}],
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
                                                  'explanation': 'Methicillin-resistant Staphylococcus aureus (MRSA) harbors mecA (or mecC), encoding altered penicillin-binding protein PBP2a with reduced β-lactam affinity. Phenotypic detection uses cefoxitin or oxacillin testing, and molecular assays may target mecA directly. MRSA identification triggers infection-control measures and guides antibiotic selection away from standard β-lactams.'},
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
                                                  'explanation': 'Obligate anaerobes are killed or inhibited by oxygen exposure during collection and transport. Successful anaerobic culture requires oxygen-free transport systems, prompt plating onto prereduced media, and incubation in anaerobic atmospheres. Poor preanalytics are a common cause of false-negative anaerobic cultures.'},
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
                                                  'explanation': 'Blood-culture contaminants are often skin flora recovered from only one bottle or one set when multiple sets are drawn. True bacteremia more often appears in multiple sets with recognized pathogens and compatible clinical findings. Distinguishing contamination from infection prevents unnecessary antibiotics and repeat procedures.'}],
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
                                                     'explanation': 'Carbapenemase-producing Enterobacterales hydrolyze carbapenems and many other β-lactams, severely limiting therapeutic options. Specialized phenotypic and molecular tests detect carbapenemase production to guide therapy and infection control. These organisms are high-priority multidrug-resistant pathogens with substantial public-health impact.'},
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
                                                     'explanation': 'Neisseria meningitidis can cause severe laboratory-acquired infection through aerosol exposure during manipulation of cultures. Work requiring aerosol-generating procedures is performed with appropriate biosafety level practices, PPE, and often vaccination policies. Strict handling protects laboratory personnel.'},
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
                                                     'explanation': 'Matrix-assisted laser desorption/ionization time-of-flight (MALDI-TOF) mass spectrometry identifies microorganisms from characteristic ribosomal protein spectra. Spectra are matched to validated databases for genus/species-level identification within minutes after colony growth. Rapid ID shortens time to targeted therapy compared with biochemical panels alone.'}]},
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
                                        'explanation': 'Enzyme-linked immunosorbent assay (ELISA) immobilizes antigen or antibody on a solid phase and uses an enzyme-conjugated detection reagent to generate a measurable signal. Depending on design, ELISA can quantify antigen or specific antibody. It remains a workhorse platform for infectious-disease and autoimmune serology.'},
                                       {'question': 'IgM generally indicates?',
                                        'options': ['A) Acute/recent response themes',
                                                    'B) Only lifelong remote immunity always',
                                                    'C) Only allergy only forever',
                                                    'D) Only transfusion reaction only'],
                                        'answer': 'A) Acute/recent response themes',
                                        'explanation': 'IgM is the isotype produced earliest in a primary humoral response and therefore often marks acute or recent antigen exposure. IgM may also persist or reappear with reactivation in some infections, so clinical and assay context matter. Paired IgG testing and symptom timing refine serologic interpretation.'},
                                       {'question': 'Blood type ABO based on?',
                                        'options': ['A) RBC antigens / plasma isoagglutinins',
                                                    'B) Only RhD alone',
                                                    'C) Only HLA only',
                                                    'D) Only platelet antigens only'],
                                        'answer': 'A) RBC antigens / plasma isoagglutinins',
                                        'explanation': 'ABO blood group is defined by carbohydrate antigens on the red-cell surface and by reciprocal isoagglutinins (anti-A/anti-B) in plasma. Forward typing detects RBC antigens; reverse typing confirms expected plasma antibodies. This antigen–antibody relationship is foundational to transfusion compatibility.'}],
                              'medium': [{'question': 'ANA testing used in?',
                                          'options': ['A) Autoimmune disease workups',
                                                      'B) Only UTI',
                                                      'C) Only fracture healing',
                                                      'D) Only caries'],
                                          'answer': 'A) Autoimmune disease workups',
                                          'explanation': 'Antinuclear antibody (ANA) testing screens for autoantibodies directed against nuclear antigens and is used in the workup of systemic autoimmune diseases such as SLE. Indirect immunofluorescence reports titer and pattern, which help prioritize antigen-specific follow-up assays. Low-titer ANA can occur in healthy individuals, so clinical correlation is essential.'},
                                         {'question': 'Window period means?',
                                          'options': ['A) Infection present but markers not yet '
                                                      'detectable',
                                                      'B) Always lifelong immunity',
                                                      'C) Assay never works',
                                                      'D) Only sample clotting'],
                                          'answer': 'A) Infection present but markers not yet '
                                                    'detectable',
                                          'explanation': 'The serologic window period is the interval after infection when the pathogen is present but diagnostic markers remain below detection limits. Antibody assays have longer windows than many nucleic acid tests for the same agent. Understanding window periods is critical for donor screening and early-infection diagnosis.'},
                                         {'question': 'Complement C3/C4 low in?',
                                          'options': ['A) Some immune complex diseases (e.g., '
                                                      'lupus nephritis themes)',
                                                      'B) Always healthy states only',
                                                      'C) Only dehydration',
                                                      'D) Only iron deficiency'],
                                          'answer': 'A) Some immune complex diseases (e.g., lupus '
                                                    'nephritis themes)',
                                          'explanation': 'Complement components C3 and C4 are consumed in classical-pathway activation by immune complexes. Low C3/C4 levels are characteristic of active systemic lupus erythematosus with nephritis and some other immune-complex diseases. Serial complement measurement helps monitor disease activity alongside clinical findings.'}],
                              'hard': [{'question': 'A junior colleague asks for the single best '
                                                    'answer. Prozone/hook in serology causes? '
                                                    'Beware of near-miss distractors.',
                                        'options': ['A) False negative at antibody excess',
                                                    'B) Always true positive stronger',
                                                    'C) Only hemolysis',
                                                    'D) Only icterus'],
                                        'answer': 'A) False negative at antibody excess',
                                        'explanation': 'Prozone (antibody excess) in agglutination or precipitation serology can prevent lattice formation, yielding a false-negative result despite high specific antibody. Diluting the specimen reduces antibody concentration into the zone of equivalence and unmasks reactivity. Hook effects in immunoassays are related phenomena at extreme analyte excess.'},
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
                                        'explanation': 'Flow cytometric immunophenotyping uses fluorochrome-labeled antibodies to quantify lineage and maturation antigens on intact cells. In hematopathology, CD marker panels distinguish lymphoid from myeloid neoplasms and subclassify leukemias and lymphomas. Multiparameter analysis is essential for diagnosis and MRD monitoring.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Rheumatoid factor can interfere with? '
                                                    'Beware of near-miss distractors.',
                                        'options': ['A) Some immunoassays',
                                                    'B) Never any assay',
                                                    'C) Only gram stains',
                                                    'D) Only microhematocrit'],
                                        'answer': 'A) Some immunoassays',
                                        'explanation': 'Rheumatoid factor is an autoantibody, usually IgM, that binds the Fc portion of IgG. In immunoassays, RF can bridge capture and detection antibodies or otherwise distort antigen–antibody reactions, producing false-positive or false-negative results. Awareness of RF interference guides method selection and confirmatory testing.'}],
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
                                           'explanation': 'Heterophile antibodies are human antibodies that recognize animal immunoglobulin reagents used in sandwich immunoassays. They can create false bridges between capture and detection antibodies, generating spuriously high or low analyte values. Discordance with the clinical picture prompts heterophile-blocking reagents, alternative methods, or dilutions.'},
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
                                           'explanation': 'Interferon-γ release assays (IGRAs) such as QuantiFERON measure T-cell IFN-γ responses to Mycobacterium tuberculosis–specific antigens. A positive result indicates immune sensitization consistent with TB infection but does not by itself distinguish latent from active disease. Interpretation requires clinical, radiographic, and microbiologic correlation.'},
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
                                           'explanation': 'Cryoglobulins precipitate at temperatures below body temperature and redissolve on warming. For accurate detection, blood must be collected and transported warm (approximately 37 °C) until serum is separated. Cold exposure before separation can falsely lower measured cryoglobulin by premature precipitation.'}]},
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
                                        'explanation': 'ABO forward typing uses reagent anti-A and anti-B to detect A and B antigens on the patient’s red cells. Reverse typing tests patient plasma against A1 and B reagent cells to detect isoagglutinins. Concordant forward and reverse results establish the ABO type used for transfusion.'},
                                       {'question': 'Crossmatch checks?',
                                        'options': ['A) Compatibility between donor RBC and '
                                                    'recipient plasma',
                                                    'B) Only donor HIV only',
                                                    'C) Only platelet count',
                                                    'D) Only ESR'],
                                        'answer': 'A) Compatibility between donor RBC and '
                                                  'recipient plasma',
                                        'explanation': 'A serologic crossmatch combines donor red cells with recipient plasma to detect incompatibility from ABO mismatch or unexpected alloantibodies. Compatibility testing is a final pretransfusion check after type and antibody screen. Electronic crossmatch may substitute when validated conditions are met.'},
                                       {'question': 'O negative often used as?',
                                        'options': ['A) Emergency uncrossmatched RBC in selected '
                                                    'protocols',
                                                    'B) Universal plasma always',
                                                    'C) Only platelet product',
                                                    'D) Only cryoprecipitate'],
                                        'answer': 'A) Emergency uncrossmatched RBC in selected '
                                                  'protocols',
                                        'explanation': 'Group O RhD-negative red cells lack A, B, and RhD antigens and are therefore preferred for emergency transfusion when the recipient’s blood type is unknown. Institutional massive-transfusion protocols define when uncrossmatched O-negative (or O-positive in selected males) units may be issued. Switch to type-specific blood as soon as typing is complete.'}],
                              'medium': [{'question': 'RhIg indicated for?',
                                          'options': ['A) RhD-negative mother at risk for anti-D '
                                                      'sensitization themes',
                                                      'B) All mothers always regardless of Rh',
                                                      'C) Only fathers',
                                                      'D) Only platelet donors always'],
                                          'answer': 'A) RhD-negative mother at risk for anti-D '
                                                    'sensitization themes',
                                          'explanation': 'Rh immune globulin (RhIg) provides passive anti-D that prevents RhD-negative individuals from forming alloanti-D after exposure to RhD-positive red cells. It is indicated in obstetrics for RhD-negative pregnant patients at risk of fetomaternal hemorrhage and after certain sensitizing events. Correct dosing is based on estimated volume of RhD-positive RBCs.'},
                                         {'question': 'Acute hemolytic reaction classic cause?',
                                          'options': ['A) ABO incompatibility',
                                                      'B) Only mild allergic always',
                                                      'C) Only citrate only',
                                                      'D) Only TACO only'],
                                          'answer': 'A) ABO incompatibility',
                                          'explanation': 'Acute hemolytic transfusion reactions are most often caused by ABO-incompatible red-cell transfusion due to clerical or identification error. Preformed isoagglutinins fix complement and produce intravascular hemolysis with fever, hypotension, and hemoglobinuria. Immediate cessation of transfusion and clerical recheck are mandatory first steps.'},
                                         {'question': 'DAT detects?',
                                          'options': ['A) In vivo coated RBCs',
                                                      'B) Only free plasma antibody always only',
                                                      'C) Only bacteria',
                                                      'D) Only glucose'],
                                          'answer': 'A) In vivo coated RBCs',
                                          'explanation': 'The direct antiglobulin test (DAT) detects IgG and/or complement already bound to red cells in vivo using anti-human globulin reagent. A positive DAT supports immune hemolysis in autoimmune hemolytic anemia, hemolytic disease of the fetus/newborn, or drug- and transfusion-related processes. Elution and antibody identification characterize the coating antibody.'}],
                              'hard': [{'question': 'A junior colleague asks for the single best '
                                                    'answer. Antibody screen positive next? Beware '
                                                    'of near-miss distractors.',
                                        'options': ['A) Antibody identification panel',
                                                    'B) Ignore and issue anything',
                                                    'C) Only give platelets',
                                                    'D) Cancel blood bank forever'],
                                        'answer': 'A) Antibody identification panel',
                                        'explanation': 'A positive antibody screen indicates unexpected red-cell alloantibody (or autoantibody) in the plasma and requires an identification panel against typed reagent cells. Once specificity is known, donor units lacking the corresponding antigen are selected and crossmatched. Incomplete identification risks hemolytic transfusion reactions.'},
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
                                        'explanation': 'TRALI is non-cardiogenic permeability pulmonary edema related to donor antibodies or biologic response modifiers, whereas TACO is hydrostatic pulmonary edema from volume overload. Both present with post-transfusion respiratory distress but differ in blood pressure, BNP, and cardiac findings. Distinguishing them guides diuretics, ventilatory support, and donor-center reporting.'},
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
                                        'explanation': 'Massive transfusion dilutes coagulation factors and platelets and can cause hypothermia and citrate-related hypocalcemia. Balanced ratios of RBC, plasma, and platelets, plus calcium repletion and warming, mitigate trauma-induced coagulopathy. Viscoelastic testing may refine component therapy in real time.'}],
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
                                           'explanation': 'Emergency release of uncrossmatched blood requires documented physician acknowledgment of urgency and acceptance of residual incompatibility risk. The transfusion service continues ABO/Rh typing, antibody screen, and compatibility testing as specimens become available. Traceability and follow-up documentation satisfy safety and regulatory standards.'},
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
                                           'explanation': 'Warm autoimmune hemolytic anemia coats autologous and allogeneic red cells with IgG, often causing panagglutination that obscures alloantibody detection and crossmatch. Special techniques such as adsorptions help reveal underlying alloantibodies. Transfusion decisions use least-incompatible units coordinated with the clinical team.'},
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
                                           'explanation': 'Platelet components are stored at room temperature with agitation to preserve function, which also favors bacterial proliferation if contamination occurs. Bacterial sepsis from platelets has historically been a leading infectious transfusion risk. Visual inspection, culture or rapid bacterial detection, and pathogen-reduction strategies mitigate this hazard.'}]},
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
                                            'explanation': 'Neutral buffered formalin cross-links proteins and stabilizes tissue architecture for histologic processing. Adequate fixation time and volume prevent autolysis and preserve morphologic detail for H&E and many ancillary studies. Over- or under-fixation can compromise both morphology and antigenicity.'},
                                           {'question': 'H&E stain shows?',
                                            'options': ['A) General tissue morphology',
                                                        'B) Only fat exclusively',
                                                        'C) Only organisms always only',
                                                        'D) Only iron only'],
                                            'answer': 'A) General tissue morphology',
                                            'explanation': 'Hematoxylin and eosin (H&E) is the routine histologic stain: hematoxylin colors nucleic acids blue-purple and eosin stains proteins pink. H&E provides the primary morphologic assessment of tissue architecture and cytologic features. Most diagnoses begin with H&E before special stains or immunohistochemistry.'},
                                           {'question': 'Pap smear is a?',
                                            'options': ['A) Cytology screening test',
                                                        'B) Only blood culture',
                                                        'C) Only CBC',
                                                        'D) Only PT'],
                                            'answer': 'A) Cytology screening test',
                                            'explanation': 'The Papanicolaou (Pap) smear is a cytologic screening test that samples cervical epithelial cells to detect squamous intraepithelial lesions and carcinoma. Liquid-based cytology improves adequacy and permits HPV co-testing in many algorithms. Abnormal cytology triggers colposcopic evaluation and biopsy as indicated.'}],
                                  'medium': [{'question': 'Immunohistochemistry detects?',
                                              'options': ['A) Antigens in tissue with antibodies',
                                                          'B) Only electrolytes in serum',
                                                          'C) Only urine SG',
                                                          'D) Only ESR'],
                                              'answer': 'A) Antigens in tissue with antibodies',
                                              'explanation': 'Immunohistochemistry (IHC) uses antibodies to localize specific antigens in tissue sections, visualized by chromogenic or fluorescent detection. IHC supports tumor classification, predicts therapy targets, and detects infectious organisms in situ. Antibody validation, controls, and fixation conditions determine result reliability.'},
                                             {'question': 'Frozen section purpose?',
                                              'options': ['A) Intraoperative rapid diagnosis',
                                                          'B) Permanent best morphology always '
                                                          'superior to paraffin forever for '
                                                          'everything',
                                                          'C) Only research posters',
                                                          'D) Only teaching without clinical use'],
                                              'answer': 'A) Intraoperative rapid diagnosis',
                                              'explanation': 'Frozen section provides rapid intraoperative histologic diagnosis on freshly frozen tissue to guide immediate surgical decisions such as margin status or tumor confirmation. Freezing artifact and limited sampling reduce morphologic quality compared with formalin-fixed paraffin-embedded sections. Permanent sections remain the definitive diagnostic standard.'},
                                             {'question': 'Cytopathology adequacy matters because?',
                                              'options': ['A) Insufficient cells → unsatisfactory '
                                                          'interpretation',
                                                          'B) Always diagnostic regardless',
                                                          'C) Volume never matters',
                                                          'D) Labels optional'],
                                              'answer': 'A) Insufficient cells → unsatisfactory '
                                                        'interpretation',
                                              'explanation': 'Cytopathology adequacy criteria ensure that sufficient well-preserved cells are present for a reliable interpretation. Unsatisfactory specimens risk false-negative reports and usually require recollection. Reporting systems such as Bethesda for thyroid or cervical cytology standardize adequacy and diagnostic categories.'}],
                                  'hard': [{'question': 'A junior colleague asks for the single '
                                                        'best answer. Poor fixation artifact can? '
                                                        'Beware of near-miss distractors.',
                                            'options': ['A) Mimic/ obscure pathology',
                                                        'B) Improve IHC always',
                                                        'C) Never affect diagnosis',
                                                        'D) Only change barcode'],
                                            'answer': 'A) Mimic/ obscure pathology',
                                            'explanation': 'Inadequate fixation allows autolysis and poor nuclear detail that can mimic or obscure neoplasia and inflammation. Delayed immersion, thick specimens, or insufficient formalin volume are common causes. Controlled preanalytic handling is essential for accurate anatomic pathology interpretation.'},
                                           {'question': 'A junior colleague asks for the single '
                                                        'best answer. Special stain AFB used for? '
                                                        'Beware of near-miss distractors.',
                                            'options': ['A) Mycobacteria in tissue',
                                                        'B) Only glycogen only',
                                                        'C) Only collagen only',
                                                        'D) Only amyloid only'],
                                            'answer': 'A) Mycobacteria in tissue',
                                            'explanation': 'Acid-fast bacillus (AFB) special stains on tissue highlight mycobacteria that may be sparse in granulomatous inflammation. Findings should be correlated with microbiology culture and molecular assays for speciation and susceptibility. A negative tissue stain does not exclude mycobacterial infection because of limited sensitivity.'},
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
                                            'explanation': 'Molecular assays on formalin-fixed paraffin-embedded (FFPE) tissue require adequate tumor cellularity and nucleic acid quality after fixation and processing. Macrodissection or microdissection enriches neoplastic DNA/RNA for mutation, fusion, or MSI testing. Poor quality or low tumor content yields false-negative or uninterpretable genomic results.'}],
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
                                               'explanation': 'An unexpected malignant diagnosis on frozen section can immediately alter the surgical plan. The pathologist must communicate findings clearly, directly, and promptly to the operating surgeon, documenting the intraoperative consultation. Ambiguous wording risks inappropriate resection or missed intervention.'},
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
                                               'explanation': 'Cytotechnologists perform primary screening of cytology slides, but abnormal or difficult cases require pathologist review per laboratory hierarchy and regulations. This layered review improves diagnostic accuracy and compliance with quality standards. Clear escalation pathways protect patients from missed high-grade lesions.'},
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
                                               'explanation': 'Decalcification softens mineralized bone so it can be sectioned, but prolonged or harsh acid decalcification degrades morphology and can destroy antigens and nucleic acids. Laboratories balance the minimum decalcification needed for cutting against preservation for IHC and molecular testing. Gentle or EDTA-based methods better preserve biomolecules.'}]},
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
                                          'explanation': 'Stool ova-and-parasite (O&P) examination detects helminth eggs and protozoan cysts or trophozoites using concentration techniques and permanent stained smears. Multiple specimens improve sensitivity because shedding can be intermittent. Clinical history including travel and immune status guides which parasites are sought.'},
                                         {'question': 'Malaria diagnosed commonly by?',
                                          'options': ['A) Blood films (thick/thin)',
                                                      'B) Only urine dipstick',
                                                      'C) Only chest x-ray',
                                                      'D) Only ECG'],
                                          'answer': 'A) Blood films (thick/thin)',
                                          'explanation': 'Malaria diagnosis classically relies on Giemsa-stained thick and thin blood films. Thick films maximize sensitivity; thin films preserve morphology for Plasmodium species identification and parasitemia estimation. Rapid antigen tests and PCR complement microscopy but speciation still guides therapy.'},
                                         {'question': 'Enterobius best sampled by?',
                                          'options': ['A) Perianal tape test',
                                                      'B) Only blood culture',
                                                      'C) Only throat swab',
                                                      'D) Only CSF'],
                                          'answer': 'A) Perianal tape test',
                                          'explanation': 'Enterobius vermicularis (pinworm) females deposit eggs on perianal skin, usually at night. The cellulose-tape (paddle) test samples that area and is more sensitive than routine stool O&P for this nematode. Eggs are flattened on one side and are diagnostic when identified microscopically.'}],
                                'medium': [{'question': 'Giardia trophozoites seen in?',
                                            'options': ['A) Stool (or duodenal) specimens',
                                                        'B) Only blood',
                                                        'C) Only sputum always',
                                                        'D) Only CSF always'],
                                            'answer': 'A) Stool (or duodenal) specimens',
                                            'explanation': 'Giardia duodenalis trophozoites and cysts are identified in stool by microscopy, and antigen or NAAT assays increase detection sensitivity. Trophozoites may also be recovered from duodenal fluid in difficult cases. Infection causes small-bowel malabsorption with greasy, foul-smelling diarrhea.'},
                                           {'question': 'E. histolytica concern?',
                                            'options': ['A) Invasive amebiasis; distinguish from '
                                                        'nonpathogenic amebae',
                                                        'B) Always harmless commensals identical',
                                                        'C) Only skin flora',
                                                        'D) Only contaminants never pathogenic'],
                                            'answer': 'A) Invasive amebiasis; distinguish from '
                                                      'nonpathogenic amebae',
                                            'explanation': 'Entamoeba histolytica can invade intestinal mucosa and disseminate to form liver abscesses, whereas morphologically similar nonpathogenic amebae do not. Differentiation uses antigen detection, molecular assays, or careful morphologic criteria with ingested erythrocytes as a clue. Correct identification prevents both undertreatment and unnecessary therapy.'},
                                           {'question': 'Ziehl-Neelsen modified may help detect?',
                                            'options': ['A) Cryptosporidium oocysts among uses',
                                                        'B) Only staphylococci',
                                                        'C) Only yeast always better gram',
                                                        'D) Only mycobacteria exclusively never '
                                                        'crypto'],
                                            'answer': 'A) Cryptosporidium oocysts among uses',
                                            'explanation': 'Cryptosporidium oocysts retain modified acid-fast stains and appear as small (about 4–6 µm) red spheres against a blue-green background. Modified Ziehl–Neelsen or safranin methods improve detection compared with routine trichrome alone. Immunocompromised patients are at particular risk for prolonged watery diarrhea.'}],
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
                                          'explanation': 'Babesia intraerythrocytic parasites may form pathognomonic tetrad “Maltese cross” arrangements and can mimic Plasmodium on blood films. Unlike malaria, babesiosis is tick-borne, has no travel requirement, and does not produce hemozoin pigment. Accurate differentiation directs antiparasitic therapy and transfusion precautions.'},
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
                                          'explanation': 'Echinococcal (hydatid) cysts contain highly antigenic fluid; spillage during surgery or grossing can trigger anaphylaxis and secondary cyst dissemination. Laboratory and surgical teams handle intact cysts with controlled aspiration protocols and avoid unnecessary puncture. Coordination between pathology and surgery minimizes rupture risk.'},
                                         {'question': 'A junior colleague asks for the single best '
                                                      'answer. Concentration methods increase? '
                                                      'Beware of near-miss distractors.',
                                          'options': ['A) Sensitivity for ova/cysts',
                                                      'B) Specificity to 100% always',
                                                      'C) Only turnaround slower without benefit',
                                                      'D) No use'],
                                          'answer': 'A) Sensitivity for ova/cysts',
                                          'explanation': 'Parasitology concentration methods such as formalin–ethyl acetate sedimentation increase recovery of eggs, cysts, and larvae by separating them from fecal debris. Concentrates improve analytic sensitivity compared with direct wet mounts alone. Permanent stains of fixed stool remain necessary for many protozoan identifications.'}],
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
                                             'explanation': 'Leishmania amastigotes parasitize macrophages and are demonstrated in bone marrow, splenic, or tissue aspirates/biopsies as intracellular organisms with a nucleus and kinetoplast. Species identification and clinical syndrome (visceral vs cutaneous) guide therapy. Diagnosis is often performed in specialized reference settings with culture or PCR support.'},
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
                                             'explanation': 'Automated hematology analyzers may flag malaria-related abnormalities but lack sufficient specificity and speciation capability for definitive diagnosis. Expert thick-and-thin smear review remains required to confirm infection, identify Plasmodium species, and quantify parasitemia. Mis-speciation can lead to inappropriate antimalarial regimens.'},
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
                                             'explanation': 'Formalin used in stool fixative vials is a hazardous chemical with toxic and sensitizing properties defined in the safety data sheet (SDS). Laboratories handle, store, and dispose of formalin-containing specimens under chemical hygiene controls and appropriate PPE. Minimizing exposure protects technologists during O&P processing.'}]},
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
                                                   'explanation': 'Polymerase chain reaction (PCR) enzymatically amplifies a defined nucleic acid target through repeated cycles of denaturation, annealing, and extension. Exponential amplification enables detection of low-abundance DNA or RNA (after reverse transcription). PCR underpins much of clinical molecular infectious-disease and genetic testing.'},
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
                                                   'explanation': 'PCR is highly susceptible to false positives from amplicon or specimen contamination. Laboratories use unidirectional workflow, physically separated pre- and post-PCR areas, aerosol-resistant tips, and no-template controls to detect contamination events. Strict contamination control preserves analytic specificity.'},
                                                  {'question': 'Viral load assays monitor?',
                                                   'options': ['A) Quantity of virus nucleic acid',
                                                               'B) Only bacterial colonies on '
                                                               'plate only',
                                                               'C) Only HbA1c',
                                                               'D) Only urine color'],
                                                   'answer': 'A) Quantity of virus nucleic acid',
                                                   'explanation': 'Viral load assays quantify pathogen nucleic acid, typically as IU/mL or copies/mL, using calibrated real-time PCR or related methods. Serial HIV and HCV viral loads monitor treatment efficacy and detect virologic failure. Standardization and assay dynamics determine how results are compared over time.'}],
                                         'medium': [{'question': 'Ct value roughly relates to?',
                                                     'options': ['A) Inverse of target amount '
                                                                 '(method-dependent)',
                                                                 'B) Always exact organism count '
                                                                 'identical across platforms',
                                                                 'C) Only cycle of moon',
                                                                 'D) Only reagent lot letter'],
                                                     'answer': 'A) Inverse of target amount '
                                                               '(method-dependent)',
                                                     'explanation': 'In real-time PCR, the cycle threshold (Ct) is the cycle at which fluorescence exceeds a defined threshold. Lower Ct values generally indicate higher starting target concentration, though the relationship is assay- and matrix-dependent. Ct values are interpretive aids, not universal quantitative units across platforms.'},
                                                    {'question': 'Internal control failure '
                                                                 'suggests?',
                                                     'options': ['A) Inhibition/extraction problem',
                                                                 'B) Perfect run',
                                                                 'C) Always true negative',
                                                                 'D) Ignore'],
                                                     'answer': 'A) Inhibition/extraction problem',
                                                     'explanation': 'An internal control co-extracted and co-amplified with the patient specimen monitors extraction efficiency and PCR inhibition. Internal-control failure with a negative target result renders the test invalid because true target could be masked. Repeat testing after re-extraction or recollection is required.'},
                                                    {'question': 'Genotyping may guide?',
                                                     'options': ['A) Therapy (e.g., '
                                                                 'resistance/pharmacogenetics)',
                                                                 'B) Only room assignment',
                                                                 'C) Only meal choice',
                                                                 'D) Only parking'],
                                                     'answer': 'A) Therapy (e.g., '
                                                               'resistance/pharmacogenetics)',
                                                     'explanation': 'Genotyping identifies sequence variants that predict drug resistance or alter drug metabolism, as in HIV resistance testing or pharmacogenetic loci such as CYP2C19. Results support selection or avoidance of specific therapies. Clinical utility depends on validated variant interpretation guidelines.'}],
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
                                                   'explanation': 'Next-generation sequencing (NGS) panels generate massive parallel reads that require bioinformatic pipelines for alignment, variant calling, filtering, and annotation. Quality metrics such as coverage depth, uniformity, and contamination estimates determine whether a result is reportable. Clinical interpretation integrates technical findings with disease-specific knowledge bases.'},
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
                                                   'explanation': 'MRD PCR assays amplify leukemia-specific targets such as fusion transcripts or clonal immunoglobulin/T-cell receptor rearrangements at very low levels. Sensitivities often reach 10⁻⁴ to 10⁻⁶, far below morphologic detection. Quantitative MRD kinetics guide consolidation intensity and transplant decisions in hematologic malignancies.'},
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
                                                   'explanation': 'Specimen identity errors can cause catastrophic molecular misdiagnosis. Laboratories use barcodes, chain-of-custody checks, and sometimes polymorphic genetic markers to verify that the nucleic acid matches the intended patient. Detecting sample swaps prevents incorrect genotype-directed therapy.'}],
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
                                                      'explanation': 'Laboratory-developed tests (LDTs) must be validated or verified for accuracy, precision, reportable range, and other performance characteristics before clinical use under CLIA and accreditation standards. Documentation of analytic and clinical performance supports patient-care reporting. Unvalidated research assays are not acceptable for clinical decisions.'},
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
                                                      'explanation': 'Amplicon contamination outbreaks produce clusters of unexpected positive PCR results, often with late Ct values or positivity in negative controls. Immediate cessation of testing, environmental cleaning, reagent discard, and root-cause analysis are required. Resumption occurs only after contamination is eradicated and controls perform as expected.'},
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
                                                      'explanation': 'Circulating cell-free DNA assays measure fragmented extracellular DNA present at low concentrations in plasma. Preanalytic variables—tube type, time to spin, and double centrifugation—strongly affect yield and contaminating genomic DNA. Analytic sensitivity must account for low mutant allele fractions and fragment size distributions.'}]},
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
                                    'explanation': 'Quality assurance (QA) encompasses the organized systems, policies, and monitoring activities that ensure laboratory results are accurate, reliable, and clinically useful. QA spans preanalytic, analytic, and postanalytic phases rather than a single control material. Continuous improvement and documentation are integral to accreditation.'},
                                   {'question': 'QC monitors?',
                                    'options': ['A) Method performance over time',
                                                'B) Only staff birthdays',
                                                'C) Only paint color',
                                                'D) Only lunch breaks'],
                                    'answer': 'A) Method performance over time',
                                    'explanation': 'Quality control (QC) uses materials of known target values to monitor analytic method stability over time. Results are plotted on Levey–Jennings charts and evaluated against means and standard deviations. Shifts and trends signal systematic error before patient results are compromised.'},
                                   {'question': 'SOP stands for?',
                                    'options': ['A) Standard operating procedure',
                                                'B) Special optional print',
                                                'C) Serum only processing',
                                                'D) Shift overtime pay'],
                                    'answer': 'A) Standard operating procedure',
                                    'explanation': 'A standard operating procedure (SOP) is the controlled written instruction detailing how a method or process is performed. Staff must follow the current approved SOP to ensure consistency, safety, and regulatory compliance. Unauthorized deviations undermine result quality and traceability.'}],
                          'medium': [{'question': 'Westgard rules help detect?',
                                      'options': ['A) Random/systematic error patterns',
                                                  'B) Only staffing needs',
                                                  'C) Only inventory of gloves',
                                                  'D) Only temperature of break room'],
                                      'answer': 'A) Random/systematic error patterns',
                                      'explanation': 'Westgard multirule QC applies combinations of control rules (for example 1₃ₛ, 2₂ₛ, R₄ₛ) to distinguish random from systematic error. Rule violations trigger investigation, corrective action, and assessment of whether patient results were affected. Multirule strategies improve error detection while limiting false rejections.'},
                                     {'question': 'Proficiency testing evaluates?',
                                      'options': ['A) Laboratory accuracy vs external unknowns',
                                                  'B) Only typing speed',
                                                  'C) Only parking skills',
                                                  'D) Only phone etiquette'],
                                      'answer': 'A) Laboratory accuracy vs external unknowns',
                                      'explanation': 'Proficiency testing (PT) submits blinded external specimens for analysis and compares laboratory results with peer or reference targets. Successful PT demonstrates ongoing accuracy and is required for accreditation and licensure of tested analytes. Failures mandate investigation and corrective action.'},
                                     {'question': 'Critical results require?',
                                      'options': ['A) Timely notification and '
                                                  'read-back/documentation',
                                                  'B) Batching next month',
                                                  'C) No records',
                                                  'D) Texting only the patient'],
                                      'answer': 'A) Timely notification and '
                                                'read-back/documentation',
                                      'explanation': 'Critical results are laboratory values that indicate potentially life-threatening conditions and require immediate clinician notification. Policies specify time frames, acceptable recipients, read-back confirmation, and documentation. Reliable critical reporting is a fundamental patient-safety practice.'}],
                          'hard': [{'question': 'A junior colleague asks for the single best '
                                                'answer. Root cause analysis after error aims to? '
                                                'Beware of near-miss distractors.',
                                    'options': ['A) Fix system causes not only blame individuals',
                                                'B) Punish only and stop',
                                                'C) Hide the event',
                                                'D) Change result without review'],
                                    'answer': 'A) Fix system causes not only blame individuals',
                                    'explanation': 'Root cause analysis after a laboratory error investigates underlying system failures such as process design, training gaps, or interface problems rather than stopping at individual blame. Corrective and preventive actions address those systemic causes to reduce recurrence. Just culture balances accountability with learning.'},
                                   {'question': 'A junior colleague asks for the single best '
                                                'answer. Document control ensures? Beware of '
                                                'near-miss distractors.',
                                    'options': ['A) Only current approved SOPs in use',
                                                'B) Mixed obsolete versions everywhere',
                                                'C) No version numbers',
                                                'D) Sticky notes replace SOPs'],
                                    'answer': 'A) Only current approved SOPs in use',
                                    'explanation': 'Document control ensures that only the current, approved version of each SOP, form, and policy is available at the point of use. Obsolete documents are removed or marked to prevent unintended use. Controlled documentation is a requirement of ISO 15189 and CAP laboratory standards.'},
                                   {'question': 'A junior colleague asks for the single best '
                                                'answer. Risk management in labs includes? Beware '
                                                'of near-miss distractors.',
                                    'options': ['A) Identifying failure modes and mitigations',
                                                'B) Ignoring near misses',
                                                'C) No incident reports',
                                                'D) Skipping training'],
                                    'answer': 'A) Identifying failure modes and mitigations',
                                    'explanation': 'Laboratory risk management systematically identifies potential failure modes across testing pathways and implements mitigations proportional to severity and likelihood. Tools may include process mapping and failure mode and effects analysis (FMEA). Proactive risk reduction complements reactive incident review.'}],
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
                                       'explanation': 'Accreditation nonconformances require documented corrective and preventive action (CAPA) with evidence that the fix is effective. Simply acknowledging a citation without follow-through leaves patients at continued risk. Closing the loop with verification completes the quality-management response.'},
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
                                       'explanation': 'Laboratory information system (LIS) downtime procedures provide validated manual workflows for order entry, specimen identification, result recording, and reporting. Maintaining positive patient identification during downtime prevents mislabeled results. Business continuity plans are tested so care continues safely when electronic systems fail.'},
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
                                       'explanation': 'Altering quality-control data to force a method to “pass” is scientific misconduct and endangers patients by concealing analytic failure. Ethical practice requires honest QC review, stopping testing when controls fail, and reporting integrity concerns through proper channels. Professional codes of conduct prohibit falsification of laboratory records.'}]},
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
                                        'explanation': 'Urine dipstick “blood” reagents detect heme’s peroxidase-like activity and therefore react with intact red cells, free hemoglobin, and myoglobin. Microscopic examination distinguishes hematuria (RBCs present) from hemoglobinuria or myoglobinuria (few or no RBCs). Clinical context and plasma appearance further refine the interpretation.'},
                                       {'question': 'Specific gravity estimates?',
                                        'options': ['A) Urine concentration',
                                                    'B) Only color preference',
                                                    'C) Only odor',
                                                    'D) Only volume alone without concentration'],
                                        'answer': 'A) Urine concentration',
                                        'explanation': 'Urine specific gravity estimates the density of urine relative to water and reflects renal concentrating and diluting ability. Values rise with dehydration or glycosuria and fall with water diuresis or concentrating defects. It is a routine urinalysis parameter alongside chemical and microscopic findings.'},
                                       {'question': 'CSF tube order typically?',
                                        'options': ['A) Chemistry/micro/heme allocations per '
                                                    'protocol',
                                                    'B) Random any order always fine',
                                                    'C) Only one tube ever allowed worldwide',
                                                    'D) No labeling'],
                                        'answer': 'A) Chemistry/micro/heme allocations per '
                                                  'protocol',
                                        'explanation': 'CSF is typically collected into sequentially numbered tubes allocated to chemistry, microbiology, and hematology per institutional protocol. Splitting specimens this way reduces contamination of culture tubes and preserves appropriate aliquots for each test. Local SOPs define exact tube order and volumes.'}],
                              'medium': [{'question': 'RBC casts suggest?',
                                          'options': ['A) Glomerular disease',
                                                      'B) Always contamination only',
                                                      'C) Only lower UTI exclusively',
                                                      'D) Only crystals only'],
                                          'answer': 'A) Glomerular disease',
                                          'explanation': 'Red blood cell casts form when RBCs are embedded in Tamm–Horsfall protein within renal tubules and indicate glomerular bleeding. Their presence supports glomerulonephritis rather than lower-urinary-tract hematuria. Careful bright-field or phase-contrast microscopy is required for reliable cast identification.'},
                                         {'question': 'Oval fat bodies associate with?',
                                          'options': ['A) Nephrotic syndrome themes',
                                                      'B) Only diabetes insipidus only',
                                                      'C) Only dehydration only',
                                                      'D) Only contamination ink'],
                                          'answer': 'A) Nephrotic syndrome themes',
                                          'explanation': 'Oval fat bodies are renal tubular epithelial cells or macrophages laden with lipid, classically associated with heavy proteinuria of nephrotic syndrome. Under polarized light, cholesterol droplets may show Maltese-cross birefringence. Lipiduria complements hypoalbuminemia and edema in the nephrotic presentation.'},
                                         {'question': 'Synovial fluid crystals: needle strongly '
                                                      'birefringent negative?',
                                          'options': ['A) Monosodium urate (gout) themes',
                                                      'B) Always CPPD exclusively',
                                                      'C) Always cholesterol only',
                                                      'D) Always starch'],
                                          'answer': 'A) Monosodium urate (gout) themes',
                                          'explanation': 'Monosodium urate crystals of gout are needle-shaped and show strong negative birefringence under compensated polarized light (yellow when aligned with the compensator axis). Calcium pyrophosphate crystals of pseudogout are rhomboid or rod-shaped with weak positive birefringence. Crystal identification in synovial fluid confirms crystal arthropathy.'}],
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
                                        'explanation': 'Xanthochromia is yellowish CSF discoloration from bilirubin formed in situ after subarachnoid hemorrhage, appearing hours after bleeding. Visual inspection can be subjective; spectrophotometry for bilirubin improves detection and helps exclude oxyhemoglobin from traumatic tap artifact. Timing of lumbar puncture relative to symptom onset affects sensitivity.'},
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
                                        'explanation': 'Dipstick blood pads cannot distinguish myoglobin from hemoglobin because both possess heme groups that catalyze the indicator reaction. Myoglobinuria typically accompanies clear plasma and marked muscle injury with elevated CK, whereas hemolysis often shows pink plasma and reduced haptoglobin. Microscopy and clinical chemistry resolve the differential.'},
                                       {'question': 'A junior colleague asks for the single best '
                                                    'answer. Transudate vs exudate uses? Beware of '
                                                    'near-miss distractors.',
                                        'options': ["A) Light's criteria themes for pleural fluid",
                                                    'B) Only color forever',
                                                    'C) Only patient age',
                                                    'D) Only tube number'],
                                        'answer': "A) Light's criteria themes for pleural fluid",
                                        'explanation': 'Light’s criteria compare pleural fluid and serum protein and LDH to classify effusions as exudates or transudates. Exudates meet thresholds suggesting inflammation, infection, or malignancy; transudates reflect hydrostatic or oncotic imbalances such as heart failure. Accurate classification requires paired fluid and serum chemistry measured by validated methods.'}],
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
                                           'explanation': 'Automated body-fluid cell counts require method validation for each fluid type because matrices differ from blood. Smear review remains necessary to detect malignant cells, crystals, or misclassified debris that analyzers may miss or miscount. Morphology complements numeric counts for clinically critical fluids.'},
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
                                           'explanation': 'Critical CSF findings—such as organisms on Gram stain, marked neutrophilic pleocytosis, or xanthochromia suggestive of SAH—require immediate clinician notification. Delays can worsen outcomes in bacterial meningitis and intracranial hemorrhage. Laboratories maintain defined critical lists and escalation pathways for CSF.'},
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
                                           'explanation': 'Clean-catch midstream urine contaminated by periurethral flora often shows abundant squamous epithelial cells and mixed bacterial morphologies without a dominant uropathogen. Such findings suggest poor collection technique rather than true UTI. Patient recollection with proper instructions improves culture interpretability.'}]},
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
