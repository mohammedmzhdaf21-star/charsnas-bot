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
                'questions': {'easy': [{'question': 'On a CBC, which red-cell index is most useful '
                                                    'for classifying anemia as microcytic, '
                                                    'normocytic, or macrocytic?',
                                        'options': ['A) Mean corpuscular volume (MCV)',
                                                    'B) Red-cell distribution width alone without '
                                                    'MCV',
                                                    'C) Absolute neutrophil count',
                                                    'D) Mean platelet volume'],
                                        'answer': 'A) Mean corpuscular volume (MCV)',
                                        'explanation': 'MCV reports average erythrocyte volume and '
                                                       'is the primary morphologic classifier for '
                                                       'anemia workups (microcytic, normocytic, or '
                                                       'macrocytic). RDW adds anisocytosis '
                                                       'information but does not replace MCV-based '
                                                       'classification. Leukocyte and platelet '
                                                       'indices address other lineages and do not '
                                                       'size red cells.',
                                        'choice_explanations': {'A': 'MCV is the average '
                                                                     'erythrocyte volume and is '
                                                                     'the standard CBC index used '
                                                                     'to classify anemia as '
                                                                     'microcytic, normocytic, or '
                                                                     'macrocytic before kinetic or '
                                                                     'etiology workup.',
                                                                'B': 'RDW quantifies anisocytosis '
                                                                     'and can support mixed '
                                                                     'deficiencies or early iron '
                                                                     'deficiency, but anemia '
                                                                     'morphologic class is defined '
                                                                     'by MCV, not RDW alone.',
                                                                'C': 'Absolute neutrophil count '
                                                                     'evaluates the granulocyte '
                                                                     'lineage for infection or '
                                                                     'marrow stress and does not '
                                                                     'classify red-cell size in '
                                                                     'anemia.',
                                                                'D': 'Mean platelet volume '
                                                                     'reflects platelet size and '
                                                                     'activation themes; it is '
                                                                     'unrelated to erythrocyte '
                                                                     'volume classification by '
                                                                     'MCV.'}},
                                       {'question': 'A peripheral blood smear is most '
                                                    'appropriately reviewed when the analyzer '
                                                    'flags which finding?',
                                        'options': ['A) Normal CBC without flags or clinical '
                                                    'concern',
                                                    'B) Suspected blasts, schistocytes, or '
                                                    'critical cytopenia flags',
                                                    'C) Only a slightly high MCHC within local '
                                                    'reference limits',
                                                    'D) Isolated mild eosinophilia with known '
                                                    'allergy and no flags'],
                                        'answer': 'B) Suspected blasts, schistocytes, or critical '
                                                  'cytopenia flags',
                                        'explanation': 'Instrument flags for blasts, fragmented '
                                                       'cells, platelet clumps, or critical '
                                                       'cytopenias trigger smear review because '
                                                       'morphology may change diagnosis and '
                                                       'urgency. Unflagged, clinically '
                                                       'uncomplicated CBCs usually do not require '
                                                       'smear. Mild isolated abnormalities within '
                                                       'policy may not mandate review.',
                                        'choice_explanations': {'A': 'A normal unflagged CBC '
                                                                     'without clinical concern '
                                                                     'does not require smear '
                                                                     'review; morphology review is '
                                                                     'reserved for flags, '
                                                                     'discrepancies, or clinical '
                                                                     'indications.',
                                                                'B': 'Flags suggesting blasts, '
                                                                     'schistocytes, clumping, or '
                                                                     'critical cytopenias warrant '
                                                                     'smear review because '
                                                                     'morphology can confirm '
                                                                     'life-threatening processes '
                                                                     'and guide urgent action.',
                                                                'C': 'A trivial MCHC shift within '
                                                                     'reference limits alone is '
                                                                     'not a classic smear trigger; '
                                                                     'review is driven by '
                                                                     'significant flags, deltas, '
                                                                     'or clinical urgency.',
                                                                'D': 'Mild eosinophilia with a '
                                                                     'known allergic context and '
                                                                     'no instrument flags is '
                                                                     'typically managed clinically '
                                                                     'without mandatory smear '
                                                                     'review.'}},
                                       {'question': 'Which specimen problem most commonly '
                                                    'invalidates a platelet count by causing '
                                                    'falsely low automated results?',
                                        'options': ['A) Properly mixed EDTA tube drawn without '
                                                    'delay',
                                                    'B) Arterial blood gas syringe analyzed for '
                                                    'gases only',
                                                    'C) EDTA-dependent platelet clumping '
                                                    '(pseudothrombocytopenia)',
                                                    'D) Mild lipemia that does not affect '
                                                    'impedance counting'],
                                        'answer': 'C) EDTA-dependent platelet clumping '
                                                  '(pseudothrombocytopenia)',
                                        'explanation': 'EDTA-dependent antibodies can aggregate '
                                                       'platelets in vitro, so the analyzer '
                                                       'undercounts free platelets and reports '
                                                       'spurious thrombocytopenia. Smear review '
                                                       'shows clumps, and recounting in citrate or '
                                                       'another anticoagulant usually corrects the '
                                                       'count. True thrombocytopenia lacks this '
                                                       'artifact pattern.',
                                        'choice_explanations': {'A': 'A promptly mixed EDTA '
                                                                     'specimen is the standard CBC '
                                                                     'anticoagulant and does not '
                                                                     'by itself create '
                                                                     'pseudothrombocytopenia.',
                                                                'B': 'ABG syringes are for '
                                                                     'blood-gas analysis; they are '
                                                                     'not the usual mechanism of '
                                                                     'EDTA-clump '
                                                                     'pseudothrombocytopenia on '
                                                                     'hematology analyzers.',
                                                                'C': 'EDTA-dependent platelet '
                                                                     'agglutination causes '
                                                                     'in-vitro clumping, falsely '
                                                                     'low automated platelet '
                                                                     'counts, and visible '
                                                                     'aggregates on smear—classic '
                                                                     'pseudothrombocytopenia.',
                                                                'D': 'Mild lipemia may interfere '
                                                                     'with some optical assays but '
                                                                     'is not the classic cause of '
                                                                     'EDTA-clump–related falsely '
                                                                     'low platelet counts.'}}],
                              'medium': [{'question': 'A smear shows numerous schistocytes with '
                                                      'elevated LDH and low haptoglobin. Which '
                                                      'pathophysiologic process is most strongly '
                                                      'supported?',
                                          'options': ['A) Pure megaloblastic maturation without '
                                                      'fragmentation',
                                                      'B) Iron deficiency with pencil cells only',
                                                      'C) Hereditary spherocytosis without '
                                                      'microvascular shear',
                                                      'D) Microangiopathic hemolytic anemia '
                                                      '(mechanical RBC fragmentation)'],
                                          'answer': 'D) Microangiopathic hemolytic anemia '
                                                    '(mechanical RBC fragmentation)',
                                          'explanation': 'Schistocytes form when erythrocytes are '
                                                         'sheared by fibrin strands or abnormal '
                                                         'microvasculature. Paired with '
                                                         'biochemical hemolysis markers, they '
                                                         'support MAHA (TTP, HUS, DIC, mechanical '
                                                         'valves). Megaloblastic, iron-deficiency, '
                                                         'and membrane-defect patterns produce '
                                                         'other morphologies.',
                                          'choice_explanations': {'A': 'Megaloblastic anemia '
                                                                       'yields macro-ovalocytes '
                                                                       'and hypersegmented '
                                                                       'neutrophils from impaired '
                                                                       'DNA synthesis, not '
                                                                       'fibrin-shear schistocytes.',
                                                                  'B': 'Iron deficiency '
                                                                       'classically shows '
                                                                       'hypochromic microcytes and '
                                                                       'pencil cells from '
                                                                       'inadequate hemoglobin '
                                                                       'synthesis, not mechanical '
                                                                       'fragments.',
                                                                  'C': 'Hereditary spherocytosis '
                                                                       'produces dense spherocytes '
                                                                       'from membrane–cytoskeleton '
                                                                       'defects with extravascular '
                                                                       'hemolysis, not MAHA '
                                                                       'fragments.',
                                                                  'D': 'Schistocytes plus '
                                                                       'intravascular hemolysis '
                                                                       'markers indicate '
                                                                       'mechanical RBC shearing in '
                                                                       'microangiopathic hemolytic '
                                                                       'anemia.'}},
                                         {'question': 'Which coagulation test is the primary '
                                                      'standardized monitor for warfarin’s effect '
                                                      'on the extrinsic/common pathway?',
                                          'options': ['A) Prothrombin time reported as INR',
                                                      'B) Bleeding time for primary hemostasis '
                                                      'only',
                                                      'C) D-dimer as a fibrinolysis screen alone',
                                                      'D) Mixing study without a baseline PT/INR'],
                                          'answer': 'A) Prothrombin time reported as INR',
                                          'explanation': 'Warfarin inhibits vitamin K–dependent '
                                                         'factors (II, VII, IX, X). PT/INR '
                                                         'standardizes thromboplastin variability '
                                                         'and is used to monitor therapy against '
                                                         'indication-specific targets. Bleeding '
                                                         'time, D-dimer, and mixing studies answer '
                                                         'different hemostasis questions.',
                                          'choice_explanations': {'A': 'INR standardizes PT across '
                                                                       'reagents and monitors '
                                                                       'warfarin’s effect on the '
                                                                       'extrinsic and common '
                                                                       'pathways against '
                                                                       'therapeutic targets.',
                                                                  'B': 'Bleeding time assesses '
                                                                       'primary hemostasis '
                                                                       '(platelets/vessel wall) '
                                                                       'and does not monitor '
                                                                       'vitamin K–antagonist '
                                                                       'effect.',
                                                                  'C': 'D-dimer reflects fibrin '
                                                                       'degradation and screens '
                                                                       'thrombosis/fibrinolysis; '
                                                                       'it is not the warfarin '
                                                                       'monitoring assay.',
                                                                  'D': 'Mixing studies evaluate '
                                                                       'inhibitor versus factor '
                                                                       'deficiency after an '
                                                                       'abnormal PT/aPTT; they do '
                                                                       'not replace INR monitoring '
                                                                       'of warfarin.'}},
                                         {'question': 'A “left shift” on the leukocyte '
                                                      'differential most accurately means which '
                                                      'finding?',
                                          'options': ['A) Absolute basophilia without neutrophil '
                                                      'precursors',
                                                      'B) Increased circulating immature '
                                                      'neutrophils (e.g., bands)',
                                                      'C) Isolated lymphocytosis of viral illness '
                                                      'only',
                                                      'D) Eosinophilia from parasitic infection '
                                                      'alone'],
                                          'answer': 'B) Increased circulating immature neutrophils '
                                                    '(e.g., bands)',
                                          'explanation': 'Left shift denotes accelerated marrow '
                                                         'release of immature neutrophils such as '
                                                         'bands (and sometimes earlier forms) '
                                                         'during infection, inflammation, or '
                                                         'stress. Other lineage expansions are '
                                                         'described by their own terms and do not '
                                                         'define a neutrophil left shift.',
                                          'choice_explanations': {'A': 'Basophilia is a separate '
                                                                       'lineage finding and does '
                                                                       'not constitute a '
                                                                       'neutrophil left shift.',
                                                                  'B': 'Left shift means increased '
                                                                       'immature neutrophilic '
                                                                       'forms in circulation, '
                                                                       'typically bands, from '
                                                                       'accelerated marrow '
                                                                       'release.',
                                                                  'C': 'Lymphocytosis expands '
                                                                       'lymphocytes and may '
                                                                       'suggest viral processes; '
                                                                       'it is not the definition '
                                                                       'of a neutrophil left '
                                                                       'shift.',
                                                                  'D': 'Eosinophilia has '
                                                                       'allergic/parasitic '
                                                                       'associations and is '
                                                                       'distinct from '
                                                                       'immature-neutrophil left '
                                                                       'shift.'}}],
                              'hard': [{'question': 'A hospitalized patient on unfractionated '
                                                    'heparin has a >50% platelet-count fall by day '
                                                    '7 and a new lower-extremity arterial '
                                                    'thrombus. Which laboratory/clinical '
                                                    'interpretation is most appropriate?',
                                        'options': ['A) EDTA clumping only — ignore thrombosis '
                                                    'risk',
                                                    'B) Expected dilutional thrombocytopenia '
                                                    'without immune mechanism',
                                                    'C) Suspect HIT: stop heparin and pursue HIT '
                                                    'pathway testing/alternative anticoagulation',
                                                    'D) Primary ITP unrelated to heparin exposure '
                                                    'timing'],
                                        'answer': 'C) Suspect HIT: stop heparin and pursue HIT '
                                                  'pathway testing/alternative anticoagulation',
                                        'explanation': 'HIT is an immune PF4/heparin antibody '
                                                       'syndrome causing thrombocytopenia with '
                                                       'high arterial/venous thrombosis risk, '
                                                       'typically after several days of heparin '
                                                       '(sooner if re-exposed). Management is '
                                                       'immediate heparin cessation and '
                                                       'alternative anticoagulation while '
                                                       'confirming with immunoassay ± functional '
                                                       'assay—not platelet transfusion as first '
                                                       'reflex.',
                                        'choice_explanations': {'A': 'EDTA clumping causes '
                                                                     'pseudothrombocytopenia '
                                                                     'without new arterial '
                                                                     'thrombosis; thrombosis plus '
                                                                     'timed platelet fall points '
                                                                     'to HIT, not artifact alone.',
                                                                'B': 'Simple dilution or nonimmune '
                                                                     'heparin effects lack the '
                                                                     'antibody-driven thrombotic '
                                                                     'phenotype of clinical HIT.',
                                                                'C': 'Timed platelet drop after '
                                                                     'heparin plus new thrombosis '
                                                                     'is classic HIT; stop '
                                                                     'heparin, avoid warfarin '
                                                                     'alone early, use alternative '
                                                                     'anticoagulation, and confirm '
                                                                     'with HIT assays.',
                                                                'D': 'ITP is immune '
                                                                     'thrombocytopenia without the '
                                                                     'heparin–PF4 timing and '
                                                                     'paradoxical thrombosis that '
                                                                     'define HIT.'}},
                                       {'question': 'Blasts on smear with Auer rods are identified '
                                                    'in a young adult with DIC. Which next '
                                                    'laboratory concept is most critical while '
                                                    'arranging urgent therapy?',
                                        'options': ['A) Treat as iron deficiency and delay lineage '
                                                    'studies',
                                                    'B) Assume CLL based on age alone without '
                                                    'markers',
                                                    'C) Report as reactive left shift without '
                                                    'hematopathology review',
                                                    'D) Suspect APL (APML): urgent '
                                                    'genetics/PML::RARA pathway and coagulopathy '
                                                    'management'],
                                        'answer': 'D) Suspect APL (APML): urgent '
                                                  'genetics/PML::RARA pathway and coagulopathy '
                                                  'management',
                                        'explanation': 'Auer rods mark myeloid blasts; in the '
                                                       'setting of DIC they raise strong concern '
                                                       'for acute promyelocytic leukemia (APL). '
                                                       'APL requires immediate ATRA-based therapy '
                                                       'and aggressive coagulopathy support while '
                                                       'confirming PML::RARA. Delays markedly '
                                                       'increase early hemorrhagic death.',
                                        'choice_explanations': {'A': 'Iron deficiency does not '
                                                                     'produce Auer-rod blasts or '
                                                                     'DIC; delaying leukemia '
                                                                     'workup is dangerous.',
                                                                'B': 'CLL is a mature B-cell '
                                                                     'neoplasm of older adults and '
                                                                     'does not present with Auer '
                                                                     'rods and APL-type DIC.',
                                                                'C': 'Auer rods indicate '
                                                                     'neoplastic myeloid blasts, '
                                                                     'not a simple reactive left '
                                                                     'shift; urgent '
                                                                     'hematopathology review is '
                                                                     'required.',
                                                                'D': 'Auer-rod myeloid blasts plus '
                                                                     'DIC suggest APL; initiate '
                                                                     'urgent ATRA pathway care and '
                                                                     'confirm PML::RARA while '
                                                                     'managing coagulopathy.'}},
                                       {'question': 'Flow cytometry is ordered on marrow after '
                                                    'induction chemotherapy for ALL. What is the '
                                                    'primary purpose of an MRD assay in this '
                                                    'context?',
                                        'options': ['A) Detect residual leukemic cells below '
                                                    'morphologic remission thresholds',
                                                    'B) Replace ABO typing before any future '
                                                    'transfusion',
                                                    'C) Measure serum ferritin as a surrogate for '
                                                    'blast burden',
                                                    'D) Monitor INR for asparaginase-related '
                                                    'coagulopathy only'],
                                        'answer': 'A) Detect residual leukemic cells below '
                                                  'morphologic remission thresholds',
                                        'explanation': 'MRD by multiparameter flow (or molecular '
                                                       'methods) finds leukemia-associated '
                                                       'immunophenotypes at levels far below 5% '
                                                       'morphologic blasts. Result depth informs '
                                                       'consolidation intensity and relapse risk. '
                                                       'It does not replace transfusion typing or '
                                                       'chemistry/coagulation monitoring.',
                                        'choice_explanations': {'A': 'MRD assays detect persistent '
                                                                     'leukemic cells below '
                                                                     'morphologic remission using '
                                                                     'aberrant phenotypes or '
                                                                     'molecular targets, guiding '
                                                                     'risk-adapted therapy.',
                                                                'B': 'ABO/Rh typing is a '
                                                                     'blood-bank identity assay '
                                                                     'and is independent of '
                                                                     'leukemic MRD measurement.',
                                                                'C': 'Ferritin reflects iron '
                                                                     'stores/inflammation and is '
                                                                     'not a validated surrogate '
                                                                     'for multiparameter MRD '
                                                                     'quantification.',
                                                                'D': 'INR monitors coagulation; '
                                                                     'asparaginase toxicity is a '
                                                                     'separate issue from '
                                                                     'flow-cytometric MRD of '
                                                                     'residual blasts.'}}],
                              'extreme': [{'question': 'A 28-year-old woman presents with '
                                                       'fluctuating neurologic deficits, '
                                                       'petechiae, Hb 8.4 g/dL, platelets 19 × '
                                                       '10⁹/L, numerous schistocytes, markedly '
                                                       'elevated LDH, and undetectable '
                                                       'haptoglobin. PT/aPTT and fibrinogen are '
                                                       'near normal with only mildly increased '
                                                       'D-dimer, and creatinine is 1.3 mg/dL. '
                                                       'Which interpretation best distinguishes '
                                                       'the leading diagnosis and immediate '
                                                       'laboratory/therapeutic priority?',
                                           'options': ['A) ITP alone — isolated immune platelet '
                                                       'destruction without MAHA, observe only',
                                                       'B) TTP (severe ADAMTS13 deficiency '
                                                       'phenotype): prioritize urgent plasma '
                                                       'exchange pathway over treating as DIC',
                                                       'C) Classic DIC — expect profoundly '
                                                       'prolonged PT/aPTT and low fibrinogen as '
                                                       'the dominant pattern',
                                                       'D) Isolated iron-deficiency anemia — '
                                                       'schistocytes are expected pencil-cell '
                                                       'equivalents'],
                                           'answer': 'B) TTP (severe ADAMTS13 deficiency '
                                                     'phenotype): prioritize urgent plasma '
                                                     'exchange pathway over treating as DIC',
                                           'explanation': 'MAHA plus thrombocytopenia with '
                                                          'relatively preserved coagulation '
                                                          'factors favors TTP (ADAMTS13 '
                                                          'deficiency) over DIC, which typically '
                                                          'prolongs PT/aPTT and consumes '
                                                          'fibrinogen. ITP lacks schistocytic '
                                                          'hemolysis. Urgent plasma exchange is '
                                                          'disease-modifying in TTP while ADAMTS13 '
                                                          'confirmation is pending; mislabeling as '
                                                          'DIC or ITP delays therapy.',
                                           'choice_explanations': {'A': 'ITP causes '
                                                                        'thrombocytopenia without '
                                                                        'microangiopathic '
                                                                        'hemolysis; schistocytes '
                                                                        'and marked '
                                                                        'LDH/haptoglobin changes '
                                                                        'argue strongly against '
                                                                        'isolated ITP.',
                                                                   'B': 'Preserved '
                                                                        'PT/aPTT/fibrinogen with '
                                                                        'MAHA and severe '
                                                                        'thrombocytopenia is the '
                                                                        'classic TTP pattern; '
                                                                        'urgent plasma exchange is '
                                                                        'the priority while '
                                                                        'ADAMTS13 is pending.',
                                                                   'C': 'DIC usually shows '
                                                                        'coagulopathy with '
                                                                        'prolonged PT/aPTT, low '
                                                                        'fibrinogen, and higher '
                                                                        'D-dimer; near-normal coag '
                                                                        'studies push the '
                                                                        'differential toward TTP.',
                                                                   'D': 'Iron deficiency produces '
                                                                        'hypochromic '
                                                                        'microcytes/pencil cells, '
                                                                        'not schistocytic MAHA '
                                                                        'with consumptive '
                                                                        'thrombocytopenia.'}},
                                          {'question': 'A patient develops acute dyspnea and '
                                                       'hypoxemia during RBC transfusion. BP is '
                                                       'low, fever is present, and chest '
                                                       'radiograph shows bilateral infiltrates. '
                                                       'BNP is not elevated and JVP is normal. '
                                                       'Pretransfusion sample clerical check is '
                                                       'correct, and the direct antiglobulin test '
                                                       'is negative. Which laboratory–clinical '
                                                       'synthesis is most accurate?',
                                           'options': ['A) TACO — hydrostatic overload with '
                                                       'hypertension and high BNP as the best fit',
                                                       'B) Acute hemolytic transfusion reaction — '
                                                       'expect hemoglobinemia and positive DAT '
                                                       'typically',
                                                       'C) TRALI — permeability '
                                                       'edema/inflammation; stop transfusion, '
                                                       'support respiration, report to blood bank',
                                                       'D) Febrile non-hemolytic reaction only — '
                                                       'ignore pulmonary findings'],
                                           'answer': 'C) TRALI — permeability edema/inflammation; '
                                                     'stop transfusion, support respiration, '
                                                     'report to blood bank',
                                           'explanation': 'TRALI presents with acute hypoxemic '
                                                          'respiratory distress and bilateral '
                                                          'infiltrates during/soon after '
                                                          'transfusion, often with fever and '
                                                          'hypotension, without evidence of '
                                                          'circulatory overload. TACO instead '
                                                          'shows hydrostatic edema, hypertension, '
                                                          'and elevated BNP. AHTR shows hemolysis '
                                                          'markers and usually ABO incompatibility '
                                                          'clues. All suspected TRALI events '
                                                          'require transfusion cessation, '
                                                          'supportive care, and blood-bank '
                                                          'reporting for donor lookback.',
                                           'choice_explanations': {'A': 'TACO is volume-overload '
                                                                        'edema with hypertension, '
                                                                        'raised filling pressures, '
                                                                        'and elevated BNP—opposite '
                                                                        'to this hypotensive, '
                                                                        'normal-BNP picture.',
                                                                   'B': 'Acute hemolytic reactions '
                                                                        'feature hemolysis '
                                                                        'evidence '
                                                                        '(hemoglobinemia/uria, '
                                                                        'bilirubin rise) and often '
                                                                        'DAT positivity with '
                                                                        'clerical ABO errors; '
                                                                        'those are absent here.',
                                                                   'C': 'Hypoxemia, bilateral '
                                                                        'infiltrates, '
                                                                        'fever/hypotension without '
                                                                        'overload markers fit '
                                                                        'TRALI; stop transfusion, '
                                                                        'support oxygenation, and '
                                                                        'notify the blood bank.',
                                                                   'D': 'Isolated febrile '
                                                                        'non-hemolytic reactions '
                                                                        'lack acute bilateral '
                                                                        'permeability edema; '
                                                                        'pulmonary failure '
                                                                        'requires TRALI/TACO '
                                                                        'evaluation.'}},
                                          {'question': 'An oncology patient has pancytopenia. '
                                                       'Marrow shows 40% blasts. Cytochemistry is '
                                                       'nonspecific. Which integrated approach '
                                                       'best distinguishes AML from ALL for '
                                                       'treatment planning?',
                                           'options': ['A) Use patient age alone without '
                                                       'immunophenotyping',
                                                       'B) Rely solely on hemoglobin concentration '
                                                       'to assign lineage',
                                                       'C) Treat empirically as iron deficiency '
                                                       'until blasts disappear',
                                                       'D) Integrate morphology with '
                                                       'multiparameter immunophenotyping and '
                                                       'genetic studies (WHO/ICC framework)'],
                                           'answer': 'D) Integrate morphology with multiparameter '
                                                     'immunophenotyping and genetic studies '
                                                     '(WHO/ICC framework)',
                                           'explanation': 'Acute leukemia lineage cannot be '
                                                          'assigned by age or anemia severity. '
                                                          'Standard practice combines blast '
                                                          'morphology, cytochemistry when used, '
                                                          'flow immunophenotyping, and '
                                                          'cytogenetic/molecular studies under '
                                                          'WHO/ICC classification. Lineage and '
                                                          'genetics drive induction choice and '
                                                          'risk stratification.',
                                           'choice_explanations': {'A': 'Age shifts pretest '
                                                                        'probability but cannot '
                                                                        'prove myeloid versus '
                                                                        'lymphoid lineage without '
                                                                        'marker/genetic data.',
                                                                   'B': 'Hemoglobin reflects '
                                                                        'anemia severity, not '
                                                                        'blast lineage identity.',
                                                                   'C': 'Iron deficiency is '
                                                                        'irrelevant to a marrow '
                                                                        'with 40% blasts; delaying '
                                                                        'leukemia classification '
                                                                        'is unsafe.',
                                                                   'D': 'Definitive AML vs ALL '
                                                                        'distinction uses '
                                                                        'morphology plus '
                                                                        'immunophenotype and '
                                                                        'genetics within modern '
                                                                        'classification '
                                                                        'systems.'}}]},
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
                        'questions': {'easy': [{'question': 'Which analytes are included in a '
                                                            'routine basic electrolyte panel on '
                                                            'most chemistry analyzers?',
                                                'options': ['A) Sodium, potassium, chloride, and '
                                                            'bicarbonate (total CO2)',
                                                            'B) Troponin I only without '
                                                            'electrolytes',
                                                            'C) Hemoglobin A1c as the sole '
                                                            'electrolyte surrogate',
                                                            'D) Blood culture bottles incubated '
                                                            'for growth'],
                                                'answer': 'A) Sodium, potassium, chloride, and '
                                                          'bicarbonate (total CO2)',
                                                'explanation': 'The basic electrolyte panel '
                                                               'quantifies Na, K, Cl, and HCO3 '
                                                               '(often as total CO2) to assess '
                                                               'fluid, acid–base, and membrane '
                                                               'potential status. Cardiac markers, '
                                                               'A1c, and cultures address other '
                                                               'clinical questions and are not '
                                                               'electrolyte panel components.',
                                                'choice_explanations': {'A': 'Routine electrolyte '
                                                                             'panels measure Na, '
                                                                             'K, Cl, and '
                                                                             'bicarbonate/total '
                                                                             'CO2, the core ions '
                                                                             'for hydration and '
                                                                             'acid–base '
                                                                             'interpretation.',
                                                                        'B': 'Troponin is a '
                                                                             'cardiac injury '
                                                                             'marker assayed '
                                                                             'separately from the '
                                                                             'electrolyte panel.',
                                                                        'C': 'HbA1c reflects '
                                                                             'average glycemia '
                                                                             'over weeks to months '
                                                                             'and is not an '
                                                                             'electrolyte.',
                                                                        'D': 'Blood cultures '
                                                                             'detect bacteremia '
                                                                             'microbiologically '
                                                                             'and are unrelated to '
                                                                             'chemistry '
                                                                             'electrolyte '
                                                                             'measurement.'}},
                                               {'question': 'Why must grossly hemolyzed potassium '
                                                            'specimens usually be rejected or '
                                                            'redrawn rather than reported as '
                                                            'patient hyperkalemia?',
                                                'options': ['A) Hemolysis has no effect on '
                                                            'measured potassium',
                                                            'B) RBC lysis releases intracellular '
                                                            'K+, falsely elevating serum/plasma '
                                                            'potassium',
                                                            'C) Hemolysis only lowers potassium by '
                                                            'dilution always',
                                                            'D) Hemolysis uniquely validates '
                                                            'critical hyperkalemia without '
                                                            'clinical review'],
                                                'answer': 'B) RBC lysis releases intracellular K+, '
                                                          'falsely elevating serum/plasma '
                                                          'potassium',
                                                'explanation': 'Erythrocytes contain high '
                                                               'potassium; in-vitro hemolysis '
                                                               'spills K+ into the specimen and '
                                                               'mimics pathologic hyperkalemia. '
                                                               'Labs reject or qualify hemolyzed '
                                                               'K+ results and request '
                                                               'recollection when clinically '
                                                               'appropriate, correlating with ECG '
                                                               'and prior values.',
                                                'choice_explanations': {'A': 'Hemolysis '
                                                                             'substantially '
                                                                             'elevates measured '
                                                                             'potassium; claiming '
                                                                             'no effect is '
                                                                             'analytically '
                                                                             'incorrect.',
                                                                        'B': 'Intracellular '
                                                                             'potassium released '
                                                                             'by RBC lysis falsely '
                                                                             'raises the reported '
                                                                             'K+, a classic '
                                                                             'preanalytic '
                                                                             'interference '
                                                                             'requiring '
                                                                             'rejection/redraw '
                                                                             'policies.',
                                                                        'C': 'Hemolysis does not '
                                                                             'systematically lower '
                                                                             'potassium; the '
                                                                             'dominant bias for K+ '
                                                                             'is false elevation.',
                                                                        'D': 'Hemolyzed “critical” '
                                                                             'K+ is often '
                                                                             'artifactual; it must '
                                                                             'not be treated as '
                                                                             'confirmed in vivo '
                                                                             'hyperkalemia without '
                                                                             'verification.'}},
                                               {'question': 'Serum creatinine is used clinically '
                                                            'primarily as a marker of which '
                                                            'physiologic function (with '
                                                            'acknowledged muscle-mass '
                                                            'limitations)?',
                                                'options': ['A) Pancreatic exocrine enzyme output '
                                                            'only',
                                                            'B) Pulmonary gas exchange efficiency',
                                                            'C) Glomerular filtration rate '
                                                            'approximation',
                                                            'D) Bone marrow erythropoietic rate '
                                                            'alone'],
                                                'answer': 'C) Glomerular filtration rate '
                                                          'approximation',
                                                'explanation': 'Creatinine is filtered by '
                                                               'glomeruli (with minor secretion). '
                                                               'Rising serum creatinine and '
                                                               'falling eGFR estimate reduced GFR, '
                                                               'though muscle mass, diet, and some '
                                                               'drugs alter interpretation. It is '
                                                               'not a pancreas, lung, or marrow '
                                                               'function test.',
                                                'choice_explanations': {'A': 'Pancreatic exocrine '
                                                                             'function is assessed '
                                                                             'with enzymes such as '
                                                                             'lipase/amylase or '
                                                                             'fecal elastase, not '
                                                                             'creatinine.',
                                                                        'B': 'Gas exchange is '
                                                                             'evaluated by blood '
                                                                             'gases and oximetry, '
                                                                             'not creatinine.',
                                                                        'C': 'Creatinine (and eGFR '
                                                                             'equations) '
                                                                             'approximate GFR for '
                                                                             'chronic kidney '
                                                                             'disease staging, '
                                                                             'with caveats for '
                                                                             'muscle mass and '
                                                                             'non-GFR '
                                                                             'determinants.',
                                                                        'D': 'Erythropoiesis is '
                                                                             'reflected by '
                                                                             'CBC/reticulocyte '
                                                                             'data, not serum '
                                                                             'creatinine.'}}],
                                      'medium': [{'question': 'A chemistry panel shows AST and ALT '
                                                              'many times the upper limit with '
                                                              'only mild ALP elevation. Which '
                                                              'injury pattern is most consistent?',
                                                  'options': ['A) Pure bone ALP induction without '
                                                              'hepatocyte injury',
                                                              'B) Isolated hemolysis explaining '
                                                              'both AST and ALT equally always',
                                                              'C) Extrahepatic biliary obstruction '
                                                              'as the sole pattern',
                                                              'D) Hepatocellular injury pattern'],
                                                  'answer': 'D) Hepatocellular injury pattern',
                                                  'explanation': 'Marked aminotransferase '
                                                                 'elevation with comparatively '
                                                                 'modest ALP suggests '
                                                                 'hepatocellular injury (viral '
                                                                 'hepatitis, toxins, ischemia). '
                                                                 'Cholestatic patterns reverse '
                                                                 'that ratio. Hemolysis can raise '
                                                                 'AST more than ALT but does not '
                                                                 'define the classic hepatitis '
                                                                 'pattern alone.',
                                                  'choice_explanations': {'A': 'Bone-source ALP '
                                                                               'elevation is a '
                                                                               'cholestatic/infiltrative '
                                                                               'or bone-turnover '
                                                                               'theme, not '
                                                                               'aminotransferase-dominant '
                                                                               'hepatitis.',
                                                                          'B': 'Hemolysis may '
                                                                               'increase AST, but '
                                                                               'concurrent marked '
                                                                               'ALT usually '
                                                                               'indicates '
                                                                               'hepatocyte injury '
                                                                               'rather than '
                                                                               'hemolysis alone.',
                                                                          'C': 'Extrahepatic '
                                                                               'obstruction '
                                                                               'typically elevates '
                                                                               'ALP/GGT out of '
                                                                               'proportion to '
                                                                               'AST/ALT.',
                                                                          'D': 'AST/ALT-predominant '
                                                                               'enzyme rises '
                                                                               'indicate '
                                                                               'hepatocellular '
                                                                               'injury patterns on '
                                                                               'liver panels.'}},
                                                 {'question': 'High-sensitivity troponin is '
                                                              'elevated in a patient with chest '
                                                              'pain. What does a rising/falling '
                                                              'troponin pattern most specifically '
                                                              'support among the listed options?',
                                                  'options': ['A) Acute myocardial injury '
                                                              '(interpret with clinical ischemic '
                                                              'context)',
                                                              'B) Guaranteed stable angina without '
                                                              'plaque events',
                                                              'C) Proof of pulmonary embolism '
                                                              'exclusive of cardiac injury',
                                                              'D) Normal skeletal muscle strain as '
                                                              'the only cause always'],
                                                  'answer': 'A) Acute myocardial injury (interpret '
                                                            'with clinical ischemic context)',
                                                  'explanation': 'Troponin is a cardiomyocyte '
                                                                 'structural protein; a '
                                                                 'rising/falling pattern indicates '
                                                                 'acute myocardial injury. MI '
                                                                 'diagnosis still requires '
                                                                 'ischemic clinical/ECG context '
                                                                 'because non-ACS injury '
                                                                 '(myocarditis, PE strain, renal '
                                                                 'disease baselines) can elevate '
                                                                 'troponin.',
                                                  'choice_explanations': {'A': 'Dynamic troponin '
                                                                               'change marks acute '
                                                                               'myocardial injury '
                                                                               'and, with ischemic '
                                                                               'features, supports '
                                                                               'MI; context '
                                                                               'distinguishes type '
                                                                               '1 vs other injury.',
                                                                          'B': 'Stable angina '
                                                                               'without acute '
                                                                               'plaque rupture '
                                                                               'typically lacks a '
                                                                               'rising/falling '
                                                                               'troponin injury '
                                                                               'curve.',
                                                                          'C': 'PE may raise '
                                                                               'troponin via '
                                                                               'right-heart strain '
                                                                               'but is not proven '
                                                                               'by troponin alone '
                                                                               'nor exclusive of '
                                                                               'myocardial injury '
                                                                               'mechanisms.',
                                                                          'D': 'Contemporary '
                                                                               'cardiac troponin '
                                                                               'assays are highly '
                                                                               'cardiac-specific; '
                                                                               'skeletal strain is '
                                                                               'not the usual '
                                                                               'explanation for '
                                                                               'hs-cTn rises.'}},
                                                 {'question': 'HbA1c most closely estimates which '
                                                              'glycemic concept when '
                                                              'hemoglobinopathy and altered RBC '
                                                              'turnover are absent?',
                                                  'options': ['A) Instantaneous capillary glucose '
                                                              'at the moment of phlebotomy only',
                                                              'B) Average glycemia over '
                                                              'approximately the prior 2–3 months',
                                                              'C) Postprandial spike exclusive of '
                                                              'fasting glycemia',
                                                              'D) Urinary glucose threshold '
                                                              'independent of plasma glucose'],
                                                  'answer': 'B) Average glycemia over '
                                                            'approximately the prior 2–3 months',
                                                  'explanation': 'HbA1c reflects nonenzymatic '
                                                                 'glycation of hemoglobin over the '
                                                                 'erythrocyte lifespan (~120 '
                                                                 'days), approximating 2–3 month '
                                                                 'mean glucose. It is not a '
                                                                 'point-of-care instantaneous '
                                                                 'glucose and can be misleading '
                                                                 'with hemoglobin variants or '
                                                                 'altered RBC survival.',
                                                  'choice_explanations': {'A': 'Point glucose '
                                                                               'measures current '
                                                                               'glycemia; A1c '
                                                                               'integrates '
                                                                               'longer-term '
                                                                               'exposure.',
                                                                          'B': 'A1c estimates mean '
                                                                               'glycemia over '
                                                                               'roughly 2–3 months '
                                                                               'when RBC lifespan '
                                                                               'is normal.',
                                                                          'C': 'A1c averages '
                                                                               'fasting and '
                                                                               'postprandial '
                                                                               'contributions '
                                                                               'rather than '
                                                                               'isolating '
                                                                               'postprandial '
                                                                               'spikes.',
                                                                          'D': 'Urine glucose '
                                                                               'depends on renal '
                                                                               'threshold and does '
                                                                               'not replace A1c '
                                                                               'for average '
                                                                               'glycemia.'}}],
                                      'hard': [{'question': 'Measured osmolality is 320 mOsm/kg '
                                                            'while calculated osmolarity is 290 '
                                                            'mOsm/L in a comatose patient. Which '
                                                            'interpretation is most appropriate?',
                                                'options': ['A) Laboratory error only — ignore '
                                                            'osmolar gap',
                                                            'B) Mandatory diabetes insipidus '
                                                            'without toxin consideration',
                                                            'C) Elevated osmolar gap suggesting '
                                                            'unmeasured osmotically active solutes '
                                                            '(e.g., alcohols)',
                                                            'D) Pure hypernatremia explaining the '
                                                            'entire gap always'],
                                                'answer': 'C) Elevated osmolar gap suggesting '
                                                          'unmeasured osmotically active solutes '
                                                          '(e.g., alcohols)',
                                                'explanation': 'Osmolar gap = measured − '
                                                               'calculated osmolarity. A large gap '
                                                               'implies osmotically active '
                                                               'substances not in the calculation '
                                                               '(ethanol, methanol, ethylene '
                                                               'glycol, isopropanol, etc.). '
                                                               'Clinical toxicology correlation '
                                                               'and specific assays follow; gap '
                                                               'alone does not name the toxin.',
                                                'choice_explanations': {'A': 'A 30 mOsm gap is '
                                                                             'clinically '
                                                                             'meaningful and '
                                                                             'should not be '
                                                                             'dismissed as trivial '
                                                                             'error without '
                                                                             'investigation.',
                                                                        'B': 'Diabetes insipidus '
                                                                             'affects water '
                                                                             'balance/sodium but '
                                                                             'does not by itself '
                                                                             'create a classic '
                                                                             'toxic alcohol '
                                                                             'osmolar gap pattern.',
                                                                        'C': 'A substantial '
                                                                             'osmolar gap points '
                                                                             'to unmeasured '
                                                                             'osmoles such as '
                                                                             'toxic alcohols '
                                                                             'pending specific '
                                                                             'confirmation.',
                                                                        'D': 'Sodium is included '
                                                                             'in calculated '
                                                                             'osmolarity; '
                                                                             'hypernatremia raises '
                                                                             'both measured and '
                                                                             'calculated values '
                                                                             'and does not solely '
                                                                             'create a large '
                                                                             'gap.'}},
                                               {'question': 'A sandwich immunoassay for a tumor '
                                                            'marker reports a near-normal value, '
                                                            'yet the clinician suspects massive '
                                                            'marker elevation and imaging is '
                                                            'discordant. Dilution yields a much '
                                                            'higher result. What analytic '
                                                            'phenomenon is most likely?',
                                                'options': ['A) Simple reagent underloading '
                                                            'unrelated to antigen excess',
                                                            'B) Icterus specifically destroying '
                                                            'only the calibrator curve',
                                                            'C) Random mislabeling that dilution '
                                                            'coincidentally fixes',
                                                            'D) High-dose hook (prozone-like) '
                                                            'effect from antigen excess'],
                                                'answer': 'D) High-dose hook (prozone-like) effect '
                                                          'from antigen excess',
                                                'explanation': 'In sandwich assays, extreme '
                                                               'antigen can saturate capture and '
                                                               'detection antibodies, preventing '
                                                               'bridge formation and yielding '
                                                               'paradoxically low signals. Serial '
                                                               'dilution restores linearity and '
                                                               'reveals the true high '
                                                               'concentration—a classic '
                                                               'hook-effect troubleshooting step.',
                                                'choice_explanations': {'A': 'Reagent issues may '
                                                                             'cause failure, but '
                                                                             'the '
                                                                             'dilution-unmasked '
                                                                             'rise after a falsely '
                                                                             'low result is the '
                                                                             'hallmark of '
                                                                             'antigen-excess hook '
                                                                             'effect.',
                                                                        'B': 'Icterus can '
                                                                             'interfere in some '
                                                                             'methods but does not '
                                                                             'specifically explain '
                                                                             'dilution-corrected '
                                                                             'sandwich hook '
                                                                             'behavior.',
                                                                        'C': 'Mislabeling is a '
                                                                             'preanalytic identity '
                                                                             'error; orderly '
                                                                             'dilution recovery of '
                                                                             'a high result points '
                                                                             'to analytic hook '
                                                                             'effect.',
                                                                        'D': 'Antigen excess '
                                                                             'saturates sandwich '
                                                                             'reagents, falsely '
                                                                             'lowering signal '
                                                                             'until dilution '
                                                                             'reveals the true '
                                                                             'high analyte—the '
                                                                             'high-dose hook '
                                                                             'effect.'}},
                                               {'question': 'A critically ill patient’s arterial '
                                                            'blood gas shows unexpected hypoxemia '
                                                            'after a long delay at room '
                                                            'temperature before analysis. Which '
                                                            'preanalytic mechanism is most '
                                                            'plausible?',
                                                'options': ['A) Continued cellular metabolism '
                                                            'and/or air-bubble gas exchange '
                                                            'distorting pO2/pCO2',
                                                            'B) Immediate improvement of all gas '
                                                            'tensions by delayed analysis',
                                                            'C) Guaranteed accuracy because ABG '
                                                            'electrodes self-correct for time',
                                                            'D) Only bilirubin interference '
                                                            'without gas-tension change'],
                                                'answer': 'A) Continued cellular metabolism and/or '
                                                          'air-bubble gas exchange distorting '
                                                          'pO2/pCO2',
                                                'explanation': 'Delayed ABG analysis allows '
                                                               'leukocytes/platelets to consume O2 '
                                                               'and produce CO2, and air bubbles '
                                                               'equilibrate with room air, biasing '
                                                               'pO2/pCO2/pH. Specimens should be '
                                                               'analyzed promptly (and iced only '
                                                               'per current local policy). Time '
                                                               'delays are a major preanalytic ABG '
                                                               'error source.',
                                                'choice_explanations': {'A': 'Metabolism and air '
                                                                             'contamination during '
                                                                             'delay alter '
                                                                             'blood-gas '
                                                                             'tensions—classic ABG '
                                                                             'preanalytic error.',
                                                                        'B': 'Delay does not '
                                                                             'improve accuracy; it '
                                                                             'typically worsens '
                                                                             'gas-tension '
                                                                             'fidelity.',
                                                                        'C': 'Electrodes do not '
                                                                             'negate preanalytic '
                                                                             'time/temperature/air-bubble '
                                                                             'effects.',
                                                                        'D': 'Bilirubin may affect '
                                                                             'some co-oximetry '
                                                                             'readings but is not '
                                                                             'the primary '
                                                                             'explanation for '
                                                                             'delayed-analysis '
                                                                             'pO2/pCO2 '
                                                                             'distortion.'}}],
                                      'extreme': [{'question': 'A 55-year-old with known cirrhosis '
                                                               'has Na 122 mmol/L, glucose 90 '
                                                               'mg/dL, BUN 18 mg/dL, and measured '
                                                               'osmolality 255 mOsm/kg. Calculated '
                                                               'osmolarity is similarly low and '
                                                               'the osmolar gap is not increased. '
                                                               'The specimen is not lipemic or '
                                                               'hyperproteinemic. Which '
                                                               'hyponatremia classification and '
                                                               'next laboratory concept fit best?',
                                                   'options': ['A) Pseudohyponatremia from severe '
                                                               'hyperlipidemia — expect normal '
                                                               'measured osmolality',
                                                               'B) True hypotonic hyponatremia; '
                                                               'integrate volume status and '
                                                               'clinically relevant causes (e.g., '
                                                               'hypervolemic cirrhosis) rather '
                                                               'than treating as an osmolar-gap '
                                                               'toxin',
                                                               'C) Hypertonic hyponatremia from '
                                                               'marked hyperglycemia — expect high '
                                                               'measured osmolality',
                                                               'D) Factitious result from drawing '
                                                               'above an IV saline infusion '
                                                               'exclusively'],
                                                   'answer': 'B) True hypotonic hyponatremia; '
                                                             'integrate volume status and '
                                                             'clinically relevant causes (e.g., '
                                                             'hypervolemic cirrhosis) rather than '
                                                             'treating as an osmolar-gap toxin',
                                                   'explanation': 'Low Na with low measured '
                                                                  'osmolality and no osmolar gap '
                                                                  'indicates true hypotonic '
                                                                  'hyponatremia. In cirrhosis this '
                                                                  'is often hypervolemic '
                                                                  '(effective arterial '
                                                                  'underfilling with ADH). '
                                                                  'Pseudohyponatremia shows normal '
                                                                  'measured osmolality with '
                                                                  'indirect potentiometry '
                                                                  'artifacts; hypertonic '
                                                                  'hyponatremia shows high '
                                                                  'osmolality (glucose/mannitol). '
                                                                  'Management hinges on tonicity '
                                                                  'and volume assessment, not '
                                                                  'toxic-alcohol gaps.',
                                                   'choice_explanations': {'A': 'Pseudohyponatremia '
                                                                                'from extreme '
                                                                                'lipid/protein '
                                                                                'with indirect ISE '
                                                                                'typically has '
                                                                                'normal measured '
                                                                                'osmolality; here '
                                                                                'osmolality is '
                                                                                'low, so Na is '
                                                                                'truly hypotonic.',
                                                                           'B': 'Low Na + low '
                                                                                'osmolality '
                                                                                'without gap = '
                                                                                'true hypotonic '
                                                                                'hyponatremia; in '
                                                                                'cirrhosis, '
                                                                                'interpret with '
                                                                                'volume status and '
                                                                                'avoid toxin-gap '
                                                                                'framing.',
                                                                           'C': 'Hypertonic '
                                                                                'hyponatremia from '
                                                                                'hyperglycemia '
                                                                                'raises measured '
                                                                                'osmolality; this '
                                                                                'patient’s '
                                                                                'osmolality is '
                                                                                'low.',
                                                                           'D': 'IV-fluid '
                                                                                'contamination can '
                                                                                'distort '
                                                                                'electrolytes, but '
                                                                                'concurrent low '
                                                                                'measured '
                                                                                'osmolality with a '
                                                                                'cirrhotic context '
                                                                                'supports true '
                                                                                'hypotonic '
                                                                                'hyponatremia '
                                                                                'rather than that '
                                                                                'sole mechanism.'}},
                                                  {'question': 'QC for an enzyme assay shows a '
                                                               'sudden +3 SD shift on both levels '
                                                               'after a reagent lot change, while '
                                                               'patient moving averages also drift '
                                                               'upward. Calibration with the new '
                                                               'lot was accepted yesterday. Which '
                                                               'troubleshooting interpretation is '
                                                               'most sound?',
                                                   'options': ['A) Ignore QC because calibration '
                                                               'was accepted once',
                                                               'B) Attribute the shift only to a '
                                                               'single outpatient’s exercise',
                                                               'C) Investigate systematic error '
                                                               '(reagent/calibrator/lot/instrument); '
                                                               'stop patient reporting until '
                                                               'corrected and verified',
                                                               'D) Average the QC points with '
                                                               'yesterday’s in-control data to '
                                                               '“smooth” the chart'],
                                                   'answer': 'C) Investigate systematic error '
                                                             '(reagent/calibrator/lot/instrument); '
                                                             'stop patient reporting until '
                                                             'corrected and verified',
                                                   'explanation': 'A simultaneous multilevel QC '
                                                                  'shift plus patient-mean drift '
                                                                  'after a lot change indicates '
                                                                  'systematic analytic bias. '
                                                                  'Out-of-control QC requires '
                                                                  'stopping reporting, '
                                                                  'investigating (reagent, '
                                                                  'calibrator, maintenance), '
                                                                  'corrective action, and '
                                                                  'verification with in-control QC '
                                                                  'before resuming. Never '
                                                                  'mathematically blend '
                                                                  'out-of-control points to hide '
                                                                  'failure.',
                                                   'choice_explanations': {'A': 'Prior calibration '
                                                                                'acceptance does '
                                                                                'not override '
                                                                                'current '
                                                                                'out-of-control QC '
                                                                                'and patient '
                                                                                'drift; patient '
                                                                                'results must not '
                                                                                'be released.',
                                                                           'B': 'One patient’s '
                                                                                'physiology cannot '
                                                                                'shift both QC '
                                                                                'levels and the '
                                                                                'population moving '
                                                                                'average.',
                                                                           'C': 'Multilevel QC '
                                                                                'shift with '
                                                                                'patient drift '
                                                                                'signals '
                                                                                'systematic '
                                                                                'error—quarantine '
                                                                                'results, fix the '
                                                                                'system, and '
                                                                                'verify before '
                                                                                'release.',
                                                                           'D': 'Smoothing or '
                                                                                'averaging away '
                                                                                'out-of-control QC '
                                                                                'falsifies quality '
                                                                                'records and risks '
                                                                                'releasing biased '
                                                                                'patient '
                                                                                'results.'}},
                                                  {'question': 'An ICU patient’s potassium is 6.8 '
                                                               'mmol/L on a chemistry panel drawn '
                                                               'during cardiac arrest '
                                                               'resuscitation, but a simultaneous '
                                                               'blood-gas potassium is 4.1 mmol/L '
                                                               'and the ECG shows no peaked T '
                                                               'waves. The chemistry tube was '
                                                               'traumatic and markedly hemolyzed; '
                                                               'the ABG was clean. What is the '
                                                               'best laboratory action?',
                                                   'options': ['A) Report 6.8 as critical '
                                                               'hyperkalemia without comment '
                                                               'because chemistry is always '
                                                               'definitive',
                                                               'B) Average 6.8 and 4.1 and report '
                                                               '5.45 without investigation',
                                                               'C) Add hemolysis index to raise '
                                                               'the chemistry K+ further before '
                                                               'release',
                                                               'D) Cancel/qualify the hemolyzed '
                                                               'chemistry K+, correlate with '
                                                               'ABG/ECG, and request an '
                                                               'appropriate nonhemolyzed specimen '
                                                               'if still needed'],
                                                   'answer': 'D) Cancel/qualify the hemolyzed '
                                                             'chemistry K+, correlate with '
                                                             'ABG/ECG, and request an appropriate '
                                                             'nonhemolyzed specimen if still '
                                                             'needed',
                                                   'explanation': 'Discordant K+ with hemolysis, a '
                                                                  'clean ABG value, and absent ECG '
                                                                  'changes indicates preanalytic '
                                                                  'false elevation on chemistry. '
                                                                  'Best practice is to reject or '
                                                                  'prominently qualify the '
                                                                  'hemolyzed result, communicate '
                                                                  'with clinicians, and use a '
                                                                  'valid specimen—never average '
                                                                  'conflicting results or escalate '
                                                                  'an artifact.',
                                                   'choice_explanations': {'A': 'Hemolyzed '
                                                                                'chemistry K+ is '
                                                                                'unreliable; '
                                                                                'reporting it as '
                                                                                'confirmed '
                                                                                'critical '
                                                                                'hyperkalemia '
                                                                                'risks harmful '
                                                                                'treatment.',
                                                                           'B': 'Averaging an '
                                                                                'artifact with a '
                                                                                'valid result '
                                                                                'produces a '
                                                                                'meaningless '
                                                                                'hybrid number.',
                                                                           'C': 'Amplifying a '
                                                                                'hemolyzed value '
                                                                                'worsens the false '
                                                                                'elevation rather '
                                                                                'than correcting '
                                                                                'it.',
                                                                           'D': 'Reject/qualify '
                                                                                'hemolyzed K+, use '
                                                                                'clinical/ABG '
                                                                                'correlation, and '
                                                                                'recollect if '
                                                                                'necessary—the '
                                                                                'correct '
                                                                                'preanalytic '
                                                                                'response.'}}]},
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
                          'questions': {'easy': [{'question': 'In the Gram stain, why do '
                                                              'Gram-positive organisms appear '
                                                              'purple/blue after the procedure?',
                                                  'options': ['A) Thick peptidoglycan retains '
                                                              'crystal violet–iodine complex after '
                                                              'decolorization',
                                                              'B) They lack cell walls entirely so '
                                                              'dye adheres randomly',
                                                              'C) Safranin is the only dye they '
                                                              'can bind',
                                                              'D) Alcohol fixative alone creates '
                                                              'purple color without crystal '
                                                              'violet'],
                                                  'answer': 'A) Thick peptidoglycan retains '
                                                            'crystal violet–iodine complex after '
                                                            'decolorization',
                                                  'explanation': 'Gram-positive walls have thick '
                                                                 'peptidoglycan that traps the '
                                                                 'crystal violet–iodine complex '
                                                                 'during alcohol/acetone '
                                                                 'decolorization, so cells remain '
                                                                 'purple. Gram-negatives lose the '
                                                                 'complex and take safranin '
                                                                 'counterstain (pink/red).',
                                                  'choice_explanations': {'A': 'Thick '
                                                                               'peptidoglycan '
                                                                               'retains crystal '
                                                                               'violet–iodine '
                                                                               'through '
                                                                               'decolorization, '
                                                                               'yielding purple '
                                                                               'Gram-positive '
                                                                               'staining.',
                                                                          'B': 'Gram-positive '
                                                                               'bacteria have '
                                                                               'substantial cell '
                                                                               'walls; wall-less '
                                                                               'organisms stain '
                                                                               'poorly/variable '
                                                                               'and are not the '
                                                                               'Gram-positive '
                                                                               'mechanism.',
                                                                          'C': 'Safranin is the '
                                                                               'counterstain for '
                                                                               'organisms that '
                                                                               'lost crystal '
                                                                               'violet; '
                                                                               'Gram-positives '
                                                                               'retain crystal '
                                                                               'violet, not '
                                                                               'safranin as their '
                                                                               'primary color.',
                                                                          'D': 'Purple color '
                                                                               'requires crystal '
                                                                               'violet (and iodine '
                                                                               'mordant), not '
                                                                               'alcohol alone.'}},
                                                 {'question': 'Blood cultures are most '
                                                              'appropriately collected when which '
                                                              'clinical syndrome is suspected?',
                                                  'options': ['A) Isolated allergic rhinitis '
                                                              'without fever or systemic signs',
                                                              'B) Suspected bacteremia/sepsis '
                                                              'before antibiotics when possible',
                                                              'C) Stable healed wound without '
                                                              'infection signs',
                                                              'D) Routine wellness visit with '
                                                              'normal vital signs only'],
                                                  'answer': 'B) Suspected bacteremia/sepsis before '
                                                            'antibiotics when possible',
                                                  'explanation': 'Blood cultures detect viable '
                                                                 'organisms in the bloodstream and '
                                                                 'are indicated for suspected '
                                                                 'bacteremia/sepsis, endocarditis, '
                                                                 'and similar syndromes. Ideally '
                                                                 'draw before antibiotics, using '
                                                                 'proper skin antisepsis and '
                                                                 'adequate volume. They are not '
                                                                 'screening tests for well '
                                                                 'patients.',
                                                  'choice_explanations': {'A': 'Allergic rhinitis '
                                                                               'is not a '
                                                                               'bacteremia '
                                                                               'indication for '
                                                                               'blood cultures.',
                                                                          'B': 'Suspected '
                                                                               'bacteremia/sepsis '
                                                                               'is the core '
                                                                               'indication; '
                                                                               'collect '
                                                                               'aseptically, '
                                                                               'preferably before '
                                                                               'antibiotics, with '
                                                                               'adequate volume.',
                                                                          'C': 'Healed wounds '
                                                                               'without systemic '
                                                                               'infection do not '
                                                                               'warrant blood '
                                                                               'cultures.',
                                                                          'D': 'Asymptomatic '
                                                                               'wellness visits '
                                                                               'are not '
                                                                               'appropriate '
                                                                               'blood-culture '
                                                                               'indications.'}},
                                                 {'question': 'What is the primary clinical '
                                                              'purpose of antimicrobial '
                                                              'susceptibility testing on a '
                                                              'significant isolate?',
                                                  'options': ['A) Identify colony morphology '
                                                              'colors only',
                                                              'B) Quantify fecal occult blood',
                                                              'C) Guide antimicrobial therapy '
                                                              'selection using standardized '
                                                              'breakpoints',
                                                              'D) Replace infection-control '
                                                              'isolation decisions entirely'],
                                                  'answer': 'C) Guide antimicrobial therapy '
                                                            'selection using standardized '
                                                            'breakpoints',
                                                  'explanation': 'AST measures in-vitro drug '
                                                                 'activity and interprets results '
                                                                 'with CLSI/EUCAST breakpoints to '
                                                                 'support therapy choices. '
                                                                 'Identification and '
                                                                 'infection-control actions are '
                                                                 'related but distinct '
                                                                 'laboratory/clinical processes.',
                                                  'choice_explanations': {'A': 'Colony morphology '
                                                                               'aids '
                                                                               'identification but '
                                                                               'is not the purpose '
                                                                               'of susceptibility '
                                                                               'testing.',
                                                                          'B': 'Fecal occult blood '
                                                                               'is a '
                                                                               'chemistry/POCT GI '
                                                                               'test unrelated to '
                                                                               'AST.',
                                                                          'C': 'AST guides drug '
                                                                               'selection via '
                                                                               'standardized '
                                                                               'MIC/disk '
                                                                               'interpretations '
                                                                               'and breakpoints.',
                                                                          'D': 'Transmission-based '
                                                                               'precautions depend '
                                                                               'on organism and '
                                                                               'epidemiology; AST '
                                                                               'informs therapy, '
                                                                               'not all isolation '
                                                                               'decisions '
                                                                               'alone.'}}],
                                        'medium': [{'question': 'Acid-fast staining (e.g., '
                                                                'Ziehl–Neelsen/Kinyoun or '
                                                                'fluorochrome) is used primarily '
                                                                'because which organisms resist '
                                                                'ordinary Gram decolorization '
                                                                'themes?',
                                                    'options': ['A) Mycoplasma lacking any cell '
                                                                'wall lipids of interest',
                                                                'B) Typical Streptococcus pyogenes '
                                                                'only',
                                                                'C) Yeast forms that always '
                                                                'Gram-stain Gram-negative',
                                                                'D) Mycobacteria with mycolic '
                                                                'acid–rich cell walls'],
                                                    'answer': 'D) Mycobacteria with mycolic '
                                                              'acid–rich cell walls',
                                                    'explanation': 'Mycobacterial mycolic acids '
                                                                   'make walls waxy and acid-fast: '
                                                                   'they retain carbolfuchsin '
                                                                   'after acid-alcohol. This '
                                                                   'property underpins TB/NTM '
                                                                   'smear diagnosis alongside '
                                                                   'culture/NAAT. Ordinary Gram '
                                                                   'stain poorly visualizes '
                                                                   'mycobacteria.',
                                                    'choice_explanations': {'A': 'Mycoplasma lack '
                                                                                 'cell walls and '
                                                                                 'are not '
                                                                                 'acid-fast '
                                                                                 'mycobacteria.',
                                                                            'B': 'S. pyogenes is '
                                                                                 'Gram-positive '
                                                                                 'and not '
                                                                                 'diagnosed by '
                                                                                 'acid-fast '
                                                                                 'microscopy.',
                                                                            'C': 'Yeasts are seen '
                                                                                 'on '
                                                                                 'Gram/KOH/calcofluor; '
                                                                                 'acid-fast '
                                                                                 'methods target '
                                                                                 'mycobacteria/nocardia '
                                                                                 'themes, not '
                                                                                 'routine yeast '
                                                                                 'ID.',
                                                                            'D': 'Mycolic '
                                                                                 'acid–rich '
                                                                                 'mycobacterial '
                                                                                 'walls retain '
                                                                                 'acid-fast stains '
                                                                                 'after '
                                                                                 'acid-alcohol '
                                                                                 'decolorization.'}},
                                                   {'question': 'Catalase testing helps separate '
                                                                'which major Gram-positive coccus '
                                                                'groups in the algorithm?',
                                                    'options': ['A) Staphylococci '
                                                                '(catalase-positive) from '
                                                                'streptococci/enterococci '
                                                                '(catalase-negative)',
                                                                'B) All Gram-negative rods from '
                                                                'each other',
                                                                'C) Mycobacteria from Nocardia '
                                                                'exclusively without culture',
                                                                'D) Viruses from fungi on blood '
                                                                'agar'],
                                                    'answer': 'A) Staphylococci '
                                                              '(catalase-positive) from '
                                                              'streptococci/enterococci '
                                                              '(catalase-negative)',
                                                    'explanation': 'Catalase decomposes H2O2 to '
                                                                   'oxygen; bubbling indicates '
                                                                   'positivity. Staphylococci are '
                                                                   'catalase-positive, whereas '
                                                                   'streptococci and enterococci '
                                                                   'are catalase-negative—an early '
                                                                   'branch point in Gram-positive '
                                                                   'coccus identification.',
                                                    'choice_explanations': {'A': 'Catalase '
                                                                                 'separates '
                                                                                 'staphylococci '
                                                                                 '(+) from '
                                                                                 'strep/enterococci '
                                                                                 '(−) in routine '
                                                                                 'bench '
                                                                                 'algorithms.',
                                                                            'B': 'Gram-negative '
                                                                                 'rods use '
                                                                                 'oxidase, '
                                                                                 'fermentation, '
                                                                                 'and panels—not '
                                                                                 'catalase as '
                                                                                 'their primary '
                                                                                 'separator from '
                                                                                 'each other.',
                                                                            'C': 'Mycobacteria/Nocardia '
                                                                                 'need '
                                                                                 'acid-fast/modified '
                                                                                 'acid-fast and '
                                                                                 'other methods; '
                                                                                 'catalase alone '
                                                                                 'is not '
                                                                                 'definitive '
                                                                                 'separation.',
                                                                            'D': 'Viruses do not '
                                                                                 'grow as colonies '
                                                                                 'on blood agar '
                                                                                 'for catalase '
                                                                                 'differentiation '
                                                                                 'from fungi.'}},
                                                   {'question': 'CSF Gram stain and culture are '
                                                                'considered critical specimens '
                                                                'primarily because bacterial '
                                                                'meningitis requires which '
                                                                'laboratory handling theme?',
                                                    'options': ['A) Batching overnight at room '
                                                                'temperature without notification',
                                                                'B) Rapid processing, prompt '
                                                                'plating, and immediate clinician '
                                                                'communication of positives',
                                                                'C) Discarding cloudy specimens as '
                                                                'contaminated always',
                                                                'D) Waiting for PCR only and never '
                                                                'performing Gram stain'],
                                                    'answer': 'B) Rapid processing, prompt '
                                                              'plating, and immediate clinician '
                                                              'communication of positives',
                                                    'explanation': 'Suspected bacterial meningitis '
                                                                   'is time-critical. CSF should '
                                                                   'be processed urgently for cell '
                                                                   'count, chemistry, Gram stain, '
                                                                   'culture (± multiplex PCR). '
                                                                   'Positive Gram stains are '
                                                                   'critical values requiring '
                                                                   'immediate notification. Delays '
                                                                   'reduce organism recovery and '
                                                                   'slow therapy.',
                                                    'choice_explanations': {'A': 'Overnight delay '
                                                                                 'risks organism '
                                                                                 'death and '
                                                                                 'delayed '
                                                                                 'life-saving '
                                                                                 'therapy—unacceptable '
                                                                                 'for CSF.',
                                                                            'B': 'Urgent '
                                                                                 'processing and '
                                                                                 'immediate '
                                                                                 'reporting of '
                                                                                 'positive CSF '
                                                                                 'findings are '
                                                                                 'standard '
                                                                                 'critical-specimen '
                                                                                 'practices.',
                                                                            'C': 'Cloudiness may '
                                                                                 'reflect '
                                                                                 'neutrophils/organisms '
                                                                                 'in true '
                                                                                 'infection and '
                                                                                 'must be worked '
                                                                                 'up, not '
                                                                                 'discarded.',
                                                                            'D': 'Gram stain '
                                                                                 'remains '
                                                                                 'high-yield; '
                                                                                 'molecular tests '
                                                                                 'complement but '
                                                                                 'do not '
                                                                                 'universally '
                                                                                 'replace '
                                                                                 'culture/stain '
                                                                                 'workflows.'}}],
                                        'hard': [{'question': 'An isolate is coagulase-positive '
                                                              'Staphylococcus aureus. Cefoxitin '
                                                              'screening is resistant. Which '
                                                              'resistance mechanism/reporting '
                                                              'concept is most appropriate?',
                                                  'options': ['A) Report as penicillin-susceptible '
                                                              'MSSA without further markers',
                                                              'B) Assume vancomycin resistance '
                                                              'automatically for all such isolates',
                                                              'C) Interpret as MRSA (mecA/mecC '
                                                              'PBP2a theme) and report '
                                                              'oxacillin/cefoxitin-resistant',
                                                              'D) Treat cefoxitin resistance as '
                                                              'only a disk-contaminant artifact '
                                                              'always'],
                                                  'answer': 'C) Interpret as MRSA (mecA/mecC PBP2a '
                                                            'theme) and report '
                                                            'oxacillin/cefoxitin-resistant',
                                                  'explanation': 'Cefoxitin is a reliable '
                                                                 'phenotypic screen for '
                                                                 'mecA/mecC-mediated methicillin '
                                                                 'resistance (PBP2a). Such '
                                                                 'isolates are reported as '
                                                                 'MRSA/oxacillin-resistant and '
                                                                 'resistant to most β-lactams per '
                                                                 'standards. Vancomycin resistance '
                                                                 'is uncommon and separately '
                                                                 'tested; MSSA labeling would be '
                                                                 'incorrect.',
                                                  'choice_explanations': {'A': 'Cefoxitin '
                                                                               'resistance '
                                                                               'indicates '
                                                                               'methicillin '
                                                                               'resistance—not '
                                                                               'MSSA.',
                                                                          'B': 'MRSA is not '
                                                                               'synonymous with '
                                                                               'vancomycin '
                                                                               'resistance; '
                                                                               'VRSA/VISA require '
                                                                               'specific '
                                                                               'detection.',
                                                                          'C': 'Cefoxitin-resistant '
                                                                               'S. aureus is '
                                                                               'interpreted as '
                                                                               'MRSA via '
                                                                               'mec-mediated PBP2a '
                                                                               'and reported '
                                                                               'resistant to '
                                                                               'oxacillin/most '
                                                                               'β-lactams.',
                                                                          'D': 'Cefoxitin '
                                                                               'screening is '
                                                                               'validated for MRSA '
                                                                               'detection; '
                                                                               'dismissing it as '
                                                                               'artifact without '
                                                                               'investigation is '
                                                                               'unsafe.'}},
                                                 {'question': 'An anaerobic culture is requested '
                                                              'on a swab left open on the bench '
                                                              'for hours. Which preanalytic '
                                                              'judgment is most correct?',
                                                  'options': ['A) Anaerobes remain fully viable in '
                                                              'ambient air indefinitely',
                                                              'B) Results will be more sensitive '
                                                              'after aerobic delay',
                                                              'C) Only viruses are affected by '
                                                              'oxygen exposure',
                                                              'D) Oxygen exposure and delayed '
                                                              'anaerobic transport can kill '
                                                              'anaerobes — recollect with proper '
                                                              'anaerobic system if feasible'],
                                                  'answer': 'D) Oxygen exposure and delayed '
                                                            'anaerobic transport can kill '
                                                            'anaerobes — recollect with proper '
                                                            'anaerobic system if feasible',
                                                  'explanation': 'Obligate anaerobes are '
                                                                 'oxygen-intolerant. Specimens '
                                                                 'need anaerobic transport devices '
                                                                 'and prompt processing. Ambient '
                                                                 'delay yields false-negative '
                                                                 'cultures. Laboratories should '
                                                                 'educate collectors and request '
                                                                 'recollection when transport is '
                                                                 'invalid.',
                                                  'choice_explanations': {'A': 'Many clinically '
                                                                               'important '
                                                                               'anaerobes die '
                                                                               'rapidly in room '
                                                                               'air—viability is '
                                                                               'not indefinite.',
                                                                          'B': 'Aerobic delay '
                                                                               'decreases, not '
                                                                               'increases, '
                                                                               'anaerobic '
                                                                               'recovery.',
                                                                          'C': 'Oxygen toxicity is '
                                                                               'a major issue for '
                                                                               'anaerobes, not '
                                                                               'only viruses.',
                                                                          'D': 'Improper aerobic '
                                                                               'delay jeopardizes '
                                                                               'anaerobes; use '
                                                                               'anaerobic '
                                                                               'transport and '
                                                                               'recollect when '
                                                                               'needed.'}},
                                                 {'question': 'Three of four blood-culture sets '
                                                              'grow Staphylococcus epidermidis, '
                                                              'but one bottle is negative and the '
                                                              'patient has a prosthetic valve with '
                                                              'fever. Which interpretation is most '
                                                              'defensible?',
                                                  'options': ['A) Multiple positive sets with a '
                                                              'common skin organism in a '
                                                              'prosthesis host can indicate true '
                                                              'bacteremia/endocarditis risk — '
                                                              'correlate clinically',
                                                              'B) Any coagulase-negative '
                                                              'staphylococcus is always pure '
                                                              'contamination',
                                                              'C) Report all CNS as Streptococcus '
                                                              'pyogenes automatically',
                                                              'D) Ignore positives because only '
                                                              'Gram-negatives cause endocarditis'],
                                                  'answer': 'A) Multiple positive sets with a '
                                                            'common skin organism in a prosthesis '
                                                            'host can indicate true '
                                                            'bacteremia/endocarditis risk — '
                                                            'correlate clinically',
                                                  'explanation': 'Coagulase-negative staphylococci '
                                                                 'are common contaminants, but '
                                                                 'repeated positivity across '
                                                                 'sets—especially with prosthetic '
                                                                 'material—supports true infection '
                                                                 'including endocarditis. '
                                                                 'Single-bottle CNS more often '
                                                                 'reflects contamination. '
                                                                 'Identification, timing, and '
                                                                 'clinical correlation guide '
                                                                 'significance.',
                                                  'choice_explanations': {'A': 'Multiple sets '
                                                                               'positive for CNS '
                                                                               'in a '
                                                                               'prosthetic-valve '
                                                                               'patient raise true '
                                                                               'bacteremia/endocarditis '
                                                                               'concern needing '
                                                                               'clinical '
                                                                               'correlation and '
                                                                               'ID/AST.',
                                                                          'B': 'CNS can be '
                                                                               'pathogens in '
                                                                               'device-related '
                                                                               'infections; '
                                                                               '“always '
                                                                               'contaminant” is '
                                                                               'false.',
                                                                          'C': 'S. epidermidis '
                                                                               'must not be '
                                                                               'relabeled as S. '
                                                                               'pyogenes.',
                                                                          'D': 'Gram-positive '
                                                                               'organisms, '
                                                                               'including '
                                                                               'staphylococci, are '
                                                                               'major endocarditis '
                                                                               'pathogens.'}}],
                                        'extreme': [{'question': 'A microbiology tech processing a '
                                                                 'lymph-node biopsy from a hunter '
                                                                 'with ulceroglandular illness '
                                                                 'notes tiny Gram-negative '
                                                                 'coccobacilli on stain. The '
                                                                 'organism grows poorly on '
                                                                 'chocolate agar and the physician '
                                                                 'mentions possible tularemia. '
                                                                 'Which laboratory safety and '
                                                                 'workup synthesis is most '
                                                                 'appropriate?',
                                                     'options': ['A) Continue aerosol-generating '
                                                                 'workup on an open bench without '
                                                                 'BSL upgrades',
                                                                 'B) Handle as a potential '
                                                                 'Francisella risk: minimize '
                                                                 'aerosols, use appropriate BSL '
                                                                 'practices, and refer/confirm '
                                                                 'with public-health/reference '
                                                                 'methods',
                                                                 'C) Autoclave the specimen '
                                                                 'immediately without notifying '
                                                                 'anyone and discard all cultures',
                                                                 'D) Report as routine Haemophilus '
                                                                 'influenzae based on Gram '
                                                                 'morphology alone'],
                                                     'answer': 'B) Handle as a potential '
                                                               'Francisella risk: minimize '
                                                               'aerosols, use appropriate BSL '
                                                               'practices, and refer/confirm with '
                                                               'public-health/reference methods',
                                                     'explanation': 'Francisella tularensis is a '
                                                                    'high-risk laboratory '
                                                                    'pathogen; suspected isolates '
                                                                    'require restricted '
                                                                    'manipulation, BSL-2/3 '
                                                                    'practices per guidelines, and '
                                                                    'often public-health referral. '
                                                                    'Open-bench aerosol work is '
                                                                    'dangerous. Morphology alone '
                                                                    'cannot finalize identity as '
                                                                    'Haemophilus.',
                                                     'choice_explanations': {'A': 'Open-bench '
                                                                                  'aerosolization '
                                                                                  'of possible '
                                                                                  'Francisella is '
                                                                                  'a serious '
                                                                                  'lab-acquired '
                                                                                  'infection risk.',
                                                                             'B': 'Suspect '
                                                                                  'tularemia → '
                                                                                  'heighten '
                                                                                  'biosafety, '
                                                                                  'limit '
                                                                                  'manipulation, '
                                                                                  'and confirm via '
                                                                                  'reference/public-health '
                                                                                  'pathways.',
                                                                             'C': 'Destroying '
                                                                                  'evidence '
                                                                                  'without '
                                                                                  'communication '
                                                                                  'harms diagnosis '
                                                                                  'and outbreak '
                                                                                  'response; '
                                                                                  'follow '
                                                                                  'select-agent/public-health '
                                                                                  'procedures '
                                                                                  'instead.',
                                                                             'D': 'Tiny GN '
                                                                                  'coccobacilli '
                                                                                  'are not '
                                                                                  'specific for H. '
                                                                                  'influenzae; '
                                                                                  'clinical '
                                                                                  'epidemiology '
                                                                                  'points to '
                                                                                  'Francisella '
                                                                                  'until proven '
                                                                                  'otherwise.'}},
                                                    {'question': 'An ICU outbreak investigation '
                                                                 'shows identical '
                                                                 'carbapenem-resistant Klebsiella '
                                                                 'pneumoniae from five patients’ '
                                                                 'clinical cultures and from a '
                                                                 'shared sink drain. Rectal '
                                                                 'screens of contacts are pending. '
                                                                 'Which integrated '
                                                                 'infection-control and laboratory '
                                                                 'response is best?',
                                                     'options': ['A) Suppress CRKP results from '
                                                                 'the chart to avoid alarm',
                                                                 'B) Report each isolate routinely '
                                                                 'without notifying infection '
                                                                 'prevention',
                                                                 'C) Escalate to infection '
                                                                 'prevention, support contact '
                                                                 'precautions/screening, and use '
                                                                 'methods that confirm '
                                                                 'carbapenemase themes as policy '
                                                                 'directs',
                                                                 'D) Reculture only on MacConkey '
                                                                 'without susceptibility testing'],
                                                     'answer': 'C) Escalate to infection '
                                                               'prevention, support contact '
                                                               'precautions/screening, and use '
                                                               'methods that confirm carbapenemase '
                                                               'themes as policy directs',
                                                     'explanation': 'Clustered CRKP with '
                                                                    'environmental recovery '
                                                                    'signals transmission. Labs '
                                                                    'must rapidly report, notify '
                                                                    'infection prevention, assist '
                                                                    'surveillance cultures, and '
                                                                    'characterize carbapenem '
                                                                    'resistance mechanisms per '
                                                                    'protocol. Hiding results or '
                                                                    'omitting AST undermines '
                                                                    'containment.',
                                                     'choice_explanations': {'A': 'Suppressing '
                                                                                  'multidrug-resistant '
                                                                                  'organism '
                                                                                  'results '
                                                                                  'endangers '
                                                                                  'patients and '
                                                                                  'violates '
                                                                                  'reporting '
                                                                                  'duties.',
                                                                             'B': 'Outbreak '
                                                                                  'clusters '
                                                                                  'require '
                                                                                  'immediate '
                                                                                  'infection-prevention '
                                                                                  'notification '
                                                                                  'beyond routine '
                                                                                  'single-result '
                                                                                  'release.',
                                                                             'C': 'IP '
                                                                                  'notification, '
                                                                                  'transmission-based '
                                                                                  'precautions, '
                                                                                  'screening, and '
                                                                                  'resistance '
                                                                                  'characterization '
                                                                                  'are the correct '
                                                                                  'outbreak '
                                                                                  'response.',
                                                                             'D': 'Identification '
                                                                                  'without '
                                                                                  'AST/carbapenemase '
                                                                                  'evaluation '
                                                                                  'fails '
                                                                                  'therapeutic and '
                                                                                  'epidemiologic '
                                                                                  'needs.'}},
                                                    {'question': 'MALDI-TOF reports “Burkholderia '
                                                                 'mallei” from a wound culture of '
                                                                 'a stable outpatient with no '
                                                                 'travel or animal exposure; the '
                                                                 'tech notes the colony looks like '
                                                                 'ordinary B. cepacia complex. '
                                                                 'Score is borderline. What is the '
                                                                 'most appropriate next step?',
                                                     'options': ['A) Release B. mallei immediately '
                                                                 'as a select-agent confirmed ID',
                                                                 'B) Ignore the result and release '
                                                                 'as Staphylococcus aureus',
                                                                 'C) Treat all Burkholderia as '
                                                                 'contaminants without further '
                                                                 'testing',
                                                                 'D) Hold release, verify with '
                                                                 'additional methods/reference '
                                                                 'algorithms, and follow '
                                                                 'select-agent rule-out protocols '
                                                                 'before any final '
                                                                 'high-consequence ID'],
                                                     'answer': 'D) Hold release, verify with '
                                                               'additional methods/reference '
                                                               'algorithms, and follow '
                                                               'select-agent rule-out protocols '
                                                               'before any final high-consequence '
                                                               'ID',
                                                     'explanation': 'MALDI can misidentify closely '
                                                                    'related Burkholderia. B. '
                                                                    'mallei is a select agent; '
                                                                    'discordant clinical context '
                                                                    'and borderline scores mandate '
                                                                    'confirmatory testing and '
                                                                    'public-health rule-out '
                                                                    'workflows before release. '
                                                                    'Never auto-release '
                                                                    'catastrophic IDs or '
                                                                    'arbitrarily rename organisms.',
                                                     'choice_explanations': {'A': 'Unverified '
                                                                                  'select-agent '
                                                                                  'calls have '
                                                                                  'major '
                                                                                  'regulatory and '
                                                                                  'clinical '
                                                                                  'consequences—confirmation '
                                                                                  'first.',
                                                                             'B': 'Replacing the '
                                                                                  'ID with S. '
                                                                                  'aureus without '
                                                                                  'evidence is '
                                                                                  'fraudulent '
                                                                                  'reporting.',
                                                                             'C': 'Burkholderia '
                                                                                  'can be true '
                                                                                  'pathogens '
                                                                                  '(e.g., cepacia '
                                                                                  'in CF); blanket '
                                                                                  'contaminant '
                                                                                  'labeling is '
                                                                                  'wrong.',
                                                                             'D': 'Quarantine the '
                                                                                  'report, confirm '
                                                                                  'identity, and '
                                                                                  'follow '
                                                                                  'select-agent '
                                                                                  'rule-out—correct '
                                                                                  'lab '
                                                                                  'practice.'}}]},
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
                'questions': {'easy': [{'question': 'ELISA (enzyme-linked immunosorbent assay) is '
                                                    'primarily designed to detect which analytes '
                                                    'in clinical immunology?',
                                        'options': ['A) Antigen or antibody via enzyme-linked '
                                                    'specific binding and a measurable signal',
                                                    'B) Only bacterial colony counts on agar '
                                                    'plates',
                                                    'C) Chromosome karyotypes in metaphase spreads',
                                                    'D) Arterial pO2 using Clark electrodes'],
                                        'answer': 'A) Antigen or antibody via enzyme-linked '
                                                  'specific binding and a measurable signal',
                                        'explanation': 'ELISA uses immobilized antigen or '
                                                       'antibody, patient specimen, '
                                                       'enzyme-conjugated detector reagents, and a '
                                                       'substrate signal proportional to specific '
                                                       'binding. It quantifies or qualitatively '
                                                       'detects antigens/antibodies across '
                                                       'infectious disease and autoimmune testing.',
                                        'choice_explanations': {'A': 'ELISA detects antigen or '
                                                                     'antibody through '
                                                                     'enzyme-linked immunoassays '
                                                                     'producing '
                                                                     'colorimetric/fluorometric/chemiluminescent '
                                                                     'signals.',
                                                                'B': 'Colony counts are '
                                                                     'microbiology culture '
                                                                     'methods, not ELISA '
                                                                     'immunology assays.',
                                                                'C': 'Karyotyping is cytogenetic '
                                                                     'analysis, not immunoassay.',
                                                                'D': 'Blood-gas pO2 uses '
                                                                     'electrochemical sensors, not '
                                                                     'ELISA.'}},
                                       {'question': 'In a typical primary humoral response '
                                                    'timeline, which immunoglobulin class rises '
                                                    'first after antigen exposure?',
                                        'options': ['A) IgE exclusively without IgM',
                                                    'B) IgM as the earliest circulating antibody '
                                                    'class',
                                                    'C) IgA secretory dimer as the first serum '
                                                    'class always',
                                                    'D) IgD as the dominant plasma effector '
                                                    'always'],
                                        'answer': 'B) IgM as the earliest circulating antibody '
                                                  'class',
                                        'explanation': 'Primary responses produce IgM first, '
                                                       'followed by class-switched isotypes (IgG, '
                                                       'IgA, IgE) with affinity maturation. '
                                                       'Acute-infection serology often uses IgM as '
                                                       'a marker of recent response, with caveats '
                                                       'for persistence and false positives.',
                                        'choice_explanations': {'A': 'IgE appears after class '
                                                                     'switching in '
                                                                     'allergic/parasitic themes '
                                                                     'and is not the earliest '
                                                                     'primary serum response.',
                                                                'B': 'IgM is the first circulating '
                                                                     'isotype in a primary humoral '
                                                                     'response before class '
                                                                     'switching dominates.',
                                                                'C': 'Secretory IgA is important '
                                                                     'at mucosae but is not the '
                                                                     'first systemic '
                                                                     'primary-response class.',
                                                                'D': 'IgD is mainly a B-cell '
                                                                     'receptor isotype, not the '
                                                                     'dominant early plasma '
                                                                     'effector antibody.'}},
                                       {'question': 'ABO blood group typing in the blood bank is '
                                                    'fundamentally an immunohematology test of '
                                                    'which relationship?',
                                        'options': ['A) HLA matching for solid-organ transplant '
                                                    'only',
                                                    'B) Viral load quantification by PCR',
                                                    'C) RBC antigens and reciprocal plasma '
                                                    'isoagglutinins (forward and reverse typing)',
                                                    'D) Platelet aggregation to ADP alone'],
                                        'answer': 'C) RBC antigens and reciprocal plasma '
                                                  'isoagglutinins (forward and reverse typing)',
                                        'explanation': 'ABO typing pairs forward typing (patient '
                                                       'RBCs + reagent anti-A/B) with reverse '
                                                       'typing (patient plasma + reagent A1/B '
                                                       'cells). Discrepancies must be resolved '
                                                       'before transfusion. It is not HLA, '
                                                       'molecular viral load, or platelet function '
                                                       'testing.',
                                        'choice_explanations': {'A': 'HLA typing supports '
                                                                     'transplant/platelet '
                                                                     'refractoriness workups, not '
                                                                     'ABO red-cell grouping.',
                                                                'B': 'Viral load PCR is molecular '
                                                                     'diagnostics, not ABO '
                                                                     'serology.',
                                                                'C': 'ABO typing detects A/B '
                                                                     'antigens on RBCs and '
                                                                     'expected anti-A/anti-B in '
                                                                     'plasma via forward and '
                                                                     'reverse tests.',
                                                                'D': 'Platelet aggregation assays '
                                                                     'evaluate primary hemostasis, '
                                                                     'not ABO antigens.'}}],
                              'medium': [{'question': 'Antinuclear antibody (ANA) testing is most '
                                                      'appropriately used as which kind of '
                                                      'laboratory tool?',
                                          'options': ['A) A stand-alone proof of bacterial sepsis',
                                                      'B) A newborn metabolic screen replacement',
                                                      'C) A blood-gas alternative in respiratory '
                                                      'failure',
                                                      'D) A sensitive screen supporting autoimmune '
                                                      'disease workups (e.g., SLE) with clinical '
                                                      'correlation'],
                                          'answer': 'D) A sensitive screen supporting autoimmune '
                                                    'disease workups (e.g., SLE) with clinical '
                                                    'correlation',
                                          'explanation': 'ANA IFA/EIA screens for autoantibodies '
                                                         'associated with systemic autoimmune '
                                                         'diseases. High sensitivity means '
                                                         'positives need pattern/titer, specific '
                                                         'ENA/dsDNA follow-up, and clinical '
                                                         'correlation because low-titer positives '
                                                         'occur in healthy people and other '
                                                         'conditions.',
                                          'choice_explanations': {'A': 'Sepsis diagnosis relies on '
                                                                       'cultures, lactate, and '
                                                                       'clinical criteria—not ANA.',
                                                                  'B': 'Newborn screens use '
                                                                       'targeted metabolic/genetic '
                                                                       'panels, not ANA.',
                                                                  'C': 'Respiratory failure '
                                                                       'assessment uses blood '
                                                                       'gases/oximetry, not ANA.',
                                                                  'D': 'ANA is a sensitive '
                                                                       'autoimmune screen '
                                                                       'interpreted with pretest '
                                                                       'probability and reflex '
                                                                       'specific antibodies.'}},
                                         {'question': 'A patient is in the “window period” of an '
                                                      'infection where antigen is transiently '
                                                      'undetectable and IgM/IgG are not yet '
                                                      'positive. Which interpretive concept '
                                                      'applies?',
                                          'options': ['A) Infection may be present despite '
                                                      'negative markers — consider timing, risk, '
                                                      'and alternate methods (e.g., NAAT)',
                                                      'B) Negative serology always excludes '
                                                      'infection forever',
                                                      'C) Window periods only occur after lifelong '
                                                      'vaccination',
                                                      'D) All immunoassays are immune to timing '
                                                      'effects'],
                                          'answer': 'A) Infection may be present despite negative '
                                                    'markers — consider timing, risk, and '
                                                    'alternate methods (e.g., NAAT)',
                                          'explanation': 'Serologic/antigen window periods are '
                                                         'intervals when markers are below '
                                                         'detection despite infection (classic in '
                                                         'HIV/hepatitis narratives). Clinical '
                                                         'risk, repeat testing, and nucleic-acid '
                                                         'methods close diagnostic gaps.',
                                          'choice_explanations': {'A': 'Negative markers in a '
                                                                       'biologic window do not '
                                                                       'exclude infection; timed '
                                                                       'repeats and NAAT may be '
                                                                       'required.',
                                                                  'B': 'A single negative serology '
                                                                       'cannot eternally exclude '
                                                                       'infection, especially '
                                                                       'early after exposure.',
                                                                  'C': 'Window periods relate to '
                                                                       'infection kinetics, not '
                                                                       'solely vaccination.',
                                                                  'D': 'Immunoassays are highly '
                                                                       'timing-dependent for '
                                                                       'evolving immune responses '
                                                                       'and antigenemia.'}},
                                         {'question': 'Complement consumption (low C3/C4) is '
                                                      'classically associated with which disease '
                                                      'mechanism theme?',
                                          'options': ['A) Pure immediate-type allergy without '
                                                      'immune complexes',
                                                      'B) Some immune-complex diseases (e.g., SLE, '
                                                      'certain glomerulonephritides)',
                                                      'C) Simple iron deficiency without '
                                                      'inflammation',
                                                      'D) Isolated factor VIII deficiency '
                                                      'hemophilia A'],
                                          'answer': 'B) Some immune-complex diseases (e.g., SLE, '
                                                    'certain glomerulonephritides)',
                                          'explanation': 'Immune-complex activation of classical '
                                                         'complement lowers C4/C3 in active SLE '
                                                         'and some IC-mediated renal diseases. '
                                                         'Allergy (IgE), iron deficiency, and '
                                                         'hemophilia do not define '
                                                         'complement-consumption patterns.',
                                          'choice_explanations': {'A': 'Type I hypersensitivity is '
                                                                       'IgE/mast-cell mediated and '
                                                                       'does not classically '
                                                                       'consume C3/C4 like IC '
                                                                       'disease.',
                                                                  'B': 'Immune-complex activation '
                                                                       'consumes complement '
                                                                       'proteins, lowering C3/C4 '
                                                                       'in diseases such as active '
                                                                       'SLE.',
                                                                  'C': 'Iron deficiency alters '
                                                                       'iron labs/CBC, not '
                                                                       'complement consumption.',
                                                                  'D': 'Hemophilia A is a '
                                                                       'coagulation-factor '
                                                                       'deficiency unrelated to '
                                                                       'complement levels.'}}],
                              'hard': [{'question': 'In a precipitation or agglutination '
                                                    'immunoassay, excess antibody relative to '
                                                    'antigen can yield a falsely negative result. '
                                                    'What is this phenomenon called?',
                                        'options': ['A) Postzone exclusively meaning antigen '
                                                    'absence forever',
                                                    'B) Hook effect only in competitive assays '
                                                    'without exception',
                                                    'C) Prozone (antibody excess) effect',
                                                    'D) Heterophile interference identical to '
                                                    'prozone by definition'],
                                        'answer': 'C) Prozone (antibody excess) effect',
                                        'explanation': 'Prozone occurs when antibody excess '
                                                       'prevents lattice formation needed for '
                                                       'visible agglutination/precipitation, '
                                                       'causing false negatives. Diluting serum '
                                                       'restores the equivalence zone. Postzone is '
                                                       'antigen excess; hook effect typically '
                                                       'refers to antigen excess in sandwich '
                                                       'immunoassays; heterophile antibodies are a '
                                                       'different interference.',
                                        'choice_explanations': {'A': 'Postzone is antigen excess, '
                                                                     'not a synonym for permanent '
                                                                     'antigen absence.',
                                                                'B': 'Hook effect is mainly '
                                                                     'antigen-excess sandwich '
                                                                     'immunoassay signal loss; it '
                                                                     'is not identical to classic '
                                                                     'prozone terminology.',
                                                                'C': 'Prozone is antibody excess '
                                                                     'that blocks lattice '
                                                                     'formation and can falsely '
                                                                     'negative '
                                                                     'agglutination/precipitation '
                                                                     'tests; dilution corrects it.',
                                                                'D': 'Heterophile antibodies cause '
                                                                     'bridging interference in '
                                                                     'immunoassays, a mechanism '
                                                                     'distinct from stoichiometric '
                                                                     'prozone.'}},
                                       {'question': 'Flow cytometric immunophenotyping of '
                                                    'peripheral blood for leukemia/lymphoma '
                                                    'staging primarily provides which information?',
                                        'options': ['A) Serum protein electrophoresis fractions '
                                                    'only',
                                                    'B) Karyotype banding resolution equal to FISH '
                                                    'always',
                                                    'C) Culture-based MIC values for blasts',
                                                    'D) Lineage and maturation marker patterns on '
                                                    'individual cells'],
                                        'answer': 'D) Lineage and maturation marker patterns on '
                                                  'individual cells',
                                        'explanation': 'Flow cytometry measures '
                                                       'surface/cytoplasmic markers on single '
                                                       'cells, assigning lineage (myeloid vs B/T '
                                                       'lymphoid) and detecting aberrant '
                                                       'phenotypes for diagnosis and MRD. It does '
                                                       'not replace SPEP, cytogenetics entirely, '
                                                       'or antimicrobial MIC testing.',
                                        'choice_explanations': {'A': 'SPEP separates serum '
                                                                     'proteins in fluid phase, not '
                                                                     'single-cell '
                                                                     'immunophenotypes.',
                                                                'B': 'Cytogenetics/FISH assess '
                                                                     'chromosomes/genes; flow '
                                                                     'assesses antigen expression, '
                                                                     'not banding.',
                                                                'C': 'MIC testing is antimicrobial '
                                                                     'susceptibility, irrelevant '
                                                                     'to blast immunophenotyping.',
                                                                'D': 'Flow defines '
                                                                     'lineage/maturation antigen '
                                                                     'patterns cell-by-cell for '
                                                                     'leukemia/lymphoma '
                                                                     'characterization.'}},
                                       {'question': 'Biotin supplements can interfere with some '
                                                    'streptavidin–biotin immunoassay designs. '
                                                    'Which outcome is possible?',
                                        'options': ['A) False-positive and/or false-negative '
                                                    'results depending on assay architecture',
                                                    'B) Universal improvement of all assay '
                                                    'accuracy',
                                                    'C) Interference limited only to Gram stains',
                                                    'D) No effect because biotin never enters '
                                                    'serum'],
                                        'answer': 'A) False-positive and/or false-negative results '
                                                  'depending on assay architecture',
                                        'explanation': 'High biotin can compete in '
                                                       'biotin–streptavidin detection systems, '
                                                       'falsely lowering sandwich signals or '
                                                       'raising competitive assay results (classic '
                                                       'thyroid assay examples). Labs advise '
                                                       'holding supplements and using '
                                                       'biotin-resistant methods when interference '
                                                       'is suspected.',
                                        'choice_explanations': {'A': 'Biotin interference '
                                                                     'direction depends on '
                                                                     'sandwich vs competitive '
                                                                     'design—both false lows and '
                                                                     'false highs occur.',
                                                                'B': 'Biotin does not improve '
                                                                     'accuracy; it biases affected '
                                                                     'methods.',
                                                                'C': 'Gram stains are microscopy '
                                                                     'methods unaffected by serum '
                                                                     'biotin immunoassay '
                                                                     'interference.',
                                                                'D': 'Supplemental biotin reaches '
                                                                     'high serum levels capable of '
                                                                     'analytic interference.'}}],
                              'extreme': [{'question': 'A 32-year-old with suspected SLE has a '
                                                       'positive ANA (1:640, speckled). dsDNA is '
                                                       'negative, C3/C4 are normal, and she is '
                                                       'clinically well except mild arthralgia. An '
                                                       'extractable nuclear antigen panel shows '
                                                       'anti-SSA/Ro. Which interpretation best '
                                                       'guides the laboratory report commentary?',
                                           'options': ['A) ANA positivity alone equals diagnostic '
                                                       'SLE without clinical criteria',
                                                       'B) Correlate serology with clinical '
                                                       'criteria; anti-SSA may be relevant '
                                                       '(including pregnancy counseling themes) '
                                                       'but does not by itself confirm active '
                                                       'complement-consuming SLE',
                                                       'C) Normal complement excludes all '
                                                       'autoimmune disease permanently',
                                                       'D) Speckled ANA proves drug-induced lupus '
                                                       'from histones only'],
                                           'answer': 'B) Correlate serology with clinical '
                                                     'criteria; anti-SSA may be relevant '
                                                     '(including pregnancy counseling themes) but '
                                                     'does not by itself confirm active '
                                                     'complement-consuming SLE',
                                           'explanation': 'Autoantibody results are interpreted '
                                                          'with clinical classification criteria. '
                                                          'High-titer ANA with anti-SSA needs '
                                                          'clinical correlation; absent dsDNA and '
                                                          'normal complement argue against highly '
                                                          'active classical SLE nephritis '
                                                          'patterns. Anti-SSA has '
                                                          'obstetric/neonatal lupus implications. '
                                                          'ANA alone is not diagnostic; speckled '
                                                          'pattern is not histone-specific DIL.',
                                           'choice_explanations': {'A': 'ANA is sensitive but '
                                                                        'nonspecific; diagnosis '
                                                                        'requires clinical '
                                                                        'criteria, not serology '
                                                                        'alone.',
                                                                   'B': 'Report with clinical '
                                                                        'correlation: anti-SSA is '
                                                                        'meaningful, yet normal '
                                                                        'complement/negative dsDNA '
                                                                        'and mild symptoms do not '
                                                                        'equal active severe SLE '
                                                                        'by labs alone.',
                                                                   'C': 'Complement can be normal '
                                                                        'in many autoimmune '
                                                                        'states; normal levels do '
                                                                        'not exclude disease.',
                                                                   'D': 'Drug-induced lupus is '
                                                                        'classically anti-histone '
                                                                        'associated; speckled ANA '
                                                                        'is not specific for that '
                                                                        'entity.'}},
                                          {'question': 'An IGRA (interferon-gamma release assay) '
                                                       'is drawn for TB infection screening. The '
                                                       'mitogen control is low and the TB antigen '
                                                       'response is also low. Which laboratory '
                                                       'interpretation is correct?',
                                           'options': ['A) Definitive latent TB diagnosis because '
                                                       'any low signal means infection',
                                                       'B) Negative IGRA excluding TB with '
                                                       'certainty despite failed mitogen',
                                                       'C) Indeterminate result from inadequate '
                                                       'T-cell response/control failure — do not '
                                                       'report as negative; recollect/investigate '
                                                       'immune status',
                                                       'D) Convert automatically to a positive '
                                                       'acid-fast smear report'],
                                           'answer': 'C) Indeterminate result from inadequate '
                                                     'T-cell response/control failure — do not '
                                                     'report as negative; recollect/investigate '
                                                     'immune status',
                                           'explanation': 'IGRAs require a valid mitogen '
                                                          '(positive) control showing T cells can '
                                                          'produce IFN-γ. Failed mitogen controls '
                                                          'make the assay indeterminate—common in '
                                                          'immunosuppression—and preclude a '
                                                          'negative interpretation. Repeat testing '
                                                          'and clinical/risk assessment follow; '
                                                          'IGRA is not an AFB smear.',
                                           'choice_explanations': {'A': 'Low TB-antigen with '
                                                                        'failed mitogen is '
                                                                        'indeterminate, not '
                                                                        'diagnostic of infection.',
                                                                   'B': 'Without a valid mitogen '
                                                                        'control, a negative call '
                                                                        'is invalid.',
                                                                   'C': 'Failed mitogen → '
                                                                        'indeterminate IGRA; '
                                                                        'recollect and consider '
                                                                        'host immunity—do not '
                                                                        'release as negative.',
                                                                   'D': 'IGRA immunology results '
                                                                        'must never be rewritten '
                                                                        'as microscopy smear '
                                                                        'reports.'}},
                                          {'question': 'Cold agglutinin disease workup requires '
                                                       'special specimen handling. Which practice '
                                                       'best preserves detection of clinically '
                                                       'significant cold autoantibodies?',
                                           'options': ['A) Always freeze whole blood to −80 °C '
                                                       'before reverse typing',
                                                       'B) Warm the patient only and never control '
                                                       'specimen temperature',
                                                       'C) Use ice baths exclusively for all ABO '
                                                       'discrepancy resolutions',
                                                       'D) Collect and maintain at 37 °C until '
                                                       'serum separation/testing as method '
                                                       'requires; avoid refrigerated clotting that '
                                                       'binds antibody onto RBCs'],
                                           'answer': 'D) Collect and maintain at 37 °C until serum '
                                                     'separation/testing as method requires; avoid '
                                                     'refrigerated clotting that binds antibody '
                                                     'onto RBCs',
                                           'explanation': 'Cold agglutinins bind RBCs at low '
                                                          'temperature. If blood cools before '
                                                          'separation, antibody adsorbs onto '
                                                          'cells, depleting serum titer and '
                                                          'causing spurious CBC/typing problems. '
                                                          'Warm collection/transport and 37 °C '
                                                          'handling per procedure recover plasma '
                                                          'antibody for titration and thermal '
                                                          'amplitude studies.',
                                           'choice_explanations': {'A': 'Freezing whole blood '
                                                                        'damages cells and is '
                                                                        'inappropriate for '
                                                                        'cold-agglutinin serology.',
                                                                   'B': 'Patient warming alone '
                                                                        'does not fix in-vitro '
                                                                        'specimen temperature '
                                                                        'errors.',
                                                                   'C': 'Ice accentuates cold '
                                                                        'binding and can worsen '
                                                                        'artifacts; cold studies '
                                                                        'are controlled, not '
                                                                        'indiscriminate icing of '
                                                                        'all ABO work.',
                                                                   'D': 'Keeping specimens at 37 '
                                                                        '°C until separation '
                                                                        'prevents cold '
                                                                        'autoantibody adsorption '
                                                                        'and preserves detectable '
                                                                        'serum antibody.'}}]},
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
                'questions': {'easy': [{'question': 'Forward ABO typing primarily detects which '
                                                    'targets on patient red cells?',
                                        'options': ['A) A and B antigens using reagent antisera',
                                                    'B) Unexpected IgG alloantibodies in plasma '
                                                    'only',
                                                    'C) HLA Class II alleles by serology alone',
                                                    'D) Hemoglobin S polymerization under hypoxia'],
                                        'answer': 'A) A and B antigens using reagent antisera',
                                        'explanation': 'Forward typing mixes patient RBCs with '
                                                       'anti-A and anti-B reagents to detect A/B '
                                                       'antigens. Reverse typing separately tests '
                                                       'plasma for isoagglutinins. Antibody '
                                                       'screens detect unexpected alloantibodies; '
                                                       'HLA and sickle assays are different tests.',
                                        'choice_explanations': {'A': 'Forward typing uses reagent '
                                                                     'anti-A/anti-B to identify A '
                                                                     'and B antigens on patient '
                                                                     'erythrocytes.',
                                                                'B': 'Unexpected alloantibodies '
                                                                     'are detected by antibody '
                                                                     'screen/panel, not forward '
                                                                     'ABO antigen typing.',
                                                                'C': 'HLA typing is '
                                                                     'molecular/serologic '
                                                                     'transplant testing, not ABO '
                                                                     'forward typing.',
                                                                'D': 'Hemoglobin S solubility/HPLC '
                                                                     'assays diagnose sickle '
                                                                     'traits/disease, not ABO '
                                                                     'antigens.'}},
                                       {'question': 'What is the primary purpose of an '
                                                    'immediate-spin or electronic crossmatch (when '
                                                    'eligibility criteria are met)?',
                                        'options': ['A) Quantify CMV viral load in the donor unit',
                                                    'B) Confirm ABO compatibility between donor '
                                                    'RBCs and recipient',
                                                    'C) Replace the need for antibody screen in '
                                                    'all patients forever',
                                                    'D) Sterilize the donor unit of bacteria'],
                                        'answer': 'B) Confirm ABO compatibility between donor RBCs '
                                                  'and recipient',
                                        'explanation': 'Crossmatch verifies ABO compatibility '
                                                       '(and, in full serologic XM, detects '
                                                       'antibodies to donor antigens). Electronic '
                                                       'crossmatch requires two blood types, '
                                                       'negative antibody screen, and system '
                                                       'controls. It does not measure CMV, '
                                                       'sterilize units, or abolish screening '
                                                       'requirements outside eligibility rules.',
                                        'choice_explanations': {'A': 'CMV status is a donor '
                                                                     'attribute/labeling issue, '
                                                                     'not determined by '
                                                                     'crossmatch.',
                                                                'B': 'Crossmatch confirms the '
                                                                     'selected unit is '
                                                                     'ABO-compatible with the '
                                                                     'recipient (and may detect '
                                                                     'incompatibilities '
                                                                     'serologically).',
                                                                'C': 'Antibody screens remain '
                                                                     'foundational; electronic XM '
                                                                     'is allowed only when '
                                                                     'screen-negative criteria are '
                                                                     'met.',
                                                                'D': 'Crossmatch is a '
                                                                     'compatibility test, not a '
                                                                     'sterilization process.'}},
                                       {'question': 'In life-threatening hemorrhage before '
                                                    'type-specific blood is available, which RBC '
                                                    'product theme is used for emergency release?',
                                        'options': ['A) Autologous frozen rare units only',
                                                    'B) Platelet concentrates exclusively without '
                                                    'RBCs',
                                                    'C) Group O RBCs (often O-negative for women '
                                                    'of childbearing potential per policy) '
                                                    'uncrossmatched',
                                                    'D) AB plasma as a red-cell substitute'],
                                        'answer': 'C) Group O RBCs (often O-negative for women of '
                                                  'childbearing potential per policy) '
                                                  'uncrossmatched',
                                        'explanation': 'Emergency transfusion uses group O RBCs '
                                                       'when delay for typing/crossmatch would '
                                                       'threaten life. Policies often reserve '
                                                       'O-neg for women of childbearing potential '
                                                       'to avoid D alloimmunization; O-pos may be '
                                                       'used for men/postmenopausal women when '
                                                       'inventory demands. Switch to type-specific '
                                                       'ASAP.',
                                        'choice_explanations': {'A': 'Autologous rare units are '
                                                                     'not the standard first '
                                                                     'emergency RBC for unknown '
                                                                     'patients.',
                                                                'B': 'Platelets do not replace '
                                                                     'oxygen-carrying RBC needs in '
                                                                     'hemorrhagic shock.',
                                                                'C': 'Uncrossmatched group O RBCs '
                                                                     'are the emergency RBC '
                                                                     'standard until type-specific '
                                                                     'blood is ready.',
                                                                'D': 'AB plasma is a plasma '
                                                                     'product for coagulation '
                                                                     'factors, not an RBC '
                                                                     'substitute.'}}],
                              'medium': [{'question': 'Rh immune globulin (RhIG) is indicated '
                                                      'primarily to prevent which alloimmunization '
                                                      'scenario?',
                                          'options': ['A) Anti-A formation in group O adults after '
                                                      'diet change',
                                                      'B) Platelet refractoriness from HLA '
                                                      'antibodies only',
                                                      'C) Cold agglutinin disease onset after '
                                                      'Mycoplasma',
                                                      'D) Anti-D formation in D-negative '
                                                      'individuals exposed to D-positive RBCs '
                                                      '(e.g., pregnancy)'],
                                          'answer': 'D) Anti-D formation in D-negative individuals '
                                                    'exposed to D-positive RBCs (e.g., pregnancy)',
                                          'explanation': 'RhIG provides passive anti-D that '
                                                         'prevents D-negative mothers from forming '
                                                         'immune anti-D after fetal D-positive '
                                                         'exposure, reducing HDFN risk. It is not '
                                                         'used for ABO isoagglutinins, HLA '
                                                         'refractoriness, or cold agglutinin '
                                                         'disease.',
                                          'choice_explanations': {'A': 'Anti-A isoagglutinins are '
                                                                       'naturally occurring; RhIG '
                                                                       'does not prevent them.',
                                                                  'B': 'HLA alloimmunization '
                                                                       'management differs; RhIG '
                                                                       'targets anti-D prevention.',
                                                                  'C': 'Cold agglutinins are '
                                                                       'autoantibodies; RhIG is '
                                                                       'not therapy for CAD.',
                                                                  'D': 'RhIG prevents alloanti-D '
                                                                       'in D-negative persons '
                                                                       'after D-positive RBC '
                                                                       'exposure, classically in '
                                                                       'pregnancy.'}},
                                         {'question': 'Acute intravascular hemolytic transfusion '
                                                      'reactions are most often caused by which '
                                                      'incompatibility?',
                                          'options': ['A) ABO-incompatible RBC transfusion '
                                                      '(clerical/identification error)',
                                                      'B) Mild allergic urticaria from plasma '
                                                      'proteins only',
                                                      'C) Iron overload after one unit in a naïve '
                                                      'recipient',
                                                      'D) Citrate toxicity without hemolysis'],
                                          'answer': 'A) ABO-incompatible RBC transfusion '
                                                    '(clerical/identification error)',
                                          'explanation': 'Preformed ABO isoagglutinins bind '
                                                         'incompatible donor RBCs, activate '
                                                         'complement, and cause intravascular '
                                                         'hemolysis—usually from '
                                                         'misidentification. Prevention centers on '
                                                         'bedside identification and clerical '
                                                         'checks. Allergic reactions, iron '
                                                         'overload, and citrate effects are '
                                                         'different transfusion complications.',
                                          'choice_explanations': {'A': 'ABO mismatch from '
                                                                       'identification errors is '
                                                                       'the classic cause of acute '
                                                                       'intravascular HTR.',
                                                                  'B': 'Urticarial allergic '
                                                                       'reactions are '
                                                                       'histamine-mediated and not '
                                                                       'intravascular hemolysis.',
                                                                  'C': 'Iron overload is a chronic '
                                                                       'transfusion complication, '
                                                                       'not acute intravascular '
                                                                       'hemolysis from one unit.',
                                                                  'D': 'Citrate can cause '
                                                                       'hypocalcemia with massive '
                                                                       'transfusion but is not '
                                                                       'hemolysis.'}},
                                         {'question': 'A positive direct antiglobulin test (DAT) '
                                                      'indicates which in vivo finding?',
                                          'options': ['A) Only that the antibody screen must be '
                                                      'negative',
                                                      'B) In vivo coating of RBCs with IgG and/or '
                                                      'complement',
                                                      'C) That reverse typing reagents are expired '
                                                      'only',
                                                      'D) Definite proof of laboratory sample '
                                                      'mix-up alone'],
                                          'answer': 'B) In vivo coating of RBCs with IgG and/or '
                                                    'complement',
                                          'explanation': 'DAT detects IgG/complement already bound '
                                                         'to circulating RBCs (autoimmune '
                                                         'hemolysis, HDFN, drug reactions, '
                                                         'alloimmune HTRs). It does not by itself '
                                                         'prove mix-up or dictate antibody screen '
                                                         'results. Elution/identification clarify '
                                                         'antibody specificity when needed.',
                                          'choice_explanations': {'A': 'DAT and antibody screen '
                                                                       'assess different '
                                                                       'compartments (RBC-bound vs '
                                                                       'plasma antibody); both can '
                                                                       'be positive.',
                                                                  'B': 'DAT positivity means IgG '
                                                                       'and/or complement are '
                                                                       'bound to RBCs in vivo.',
                                                                  'C': 'Reagent expiration is a QC '
                                                                       'issue unrelated to the '
                                                                       'biologic meaning of a '
                                                                       'positive DAT.',
                                                                  'D': 'Mix-ups are identification '
                                                                       'errors; DAT reflects '
                                                                       'immune coating, not proof '
                                                                       'of mix-up alone.'}}],
                              'hard': [{'question': 'Antibody screen is positive. What is the '
                                                    'usual next immunohematology step before '
                                                    'selecting RBC units?',
                                        'options': ['A) Issue any ABO-compatible unit without '
                                                    'further testing',
                                                    'B) Perform DAT only and skip identification '
                                                    'panels',
                                                    'C) Antibody identification panel (± '
                                                    'phenotyping/genotype) to define specificity '
                                                    'and clinical significance',
                                                    'D) Sterile docking platelets into the RBC '
                                                    'unit'],
                                        'answer': 'C) Antibody identification panel (± '
                                                  'phenotyping/genotype) to define specificity and '
                                                  'clinical significance',
                                        'explanation': 'A positive screen requires antibody '
                                                       'identification using panel cells, then '
                                                       'selection of antigen-negative units for '
                                                       'clinically significant alloantibodies, '
                                                       'with crossmatch. Skipping ID risks '
                                                       'incompatible transfusion. DAT may be '
                                                       'adjunctive but does not replace '
                                                       'alloantibody ID.',
                                        'choice_explanations': {'A': 'Issuing without antibody ID '
                                                                     'risks missing clinically '
                                                                     'significant alloantibodies.',
                                                                'B': 'DAT evaluates in vivo '
                                                                     'coating; alloantibody ID '
                                                                     'still needs panel studies.',
                                                                'C': 'Panel identification (± '
                                                                     'phenotyping) defines '
                                                                     'antibody specificity so '
                                                                     'antigen-negative units can '
                                                                     'be issued safely.',
                                                                'D': 'Combining platelets into '
                                                                     'RBCs is not an antibody-ID '
                                                                     'method.'}},
                                       {'question': 'Differentiating TRALI from TACO after '
                                                    'transfusion most hinges on which '
                                                    'clinical–laboratory contrast?',
                                        'options': ['A) Both are identical hydrostatic edema '
                                                    'syndromes by definition',
                                                    'B) TRALI never shows hypoxemia whereas TACO '
                                                    'always does',
                                                    'C) TACO is rare before age 1 only',
                                                    'D) TRALI: permeability/inflammatory edema '
                                                    'often with fever/hypotension and normal/low '
                                                    'BNP; TACO: hydrostatic overload with '
                                                    'hypertension and elevated BNP'],
                                        'answer': 'D) TRALI: permeability/inflammatory edema often '
                                                  'with fever/hypotension and normal/low BNP; '
                                                  'TACO: hydrostatic overload with hypertension '
                                                  'and elevated BNP',
                                        'explanation': 'Both cause acute pulmonary edema '
                                                       'post-transfusion, but TRALI is '
                                                       'permeability injury (often fever, '
                                                       'hypotension, non-elevated BNP) whereas '
                                                       'TACO is volume overload (hypertension, '
                                                       'high BNP, response to diuretics). '
                                                       'Distinguishing them guides management and '
                                                       'donor/product follow-up.',
                                        'choice_explanations': {'A': 'TRALI and TACO differ in '
                                                                     'mechanism—permeability vs '
                                                                     'hydrostatic—despite '
                                                                     'overlapping imaging.',
                                                                'B': 'Both feature hypoxemia; gas '
                                                                     'exchange failure does not '
                                                                     'separate them.',
                                                                'C': 'TACO can occur at any age '
                                                                     'with volume intolerance; it '
                                                                     'is not limited to infants.',
                                                                'D': 'Clinical hemodynamics and '
                                                                     'BNP help separate TRALI '
                                                                     '(permeability) from TACO '
                                                                     '(overload).'}},
                                       {'question': 'Massive transfusion protocols address which '
                                                    'constellation of laboratory/clinical problems '
                                                    'beyond anemia alone?',
                                        'options': ['A) Coagulopathy, citrate effects, electrolyte '
                                                    'shifts (↓Ca, ↓K or ↑K), and hypothermia '
                                                    'themes',
                                                    'B) Only hyperglycemia management',
                                                    'C) Exclusive treatment of iron deficiency '
                                                    'without plasma/platelets',
                                                    'D) Prevention of all future alloantibodies by '
                                                    'giving random plasma'],
                                        'answer': 'A) Coagulopathy, citrate effects, electrolyte '
                                                  'shifts (↓Ca, ↓K or ↑K), and hypothermia themes',
                                        'explanation': 'Massive transfusion replaces RBCs plus '
                                                       'plasma/platelets in ratios, while '
                                                       'monitoring ionized calcium (citrate '
                                                       'binding), potassium, acid–base status, and '
                                                       'temperature. Focusing only on hemoglobin '
                                                       'ignores dilutional coagulopathy and '
                                                       'metabolic complications.',
                                        'choice_explanations': {'A': 'MTP care targets oxygen '
                                                                     'delivery plus coagulopathy '
                                                                     'and metabolic sequelae of '
                                                                     'large-volume transfusion.',
                                                                'B': 'Glucose control may matter '
                                                                     'clinically but is not the '
                                                                     'defining MTP laboratory '
                                                                     'problem set.',
                                                                'C': 'Iron deficiency is '
                                                                     'irrelevant to acute '
                                                                     'hemorrhagic MTP component '
                                                                     'therapy.',
                                                                'D': 'Random plasma does not '
                                                                     'prevent alloimmunization; '
                                                                     'antigen matching and RhIG '
                                                                     'policies do.'}}],
                              'extreme': [{'question': 'A trauma patient is exsanguinating. The '
                                                       'blood bank has just received an unlabeled '
                                                       'emergency specimen. Two prior historical '
                                                       'types in the LIS conflict (one A-pos, one '
                                                       'O-pos). The OR demands blood now. Which '
                                                       'action best protects the patient?',
                                           'options': ['A) Issue A-positive RBCs based on the more '
                                                       'recent historical type without a current '
                                                       'specimen',
                                                       'B) Issue emergency group O RBCs '
                                                       '(policy-appropriate Rh), obtain a properly '
                                                       'labeled current specimen for typing ASAP, '
                                                       'and resolve the historical discrepancy '
                                                       'before switching to type-specific units',
                                                       'C) Delay all transfusion until both '
                                                       'historical records are deleted',
                                                       'D) Issue AB-positive RBCs as universal red '
                                                       'cells'],
                                           'answer': 'B) Issue emergency group O RBCs '
                                                     '(policy-appropriate Rh), obtain a properly '
                                                     'labeled current specimen for typing ASAP, '
                                                     'and resolve the historical discrepancy '
                                                     'before switching to type-specific units',
                                           'explanation': 'Conflicting historical ABO types are a '
                                                          'critical identity/safety signal. In '
                                                          'life-threatening bleed, give emergency '
                                                          'O RBCs while securing a correctly '
                                                          'labeled current sample. Do not issue '
                                                          'type-specific blood until discrepancy '
                                                          'resolution. AB RBCs are not universal '
                                                          'donor red cells (O is).',
                                           'choice_explanations': {'A': 'Conflicting histories '
                                                                        'forbid trusting a single '
                                                                        'prior type for non-O '
                                                                        'issue without a verified '
                                                                        'current specimen.',
                                                                   'B': 'Emergency O RBCs bridge '
                                                                        'life-saving care while a '
                                                                        'valid sample and '
                                                                        'discrepancy workup '
                                                                        'protect against ABO '
                                                                        'disaster.',
                                                                   'C': 'Withholding all blood '
                                                                        'during exsanguination '
                                                                        'causes preventable death; '
                                                                        'emergency O is the '
                                                                        'bridge.',
                                                                   'D': 'Group AB RBCs express A '
                                                                        'and B antigens and are '
                                                                        'not universal donor red '
                                                                        'cells.'}},
                                          {'question': 'A warm autoimmune hemolytic anemia patient '
                                                       'needs RBC transfusion. Panagglutination is '
                                                       'present in serum and DAT is IgG-positive. '
                                                       'Adsorption studies reveal an underlying '
                                                       'anti-e. Which crossmatch/transfusion '
                                                       'strategy is most appropriate?',
                                           'options': ['A) Refuse all transfusion regardless of '
                                                       'life-threatening anemia',
                                                       'B) Transfuse random ABO-compatible units '
                                                       'without regard to e antigen or autocontrol',
                                                       'C) Provide e-negative, ABO-compatible '
                                                       'units that are least incompatible after '
                                                       'autoadsorption workup, with close clinical '
                                                       'monitoring',
                                                       'D) Issue only platelets because RBCs will '
                                                       'always hemolyze completely'],
                                           'answer': 'C) Provide e-negative, ABO-compatible units '
                                                     'that are least incompatible after '
                                                     'autoadsorption workup, with close clinical '
                                                     'monitoring',
                                           'explanation': 'In WAIHA, autoantibodies complicate '
                                                          'crossmatching. After separating auto '
                                                          'from alloantibody (adsorption), '
                                                          'antigen-negative units for clinically '
                                                          'significant alloantibodies are '
                                                          'selected; units may still be '
                                                          '“incompatible” with autoantibody but '
                                                          'are the safest available. Withhold only '
                                                          'if anemia is not life-threatening; '
                                                          'platelets do not treat RBC oxygen debt.',
                                           'choice_explanations': {'A': 'Life-threatening anemia '
                                                                        'may still require '
                                                                        'transfusion despite '
                                                                        'serologic difficulty.',
                                                                   'B': 'Ignoring identified '
                                                                        'anti-e risks alloimmune '
                                                                        'hemolysis layered on '
                                                                        'WAIHA.',
                                                                   'C': 'After adsorption reveals '
                                                                        'anti-e, select e-negative '
                                                                        'ABO-compatible '
                                                                        'least-incompatible units '
                                                                        'and monitor closely.',
                                                                   'D': 'Platelets do not replace '
                                                                        'RBC transfusion needs in '
                                                                        'severe anemia.'}},
                                          {'question': 'A platelet unit stored at room temperature '
                                                       'on an agitator is requested for a '
                                                       'neutropenic patient with mucositis. The '
                                                       'unit bag is swollen and discolored 24 '
                                                       'hours after issue eligibility checks. '
                                                       'Culture is pending. What is the safest '
                                                       'blood-bank decision?',
                                           'options': ['A) Issue anyway because platelets are '
                                                       'always culture-negative at release',
                                                       'B) Warm the unit further to reduce '
                                                       'bacterial growth before issue',
                                                       'C) Irradiate only and ignore visual '
                                                       'anomalies',
                                                       'D) Quarantine/do not issue the visually '
                                                       'abnormal unit; investigate bacterial '
                                                       'contamination risk and report per '
                                                       'procedure'],
                                           'answer': 'D) Quarantine/do not issue the visually '
                                                     'abnormal unit; investigate bacterial '
                                                     'contamination risk and report per procedure',
                                           'explanation': 'Room-temperature platelet storage '
                                                          'supports bacterial proliferation. '
                                                          'Swelling/discoloration are classic '
                                                          'contamination warnings. Do not '
                                                          'transfuse; quarantine, culture, notify '
                                                          'clinicians/suppliers, and document. '
                                                          'Irradiation prevents TA-GVHD but does '
                                                          'not sterilize bacteria; warming worsens '
                                                          'growth.',
                                           'choice_explanations': {'A': 'Visual abnormalities '
                                                                        'override prior release '
                                                                        'checks—bacterial '
                                                                        'contamination can evolve '
                                                                        'after testing.',
                                                                   'B': 'Warming increases '
                                                                        'bacterial growth risk and '
                                                                        'is contraindicated.',
                                                                   'C': 'Irradiation does not '
                                                                        'eliminate bacterial '
                                                                        'contamination concerns '
                                                                        'from a swollen/discolored '
                                                                        'bag.',
                                                                   'D': 'Quarantine and '
                                                                        'investigate suspected '
                                                                        'contaminated '
                                                                        'platelets—never '
                                                                        'issue.'}}]},
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
                    'questions': {'easy': [{'question': 'What is the primary purpose of formalin '
                                                        'fixation before routine paraffin '
                                                        'processing?',
                                            'options': ['A) Preserve tissue morphology by '
                                                        'cross-linking proteins and preventing '
                                                        'autolysis/putrefaction',
                                                        'B) Dissolve all nuclei so only cytoplasm '
                                                        'remains',
                                                        'C) Sterilize slides after coverslipping '
                                                        'only',
                                                        'D) Replace the need for gross examination '
                                                        'entirely'],
                                            'answer': 'A) Preserve tissue morphology by '
                                                      'cross-linking proteins and preventing '
                                                      'autolysis/putrefaction',
                                            'explanation': 'Aldehyde fixatives (buffered formalin) '
                                                           'cross-link proteins, halt autolysis, '
                                                           'and harden tissue for processing while '
                                                           'preserving morphologic detail for H&E. '
                                                           'Fixation does not eliminate grossing, '
                                                           'nor should it destroy nuclei.',
                                            'choice_explanations': {'A': 'Formalin fixation '
                                                                         'stabilizes proteins and '
                                                                         'preserves microscopic '
                                                                         'architecture for '
                                                                         'diagnosis.',
                                                                    'B': 'Nuclei must be preserved '
                                                                         'for diagnosis; fixation '
                                                                         'should not dissolve '
                                                                         'them.',
                                                                    'C': 'Sterility after '
                                                                         'coverslipping is '
                                                                         'unrelated to primary '
                                                                         'fixation purpose.',
                                                                    'D': 'Gross examination '
                                                                         'remains essential for '
                                                                         'sampling and staging '
                                                                         'context.'}},
                                           {'question': 'Hematoxylin and eosin (H&E) staining is '
                                                        'used primarily to demonstrate which '
                                                        'tissue features?',
                                            'options': ['A) Only acid-fast mycobacteria without '
                                                        'morphology',
                                                        'B) General morphology — nuclei '
                                                        '(hematoxylin) and '
                                                        'cytoplasmic/extracellular detail (eosin)',
                                                        'C) Amyloid confirmed without Congo red',
                                                        'D) Iron stores better than Prussian blue '
                                                        'always'],
                                            'answer': 'B) General morphology — nuclei '
                                                      '(hematoxylin) and cytoplasmic/extracellular '
                                                      'detail (eosin)',
                                            'explanation': 'H&E is the routine stain: hematoxylin '
                                                           'colors nuclei blue/purple; eosin '
                                                           'colors cytoplasm and extracellular '
                                                           'matrix pink. Special stains/IHC '
                                                           'address organisms, amyloid, iron, and '
                                                           'specific antigens.',
                                            'choice_explanations': {'A': 'Acid-fast organisms need '
                                                                         'AFB stains; H&E is '
                                                                         'general morphology.',
                                                                    'B': 'H&E provides the '
                                                                         'standard '
                                                                         'nuclear–cytoplasmic '
                                                                         'morphologic overview for '
                                                                         'histopathology.',
                                                                    'C': 'Amyloid requires Congo '
                                                                         'red (± polarized light), '
                                                                         'not H&E alone for '
                                                                         'confirmation.',
                                                                    'D': 'Iron is demonstrated '
                                                                         'with Prussian blue; H&E '
                                                                         'is nonspecific for iron '
                                                                         'stores.'}},
                                           {'question': 'A Pap test specimen is best categorized '
                                                        'as which kind of laboratory sample?',
                                            'options': ['A) Fresh intraoperative frozen section of '
                                                        'liver',
                                                        'B) Twenty-four-hour urine for creatinine '
                                                        'clearance only',
                                                        'C) Cytologic screening specimen for '
                                                        'cervical/vaginal cells',
                                                        'D) Anaerobic wound culture swab '
                                                        'exclusively'],
                                            'answer': 'C) Cytologic screening specimen for '
                                                      'cervical/vaginal cells',
                                            'explanation': 'Pap tests collect cervical cytology '
                                                           'for morphologic screening of '
                                                           'squamous/glandular lesions and '
                                                           'infectious changes, often with HPV '
                                                           'cotesting. They are not frozen '
                                                           'sections, chemistry clearances, or '
                                                           'culture swabs.',
                                            'choice_explanations': {'A': 'Frozen section is '
                                                                         'intraoperative tissue '
                                                                         'histology, not Pap '
                                                                         'cytology.',
                                                                    'B': 'Creatinine clearance is '
                                                                         'a chemistry function '
                                                                         'test on timed urine.',
                                                                    'C': 'Pap specimens are '
                                                                         'cytologic preparations '
                                                                         'for cervical cancer '
                                                                         'screening pathways.',
                                                                    'D': 'Culture swabs are '
                                                                         'microbiology specimens; '
                                                                         'Pap is cytology.'}}],
                                  'medium': [{'question': 'Immunohistochemistry (IHC) detects '
                                                          'targets in tissue by which mechanism?',
                                              'options': ['A) Measuring serum enzyme activity only',
                                                          'B) Karyotyping metaphase cells from '
                                                          'culture',
                                                          'C) Quantifying blood gases in paraffin '
                                                          'blocks',
                                                          'D) Antibody binding to tissue antigens '
                                                          'with a visualized reporter'],
                                              'answer': 'D) Antibody binding to tissue antigens '
                                                        'with a visualized reporter',
                                              'explanation': 'IHC uses primary antibodies against '
                                                             'cellular antigens plus detection '
                                                             'systems (enzymes/fluorophores) to '
                                                             'localize proteins in situ—critical '
                                                             'for tumor classification and '
                                                             'predictive markers. It is distinct '
                                                             'from serum chemistry, cytogenetics, '
                                                             'and blood gas analysis.',
                                              'choice_explanations': {'A': 'Serum enzyme assays '
                                                                           'are clinical '
                                                                           'chemistry, not tissue '
                                                                           'IHC.',
                                                                      'B': 'Karyotyping is '
                                                                           'cytogenetics on '
                                                                           'dividing cells.',
                                                                      'C': 'Blood gases are not '
                                                                           'measured in paraffin '
                                                                           'sections.',
                                                                      'D': 'IHC visualizes '
                                                                           'antibody–antigen '
                                                                           'binding in tissue with '
                                                                           'chromogenic or '
                                                                           'fluorescent '
                                                                           'reporters.'}},
                                             {'question': 'Frozen section consultation is '
                                                          'primarily indicated for which '
                                                          'intraoperative need?',
                                              'options': ['A) Rapid intraoperative '
                                                          'diagnosis/margin assessment to guide '
                                                          'surgery',
                                                          'B) Elective research biobanking without '
                                                          'surgical decisions',
                                                          'C) Routine storage of all placentas for '
                                                          '10 years only',
                                                          'D) Replacing formalin fixation for all '
                                                          'permanent diagnoses'],
                                              'answer': 'A) Rapid intraoperative diagnosis/margin '
                                                        'assessment to guide surgery',
                                              'explanation': 'Frozen sections provide rapid '
                                                             'histologic guidance (margins, '
                                                             'confirmation of lesional tissue). '
                                                             'Permanent formalin-fixed paraffin '
                                                             'sections remain the gold standard '
                                                             'for final diagnosis because freezing '
                                                             'artifacts limit detail.',
                                              'choice_explanations': {'A': 'Frozen section’s '
                                                                           'purpose is immediate '
                                                                           'surgical guidance via '
                                                                           'rapid microscopy.',
                                                                      'B': 'Research banking is '
                                                                           'not the clinical '
                                                                           'indication for frozen '
                                                                           'section consultation.',
                                                                      'C': 'Long-term storage '
                                                                           'policies are '
                                                                           'administrative, not '
                                                                           'frozen-section '
                                                                           'indications.',
                                                                      'D': 'Permanent FFPE '
                                                                           'diagnosis is not '
                                                                           'replaced by frozen '
                                                                           'section for final '
                                                                           'reporting.'}},
                                             {'question': 'Why does inadequate tumor content on a '
                                                          'small biopsy threaten molecular '
                                                          'oncology testing?',
                                              'options': ['A) Molecular assays ignore neoplastic '
                                                          'cellularity requirements',
                                                          'B) Inadequate neoplastic cellularity '
                                                          'risks false-negative mutation/fusion '
                                                          'calls',
                                                          'C) Extra stroma always improves '
                                                          'analytic sensitivity',
                                                          'D) Only blood contamination improves '
                                                          'DNA yield quality always'],
                                              'answer': 'B) Inadequate neoplastic cellularity '
                                                        'risks false-negative mutation/fusion '
                                                        'calls',
                                              'explanation': 'Molecular assays need sufficient '
                                                             'neoplastic DNA/RNA above method '
                                                             'limits of detection. Heavy benign '
                                                             'stroma/inflammation dilutes tumor '
                                                             'signal and can miss actionable '
                                                             'variants. Pathologists assess tumor '
                                                             'content before testing.',
                                              'choice_explanations': {'A': 'Cellular fraction '
                                                                           'requirements are '
                                                                           'central to molecular '
                                                                           'pathology adequacy.',
                                                                      'B': 'Low tumor content can '
                                                                           'falsely negative '
                                                                           'molecular results by '
                                                                           'diluting mutant '
                                                                           'alleles.',
                                                                      'C': 'Excess stroma dilutes '
                                                                           'tumor nucleic acid and '
                                                                           'harms sensitivity.',
                                                                      'D': 'Blood contamination '
                                                                           'can inhibit or dilute '
                                                                           'assays; it does not '
                                                                           'reliably improve '
                                                                           'quality.'}}],
                                  'hard': [{'question': 'Prolonged cold ischemia before fixation '
                                                        'most likely causes which laboratory '
                                                        'problem?',
                                            'options': ['A) Improved IHC intensity for all '
                                                        'phosphoproteins always',
                                                        'B) Guaranteed sterility without formalin',
                                                        'C) Autolysis/degradation that distorts '
                                                        'morphology and impairs IHC/molecular '
                                                        'integrity',
                                                        'D) Instantaneous paraffin infiltration '
                                                        'without processing'],
                                            'answer': 'C) Autolysis/degradation that distorts '
                                                      'morphology and impairs IHC/molecular '
                                                      'integrity',
                                            'explanation': 'Delay between excision and fixation '
                                                           'allows enzymatic degradation, harming '
                                                           'nuclear detail, antigenicity, and '
                                                           'nucleic acids. Cold ischemia time is a '
                                                           'critical preanalytic variable for '
                                                           'morphology, IHC, and molecular tests.',
                                            'choice_explanations': {'A': 'Phospho-epitopes are '
                                                                         'especially labile; delay '
                                                                         'usually worsens, not '
                                                                         'improves, IHC.',
                                                                    'B': 'Cold ischemia does not '
                                                                         'sterilize tissue or '
                                                                         'replace fixation.',
                                                                    'C': 'Autolysis from delayed '
                                                                         'fixation degrades '
                                                                         'morphology and '
                                                                         'biomolecules needed for '
                                                                         'IHC/molecular assays.',
                                                                    'D': 'Paraffin infiltration '
                                                                         'requires controlled '
                                                                         'processing after '
                                                                         'fixation/dehydration—not '
                                                                         'an automatic result of '
                                                                         'delay.'}},
                                           {'question': 'Which special stain category is most '
                                                        'appropriate when acid-fast organisms are '
                                                        'suspected in tissue?',
                                            'options': ['A) Oil red O on paraffin sections without '
                                                        'fixation concern',
                                                        'B) Prussian blue for ferric iron only',
                                                        'C) Reticulin stain for type III collagen '
                                                        'framework only',
                                                        'D) Ziehl–Neelsen/Fite or auramine-type '
                                                        'acid-fast stains'],
                                            'answer': 'D) Ziehl–Neelsen/Fite or auramine-type '
                                                      'acid-fast stains',
                                            'explanation': 'Mycobacteria and related organisms '
                                                           'require acid-fast methods (ZN, Fite '
                                                           'for Nocardia partially, fluorochrome). '
                                                           'Iron, lipid, and reticulin stains '
                                                           'answer different morphologic '
                                                           'questions.',
                                            'choice_explanations': {'A': 'Oil red O demonstrates '
                                                                         'lipids on appropriate '
                                                                         '(often frozen) sections, '
                                                                         'not acid-fast organisms.',
                                                                    'B': 'Prussian blue detects '
                                                                         'iron, not mycobacteria.',
                                                                    'C': 'Reticulin outlines '
                                                                         'architecture, not '
                                                                         'acid-fast bacilli.',
                                                                    'D': 'Acid-fast stains are the '
                                                                         'tissue methods for '
                                                                         'suspected '
                                                                         'mycobacteria/related '
                                                                         'organisms.'}},
                                           {'question': 'Before sending a paraffin block for NGS '
                                                        'oncology panels, which adequacy factor is '
                                                        'most critical to document?',
                                            'options': ['A) Estimated tumor cellularity/nucleic '
                                                        'acid adequacy and appropriate block '
                                                        'selection',
                                                        'B) Patient’s favorite color for report '
                                                        'aesthetics',
                                                        'C) Whether the courier prefers ambient or '
                                                        'iced transport only for glass slides of '
                                                        'H&E already stained',
                                                        'D) Exact number of eosin dips during '
                                                        'staining'],
                                            'answer': 'A) Estimated tumor cellularity/nucleic acid '
                                                      'adequacy and appropriate block selection',
                                            'explanation': 'NGS success depends on selecting '
                                                           'blocks with adequate neoplastic '
                                                           'cellularity and nucleic acid '
                                                           'quality/quantity. Stain cosmetics and '
                                                           'courier preferences for '
                                                           'already-stained slides are irrelevant '
                                                           'to molecular adequacy decisions.',
                                            'choice_explanations': {'A': 'Tumor content and '
                                                                         'nucleic acid adequacy '
                                                                         'determine whether NGS '
                                                                         'can reliably detect '
                                                                         'variants.',
                                                                    'B': 'Report aesthetics are '
                                                                         'unrelated to analytic '
                                                                         'adequacy.',
                                                                    'C': 'Transport of stained '
                                                                         'slides is not the '
                                                                         'molecular adequacy '
                                                                         'criterion for block '
                                                                         'selection.',
                                                                    'D': 'Eosin dip counts do not '
                                                                         'determine DNA/RNA '
                                                                         'adequacy for NGS.'}}],
                                  'extreme': [{'question': 'Two breast lumpectomy specimens arrive '
                                                           'with transposed labels suspected after '
                                                           'the surgeon calls. Grossing has not '
                                                           'begun. Cassette writing would proceed '
                                                           'in 10 minutes. Which action is '
                                                           'mandatory?',
                                               'options': ['A) Guess the correct identity from '
                                                           'specimen size and continue processing '
                                                           'to avoid delay',
                                                           'B) Stop all processing, quarantine '
                                                           'both specimens, and resolve identity '
                                                           'with the clinical team before any '
                                                           'cut-up or reporting',
                                                           'C) Process both as a combined specimen '
                                                           'under one accession',
                                                           'D) Relabel randomly and issue a '
                                                           'preliminary cancer diagnosis'],
                                               'answer': 'B) Stop all processing, quarantine both '
                                                         'specimens, and resolve identity with the '
                                                         'clinical team before any cut-up or '
                                                         'reporting',
                                               'explanation': 'Specimen identity errors can cause '
                                                              'catastrophic wrong-patient therapy. '
                                                              'When labels may be swapped, '
                                                              'processing stops immediately; '
                                                              'specimens are quarantined until '
                                                              'surgical/clinical reconciliation. '
                                                              'Guessing, merging, or fabricating '
                                                              'labels is unacceptable.',
                                               'choice_explanations': {'A': 'Morphologic guessing '
                                                                            'cannot verify patient '
                                                                            'identity and risks '
                                                                            'wrong-site/wrong-patient '
                                                                            'diagnosis.',
                                                                       'B': 'Stop, quarantine, and '
                                                                            'resolve identity '
                                                                            'before any '
                                                                            'processing—the '
                                                                            'non-negotiable safety '
                                                                            'response.',
                                                                       'C': 'Merging potentially '
                                                                            'different patients’ '
                                                                            'tissues destroys '
                                                                            'chain-of-custody and '
                                                                            'interpretability.',
                                                                       'D': 'Random relabeling and '
                                                                            'premature cancer '
                                                                            'diagnosis are '
                                                                            'reportable safety '
                                                                            'events.'}},
                                              {'question': 'A cytology prep from pleural fluid '
                                                           'shows atypical cells concerning for '
                                                           'malignancy on a concentrated cytospin '
                                                           'made in hematology. Automated counts '
                                                           'were released as “normal WBC '
                                                           'differential.” What should happen '
                                                           'next?',
                                               'options': ['A) Leave the normal count report '
                                                           'unchanged without commentary',
                                                           'B) Dilute the fluid until atypical '
                                                           'cells disappear and rerelease',
                                                           'C) Escalate for pathologist/cytology '
                                                           'review, amend/annotate reports per '
                                                           'policy, and notify the clinical team '
                                                           'of possible malignancy',
                                                           'D) Culture the fluid for mycobacteria '
                                                           'only and ignore morphology'],
                                               'answer': 'C) Escalate for pathologist/cytology '
                                                         'review, amend/annotate reports per '
                                                         'policy, and notify the clinical team of '
                                                         'possible malignancy',
                                               'explanation': 'Unexpected atypical/malignant cells '
                                                              'in body fluids are critical '
                                                              'findings. Hematology differentials '
                                                              'must not bury morphology needing '
                                                              'cytology/pathology diagnosis. '
                                                              'Escalate, correct reporting '
                                                              'pathways, and communicate urgently.',
                                               'choice_explanations': {'A': 'A “normal '
                                                                            'differential” is '
                                                                            'misleading if '
                                                                            'malignant cells are '
                                                                            'present—amend and '
                                                                            'escalate.',
                                                                       'B': 'Diluting away '
                                                                            'atypical cells '
                                                                            'falsifies the '
                                                                            'diagnostic specimen.',
                                                                       'C': 'Pathologist/cytology '
                                                                            'review plus clinical '
                                                                            'notification is '
                                                                            'required for '
                                                                            'suspected malignant '
                                                                            'fluid cells.',
                                                                       'D': 'Microbiology may be '
                                                                            'adjunctive, but '
                                                                            'morphologic '
                                                                            'escalation cannot be '
                                                                            'skipped.'}},
                                              {'question': 'A bone biopsy is received for '
                                                           'suspected osteomyelitis and possible '
                                                           'malignancy. The surgeon asks for '
                                                           'routine processing and also culture. '
                                                           'Decalcification is being considered. '
                                                           'Which integrated laboratory plan is '
                                                           'safest?',
                                               'options': ['A) Decalcify the entire specimen in '
                                                           'strong acid immediately so culture and '
                                                           'IHC are still perfect',
                                                           'B) Freeze the whole bone at −80 °C '
                                                           'before any split for culture',
                                                           'C) Submit only crushed fragments in '
                                                           'formalin and discard sterile aliquots',
                                                           'D) Divide specimen thoughtfully: '
                                                           'sterile aliquot for microbiology '
                                                           'before fixative/decalcification; '
                                                           'reserve tissue for histology with '
                                                           'controlled decalcification that '
                                                           'preserves diagnostic needs'],
                                               'answer': 'D) Divide specimen thoughtfully: sterile '
                                                         'aliquot for microbiology before '
                                                         'fixative/decalcification; reserve tissue '
                                                         'for histology with controlled '
                                                         'decalcification that preserves '
                                                         'diagnostic needs',
                                               'explanation': 'Culture requires a sterile, unfixed '
                                                              'sample. Harsh decalcification can '
                                                              'destroy organisms, antigens, and '
                                                              'nucleic acids. Proper triage splits '
                                                              'tissue for micro vs histology and '
                                                              'uses the gentlest decalcification '
                                                              'compatible with the tests ordered.',
                                               'choice_explanations': {'A': 'Strong acid '
                                                                            'decalcification of '
                                                                            'the entire specimen '
                                                                            'ruins cultures and '
                                                                            'can impair '
                                                                            'IHC/molecular '
                                                                            'studies.',
                                                                       'B': 'Freezing the entire '
                                                                            'specimen can create '
                                                                            'artifact and still '
                                                                            'does not replace '
                                                                            'sterile culture '
                                                                            'allotment before '
                                                                            'fixative.',
                                                                       'C': 'Discarding sterile '
                                                                            'aliquots eliminates '
                                                                            'microbiologic '
                                                                            'diagnosis of '
                                                                            'osteomyelitis.',
                                                                       'D': 'Correct triage: '
                                                                            'sterile micro first, '
                                                                            'then fixed histology '
                                                                            'with appropriate '
                                                                            'decalcification.'}}]},
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
                  'questions': {'easy': [{'question': 'What does a routine O&P (ova and parasite) '
                                                      'stool examination primarily look for?',
                                          'options': ['A) Parasitic eggs, larvae, and protozoan '
                                                      'trophozoites/cysts by microscopy',
                                                      'B) Serum IgE quantification only',
                                                      'C) Bacterial MIC panels exclusively',
                                                      'D) Viral plaque assays on stool filtrate'],
                                          'answer': 'A) Parasitic eggs, larvae, and protozoan '
                                                    'trophozoites/cysts by microscopy',
                                          'explanation': 'O&P microscopy (direct, concentrated, '
                                                         'permanent stained smears) detects '
                                                         'helminth ova/larvae and protozoa. '
                                                         'Antigen/NAAT panels may supplement. O&P '
                                                         'is not IgE, AST, or viral culture.',
                                          'choice_explanations': {'A': 'O&P examines stool '
                                                                       'microscopically for '
                                                                       'parasite stages (ova, '
                                                                       'larvae, cysts, '
                                                                       'trophozoites).',
                                                                  'B': 'IgE is a serum immunology '
                                                                       'test, not stool O&P.',
                                                                  'C': 'MIC panels are '
                                                                       'antibacterial '
                                                                       'susceptibility tests.',
                                                                  'D': 'Viral plaque assays are '
                                                                       'not the routine O&P '
                                                                       'method.'}},
                                         {'question': 'Which laboratory method remains '
                                                      'foundational for diagnosing malaria in many '
                                                      'clinical settings?',
                                          'options': ['A) Throat swab rapid strep antigen only',
                                                      'B) Thick and thin blood film microscopy '
                                                      '(Giemsa)',
                                                      'C) Urine dipstick leukocyte esterase alone',
                                                      'D) Stool flotation for Ascaris only'],
                                          'answer': 'B) Thick and thin blood film microscopy '
                                                    '(Giemsa)',
                                          'explanation': 'Thick films maximize sensitivity; thin '
                                                         'films allow species identification and '
                                                         'parasitemia quantitation. Rapid antigen '
                                                         'tests and PCR adjunct, but microscopy '
                                                         'remains a core competency. Other '
                                                         'specimen types do not diagnose '
                                                         'blood-stage malaria.',
                                          'choice_explanations': {'A': 'Strep antigen tests '
                                                                       'diagnose pharyngitis, not '
                                                                       'malaria.',
                                                                  'B': 'Giemsa-stained thick/thin '
                                                                       'blood films are the '
                                                                       'classic malaria diagnostic '
                                                                       'mainstay.',
                                                                  'C': 'LE on urine suggests '
                                                                       'pyuria, not Plasmodium.',
                                                                  'D': 'Stool exams detect '
                                                                       'intestinal helminths, not '
                                                                       'erythrocytic malaria.'}},
                                         {'question': 'Enterobius vermicularis (pinworm) is best '
                                                      'recovered by which collection approach?',
                                          'options': ['A) Midstream clean-catch urine culture',
                                                      'B) Sputum acid-fast smear',
                                                      'C) First-morning perianal cellulose tape or '
                                                      'paddle test',
                                                      'D) Nasopharyngeal viral swab'],
                                          'answer': 'C) First-morning perianal cellulose tape or '
                                                    'paddle test',
                                          'explanation': 'Pinworm females lay eggs on perianal '
                                                         'skin at night; tape/paddle sampling in '
                                                         'the morning captures eggs more reliably '
                                                         'than random stool O&P. Urine, sputum, '
                                                         'and NP swabs target other pathogens.',
                                          'choice_explanations': {'A': 'Urine culture diagnoses '
                                                                       'bacteriuria, not '
                                                                       'Enterobius.',
                                                                  'B': 'AFB sputum exams target '
                                                                       'mycobacteria.',
                                                                  'C': 'Perianal tape/paddle '
                                                                       'testing is the preferred '
                                                                       'pinworm egg recovery '
                                                                       'method.',
                                                                  'D': 'NP swabs are for '
                                                                       'respiratory viruses, not '
                                                                       'pinworm.'}}],
                                'medium': [{'question': 'Giardia duodenalis trophozoites/cysts are '
                                                        'most often sought in which specimen using '
                                                        'antigen/NAAT or microscopy?',
                                            'options': ['A) CSF in aseptic meningitis protocols '
                                                        'only',
                                                        'B) Peripheral blood thin films '
                                                        'exclusively',
                                                        'C) Bone marrow aspirate for amastigotes',
                                                        'D) Stool (and sometimes duodenal fluid) '
                                                        'examinations'],
                                            'answer': 'D) Stool (and sometimes duodenal fluid) '
                                                      'examinations',
                                            'explanation': 'Giardia is an intestinal flagellate '
                                                           'diagnosed from stool by microscopy, '
                                                           'EIA, or NAAT; duodenal sampling is '
                                                           'occasionally used. Blood films and '
                                                           'marrow target different parasites '
                                                           '(malaria/Leishmania).',
                                            'choice_explanations': {'A': 'CSF is not the routine '
                                                                         'Giardia specimen.',
                                                                    'B': 'Blood films diagnose '
                                                                         'intraerythrocytic '
                                                                         'parasites, not Giardia.',
                                                                    'C': 'Marrow amastigotes '
                                                                         'suggest Leishmania, not '
                                                                         'Giardia.',
                                                                    'D': 'Stool (± duodenal fluid) '
                                                                         'is the standard Giardia '
                                                                         'diagnostic specimen.'}},
                                           {'question': 'Entamoeba histolytica infection is '
                                                        'clinically concerning because it can '
                                                        'cause which invasive disease theme?',
                                            'options': ['A) Invasive amebiasis (colitis and/or '
                                                        'amebic liver abscess)',
                                                        'B) Only asymptomatic skin colonization '
                                                        'forever',
                                                        'C) Exclusive viral encephalitis without '
                                                        'intestinal disease',
                                                        'D) Pinworm-like perianal egg deposition '
                                                        'as the main pathology'],
                                            'answer': 'A) Invasive amebiasis (colitis and/or '
                                                      'amebic liver abscess)',
                                            'explanation': 'Pathogenic E. histolytica invades '
                                                           'colonic mucosa and can hematogenously '
                                                           'seed the liver. Differentiation from '
                                                           'nonpathogenic amebae matters; '
                                                           'antigen/PCR help. It is not a pinworm '
                                                           'look-alike disease.',
                                            'choice_explanations': {'A': 'Invasive amebiasis '
                                                                         'includes dysentery and '
                                                                         'extraintestinal '
                                                                         'abscesses, especially '
                                                                         'hepatic.',
                                                                    'B': 'While colonization can '
                                                                         'occur, the feared '
                                                                         'syndrome is invasive '
                                                                         'disease—not lifelong '
                                                                         'benign skin carriage.',
                                                                    'C': 'Amebiasis is not a '
                                                                         'primary viral '
                                                                         'encephalitis entity.',
                                                                    'D': 'Perianal egg laying '
                                                                         'characterizes '
                                                                         'Enterobius, not '
                                                                         'Entamoeba.'}},
                                           {'question': 'Modified acid-fast staining of stool is '
                                                        'particularly useful to detect which '
                                                        'organisms?',
                                            'options': ['A) Adult Ascaris worms only on gross exam',
                                                        'B) Coccidian oocysts such as '
                                                        'Cryptosporidium (and related coccidia)',
                                                        'C) Plasmodium schizonts in erythrocytes',
                                                        'D) Gram-positive branching rods '
                                                        'exclusively'],
                                            'answer': 'B) Coccidian oocysts such as '
                                                      'Cryptosporidium (and related coccidia)',
                                            'explanation': 'Cryptosporidium, Cyclospora, and '
                                                           'Cystoisospora oocysts stain with '
                                                           'modified acid-fast methods. Routine '
                                                           'O&P may miss them without special '
                                                           'stains/antigen/NAAT. Malaria is blood '
                                                           'microscopy; Ascaris adults are gross '
                                                           'findings.',
                                            'choice_explanations': {'A': 'Ascaris adults are '
                                                                         'identified grossly/by '
                                                                         'O&P eggs, not modified '
                                                                         'AFB oocyst stains.',
                                                                    'B': 'Modified acid-fast stool '
                                                                         'stains highlight '
                                                                         'coccidian oocysts such '
                                                                         'as Cryptosporidium.',
                                                                    'C': 'Plasmodium is diagnosed '
                                                                         'on blood films, not '
                                                                         'stool AFB.',
                                                                    'D': 'Branching GPRs suggest '
                                                                         'Nocardia/Actinomyces '
                                                                         'workups, not stool '
                                                                         'coccidia stains.'}}],
                                'hard': [{'question': 'Blood films show intraerythrocytic ring '
                                                      'forms. The patient has never left the '
                                                      'northeastern U.S. but has had a tick bite. '
                                                      'Which interpretive clue most supports '
                                                      'Babesia over Plasmodium?',
                                          'options': ['A) Travel to sub-Saharan Africa last week '
                                                      'exclusively',
                                                      'B) Banana-shaped gametocytes of P. '
                                                      'falciparum clearly present',
                                                      'C) Maltese cross (tetrad) forms and '
                                                      'epidemiologic tick exposure without malaria '
                                                      'travel',
                                                      'D) Schüffner dots proving P. vivax '
                                                      'automatically without travel history'],
                                          'answer': 'C) Maltese cross (tetrad) forms and '
                                                    'epidemiologic tick exposure without malaria '
                                                    'travel',
                                          'explanation': 'Babesia and Plasmodium both show rings; '
                                                         'tetrads (Maltese cross) and '
                                                         'non-malarious geography/tick exposure '
                                                         'favor babesiosis. Species-specific '
                                                         'Plasmodium forms and travel history '
                                                         'support malaria. Expert confirmation and '
                                                         'PCR may be needed.',
                                          'choice_explanations': {'A': 'Recent African travel '
                                                                       'increases malaria pretest '
                                                                       'probability, opposite this '
                                                                       'scenario.',
                                                                  'B': 'Banana gametocytes '
                                                                       'indicate P. falciparum, '
                                                                       'not Babesia.',
                                                                  'C': 'Tetrads plus tick exposure '
                                                                       'without malaria travel '
                                                                       'strongly support Babesia.',
                                                                  'D': 'Schüffner dots suggest P. '
                                                                       'vivax/ovale and still need '
                                                                       'epidemiologic sense; they '
                                                                       'do not fit this tick-only '
                                                                       'story.'}},
                                         {'question': 'During surgery for a hydatid (echinococcal) '
                                                      'cyst, which laboratory/clinical handling '
                                                      'warning is critical?',
                                          'options': ['A) Spill cystic fluid freely to improve '
                                                      'antigen exposure for serology',
                                                      'B) Freeze fluid and inject back into the '
                                                      'patient for autoimmunization',
                                                      'C) Culture cyst fluid aerobically as if it '
                                                      'were routine staph abscess only',
                                                      'D) Avoid spillage of cyst contents — risk '
                                                      'of anaphylaxis and secondary seeding of '
                                                      'scolices'],
                                          'answer': 'D) Avoid spillage of cyst contents — risk of '
                                                    'anaphylaxis and secondary seeding of scolices',
                                          'explanation': 'Echinococcal cyst fluid contains '
                                                         'antigens and protoscolices; rupture can '
                                                         'cause anaphylaxis and metastatic cystic '
                                                         'disease. Surgical technique emphasizes '
                                                         'controlled removal; labs handle fluid '
                                                         'cautiously if received.',
                                          'choice_explanations': {'A': 'Spillage is dangerous, not '
                                                                       'diagnostically helpful in '
                                                                       'the OR.',
                                                                  'B': 'Reinjecting cyst fluid is '
                                                                       'harmful and not a therapy.',
                                                                  'C': 'While secondary infection '
                                                                       'can occur, treating '
                                                                       'hydatid fluid as routine '
                                                                       'pyogenic abscess ignores '
                                                                       'parasite dissemination '
                                                                       'risk.',
                                                                  'D': 'Preventing spillage avoids '
                                                                       'anaphylaxis and scolex '
                                                                       'seeding—the key safety '
                                                                       'theme.'}},
                                         {'question': 'Why are concentration techniques '
                                                      '(flotation/sedimentation) used in O&P '
                                                      'protocols?',
                                          'options': ['A) To increase sensitivity for recovering '
                                                      'ova/cysts present in low numbers',
                                                      'B) To sterilize stool for safe discard only',
                                                      'C) To convert all protozoa into helminths '
                                                      'chemically',
                                                      'D) To measure fecal fat quantitatively as '
                                                      'the main goal'],
                                          'answer': 'A) To increase sensitivity for recovering '
                                                    'ova/cysts present in low numbers',
                                          'explanation': 'Concentration separates parasites from '
                                                         'fecal debris, improving detection when '
                                                         'burden is low. Permanent stains still '
                                                         'aid protozoan ID. Concentration is not '
                                                         'sterilization, metamorphosis, or '
                                                         'fecal-fat quantitation.',
                                          'choice_explanations': {'A': 'Concentration methods '
                                                                       'enrich ova/cysts to raise '
                                                                       'microscopic sensitivity.',
                                                                  'B': 'Concentration is '
                                                                       'diagnostic, not a '
                                                                       'sterilization step.',
                                                                  'C': 'No reagent converts '
                                                                       'protozoa into helminths.',
                                                                  'D': 'Fecal fat assays are '
                                                                       'separate malabsorption '
                                                                       'tests.'}}],
                                'extreme': [{'question': 'A returned traveler has fever, '
                                                         'hemolysis, and dark urine. Thick films '
                                                         'show high parasitemia with delicate '
                                                         'rings and some appliqué forms; '
                                                         'gametocytes are banana-shaped. '
                                                         'Creatinine is rising. Which species '
                                                         'interpretation and laboratory urgency '
                                                         'are most accurate?',
                                             'options': ['A) Babesia limited disease — observe '
                                                         'without reporting parasitemia',
                                                         'B) P. falciparum malaria with severe '
                                                         'features: urgent quantitation, immediate '
                                                         'clinician notification, and rapid '
                                                         'therapy coordination',
                                                         'C) P. malariae chronic nephritis only — '
                                                         'no need for prompt reporting',
                                                         'D) Nonpathogenic Plasmodium falciparum '
                                                         'laboratory contaminant'],
                                             'answer': 'B) P. falciparum malaria with severe '
                                                       'features: urgent quantitation, immediate '
                                                       'clinician notification, and rapid therapy '
                                                       'coordination',
                                             'explanation': 'Banana gametocytes and appliqué rings '
                                                            'indicate P. falciparum. High '
                                                            'parasitemia with organ dysfunction is '
                                                            'severe malaria requiring immediate '
                                                            'notification and treatment. Babesia '
                                                            'lacks Plasmodium gametocytes; P. '
                                                            'malariae is low-grade; falciparum is '
                                                            'never a harmless contaminant.',
                                             'choice_explanations': {'A': 'Banana gametocytes are '
                                                                          'Plasmodium falciparum, '
                                                                          'not Babesia.',
                                                                     'B': 'Morphology plus '
                                                                          'severity markers demand '
                                                                          'urgent falciparum '
                                                                          'malaria reporting and '
                                                                          'care coordination.',
                                                                     'C': 'P. malariae lacks these '
                                                                          'morphologic hallmarks '
                                                                          'and still would not '
                                                                          'justify ignoring acute '
                                                                          'severe malaria films.',
                                                                     'D': 'P. falciparum is a true '
                                                                          'pathogen; contaminant '
                                                                          'framing is '
                                                                          'inappropriate.'}},
                                            {'question': 'Bone marrow shows macrophages filled '
                                                         'with small amastigotes with kinetoplasts '
                                                         'in a febrile patient from an endemic '
                                                         'region. Blood cultures are negative. '
                                                         'Which diagnosis and reporting approach '
                                                         'fit best?',
                                             'options': ['A) Malaria trophozoites mis-shelved into '
                                                         'marrow slides',
                                                         'B) Histoplasma exclusively — '
                                                         'kinetoplasts prove yeast budding',
                                                         'C) Leishmania amastigotes in '
                                                         'macrophages: confirm with '
                                                         'experts/special stains/NAAT as available '
                                                         'and notify clinicians of visceral '
                                                         'leishmaniasis concern',
                                                         'D) Toxoplasma tissue cysts without '
                                                         'tachyzoites as the only match'],
                                             'answer': 'C) Leishmania amastigotes in macrophages: '
                                                       'confirm with experts/special stains/NAAT '
                                                       'as available and notify clinicians of '
                                                       'visceral leishmaniasis concern',
                                             'explanation': 'Intracellular amastigotes with '
                                                            'kinetoplasts in marrow macrophages '
                                                            'indicate Leishmania (visceral '
                                                            'leishmaniasis). Histoplasma yeasts '
                                                            'lack kinetoplasts; malaria is '
                                                            'erythrocytic; Toxoplasma morphology '
                                                            'differs. Expert confirmation and '
                                                            'clinical notification are warranted.',
                                             'choice_explanations': {'A': 'Malaria parasites '
                                                                          'infect RBCs, not marrow '
                                                                          'macrophage cytoplasm '
                                                                          'with kinetoplasts.',
                                                                     'B': 'Kinetoplasts '
                                                                          'distinguish '
                                                                          'Leishmania/Trypanosoma '
                                                                          'amastigotes from '
                                                                          'Histoplasma yeasts.',
                                                                     'C': 'Macrophage amastigotes '
                                                                          'with kinetoplasts = '
                                                                          'Leishmania; escalate '
                                                                          'confirmation and '
                                                                          'clinical alert.',
                                                                     'D': 'Toxoplasma '
                                                                          'cysts/tachyzoites have '
                                                                          'different morphology '
                                                                          'and tissue niches.'}},
                                            {'question': 'A laboratory receives a bottle labeled '
                                                         '“parasite for identification” containing '
                                                         'a moving arthropod removed from skin; '
                                                         'the requester asks for “species-level ID '
                                                         'for legal case.” Staff have only '
                                                         'student-level entomology skills. What is '
                                                         'the most appropriate action?',
                                             'options': ['A) Guess a species name to satisfy the '
                                                         'legal deadline',
                                                         'B) Discard the specimen to avoid '
                                                         'paperwork',
                                                         'C) Report “insect, NOS” without '
                                                         'preserving the specimen',
                                                         'D) Preserve the specimen properly, '
                                                         'document chain of custody, and refer to '
                                                         'an experienced entomologist/reference '
                                                         'laboratory rather than overcalling '
                                                         'species'],
                                             'answer': 'D) Preserve the specimen properly, '
                                                       'document chain of custody, and refer to an '
                                                       'experienced entomologist/reference '
                                                       'laboratory rather than overcalling species',
                                             'explanation': 'Medicolegal parasite/vector IDs '
                                                            'require expertise and custody '
                                                            'documentation. Overcalling species '
                                                            'can harm legal outcomes. Preserve '
                                                            '(ethanol/method per guide), '
                                                            'photograph, and refer; do not guess '
                                                            'or destroy evidence.',
                                             'choice_explanations': {'A': 'Speculative species '
                                                                          'calls are '
                                                                          'scientifically and '
                                                                          'legally inappropriate.',
                                                                     'B': 'Discarding potential '
                                                                          'evidence is '
                                                                          'unacceptable.',
                                                                     'C': 'Vague reporting without '
                                                                          'preservation loses '
                                                                          'diagnostic/legal value.',
                                                                     'D': 'Preserve, maintain '
                                                                          'custody, and refer for '
                                                                          'expert ID—the correct '
                                                                          'laboratory '
                                                                          'response.'}}]},
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
                           'questions': {'easy': [{'question': 'Polymerase chain reaction (PCR) is '
                                                               'designed to amplify which '
                                                               'laboratory analyte class?',
                                                   'options': ['A) Target nucleic acid (DNA or '
                                                               'reverse-transcribed RNA)',
                                                               'B) Serum electrolytes by '
                                                               'ion-selective electrodes',
                                                               'C) Hemoglobin protein by '
                                                               'spectrophotometry only',
                                                               'D) Bacterial colonies without '
                                                               'lysis or primers'],
                                                   'answer': 'A) Target nucleic acid (DNA or '
                                                             'reverse-transcribed RNA)',
                                                   'explanation': 'PCR uses primers, polymerase, '
                                                                  'and thermal cycling to amplify '
                                                                  'specific DNA sequences; RNA '
                                                                  'targets require reverse '
                                                                  'transcription first (RT-PCR). '
                                                                  'It is not an electrolyte, '
                                                                  'hemoglobin protein, or '
                                                                  'intact-colony assay without '
                                                                  'nucleic acid extraction.',
                                                   'choice_explanations': {'A': 'PCR amplifies '
                                                                                'defined nucleic '
                                                                                'acid targets '
                                                                                'exponentially for '
                                                                                'detection/quantitation.',
                                                                           'B': 'ISE chemistry '
                                                                                'measures ions, '
                                                                                'not nucleic '
                                                                                'acids.',
                                                                           'C': 'Hemoglobin assays '
                                                                                'quantify '
                                                                                'protein/pigment, '
                                                                                'not amplify '
                                                                                'DNA/RNA.',
                                                                           'D': 'Colonies may be '
                                                                                'inputs after '
                                                                                'extraction, but '
                                                                                'PCR requires '
                                                                                'nucleic acid and '
                                                                                'primers—not '
                                                                                'intact unlysed '
                                                                                'colonies alone.'}},
                                                  {'question': 'Why do molecular laboratories '
                                                               'emphasize unidirectional workflow '
                                                               'and separate '
                                                               'pre-/post-amplification areas?',
                                                   'options': ['A) To decorate benches differently '
                                                               'for inspections only',
                                                               'B) To reduce amplicon '
                                                               'contamination that causes '
                                                               'false-positive PCR results',
                                                               'C) To increase random pipetting '
                                                               'errors deliberately',
                                                               'D) To eliminate the need for '
                                                               'negative controls forever'],
                                                   'answer': 'B) To reduce amplicon contamination '
                                                             'that causes false-positive PCR '
                                                             'results',
                                                   'explanation': 'Amplification generates '
                                                                  'billions of amplicons that can '
                                                                  'contaminate subsequent '
                                                                  'reactions. Physical separation, '
                                                                  'unidirectional flow, '
                                                                  'bleach/enzymatic controls, and '
                                                                  'NTC monitoring reduce false '
                                                                  'positives. Controls remain '
                                                                  'mandatory.',
                                                   'choice_explanations': {'A': 'Workflow design '
                                                                                'is a '
                                                                                'contamination-control '
                                                                                'measure, not '
                                                                                'decoration.',
                                                                           'B': 'Separating pre- '
                                                                                'and post-PCR '
                                                                                'areas limits '
                                                                                'amplicon '
                                                                                'carryover false '
                                                                                'positives.',
                                                                           'C': 'Quality systems '
                                                                                'aim to reduce, '
                                                                                'not increase, '
                                                                                'pipetting error.',
                                                                           'D': 'Negative/no-template '
                                                                                'controls remain '
                                                                                'essential '
                                                                                'contamination '
                                                                                'monitors.'}},
                                                  {'question': 'A viral load assay reports '
                                                               'copies/mL or IU/mL. What '
                                                               'physiologic/analytic concept does '
                                                               'this primarily represent?',
                                                   'options': ['A) Colony-forming units on blood '
                                                               'agar only',
                                                               'B) Antibody titer by serial '
                                                               'agglutination alone',
                                                               'C) Quantity of viral nucleic acid '
                                                               'in the tested specimen',
                                                               'D) Exact number of infected CD4 '
                                                               'cells always'],
                                                   'answer': 'C) Quantity of viral nucleic acid in '
                                                             'the tested specimen',
                                                   'explanation': 'Quantitative NAAT viral loads '
                                                                  'estimate nucleic acid '
                                                                  'concentration, used to monitor '
                                                                  'therapy (HIV, HBV, HCV, CMV). '
                                                                  'They are not culture CFU '
                                                                  'counts, serologic titers, or '
                                                                  'direct CD4-infected cell '
                                                                  'counts.',
                                                   'choice_explanations': {'A': 'CFU counts '
                                                                                'reflect viable '
                                                                                'culture growth, '
                                                                                'not NAAT viral '
                                                                                'load units.',
                                                                           'B': 'Antibody titers '
                                                                                'are serology, not '
                                                                                'nucleic acid '
                                                                                'quantitation.',
                                                                           'C': 'Viral load '
                                                                                'measures target '
                                                                                'nucleic acid '
                                                                                'amount in the '
                                                                                'specimen '
                                                                                '(method-specific '
                                                                                'units).',
                                                                           'D': 'CD4 counts are '
                                                                                'cellular '
                                                                                'immunology assays '
                                                                                'distinct from '
                                                                                'viral nucleic '
                                                                                'acid load.'}}],
                                         'medium': [{'question': 'In real-time quantitative PCR, '
                                                                 'Ct (or Cp) values typically '
                                                                 'relate how to initial target '
                                                                 'amount?',
                                                     'options': ['A) Directly proportional always, '
                                                                 'with higher Ct meaning more '
                                                                 'target',
                                                                 'B) Unrelated to quantity in '
                                                                 'validated assays',
                                                                 'C) Identical for all targets '
                                                                 'regardless of input',
                                                                 'D) Inversely related — lower Ct '
                                                                 'usually means more starting '
                                                                 'target (within the dynamic '
                                                                 'range)'],
                                                     'answer': 'D) Inversely related — lower Ct '
                                                               'usually means more starting target '
                                                               '(within the dynamic range)',
                                                     'explanation': 'Ct is the cycle where '
                                                                    'fluorescence crosses '
                                                                    'threshold. More starting '
                                                                    'template reaches threshold '
                                                                    'earlier → lower Ct. Standard '
                                                                    'curves convert Ct to '
                                                                    'quantity. Outside dynamic '
                                                                    'range or with inhibition, '
                                                                    'interpretation changes.',
                                                     'choice_explanations': {'A': 'Higher Ct '
                                                                                  'usually means '
                                                                                  'less, not more, '
                                                                                  'initial target.',
                                                                             'B': 'Validated qPCR '
                                                                                  'assays are '
                                                                                  'quantitative '
                                                                                  'via Ct–quantity '
                                                                                  'relationships.',
                                                                             'C': 'Ct varies with '
                                                                                  'input amount '
                                                                                  'and assay '
                                                                                  'efficiency.',
                                                                             'D': 'Within range, '
                                                                                  'Ct inversely '
                                                                                  'tracks starting '
                                                                                  'nucleic acid '
                                                                                  'amount.'}},
                                                    {'question': 'An internal control fails (no '
                                                                 'amplification) while the '
                                                                 'pathogen target is also '
                                                                 'negative. What is the most '
                                                                 'appropriate interpretation?',
                                                     'options': ['A) Possible inhibition or '
                                                                 'extraction/process failure — do '
                                                                 'not report a reliable negative; '
                                                                 'troubleshoot/repeat',
                                                                 'B) Definitive proof the pathogen '
                                                                 'is absent',
                                                                 'C) Positive contamination of all '
                                                                 'reagents',
                                                                 'D) Instrument overheating '
                                                                 'proving true infection'],
                                                     'answer': 'A) Possible inhibition or '
                                                               'extraction/process failure — do '
                                                               'not report a reliable negative; '
                                                               'troubleshoot/repeat',
                                                     'explanation': 'Internal controls monitor '
                                                                    'extraction and amplification '
                                                                    'integrity. IC failure '
                                                                    'invalidates a negative '
                                                                    'pathogen result because '
                                                                    'inhibition or process failure '
                                                                    'could mask true target. '
                                                                    'Repeat after '
                                                                    'dilution/re-extraction as '
                                                                    'protocol directs.',
                                                     'choice_explanations': {'A': 'Failed IC means '
                                                                                  'the negative '
                                                                                  'target result '
                                                                                  'is unreliable '
                                                                                  'until the '
                                                                                  'process is '
                                                                                  'corrected.',
                                                                             'B': 'Without a valid '
                                                                                  'IC, absence of '
                                                                                  'pathogen signal '
                                                                                  'cannot be '
                                                                                  'trusted.',
                                                                             'C': 'IC failure '
                                                                                  'suggests '
                                                                                  'inhibition/process '
                                                                                  'failure more '
                                                                                  'than universal '
                                                                                  'positive '
                                                                                  'contamination.',
                                                                             'D': 'Overheating is '
                                                                                  'not the '
                                                                                  'interpretive '
                                                                                  'meaning of IC '
                                                                                  'failure and '
                                                                                  'does not prove '
                                                                                  'infection.'}},
                                                    {'question': 'Pharmacogenetic or resistance '
                                                                 'genotyping results are used '
                                                                 'primarily to guide which '
                                                                 'clinical decision theme?',
                                                     'options': ['A) Choice of urine collection '
                                                                 'cup color',
                                                                 'B) Therapy selection/avoidance '
                                                                 'based on genetic variants '
                                                                 'affecting drug response or '
                                                                 'pathogen resistance',
                                                                 'C) Replacement of all culture '
                                                                 'identification',
                                                                 'D) Determination of ABO group '
                                                                 'without serology ever'],
                                                     'answer': 'B) Therapy selection/avoidance '
                                                               'based on genetic variants '
                                                               'affecting drug response or '
                                                               'pathogen resistance',
                                                     'explanation': 'PGx (e.g., CYP2C19, TPMT) and '
                                                                    'microbial resistance '
                                                                    'genotypes inform drug '
                                                                    'choice/dosing or antibiotic '
                                                                    'decisions. They complement, '
                                                                    'rather than universally '
                                                                    'replace, culture/serology '
                                                                    'workflows.',
                                                     'choice_explanations': {'A': 'Cup aesthetics '
                                                                                  'are unrelated '
                                                                                  'to molecular '
                                                                                  'PGx/resistance '
                                                                                  'testing.',
                                                                             'B': 'Genotyping '
                                                                                  'guides therapy '
                                                                                  'by revealing '
                                                                                  'host metabolism '
                                                                                  'variants or '
                                                                                  'pathogen '
                                                                                  'resistance '
                                                                                  'markers.',
                                                                             'C': 'Culture remains '
                                                                                  'essential for '
                                                                                  'many '
                                                                                  'infections; '
                                                                                  'genotyping '
                                                                                  'supplements '
                                                                                  'ID/AST themes.',
                                                                             'D': 'ABO typing '
                                                                                  'remains '
                                                                                  'serologic/molecular '
                                                                                  'RBC antigen '
                                                                                  'testing—not '
                                                                                  'general PGx '
                                                                                  'panels.'}}],
                                         'hard': [{'question': 'Next-generation sequencing (NGS) '
                                                               'clinical reports depend heavily on '
                                                               'which post-analytic components?',
                                                   'options': ['A) Only the color of the flow cell '
                                                               'plastic',
                                                               'B) Ignoring QC metrics if a '
                                                               'variant looks interesting',
                                                               'C) Bioinformatic pipelines, '
                                                               'coverage/QC metrics, and curated '
                                                               'clinical interpretation',
                                                               'D) Manual Gram stain correlation '
                                                               'as the sole validator'],
                                                   'answer': 'C) Bioinformatic pipelines, '
                                                             'coverage/QC metrics, and curated '
                                                             'clinical interpretation',
                                                   'explanation': 'NGS accuracy hinges on adequate '
                                                                  'coverage, variant-calling '
                                                                  'pipelines, artifact filters, '
                                                                  'and evidence-based '
                                                                  'interpretation (e.g., AMP/ACMG '
                                                                  'frameworks). Aesthetic factors '
                                                                  'and skipping QC are '
                                                                  'unacceptable; Gram stain does '
                                                                  'not validate most '
                                                                  'germline/somatic NGS calls.',
                                                   'choice_explanations': {'A': 'Flow-cell color '
                                                                                'is irrelevant to '
                                                                                'analytic '
                                                                                'validity.',
                                                                           'B': 'Releasing '
                                                                                'variants without '
                                                                                'QC risks '
                                                                                'reporting '
                                                                                'artifacts.',
                                                                           'C': 'Pipelines, '
                                                                                'QC/coverage, and '
                                                                                'curated '
                                                                                'interpretation '
                                                                                'constitute the '
                                                                                'clinical NGS '
                                                                                'post-analytic '
                                                                                'core.',
                                                                           'D': 'Gram stains do '
                                                                                'not confirm '
                                                                                'sequencing '
                                                                                'variant calls.'}},
                                                  {'question': 'Minimal residual disease PCR/NGS '
                                                               'assays after leukemia therapy are '
                                                               'designed to detect which level of '
                                                               'disease?',
                                                   'options': ['A) Only morphologically obvious '
                                                               '>20% marrow blasts',
                                                               'B) Serum protein spikes without '
                                                               'nucleic acid targets',
                                                               'C) Skin colonization flora '
                                                               'exclusively',
                                                               'D) Very low-level residual disease '
                                                               'below standard morphology '
                                                               'thresholds'],
                                                   'answer': 'D) Very low-level residual disease '
                                                             'below standard morphology thresholds',
                                                   'explanation': 'Molecular MRD assays target '
                                                                  'leukemia-specific sequences or '
                                                                  'phenotypes at sensitivities '
                                                                  'often to 10⁻⁴–10⁻⁶, far below '
                                                                  'morphologic remission cutoffs, '
                                                                  'informing prognosis and '
                                                                  'therapy.',
                                                   'choice_explanations': {'A': 'MRD methods '
                                                                                'specifically find '
                                                                                'disease below '
                                                                                'morphologic blast '
                                                                                'percentages.',
                                                                           'B': 'SPEP detects '
                                                                                'paraproteins; '
                                                                                'molecular MRD '
                                                                                'detects nucleic '
                                                                                'acid targets.',
                                                                           'C': 'Skin flora is '
                                                                                'unrelated to '
                                                                                'leukemic MRD '
                                                                                'assays.',
                                                                           'D': 'MRD NAAT/NGS '
                                                                                'detects residual '
                                                                                'leukemic nucleic '
                                                                                'acid below '
                                                                                'morphology '
                                                                                'limits.'}},
                                                  {'question': 'A molecular specimen for '
                                                               'identity/relationship testing '
                                                               'arrives without chain-of-custody '
                                                               'seals intact. What is the correct '
                                                               'laboratory response?',
                                                   'options': ['A) Reject or quarantine per policy '
                                                               '— compromised custody can '
                                                               'invalidate legal/identity results',
                                                               'B) Test anyway and omit custody '
                                                               'documentation',
                                                               'C) Relabel with a random medical '
                                                               'record number',
                                                               'D) Pool with another patient’s DNA '
                                                               'to save reagents'],
                                                   'answer': 'A) Reject or quarantine per policy — '
                                                             'compromised custody can invalidate '
                                                             'legal/identity results',
                                                   'explanation': 'Identity/forensic/relationship '
                                                                  'molecular tests require '
                                                                  'unbroken chain of custody. '
                                                                  'Compromised seals threaten '
                                                                  'legal admissibility and patient '
                                                                  'safety. Follow '
                                                                  'rejection/recollection '
                                                                  'policies; never pool or '
                                                                  'fabricate labels.',
                                                   'choice_explanations': {'A': 'Broken custody → '
                                                                                'reject/quarantine '
                                                                                'per SOP; results '
                                                                                'may be legally '
                                                                                'invalid.',
                                                                           'B': 'Testing without '
                                                                                'custody '
                                                                                'documentation '
                                                                                'undermines the '
                                                                                'purpose of '
                                                                                'identity testing.',
                                                                           'C': 'Random relabeling '
                                                                                'is a critical '
                                                                                'identity error.',
                                                                           'D': 'Pooling DNA '
                                                                                'destroys '
                                                                                'individual '
                                                                                'identity and is '
                                                                                'unacceptable.'}}],
                                         'extreme': [{'question': 'A laboratory wants to add a '
                                                                  'laboratory-developed '
                                                                  'respiratory multiplex PCR. '
                                                                  'Before reporting patient '
                                                                  'results, which '
                                                                  'regulatory/quality pathway is '
                                                                  'essential?',
                                                      'options': ['A) Begin patient testing '
                                                                  'immediately after reading the '
                                                                  'package insert of a research '
                                                                  'kit',
                                                                  'B) Perform method '
                                                                  'validation/verification per '
                                                                  'CLIA/CAP (or local) '
                                                                  'requirements for accuracy, '
                                                                  'precision, reportable range, '
                                                                  'and intended use—including '
                                                                  'contamination controls',
                                                                  'C) Validate using only two '
                                                                  'leftover positives without '
                                                                  'negatives or IC checks',
                                                                  'D) Skip validation if the '
                                                                  'medical director verbally likes '
                                                                  'the assay'],
                                                      'answer': 'B) Perform method '
                                                                'validation/verification per '
                                                                'CLIA/CAP (or local) requirements '
                                                                'for accuracy, precision, '
                                                                'reportable range, and intended '
                                                                'use—including contamination '
                                                                'controls',
                                                      'explanation': 'New LDTs/modified methods '
                                                                     'require documented '
                                                                     'validation (or verification '
                                                                     'of FDA-cleared methods) '
                                                                     'covering performance '
                                                                     'characteristics and '
                                                                     'contamination risk before '
                                                                     'patient testing. Informal '
                                                                     'approval or tiny incomplete '
                                                                     'studies do not meet '
                                                                     'accreditation standards.',
                                                      'choice_explanations': {'A': 'Research-use '
                                                                                   'reagents and '
                                                                                   'unread '
                                                                                   'performance '
                                                                                   'claims do not '
                                                                                   'authorize '
                                                                                   'clinical '
                                                                                   'reporting.',
                                                                              'B': 'Formal '
                                                                                   'validation/verification '
                                                                                   'with defined '
                                                                                   'performance '
                                                                                   'specs is '
                                                                                   'mandatory '
                                                                                   'before patient '
                                                                                   'reporting.',
                                                                              'C': 'Two positives '
                                                                                   'without '
                                                                                   'negatives/IC '
                                                                                   'assessment '
                                                                                   'cannot '
                                                                                   'establish '
                                                                                   'clinical '
                                                                                   'performance.',
                                                                              'D': 'Verbal '
                                                                                   'preference '
                                                                                   'cannot replace '
                                                                                   'documented '
                                                                                   'analytic '
                                                                                   'validation.'}},
                                                     {'question': 'After moving PCR master mix '
                                                                  'preparation to a new room, the '
                                                                  'lab notes a cluster of '
                                                                  'unexpected low-level positives '
                                                                  'across unrelated targets, while '
                                                                  'NTCs intermittently amplify. '
                                                                  'Extraction blanks are sometimes '
                                                                  'positive. Which root-cause '
                                                                  'theme is most likely?',
                                                      'options': ['A) True simultaneous rare '
                                                                  'infections in all patients by '
                                                                  'coincidence',
                                                                  'B) Improved analytic '
                                                                  'specificity from the move',
                                                                  'C) Amplicon/environmental '
                                                                  'contamination or workflow '
                                                                  'breach — stop testing, '
                                                                  'decontaminate, investigate, and '
                                                                  'verify with clean NTCs before '
                                                                  'resuming',
                                                                  'D) Instrument under-reporting '
                                                                  'of Ct values proving higher '
                                                                  'viral loads'],
                                                      'answer': 'C) Amplicon/environmental '
                                                                'contamination or workflow breach '
                                                                '— stop testing, decontaminate, '
                                                                'investigate, and verify with '
                                                                'clean NTCs before resuming',
                                                      'explanation': 'Clusters of unexpected '
                                                                     'positives with dirty '
                                                                     'NTCs/extraction blanks after '
                                                                     'workflow changes scream '
                                                                     'contamination. Cease patient '
                                                                     'reporting, '
                                                                     'bleach/UV/enzymatic clean, '
                                                                     'review unidirectional flow, '
                                                                     'replace reagents, and '
                                                                     'document corrective action '
                                                                     'with consecutive clean '
                                                                     'controls.',
                                                      'choice_explanations': {'A': 'Identical '
                                                                                   'low-level '
                                                                                   'multi-target '
                                                                                   'positives with '
                                                                                   'dirty NTCs are '
                                                                                   'not biologic '
                                                                                   'coincidence.',
                                                                              'B': 'Contamination '
                                                                                   'reduces '
                                                                                   'specificity; '
                                                                                   'it does not '
                                                                                   'improve it.',
                                                                              'C': 'Stop, '
                                                                                   'decontaminate, '
                                                                                   'fix workflow, '
                                                                                   'and prove '
                                                                                   'clean '
                                                                                   'NTCs—classic '
                                                                                   'molecular '
                                                                                   'contamination '
                                                                                   'response.',
                                                                              'D': 'Ct artifacts '
                                                                                   'from '
                                                                                   'contamination '
                                                                                   'are not true '
                                                                                   'viral load '
                                                                                   'increases.'}},
                                                     {'question': 'An FFPE tumor NGS specimen '
                                                                  'shows 5% neoplastic '
                                                                  'cellularity, heavy necrosis, '
                                                                  'and Qubit DNA below the assay’s '
                                                                  'validated input after '
                                                                  'extraction. The oncologist '
                                                                  'demands results today for a '
                                                                  'therapy decision. What should '
                                                                  'the laboratory do?',
                                                      'options': ['A) Dilute noise and call '
                                                                  'pathogenic variants anyway '
                                                                  'without disclaimers',
                                                                  'B) Report “no mutations” as a '
                                                                  'definitive negative despite '
                                                                  'inadequate input',
                                                                  'C) Swap in a different '
                                                                  'patient’s high-quality DNA to '
                                                                  'meet turnaround time',
                                                                  'D) Reject or limit the report '
                                                                  'with clear inadequacy language; '
                                                                  'request a better block/rebiopsy '
                                                                  'rather than risk false '
                                                                  'negatives/positives'],
                                                      'answer': 'D) Reject or limit the report '
                                                                'with clear inadequacy language; '
                                                                'request a better block/rebiopsy '
                                                                'rather than risk false '
                                                                'negatives/positives',
                                                      'explanation': 'Below-validated input and '
                                                                     'low tumor fraction risk '
                                                                     'false-negative (and '
                                                                     'sometimes artifact '
                                                                     'false-positive) calls. '
                                                                     'Ethical practice is to '
                                                                     'refuse overstated results, '
                                                                     'explain limitations, and '
                                                                     'seek adequate tissue—even '
                                                                     'under clinical pressure. '
                                                                     'Patient swapping is '
                                                                     'misconduct.',
                                                      'choice_explanations': {'A': 'Calling '
                                                                                   'variants from '
                                                                                   'inadequate '
                                                                                   'noisy '
                                                                                   'libraries '
                                                                                   'endangers '
                                                                                   'therapy '
                                                                                   'decisions.',
                                                                              'B': 'A definitive '
                                                                                   'negative is '
                                                                                   'invalid when '
                                                                                   'input/tumor '
                                                                                   'content fail '
                                                                                   'validation '
                                                                                   'thresholds.',
                                                                              'C': 'Using another '
                                                                                   'patient’s DNA '
                                                                                   'is a critical '
                                                                                   'identity/ethics '
                                                                                   'violation.',
                                                                              'D': 'Document '
                                                                                   'inadequacy, '
                                                                                   'limit/reject, '
                                                                                   'and obtain '
                                                                                   'better '
                                                                                   'material—the '
                                                                                   'correct '
                                                                                   'quality '
                                                                                   'response.'}}]},
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
            'questions': {'easy': [{'question': 'In laboratory quality management, what does QA '
                                                '(quality assurance) primarily encompass?',
                                    'options': ['A) Systems ensuring quality across preanalytic, '
                                                'analytic, and postanalytic phases',
                                                'B) Only the color of reagent bottles',
                                                'C) Exclusive focus on cafeteria surveys',
                                                'D) Ignoring external proficiency testing results'],
                                    'answer': 'A) Systems ensuring quality across preanalytic, '
                                              'analytic, and postanalytic phases',
                                    'explanation': 'QA is the overarching program of policies, '
                                                   'processes, and monitors that keep results '
                                                   'accurate and timely across the total testing '
                                                   'process. QC is one analytic component within '
                                                   'QA.',
                                    'choice_explanations': {'A': 'QA covers the total testing '
                                                                 'process—preanalytic through '
                                                                 'postanalytic systems.',
                                                            'B': 'Bottle aesthetics are not QA’s '
                                                                 'purpose.',
                                                            'C': 'Cafeteria surveys are unrelated '
                                                                 'to laboratory QA.',
                                                            'D': 'PT/EQA participation and '
                                                                 'response are core QA activities, '
                                                                 'not optional.'}},
                                   {'question': 'Internal quality control (QC) materials are run '
                                                'primarily to monitor what?',
                                    'options': ['A) Employee vacation balances',
                                                'B) Analytic method performance over time '
                                                '(precision/accuracy shifts)',
                                                'C) Only the hospital’s marketing metrics',
                                                'D) Patient satisfaction with waiting-room chairs'],
                                    'answer': 'B) Analytic method performance over time '
                                              '(precision/accuracy shifts)',
                                    'explanation': 'QC specimens of known acceptable ranges detect '
                                                   'random and systematic analytic error before '
                                                   'patient results are released. Westgard-type '
                                                   'rules guide acceptance/rejection decisions.',
                                    'choice_explanations': {'A': 'HR metrics are not analytic QC.',
                                                            'B': 'QC monitors ongoing analytic '
                                                                 'performance for shifts, trends, '
                                                                 'and imprecision.',
                                                            'C': 'Marketing metrics are outside '
                                                                 'laboratory QC.',
                                                            'D': 'Waiting-room comfort is not a '
                                                                 'method QC parameter.'}},
                                   {'question': 'What does SOP stand for in the clinical '
                                                'laboratory?',
                                    'options': ['A) Selective optional practice',
                                                'B) Specimen only protocol without analytics',
                                                'C) Standard operating procedure',
                                                'D) Secondary outpatient preference'],
                                    'answer': 'C) Standard operating procedure',
                                    'explanation': 'SOPs are controlled documents detailing how '
                                                   'tests and processes are performed so work is '
                                                   'reproducible and compliant. Staff must use '
                                                   'current approved versions.',
                                    'choice_explanations': {'A': 'SOPs are mandatory controlled '
                                                                 'procedures, not optional '
                                                                 'preferences.',
                                                            'B': 'SOPs cover analytic and '
                                                                 'operational steps, not “specimen '
                                                                 'only.”',
                                                            'C': 'SOP means standard operating '
                                                                 'procedure—the controlled method '
                                                                 'document.',
                                                            'D': 'That expansion is incorrect '
                                                                 'jargon.'}}],
                          'medium': [{'question': 'Levey–Jennings charts are used primarily to '
                                                  'visualize which QC concepts?',
                                      'options': ['A) Only patient bed assignments',
                                                  'B) Inventory expiration in the cafeteria',
                                                  'C) Physician handwriting styles',
                                                  'D) Random error and systematic shift/trend '
                                                  'patterns versus control limits'],
                                      'answer': 'D) Random error and systematic shift/trend '
                                                'patterns versus control limits',
                                      'explanation': 'LJ charts plot QC values over time against '
                                                     'mean ± SD limits, revealing imprecision '
                                                     '(scatter) and bias (shifts/trends) that '
                                                     'trigger Westgard rule evaluation.',
                                      'choice_explanations': {'A': 'Bed assignments are clinical '
                                                                   'operations, not QC charts.',
                                                              'B': 'Cafeteria inventory is '
                                                                   'unrelated to analytic LJ '
                                                                   'charts.',
                                                              'C': 'Handwriting is not a '
                                                                   'Levey–Jennings parameter.',
                                                              'D': 'LJ charts display QC '
                                                                   'performance patterns against '
                                                                   'statistical limits.'}},
                                     {'question': 'External proficiency testing (PT/EQA) primarily '
                                                  'evaluates which laboratory capability?',
                                      'options': ['A) Accuracy on blinded external unknowns '
                                                  'compared with peer/referee targets',
                                                  'B) Speed of cafeteria checkout lines',
                                                  'C) Ability to ignore manufacturer instructions',
                                                  'D) Only the cleanliness of parking lots'],
                                      'answer': 'A) Accuracy on blinded external unknowns compared '
                                                'with peer/referee targets',
                                      'explanation': 'PT sends unknown specimens; laboratories '
                                                     'assay them like patients and are scored '
                                                     'against intended results/peers. Failures '
                                                     'require investigation and corrective action.',
                                      'choice_explanations': {'A': 'PT assesses whether the lab '
                                                                   'obtains acceptable results on '
                                                                   'external unknowns.',
                                                              'B': 'Cafeteria speed is unrelated '
                                                                   'to PT.',
                                                              'C': 'PT evaluates correct testing '
                                                                   'practice, not defiance of '
                                                                   'instructions.',
                                                              'D': 'Parking lots are not PT '
                                                                   'analytes.'}},
                                     {'question': 'Critical value policy requires which '
                                                  'postanalytic communication practice?',
                                      'options': ['A) Filing the result silently in the LIS '
                                                  'without calls',
                                                  'B) Timely clinician notification with read-back '
                                                  'and documentation',
                                                  'C) Waiting until monthly QA meetings to mention '
                                                  'criticals',
                                                  'D) Texting results to unverified personal '
                                                  'social media contacts'],
                                      'answer': 'B) Timely clinician notification with read-back '
                                                'and documentation',
                                      'explanation': 'Critical results need rapid notification to '
                                                     'responsible licensed caregivers, '
                                                     'verification by read-back, and documentation '
                                                     'of time, person, and values. Informal social '
                                                     'media disclosure violates privacy and '
                                                     'policy.',
                                      'choice_explanations': {'A': 'Silent filing defeats the '
                                                                   'purpose of critical-value '
                                                                   'alerting.',
                                                              'B': 'Notify promptly, obtain '
                                                                   'read-back, and document—the '
                                                                   'standard critical-value '
                                                                   'process.',
                                                              'C': 'Monthly delay is unacceptable '
                                                                   'for life-threatening results.',
                                                              'D': 'Social media is not a secure '
                                                                   'clinical notification '
                                                                   'channel.'}}],
                          'hard': [{'question': 'A root-cause analysis after a wrong-blood-in-tube '
                                                'event should emphasize which quality principle?',
                                    'options': ['A) Punish only the last person who touched the '
                                                'tube without system review',
                                                'B) Hide the event from risk management to protect '
                                                'metrics',
                                                'C) Correct system causes (identification process, '
                                                'labeling at bedside, IT hard stops), not only '
                                                'individual blame',
                                                'D) Disable all patient identifiers to speed '
                                                'phlebotomy'],
                                    'answer': 'C) Correct system causes (identification process, '
                                              'labeling at bedside, IT hard stops), not only '
                                              'individual blame',
                                    'explanation': 'Modern patient safety uses systems thinking: '
                                                   'latent process failures enable active errors. '
                                                   'RCA seeks sustainable fixes (positive patient '
                                                   'ID, bedside labeling, barcode forcing '
                                                   'functions). Pure blame and secrecy perpetuate '
                                                   'harm.',
                                    'choice_explanations': {'A': 'Individual punishment without '
                                                                 'system redesign fails to prevent '
                                                                 'recurrence.',
                                                            'B': 'Event hiding blocks learning and '
                                                                 'is noncompliant.',
                                                            'C': 'System-focused corrective '
                                                                 'actions address the true causes '
                                                                 'of WBIT errors.',
                                                            'D': 'Removing identifiers increases, '
                                                                 'not decreases, '
                                                                 'misidentification.'}},
                                   {'question': 'Document control programs exist mainly to ensure '
                                                'which condition?',
                                    'options': ['A) Staff may use any downloaded internet protocol '
                                                'interchangeably',
                                                'B) Only obsolete SOPs are kept at benches for '
                                                'nostalgia',
                                                'C) Multiple conflicting uncontrolled copies guide '
                                                'testing',
                                                'D) Only current approved SOPs are in use at the '
                                                'point of testing'],
                                    'answer': 'D) Only current approved SOPs are in use at the '
                                              'point of testing',
                                    'explanation': 'Document control versions, approves, '
                                                   'distributes, and retires procedures so staff '
                                                   'cannot follow obsolete methods. Uncontrolled '
                                                   'internet printouts and conflicting copies are '
                                                   'accreditation findings.',
                                    'choice_explanations': {'A': 'Uncontrolled internet protocols '
                                                                 'bypass approval and validation.',
                                                            'B': 'Obsolete SOPs must be removed '
                                                                 'from use.',
                                                            'C': 'Conflicting copies cause method '
                                                                 'drift and errors.',
                                                            'D': 'Current approved SOPs at the '
                                                                 'bench are the document-control '
                                                                 'goal.'}},
                                   {'question': 'Failure Mode and Effects Analysis (FMEA) is best '
                                                'described as which quality tool?',
                                    'options': ['A) Prospective identification of process failure '
                                                'modes with risk prioritization and preventive '
                                                'controls',
                                                'B) Retrospective only celebration of perfect runs',
                                                'C) A billing audit technique for cafeteria trays',
                                                'D) Random deletion of QC points that look bad'],
                                    'answer': 'A) Prospective identification of process failure '
                                              'modes with risk prioritization and preventive '
                                              'controls',
                                    'explanation': 'FMEA proactively maps how a process can fail, '
                                                   'scores severity/occurrence/detection, and '
                                                   'implements controls before patients are '
                                                   'harmed. It is not a method to falsify QC.',
                                    'choice_explanations': {'A': 'FMEA is a prospective '
                                                                 'risk-assessment tool for failure '
                                                                 'modes and preventive actions.',
                                                            'B': 'FMEA is proactive analysis, not '
                                                                 'a party for perfect runs.',
                                                            'C': 'Cafeteria billing is unrelated '
                                                                 'to laboratory FMEA.',
                                                            'D': 'Deleting QC points is data '
                                                                 'integrity fraud, not FMEA.'}}],
                          'extreme': [{'question': 'Both levels of chemistry QC are −3 SD after a '
                                                   'calibrator lot change. Patient moving averages '
                                                   'shifted the same direction. Testers continued '
                                                   'releasing results for 6 hours “to not delay '
                                                   'the ER.” Which statement best describes the '
                                                   'required quality response now?',
                                       'options': ['A) Continue releasing because ER turnaround '
                                                   'time outranks analytic truth',
                                                   'B) Implement CAPA: stop testing, recall/amend '
                                                   'affected results, fix calibrator/method '
                                                   'issues, verify with in-control QC, document '
                                                   'effectiveness, and notify clinicians as needed',
                                                   'C) Delete the out-of-control QC points and '
                                                   'keep patient data as-is',
                                                   'D) Average out-of-control QC with last week’s '
                                                   'means to pass inspection'],
                                       'answer': 'B) Implement CAPA: stop testing, recall/amend '
                                                 'affected results, fix calibrator/method issues, '
                                                 'verify with in-control QC, document '
                                                 'effectiveness, and notify clinicians as needed',
                                       'explanation': 'Releasing known out-of-control results is a '
                                                      'serious quality failure. Corrective and '
                                                      'preventive action includes stopping the '
                                                      'analyzer, assessing patient impact, '
                                                      'amending/recalling, repairing the '
                                                      'systematic error, proving control, and '
                                                      'documenting effectiveness. Falsifying QC is '
                                                      'misconduct.',
                                       'choice_explanations': {'A': 'Speed never justifies '
                                                                    'knowingly releasing biased '
                                                                    'patient results.',
                                                               'B': 'Full CAPA with result '
                                                                    'remediation and verification '
                                                                    'is mandatory after prolonged '
                                                                    'out-of-control release.',
                                                               'C': 'Deleting QC evidence is fraud '
                                                                    'and worsens patient risk.',
                                                               'D': 'Averaging away failures '
                                                                    'falsifies quality records.'}},
                                      {'question': 'During a total LIS downtime, printers and '
                                                   'interfaces fail. Specimens continue to arrive. '
                                                   'Which continuity strategy is most appropriate?',
                                       'options': ['A) Refuse all specimens including critical ED '
                                                   'tests until the LIS returns days later',
                                                   'B) Invent temporary MRNs that will never be '
                                                   'reconciled',
                                                   'C) Activate downtime procedures: unique manual '
                                                   'identifiers, paper worksheets, validated '
                                                   'result delivery, and full retrospective '
                                                   'reconciliation when systems recover',
                                                   'D) Text unlabeled photos of results to '
                                                   'personal phones without documentation'],
                                       'answer': 'C) Activate downtime procedures: unique manual '
                                                 'identifiers, paper worksheets, validated result '
                                                 'delivery, and full retrospective reconciliation '
                                                 'when systems recover',
                                       'explanation': 'Downtime SOPs maintain positive ID, '
                                                      'testing, critical notification, and later '
                                                      'electronic catch-up. Inventing unreconciled '
                                                      'IDs or using insecure personal channels '
                                                      'creates permanent safety/privacy failures. '
                                                      'Critical testing should continue under '
                                                      'controlled manual systems.',
                                       'choice_explanations': {'A': 'Blanket refusal of critical '
                                                                    'testing harms patients; '
                                                                    'downtime procedures exist to '
                                                                    'continue safely.',
                                                               'B': 'Unreconciled temporary IDs '
                                                                    'cause permanent chart '
                                                                    'mismatches.',
                                                               'C': 'Controlled manual ID, '
                                                                    'documentation, communication, '
                                                                    'and reconciliation are the '
                                                                    'correct downtime response.',
                                                               'D': 'Personal-phone result photos '
                                                                    'violate privacy and '
                                                                    'documentation standards.'}},
                                      {'question': 'A supervisor asks a technologist to “just '
                                                   'tweak” yesterday’s failed proficiency-testing '
                                                   'results before submission, saying “everyone '
                                                   'knows the method is fine.” Altering the values '
                                                   'would hide a potential analytic failure from '
                                                   'the PT provider. What is the correct '
                                                   'professional action?',
                                       'options': ['A) Alter the PT values as requested to protect '
                                                   'the laboratory’s score',
                                                   'B) Submit half-altered results as a compromise',
                                                   'C) Ignore PT entirely going forward',
                                                   'D) Refuse to falsify PT; report integrity '
                                                   'concerns through proper channels and '
                                                   'investigate the real method problem'],
                                       'answer': 'D) Refuse to falsify PT; report integrity '
                                                 'concerns through proper channels and investigate '
                                                 'the real method problem',
                                       'explanation': 'PT integrity is a regulatory red line. '
                                                      'Falsification can revoke '
                                                      'licensure/accreditation. The ethical duty '
                                                      'is refusal, escalation (compliance '
                                                      'hotline/medical director), and genuine '
                                                      'troubleshooting of method performance.',
                                       'choice_explanations': {'A': 'Altering PT is fraud with '
                                                                    'severe regulatory '
                                                                    'consequences.',
                                                               'B': 'Partial falsification remains '
                                                                    'falsification.',
                                                               'C': 'PT participation is required; '
                                                                    'abandoning it is '
                                                                    'noncompliant.',
                                                               'D': 'Refuse fraud, escalate, and '
                                                                    'fix real analytic '
                                                                    'problems—the only acceptable '
                                                                    'path.'}}]},
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
                'questions': {'easy': [{'question': 'A positive urine dipstick blood reaction may '
                                                    'detect which of the following?',
                                        'options': ['A) Intact RBCs, free hemoglobin, or myoglobin',
                                                    'B) Only dietary nitrates from vegetables',
                                                    'C) Glucose exclusively via oxidase strips',
                                                    'D) Leukocyte esterase as the same pad '
                                                    'chemistry'],
                                        'answer': 'A) Intact RBCs, free hemoglobin, or myoglobin',
                                        'explanation': 'The blood pad detects heme peroxidase '
                                                       'activity from RBCs, hemoglobinuria, or '
                                                       'myoglobinuria. Microscopy distinguishes '
                                                       'intact RBCs; clinical correlation '
                                                       'separates hemoglobin vs myoglobin. It is '
                                                       'not the glucose or LE pad.',
                                        'choice_explanations': {'A': 'Dipstick “blood” responds to '
                                                                     'RBC heme, free hemoglobin, '
                                                                     'or myoglobin.',
                                                                'B': 'Nitrates/nitrites relate to '
                                                                     'the nitrite pad and '
                                                                     'diet/bacteria themes, not '
                                                                     'the blood pad’s heme '
                                                                     'reaction.',
                                                                'C': 'Glucose has a separate '
                                                                     'oxidase/peroxidase pad.',
                                                                'D': 'LE detects leukocyte '
                                                                     'esterases on a different '
                                                                     'pad.'}},
                                       {'question': 'Urine specific gravity on refractometer or '
                                                    'dipstick is used primarily to assess which '
                                                    'function?',
                                        'options': ['A) Hepatic synthetic function via albumin '
                                                    'alone',
                                                    'B) Relative concentrating/diluting ability of '
                                                    'the kidney (with caveats)',
                                                    'C) Exact GFR equal to inulin clearance',
                                                    'D) Pancreatic amylase output'],
                                        'answer': 'B) Relative concentrating/diluting ability of '
                                                  'the kidney (with caveats)',
                                        'explanation': 'SG reflects urine solute concentration, '
                                                       'approximating concentrating ability. '
                                                       'Interferents (glucose, protein, contrast) '
                                                       'and extreme hydration alter '
                                                       'interpretation. It is not GFR, hepatic '
                                                       'synthesis, or pancreatic function.',
                                        'choice_explanations': {'A': 'Hepatic synthesis is '
                                                                     'assessed with serum '
                                                                     'albumin/INR, not urine SG.',
                                                                'B': 'SG estimates urine '
                                                                     'concentration and thus renal '
                                                                     'concentrating/diluting '
                                                                     'status with known '
                                                                     'limitations.',
                                                                'C': 'GFR requires clearance/eGFR '
                                                                     'methods, not SG.',
                                                                'D': 'Amylase is a '
                                                                     'pancreatic/chemistry '
                                                                     'analyte.'}},
                                       {'question': 'Proper urine specimen triage for culture '
                                                    'versus routine UA generally requires which '
                                                    'practice?',
                                        'options': ['A) Dipping the reagent strip into the culture '
                                                    'bottle repeatedly',
                                                    'B) Leaving uncapped urine at 37 °C overnight '
                                                    'before any testing',
                                                    'C) Aliquoting with clean technique: culture '
                                                    'first if both are ordered, avoiding '
                                                    'contaminated pour-backs',
                                                    'D) Adding bleach to stabilize bacteria for '
                                                    'culture'],
                                        'answer': 'C) Aliquoting with clean technique: culture '
                                                  'first if both are ordered, avoiding '
                                                  'contaminated pour-backs',
                                        'explanation': 'If UA and culture are both ordered, '
                                                       'sterile culture aliquots should be taken '
                                                       'first (or separate midstream containers '
                                                       'used) so strip dipping does not '
                                                       'contaminate microbiology specimens. Heat '
                                                       'and bleach destroy diagnostic value.',
                                        'choice_explanations': {'A': 'Dipping strips into culture '
                                                                     'containers contaminates '
                                                                     'them.',
                                                                'B': 'Warm overnight standing '
                                                                     'grows contaminants and lyses '
                                                                     'cells/casts.',
                                                                'C': 'Culture-first clean aliquots '
                                                                     'prevent contamination of '
                                                                     'microbiology specimens.',
                                                                'D': 'Bleach kills organisms and '
                                                                     'invalidates culture.'}}],
                              'medium': [{'question': 'Dysmorphic RBCs and RBC casts on '
                                                      'microscopic UA most strongly suggest which '
                                                      'source of hematuria?',
                                          'options': ['A) Lower urinary tract contamination with '
                                                      'menstrual blood only',
                                                      'B) Skin abrasions remote from the urinary '
                                                      'tract',
                                                      'C) Factitious addition of food dye without '
                                                      'RBCs',
                                                      'D) Glomerular bleeding/disease'],
                                          'answer': 'D) Glomerular bleeding/disease',
                                          'explanation': 'RBC casts form in renal tubules when '
                                                         'glomerular bleeding mixes with '
                                                         'Tamm–Horsfall protein. Dysmorphic RBCs '
                                                         'support glomerular origin versus '
                                                         'isomorphic lower-tract bleeding.',
                                          'choice_explanations': {'A': 'Menstrual contamination '
                                                                       'may add RBCs but does not '
                                                                       'form true RBC casts from '
                                                                       'glomerular bleeding.',
                                                                  'B': 'Remote skin abrasions do '
                                                                       'not create urinary RBC '
                                                                       'casts.',
                                                                  'C': 'Dye without RBCs fails '
                                                                       'microscopy for '
                                                                       'hematuria/casts.',
                                                                  'D': 'Dysmorphic RBCs and RBC '
                                                                       'casts point to glomerular '
                                                                       'disease.'}},
                                         {'question': 'Oval fat bodies and fatty casts accompany '
                                                      'heavy proteinuria in which classic syndrome '
                                                      'pattern?',
                                          'options': ['A) Nephrotic-range proteinuria with '
                                                      'lipiduria',
                                                      'B) Pure central diabetes insipidus without '
                                                      'protein loss',
                                                      'C) Acute cystitis with nitrite positivity '
                                                      'only',
                                                      'D) Myoglobinuria without proteinuria'],
                                          'answer': 'A) Nephrotic-range proteinuria with lipiduria',
                                          'explanation': 'Nephrotic syndrome features heavy '
                                                         'proteinuria, hypoalbuminemia, edema, and '
                                                         'hyperlipidemia; lipiduria appears as '
                                                         'oval fat bodies/Maltese crosses and '
                                                         'fatty casts. DI, simple cystitis, and '
                                                         'isolated myoglobinuria lack that '
                                                         'pattern.',
                                          'choice_explanations': {'A': 'Oval fat bodies/fatty '
                                                                       'casts are hallmark '
                                                                       'lipiduria findings in '
                                                                       'nephrotic-range '
                                                                       'proteinuria.',
                                                                  'B': 'DI causes dilute urine '
                                                                       'without nephrotic '
                                                                       'lipiduria.',
                                                                  'C': 'Cystitis shows '
                                                                       'leukocytes/nitrite themes, '
                                                                       'not fatty casts from '
                                                                       'nephrosis.',
                                                                  'D': 'Myoglobin may trigger the '
                                                                       'blood pad without RBCs but '
                                                                       'does not define nephrotic '
                                                                       'fatty casts.'}},
                                         {'question': 'Polarized microscopy of urine sediment '
                                                      'shows needle-shaped negatively birefringent '
                                                      'crystals. Which crystal type fits best?',
                                          'options': ['A) Triple phosphate coffin lids without '
                                                      'birefringence interest',
                                                      'B) Monosodium urate (gout) — needle-shaped '
                                                      'negative birefringence',
                                                      'C) Calcium carbonate dumbbells exclusively '
                                                      'in acid urine always',
                                                      'D) Cholesterol plates that look identical '
                                                      'to urate needles'],
                                          'answer': 'B) Monosodium urate (gout) — needle-shaped '
                                                    'negative birefringence',
                                          'explanation': 'MSU crystals are needles with strong '
                                                         'negative birefringence under compensated '
                                                         'polarized light—classic for gout (often '
                                                         'synovial fluid, also urine contexts). '
                                                         'Triple phosphate are coffin lids in '
                                                         'alkaline urine; cholesterol forms '
                                                         'notched plates.',
                                          'choice_explanations': {'A': 'Struvite/triple phosphate '
                                                                       'crystals are coffin-lid '
                                                                       'shaped, not needles with '
                                                                       'MSU optics.',
                                                                  'B': 'Needle-shaped negatively '
                                                                       'birefringent crystals are '
                                                                       'monosodium urate.',
                                                                  'C': 'Calcium carbonate '
                                                                       'morphology/optics differ '
                                                                       'from MSU needles.',
                                                                  'D': 'Cholesterol crystals are '
                                                                       'rectangular/notched '
                                                                       'plates, not urate '
                                                                       'needles.'}}],
                              'hard': [{'question': 'CSF is grossly bloody. Tube 1 is much redder '
                                                    'than tube 4, and the supernatant is clear '
                                                    'after centrifugation shortly after '
                                                    'collection. Which interpretation is more '
                                                    'likely?',
                                        'options': ['A) Subarachnoid hemorrhage with xanthochromia '
                                                    'guaranteed',
                                                    'B) Normal CSF without explanation needed',
                                                    'C) Traumatic tap pattern more than SAH — '
                                                    'still correlate clinically and with '
                                                    'timing/xanthochromia protocols',
                                                    'D) Only bacterial meningitis can cause red '
                                                    'CSF'],
                                        'answer': 'C) Traumatic tap pattern more than SAH — still '
                                                  'correlate clinically and with '
                                                  'timing/xanthochromia protocols',
                                        'explanation': 'Clearing RBC counts from tube 1→4 and '
                                                       'colorless supernatant early after a '
                                                       'traumatic tap favor procedure trauma. SAH '
                                                       'more often shows persistent RBCs and '
                                                       'xanthochromia after sufficient time in '
                                                       'vivo. Always correlate with '
                                                       'clinical/imaging protocols.',
                                        'choice_explanations': {'A': 'Clear supernatant and '
                                                                     'clearing across tubes argue '
                                                                     'against classic SAH '
                                                                     'xanthochromia patterns.',
                                                                'B': 'Bloody CSF is never simply '
                                                                     '“normal.”',
                                                                'C': 'Decreasing blood across '
                                                                     'tubes with clear supernatant '
                                                                     'supports traumatic tap, with '
                                                                     'required clinical '
                                                                     'correlation.',
                                                                'D': 'Bacterial meningitis causes '
                                                                     'neutrophils/low glucose '
                                                                     'themes, not primary bright '
                                                                     'red blood patterns.'}},
                                       {'question': 'Dipstick blood is strongly positive but '
                                                    'microscopy shows no RBCs. Plasma is clear and '
                                                    'CK is massively elevated after a crush '
                                                    'injury. Which explanation fits best?',
                                        'options': ['A) Menstrual contamination with invisible '
                                                    'RBCs',
                                                    'B) Instrument failure proving true hematuria',
                                                    'C) Factitious ketchup addition explaining CK '
                                                    'rise',
                                                    'D) Myoglobinuria — heme-positive dipstick '
                                                    'without RBCs; correlate with clinical '
                                                    'rhabdomyolysis'],
                                        'answer': 'D) Myoglobinuria — heme-positive dipstick '
                                                  'without RBCs; correlate with clinical '
                                                  'rhabdomyolysis',
                                        'explanation': 'Myoglobin and hemoglobin both trigger the '
                                                       'blood pad. Absent RBCs plus clear plasma '
                                                       'and rhabdomyolysis markers favor '
                                                       'myoglobin. Hemoglobinuria often '
                                                       'accompanies pink plasma/hemolysis. '
                                                       'Clinical correlation prevents missed '
                                                       'compartment syndrome/rhabdo care.',
                                        'choice_explanations': {'A': 'Menstrual blood should show '
                                                                     'RBCs on microscopy.',
                                                                'B': 'Absent RBCs with heme '
                                                                     'positivity is a recognized '
                                                                     'myoglobin/hemoglobin '
                                                                     'pattern, not proof of '
                                                                     'analyzer failure alone.',
                                                                'C': 'Ketchup does not elevate CK.',
                                                                'D': 'Heme+ without RBCs in '
                                                                     'rhabdomyolysis = '
                                                                     'myoglobinuria until proven '
                                                                     'otherwise.'}},
                                       {'question': 'Pleural fluid LDH and protein are compared '
                                                    'with serum values using Light’s criteria '
                                                    'primarily to distinguish which categories?',
                                        'options': ['A) Transudate versus exudate themes for '
                                                    'effusion workup',
                                                    'B) Viral versus bacterial pneumonia by color '
                                                    'alone',
                                                    'C) CSF from ventricular versus lumbar sources '
                                                    'only',
                                                    'D) Urine from plasma without creatinine'],
                                        'answer': 'A) Transudate versus exudate themes for '
                                                  'effusion workup',
                                        'explanation': 'Light’s criteria use fluid/serum protein '
                                                       'and LDH ratios (and fluid LDH vs serum '
                                                       'ULN) to classify exudates vs transudates, '
                                                       'guiding differential diagnosis of pleural '
                                                       'effusions.',
                                        'choice_explanations': {'A': 'Light’s criteria classify '
                                                                     'pleural fluid as exudate or '
                                                                     'transudate using protein/LDH '
                                                                     'relationships.',
                                                                'B': 'Color alone does not replace '
                                                                     'Light’s biochemical '
                                                                     'classification or '
                                                                     'microbiologic testing.',
                                                                'C': 'CSF source differentiation '
                                                                     'uses other methods, not '
                                                                     'Light’s pleural criteria.',
                                                                'D': 'Urine vs plasma identity '
                                                                     'uses creatinine/urea '
                                                                     'comparisons, not Light’s '
                                                                     'criteria.'}}],
                              'extreme': [{'question': 'An automated urine microscopy system flags '
                                                       '“many bacteria and WBCs” on a specimen '
                                                       'from an asymptomatic pregnant patient, but '
                                                       'the tech’s manual review shows mostly '
                                                       'squamous cells with bacterial overlay '
                                                       'consistent with contamination, and the '
                                                       'culture was collected via poorly performed '
                                                       'clean-catch. Nitrite is negative. What is '
                                                       'the best laboratory–clinical synthesis?',
                                           'options': ['A) Report definitive pyelonephritis '
                                                       'without culture correlation',
                                                       'B) Interpret as likely contamination; '
                                                       'suggest properly collected midstream or '
                                                       'catheter specimen before diagnosing UTI, '
                                                       'and avoid overcalling automated flags',
                                                       'C) Add bleach and re-run until squamous '
                                                       'cells vanish',
                                                       'D) Diagnose gonorrhea from squamous cells '
                                                       'alone'],
                                           'answer': 'B) Interpret as likely contamination; '
                                                     'suggest properly collected midstream or '
                                                     'catheter specimen before diagnosing UTI, and '
                                                     'avoid overcalling automated flags',
                                           'explanation': 'Heavy squamous epithelium with mixed '
                                                          'bacteria often means perineal '
                                                          'contamination, especially with poor '
                                                          'clean-catch technique. Automated flags '
                                                          'need microscopic correlation. '
                                                          'Asymptomatic pregnancy bacteriuria '
                                                          'requires proper specimens, not '
                                                          'contaminated overcalls. Bleach and STI '
                                                          'guesses are inappropriate.',
                                           'choice_explanations': {'A': 'Contamination patterns do '
                                                                        'not diagnose '
                                                                        'pyelonephritis.',
                                                                   'B': 'Correlate automation with '
                                                                        'morphology/collection '
                                                                        'quality; recommend '
                                                                        'recollection rather than '
                                                                        'overcalling UTI.',
                                                                   'C': 'Bleach destroys the '
                                                                        'specimen and is not an '
                                                                        'analytic fix.',
                                                                   'D': 'Squamous cells do not '
                                                                        'diagnose Neisseria '
                                                                        'gonorrhoeae.'}},
                                          {'question': 'A synovial fluid from a hot swollen joint '
                                                       'is sent in a lithium-heparin tube for '
                                                       'crystal analysis and arrives refrigerated '
                                                       'after 18 hours. The fluid is scant. '
                                                       'Polarized microscopy is negative for '
                                                       'crystals, but the clinician insists on '
                                                       'ruling out gout tonight. Which limitations '
                                                       'should the laboratory communicate?',
                                           'options': ['A) Negative microscopy after 18 hours '
                                                       'always excludes gout forever',
                                                       'B) Refrigeration creates MSU crystals de '
                                                       'novo guaranteeing false positives always',
                                                       'C) Delayed refrigerated samples and wrong '
                                                       'anticoagulant can reduce crystal detection '
                                                       'sensitivity; recommend prompt fresh '
                                                       'collection in the preferred '
                                                       'anticoagulant/container per SOP and avoid '
                                                       'over-reassuring negatives',
                                                       'D) Heparin tubes convert all CPPD into '
                                                       'urate needles'],
                                           'answer': 'C) Delayed refrigerated samples and wrong '
                                                     'anticoagulant can reduce crystal detection '
                                                     'sensitivity; recommend prompt fresh '
                                                     'collection in the preferred '
                                                     'anticoagulant/container per SOP and avoid '
                                                     'over-reassuring negatives',
                                           'explanation': 'Crystal analysis is preanalytically '
                                                          'sensitive. Delay, temperature extremes, '
                                                          'and inappropriate anticoagulants (e.g., '
                                                          'EDTA/oxalate issues; follow local '
                                                          'synovial SOP—often heparin or plain) '
                                                          'can dissolve or obscure crystals. A '
                                                          'negative delayed exam cannot '
                                                          'categorically exclude gout; advise '
                                                          'recollection.',
                                           'choice_explanations': {'A': 'Delayed negatives are not '
                                                                        'absolute exclusions of '
                                                                        'crystal arthritis.',
                                                                   'B': 'Refrigeration is not a '
                                                                        'reliable method to '
                                                                        'manufacture diagnostic '
                                                                        'MSU positives.',
                                                                   'C': 'Communicate preanalytic '
                                                                        'limitations and request '
                                                                        'an optimal fresh specimen '
                                                                        'rather than overcalling a '
                                                                        'delayed negative.',
                                                                   'D': 'Anticoagulants do not '
                                                                        'convert CPPD into '
                                                                        'urate.'}},
                                          {'question': 'CSF tube #4 xanthochromia '
                                                       'spectrophotometry is requested 30 minutes '
                                                       'after a suspected thunderclap headache '
                                                       'onset; the tap was traumatic with falling '
                                                       'RBC counts. The supernatant looks '
                                                       'colorless visually. Which reporting '
                                                       'approach is most scientifically sound?',
                                           'options': ['A) Report “SAH excluded” solely because '
                                                       'visual color is absent at 30 minutes',
                                                       'B) Report “SAH proven” because any '
                                                       'traumatic tap equals SAH',
                                                       'C) Replace CSF protein with urine protein '
                                                       'dipstick as an SAH rule-out',
                                                       'D) State that early sampling may miss '
                                                       'xanthochromia, traumatic blood complicates '
                                                       'interpretation, and clinical/imaging '
                                                       'correlation is required—follow timed '
                                                       'xanthochromia guidelines'],
                                           'answer': 'D) State that early sampling may miss '
                                                     'xanthochromia, traumatic blood complicates '
                                                     'interpretation, and clinical/imaging '
                                                     'correlation is required—follow timed '
                                                     'xanthochromia guidelines',
                                           'explanation': 'Xanthochromia from in vivo hemoglobin '
                                                          'breakdown needs time (often assessed '
                                                          '≥12 hours in many protocols). Very '
                                                          'early sampling and traumatic RBCs '
                                                          'confound visual/spectrophotometric '
                                                          'interpretation. Labs should report '
                                                          'limitations and defer to '
                                                          'neurology/imaging pathways rather than '
                                                          'absolute SAH rule-in/out from a '
                                                          '30-minute colorless supernatant.',
                                           'choice_explanations': {'A': 'Too-early colorless '
                                                                        'supernatant cannot '
                                                                        'reliably exclude SAH.',
                                                                   'B': 'Traumatic taps are common '
                                                                        'and do not prove SAH.',
                                                                   'C': 'Urine dipsticks are not '
                                                                        'CSF xanthochromia '
                                                                        'methods.',
                                                                   'D': 'Explain timing and trauma '
                                                                        'limitations; require '
                                                                        'clinical/imaging '
                                                                        'correlation per '
                                                                        'guidelines.'}}]},
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
