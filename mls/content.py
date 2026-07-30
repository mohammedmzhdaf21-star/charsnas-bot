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
                                                    'B) About 8–10 g/dL (lab-dependent)',
                                                    'C) About 18–22 g/dL (lab-dependent)',
                                                    'D) About 5–7 g/dL (lab-dependent)'],
                                        'answer': 'A) About 13–17 g/dL (lab-dependent)',
                                        'explanation': 'Adult male hemoglobin reference intervals '
                                                       'are typically about 13–17 g/dL, though '
                                                       'exact cutoffs vary by laboratory, '
                                                       'altitude, and method. Hemoglobin '
                                                       'concentration reflects circulating '
                                                       'oxygen-carrying capacity and is '
                                                       'interpreted with hematocrit and red-cell '
                                                       'indices. Sex- and age-specific intervals '
                                                       'from the reporting laboratory define the '
                                                       'interpretive reference.'},
                                       {'question': 'CBC primarily measures?',
                                        'options': ['A) Plasma electrolyte concentrations',
                                                    'B) Blood cell counts and indices',
                                                    'C) Coagulation factor activities',
                                                    'D) Arterial blood gas tensions'],
                                        'answer': 'B) Blood cell counts and indices',
                                        'explanation': 'A complete blood count (CBC) quantifies '
                                                       'leukocytes, erythrocytes, and platelets '
                                                       'and reports red-cell indices such as MCV, '
                                                       'MCH, and MCHC. Automated analyzers also '
                                                       'provide leukocyte differentials and flags '
                                                       'that prompt smear review. The CBC is the '
                                                       'foundational screening test in hematology '
                                                       'for anemia, infection, and cytopenias.'},
                                       {'question': 'Anemia means?',
                                        'options': ['A) Elevated leukocyte count for age/sex',
                                                    'B) Elevated platelet count for age/sex',
                                                    'C) Low hemoglobin/RBC mass for age/sex',
                                                    'D) Elevated hematocrit with normal '
                                                    'hemoglobin'],
                                        'answer': 'C) Low hemoglobin/RBC mass for age/sex',
                                        'explanation': 'Anemia is a reduction in hemoglobin '
                                                       'concentration or red-cell mass below the '
                                                       'reference interval for age and sex. It may '
                                                       'result from decreased production, '
                                                       'increased destruction, or blood loss. '
                                                       'Morphologic (MCV-based) and kinetic '
                                                       'approaches guide the subsequent laboratory '
                                                       'workup.'}],
                              'medium': [{'question': 'Schistocytes suggest?',
                                          'options': ['A) Iron-deficiency anemia with pencil cells',
                                                      'B) Megaloblastic anemia with '
                                                      'macro-ovalocytes',
                                                      'C) Hereditary spherocytosis with dense '
                                                      'spherocytes',
                                                      'D) Microangiopathic hemolysis'],
                                          'answer': 'D) Microangiopathic hemolysis',
                                          'explanation': 'Schistocytes are fragmented red cells '
                                                         'formed when erythrocytes are sheared by '
                                                         'fibrin strands or abnormal vasculature. '
                                                         'Their presence supports microangiopathic '
                                                         'hemolytic anemia (MAHA), as seen in TTP, '
                                                         'HUS, DIC, and mechanical valve injury. '
                                                         'Correlation with LDH, haptoglobin, '
                                                         'bilirubin, and platelet count refines '
                                                         'the differential.'},
                                         {'question': 'Left shift means?',
                                          'options': ['A) Increased immature neutrophils',
                                                      'B) Increased absolute lymphocytosis',
                                                      'C) Increased absolute eosinophilia',
                                                      'D) Increased absolute basophilia'],
                                          'answer': 'A) Increased immature neutrophils',
                                          'explanation': 'A left shift denotes increased '
                                                         'circulating immature neutrophils such as '
                                                         'bands and earlier myeloid forms. It '
                                                         'commonly accompanies acute bacterial '
                                                         'infection, inflammation, or physiologic '
                                                         'stress with accelerated marrow release. '
                                                         'Marked left shift with dysplasia or '
                                                         'blasts requires morphologic review to '
                                                         'exclude myeloid malignancy.'},
                                         {'question': 'INR monitors?',
                                          'options': ['A) Unfractionated heparin via anti-Xa assay',
                                                      'B) Warfarin therapy (extrinsic/common '
                                                      'pathway)',
                                                      'C) Primary hemostasis via bleeding time',
                                                      'D) Fibrinolysis via D-dimer alone'],
                                          'answer': 'B) Warfarin therapy (extrinsic/common '
                                                    'pathway)',
                                          'explanation': 'The international normalized ratio (INR) '
                                                         'standardizes the prothrombin time (PT) '
                                                         'across thromboplastin reagents. PT/INR '
                                                         'primarily assesses the extrinsic and '
                                                         'common coagulation pathways and is used '
                                                         'to monitor vitamin K antagonist '
                                                         '(warfarin) therapy. Results are '
                                                         'interpreted with the therapeutic target '
                                                         'appropriate to the clinical '
                                                         'indication.'}],
                              'hard': [{'question': 'PNH relates to?',
                                        'options': ['A) Extrinsic hemolysis from warm IgG '
                                                    'autoimmune antibody',
                                                    'B) Intrinsic hemolysis from spectrin '
                                                    'cytoskeleton defect',
                                                    'C) Complement-mediated hemolysis due to '
                                                    'GPI-anchor defect',
                                                    'D) Sequestration hemolysis from hypersplenism '
                                                    'alone'],
                                        'answer': 'C) Complement-mediated hemolysis due to '
                                                  'GPI-anchor defect',
                                        'explanation': 'Paroxysmal nocturnal hemoglobinuria (PNH) '
                                                       'arises from acquired PIGA mutations that '
                                                       'impair GPI-anchor synthesis, depleting '
                                                       'complement-regulatory proteins CD55 and '
                                                       'CD59 on blood cells. Unopposed complement '
                                                       'activity produces intravascular hemolysis '
                                                       'and contributes to thrombosis risk. '
                                                       'High-sensitivity flow cytometry for '
                                                       'GPI-deficient clones is the diagnostic '
                                                       'method of choice.'},
                                       {'question': 'AML vs ALL distinction uses?',
                                        'options': ['A) Patient age alone without lineage studies',
                                                    'B) Hemoglobin value alone without blast '
                                                    'markers',
                                                    'C) Platelet count alone without '
                                                    'immunophenotype',
                                                    'D) Morphology + '
                                                    'cytochemistry/immunophenotype/genetics'],
                                        'answer': 'D) Morphology + '
                                                  'cytochemistry/immunophenotype/genetics',
                                        'explanation': 'Acute myeloid leukemia (AML) and acute '
                                                       'lymphoblastic leukemia (ALL) cannot be '
                                                       'reliably separated by age or blood counts '
                                                       'alone. Distinction relies on blast '
                                                       'morphology, cytochemistry when used, '
                                                       'multiparameter immunophenotyping, and '
                                                       'genetic/cytogenetic findings under WHO/ICC '
                                                       'frameworks. Accurate lineage assignment '
                                                       'directs induction therapy and risk '
                                                       'stratification.'},
                                       {'question': 'HIT is?',
                                        'options': ['A) Heparin-induced thrombocytopenia — immune, '
                                                    'thrombosis risk',
                                                    'B) EDTA-dependent platelet clumping '
                                                    'pseudothrombocytopenia',
                                                    'C) Heparin-associated nonimmune platelet '
                                                    'sequestration',
                                                    'D) Drug-induced marrow suppression without '
                                                    'thrombosis risk'],
                                        'answer': 'A) Heparin-induced thrombocytopenia — immune, '
                                                  'thrombosis risk',
                                        'explanation': 'Heparin-induced thrombocytopenia (HIT) is '
                                                       'an immune-mediated disorder in which '
                                                       'antibodies against platelet factor '
                                                       '4–heparin complexes activate platelets. '
                                                       'Paradoxically, patients develop '
                                                       'thrombocytopenia with a high risk of '
                                                       'arterial and venous thrombosis. Laboratory '
                                                       'evaluation may include immunoassay and '
                                                       'functional assays, and heparin must be '
                                                       'discontinued with alternative '
                                                       'anticoagulation.'}],
                              'extreme': [{'question': 'APML emergency risk?',
                                           'options': ['A) Isolated iron deficiency without '
                                                       'coagulopathy',
                                                       'B) DIC/bleeding — urgent ATRA pathway',
                                                       'C) Hyperviscosity from extreme '
                                                       'leukocytosis alone',
                                                       'D) Tumor lysis without coagulopathy '
                                                       'concern'],
                                           'answer': 'B) DIC/bleeding — urgent ATRA pathway',
                                           'explanation': 'Acute promyelocytic leukemia (APML/APL) '
                                                          'is driven by PML::RARA and '
                                                          'characteristically presents with '
                                                          'coagulopathy and DIC-related bleeding. '
                                                          'Early recognition of abnormal '
                                                          'promyelocytes, often with Auer rods, '
                                                          'warrants urgent initiation of all-trans '
                                                          'retinoic acid (ATRA)–based therapy. '
                                                          'Delayed treatment markedly increases '
                                                          'early hemorrhagic mortality.'},
                                          {'question': 'TTP pentad classic teaching includes?',
                                           'options': ['A) Isolated neutropenia with normal smear '
                                                       'and platelets',
                                                       'B) Polycythemia with thrombocytosis and '
                                                       'leukocytosis',
                                                       'C) MAHA, thrombocytopenia, neurologic '
                                                       'change (± renal/fever)',
                                                       'D) Eosinophilia with pulmonary infiltrates '
                                                       'alone'],
                                           'answer': 'C) MAHA, thrombocytopenia, neurologic change '
                                                     '(± renal/fever)',
                                           'explanation': 'Thrombotic thrombocytopenic purpura '
                                                          '(TTP) classically features '
                                                          'microangiopathic hemolytic anemia and '
                                                          'thrombocytopenia, often with neurologic '
                                                          'findings; fever and renal involvement '
                                                          'may occur. Severe ADAMTS13 deficiency '
                                                          'allows uncleaved ultra-large von '
                                                          'Willebrand multimers to drive platelet '
                                                          'microthrombi. Prompt plasma exchange is '
                                                          'disease-modifying therapy.'},
                                          {'question': 'Flow cytometry MRD aims to?',
                                           'options': ['A) Replace coagulation monitoring after '
                                                       'induction',
                                                       'B) Quantify plasma glucose during steroid '
                                                       'therapy',
                                                       'C) Determine ABO/Rh type before '
                                                       'transfusion',
                                                       'D) Detect residual disease below '
                                                       'morphology threshold'],
                                           'answer': 'D) Detect residual disease below morphology '
                                                     'threshold',
                                           'explanation': 'Minimal residual disease (MRD) '
                                                          'assessment by multiparameter flow '
                                                          'cytometry detects leukemic cells below '
                                                          'the threshold of morphologic remission. '
                                                          'Sensitive MRD monitoring informs '
                                                          'treatment response, risk '
                                                          'stratification, and need for therapy '
                                                          'intensification. Assay design requires '
                                                          'disease-specific antigen aberrant '
                                                          'phenotypes and validated sensitivity '
                                                          'limits.'}]},
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
                                                'options': ['A) Na, K, Cl, and bicarbonate (total '
                                                            'CO2)',
                                                            'B) HbA1c and fructosamine only',
                                                            'C) CBC indices without chemistry '
                                                            'analytes',
                                                            'D) PT/INR without electrolyte '
                                                            'measurement'],
                                                'answer': 'A) Na, K, Cl, and bicarbonate (total '
                                                          'CO2)',
                                                'explanation': 'A routine electrolyte panel '
                                                               'typically measures sodium, '
                                                               'potassium, chloride, and '
                                                               'bicarbonate (total CO2), '
                                                               'reflecting extracellular fluid '
                                                               'composition and acid–base balance. '
                                                               'These analytes are central to '
                                                               'evaluating dehydration, renal '
                                                               'disorders, and metabolic '
                                                               'disturbances. Interpretation '
                                                               'requires awareness of preanalytic '
                                                               'factors such as hemolysis '
                                                               'affecting potassium.'},
                                               {'question': 'Creatinine mainly reflects?',
                                                'options': ['A) Hepatic synthetic function '
                                                            '(albumin/INR)',
                                                            'B) Glomerular filtration (with '
                                                            'muscle-mass caveats)',
                                                            'C) Skeletal muscle enzyme leakage '
                                                            '(CK)',
                                                            'D) Pancreatic amylase secretory '
                                                            'capacity'],
                                                'answer': 'B) Glomerular filtration (with '
                                                          'muscle-mass caveats)',
                                                'explanation': 'Serum creatinine is produced from '
                                                               'muscle creatine metabolism and is '
                                                               'cleared primarily by glomerular '
                                                               'filtration. Rising creatinine '
                                                               'generally indicates reduced '
                                                               'glomerular filtration rate, though '
                                                               'levels also depend on muscle mass, '
                                                               'age, sex, and some drugs. '
                                                               'Estimated GFR equations convert '
                                                               'creatinine into a more '
                                                               'physiologically interpretable '
                                                               'filtration index.'},
                                               {'question': 'Hypoglycemia means?',
                                                'options': ['A) Abnormally high blood glucose',
                                                            'B) Isolated ketonemia with normal '
                                                            'glucose',
                                                            'C) Abnormally low blood glucose',
                                                            'D) Elevated hemoglobin without '
                                                            'glucose change'],
                                                'answer': 'C) Abnormally low blood glucose',
                                                'explanation': 'Hypoglycemia denotes abnormally '
                                                               'low plasma glucose and can cause '
                                                               'neuroglycopenic and autonomic '
                                                               'symptoms. Critical hypoglycemia is '
                                                               'a medical emergency requiring '
                                                               'rapid confirmation and treatment. '
                                                               'Laboratory practice includes '
                                                               'critical-value notification and '
                                                               'investigation of causes ranging '
                                                               'from insulin excess to hepatic '
                                                               'failure and adrenal '
                                                               'insufficiency.'}],
                                      'medium': [{'question': 'AST/ALT pattern helps assess?',
                                                  'options': ['A) Osteoblastic bone turnover alone',
                                                              'B) Intravascular hemolysis alone',
                                                              'C) Primary thyroid dysfunction '
                                                              'alone',
                                                              'D) Hepatocellular injury'],
                                                  'answer': 'D) Hepatocellular injury',
                                                  'explanation': 'Aspartate and alanine '
                                                                 'aminotransferases (AST and ALT) '
                                                                 'are cytosolic enzymes released '
                                                                 'with hepatocyte injury. '
                                                                 'Elevations with an '
                                                                 'hepatocellular pattern support '
                                                                 'hepatitis, ischemic injury, or '
                                                                 'toxin-mediated damage. In '
                                                                 'contrast, ALP and GGT elevations '
                                                                 'more often reflect cholestasis '
                                                                 'or biliary obstruction.'},
                                                 {'question': 'Troponin rise suggests?',
                                                  'options': ['A) Myocardial injury',
                                                              'B) Uncomplicated lower UTI',
                                                              'C) Iron-deficiency anemia alone',
                                                              'D) Stable chronic kidney disease '
                                                              'without injury'],
                                                  'answer': 'A) Myocardial injury',
                                                  'explanation': 'Cardiac troponins I and T are '
                                                                 'regulatory proteins released '
                                                                 'into blood after cardiomyocyte '
                                                                 'necrosis or injury. Serial rises '
                                                                 'and/or falls above the '
                                                                 'assay-specific 99th percentile '
                                                                 'support myocardial injury and, '
                                                                 'with clinical criteria, acute '
                                                                 'myocardial infarction. '
                                                                 'High-sensitivity assays detect '
                                                                 'earlier and smaller elevations '
                                                                 'but require clinical '
                                                                 'correlation.'},
                                                 {'question': 'HbA1c reflects?',
                                                  'options': ['A) A single fasting glucose '
                                                              'measurement',
                                                              'B) Average glycemia over ~2–3 '
                                                              'months',
                                                              'C) Urine glucose excretion at '
                                                              'collection',
                                                              'D) Immediate postprandial insulin '
                                                              'dose'],
                                                  'answer': 'B) Average glycemia over ~2–3 months',
                                                  'explanation': 'Hemoglobin A1c forms by '
                                                                 'nonenzymatic glycation of '
                                                                 'hemoglobin and reflects average '
                                                                 'glycemia over approximately the '
                                                                 'preceding 2–3 months, '
                                                                 'corresponding to erythrocyte '
                                                                 'lifespan. It is used for '
                                                                 'diabetes diagnosis and long-term '
                                                                 'glycemic monitoring when '
                                                                 'conditions affecting red-cell '
                                                                 'turnover are absent. '
                                                                 'Method-specific NGSP/IFCC '
                                                                 'standardization underpins '
                                                                 'comparability.'}],
                                      'hard': [{'question': 'Osmolal gap increases with?',
                                                'options': ['A) Isotonic saline infusion without '
                                                            'osmoles added',
                                                            'B) Supplemental oxygen without solute '
                                                            'change',
                                                            'C) Unmeasured osmotically active '
                                                            'solutes (e.g., toxic alcohols)',
                                                            'D) Water-soluble vitamin intake '
                                                            'alone'],
                                                'answer': 'C) Unmeasured osmotically active '
                                                          'solutes (e.g., toxic alcohols)',
                                                'explanation': 'The osmolal gap is the difference '
                                                               'between measured serum osmolality '
                                                               'and osmolality calculated from '
                                                               'sodium, glucose, and urea. An '
                                                               'elevated gap suggests unmeasured '
                                                               'osmotically active solutes such as '
                                                               'methanol, ethylene glycol, or '
                                                               'isopropanol. Toxic-alcohol '
                                                               'evaluation pairs the gap with '
                                                               'anion gap, blood gases, and '
                                                               'specific analyte assays.'},
                                               {'question': 'Hook effect can cause?',
                                                'options': ['A) Falsely high results from reagent '
                                                            'underloading',
                                                            'B) Specimen hemolysis altering tube '
                                                            'color only',
                                                            'C) Barcode misreads without '
                                                            'concentration error',
                                                            'D) Falsely low immunoassay results at '
                                                            'very high analyte'],
                                                'answer': 'D) Falsely low immunoassay results at '
                                                          'very high analyte',
                                                'explanation': 'The high-dose hook (prozone-like) '
                                                               'effect in sandwich immunoassays '
                                                               'occurs when extremely high antigen '
                                                               'concentrations saturate capture '
                                                               'and detection antibodies, '
                                                               'preventing sandwich formation. The '
                                                               'reported result can be falsely low '
                                                               'or normal despite massive analyte '
                                                               'excess. Dilution of the specimen '
                                                               'restores linearity and reveals the '
                                                               'true high concentration.'},
                                               {'question': 'Pseudohyponatremia classic with?',
                                                'options': ['A) Severe '
                                                            'hyperlipidemia/hyperproteinemia '
                                                            '(indirect ISE)',
                                                            'B) True hypotonic hyponatremia from '
                                                            'SIADH alone',
                                                            'C) Hypertonic hyponatremia from '
                                                            'hyperglycemia alone',
                                                            'D) Hypovolemic hyponatremia from GI '
                                                            'losses alone'],
                                                'answer': 'A) Severe '
                                                          'hyperlipidemia/hyperproteinemia '
                                                          '(indirect ISE)',
                                                'explanation': 'Pseudohyponatremia is an '
                                                               'artifactual low sodium reported by '
                                                               'indirect potentiometry when marked '
                                                               'hyperlipidemia or hyperproteinemia '
                                                               'expands the non-aqueous plasma '
                                                               'fraction. Direct ion-selective '
                                                               'electrode methods that measure '
                                                               'activity in the undiluted aqueous '
                                                               'phase are largely unaffected. '
                                                               'Recognizing method dependence '
                                                               'prevents inappropriate hypotonic '
                                                               'fluid therapy.'}],
                                      'extreme': [{'question': 'Critical value policy requires?',
                                                   'options': ['A) Batch filing of alerts at '
                                                               'weekly review',
                                                               'B) Rapid clinician notification '
                                                               'and documentation',
                                                               'C) Release without repeat or '
                                                               'verification steps',
                                                               'D) Direct patient email without '
                                                               'clinician contact'],
                                                   'answer': 'B) Rapid clinician notification and '
                                                             'documentation',
                                                   'explanation': 'Critical laboratory values '
                                                                  'identify results that may '
                                                                  'indicate life-threatening '
                                                                  'conditions requiring immediate '
                                                                  'clinical action. Laboratory '
                                                                  'policy mandates rapid clinician '
                                                                  'notification, read-back '
                                                                  'verification, and documentation '
                                                                  'of the communication. Timely '
                                                                  'reporting is a core '
                                                                  'patient-safety and '
                                                                  'accreditation requirement.'},
                                                  {'question': 'Delta check flags?',
                                                   'options': ['A) New patient registration '
                                                               'without prior values',
                                                               'B) Preferred collection-tube color '
                                                               'mismatch',
                                                               'C) Implausible change versus prior '
                                                               'patient results',
                                                               'D) Printer or label-stock hardware '
                                                               'faults'],
                                                   'answer': 'C) Implausible change versus prior '
                                                             'patient results',
                                                   'explanation': 'Delta checks compare a current '
                                                                  'result with a patient’s recent '
                                                                  'prior values to detect '
                                                                  'implausible analytic or '
                                                                  'identity errors. Large '
                                                                  'unexpected changes may indicate '
                                                                  'specimen mix-up, IV '
                                                                  'contamination, or instrument '
                                                                  'malfunction rather than true '
                                                                  'physiology. Investigation '
                                                                  'before release protects against '
                                                                  'reporting erroneous results.'},
                                                  {'question': 'Blood gas preanalytics: air '
                                                               'bubbles cause?',
                                                   'options': ['A) Improved accuracy by ambient '
                                                               'equilibration',
                                                               'B) No measurable effect on '
                                                               'blood-gas values',
                                                               'C) Isolated glucose elevation '
                                                               'without gas change',
                                                               'D) Distorted pO2/pCO2 from gas '
                                                               'exchange'],
                                                   'answer': 'D) Distorted pO2/pCO2 from gas '
                                                             'exchange',
                                                   'explanation': 'Air bubbles in arterial '
                                                                  'blood-gas syringes allow gas '
                                                                  'exchange that can falsely raise '
                                                                  'pO2 toward ambient air and '
                                                                  'alter pCO2. Delayed analysis '
                                                                  'permits ongoing cellular '
                                                                  'metabolism that consumes oxygen '
                                                                  'and generates CO2. Specimens '
                                                                  'should be carefully debubbled, '
                                                                  'mixed, and analyzed promptly '
                                                                  'under anaerobic conditions.'}]},
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
                                                  'options': ['A) Purple/blue (retain crystal '
                                                              'violet)',
                                                              'B) Pink/red (take safranin '
                                                              'counterstain)',
                                                              'C) Colorless after decolorization '
                                                              'step',
                                                              'D) Acid-fast red without Gram '
                                                              'reagents'],
                                                  'answer': 'A) Purple/blue (retain crystal '
                                                            'violet)',
                                                  'explanation': 'Gram-positive bacteria retain '
                                                                 'crystal violet–iodine complex '
                                                                 'within a thick peptidoglycan '
                                                                 'cell wall and appear '
                                                                 'purple/blue. Gram-negative '
                                                                 'organisms lose the complex '
                                                                 'during decolorization and take '
                                                                 'up the pink/red counterstain. '
                                                                 'Correct interpretation requires '
                                                                 'properly made smears and '
                                                                 'controlled decolorization.'},
                                                 {'question': 'Blood culture indication theme?',
                                                  'options': ['A) Routine wellness screening '
                                                              'without fever',
                                                              'B) Suspected bacteremia/sepsis',
                                                              'C) Isolated asymptomatic '
                                                              'bacteriuria workup',
                                                              'D) Surveillance of environmental '
                                                              'surfaces'],
                                                  'answer': 'B) Suspected bacteremia/sepsis',
                                                  'explanation': 'Blood cultures are indicated '
                                                                 'when bacteremia or sepsis is '
                                                                 'suspected clinically. Adequate '
                                                                 'blood volume per bottle and '
                                                                 'collection of multiple sets '
                                                                 'before antibiotics maximize '
                                                                 'recovery. Timing, skin '
                                                                 'antisepsis, and bottle fill '
                                                                 'volume critically affect '
                                                                 'sensitivity and contamination '
                                                                 'rates.'},
                                                 {'question': 'Antibiotic susceptibility testing '
                                                              'guides?',
                                                  'options': ['A) Species identification without '
                                                              'MIC data',
                                                              'B) Only infection-control isolation '
                                                              'decisions',
                                                              'C) Antimicrobial therapy selection',
                                                              'D) Only vaccine schedule '
                                                              'recommendations'],
                                                  'answer': 'C) Antimicrobial therapy selection',
                                                  'explanation': 'Antimicrobial susceptibility '
                                                                 'testing determines whether an '
                                                                 'isolate is inhibited by '
                                                                 'achievable drug concentrations. '
                                                                 'Interpreted breakpoints '
                                                                 '(CLSI/EUCAST) categorize '
                                                                 'isolates as susceptible, '
                                                                 'intermediate, or resistant to '
                                                                 'guide therapy. Results must be '
                                                                 'linked to correct organism '
                                                                 'identification and clinical site '
                                                                 'of infection.'}],
                                        'medium': [{'question': 'Acid-fast stain used for?',
                                                    'options': ['A) Routine Enterobacterales Gram '
                                                                'morphology',
                                                                'B) Fungal hyphae on KOH '
                                                                'preparation',
                                                                'C) Parasitic ova on saline wet '
                                                                'mount',
                                                                'D) Mycobacteria (mycolic '
                                                                'acid–rich walls)'],
                                                    'answer': 'D) Mycobacteria (mycolic acid–rich '
                                                              'walls)',
                                                    'explanation': 'Acid-fast stains such as '
                                                                   'Ziehl–Neelsen or fluorochrome '
                                                                   'auramine exploit mycolic '
                                                                   'acid–rich cell walls that '
                                                                   'resist acid-alcohol '
                                                                   'decolorization, highlighting '
                                                                   'mycobacteria. Partial '
                                                                   'acid-fastness also aids '
                                                                   'detection of Nocardia and some '
                                                                   'coccidia. Results are '
                                                                   'correlated with culture and '
                                                                   'molecular assays.'},
                                                   {'question': 'Catalase-positive gram-positive '
                                                                'cocci suggest?',
                                                    'options': ['A) Staphylococci',
                                                                'B) Streptococci '
                                                                '(catalase-negative)',
                                                                'C) Enterococci '
                                                                '(catalase-negative)',
                                                                'D) Lactobacilli '
                                                                '(catalase-negative rods)'],
                                                    'answer': 'A) Staphylococci',
                                                    'explanation': 'Catalase decomposes hydrogen '
                                                                   'peroxide to water and oxygen; '
                                                                   'bubbling indicates a positive '
                                                                   'reaction. Among gram-positive '
                                                                   'cocci, staphylococci are '
                                                                   'catalase-positive whereas '
                                                                   'streptococci and enterococci '
                                                                   'are catalase-negative. Further '
                                                                   'tests (coagulase, MALDI-TOF) '
                                                                   'refine species '
                                                                   'identification.'},
                                                   {'question': 'CSF Gram stain urgency?',
                                                    'options': ['A) Low priority elective '
                                                                'outpatient screen',
                                                                'B) Critical for suspected '
                                                                'bacterial meningitis',
                                                                'C) Useful only after 72-hour '
                                                                'culture growth',
                                                                'D) Replaced entirely by chemistry '
                                                                'panels'],
                                                    'answer': 'B) Critical for suspected bacterial '
                                                              'meningitis',
                                                    'explanation': 'CSF Gram stain is a '
                                                                   'time-critical test in '
                                                                   'suspected bacterial meningitis '
                                                                   'because early morphologic '
                                                                   'clues can guide empiric '
                                                                   'therapy. Rapid reporting of '
                                                                   'organisms and leukocytes '
                                                                   'supports antimicrobial and '
                                                                   'infection-control decisions. '
                                                                   'Negative stains do not exclude '
                                                                   'infection when clinical '
                                                                   'suspicion remains high.'}],
                                        'hard': [{'question': 'MRSA detected by?',
                                                  'options': ['A) Penicillin disk testing alone '
                                                              'without cefoxitin',
                                                              'B) Macrolike D-test alone without '
                                                              'oxacillin screen',
                                                              'C) Oxacillin/cefoxitin testing '
                                                              'and/or mecA detection',
                                                              'D) Aminoglycoside synergy screen '
                                                              'alone'],
                                                  'answer': 'C) Oxacillin/cefoxitin testing and/or '
                                                            'mecA detection',
                                                  'explanation': 'Methicillin-resistant '
                                                                 'Staphylococcus aureus (MRSA) '
                                                                 'harbors mecA (or mecC), encoding '
                                                                 'altered penicillin-binding '
                                                                 'protein PBP2a. Cefoxitin disk or '
                                                                 'MIC testing and molecular mecA '
                                                                 'assays are preferred '
                                                                 'phenotypic/genotypic detectors. '
                                                                 'Accurate MRSA recognition drives '
                                                                 'therapy and infection-control '
                                                                 'precautions.'},
                                                 {'question': 'Anaerobic culture needs?',
                                                  'options': ['A) Ambient-air swabs held overnight '
                                                              'unsealed',
                                                              'B) CO2 jar without anaerobic '
                                                              'indicator systems',
                                                              'C) Refrigeration of all anaerobe '
                                                              'specimens only',
                                                              'D) Oxygen-free transport and '
                                                              'incubation conditions'],
                                                  'answer': 'D) Oxygen-free transport and '
                                                            'incubation conditions',
                                                  'explanation': 'Obligate anaerobes are killed or '
                                                                 'inhibited by oxygen exposure '
                                                                 'during collection and transport. '
                                                                 'Successful anaerobic culture '
                                                                 'requires appropriate oxygen-free '
                                                                 'transport devices, prompt '
                                                                 'plating, and incubation in '
                                                                 'validated anaerobic atmospheres. '
                                                                 'Specimen quality and site '
                                                                 'selection are as important as '
                                                                 'media choice.'},
                                                 {'question': 'Blood culture contamination clues?',
                                                  'options': ['A) Common skin flora in only 1 of '
                                                              'multiple sets',
                                                              'B) Same pathogen in multiple sets '
                                                              'drawn apart',
                                                              'C) Growth of Enterobacterales in '
                                                              'all bottles rapidly',
                                                              'D) Candida in multiple sets from '
                                                              'central lines'],
                                                  'answer': 'A) Common skin flora in only 1 of '
                                                            'multiple sets',
                                                  'explanation': 'Blood-culture contaminants are '
                                                                 'often skin flora recovered from '
                                                                 'only one bottle or one set when '
                                                                 'multiple sets are drawn. True '
                                                                 'bacteremia more often yields the '
                                                                 'same organism in multiple sets '
                                                                 'with a compatible clinical '
                                                                 'picture. Distinguishing '
                                                                 'contamination prevents '
                                                                 'unnecessary antibiotics and '
                                                                 'workups.'}],
                                        'extreme': [{'question': 'Carbapenemase-producing '
                                                                 'Enterobacterales require?',
                                                     'options': ['A) Routine community AST without '
                                                                 'confirmatory assays',
                                                                 'B) Infection control plus '
                                                                 'specialized testing/stewardship',
                                                                 'C) Outpatient observation '
                                                                 'without isolation review',
                                                                 'D) Standard ampicillin therapy '
                                                                 'without resistance workup'],
                                                     'answer': 'B) Infection control plus '
                                                               'specialized testing/stewardship',
                                                     'explanation': 'Carbapenemase-producing '
                                                                    'Enterobacterales hydrolyze '
                                                                    'carbapenems and many other '
                                                                    'β-lactams, severely limiting '
                                                                    'therapeutic options. '
                                                                    'Detection triggers '
                                                                    'infection-control precautions '
                                                                    'and often specialized '
                                                                    'confirmatory tests and '
                                                                    'stewardship consultation. '
                                                                    'Misclassification risks both '
                                                                    'treatment failure and '
                                                                    'institutional spread.'},
                                                    {'question': 'Biosafety for Neisseria '
                                                                 'meningitidis work?',
                                                     'options': ['A) Open-bench sniffing of plate '
                                                                 'odors for ID',
                                                                 'B) BSL-1 practices without '
                                                                 'aerosol controls',
                                                                 'C) Appropriate BSL practices to '
                                                                 'protect staff',
                                                                 'D) No risk once colonies appear '
                                                                 'on solid media'],
                                                     'answer': 'C) Appropriate BSL practices to '
                                                               'protect staff',
                                                     'explanation': 'Neisseria meningitidis can '
                                                                    'cause severe '
                                                                    'laboratory-acquired infection '
                                                                    'through aerosol exposure '
                                                                    'during manipulation of '
                                                                    'cultures. Work with '
                                                                    'potentially infectious '
                                                                    'material requires appropriate '
                                                                    'biosafety level practices, '
                                                                    'PPE, and vaccination policies '
                                                                    'where indicated. Suspect '
                                                                    'isolates should be handled '
                                                                    'with heightened precautions.'},
                                                    {'question': 'MALDI-TOF identifies?',
                                                     'options': ['A) Antimicrobial MICs by '
                                                                 'spectral peak height',
                                                                 'B) Only viral loads from plasma '
                                                                 'protein spectra',
                                                                 'C) Only toxin genes without '
                                                                 'culture isolate',
                                                                 'D) Organisms by protein mass '
                                                                 'spectral fingerprints'],
                                                     'answer': 'D) Organisms by protein mass '
                                                               'spectral fingerprints',
                                                     'explanation': 'Matrix-assisted laser '
                                                                    'desorption/ionization '
                                                                    'time-of-flight (MALDI-TOF) '
                                                                    'mass spectrometry identifies '
                                                                    'microorganisms from '
                                                                    'characteristic protein mass '
                                                                    'spectra compared with '
                                                                    'reference libraries. It '
                                                                    'rapidly IDs many bacteria and '
                                                                    'yeasts from culture but does '
                                                                    'not replace susceptibility '
                                                                    'testing. Library coverage and '
                                                                    'extraction methods affect '
                                                                    'performance for some taxa.'}]},
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
                                                    'B) Blood-film morphologic differentials',
                                                    'C) Serum electrolyte concentrations',
                                                    'D) Urine crystal identification'],
                                        'answer': 'A) Antigen or antibody via enzyme-linked assay',
                                        'explanation': 'Enzyme-linked immunosorbent assay (ELISA) '
                                                       'immobilizes antigen or antibody on a solid '
                                                       'phase and uses an enzyme-conjugated '
                                                       'detector to generate a measurable signal. '
                                                       'Formats can detect antigen or antibody '
                                                       'depending on assay design. Controls and '
                                                       'cutoff verification are essential for '
                                                       'valid qualitative or quantitative '
                                                       'results.'},
                                       {'question': 'IgM generally indicates?',
                                        'options': ['A) Long-term immune memory only (IgG pattern)',
                                                    'B) Acute/recent humoral response',
                                                    'C) Mucosal secretory immunity only (IgA)',
                                                    'D) Mast-cell bound allergy only (IgE)'],
                                        'answer': 'B) Acute/recent humoral response',
                                        'explanation': 'IgM is the isotype produced earliest in a '
                                                       'primary humoral response and therefore '
                                                       'often marks acute or recent antigen '
                                                       'exposure. IgG typically rises later and '
                                                       'persists in memory responses. '
                                                       'Interpretation must consider rheumatoid '
                                                       'factor, class switching, and '
                                                       'assay-specific cutoffs.'},
                                       {'question': 'Blood type ABO based on?',
                                        'options': ['A) HLA class I typing of lymphocytes alone',
                                                    'B) Serum immunoglobulin subclass levels alone',
                                                    'C) RBC antigens and reciprocal plasma '
                                                    'isoagglutinins',
                                                    'D) Platelet glycoprotein antigen typing '
                                                    'alone'],
                                        'answer': 'C) RBC antigens and reciprocal plasma '
                                                  'isoagglutinins',
                                        'explanation': 'ABO blood group is defined by carbohydrate '
                                                       'antigens on the red-cell surface and by '
                                                       'reciprocal isoagglutinins (anti-A/anti-B) '
                                                       'in plasma. Forward and reverse typing must '
                                                       'agree for valid ABO assignment. '
                                                       'Discrepancies require resolution before '
                                                       'transfusion.'}],
                              'medium': [{'question': 'ANA testing used in?',
                                          'options': ['A) Acute bacterial culture identification',
                                                      'B) Routine newborn metabolic screening',
                                                      'C) Therapeutic drug monitoring of digoxin',
                                                      'D) Autoimmune disease workups (e.g., SLE '
                                                      'themes)'],
                                          'answer': 'D) Autoimmune disease workups (e.g., SLE '
                                                    'themes)',
                                          'explanation': 'Antinuclear antibody (ANA) testing '
                                                         'screens for autoantibodies directed '
                                                         'against nuclear antigens and is used in '
                                                         'the workup of systemic autoimmune '
                                                         'diseases such as SLE. Pattern and titer '
                                                         'information guide reflex '
                                                         'antigen-specific assays. Low-titer '
                                                         'positives can occur in healthy '
                                                         'individuals and require clinical '
                                                         'correlation.'},
                                         {'question': 'Window period means?',
                                          'options': ['A) Infection present but markers not yet '
                                                      'detectable',
                                                      'B) Infection cleared with lifelong '
                                                      'seronegativity',
                                                      'C) Vaccine response mistaken for acute '
                                                      'infection',
                                                      'D) Assay interference from heterophile '
                                                      'antibodies only'],
                                          'answer': 'A) Infection present but markers not yet '
                                                    'detectable',
                                          'explanation': 'The serologic window period is the '
                                                         'interval after infection when the '
                                                         'pathogen is present but diagnostic '
                                                         'markers remain below assay detection '
                                                         'limits. During this time, antibody or '
                                                         'even some antigen/NAAT assays may be '
                                                         'negative despite transmissibility. '
                                                         'Understanding window periods informs '
                                                         'retesting strategy and counseling.'},
                                         {'question': 'Complement C3/C4 low in?',
                                          'options': ['A) Most IgE-mediated allergic rhinitis '
                                                      'episodes',
                                                      'B) Some immune-complex diseases (e.g., '
                                                      'lupus nephritis)',
                                                      'C) Uncomplicated iron-deficiency anemia',
                                                      'D) Isolated osteoarthritis without '
                                                      'inflammation'],
                                          'answer': 'B) Some immune-complex diseases (e.g., lupus '
                                                    'nephritis)',
                                          'explanation': 'Complement components C3 and C4 are '
                                                         'consumed in classical-pathway activation '
                                                         'by immune complexes. Low C3/C4 levels '
                                                         'are classically seen in active SLE, '
                                                         'especially lupus nephritis, and some '
                                                         'other immune-complex disorders. Serial '
                                                         'levels help monitor disease activity '
                                                         'alongside clinical findings.'}],
                              'hard': [{'question': 'Prozone/hook in serology causes?',
                                        'options': ['A) False-positive results at antigen deficit '
                                                    'only',
                                                    'B) Correct titers without need for dilution',
                                                    'C) False-negative results at antibody excess',
                                                    'D) Only hemolysis without titer effects'],
                                        'answer': 'C) False-negative results at antibody excess',
                                        'explanation': 'Prozone (antibody excess) in agglutination '
                                                       'or precipitation serology can prevent '
                                                       'lattice formation and yield a '
                                                       'false-negative result. Diluting the '
                                                       'specimen restores the zone of equivalence '
                                                       'and reveals true reactivity. Recognizing '
                                                       'prozone prevents missed diagnoses in '
                                                       'high-titer sera.'},
                                       {'question': 'Flow cytometry immunophenotyping used for?',
                                        'options': ['A) Measuring serum electrolyte panels only',
                                                    'B) Quantifying urine specific gravity only',
                                                    'C) Determining PT/INR therapeutic ranges only',
                                                    'D) Lineage/marker characterization of cell '
                                                    'populations'],
                                        'answer': 'D) Lineage/marker characterization of cell '
                                                  'populations',
                                        'explanation': 'Flow cytometry immunophenotyping uses '
                                                       'fluorescent antibodies to characterize '
                                                       'cell-surface and intracellular markers. It '
                                                       'is central to diagnosing and classifying '
                                                       'leukemias/lymphomas and assessing immune '
                                                       'subsets. Gating strategy, controls, and '
                                                       'panel design determine interpretive '
                                                       'accuracy.'},
                                       {'question': 'Rheumatoid factor can interfere with?',
                                        'options': ['A) Some immunoassays (false-positive/negative '
                                                    'themes)',
                                                    'B) Blood gas pH electrode calibration only',
                                                    'C) Gram-stain decolorization timing only',
                                                    'D) Urine dipstick leukocyte esterase only'],
                                        'answer': 'A) Some immunoassays (false-positive/negative '
                                                  'themes)',
                                        'explanation': 'Rheumatoid factor (typically IgM anti-IgG) '
                                                       'can bridge capture and detection '
                                                       'antibodies in sandwich immunoassays, '
                                                       'causing false-positive signals, or '
                                                       'otherwise perturb assay architecture. '
                                                       'Blocking reagents and alternative assay '
                                                       'designs mitigate interference. Unexpected '
                                                       'serology results may prompt RF '
                                                       'investigation.'}],
                              'extreme': [{'question': 'Heterophile antibodies may cause?',
                                           'options': ['A) Only true pathogen-specific '
                                                       'neutralizing titers',
                                                       'B) False-positive or false-negative '
                                                       'immunoassay results',
                                                       'C) Only elevated ESR without immunoassay '
                                                       'effect',
                                                       'D) Only ABO discrepancies without serology '
                                                       'effect'],
                                           'answer': 'B) False-positive or false-negative '
                                                     'immunoassay results',
                                           'explanation': 'Heterophile antibodies are polyspecific '
                                                          'human antibodies that can bind assay '
                                                          'immunoglobulins and distort immunoassay '
                                                          'signals. They may produce falsely high '
                                                          'or low analyte results depending on '
                                                          'assay format. Heterophile blockers and '
                                                          'alternative methods help confirm '
                                                          'suspected interference.'},
                                          {'question': 'QuantiFERON-TB (IGRA) interprets?',
                                           'options': ['A) Direct acid-fast smear of sputum alone',
                                                       'B) Serum IgM to mycobacterial cell wall '
                                                       'alone',
                                                       'C) T-cell IFN-γ response to TB antigens',
                                                       'D) TST induration millimeters without '
                                                       'antigens'],
                                           'answer': 'C) T-cell IFN-γ response to TB antigens',
                                           'explanation': 'Interferon-gamma release assays such as '
                                                          'QuantiFERON measure T-cell IFN-γ '
                                                          'release after stimulation with M. '
                                                          'tuberculosis–specific antigens. Results '
                                                          'aid diagnosis of latent or active TB '
                                                          'infection in conjunction with clinical '
                                                          'and radiographic data. Indeterminate '
                                                          'results often reflect immunosuppression '
                                                          'or technical failure of controls.'},
                                          {'question': 'Cryoglobulin specimens require?',
                                           'options': ['A) Immediate refrigeration before clotting',
                                                       'B) Frozen transport on dry ice before '
                                                       'clotting',
                                                       'C) Room-temperature delay of several days',
                                                       'D) Collection/transport at 37°C before '
                                                       'separation'],
                                           'answer': 'D) Collection/transport at 37°C before '
                                                     'separation',
                                           'explanation': 'Cryoglobulins precipitate at cold '
                                                          'temperatures, so specimens must be '
                                                          'collected and maintained at 37°C until '
                                                          'serum is separated. Premature cooling '
                                                          'can falsely lower measured cryoglobulin '
                                                          'by precipitating it into the clot. '
                                                          'Proper preanalytics are essential for '
                                                          'detecting cryoglobulinemic disease.'}]},
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
                                        'options': ['A) RBC antigens (using reagent antisera)',
                                                    'B) Plasma antibodies only (reverse typing)',
                                                    'C) Hemoglobin concentration by '
                                                    'spectrophotometry',
                                                    'D) Leukocyte antigen HLA-A/B typing'],
                                        'answer': 'A) RBC antigens (using reagent antisera)',
                                        'explanation': 'Forward (cell) typing mixes patient red '
                                                       'cells with reagent anti-A, anti-B, and '
                                                       'often anti-D to detect A, B, and D '
                                                       'antigens. Reverse typing separately '
                                                       'detects expected isoagglutinins in plasma. '
                                                       'Concordant forward and reverse results '
                                                       'establish the ABO group.'},
                                       {'question': 'Crossmatch checks?',
                                        'options': ['A) Donor hemoglobin adequacy alone',
                                                    'B) Serologic compatibility between donor RBC '
                                                    'and recipient',
                                                    'C) Recipient platelet count alone',
                                                    'D) Donor infectious-disease NAT alone'],
                                        'answer': 'B) Serologic compatibility between donor RBC '
                                                  'and recipient',
                                        'explanation': 'A crossmatch tests donor red cells against '
                                                       'recipient plasma/serum to detect '
                                                       'incompatibility from ABO or unexpected '
                                                       'antibodies. Immediate-spin, antiglobulin, '
                                                       'or electronic crossmatch pathways are '
                                                       'selected per antibody-screen status and '
                                                       'policy. Compatible crossmatch reduces risk '
                                                       'of acute hemolytic transfusion reaction.'},
                                       {'question': 'O negative often used as?',
                                        'options': ['A) Universal plasma donor of first choice '
                                                    'always',
                                                    'B) Preferred platelets for all alloimmunized '
                                                    'patients',
                                                    'C) Emergency uncrossmatched RBC when type '
                                                    'unknown',
                                                    'D) Only autologous donation product type'],
                                        'answer': 'C) Emergency uncrossmatched RBC when type '
                                                  'unknown',
                                        'explanation': 'Group O RhD-negative red cells lack A/B '
                                                       'antigens and D antigen, making them the '
                                                       'usual emergency uncrossmatched RBC choice '
                                                       'when the recipient’s type is unknown. '
                                                       'Switch to type-specific blood as soon as '
                                                       'typing is complete to conserve O-negative '
                                                       'inventory. RhD-negative preference is '
                                                       'especially important for females of '
                                                       'childbearing potential.'}],
                              'medium': [{'question': 'RhIg indicated for?',
                                          'options': ['A) RhD-positive mothers after every '
                                                      'delivery',
                                                      'B) ABO-incompatible platelet transfusion '
                                                      'only',
                                                      'C) All RhD-negative males after trauma only',
                                                      'D) RhD-negative pregnancy at risk for D '
                                                      'alloimmunization'],
                                          'answer': 'D) RhD-negative pregnancy at risk for D '
                                                    'alloimmunization',
                                          'explanation': 'Rh immune globulin (RhIg) prevents '
                                                         'anti-D formation in RhD-negative '
                                                         'individuals exposed to RhD-positive red '
                                                         'cells, classically in pregnancy. '
                                                         'Antenatal and postpartum dosing follow '
                                                         'gestational timing and fetomaternal '
                                                         'hemorrhage assessment. Failure to give '
                                                         'indicated RhIg risks hemolytic disease '
                                                         'of the fetus/newborn in future '
                                                         'pregnancies.'},
                                         {'question': 'Acute hemolytic reaction classic cause?',
                                          'options': ['A) ABO-incompatible RBC transfusion '
                                                      '(clerical error themes)',
                                                      'B) Febrile nonhemolytic reaction from '
                                                      'cytokines alone',
                                                      'C) Allergic urticaria from plasma proteins '
                                                      'alone',
                                                      'D) TRALI from donor leukocyte antibodies '
                                                      'alone'],
                                          'answer': 'A) ABO-incompatible RBC transfusion (clerical '
                                                    'error themes)',
                                          'explanation': 'Acute hemolytic transfusion reactions '
                                                         'classically result from ABO-incompatible '
                                                         'red-cell transfusion, often due to '
                                                         'clerical identification errors. '
                                                         'Preformed isohemagglutinins fix '
                                                         'complement and cause intravascular '
                                                         'hemolysis. Immediate stop of '
                                                         'transfusion, clerical check, and '
                                                         'laboratory workup are mandatory.'},
                                         {'question': 'DAT detects?',
                                          'options': ['A) In vitro antibody screen panel '
                                                      'reactivity only',
                                                      'B) In vivo coating of RBCs with IgG and/or '
                                                      'complement',
                                                      'C) Free plasma hemoglobin after '
                                                      'centrifugation only',
                                                      'D) Donor unit culture contamination only'],
                                          'answer': 'B) In vivo coating of RBCs with IgG and/or '
                                                    'complement',
                                          'explanation': 'The direct antiglobulin test (DAT) '
                                                         'detects IgG and/or complement already '
                                                         'bound to circulating red cells in vivo. '
                                                         'It is used in evaluating autoimmune '
                                                         'hemolysis, hemolytic disease of the '
                                                         'newborn, and suspected hemolytic '
                                                         'transfusion reactions. Reagent '
                                                         'specificity (anti-IgG vs anti-C3) '
                                                         'refines interpretation.'}],
                              'hard': [{'question': 'Antibody screen positive next?',
                                        'options': ['A) Issue any ABO-identical unit without '
                                                    'further work',
                                                    'B) Discontinue all future transfusion '
                                                    'permanently',
                                                    'C) Antibody identification panel (± '
                                                    'phenotyping/crossmatch)',
                                                    'D) Repeat forward typing only and release '
                                                    'units'],
                                        'answer': 'C) Antibody identification panel (± '
                                                  'phenotyping/crossmatch)',
                                        'explanation': 'A positive antibody screen indicates '
                                                       'unexpected red-cell alloantibody (or '
                                                       'autoantibody) needing identification '
                                                       'before transfusion when possible. Antibody '
                                                       'panels, selected-cell panels, and antigen '
                                                       'typing guide compatible unit selection. '
                                                       'Delayed workup risks hemolytic transfusion '
                                                       'reactions.'},
                                       {'question': 'TRALI vs TACO?',
                                        'options': ['A) TRALI: volume overload; TACO: permeability '
                                                    'edema only',
                                                    'B) Both are identical IgE-mediated '
                                                    'anaphylaxis only',
                                                    'C) Both are delayed serologic hemolysis only',
                                                    'D) TRALI: permeability edema/inflammation; '
                                                    'TACO: hydrostatic overload'],
                                        'answer': 'D) TRALI: permeability edema/inflammation; '
                                                  'TACO: hydrostatic overload',
                                        'explanation': 'TRALI presents as acute noncardiogenic '
                                                       'permeability pulmonary edema related to '
                                                       'donor antibodies or bioactive lipids, '
                                                       'whereas TACO is hydrostatic cardiogenic '
                                                       'overload from volume. Distinguishing '
                                                       'features include blood pressure, BNP/echo '
                                                       'findings, and response to diuretics. '
                                                       'Product imputation and donor management '
                                                       'differ by diagnosis.'},
                                       {'question': 'Massive transfusion issues include?',
                                        'options': ['A) Coagulopathy, citrate effects, electrolyte '
                                                    'shifts, hypothermia themes',
                                                    'B) Only iron overload within the first hour',
                                                    'C) Only delayed serologic reactions in '
                                                    'minutes',
                                                    'D) Only graft-versus-host disease within '
                                                    'minutes'],
                                        'answer': 'A) Coagulopathy, citrate effects, electrolyte '
                                                  'shifts, hypothermia themes',
                                        'explanation': 'Massive transfusion can cause dilutional '
                                                       'coagulopathy, citrate-related '
                                                       'hypocalcemia, hyperkalemia or hypokalemia, '
                                                       'and hypothermia that worsen bleeding. '
                                                       'Ratio-based resuscitation and monitoring '
                                                       'of coag, ionized calcium, and temperature '
                                                       'mitigate complications. Laboratory support '
                                                       'is integral to damage-control '
                                                       'transfusion.'}],
                              'extreme': [{'question': 'Emergency release RBC when?',
                                           'options': ['A) Elective surgery with completed type '
                                                       'and screen',
                                                       'B) Life-threatening bleed before '
                                                       'compatibility testing completes',
                                                       'C) Stable anemia awaiting antibody '
                                                       'identification',
                                                       'D) Outpatient hemoglobin optimization over '
                                                       'weeks'],
                                           'answer': 'B) Life-threatening bleed before '
                                                     'compatibility testing completes',
                                           'explanation': 'Emergency-release (uncrossmatched) RBCs '
                                                          'are issued when delay for full '
                                                          'compatibility testing would endanger a '
                                                          'bleeding patient. O-negative or '
                                                          'type-specific units are released with '
                                                          'documentation of physician acceptance '
                                                          'of risk. Concurrent specimens for type, '
                                                          'screen, and crossmatch are obtained as '
                                                          'soon as possible.'},
                                          {'question': 'Warm AIHA transfusion approach?',
                                           'options': ['A) Refuse all RBC transfusion regardless '
                                                       'of hypoxia',
                                                       'B) Require only cold-agglutinin-compatible '
                                                       'units',
                                                       'C) Transfuse least-incompatible '
                                                       'crossmatch; treat underlying AIHA',
                                                       'D) Ignore alloantibodies if auto control '
                                                       'is positive'],
                                           'answer': 'C) Transfuse least-incompatible crossmatch; '
                                                     'treat underlying AIHA',
                                           'explanation': 'In warm autoimmune hemolytic anemia, '
                                                          'panagglutination often precludes '
                                                          'finding fully compatible units. '
                                                          'Transfusion, when necessary, uses the '
                                                          'least-incompatible crossmatched units '
                                                          'while treating the underlying process '
                                                          'and excluding underlying '
                                                          'alloantibodies. Communication between '
                                                          'blood bank and clinicians is '
                                                          'essential.'},
                                          {'question': 'Bacterial contamination risk highest with?',
                                           'options': ['A) Frozen plasma stored at ≤−18°C',
                                                       'B) Frozen cryoprecipitate in freezer '
                                                       'storage',
                                                       'C) Frozen RBC glycerolized units in '
                                                       'freezer',
                                                       'D) Platelets (room-temperature storage)'],
                                           'answer': 'D) Platelets (room-temperature storage)',
                                           'explanation': 'Platelets are stored at room '
                                                          'temperature with agitation, creating '
                                                          'conditions permissive for bacterial '
                                                          'growth if contaminated. Culture or '
                                                          'pathogen-reduction strategies and '
                                                          'visual inspection reduce septic '
                                                          'transfusion risk. Recipients with '
                                                          'fever/rigors during or after platelet '
                                                          'transfusion need prompt evaluation for '
                                                          'sepsis.'}]},
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
                                            'options': ['A) Fix tissues (preserve morphology)',
                                                        'B) Stain nuclei as a primary dye',
                                                        'C) Culture bacteria from tissue',
                                                        'D) Measure tissue glucose content'],
                                            'answer': 'A) Fix tissues (preserve morphology)',
                                            'explanation': 'Formalin (formaldehyde solution) '
                                                           'cross-links proteins to fix tissues, '
                                                           'preserving morphologic detail for '
                                                           'histologic processing. Adequate '
                                                           'fixation time and volume ratio prevent '
                                                           'autolysis and artifact. Overfixation '
                                                           'or underfixation can impair morphology '
                                                           'and some ancillary tests.'},
                                           {'question': 'H&E stain shows?',
                                            'options': ['A) Only mycobacteria by acid-fast '
                                                        'chemistry',
                                                        'B) General tissue morphology '
                                                        '(nuclei/cytoplasm)',
                                                        'C) Only amyloid by Congo red dichroism',
                                                        'D) Only iron by Prussian blue reaction'],
                                            'answer': 'B) General tissue morphology '
                                                      '(nuclei/cytoplasm)',
                                            'explanation': 'Hematoxylin and eosin (H&E) is the '
                                                           'routine histologic stain: hematoxylin '
                                                           'colors nuclei blue/purple and eosin '
                                                           'colors cytoplasm and extracellular '
                                                           'matrix pink. It provides the primary '
                                                           'morphologic assessment of tissue '
                                                           'architecture. Special stains and IHC '
                                                           'are added when H&E raises specific '
                                                           'questions.'},
                                           {'question': 'Pap smear is a?',
                                            'options': ['A) Histologic full-thickness cervical '
                                                        'biopsy only',
                                                        'B) Microbiology culture plate for STI '
                                                        'only',
                                                        'C) Cytologic screening specimen for '
                                                        'cervical neoplasia',
                                                        'D) Serum HPV antibody titer assay only'],
                                            'answer': 'C) Cytologic screening specimen for '
                                                      'cervical neoplasia',
                                            'explanation': 'The Papanicolaou (Pap) smear/cytology '
                                                           'samples exfoliated cervical cells to '
                                                           'screen for squamous intraepithelial '
                                                           'lesions and carcinoma. Liquid-based '
                                                           'cytology and HPV cotesting improve '
                                                           'detection pathways. Abnormal cytology '
                                                           'triggers colposcopic biopsy for '
                                                           'histologic confirmation.'}],
                                  'medium': [{'question': 'Immunohistochemistry detects?',
                                              'options': ['A) Only nucleic acid sequences by PCR '
                                                          'on slides',
                                                          'B) Only inorganic ions by '
                                                          'histochemistry alone',
                                                          'C) Only live organisms by culture from '
                                                          'blocks',
                                                          'D) Antigens in tissue using antibody '
                                                          'labeling'],
                                              'answer': 'D) Antigens in tissue using antibody '
                                                        'labeling',
                                              'explanation': 'Immunohistochemistry (IHC) uses '
                                                             'antibodies to localize specific '
                                                             'antigens in tissue sections via '
                                                             'chromogenic or fluorescent '
                                                             'detection. It supports tumor '
                                                             'classification, predictive marker '
                                                             'testing, and infectious-agent '
                                                             'detection. Controls and fixation '
                                                             'quality critically affect staining '
                                                             'validity.'},
                                             {'question': 'Frozen section purpose?',
                                              'options': ['A) Rapid intraoperative '
                                                          'diagnosis/margin assessment',
                                                          'B) Permanent archival staining without '
                                                          'urgency',
                                                          'C) Long-term nucleic acid banking only',
                                                          'D) Decalcification of dense bone '
                                                          'overnight'],
                                              'answer': 'A) Rapid intraoperative diagnosis/margin '
                                                        'assessment',
                                              'explanation': 'Frozen section provides rapid '
                                                             'intraoperative histologic assessment '
                                                             'for diagnosis, margins, or tissue '
                                                             'triage. Cryostat sections are '
                                                             'stained (often H&E) and interpreted '
                                                             'within minutes. Limitations include '
                                                             'freezing artifact and reduced '
                                                             'suitability for some ancillary '
                                                             'tests.'},
                                             {'question': 'Cytopathology adequacy matters because?',
                                              'options': ['A) Adequacy never affects interpretive '
                                                          'confidence',
                                                          'B) Inadequate samples risk false '
                                                          'negatives/repeat procedures',
                                                          'C) Only stains matter; cellularity is '
                                                          'irrelevant',
                                                          'D) Adequacy applies only to '
                                                          'microbiology cultures'],
                                              'answer': 'B) Inadequate samples risk false '
                                                        'negatives/repeat procedures',
                                              'explanation': 'Specimen adequacy criteria ensure '
                                                             'sufficient well-preserved '
                                                             'cells/material for reliable '
                                                             'cytologic interpretation. Inadequate '
                                                             'samples can miss neoplasia and '
                                                             'necessitate repeats, delaying care. '
                                                             'Rapid on-site evaluation (ROSE) '
                                                             'helps improve adequacy for many FNA '
                                                             'procedures.'}],
                                  'hard': [{'question': 'Poor fixation artifact can?',
                                            'options': ['A) Improve nuclear detail beyond '
                                                        'well-fixed tissue',
                                                        'B) Eliminate need for gross examination '
                                                        'entirely',
                                                        'C) Distort morphology and impair '
                                                        'IHC/molecular tests',
                                                        'D) Convert all specimens to microbiology '
                                                        'culture'],
                                            'answer': 'C) Distort morphology and impair '
                                                      'IHC/molecular tests',
                                            'explanation': 'Inadequate or delayed fixation allows '
                                                           'autolysis and poor nuclear/cytoplasmic '
                                                           'preservation that mimic or obscure '
                                                           'pathology. Antigenicity and nucleic '
                                                           'acid quality for IHC and molecular '
                                                           'assays may also degrade. Prompt '
                                                           'adequate formalin fixation (or '
                                                           'validated alternatives) is '
                                                           'foundational QA.'},
                                           {'question': 'Special stain AFB used for?',
                                            'options': ['A) Highlighting collagen only (trichrome '
                                                        'role)',
                                                        'B) Demonstrating fungi only (GMS/PAS '
                                                        'role)',
                                                        'C) Staining mucin only (mucicarmine role)',
                                                        'D) Detecting acid-fast organisms (e.g., '
                                                        'mycobacteria)'],
                                            'answer': 'D) Detecting acid-fast organisms (e.g., '
                                                      'mycobacteria)',
                                            'explanation': 'Acid-fast bacillus (AFB) special '
                                                           'stains detect organisms with mycolic '
                                                           'acid–rich walls, notably mycobacteria, '
                                                           'in tissue sections. Fluorochrome '
                                                           'methods increase screening '
                                                           'sensitivity; culture and PCR provide '
                                                           'complementary confirmation. Negative '
                                                           'stains do not fully exclude infection '
                                                           'when suspicion is high.'},
                                           {'question': 'Molecular tests on FFPE need?',
                                            'options': ['A) Adequate tumor content and nucleic '
                                                        'acid quality',
                                                        'B) Only H&E morphology without DNA/RNA QC',
                                                        'C) Decalcification in strong acid for all '
                                                        'blocks',
                                                        'D) Room-temperature paraffin without '
                                                        'fixation history'],
                                            'answer': 'A) Adequate tumor content and nucleic acid '
                                                      'quality',
                                            'explanation': 'Molecular assays on formalin-fixed '
                                                           'paraffin-embedded (FFPE) tissue '
                                                           'require sufficient neoplastic '
                                                           'cellularity and extractable nucleic '
                                                           'acid of acceptable quality/quantity. '
                                                           'Acid decalcification and prolonged '
                                                           'ischemia can damage DNA/RNA. '
                                                           'Pathologist enrichment and QC metrics '
                                                           'prevent false-negative or '
                                                           'uninterpretable results.'}],
                                  'extreme': [{'question': 'Critical specimen mislabeling '
                                                           'requires?',
                                               'options': ['A) Continue embedding and report under '
                                                           'either name',
                                                           'B) Stop processing; resolve identity '
                                                           'before reporting',
                                                           'C) Relabel to the more common clinic '
                                                           'name',
                                                           'D) Discard without documenting the '
                                                           'discrepancy'],
                                               'answer': 'B) Stop processing; resolve identity '
                                                         'before reporting',
                                               'explanation': 'Specimen mislabeling is a critical '
                                                              'patient-safety event because '
                                                              'wrong-patient diagnosis can lead to '
                                                              'catastrophic treatment errors. '
                                                              'Processing should halt while '
                                                              'identity is investigated using '
                                                              'available paperwork, tissue '
                                                              'comparison, and institutional '
                                                              'protocol. Documentation and '
                                                              'disclosure follow risk-management '
                                                              'policy.'},
                                              {'question': 'Cytotech finds malignant cells '
                                                           'unexpectedly?',
                                               'options': ['A) Release as negative without '
                                                           'pathologist review',
                                                           'B) Discard the slide as likely '
                                                           'contaminant silently',
                                                           'C) Escalate for pathologist review and '
                                                           'clinical notification pathways',
                                                           'D) Repeat only if the clinician calls '
                                                           'later'],
                                               'answer': 'C) Escalate for pathologist review and '
                                                         'clinical notification pathways',
                                               'explanation': 'Unexpected malignant cells in '
                                                              'cytology or fluids require '
                                                              'pathologist confirmation and '
                                                              'appropriate clinical communication '
                                                              'per policy. Premature release as '
                                                              '“negative” can delay cancer care. '
                                                              'Correlation with history and '
                                                              'ancillary studies supports accurate '
                                                              'classification.'},
                                              {'question': 'Decalcification of bone for histology?',
                                               'options': ['A) Adds mineral to harden soft tissues '
                                                           'for cutting',
                                                           'B) Replaces formalin fixation entirely '
                                                           'for soft tissue',
                                                           'C) Is required for all cytology '
                                                           'liquid-based specimens',
                                                           'D) Removes mineral to allow '
                                                           'sectioning; may affect some tests'],
                                               'answer': 'D) Removes mineral to allow sectioning; '
                                                         'may affect some tests',
                                               'explanation': 'Decalcification removes calcium '
                                                              'from bone/mineralized tissue so '
                                                              'microtomes can cut sections. Acid '
                                                              'methods are faster but can impair '
                                                              'DNA and some antigens more than '
                                                              'gentler chelating methods. Test '
                                                              'menus should consider '
                                                              'decalcification effects when '
                                                              'ordering molecular or IHC '
                                                              'studies.'}]},
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
                                                      'B) Only aerobic bacterial colony counts',
                                                      'C) Only viral antigen panels',
                                                      'D) Only fecal occult blood chemistry'],
                                          'answer': 'A) Ova and parasites',
                                          'explanation': 'Ova and parasite (O&P) examination '
                                                         'evaluates stool for helminth eggs, '
                                                         'larvae, and protozoan cysts/trophozoites '
                                                         'using microscopy with concentration and '
                                                         'stained smears. Multiple specimens may '
                                                         'be needed because shedding can be '
                                                         'intermittent. Findings guide '
                                                         'antiparasitic therapy and public-health '
                                                         'follow-up.'},
                                         {'question': 'Malaria diagnosed commonly by?',
                                          'options': ['A) Stool wet mount for trophozoites only',
                                                      'B) Blood film microscopy (thick/thin '
                                                      'smears)',
                                                      'C) Urine dipstick leukocyte esterase only',
                                                      'D) CSF cryptococcal antigen only'],
                                          'answer': 'B) Blood film microscopy (thick/thin smears)',
                                          'explanation': 'Malaria diagnosis classically relies on '
                                                         'Giemsa-stained thick and thin blood '
                                                         'films to detect and speciate Plasmodium. '
                                                         'Rapid antigen tests and molecular assays '
                                                         'are adjuncts depending on setting. '
                                                         'Parasite density and species '
                                                         'identification guide urgency and drug '
                                                         'selection.'},
                                         {'question': 'Enterobius best sampled by?',
                                          'options': ['A) Midstream clean-catch urine culture',
                                                      'B) Sputum acid-fast smear for eggs',
                                                      'C) Perianal cellulose tape test',
                                                      'D) Peripheral blood thin film for adults'],
                                          'answer': 'C) Perianal cellulose tape test',
                                          'explanation': 'Enterobius vermicularis (pinworm) '
                                                         'females deposit eggs on perianal skin, '
                                                         'so the cellulose tape or paddle test '
                                                         'collects eggs more reliably than stool '
                                                         'O&P. Specimens are best obtained in the '
                                                         'morning before bathing. Identification '
                                                         'of eggs confirms infection and guides '
                                                         'household treatment.'}],
                                'medium': [{'question': 'Giardia trophozoites seen in?',
                                            'options': ['A) Peripheral blood erythrocytes as ring '
                                                        'forms',
                                                        'B) Sputum as operculated eggs',
                                                        'C) Skin scrapings as burrowing mites',
                                                        'D) Duodenal fluid/stool (pear-shaped, '
                                                        'falling-leaf motility)'],
                                            'answer': 'D) Duodenal fluid/stool (pear-shaped, '
                                                      'falling-leaf motility)',
                                            'explanation': 'Giardia duodenalis trophozoites are '
                                                           'pear-shaped flagellates with '
                                                           'distinctive motility, found in stool '
                                                           'or duodenal specimens; cysts are the '
                                                           'environmentally resistant form. '
                                                           'Antigen and molecular assays '
                                                           'complement microscopy. Infection '
                                                           'causes small-bowel malabsorption and '
                                                           'diarrhea.'},
                                           {'question': 'E. histolytica concern?',
                                            'options': ['A) Invasive amebiasis (colitis/liver '
                                                        'abscess themes)',
                                                        'B) Only noninvasive luminal colonization '
                                                        'forever',
                                                        'C) Only bloodstream microfilariae without '
                                                        'colitis',
                                                        'D) Only muscle cysts of Trichinella'],
                                            'answer': 'A) Invasive amebiasis (colitis/liver '
                                                      'abscess themes)',
                                            'explanation': 'Entamoeba histolytica can invade '
                                                           'intestinal mucosa causing dysentery '
                                                           'and may spread to form liver '
                                                           'abscesses. Differentiation from '
                                                           'nonpathogenic Entamoeba dispar '
                                                           'requires antigen/molecular methods '
                                                           'when morphology overlaps. '
                                                           'Extraintestinal disease may lack '
                                                           'concurrent stool organisms.'},
                                           {'question': 'Ziehl-Neelsen modified may help detect?',
                                            'options': ['A) Helminth adults in blood films',
                                                        'B) Coccidian oocysts (e.g., '
                                                        'Cryptosporidium)',
                                                        'C) Only Giardia cysts without '
                                                        'acid-fastness',
                                                        'D) Only Enterobius eggs on tape tests'],
                                            'answer': 'B) Coccidian oocysts (e.g., '
                                                      'Cryptosporidium)',
                                            'explanation': 'Modified Ziehl–Neelsen (acid-fast) '
                                                           'staining highlights coccidian oocysts '
                                                           'such as Cryptosporidium, Cyclospora, '
                                                           'and Cystoisospora in stool. Standard '
                                                           'O&P stains may miss these organisms. '
                                                           'Antigen/NAAT methods further improve '
                                                           'Cryptosporidium detection.'}],
                                'hard': [{'question': 'Babesia vs malaria on film?',
                                          'options': ['A) Babesia always has schizonts with '
                                                      'hemozoin pigment',
                                                      'B) Malaria never shows ring forms in RBCs',
                                                      'C) Babesia may show Maltese cross; often no '
                                                      'travel; different therapy',
                                                      'D) Both are identical and treated the same '
                                                      'always'],
                                          'answer': 'C) Babesia may show Maltese cross; often no '
                                                    'travel; different therapy',
                                          'explanation': 'Babesia intraerythrocytic parasites may '
                                                         'form pathognomonic tetrad “Maltese '
                                                         'cross” arrangements and can mimic '
                                                         'Plasmodium rings. Epidemiology (tick '
                                                         'exposure, no travel), absent hemozoin, '
                                                         'and extracellular forms help '
                                                         'differentiation. Therapy and '
                                                         'blood-product implications differ from '
                                                         'malaria.'},
                                         {'question': 'Hydatid disease caution in lab?',
                                          'options': ['A) Routine open-bench culture of cyst fluid '
                                                      'for ID',
                                                      'B) Freeze-thaw only without containment '
                                                      'concerns',
                                                      'C) Ignore PPE if the cyst appears inactive',
                                                      'D) Avoid spilling cystic fluid '
                                                      '(anaphylaxis/dissemination risk)'],
                                          'answer': 'D) Avoid spilling cystic fluid '
                                                    '(anaphylaxis/dissemination risk)',
                                          'explanation': 'Echinococcal (hydatid) cysts contain '
                                                         'highly antigenic fluid; spillage during '
                                                         'surgery or grossing can trigger '
                                                         'anaphylaxis and secondary dissemination '
                                                         'of protoscolices. Laboratories and OR '
                                                         'teams use careful containment and PPE. '
                                                         'Serology and imaging complement '
                                                         'parasitologic confirmation.'},
                                         {'question': 'Concentration methods increase?',
                                          'options': ['A) Sensitivity for recovering ova/cysts',
                                                      'B) Specificity by destroying all cysts',
                                                      'C) Only bacterial colony counts on '
                                                      'MacConkey',
                                                      'D) Only viral culture yield from stool'],
                                          'answer': 'A) Sensitivity for recovering ova/cysts',
                                          'explanation': 'Parasitology concentration methods such '
                                                         'as formalin–ethyl acetate sedimentation '
                                                         'increase recovery of eggs, cysts, and '
                                                         'larvae from stool. Concentrates are '
                                                         'examined wet and with permanent stains '
                                                         'as indicated. Improved sensitivity '
                                                         'reduces false-negative O&P exams.'}],
                                'extreme': [{'question': 'Leishmania amastigotes found in?',
                                             'options': ['A) Circulating erythrocytes as banana '
                                                         'gametocytes',
                                                         'B) Macrophages in tissue/bone marrow',
                                                         'C) Stool as operculated trematode eggs',
                                                         'D) Urine as schistosome eggs only'],
                                             'answer': 'B) Macrophages in tissue/bone marrow',
                                             'explanation': 'Leishmania amastigotes parasitize '
                                                            'macrophages and are demonstrated in '
                                                            'bone marrow, splenic, or tissue '
                                                            'aspirates/biopsies. Morphology shows '
                                                            'kinetoplasts alongside nuclei. '
                                                            'Culture, serology, and PCR support '
                                                            'species-level diagnosis and '
                                                            'management.'},
                                            {'question': 'Automated malaria analyzers still need?',
                                             'options': ['A) No microscopic review if any flag '
                                                         'appears',
                                                         'B) Only stool O&P to confirm blood flags',
                                                         'C) Expert smear review for '
                                                         'confirmation/speciation',
                                                         'D) Only serology without blood-film '
                                                         'correlation'],
                                             'answer': 'C) Expert smear review for '
                                                       'confirmation/speciation',
                                             'explanation': 'Automated hematology analyzers may '
                                                            'flag malaria-related abnormalities '
                                                            'but lack sufficient specificity and '
                                                            'speciation capability for definitive '
                                                            'diagnosis. Expert thick/thin smear '
                                                            'review (or validated rapid/molecular '
                                                            'testing) remains required. Species '
                                                            'and density determine therapy.'},
                                            {'question': 'Formalin stool vials hazard?',
                                             'options': ['A) Completely nonhazardous household '
                                                         'saline',
                                                         'B) Radioactive waste requiring lead '
                                                         'shielding',
                                                         'C) Biohazard only with no chemical '
                                                         'toxicity',
                                                         'D) Chemical exposure risk — handle per '
                                                         'SDS/PPE'],
                                             'answer': 'D) Chemical exposure risk — handle per '
                                                       'SDS/PPE',
                                             'explanation': 'Formalin used in stool fixative vials '
                                                            'is a hazardous chemical with toxic '
                                                            'and sensitizing properties defined in '
                                                            'the safety data sheet. Staff should '
                                                            'use PPE, ventilation, and spill '
                                                            'procedures per laboratory policy. '
                                                            'Proper labeling and disposal protect '
                                                            'personnel.'}]},
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
                                                               'B) Target proteins without nucleic '
                                                               'acid',
                                                               'C) Target lipids in membrane '
                                                               'extracts',
                                                               'D) Target glucose in plasma '
                                                               'filtrates'],
                                                   'answer': 'A) Target nucleic acid',
                                                   'explanation': 'Polymerase chain reaction (PCR) '
                                                                  'enzymatically amplifies a '
                                                                  'defined nucleic acid target '
                                                                  'through repeated cycles of '
                                                                  'denaturation, annealing, and '
                                                                  'extension. Exponential '
                                                                  'amplification enables sensitive '
                                                                  'detection of pathogens and '
                                                                  'genetic variants. Primer/probe '
                                                                  'design determines specificity.'},
                                                  {'question': 'Contamination control in PCR '
                                                               'includes?',
                                                   'options': ['A) Shared pipettes across pre- and '
                                                               'post-PCR benches',
                                                               'B) Separate areas, unidirectional '
                                                               'workflow, and controls',
                                                               'C) Open amplicon handling beside '
                                                               'extraction',
                                                               'D) Skipping no-template controls '
                                                               'to save wells'],
                                                   'answer': 'B) Separate areas, unidirectional '
                                                             'workflow, and controls',
                                                   'explanation': 'PCR is highly susceptible to '
                                                                  'false positives from amplicon '
                                                                  'or specimen contamination. '
                                                                  'Laboratories use unidirectional '
                                                                  'workflow, physical separation '
                                                                  'of pre- and post-PCR areas, '
                                                                  'dedicated reagents, and '
                                                                  'negative controls. '
                                                                  'Environmental wipe testing '
                                                                  'helps detect covert '
                                                                  'contamination.'},
                                                  {'question': 'Viral load assays monitor?',
                                                   'options': ['A) Only qualitative serology IgG '
                                                               'presence',
                                                               'B) Only plaque morphology on '
                                                               'culture plates',
                                                               'C) Quantity of viral nucleic acid',
                                                               'D) Only CD4 percentage without '
                                                               'nucleic acid'],
                                                   'answer': 'C) Quantity of viral nucleic acid',
                                                   'explanation': 'Viral load assays quantify '
                                                                  'pathogen nucleic acid, '
                                                                  'typically as IU/mL or '
                                                                  'copies/mL, using calibrated '
                                                                  'real-time PCR or related '
                                                                  'methods. Serial results monitor '
                                                                  'treatment response in '
                                                                  'infections such as HIV, HBV, '
                                                                  'and HCV. Standardization and '
                                                                  'log-change interpretation guide '
                                                                  'clinical decisions.'}],
                                         'medium': [{'question': 'Ct value roughly relates to?',
                                                     'options': ['A) Directly proportional to '
                                                                 'target amount always',
                                                                 'B) Independent of template '
                                                                 'concentration always',
                                                                 'C) Only to extraction volume, '
                                                                 'never template',
                                                                 'D) Inversely to target amount '
                                                                 '(method-dependent)'],
                                                     'answer': 'D) Inversely to target amount '
                                                               '(method-dependent)',
                                                     'explanation': 'In real-time PCR, the cycle '
                                                                    'threshold (Ct) is the cycle '
                                                                    'at which fluorescence exceeds '
                                                                    'a defined threshold. Lower Ct '
                                                                    'values generally indicate '
                                                                    'more starting target nucleic '
                                                                    'acid, though exact '
                                                                    'quantification requires a '
                                                                    'calibration curve. Assay '
                                                                    'design and efficiency affect '
                                                                    'the Ct–quantity '
                                                                    'relationship.'},
                                                    {'question': 'Internal control failure '
                                                                 'suggests?',
                                                     'options': ['A) Inhibition or extraction '
                                                                 'problem',
                                                                 'B) Confirmed true-negative '
                                                                 'without caveats',
                                                                 'C) Instrument optical failure '
                                                                 'only, never inhibition',
                                                                 'D) Primer redesign is always '
                                                                 'required immediately'],
                                                     'answer': 'A) Inhibition or extraction '
                                                               'problem',
                                                     'explanation': 'An internal control '
                                                                    'co-extracted and co-amplified '
                                                                    'with the patient specimen '
                                                                    'monitors extraction '
                                                                    'efficiency and PCR '
                                                                    'inhibition. Failure of the '
                                                                    'internal control invalidates '
                                                                    'a negative target result and '
                                                                    'prompts re-extraction or '
                                                                    'dilution studies. Valid '
                                                                    'controls are required before '
                                                                    'clinical reporting.'},
                                                    {'question': 'Genotyping may guide?',
                                                     'options': ['A) Only specimen transport '
                                                                 'temperature logs',
                                                                 'B) Therapy '
                                                                 '(resistance/pharmacogenetics '
                                                                 'themes)',
                                                                 'C) Only centrifuge RPM '
                                                                 'validation schedules',
                                                                 'D) Only pipette calibration '
                                                                 'intervals'],
                                                     'answer': 'B) Therapy '
                                                               '(resistance/pharmacogenetics '
                                                               'themes)',
                                                     'explanation': 'Genotyping identifies '
                                                                    'sequence variants that '
                                                                    'predict drug resistance or '
                                                                    'alter drug metabolism, as in '
                                                                    'HIV resistance testing or '
                                                                    'pharmacogenetic panels. '
                                                                    'Results help select effective '
                                                                    'therapy and dosing. Analytic '
                                                                    'validity and clinical '
                                                                    'annotation databases support '
                                                                    'interpretation.'}],
                                         'hard': [{'question': 'NGS panels need?',
                                                   'options': ['A) Wet-lab sequencing alone '
                                                               'without analysis',
                                                               'B) Sanger confirmation of every '
                                                               'wild-type base',
                                                               'C) Bioinformatic pipelines, QC '
                                                               'metrics, and interpretation',
                                                               'D) No coverage thresholds for '
                                                               'clinical reporting'],
                                                   'answer': 'C) Bioinformatic pipelines, QC '
                                                             'metrics, and interpretation',
                                                   'explanation': 'Next-generation sequencing '
                                                                  '(NGS) panels generate massive '
                                                                  'parallel reads that require '
                                                                  'bioinformatic pipelines for '
                                                                  'alignment, variant calling, and '
                                                                  'annotation. Quality metrics '
                                                                  '(coverage, uniformity, '
                                                                  'contamination checks) gate '
                                                                  'reportability. '
                                                                  'Multidisciplinary '
                                                                  'interpretation links variants '
                                                                  'to clinical actionability.'},
                                                  {'question': 'Minimal residual disease PCR '
                                                               'detects?',
                                                   'options': ['A) Only morphologic blast '
                                                               'percentage above 5%',
                                                               'B) Only cytogenetic metaphases '
                                                               'without DNA target',
                                                               'C) Only serum protein '
                                                               'electrophoresis clones',
                                                               'D) Very low-level residual disease '
                                                               'target'],
                                                   'answer': 'D) Very low-level residual disease '
                                                             'target',
                                                   'explanation': 'MRD PCR assays amplify '
                                                                  'leukemia-specific targets such '
                                                                  'as fusion transcripts or clonal '
                                                                  'immunoglobulin/T-cell receptor '
                                                                  'rearrangements at high '
                                                                  'sensitivity. Detectable MRD '
                                                                  'after therapy informs relapse '
                                                                  'risk and consolidation '
                                                                  'decisions. Assay limit of '
                                                                  'detection must be validated and '
                                                                  'reported.'},
                                                  {'question': 'Sample swap detection uses?',
                                                   'options': ['A) Identity checks/barcodes (± '
                                                               'genetic ID strategies)',
                                                               'B) Ignoring identifiers if Ct '
                                                               'values look expected',
                                                               'C) Relying only on handwritten '
                                                               'first names',
                                                               'D) Skipping accession checks for '
                                                               'add-on tests'],
                                                   'answer': 'A) Identity checks/barcodes (± '
                                                             'genetic ID strategies)',
                                                   'explanation': 'Specimen identity errors can '
                                                                  'cause catastrophic molecular '
                                                                  'misdiagnosis. Laboratories use '
                                                                  'barcodes, chain-of-custody '
                                                                  'checks, and sometimes genetic '
                                                                  'identity markers to detect '
                                                                  'swaps. Discrepancies halt '
                                                                  'reporting until identity is '
                                                                  'resolved.'}],
                                         'extreme': [{'question': 'Laboratory-developed tests '
                                                                  'require?',
                                                      'options': ['A) Immediate patient reporting '
                                                                  'without performance data',
                                                                  'B) Validation/verification per '
                                                                  'regulations before clinical use',
                                                                  'C) Research-use-only reagents '
                                                                  'without local validation',
                                                                  'D) Vendor marketing claims as '
                                                                  'sole acceptance criteria'],
                                                      'answer': 'B) Validation/verification per '
                                                                'regulations before clinical use',
                                                      'explanation': 'Laboratory-developed tests '
                                                                     '(LDTs) must be validated or '
                                                                     'verified for accuracy, '
                                                                     'precision, reportable range, '
                                                                     'and other performance '
                                                                     'characteristics before '
                                                                     'clinical use per applicable '
                                                                     'regulations and '
                                                                     'accreditation standards. '
                                                                     'Documentation of acceptance '
                                                                     'criteria and limitations is '
                                                                     'mandatory. Ongoing QC '
                                                                     'sustains performance after '
                                                                     'go-live.'},
                                                     {'question': 'Amplicon contamination outbreak '
                                                                  'presents as?',
                                                      'options': ['A) Isolated true positives with '
                                                                  'epidemiologic links only',
                                                                  'B) Only internal-control '
                                                                  'failures without positives',
                                                                  'C) Clusters of unexpected '
                                                                  'positive PCR results',
                                                                  'D) Only reagent lot shortages '
                                                                  'without result patterns'],
                                                      'answer': 'C) Clusters of unexpected '
                                                                'positive PCR results',
                                                      'explanation': 'Amplicon contamination '
                                                                     'outbreaks produce clusters '
                                                                     'of unexpected positive PCR '
                                                                     'results, often with late Ct '
                                                                     'values or positives in '
                                                                     'negative controls. Immediate '
                                                                     'containment includes '
                                                                     'stopping testing, '
                                                                     'environmental cleaning, and '
                                                                     'root-cause investigation. '
                                                                     'Retesting from primary '
                                                                     'specimens after remediation '
                                                                     'confirms integrity.'},
                                                     {'question': 'Cell-free DNA assays challenges '
                                                                  'include?',
                                                      'options': ['A) Abundant intact genomic DNA '
                                                                  'identical to tissue',
                                                                  'B) No need for specialized '
                                                                  'blood-collection tubes',
                                                                  'C) Stability for weeks at '
                                                                  'ambient temperature always',
                                                                  'D) Low analyte levels, '
                                                                  'fragmentation, and '
                                                                  'preanalytics'],
                                                      'answer': 'D) Low analyte levels, '
                                                                'fragmentation, and preanalytics',
                                                      'explanation': 'Circulating cell-free DNA '
                                                                     'assays measure fragmented '
                                                                     'extracellular DNA present at '
                                                                     'low concentrations in '
                                                                     'plasma. Preanalytic '
                                                                     'variables (tube type, time '
                                                                     'to spin, hemolysis) strongly '
                                                                     'affect yield and fragment '
                                                                     'profiles. Sensitive methods '
                                                                     'and careful controls are '
                                                                     'required for reliable '
                                                                     'detection.'}]},
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
                                    'options': ['A) Quality assurance — systems ensuring reliable '
                                                'results',
                                                'B) Quick assay — fastest method regardless of QC',
                                                'C) Quiet area — noise limits for analyzers only',
                                                'D) Quarterly absence — staffing vacation '
                                                'tracking'],
                                    'answer': 'A) Quality assurance — systems ensuring reliable '
                                              'results',
                                    'explanation': 'Quality assurance (QA) encompasses the '
                                                   'organized systems, policies, and monitoring '
                                                   'activities that ensure laboratory results are '
                                                   'reliable and fit for clinical use. QA spans '
                                                   'preanalytic, analytic, and postanalytic '
                                                   'phases. It is broader than daily QC and '
                                                   'includes PT, document control, and continual '
                                                   'improvement.'},
                                   {'question': 'QC monitors?',
                                    'options': ['A) Only clinician satisfaction survey scores',
                                                'B) Analytic method performance over time',
                                                'C) Only purchasing contract renewal dates',
                                                'D) Only building temperature for HVAC billing'],
                                    'answer': 'B) Analytic method performance over time',
                                    'explanation': 'Quality control (QC) uses materials of known '
                                                   'target values to monitor analytic method '
                                                   'stability over time. Results are plotted and '
                                                   'evaluated with rules to detect shifts, trends, '
                                                   'and imprecision. QC failures trigger '
                                                   'investigation before patient results are '
                                                   'released.'},
                                   {'question': 'SOP stands for?',
                                    'options': ['A) Selective optional protocol',
                                                'B) Specimen overflow process',
                                                'C) Standard operating procedure',
                                                'D) Supervisor oral permission'],
                                    'answer': 'C) Standard operating procedure',
                                    'explanation': 'A standard operating procedure (SOP) is the '
                                                   'controlled written instruction detailing how a '
                                                   'method or process is performed. Staff must '
                                                   'follow the current approved SOP version. '
                                                   'Document control ensures obsolete instructions '
                                                   'are removed from use.'}],
                          'medium': [{'question': 'Westgard rules help detect?',
                                      'options': ['A) Only patient delta-check identity mismatches',
                                                  'B) Only proficiency shipping delays',
                                                  'C) Only critical-value phone read-back failures',
                                                  'D) Random and systematic error patterns in QC'],
                                      'answer': 'D) Random and systematic error patterns in QC',
                                      'explanation': 'Westgard multirule QC applies combinations '
                                                     'of control rules (for example 1₃ₛ, 2₂ₛ, R₄ₛ) '
                                                     'to distinguish random from systematic error. '
                                                     'Rule violations prompt troubleshooting of '
                                                     'reagents, calibration, and instrumentation. '
                                                     'Appropriate rule selection balances error '
                                                     'detection with false rejection.'},
                                     {'question': 'Proficiency testing evaluates?',
                                      'options': ['A) Laboratory accuracy on external unknown '
                                                  'specimens',
                                                  'B) Only internal QC means without peer '
                                                  'comparison',
                                                  'C) Only employee continuing-education '
                                                  'attendance',
                                                  'D) Only analyzer uptime percentage metrics'],
                                      'answer': 'A) Laboratory accuracy on external unknown '
                                                'specimens',
                                      'explanation': 'Proficiency testing (PT) submits blinded '
                                                     'external specimens for analysis and compares '
                                                     'laboratory results with peer or reference '
                                                     'targets. Successful PT is an accreditation '
                                                     'requirement demonstrating analytic accuracy. '
                                                     'Failures require investigation and '
                                                     'corrective action.'},
                                     {'question': 'Critical results require?',
                                      'options': ['A) Release into the chart without clinician '
                                                  'contact',
                                                  'B) Timely notification with read-back and '
                                                  'documentation',
                                                  'C) Notification only at the next shift change',
                                                  'D) Patient self-notification via portal only'],
                                      'answer': 'B) Timely notification with read-back and '
                                                'documentation',
                                      'explanation': 'Critical results are laboratory values that '
                                                     'indicate potentially life-threatening '
                                                     'conditions and require immediate clinical '
                                                     'notification. Read-back verification and '
                                                     'documentation complete the communication '
                                                     'loop. Policies define analyte lists, '
                                                     'timeframes, and escalation paths.'}],
                          'hard': [{'question': 'Root cause analysis after error aims to?',
                                    'options': ['A) Punish the last person who touched the '
                                                'specimen',
                                                'B) Hide the event from accreditation surveyors',
                                                'C) Correct system causes, not only blame '
                                                'individuals',
                                                'D) Rewrite QC data to erase the incident trail'],
                                    'answer': 'C) Correct system causes, not only blame '
                                              'individuals',
                                    'explanation': 'Root cause analysis after a laboratory error '
                                                   'investigates underlying system failures such '
                                                   'as process design, training gaps, and '
                                                   'interface issues rather than stopping at '
                                                   'individual blame. Effective CAPA addresses '
                                                   'latent conditions that allowed the error. '
                                                   'Sharing lessons learned prevents recurrence.'},
                                   {'question': 'Document control ensures?',
                                    'options': ['A) Staff may keep personal unofficial binders',
                                                'B) Obsolete SOPs remain at benches for reference',
                                                'C) Draft procedures are used before approval',
                                                'D) Only current approved SOPs are in use'],
                                    'answer': 'D) Only current approved SOPs are in use',
                                    'explanation': 'Document control ensures that only the '
                                                   'current, approved version of each SOP, form, '
                                                   'and policy is available at the point of use. '
                                                   'Obsolete documents are removed or clearly '
                                                   'archived. Version history and approval '
                                                   'signatures support accreditation compliance.'},
                                   {'question': 'Risk management in labs includes?',
                                    'options': ['A) Identifying failure modes and implementing '
                                                'mitigations',
                                                'B) Waiting for patient harm before any review',
                                                'C) Eliminating all QC to reduce false rejects',
                                                'D) Outsourcing all critical-value calls '
                                                'permanently'],
                                    'answer': 'A) Identifying failure modes and implementing '
                                              'mitigations',
                                    'explanation': 'Laboratory risk management systematically '
                                                   'identifies potential failure modes across '
                                                   'testing pathways and implements mitigations '
                                                   'proportional to severity and likelihood. Tools '
                                                   'may include process mapping and failure mode '
                                                   'effects analysis. Residual risk is monitored '
                                                   'through QC, audits, and incident review.'}],
                          'extreme': [{'question': 'Accreditation nonconformance demands?',
                                       'options': ['A) Verbal promise without documented CAPA',
                                                   'B) Corrective/preventive action with '
                                                   'effectiveness evidence',
                                                   'C) Ignoring findings until the next survey '
                                                   'cycle',
                                                   'D) Rewording the SOP title without process '
                                                   'change'],
                                       'answer': 'B) Corrective/preventive action with '
                                                 'effectiveness evidence',
                                       'explanation': 'Accreditation nonconformances require '
                                                      'documented corrective and preventive action '
                                                      '(CAPA) with evidence that the fix is '
                                                      'effective. Root cause, implementation, and '
                                                      'follow-up monitoring are assessed by '
                                                      'surveyors. Timely closure protects patient '
                                                      'safety and accreditation status.'},
                                      {'question': 'LIS downtime procedure must?',
                                       'options': ['A) Stop all testing until IT returns next week',
                                                   'B) Release results without patient identifiers',
                                                   'C) Maintain safe manual identification and '
                                                   'reporting',
                                                   'D) Use informal texts as the permanent record '
                                                   'only'],
                                       'answer': 'C) Maintain safe manual identification and '
                                                 'reporting',
                                       'explanation': 'Laboratory information system (LIS) '
                                                      'downtime procedures provide validated '
                                                      'manual workflows for order entry, specimen '
                                                      'identification, result recording, and '
                                                      'reporting. Patient ID integrity and '
                                                      'critical-value communication must continue. '
                                                      'After recovery, data are entered and '
                                                      'reconciled per protocol.'},
                                      {'question': 'Ethical reflex: altered QC to pass?',
                                       'options': ['A) Acceptable if patient results look '
                                                   'plausible',
                                                   'B) Allowed when reagent costs are high that '
                                                   'week',
                                                   'C) Required to keep turnaround time statistics '
                                                   'green',
                                                   'D) Fraud — never alter QC; report integrity '
                                                   'concerns'],
                                       'answer': 'D) Fraud — never alter QC; report integrity '
                                                 'concerns',
                                       'explanation': 'Altering quality-control data to force a '
                                                      'method to “pass” is scientific misconduct '
                                                      'and endangers patients by concealing '
                                                      'analytic failure. Staff must refuse '
                                                      'falsification and escalate integrity '
                                                      'concerns through proper channels. A culture '
                                                      'of safety supports transparent '
                                                      'troubleshooting.'}]},
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
                                        'options': ['A) Intact RBCs, free hemoglobin, or myoglobin',
                                                    'B) Glucose via glucose oxidase only',
                                                    'C) Ketones via nitroprusside only',
                                                    'D) Leukocyte esterase from WBC enzymes only'],
                                        'answer': 'A) Intact RBCs, free hemoglobin, or myoglobin',
                                        'explanation': 'Urine dipstick “blood” reagents detect '
                                                       'heme’s peroxidase-like activity and '
                                                       'therefore react with intact red cells, '
                                                       'free hemoglobin, and myoglobin. Microscopy '
                                                       'distinguishes hematuria from heme-positive '
                                                       'pigmenturia. Clinical context separates '
                                                       'hemoglobinuria from myoglobinuria.'},
                                       {'question': 'Specific gravity estimates?',
                                        'options': ['A) Exact 24-hour protein excretion grams',
                                                    'B) Urine concentrating ability (relative '
                                                    'density)',
                                                    'C) Bacterial species identification',
                                                    'D) Urine pH buffering capacity alone'],
                                        'answer': 'B) Urine concentrating ability (relative '
                                                  'density)',
                                        'explanation': 'Urine specific gravity estimates the '
                                                       'density of urine relative to water and '
                                                       'reflects renal concentrating and diluting '
                                                       'ability. Refractometer or reagent-strip '
                                                       'methods are commonly used; osmolality is a '
                                                       'related but distinct measure. '
                                                       'Interpretation considers hydration status '
                                                       'and interfering large molecules.'},
                                       {'question': 'CSF tube order typically?',
                                        'options': ['A) All tubes pooled into one chemistry cup',
                                                    'B) Only the first tube used for all testing',
                                                    'C) Allocated to chemistry, microbiology, and '
                                                    'hematology per protocol',
                                                    'D) Random tube assignment without labeling'],
                                        'answer': 'C) Allocated to chemistry, microbiology, and '
                                                  'hematology per protocol',
                                        'explanation': 'CSF is typically collected into '
                                                       'sequentially numbered tubes allocated to '
                                                       'chemistry, microbiology, and hematology '
                                                       'per institutional protocol. Tube order '
                                                       'reduces blood-contamination effects on '
                                                       'selected tests. Clear labeling and prompt '
                                                       'delivery preserve analytic integrity.'}],
                              'medium': [{'question': 'RBC casts suggest?',
                                          'options': ['A) Lower-tract contamination without renal '
                                                      'disease',
                                                      'B) Only pyelonephritis with WBC casts '
                                                      'exclusively',
                                                      'C) Only nephrotic syndrome with fatty casts '
                                                      'exclusively',
                                                      'D) Glomerular bleeding/disease'],
                                          'answer': 'D) Glomerular bleeding/disease',
                                          'explanation': 'Red blood cell casts form when RBCs are '
                                                         'embedded in Tamm–Horsfall protein within '
                                                         'renal tubules and indicate glomerular '
                                                         'bleeding. They support diagnoses such as '
                                                         'glomerulonephritis. Careful microscopy '
                                                         'distinguishes true casts from look-alike '
                                                         'artifacts.'},
                                         {'question': 'Oval fat bodies associate with?',
                                          'options': ['A) Nephrotic-range proteinuria/lipiduria '
                                                      'themes',
                                                      'B) Isolated lower UTI without proteinuria',
                                                      'C) Acute cystitis with squamous cells only',
                                                      'D) Diabetes insipidus with dilute urine '
                                                      'only'],
                                          'answer': 'A) Nephrotic-range proteinuria/lipiduria '
                                                    'themes',
                                          'explanation': 'Oval fat bodies are renal tubular '
                                                         'epithelial cells or macrophages laden '
                                                         'with lipid, classically associated with '
                                                         'heavy proteinuria of nephrotic syndrome. '
                                                         'Polarized microscopy may show '
                                                         'Maltese-cross fat droplets. Correlation '
                                                         'with urine protein quantitation and '
                                                         'serum albumin supports the diagnosis.'},
                                         {'question': 'Synovial fluid crystals: needle, strong '
                                                      'negative birefringence?',
                                          'options': ['A) Calcium pyrophosphate (pseudogout) '
                                                      'rhomboids',
                                                      'B) Monosodium urate (gout)',
                                                      'C) Cholesterol plates from chronic '
                                                      'effusions only',
                                                      'D) Hydroxyapatite clumps without '
                                                      'birefringence only'],
                                          'answer': 'B) Monosodium urate (gout)',
                                          'explanation': 'Monosodium urate crystals of gout are '
                                                         'needle-shaped and show strong negative '
                                                         'birefringence under compensated '
                                                         'polarized light. Calcium pyrophosphate '
                                                         'crystals of pseudogout are typically '
                                                         'rhomboid/rod-shaped with weak positive '
                                                         'birefringence. Correct crystal ID '
                                                         'directs acute arthritis therapy.'}],
                              'hard': [{'question': 'Xanthochromia in CSF suggests?',
                                        'options': ['A) Only traumatic tap without pigment '
                                                    'evaluation',
                                                    'B) Only bacterial meningitis without '
                                                    'hemorrhage',
                                                    'C) Subarachnoid hemorrhage after excluding '
                                                    'artifact',
                                                    'D) Only viral PCR positivity without color '
                                                    'change'],
                                        'answer': 'C) Subarachnoid hemorrhage after excluding '
                                                  'artifact',
                                        'explanation': 'Xanthochromia is yellowish CSF '
                                                       'discoloration from bilirubin formed in '
                                                       'situ after subarachnoid hemorrhage, '
                                                       'appearing hours after onset. '
                                                       'Spectrophotometry and timing help '
                                                       'distinguish SAH from traumatic tap '
                                                       'artifact. Immediate clinical notification '
                                                       'is required when SAH is suspected.'},
                                       {'question': 'Myoglobin vs hemoglobin on dipstick?',
                                        'options': ['A) Dipstick distinguishes them by two '
                                                    'separate pads',
                                                    'B) Myoglobin never reacts with the blood pad',
                                                    'C) Hemoglobinuria always shows clear plasma '
                                                    'always',
                                                    'D) Both can read blood-positive; '
                                                    'plasma/clinical clues differ'],
                                        'answer': 'D) Both can read blood-positive; '
                                                  'plasma/clinical clues differ',
                                        'explanation': 'Dipstick blood pads cannot distinguish '
                                                       'myoglobin from hemoglobin because both '
                                                       'possess heme groups that catalyze the '
                                                       'indicator reaction. Clear plasma with '
                                                       'heme-positive urine suggests '
                                                       'myoglobinuria; pink/red plasma supports '
                                                       'hemoglobinuria. CK, clinical context, and '
                                                       'microscopy refine the distinction.'},
                                       {'question': 'Transudate vs exudate uses?',
                                        'options': ['A) Light’s criteria themes for pleural fluid',
                                                    'B) Only fluid color without chemistry '
                                                    'comparison',
                                                    'C) Only Gram stain without protein/LDH ratios',
                                                    'D) Only cell count without serum correlation'],
                                        'answer': 'A) Light’s criteria themes for pleural fluid',
                                        'explanation': 'Light’s criteria compare pleural fluid and '
                                                       'serum protein and LDH to classify '
                                                       'effusions as exudates or transudates. '
                                                       'Exudates suggest local pleural pathology; '
                                                       'transudates suggest systemic '
                                                       'hydrostatic/oncotic imbalance. Correct '
                                                       'classification focuses subsequent '
                                                       'workup.'}],
                              'extreme': [{'question': 'Body fluid cell counts on automated '
                                                       'analyzers need?',
                                           'options': ['A) No validation because blood modes '
                                                       'always transfer',
                                                       'B) Validation plus smear review for '
                                                       'atypical cells',
                                                       'C) Autorelease of blasts without '
                                                       'morphologic review',
                                                       'D) Replacement of all microbiology Gram '
                                                       'stains'],
                                           'answer': 'B) Validation plus smear review for atypical '
                                                     'cells',
                                           'explanation': 'Automated body-fluid cell counts '
                                                          'require method validation for each '
                                                          'fluid type because matrices differ from '
                                                          'blood. Smear review detects malignant '
                                                          'or atypical cells that counters alone '
                                                          'may misclassify. Flags and laboratory '
                                                          'policy define when manual counts and '
                                                          'pathologist review are required.'},
                                          {'question': 'Critical CSF findings require?',
                                           'options': ['A) Batch reporting with next morning '
                                                       'results',
                                                       'B) Chart release without verbal/read-back '
                                                       'alert',
                                                       'C) Immediate clinician notification',
                                                       'D) Notification only if culture later '
                                                       'turns positive'],
                                           'answer': 'C) Immediate clinician notification',
                                           'explanation': 'Critical CSF findings—such as organisms '
                                                          'on Gram stain, marked neutrophilic '
                                                          'pleocytosis, or xanthochromia '
                                                          'suggestive of SAH—require immediate '
                                                          'clinician notification. Delays can '
                                                          'worsen meningitis or neurosurgical '
                                                          'outcomes. Documentation of notification '
                                                          'is mandatory.'},
                                          {'question': 'Contaminated clean-catch clues?',
                                           'options': ['A) Pure single uropathogen ≥10^5 CFU/mL '
                                                       'without squamous cells',
                                                       'B) WBC casts with hematuria indicating '
                                                       'glomerulonephritis',
                                                       'C) Positive nitrite with few epithelial '
                                                       'cells only',
                                                       'D) Many squamous epithelial cells with '
                                                       'mixed flora'],
                                           'answer': 'D) Many squamous epithelial cells with mixed '
                                                     'flora',
                                           'explanation': 'Clean-catch midstream urine '
                                                          'contaminated by periurethral flora '
                                                          'often shows abundant squamous '
                                                          'epithelial cells and mixed organisms. '
                                                          'True UTI more often shows pyuria with a '
                                                          'predominant uropathogen. Recollection '
                                                          'with better technique may be needed '
                                                          'before treating mixed cultures.'}]},
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
        "🔬 *CharaNas MLS*\n"
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
