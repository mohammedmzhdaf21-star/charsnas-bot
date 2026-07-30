"""Undergraduate MLS study content by specialty and difficulty."""
from __future__ import annotations

import random

from quiz_bank import DIFFICULTIES, DIFFICULTY_LABELS, LABEL_TO_DIFFICULTY

SPECIALTY_ORDER = ['hematology', 'clinical_chemistry', 'medical_microbiology', 'immunology', 'blood_bank', 'histopathology', 'parasitology', 'molecular_diagnostics', 'lab_qa', 'urinalysis']

SPECIALTIES: dict[str, dict] = {
    "hematology": {
        "label": "Hematology",
        "books": [
            "Clinical Hematology — Rodak",
            "Hoffbrand's Essential Haematology",
            "CLSI hematology method documents",
        ],
        "pdf_notes": [
            "Always correlate CBC with smear morphology.",
            "Microcytic anemia: iron deficiency vs thalassemia themes.",
            "Blasts on smear = urgent hematology review.",
            "PT/INR vs aPTT vs anti-Xa — know what each monitors.",
            "Preanalytic errors (clotted/hemolyzed) invalidate many results.",
        ],
        "questions": {
            "easy": [
                {
                    "question": "Normal adult male hemoglobin roughly?",
                    "options": [
                        "A) About 13–17 g/dL (lab-dependent)",
                        "B) About 8–10 g/dL (lab-dependent)",
                        "C) About 18–22 g/dL (lab-dependent)",
                        "D) About 5–7 g/dL (lab-dependent)",
                    ],
                    "answer": "A) About 13–17 g/dL (lab-dependent)",
                    "explanation": "Adult male hemoglobin reference intervals are typically about 13–17 g/dL, though exact cutoffs vary by laboratory, altitude, and method. Hemoglobin concentration reflects circulating oxygen-carrying capacity and is interpreted with hematocrit and red-cell indices. Sex- and age-specific intervals from the reporting laboratory define the interpretive reference.",
                    "choice_explanations": {
                        "A": "Adult male hemoglobin reference intervals are typically about 13–17 g/dL, reflecting circulating oxygen-carrying capacity; exact cutoffs vary by laboratory, altitude, and method.",
                        "B": "Hemoglobin around 8–10 g/dL is within anemic territory for adult males, not the usual reference interval. That range indicates reduced red-cell oxygen-carrying capacity rather than a normal adult male value.",
                        "C": "Hemoglobin of about 18–22 g/dL exceeds typical adult male reference limits and suggests erythrocytosis or analytic/physiologic elevation, not the ordinary normal interval.",
                        "D": "Hemoglobin of about 5–7 g/dL represents severe anemia with critically reduced oxygen-carrying capacity, far below adult male reference intervals.",
                    },
                },
                {
                    "question": "CBC primarily measures?",
                    "options": [
                        "A) Plasma electrolyte concentrations",
                        "B) Blood cell counts and indices",
                        "C) Coagulation factor activities",
                        "D) Arterial blood gas tensions",
                    ],
                    "answer": "B) Blood cell counts and indices",
                    "explanation": "A complete blood count (CBC) quantifies leukocytes, erythrocytes, and platelets and reports red-cell indices such as MCV, MCH, and MCHC. Automated analyzers also provide leukocyte differentials and flags that prompt smear review. The CBC is the foundational screening test in hematology for anemia, infection, and cytopenias.",
                    "choice_explanations": {
                        "A": "Plasma electrolytes (Na, K, Cl, HCO3) are chemistry analytes measured on serum/plasma analyzers, not the primary CBC output. The CBC instead quantifies blood cells and red-cell indices.",
                        "B": "A complete blood count quantifies leukocytes, erythrocytes, and platelets and reports indices such as MCV, MCH, and MCHC, forming the foundational hematology screening panel.",
                        "C": "Coagulation factor activities are assessed with PT/aPTT, factor assays, or chromogenic methods, not by the CBC. The CBC reports cellular counts and indices rather than clotting-factor function.",
                        "D": "Arterial blood-gas tensions (pO2, pCO2, pH) are measured on blood-gas analyzers. They evaluate gas exchange and acid–base status, not blood-cell counts.",
                    },
                },
                {
                    "question": "Anemia means?",
                    "options": [
                        "A) Elevated leukocyte count for age/sex",
                        "B) Elevated platelet count for age/sex",
                        "C) Low hemoglobin/RBC mass for age/sex",
                        "D) Elevated hematocrit with normal hemoglobin",
                    ],
                    "answer": "C) Low hemoglobin/RBC mass for age/sex",
                    "explanation": "Anemia is a reduction in hemoglobin concentration or red-cell mass below the reference interval for age and sex. It may result from decreased production, increased destruction, or blood loss. Morphologic (MCV-based) and kinetic approaches guide the subsequent laboratory workup.",
                    "choice_explanations": {
                        "A": "Elevated leukocyte count defines leukocytosis, which may accompany infection or inflammation but is not the definition of anemia. Anemia is low hemoglobin or red-cell mass for age and sex.",
                        "B": "Elevated platelet count defines thrombocytosis. Platelet number is independent of the hemoglobin/RBC-mass reduction that defines anemia.",
                        "C": "Anemia is a reduction in hemoglobin concentration or circulating red-cell mass below the age- and sex-specific reference interval, from underproduction, hemolysis, or blood loss.",
                        "D": "Elevated hematocrit with normal hemoglobin is not anemia; anemia requires low hemoglobin or red-cell mass. Discordant Hct/Hb pairs instead prompt analytic or hydration correlation.",
                    },
                },
            ],
            "medium": [
                {
                    "question": "Schistocytes suggest?",
                    "options": [
                        "A) Iron-deficiency anemia with pencil cells",
                        "B) Megaloblastic anemia with macro-ovalocytes",
                        "C) Hereditary spherocytosis with dense spherocytes",
                        "D) Microangiopathic hemolysis",
                    ],
                    "answer": "D) Microangiopathic hemolysis",
                    "explanation": "Schistocytes are fragmented red cells formed when erythrocytes are sheared by fibrin strands or abnormal vasculature. Their presence supports microangiopathic hemolytic anemia (MAHA), as seen in TTP, HUS, DIC, and mechanical valve injury. Correlation with LDH, haptoglobin, bilirubin, and platelet count refines the differential.",
                    "choice_explanations": {
                        "A": "Iron-deficiency anemia classically shows hypochromic microcytes and pencil cells from impaired hemoglobin synthesis, not mechanical red-cell fragmentation. Schistocytes indicate shear injury instead.",
                        "B": "Megaloblastic anemia produces macro-ovalocytes and hypersegmented neutrophils from impaired DNA synthesis, not fibrin-shear fragments. Schistocytes point to microangiopathic hemolysis.",
                        "C": "Hereditary spherocytosis yields dense spherocytes from membrane–cytoskeleton defects with extravascular hemolysis, not fragmented schistocytes of microvascular shear.",
                        "D": "Schistocytes are fragmented erythrocytes sheared by fibrin strands or abnormal vasculature, supporting microangiopathic hemolytic anemia as in TTP, HUS, DIC, or mechanical valves.",
                    },
                },
                {
                    "question": "Left shift means?",
                    "options": [
                        "A) Increased immature neutrophils",
                        "B) Increased absolute lymphocytosis",
                        "C) Increased absolute eosinophilia",
                        "D) Increased absolute basophilia",
                    ],
                    "answer": "A) Increased immature neutrophils",
                    "explanation": "A left shift denotes increased circulating immature neutrophils such as bands and earlier myeloid forms. It commonly accompanies acute bacterial infection, inflammation, or physiologic stress with accelerated marrow release. Marked left shift with dysplasia or blasts requires morphologic review to exclude myeloid malignancy.",
                    "choice_explanations": {
                        "A": "A left shift denotes increased circulating immature neutrophils (bands and earlier myeloid forms), typically from accelerated marrow release during bacterial infection, inflammation, or stress.",
                        "B": "Absolute lymphocytosis expands the lymphoid lineage and does not define a neutrophil left shift. Left shift specifically refers to immature neutrophilic forms in circulation.",
                        "C": "Eosinophilia reflects allergic, parasitic, or certain clonal processes and is unrelated to the band/immature-neutrophil increase that constitutes a left shift.",
                        "D": "Basophilia may accompany myeloproliferative neoplasms or hypersensitivity but is not a left shift, which is defined by immature neutrophils.",
                    },
                },
                {
                    "question": "INR monitors?",
                    "options": [
                        "A) Unfractionated heparin via anti-Xa assay",
                        "B) Warfarin therapy (extrinsic/common pathway)",
                        "C) Primary hemostasis via bleeding time",
                        "D) Fibrinolysis via D-dimer alone",
                    ],
                    "answer": "B) Warfarin therapy (extrinsic/common pathway)",
                    "explanation": "The international normalized ratio (INR) standardizes the prothrombin time (PT) across thromboplastin reagents. PT/INR primarily assesses the extrinsic and common coagulation pathways and is used to monitor vitamin K antagonist (warfarin) therapy. Results are interpreted with the therapeutic target appropriate to the clinical indication.",
                    "choice_explanations": {
                        "A": "Unfractionated heparin is monitored with anti-Xa activity or aPTT, not INR. INR standardizes PT for the vitamin K–dependent extrinsic/common pathway, classically used for warfarin.",
                        "B": "INR standardizes the prothrombin time across thromboplastin reagents and monitors warfarin’s effect on the vitamin K–dependent extrinsic and common coagulation pathways.",
                        "C": "Bleeding time and related assays assess primary hemostasis (platelets/vessel wall), not the extrinsic-pathway clotting factors reflected by PT/INR.",
                        "D": "D-dimer reflects fibrin degradation from plasmin activity and screens for thrombosis/fibrinolysis; it does not monitor warfarin’s vitamin K–antagonist effect as INR does.",
                    },
                },
            ],
            "hard": [
                {
                    "question": "PNH relates to?",
                    "options": [
                        "A) Extrinsic hemolysis from warm IgG autoimmune antibody",
                        "B) Intrinsic hemolysis from spectrin cytoskeleton defect",
                        "C) Complement-mediated hemolysis due to GPI-anchor defect",
                        "D) Sequestration hemolysis from hypersplenism alone",
                    ],
                    "answer": "C) Complement-mediated hemolysis due to GPI-anchor defect",
                    "explanation": "Paroxysmal nocturnal hemoglobinuria (PNH) arises from acquired PIGA mutations that impair GPI-anchor synthesis, depleting complement-regulatory proteins CD55 and CD59 on blood cells. Unopposed complement activity produces intravascular hemolysis and contributes to thrombosis risk. High-sensitivity flow cytometry for GPI-deficient clones is the diagnostic method of choice.",
                    "choice_explanations": {
                        "A": "Warm autoimmune hemolysis is antibody-mediated extravascular (and sometimes intravascular) destruction with a positive DAT, not the GPI-anchor complement-regulatory defect of PNH.",
                        "B": "Spectrin and related cytoskeletal defects cause hereditary spherocytosis with intrinsic membrane instability, distinct from PNH’s acquired complement sensitivity from lost CD55/CD59.",
                        "C": "PNH arises from acquired PIGA mutations that impair GPI-anchor synthesis, depleting CD55/CD59 so unopposed complement drives intravascular hemolysis and related cytopenias.",
                        "D": "Hypersplenism sequesters and destroys blood cells in an enlarged spleen without the GPI-anchor complement defect that defines PNH hemolysis.",
                    },
                },
                {
                    "question": "AML vs ALL distinction uses?",
                    "options": [
                        "A) Patient age alone without lineage studies",
                        "B) Hemoglobin value alone without blast markers",
                        "C) Platelet count alone without immunophenotype",
                        "D) Morphology + cytochemistry/immunophenotype/genetics",
                    ],
                    "answer": "D) Morphology + cytochemistry/immunophenotype/genetics",
                    "explanation": "Acute myeloid leukemia (AML) and acute lymphoblastic leukemia (ALL) cannot be reliably separated by age or blood counts alone. Distinction relies on blast morphology, cytochemistry when used, multiparameter immunophenotyping, and genetic/cytogenetic findings under WHO/ICC frameworks. Accurate lineage assignment directs induction therapy and risk stratification.",
                    "choice_explanations": {
                        "A": "Patient age shifts prior probabilities but cannot lineage-assign blasts; AML and ALL require morphology plus immunophenotype, cytochemistry when used, and genetics.",
                        "B": "Hemoglobin reflects anemia severity, not blast lineage. Distinguishing AML from ALL depends on marker/genetic characterization of the neoplastic cells.",
                        "C": "Platelet count indicates thrombocytopenia severity but does not determine myeloid versus lymphoid blast identity.",
                        "D": "AML versus ALL distinction integrates blast morphology with cytochemistry when used, multiparameter immunophenotyping, and genetic studies that define lineage and subtype.",
                    },
                },
                {
                    "question": "HIT is?",
                    "options": [
                        "A) Heparin-induced thrombocytopenia — immune, thrombosis risk",
                        "B) EDTA-dependent platelet clumping pseudothrombocytopenia",
                        "C) Heparin-associated nonimmune platelet sequestration",
                        "D) Drug-induced marrow suppression without thrombosis risk",
                    ],
                    "answer": "A) Heparin-induced thrombocytopenia — immune, thrombosis risk",
                    "explanation": "Heparin-induced thrombocytopenia (HIT) is an immune-mediated disorder in which antibodies against platelet factor 4–heparin complexes activate platelets. Paradoxically, patients develop thrombocytopenia with a high risk of arterial and venous thrombosis. Laboratory evaluation may include immunoassay and functional assays, and heparin must be discontinued with alternative anticoagulation.",
                    "choice_explanations": {
                        "A": "HIT is an immune disorder in which anti–PF4/heparin antibodies activate platelets, causing thrombocytopenia with a paradoxical risk of arterial and venous thrombosis.",
                        "B": "EDTA-dependent platelet clumping causes pseudothrombocytopenia on automated counts and is corrected by recounting in citrate or by smear review; it is not immune HIT.",
                        "C": "Nonimmune heparin-associated platelet effects are milder and lack the antibody-mediated thrombotic pathophysiology that defines clinical HIT.",
                        "D": "Direct marrow suppression lowers counts without the PF4/heparin antibody-driven platelet activation and thrombosis that characterize HIT.",
                    },
                },
            ],
            "extreme": [
                {
                    "question": "APML emergency risk?",
                    "options": [
                        "A) Isolated iron deficiency without coagulopathy",
                        "B) DIC/bleeding — urgent ATRA pathway",
                        "C) Hyperviscosity from extreme leukocytosis alone",
                        "D) Tumor lysis without coagulopathy concern",
                    ],
                    "answer": "B) DIC/bleeding — urgent ATRA pathway",
                    "explanation": "Acute promyelocytic leukemia (APML/APL) is driven by PML::RARA and characteristically presents with coagulopathy and DIC-related bleeding. Early recognition of abnormal promyelocytes, often with Auer rods, warrants urgent initiation of all-trans retinoic acid (ATRA)–based therapy. Delayed treatment markedly increases early hemorrhagic mortality.",
                    "choice_explanations": {
                        "A": "Isolated iron deficiency causes microcytic anemia without the PML::RARA-driven coagulopathy and DIC that make APML an immediate bleeding emergency.",
                        "B": "APML (APL) driven by PML::RARA characteristically presents with DIC and life-threatening bleeding, requiring urgent initiation of ATRA-based therapy while confirming the diagnosis.",
                        "C": "Extreme leukocytosis can cause hyperviscosity in other leukemias, but APML’s hallmark emergency is consumptive coagulopathy/DIC rather than viscosity from blast count alone.",
                        "D": "Tumor lysis can complicate high-burden leukemias, yet APML’s distinctive early threat is DIC-related hemorrhage needing prompt ATRA, not TLS alone.",
                    },
                },
                {
                    "question": "TTP pentad classic teaching includes?",
                    "options": [
                        "A) Isolated neutropenia with normal smear and platelets",
                        "B) Polycythemia with thrombocytosis and leukocytosis",
                        "C) MAHA, thrombocytopenia, neurologic change (± renal/fever)",
                        "D) Eosinophilia with pulmonary infiltrates alone",
                    ],
                    "answer": "C) MAHA, thrombocytopenia, neurologic change (± renal/fever)",
                    "explanation": "Thrombotic thrombocytopenic purpura (TTP) classically features microangiopathic hemolytic anemia and thrombocytopenia, often with neurologic findings; fever and renal involvement may occur. Severe ADAMTS13 deficiency allows uncleaved ultra-large von Willebrand multimers to drive platelet microthrombi. Prompt plasma exchange is disease-modifying therapy.",
                    "choice_explanations": {
                        "A": "Isolated neutropenia with a normal smear and platelets does not capture TTP’s microangiopathic hemolysis and consumptive thrombocytopenia from ADAMTS13 deficiency.",
                        "B": "Polycythemia with thrombocytosis and leukocytosis suggests myeloproliferative neoplasia, opposite to TTP’s MAHA and thrombocytopenia.",
                        "C": "Classic TTP teaching includes MAHA and thrombocytopenia with neurologic change, and often fever or renal involvement, driven by severe ADAMTS13 deficiency with platelet-rich microthrombi.",
                        "D": "Eosinophilia with pulmonary infiltrates suggests allergic, parasitic, or eosinophilic lung disease, not thrombotic microangiopathy.",
                    },
                },
                {
                    "question": "Flow cytometry MRD aims to?",
                    "options": [
                        "A) Replace coagulation monitoring after induction",
                        "B) Quantify plasma glucose during steroid therapy",
                        "C) Determine ABO/Rh type before transfusion",
                        "D) Detect residual disease below morphology threshold",
                    ],
                    "answer": "D) Detect residual disease below morphology threshold",
                    "explanation": "Minimal residual disease (MRD) assessment by multiparameter flow cytometry detects leukemic cells below the threshold of morphologic remission. Sensitive MRD monitoring informs treatment response, risk stratification, and need for therapy intensification. Assay design requires disease-specific antigen aberrant phenotypes and validated sensitivity limits.",
                    "choice_explanations": {
                        "A": "Coagulation monitoring uses PT/aPTT or anti-Xa assays and is unrelated to flow-cytometric detection of residual leukemic cells below morphologic remission.",
                        "B": "Plasma glucose measurement assesses carbohydrate metabolism during steroid therapy; it does not quantify leukemic MRD by aberrant immunophenotype.",
                        "C": "ABO/Rh typing identifies red-cell antigens for transfusion compatibility and does not measure residual leukemia burden.",
                        "D": "Flow-cytometric MRD detects leukemic cells below the morphologic remission threshold using leukemia-associated immunophenotypes, informing response and relapse risk.",
                    },
                },
            ],
        },
        "cases": {
            "easy": [
                {
                    "title": "Fatigue + Low Hb",
                    "stem": "A young woman has fatigue; Hb 9.5 g/dL, MCV low.",
                    "question": "Likely anemia type theme?",
                    "answer": "Microcytic anemia — consider iron deficiency among differentials.",
                    "discussion": "Check iron studies/smear as indicated.",
                    "book_hint": "Clinical Hematology — Rodak / Hoffbrand",
                },
            ],
            "medium": [
                {
                    "title": "Fever + Blasts",
                    "stem": "CBC shows marked leukocytosis with circulating blasts and anemia/thrombocytopenia.",
                    "question": "Concern?",
                    "answer": "Acute leukemia until proven otherwise — urgent hematology workup.",
                    "discussion": "Do not delay smear review.",
                    "book_hint": "Clinical Hematology — Rodak / Hoffbrand",
                },
            ],
            "hard": [
                {
                    "title": "Post-Heparin Platelet Drop + Clot",
                    "stem": "Platelets fall by >50% after heparin; new thrombosis. Choose the safest high-yield next laboratory concept.",
                    "question": "Suspect?",
                    "answer": "HIT — discontinue heparin and manage per protocol.",
                    "discussion": "Do not just transfuse platelets routinely without guidance.",
                    "book_hint": "Clinical Hematology — Rodak / Hoffbrand",
                },
            ],
            "extreme": [
                {
                    "title": "Schistocytes + Low Plt + Confusion",
                    "stem": "MAHA, thrombocytopenia, neurologic changes; coag relatively less DIC-like. Avoid reporting or actions that could harm if a critical quality risk remains open.",
                    "question": "Top concern?",
                    "answer": "TTP — urgent specialist therapy (exchange pathways).",
                    "discussion": "Time-critical.",
                    "book_hint": "Clinical Hematology — Rodak / Hoffbrand",
                },
            ],
        },
    },
    "clinical_chemistry": {
        "label": "Clinical Chemistry",
        "books": [
            "Tietz Fundamentals of Clinical Chemistry",
            "Clinical Chemistry — Bishop",
            "CLSI chemistry documents",
        ],
        "pdf_notes": [
            "Hemolysis falsely elevates K+ — reject/redraw when indicated.",
            "Know critical value notification pathways.",
            "Enzyme panels: pattern recognition > single numbers.",
            "Method interference and reference ranges are lab-specific.",
            "Preanalytic → analytic → postanalytic thinking prevents errors.",
        ],
        "questions": {
            "easy": [
                {
                    "question": "Electrolyte panel commonly includes?",
                    "options": [
                        "A) Na, K, Cl, and bicarbonate (total CO2)",
                        "B) HbA1c and fructosamine only",
                        "C) CBC indices without chemistry analytes",
                        "D) PT/INR without electrolyte measurement",
                    ],
                    "answer": "A) Na, K, Cl, and bicarbonate (total CO2)",
                    "explanation": "A routine electrolyte panel typically measures sodium, potassium, chloride, and bicarbonate (total CO2), reflecting extracellular fluid composition and acid–base balance. These analytes are central to evaluating dehydration, renal disorders, and metabolic disturbances. Interpretation requires awareness of preanalytic factors such as hemolysis affecting potassium.",
                    "choice_explanations": {
                        "A": "A routine electrolyte panel measures sodium, potassium, chloride, and bicarbonate (total CO2), reflecting extracellular fluid composition and acid–base balance.",
                        "B": "HbA1c and fructosamine assess longer-term glycemia, not the core Na/K/Cl/HCO3 set that constitutes an electrolyte panel.",
                        "C": "CBC indices quantify blood cells and are hematology outputs; they do not replace chemistry measurement of electrolytes.",
                        "D": "PT/INR evaluates coagulation pathways and warfarin effect, not electrolyte concentrations.",
                    },
                },
                {
                    "question": "Creatinine mainly reflects?",
                    "options": [
                        "A) Hepatic synthetic function (albumin/INR)",
                        "B) Glomerular filtration (with muscle-mass caveats)",
                        "C) Skeletal muscle enzyme leakage (CK)",
                        "D) Pancreatic amylase secretory capacity",
                    ],
                    "answer": "B) Glomerular filtration (with muscle-mass caveats)",
                    "explanation": "Serum creatinine is produced from muscle creatine metabolism and is cleared primarily by glomerular filtration. Rising creatinine generally indicates reduced glomerular filtration rate, though levels also depend on muscle mass, age, sex, and some drugs. Estimated GFR equations convert creatinine into a more physiologically interpretable filtration index.",
                    "choice_explanations": {
                        "A": "Hepatic synthetic function is reflected by albumin and clotting factors (e.g., INR), whereas creatinine primarily tracks glomerular filtration with muscle-mass caveats.",
                        "B": "Serum creatinine derives from muscle creatine metabolism and is cleared mainly by glomerular filtration, so rising levels generally indicate reduced GFR with interpretive caveats for muscle mass.",
                        "C": "Creatine kinase (CK) rises with skeletal-muscle membrane injury and enzyme leakage; creatinine itself is a filtration marker, not a muscle-injury enzyme.",
                        "D": "Pancreatic amylase reflects exocrine pancreatic enzyme release, unrelated to creatinine’s role as a GFR surrogate.",
                    },
                },
                {
                    "question": "Hypoglycemia means?",
                    "options": [
                        "A) Abnormally high blood glucose",
                        "B) Isolated ketonemia with normal glucose",
                        "C) Abnormally low blood glucose",
                        "D) Elevated hemoglobin without glucose change",
                    ],
                    "answer": "C) Abnormally low blood glucose",
                    "explanation": "Hypoglycemia denotes abnormally low plasma glucose and can cause neuroglycopenic and autonomic symptoms. Critical hypoglycemia is a medical emergency requiring rapid confirmation and treatment. Laboratory practice includes critical-value notification and investigation of causes ranging from insulin excess to hepatic failure and adrenal insufficiency.",
                    "choice_explanations": {
                        "A": "Abnormally high blood glucose defines hyperglycemia, the physiologic opposite of hypoglycemia.",
                        "B": "Ketonemia can accompany insulin deficiency or fasting but does not define hypoglycemia, which is low plasma glucose.",
                        "C": "Hypoglycemia denotes abnormally low plasma glucose and can produce autonomic and neuroglycopenic symptoms requiring rapid confirmation and treatment.",
                        "D": "Hemoglobin concentration is independent of plasma glucose; anemia or erythrocytosis does not define hypoglycemia.",
                    },
                },
            ],
            "medium": [
                {
                    "question": "AST/ALT pattern helps assess?",
                    "options": [
                        "A) Osteoblastic bone turnover alone",
                        "B) Intravascular hemolysis alone",
                        "C) Primary thyroid dysfunction alone",
                        "D) Hepatocellular injury",
                    ],
                    "answer": "D) Hepatocellular injury",
                    "explanation": "Aspartate and alanine aminotransferases (AST and ALT) are cytosolic enzymes released with hepatocyte injury. Elevations with an hepatocellular pattern support hepatitis, ischemic injury, or toxin-mediated damage. In contrast, ALP and GGT elevations more often reflect cholestasis or biliary obstruction.",
                    "choice_explanations": {
                        "A": "Osteoblastic bone turnover is assessed with markers such as bone ALP or osteocalcin, not the hepatocellular aminotransferase pattern of AST/ALT.",
                        "B": "Intravascular hemolysis is supported by LDH, haptoglobin, and bilirubin changes with smear findings; AST may rise secondarily but AST/ALT patterning primarily evaluates hepatocyte injury.",
                        "C": "Thyroid dysfunction is evaluated with TSH and free thyroid hormones, not aminotransferase hepatocellular patterns.",
                        "D": "AST and ALT are cytosolic enzymes released with hepatocyte injury; their elevation in a hepatocellular pattern supports hepatitis, ischemia, or toxin-mediated liver damage.",
                    },
                },
                {
                    "question": "Troponin rise suggests?",
                    "options": [
                        "A) Myocardial injury",
                        "B) Uncomplicated lower UTI",
                        "C) Iron-deficiency anemia alone",
                        "D) Stable chronic kidney disease without injury",
                    ],
                    "answer": "A) Myocardial injury",
                    "explanation": "Cardiac troponins I and T are regulatory proteins released into blood after cardiomyocyte necrosis or injury. Serial rises and/or falls above the assay-specific 99th percentile support myocardial injury and, with clinical criteria, acute myocardial infarction. High-sensitivity assays detect earlier and smaller elevations but require clinical correlation.",
                    "choice_explanations": {
                        "A": "Cardiac troponins I/T are released after cardiomyocyte injury; a rise and/or fall above the assay 99th percentile supports myocardial injury in the appropriate clinical context.",
                        "B": "Uncomplicated lower UTI involves urinary pathogens and pyuria without cardiomyocyte necrosis, so troponin is not a marker of that process.",
                        "C": "Iron-deficiency anemia lowers hemoglobin from depleted iron stores and does not itself release cardiac troponin.",
                        "D": "Stable CKD may affect baseline troponin slightly with some assays, but a rising troponin pattern indicates myocardial injury rather than chronic kidney disease alone.",
                    },
                },
                {
                    "question": "HbA1c reflects?",
                    "options": [
                        "A) A single fasting glucose measurement",
                        "B) Average glycemia over ~2–3 months",
                        "C) Urine glucose excretion at collection",
                        "D) Immediate postprandial insulin dose",
                    ],
                    "answer": "B) Average glycemia over ~2–3 months",
                    "explanation": "Hemoglobin A1c forms by nonenzymatic glycation of hemoglobin and reflects average glycemia over approximately the preceding 2–3 months, corresponding to erythrocyte lifespan. It is used for diabetes diagnosis and long-term glycemic monitoring when conditions affecting red-cell turnover are absent. Method-specific NGSP/IFCC standardization underpins comparability.",
                    "choice_explanations": {
                        "A": "A single fasting glucose is a point-in-time concentration, whereas HbA1c integrates nonenzymatic hemoglobin glycation over roughly the erythrocyte lifespan of 2–3 months.",
                        "B": "HbA1c forms by nonenzymatic glycation of hemoglobin and reflects average glycemia over about the preceding 2–3 months, corresponding to red-cell turnover.",
                        "C": "Urine glucose at collection indicates concurrent glycosuria when the renal threshold is exceeded; it does not summarize months of glycemic exposure like HbA1c.",
                        "D": "Immediate postprandial insulin dosing responds to short-term glucose dynamics, not the long-term glycation signal measured as HbA1c.",
                    },
                },
            ],
            "hard": [
                {
                    "question": "Osmolal gap increases with?",
                    "options": [
                        "A) Isotonic saline infusion without osmoles added",
                        "B) Supplemental oxygen without solute change",
                        "C) Unmeasured osmotically active solutes (e.g., toxic alcohols)",
                        "D) Water-soluble vitamin intake alone",
                    ],
                    "answer": "C) Unmeasured osmotically active solutes (e.g., toxic alcohols)",
                    "explanation": "The osmolal gap is the difference between measured serum osmolality and osmolality calculated from sodium, glucose, and urea. An elevated gap suggests unmeasured osmotically active solutes such as methanol, ethylene glycol, or isopropanol. Toxic-alcohol evaluation pairs the gap with anion gap, blood gases, and specific analyte assays.",
                    "choice_explanations": {
                        "A": "Isotonic saline adds measured sodium and water without creating a large unmeasured osmole burden, so it does not widen the osmolal gap as toxic alcohols do.",
                        "B": "Supplemental oxygen changes dissolved gas content but does not add osmotically active unmeasured solutes that elevate the osmolal gap.",
                        "C": "An elevated osmolal gap (measured minus calculated osmolality) indicates unmeasured osmotically active solutes such as methanol, ethylene glycol, or isopropanol.",
                        "D": "Water-soluble vitamins at usual intakes do not contribute clinically meaningful unmeasured osmoles to raise the osmolal gap.",
                    },
                },
                {
                    "question": "Hook effect can cause?",
                    "options": [
                        "A) Falsely high results from reagent underloading",
                        "B) Specimen hemolysis altering tube color only",
                        "C) Barcode misreads without concentration error",
                        "D) Falsely low immunoassay results at very high analyte",
                    ],
                    "answer": "D) Falsely low immunoassay results at very high analyte",
                    "explanation": "The high-dose hook (prozone-like) effect in sandwich immunoassays occurs when extremely high antigen concentrations saturate capture and detection antibodies, preventing sandwich formation. The reported result can be falsely low or normal despite massive analyte excess. Dilution of the specimen restores linearity and reveals the true high concentration.",
                    "choice_explanations": {
                        "A": "Reagent underloading may cause analytic failure, but the high-dose hook effect specifically yields falsely low sandwich-immunoassay signals when antigen is in extreme excess.",
                        "B": "Hemolysis can interfere with some assays via spectral or chemical effects; it is not the antigen-saturation hook mechanism that falsely lowers immunoassays.",
                        "C": "Barcode misreads are identification errors and do not create concentration-dependent antigen excess that prevents sandwich formation.",
                        "D": "In sandwich immunoassays, extremely high analyte can saturate capture and detection antibodies, preventing bridge formation and producing a falsely low (hook) result.",
                    },
                },
                {
                    "question": "Pseudohyponatremia classic with?",
                    "options": [
                        "A) Severe hyperlipidemia/hyperproteinemia (indirect ISE)",
                        "B) True hypotonic hyponatremia from SIADH alone",
                        "C) Hypertonic hyponatremia from hyperglycemia alone",
                        "D) Hypovolemic hyponatremia from GI losses alone",
                    ],
                    "answer": "A) Severe hyperlipidemia/hyperproteinemia (indirect ISE)",
                    "explanation": "Pseudohyponatremia is an artifactual low sodium reported by indirect potentiometry when marked hyperlipidemia or hyperproteinemia expands the non-aqueous plasma fraction. Direct ion-selective electrode methods that measure activity in the undiluted aqueous phase are largely unaffected. Recognizing method dependence prevents inappropriate hypotonic fluid therapy.",
                    "choice_explanations": {
                        "A": "Pseudohyponatremia is an artifact of indirect potentiometry when severe hyperlipidemia or hyperproteinemia expands the non-aqueous plasma fraction, lowering reported sodium without true hypotonicity.",
                        "B": "SIADH causes true hypotonic hyponatremia from inappropriate ADH with impaired free-water excretion, not the analytic artifact of pseudohyponatremia.",
                        "C": "Hyperglycemia causes hypertonic hyponatremia by osmotic water shift; sodium is truly diluted in plasma water, unlike classic pseudohyponatremia from indirect ISE.",
                        "D": "GI losses produce hypovolemic true hyponatremia from sodium and water deficits with ADH responses, not lipid/protein–related measurement artifact.",
                    },
                },
            ],
            "extreme": [
                {
                    "question": "Critical value policy requires?",
                    "options": [
                        "A) Batch filing of alerts at weekly review",
                        "B) Rapid clinician notification and documentation",
                        "C) Release without repeat or verification steps",
                        "D) Direct patient email without clinician contact",
                    ],
                    "answer": "B) Rapid clinician notification and documentation",
                    "explanation": "Critical laboratory values identify results that may indicate life-threatening conditions requiring immediate clinical action. Laboratory policy mandates rapid clinician notification, read-back verification, and documentation of the communication. Timely reporting is a core patient-safety and accreditation requirement.",
                    "choice_explanations": {
                        "A": "Batching critical alerts for weekly review delays treatment of life-threatening results. Critical-value policy requires rapid clinician notification with documentation.",
                        "B": "Critical values indicate potentially life-threatening conditions; laboratory policy requires rapid clinician notification, read-back verification, and documentation of the communication.",
                        "C": "Releasing critical results without verification steps risks reporting analytic error. Policies typically include repeat/verification plus immediate clinician contact.",
                        "D": "Direct patient email bypasses the licensed clinician responsible for emergent action and does not satisfy critical-notification requirements.",
                    },
                },
                {
                    "question": "Delta check flags?",
                    "options": [
                        "A) New patient registration without prior values",
                        "B) Preferred collection-tube color mismatch",
                        "C) Implausible change versus prior patient results",
                        "D) Printer or label-stock hardware faults",
                    ],
                    "answer": "C) Implausible change versus prior patient results",
                    "explanation": "Delta checks compare a current result with a patient’s recent prior values to detect implausible analytic or identity errors. Large unexpected changes may indicate specimen mix-up, IV contamination, or instrument malfunction rather than true physiology. Investigation before release protects against reporting erroneous results.",
                    "choice_explanations": {
                        "A": "A brand-new patient lacks priors for comparison; delta checks require previous results from the same patient to flag implausible change.",
                        "B": "Tube-color mismatch is a collection/order error detected by order rules or staff check, not by numeric delta comparison to prior results.",
                        "C": "Delta checks compare a current result with the patient’s recent priors to detect implausible analytic changes that may indicate mix-up, contamination, or true abrupt pathology.",
                        "D": "Printer or label-stock faults are hardware issues outside the numeric delta-check logic that compares serial patient results.",
                    },
                },
                {
                    "question": "Blood gas preanalytics: air bubbles cause?",
                    "options": [
                        "A) Improved accuracy by ambient equilibration",
                        "B) No measurable effect on blood-gas values",
                        "C) Isolated glucose elevation without gas change",
                        "D) Distorted pO2/pCO2 from gas exchange",
                    ],
                    "answer": "D) Distorted pO2/pCO2 from gas exchange",
                    "explanation": "Air bubbles in arterial blood-gas syringes allow gas exchange that can falsely raise pO2 toward ambient air and alter pCO2. Delayed analysis permits ongoing cellular metabolism that consumes oxygen and generates CO2. Specimens should be carefully debubbled, mixed, and analyzed promptly under anaerobic conditions.",
                    "choice_explanations": {
                        "A": "Ambient equilibration through air bubbles does not improve accuracy; it drives pO2 toward room-air values and alters pCO2 through gas exchange.",
                        "B": "Air bubbles measurably distort blood-gas tensions by allowing O2 and CO2 exchange with ambient air before analysis.",
                        "C": "Glucose changes from delayed metabolism are separate; air bubbles specifically perturb dissolved gas tensions rather than isolating a glucose artifact.",
                        "D": "Air bubbles in arterial syringes permit gas exchange that can falsely raise pO2 toward ambient air and alter pCO2, distorting blood-gas interpretation.",
                    },
                },
            ],
        },
        "cases": {
            "easy": [
                {
                    "title": "High K on Lab Call",
                    "stem": "Lab flags K 6.8 mmol/L.",
                    "question": "First lab/clinical check?",
                    "answer": "Rule out hemolysis/EDTA contamination; inform clinician for ECG/treatment.",
                    "discussion": "Preanalytical errors common.",
                    "book_hint": "Tietz Textbook of Clinical Chemistry",
                },
            ],
            "medium": [
                {
                    "title": "Jaundice Labs",
                    "stem": "High bilirubin with high ALP/GGT predominance.",
                    "question": "Pattern?",
                    "answer": "Cholestatic/obstructive theme — correlate imaging.",
                    "discussion": "vs hepatocellular AST/ALT dominant.",
                    "book_hint": "Tietz Textbook of Clinical Chemistry",
                },
            ],
            "hard": [
                {
                    "title": "Very High hCG but Assay Low",
                    "stem": "Clinical molar pregnancy suspected; hCG unexpectedly not sky-high. Choose the safest high-yield next laboratory concept.",
                    "question": "Consider?",
                    "answer": "Hook effect — dilute specimen.",
                    "discussion": "Communicate with lab.",
                    "book_hint": "Tietz Textbook of Clinical Chemistry",
                },
            ],
            "extreme": [
                {
                    "title": "Mismatch Glucose POCT vs Lab",
                    "stem": "Fingerstick 45 mg/dL; venous lab 110 mg/dL in shocked patient. Avoid reporting or actions that could harm if a critical quality risk remains open.",
                    "question": "Concept?",
                    "answer": "POCT limitations in poor perfusion — confirm critically with lab method.",
                    "discussion": "Treat patient, verify method.",
                    "book_hint": "Tietz Textbook of Clinical Chemistry",
                },
            ],
        },
    },
    "medical_microbiology": {
        "label": "Medical Microbiology",
        "books": [
            "Bailey & Scott's Diagnostic Microbiology",
            "CLSI M100",
            "Murray Medical Microbiology",
        ],
        "pdf_notes": [
            "Gram stain guides early therapy and culture workup.",
            "AST breakpoints are CLSI/EUCAST version-dependent.",
            "Blood culture contamination vs true bacteremia matters.",
            "Biosafety: never smell plates; escalate select agents correctly.",
            "Stewardship: report actionable MICs and resistance alerts.",
        ],
        "questions": {
            "easy": [
                {
                    "question": "Gram-positive organisms stain?",
                    "options": [
                        "A) Purple/blue (retain crystal violet)",
                        "B) Pink/red (take safranin counterstain)",
                        "C) Colorless after decolorization step",
                        "D) Acid-fast red without Gram reagents",
                    ],
                    "answer": "A) Purple/blue (retain crystal violet)",
                    "explanation": "Gram-positive bacteria retain crystal violet–iodine complex within a thick peptidoglycan cell wall and appear purple/blue. Gram-negative organisms lose the complex during decolorization and take up the pink/red counterstain. Correct interpretation requires properly made smears and controlled decolorization.",
                    "choice_explanations": {
                        "A": "Gram-positive organisms retain the crystal violet–iodine complex within thick peptidoglycan and appear purple/blue after the Gram procedure.",
                        "B": "Pink/red safranin staining after decolorization characterizes Gram-negative organisms with thinner peptidoglycan and outer membrane, not Gram-positives.",
                        "C": "Colorless cells after decolorization indicate failure to retain crystal violet and would not be read as Gram-positive; Gram-positives remain purple/blue.",
                        "D": "Acid-fast staining targets mycolic acid–rich mycobacteria and uses different reagents than the Gram stain’s crystal-violet retention by Gram-positives.",
                    },
                },
                {
                    "question": "Blood culture indication theme?",
                    "options": [
                        "A) Routine wellness screening without fever",
                        "B) Suspected bacteremia/sepsis",
                        "C) Isolated asymptomatic bacteriuria workup",
                        "D) Surveillance of environmental surfaces",
                    ],
                    "answer": "B) Suspected bacteremia/sepsis",
                    "explanation": "Blood cultures are indicated when bacteremia or sepsis is suspected clinically. Adequate blood volume per bottle and collection of multiple sets before antibiotics maximize recovery. Timing, skin antisepsis, and bottle fill volume critically affect sensitivity and contamination rates.",
                    "choice_explanations": {
                        "A": "Blood cultures are not indicated for asymptomatic wellness screening; they are reserved for suspected bacteremia or sepsis where recovery guides therapy.",
                        "B": "Blood cultures are indicated when bacteremia or sepsis is suspected; adequate volume and multiple sets before antibiotics maximize pathogen recovery.",
                        "C": "Asymptomatic bacteriuria workups use urine culture criteria, not routine blood cultures, unless systemic infection is suspected.",
                        "D": "Environmental surface surveillance uses swabs and contact plates for infection control, not patient blood-culture bottles.",
                    },
                },
                {
                    "question": "Antibiotic susceptibility testing guides?",
                    "options": [
                        "A) Species identification without MIC data",
                        "B) Only infection-control isolation decisions",
                        "C) Antimicrobial therapy selection",
                        "D) Only vaccine schedule recommendations",
                    ],
                    "answer": "C) Antimicrobial therapy selection",
                    "explanation": "Antimicrobial susceptibility testing determines whether an isolate is inhibited by achievable drug concentrations. Interpreted breakpoints (CLSI/EUCAST) categorize isolates as susceptible, intermediate, or resistant to guide therapy. Results must be linked to correct organism identification and clinical site of infection.",
                    "choice_explanations": {
                        "A": "Species identification names the organism but does not by itself provide MIC or breakpoint interpretation needed to select antimicrobials.",
                        "B": "Isolation decisions use transmission routes and organism epidemiology; AST specifically guides which drugs are likely to inhibit the isolate.",
                        "C": "Antimicrobial susceptibility testing determines whether achievable drug concentrations inhibit an isolate, guiding therapy via CLSI/EUCAST breakpoints.",
                        "D": "Vaccine schedules are immunization policy; they are not derived from an isolate’s AST profile.",
                    },
                },
            ],
            "medium": [
                {
                    "question": "Acid-fast stain used for?",
                    "options": [
                        "A) Routine Enterobacterales Gram morphology",
                        "B) Fungal hyphae on KOH preparation",
                        "C) Parasitic ova on saline wet mount",
                        "D) Mycobacteria (mycolic acid–rich walls)",
                    ],
                    "answer": "D) Mycobacteria (mycolic acid–rich walls)",
                    "explanation": "Acid-fast stains such as Ziehl–Neelsen or fluorochrome auramine exploit mycolic acid–rich cell walls that resist acid-alcohol decolorization, highlighting mycobacteria. Partial acid-fastness also aids detection of Nocardia and some coccidia. Results are correlated with culture and molecular assays.",
                    "choice_explanations": {
                        "A": "Enterobacterales Gram morphology uses Gram stain, not acid-fast chemistry. Acid-fast stains target mycolic acid–rich mycobacterial walls.",
                        "B": "KOH preparations clear keratin to reveal fungal elements; they are not acid-fast stains for mycobacteria.",
                        "C": "Saline wet mounts detect motile trophozoites or ova morphologically and do not use acid-fast mycolic-acid chemistry.",
                        "D": "Acid-fast stains (Ziehl–Neelsen, auramine) exploit mycolic acid–rich walls that resist acid-alcohol decolorization, highlighting mycobacteria.",
                    },
                },
                {
                    "question": "Catalase-positive gram-positive cocci suggest?",
                    "options": [
                        "A) Staphylococci",
                        "B) Streptococci (catalase-negative)",
                        "C) Enterococci (catalase-negative)",
                        "D) Lactobacilli (catalase-negative rods)",
                    ],
                    "answer": "A) Staphylococci",
                    "explanation": "Catalase decomposes hydrogen peroxide to water and oxygen; bubbling indicates a positive reaction. Among gram-positive cocci, staphylococci are catalase-positive whereas streptococci and enterococci are catalase-negative. Further tests (coagulase, MALDI-TOF) refine species identification.",
                    "choice_explanations": {
                        "A": "Among gram-positive cocci, staphylococci produce catalase that liberates oxygen from hydrogen peroxide, distinguishing them from catalase-negative streptococci/enterococci.",
                        "B": "Streptococci are catalase-negative gram-positive cocci; a positive catalase reaction points away from Streptococcus toward Staphylococcus.",
                        "C": "Enterococci are catalase-negative (or weakly reactive) gram-positive cocci in pairs/chains, not the strongly catalase-positive staphylococci.",
                        "D": "Lactobacilli are catalase-negative rods, so they match neither the coccal morphology nor the catalase-positive staphylococcal pattern.",
                    },
                },
                {
                    "question": "CSF Gram stain urgency?",
                    "options": [
                        "A) Low priority elective outpatient screen",
                        "B) Critical for suspected bacterial meningitis",
                        "C) Useful only after 72-hour culture growth",
                        "D) Replaced entirely by chemistry panels",
                    ],
                    "answer": "B) Critical for suspected bacterial meningitis",
                    "explanation": "CSF Gram stain is a time-critical test in suspected bacterial meningitis because early morphologic clues can guide empiric therapy. Rapid reporting of organisms and leukocytes supports antimicrobial and infection-control decisions. Negative stains do not exclude infection when clinical suspicion remains high.",
                    "choice_explanations": {
                        "A": "CSF Gram stain in suspected meningitis is time-critical, not an elective outpatient screen, because early organism morphology guides empiric therapy.",
                        "B": "In suspected bacterial meningitis, rapid CSF Gram stain can reveal organisms and inflammation, supporting immediate antimicrobial and infection-control decisions.",
                        "C": "Waiting 72 hours for culture growth delays life-saving therapy; Gram stain provides same-day morphologic clues while cultures incubate.",
                        "D": "CSF chemistry (glucose, protein) supports interpretation but does not replace direct visualization of organisms on Gram stain.",
                    },
                },
            ],
            "hard": [
                {
                    "question": "MRSA detected by?",
                    "options": [
                        "A) Penicillin disk testing alone without cefoxitin",
                        "B) Macrolike D-test alone without oxacillin screen",
                        "C) Oxacillin/cefoxitin testing and/or mecA detection",
                        "D) Aminoglycoside synergy screen alone",
                    ],
                    "answer": "C) Oxacillin/cefoxitin testing and/or mecA detection",
                    "explanation": "Methicillin-resistant Staphylococcus aureus (MRSA) harbors mecA (or mecC), encoding altered penicillin-binding protein PBP2a. Cefoxitin disk or MIC testing and molecular mecA assays are preferred phenotypic/genotypic detectors. Accurate MRSA recognition drives therapy and infection-control precautions.",
                    "choice_explanations": {
                        "A": "Penicillin disk testing alone does not reliably detect mecA-mediated methicillin resistance; cefoxitin/oxacillin testing or mecA assays are preferred.",
                        "B": "The D-test detects inducible clindamycin resistance (erm) and does not establish oxacillin/methicillin resistance defining MRSA.",
                        "C": "MRSA harbors mecA/mecC encoding PBP2a; detection uses oxacillin or cefoxitin phenotypic testing and/or molecular mecA assays.",
                        "D": "Aminoglycoside synergy screens assess combination activity (e.g., for enterococci) and do not define methicillin resistance in S. aureus.",
                    },
                },
                {
                    "question": "Anaerobic culture needs?",
                    "options": [
                        "A) Ambient-air swabs held overnight unsealed",
                        "B) CO2 jar without anaerobic indicator systems",
                        "C) Refrigeration of all anaerobe specimens only",
                        "D) Oxygen-free transport and incubation conditions",
                    ],
                    "answer": "D) Oxygen-free transport and incubation conditions",
                    "explanation": "Obligate anaerobes are killed or inhibited by oxygen exposure during collection and transport. Successful anaerobic culture requires appropriate oxygen-free transport devices, prompt plating, and incubation in validated anaerobic atmospheres. Specimen quality and site selection are as important as media choice.",
                    "choice_explanations": {
                        "A": "Ambient-air swabs held overnight expose obligate anaerobes to oxygen and often kill them before plating, defeating anaerobic recovery.",
                        "B": "Elevated CO2 alone does not create the oxygen-free atmosphere anaerobes require; anaerobic generators/chambers with indicators are needed.",
                        "C": "Refrigeration can harm some anaerobes and does not substitute for oxygen-free transport and incubation systems.",
                        "D": "Obligate anaerobes require oxygen-free transport devices and anaerobic incubation because atmospheric oxygen is toxic or inhibitory to them.",
                    },
                },
                {
                    "question": "Blood culture contamination clues?",
                    "options": [
                        "A) Common skin flora in only 1 of multiple sets",
                        "B) Same pathogen in multiple sets drawn apart",
                        "C) Growth of Enterobacterales in all bottles rapidly",
                        "D) Candida in multiple sets from central lines",
                    ],
                    "answer": "A) Common skin flora in only 1 of multiple sets",
                    "explanation": "Blood-culture contaminants are often skin flora recovered from only one bottle or one set when multiple sets are drawn. True bacteremia more often yields the same organism in multiple sets with a compatible clinical picture. Distinguishing contamination prevents unnecessary antibiotics and workups.",
                    "choice_explanations": {
                        "A": "Common skin flora recovered from only one of multiple independently drawn sets often represents contamination rather than true bacteremia.",
                        "B": "The same pathogen in multiple sets drawn apart in time/site more strongly supports true bacteremia than contamination.",
                        "C": "Rapid growth of Enterobacterales in multiple bottles typically indicates true bloodstream infection, not skin-flora contamination.",
                        "D": "Candida in multiple central-line sets commonly reflects true fungemia and warrants clinical action, unlike single-set skin contaminants.",
                    },
                },
            ],
            "extreme": [
                {
                    "question": "Carbapenemase-producing Enterobacterales require?",
                    "options": [
                        "A) Routine community AST without confirmatory assays",
                        "B) Infection control plus specialized testing/stewardship",
                        "C) Outpatient observation without isolation review",
                        "D) Standard ampicillin therapy without resistance workup",
                    ],
                    "answer": "B) Infection control plus specialized testing/stewardship",
                    "explanation": "Carbapenemase-producing Enterobacterales hydrolyze carbapenems and many other β-lactams, severely limiting therapeutic options. Detection triggers infection-control precautions and often specialized confirmatory tests and stewardship consultation. Misclassification risks both treatment failure and institutional spread.",
                    "choice_explanations": {
                        "A": "Routine community AST without carbapenemase confirmation can miss or under-characterize CPE, delaying infection control and specialized therapy decisions.",
                        "B": "Carbapenemase-producing Enterobacterales hydrolyze carbapenems; detection mandates infection-control precautions plus specialized confirmatory testing and stewardship-guided therapy.",
                        "C": "Outpatient observation without isolation review risks transmission of CPE, which require contact precautions and laboratory/epidemiology coordination.",
                        "D": "Ampicillin is inactive against most Enterobacterales with carbapenemases; resistance mechanisms must be characterized and therapy tailored.",
                    },
                },
                {
                    "question": "Biosafety for Neisseria meningitidis work?",
                    "options": [
                        "A) Open-bench sniffing of plate odors for ID",
                        "B) BSL-1 practices without aerosol controls",
                        "C) Appropriate BSL practices to protect staff",
                        "D) No risk once colonies appear on solid media",
                    ],
                    "answer": "C) Appropriate BSL practices to protect staff",
                    "explanation": "Neisseria meningitidis can cause severe laboratory-acquired infection through aerosol exposure during manipulation of cultures. Work with potentially infectious material requires appropriate biosafety level practices, PPE, and vaccination policies where indicated. Suspect isolates should be handled with heightened precautions.",
                    "choice_explanations": {
                        "A": "Sniffing plates risks aerosol inhalation of N. meningitidis, a documented cause of laboratory-acquired meningococcal disease.",
                        "B": "BSL-1 practices lack the aerosol controls needed for work with invasive N. meningitidis cultures.",
                        "C": "Neisseria meningitidis can cause severe laboratory-acquired infection via aerosols, so manipulation requires appropriate biosafety practices and containment.",
                        "D": "Colonies on solid media remain infectious; risk persists until organisms are inactivated or handled under proper containment.",
                    },
                },
                {
                    "question": "MALDI-TOF identifies?",
                    "options": [
                        "A) Antimicrobial MICs by spectral peak height",
                        "B) Only viral loads from plasma protein spectra",
                        "C) Only toxin genes without culture isolate",
                        "D) Organisms by protein mass spectral fingerprints",
                    ],
                    "answer": "D) Organisms by protein mass spectral fingerprints",
                    "explanation": "Matrix-assisted laser desorption/ionization time-of-flight (MALDI-TOF) mass spectrometry identifies microorganisms from characteristic protein mass spectra compared with reference libraries. It rapidly IDs many bacteria and yeasts from culture but does not replace susceptibility testing. Library coverage and extraction methods affect performance for some taxa.",
                    "choice_explanations": {
                        "A": "MALDI-TOF identifies organisms by protein mass fingerprints; it does not measure antimicrobial MICs from spectral peak height.",
                        "B": "Viral load quantitation uses nucleic-acid amplification, not bacterial colony protein spectra from MALDI-TOF.",
                        "C": "Toxin-gene detection requires molecular assays; MALDI-TOF identifies cultured isolates by proteomic spectra, not genes directly from specimens alone.",
                        "D": "MALDI-TOF MS matches characteristic protein mass spectral fingerprints of cultured organisms to reference libraries for rapid identification.",
                    },
                },
            ],
        },
        "cases": {
            "easy": [
                {
                    "title": "UTI Culture",
                    "stem": "Dysuria; midstream urine culture growing E. coli >10^5 CFU/mL.",
                    "question": "Interpretation theme?",
                    "answer": "Consistent with UTI if clinical match; report susceptibilities.",
                    "discussion": "Contamination if mixed flora skin organisms.",
                    "book_hint": "Bailey & Scott's Diagnostic Microbiology",
                },
            ],
            "medium": [
                {
                    "title": "CSF Cloudy",
                    "stem": "Fever, neck stiffness; CSF WBC high, Gram-negative diplococci.",
                    "question": "Likely?",
                    "answer": "Meningococcal meningitis theme — urgent report/treatment coordination.",
                    "discussion": "Lab biosafety.",
                    "book_hint": "Bailey & Scott's Diagnostic Microbiology",
                },
            ],
            "hard": [
                {
                    "title": "CoNS in One Bottle",
                    "stem": "One of four bottles grows coagulase-negative staph in a non-device patient. Choose the safest high-yield next laboratory concept.",
                    "question": "Likely?",
                    "answer": "Possible contaminant — correlate clinically; may not treat.",
                    "discussion": "Device patients differ.",
                    "book_hint": "Bailey & Scott's Diagnostic Microbiology",
                },
            ],
            "extreme": [
                {
                    "title": "Possible Brucella on Bench",
                    "stem": "Slow-growing gram-negative coccobacilli from blood; history of farm exposure. Avoid reporting or actions that could harm if a critical quality risk remains open.",
                    "question": "Action?",
                    "answer": "Stop aerosol-generating work; BSL precautions; notify; rule out Brucella.",
                    "discussion": "Do not sniff plates.",
                    "book_hint": "Bailey & Scott's Diagnostic Microbiology",
                },
            ],
        },
    },
    "immunology": {
        "label": "Immunology & Serology",
        "books": [
            "Clinical Immunology textbooks",
            "Henry's Clinical Diagnosis",
            "Assay package inserts / IFU",
        ],
        "pdf_notes": [
            "Sensitivity vs specificity vs PPV/NPV depend on prevalence.",
            "Syphilis algorithms: nontreponemal + treponemal confirmation themes.",
            "HIV testing follows staged algorithms — do not stop at one reactive.",
            "ANA patterns guide follow-up antibody panels.",
            "Heterophile antibodies and cross-reactivity cause false results.",
        ],
        "questions": {
            "easy": [
                {
                    "question": "ELISA detects?",
                    "options": [
                        "A) Antigen or antibody via enzyme-linked assay",
                        "B) Blood-film morphologic differentials",
                        "C) Serum electrolyte concentrations",
                        "D) Urine crystal identification",
                    ],
                    "answer": "A) Antigen or antibody via enzyme-linked assay",
                    "explanation": "Enzyme-linked immunosorbent assay (ELISA) immobilizes antigen or antibody on a solid phase and uses an enzyme-conjugated detector to generate a measurable signal. Formats can detect antigen or antibody depending on assay design. Controls and cutoff verification are essential for valid qualitative or quantitative results.",
                    "choice_explanations": {
                        "A": "ELISA immobilizes antigen or antibody on a solid phase and uses an enzyme-conjugated detector to generate a measurable signal for antigen or antibody detection.",
                        "B": "Blood-film differentials assess leukocyte morphology microscopically and do not use enzyme-linked solid-phase immunoassay chemistry.",
                        "C": "Serum electrolytes are measured by ion-selective electrodes or related chemistry methods, not ELISA immunochemistry.",
                        "D": "Urine crystal identification is microscopic and chemical, unrelated to enzyme-linked immunosorbent detection of antigen/antibody.",
                    },
                },
                {
                    "question": "IgM generally indicates?",
                    "options": [
                        "A) Long-term immune memory only (IgG pattern)",
                        "B) Acute/recent humoral response",
                        "C) Mucosal secretory immunity only (IgA)",
                        "D) Mast-cell bound allergy only (IgE)",
                    ],
                    "answer": "B) Acute/recent humoral response",
                    "explanation": "IgM is the isotype produced earliest in a primary humoral response and therefore often marks acute or recent antigen exposure. IgG typically rises later and persists in memory responses. Interpretation must consider rheumatoid factor, class switching, and assay-specific cutoffs.",
                    "choice_explanations": {
                        "A": "Long-term immune memory is typically carried by IgG (and memory B/T cells); IgM marks the early primary humoral response rather than durable memory alone.",
                        "B": "IgM is the isotype produced earliest in a primary humoral response and therefore often indicates acute or recent antigen exposure.",
                        "C": "Secretory IgA dominates mucosal immunity; IgM’s diagnostic theme is early systemic humoral response, not mucosal secretion specifically.",
                        "D": "IgE binds mast cells and mediates type I allergy; it is a different isotype from IgM’s acute/recent humoral pattern.",
                    },
                },
                {
                    "question": "Blood type ABO based on?",
                    "options": [
                        "A) HLA class I typing of lymphocytes alone",
                        "B) Serum immunoglobulin subclass levels alone",
                        "C) RBC antigens and reciprocal plasma isoagglutinins",
                        "D) Platelet glycoprotein antigen typing alone",
                    ],
                    "answer": "C) RBC antigens and reciprocal plasma isoagglutinins",
                    "explanation": "ABO blood group is defined by carbohydrate antigens on the red-cell surface and by reciprocal isoagglutinins (anti-A/anti-B) in plasma. Forward and reverse typing must agree for valid ABO assignment. Discrepancies require resolution before transfusion.",
                    "choice_explanations": {
                        "A": "HLA class I typing matches lymphocytes for transplantation and does not define ABO carbohydrate antigens and isoagglutinins.",
                        "B": "Immunoglobulin subclass quantitation assesses humoral immunodeficiency themes, not ABO red-cell antigen/antibody pairing.",
                        "C": "ABO blood group is defined by A/B carbohydrate antigens on RBCs and reciprocal anti-A/anti-B isoagglutinins in plasma, reconciled by forward and reverse typing.",
                        "D": "Platelet glycoprotein antigens relate to platelet immunology (e.g., HPA), not the ABO system on erythrocytes.",
                    },
                },
            ],
            "medium": [
                {
                    "question": "ANA testing used in?",
                    "options": [
                        "A) Acute bacterial culture identification",
                        "B) Routine newborn metabolic screening",
                        "C) Therapeutic drug monitoring of digoxin",
                        "D) Autoimmune disease workups (e.g., SLE themes)",
                    ],
                    "answer": "D) Autoimmune disease workups (e.g., SLE themes)",
                    "explanation": "Antinuclear antibody (ANA) testing screens for autoantibodies directed against nuclear antigens and is used in the workup of systemic autoimmune diseases such as SLE. Pattern and titer information guide reflex antigen-specific assays. Low-titer positives can occur in healthy individuals and require clinical correlation.",
                    "choice_explanations": {
                        "A": "Bacterial identification uses culture and biochemical/proteomic methods; ANA screens for nuclear autoantibodies in systemic autoimmunity.",
                        "B": "Newborn metabolic screens detect inborn errors via metabolites/enzymes, not antinuclear autoantibodies.",
                        "C": "Digoxin therapeutic drug monitoring measures drug concentration, unrelated to ANA autoantibody detection.",
                        "D": "ANA testing screens for autoantibodies against nuclear antigens and is used in workups of systemic autoimmune diseases such as SLE.",
                    },
                },
                {
                    "question": "Window period means?",
                    "options": [
                        "A) Infection present but markers not yet detectable",
                        "B) Infection cleared with lifelong seronegativity",
                        "C) Vaccine response mistaken for acute infection",
                        "D) Assay interference from heterophile antibodies only",
                    ],
                    "answer": "A) Infection present but markers not yet detectable",
                    "explanation": "The serologic window period is the interval after infection when the pathogen is present but diagnostic markers remain below assay detection limits. During this time, antibody or even some antigen/NAAT assays may be negative despite transmissibility. Understanding window periods informs retesting strategy and counseling.",
                    "choice_explanations": {
                        "A": "The window period is the interval after infection when pathogen is present but diagnostic markers remain below assay detection limits, risking false-negative serology/NAAT.",
                        "B": "Cleared infection with lifelong seronegativity is not the window-period concept; the window is early infection before markers rise to detectable levels.",
                        "C": "Vaccine-induced antibodies are an interpretive caveat but do not define the pre-seroconversion infectious window period.",
                        "D": "Heterophile interference can distort immunoassays but is a separate analytic artifact from the biologic detection lag of the window period.",
                    },
                },
                {
                    "question": "Complement C3/C4 low in?",
                    "options": [
                        "A) Most IgE-mediated allergic rhinitis episodes",
                        "B) Some immune-complex diseases (e.g., lupus nephritis)",
                        "C) Uncomplicated iron-deficiency anemia",
                        "D) Isolated osteoarthritis without inflammation",
                    ],
                    "answer": "B) Some immune-complex diseases (e.g., lupus nephritis)",
                    "explanation": "Complement components C3 and C4 are consumed in classical-pathway activation by immune complexes. Low C3/C4 levels are classically seen in active SLE, especially lupus nephritis, and some other immune-complex disorders. Serial levels help monitor disease activity alongside clinical findings.",
                    "choice_explanations": {
                        "A": "IgE-mediated allergic rhinitis is type I hypersensitivity without classical complement consumption lowering C3/C4 as in immune-complex disease.",
                        "B": "C3 and C4 are consumed during classical-pathway activation by immune complexes; low levels are classic in active SLE/lupus nephritis and related immune-complex diseases.",
                        "C": "Iron-deficiency anemia depletes iron stores without activating complement cascades that lower C3/C4.",
                        "D": "Osteoarthritis is primarily degenerative and does not classically consume complement like immune-complex glomerulonephritis or SLE.",
                    },
                },
            ],
            "hard": [
                {
                    "question": "Prozone/hook in serology causes?",
                    "options": [
                        "A) False-positive results at antigen deficit only",
                        "B) Correct titers without need for dilution",
                        "C) False-negative results at antibody excess",
                        "D) Only hemolysis without titer effects",
                    ],
                    "answer": "C) False-negative results at antibody excess",
                    "explanation": "Prozone (antibody excess) in agglutination or precipitation serology can prevent lattice formation and yield a false-negative result. Diluting the specimen restores the zone of equivalence and reveals true reactivity. Recognizing prozone prevents missed diagnoses in high-titer sera.",
                    "choice_explanations": {
                        "A": "Antigen deficit can cause postzone effects; prozone specifically is antibody excess that prevents lattice formation and yields false-negative serology.",
                        "B": "Prozone invalidates undiluted titers until dilution restores equivalence; correct results may require dilution, not assumption of validity.",
                        "C": "In agglutination/precipitation serology, antibody excess (prozone) prevents lattice formation and can produce a false-negative result until the specimen is diluted.",
                        "D": "Hemolysis is a specimen integrity issue; prozone is an immunologic zone-of-equivalence failure causing false-negative titers.",
                    },
                },
                {
                    "question": "Flow cytometry immunophenotyping used for?",
                    "options": [
                        "A) Measuring serum electrolyte panels only",
                        "B) Quantifying urine specific gravity only",
                        "C) Determining PT/INR therapeutic ranges only",
                        "D) Lineage/marker characterization of cell populations",
                    ],
                    "answer": "D) Lineage/marker characterization of cell populations",
                    "explanation": "Flow cytometry immunophenotyping uses fluorescent antibodies to characterize cell-surface and intracellular markers. It is central to diagnosing and classifying leukemias/lymphomas and assessing immune subsets. Gating strategy, controls, and panel design determine interpretive accuracy.",
                    "choice_explanations": {
                        "A": "Electrolyte panels use chemistry analyzers; flow immunophenotyping characterizes cells with fluorescent antibodies to lineage markers.",
                        "B": "Urine specific gravity estimates concentrating ability and is not a multiparameter immunophenotyping application.",
                        "C": "PT/INR monitors coagulation pathways; flow cytometry immunophenotypes cell populations by surface/intracellular markers.",
                        "D": "Flow cytometry immunophenotyping uses fluorescent antibodies to define lineage and maturation markers, central to leukemia/lymphoma classification and immune profiling.",
                    },
                },
                {
                    "question": "Rheumatoid factor can interfere with?",
                    "options": [
                        "A) Some immunoassays (false-positive/negative themes)",
                        "B) Blood gas pH electrode calibration only",
                        "C) Gram-stain decolorization timing only",
                        "D) Urine dipstick leukocyte esterase only",
                    ],
                    "answer": "A) Some immunoassays (false-positive/negative themes)",
                    "explanation": "Rheumatoid factor (typically IgM anti-IgG) can bridge capture and detection antibodies in sandwich immunoassays, causing false-positive signals, or otherwise perturb assay architecture. Blocking reagents and alternative assay designs mitigate interference. Unexpected serology results may prompt RF investigation.",
                    "choice_explanations": {
                        "A": "Rheumatoid factor (often IgM anti-IgG) can bridge capture and detection antibodies in sandwich immunoassays, causing false-positive or otherwise distorted results.",
                        "B": "Blood-gas pH electrode calibration depends on buffers and electrode function, not rheumatoid-factor bridging of immunoassay antibodies.",
                        "C": "Gram-stain timing is a microscopy technique variable unrelated to RF immunoassay interference.",
                        "D": "Leukocyte esterase detects WBC enzymes on dipsticks; RF interference is an immunoassay serology problem, not dipstick chemistry.",
                    },
                },
            ],
            "extreme": [
                {
                    "question": "Heterophile antibodies may cause?",
                    "options": [
                        "A) Only true pathogen-specific neutralizing titers",
                        "B) False-positive or false-negative immunoassay results",
                        "C) Only elevated ESR without immunoassay effect",
                        "D) Only ABO discrepancies without serology effect",
                    ],
                    "answer": "B) False-positive or false-negative immunoassay results",
                    "explanation": "Heterophile antibodies are polyspecific human antibodies that can bind assay immunoglobulins and distort immunoassay signals. They may produce falsely high or low analyte results depending on assay format. Heterophile blockers and alternative methods help confirm suspected interference.",
                    "choice_explanations": {
                        "A": "Heterophile antibodies are nonspecific binders of assay immunoglobulins, not proof of true pathogen-neutralizing titers.",
                        "B": "Heterophile antibodies can bind reagent immunoglobulins and distort immunoassay signals, producing falsely high or low analyte results depending on assay format.",
                        "C": "ESR elevation reflects acute-phase inflammation and does not explain heterophile-driven immunoassay signal distortion.",
                        "D": "ABO discrepancies have many causes; heterophile antibodies classically interfere with solid-phase immunoassays rather than defining ABO typing alone.",
                    },
                },
                {
                    "question": "QuantiFERON-TB (IGRA) interprets?",
                    "options": [
                        "A) Direct acid-fast smear of sputum alone",
                        "B) Serum IgM to mycobacterial cell wall alone",
                        "C) T-cell IFN-γ response to TB antigens",
                        "D) TST induration millimeters without antigens",
                    ],
                    "answer": "C) T-cell IFN-γ response to TB antigens",
                    "explanation": "Interferon-gamma release assays such as QuantiFERON measure T-cell IFN-γ release after stimulation with M. tuberculosis–specific antigens. Results aid diagnosis of latent or active TB infection in conjunction with clinical and radiographic data. Indeterminate results often reflect immunosuppression or technical failure of controls.",
                    "choice_explanations": {
                        "A": "Acid-fast sputum smear detects mycobacteria morphologically but is not an IGRA measuring T-cell IFN-γ release to TB antigens.",
                        "B": "Serum IgM to mycobacterial components is not the QuantiFERON mechanism, which quantifies antigen-specific T-cell IFN-γ production.",
                        "C": "QuantiFERON and related IGRAs measure T-cell interferon-γ release after stimulation with M. tuberculosis–specific antigens to support TB infection diagnosis.",
                        "D": "TST measures delayed-type hypersensitivity induration in vivo; IGRA instead quantifies IFN-γ from antigen-stimulated T cells in vitro.",
                    },
                },
                {
                    "question": "Cryoglobulin specimens require?",
                    "options": [
                        "A) Immediate refrigeration before clotting",
                        "B) Frozen transport on dry ice before clotting",
                        "C) Room-temperature delay of several days",
                        "D) Collection/transport at 37°C before separation",
                    ],
                    "answer": "D) Collection/transport at 37°C before separation",
                    "explanation": "Cryoglobulins precipitate at cold temperatures, so specimens must be collected and maintained at 37°C until serum is separated. Premature cooling can falsely lower measured cryoglobulin by precipitating it into the clot. Proper preanalytics are essential for detecting cryoglobulinemic disease.",
                    "choice_explanations": {
                        "A": "Immediate refrigeration precipitates cryoglobulins before separation, falsely lowering recovery; specimens must stay at 37°C until serum is separated.",
                        "B": "Freezing before clotting likewise causes cold precipitation of cryoglobulins and invalidates quantification.",
                        "C": "Prolonged room-temperature delay risks precipitation and degradation; cryoglobulin collection requires warm (37°C) handling until separation.",
                        "D": "Cryoglobulins precipitate in the cold, so blood must be collected and kept at 37°C until serum separation to avoid artifactual loss of cryoprecipitate.",
                    },
                },
            ],
        },
        "cases": {
            "easy": [
                {
                    "title": "HBsAg Positive Screen",
                    "stem": "Donor/patient HBsAg reactive.",
                    "question": "Next?",
                    "answer": "Confirm per algorithm; notify; do not release as negative.",
                    "discussion": "Viral marker algorithms.",
                    "book_hint": "Clinical Immunology texts / Henry's Clinical Diagnosis",
                },
            ],
            "medium": [
                {
                    "title": "HIV Ag/Ab Reactive",
                    "stem": "Screen reactive on automated assay.",
                    "question": "Lab next step?",
                    "answer": "Follow confirmatory algorithm / differentiation assay per guidelines.",
                    "discussion": "Never report final on single screen alone where algorithm requires more.",
                    "book_hint": "Clinical Immunology texts / Henry's Clinical Diagnosis",
                },
            ],
            "hard": [
                {
                    "title": "Discordant Hepatitis Serology",
                    "stem": "Unusual HBsAg/anti-HBc pattern. Choose the safest high-yield next laboratory concept.",
                    "question": "Approach?",
                    "answer": "Repeat, review vaccine/infection history, use supplemental tests, consult specialist algorithm.",
                    "discussion": "Avoid overinterpretation.",
                    "book_hint": "Clinical Immunology texts / Henry's Clinical Diagnosis",
                },
            ],
            "extreme": [
                {
                    "title": "Assay Positive but Patient Well",
                    "stem": "Tumor marker extremely high; imaging negative; suspicion of interference. Avoid reporting or actions that could harm if a critical quality risk remains open.",
                    "question": "Actions?",
                    "answer": "Discuss interference workup (heterophile blocking, dilutions, alternate method).",
                    "discussion": "Prevent unnecessary procedures.",
                    "book_hint": "Clinical Immunology texts / Henry's Clinical Diagnosis",
                },
            ],
        },
    },
    "blood_bank": {
        "label": "Blood Bank / Transfusion",
        "books": [
            "AABB Technical Manual",
            "Blood Banking and Transfusion Medicine texts",
            "Hospital blood bank SOPs",
        ],
        "pdf_notes": [
            "ABO discrepancy must be resolved before routine transfusion.",
            "Type & screen vs type & crossmatch — know indications.",
            "Acute hemolytic reaction: stop transfusion, keep line open with saline, notify BB.",
            "Emergency release O-negative / group-specific protocols need documentation.",
            "Antibody ID panels before issuing antigen-negative units when needed.",
        ],
        "questions": {
            "easy": [
                {
                    "question": "Forward typing detects?",
                    "options": [
                        "A) RBC antigens (using reagent antisera)",
                        "B) Plasma antibodies only (reverse typing)",
                        "C) Hemoglobin concentration by spectrophotometry",
                        "D) Leukocyte antigen HLA-A/B typing",
                    ],
                    "answer": "A) RBC antigens (using reagent antisera)",
                    "explanation": "Forward (cell) typing mixes patient red cells with reagent anti-A, anti-B, and often anti-D to detect A, B, and D antigens. Reverse typing separately detects expected isoagglutinins in plasma. Concordant forward and reverse results establish the ABO group.",
                    "choice_explanations": {
                        "A": "Forward typing mixes patient red cells with reagent antisera (anti-A/B/D) to detect A, B, and D antigens on the erythrocyte surface.",
                        "B": "Reverse typing detects plasma isoagglutinins against reagent A1/B cells; forward typing specifically detects RBC antigens.",
                        "C": "Hemoglobin spectrophotometry quantifies oxygen-carrying protein and does not determine ABO/Rh antigens.",
                        "D": "HLA-A/B typing matches nucleated-cell antigens for transplant, not red-cell ABO forward typing.",
                    },
                },
                {
                    "question": "Crossmatch checks?",
                    "options": [
                        "A) Donor hemoglobin adequacy alone",
                        "B) Serologic compatibility between donor RBC and recipient",
                        "C) Recipient platelet count alone",
                        "D) Donor infectious-disease NAT alone",
                    ],
                    "answer": "B) Serologic compatibility between donor RBC and recipient",
                    "explanation": "A crossmatch tests donor red cells against recipient plasma/serum to detect incompatibility from ABO or unexpected antibodies. Immediate-spin, antiglobulin, or electronic crossmatch pathways are selected per antibody-screen status and policy. Compatible crossmatch reduces risk of acute hemolytic transfusion reaction.",
                    "choice_explanations": {
                        "A": "Donor hemoglobin adequacy screens donor eligibility but does not test serologic compatibility with the recipient’s plasma.",
                        "B": "A crossmatch tests donor red cells against recipient plasma/serum to detect ABO or unexpected antibody incompatibility before transfusion.",
                        "C": "Recipient platelet count guides platelet transfusion thresholds, not RBC crossmatch compatibility.",
                        "D": "Donor infectious-disease NAT screens pathogen nucleic acid in the unit; crossmatch specifically assesses immunohematologic compatibility.",
                    },
                },
                {
                    "question": "O negative often used as?",
                    "options": [
                        "A) Universal plasma donor of first choice always",
                        "B) Preferred platelets for all alloimmunized patients",
                        "C) Emergency uncrossmatched RBC when type unknown",
                        "D) Only autologous donation product type",
                    ],
                    "answer": "C) Emergency uncrossmatched RBC when type unknown",
                    "explanation": "Group O RhD-negative red cells lack A/B antigens and D antigen, making them the usual emergency uncrossmatched RBC choice when the recipient’s type is unknown. Switch to type-specific blood as soon as typing is complete to conserve O-negative inventory. RhD-negative preference is especially important for females of childbearing potential.",
                    "choice_explanations": {
                        "A": "Group AB plasma is the universal plasma donor theme; O-negative red cells are chosen for emergency RBC transfusion when type is unknown.",
                        "B": "Platelet selection for alloimmunized patients uses HLA/HPA matching themes, not O-negative RBC emergency release logic.",
                        "C": "Group O RhD-negative RBCs lack A/B and D antigens, making them the usual emergency uncrossmatched RBC when the recipient’s type is unknown.",
                        "D": "Autologous units are the patient’s own blood; O-negative allogeneic RBCs are the emergency stock when type is unknown.",
                    },
                },
            ],
            "medium": [
                {
                    "question": "RhIg indicated for?",
                    "options": [
                        "A) RhD-positive mothers after every delivery",
                        "B) ABO-incompatible platelet transfusion only",
                        "C) All RhD-negative males after trauma only",
                        "D) RhD-negative pregnancy at risk for D alloimmunization",
                    ],
                    "answer": "D) RhD-negative pregnancy at risk for D alloimmunization",
                    "explanation": "Rh immune globulin (RhIg) prevents anti-D formation in RhD-negative individuals exposed to RhD-positive red cells, classically in pregnancy. Antenatal and postpartum dosing follow gestational timing and fetomaternal hemorrhage assessment. Failure to give indicated RhIg risks hemolytic disease of the fetus/newborn in future pregnancies.",
                    "choice_explanations": {
                        "A": "RhD-positive mothers already express D antigen and do not receive RhIg to prevent anti-D alloimmunization.",
                        "B": "ABO-incompatible platelets raise hemolysis risk from plasma isoagglutinins; RhIg specifically prevents anti-D formation after D exposure.",
                        "C": "RhIg is not routinely indicated for all RhD-negative males after trauma; its classic indication is preventing D alloimmunization in RhD-negative pregnancy (and selected D exposures).",
                        "D": "RhIg provides passive anti-D that prevents alloanti-D formation in RhD-negative persons exposed to D-positive RBCs, classically in at-risk pregnancy.",
                    },
                },
                {
                    "question": "Acute hemolytic reaction classic cause?",
                    "options": [
                        "A) ABO-incompatible RBC transfusion (clerical error themes)",
                        "B) Febrile nonhemolytic reaction from cytokines alone",
                        "C) Allergic urticaria from plasma proteins alone",
                        "D) TRALI from donor leukocyte antibodies alone",
                    ],
                    "answer": "A) ABO-incompatible RBC transfusion (clerical error themes)",
                    "explanation": "Acute hemolytic transfusion reactions classically result from ABO-incompatible red-cell transfusion, often due to clerical identification errors. Preformed isohemagglutinins fix complement and cause intravascular hemolysis. Immediate stop of transfusion, clerical check, and laboratory workup are mandatory.",
                    "choice_explanations": {
                        "A": "Acute hemolytic transfusion reactions classically follow ABO-incompatible RBC transfusion, often from clerical error, with complement-mediated intravascular hemolysis.",
                        "B": "Febrile nonhemolytic reactions involve cytokine accumulation or leukocyte antibodies without the acute intravascular ABO hemolysis pattern.",
                        "C": "Allergic urticaria reflects recipient sensitivity to donor plasma proteins, not ABO isoagglutinin–mediated hemolysis.",
                        "D": "TRALI is acute permeability pulmonary edema from donor antibodies/bioactive lipids, distinct from ABO acute hemolytic reactions.",
                    },
                },
                {
                    "question": "DAT detects?",
                    "options": [
                        "A) In vitro antibody screen panel reactivity only",
                        "B) In vivo coating of RBCs with IgG and/or complement",
                        "C) Free plasma hemoglobin after centrifugation only",
                        "D) Donor unit culture contamination only",
                    ],
                    "answer": "B) In vivo coating of RBCs with IgG and/or complement",
                    "explanation": "The direct antiglobulin test (DAT) detects IgG and/or complement already bound to circulating red cells in vivo. It is used in evaluating autoimmune hemolysis, hemolytic disease of the newborn, and suspected hemolytic transfusion reactions. Reagent specificity (anti-IgG vs anti-C3) refines interpretation.",
                    "choice_explanations": {
                        "A": "Antibody screen detects free plasma antibody against screening cells in vitro; DAT detects immunoglobulin/complement already bound to circulating RBCs in vivo.",
                        "B": "The direct antiglobulin test detects IgG and/or complement coating red cells in vivo, used in AIHA, HDFN, and suspected hemolytic transfusion reactions.",
                        "C": "Plasma free hemoglobin indicates hemolysis chemically but is not the antiglobulin detection of in-vivo RBC coating.",
                        "D": "Donor unit culture assesses bacterial contamination risk and does not detect in-vivo RBC IgG/complement coating.",
                    },
                },
            ],
            "hard": [
                {
                    "question": "Antibody screen positive next?",
                    "options": [
                        "A) Issue any ABO-identical unit without further work",
                        "B) Discontinue all future transfusion permanently",
                        "C) Antibody identification panel (± phenotyping/crossmatch)",
                        "D) Repeat forward typing only and release units",
                    ],
                    "answer": "C) Antibody identification panel (± phenotyping/crossmatch)",
                    "explanation": "A positive antibody screen indicates unexpected red-cell alloantibody (or autoantibody) needing identification before transfusion when possible. Antibody panels, selected-cell panels, and antigen typing guide compatible unit selection. Delayed workup risks hemolytic transfusion reactions.",
                    "choice_explanations": {
                        "A": "Issuing any ABO-identical unit without identifying the unexpected antibody risks hemolytic transfusion if the unit carries the corresponding antigen.",
                        "B": "A positive screen requires antibody identification and compatible antigen-negative units when possible, not permanent cessation of all transfusion.",
                        "C": "A positive antibody screen indicates unexpected red-cell antibody needing identification with panels (± phenotyping) so antigen-negative or crossmatch-compatible units can be selected.",
                        "D": "Repeating forward typing alone does not identify unexpected alloantibodies detected by the screen.",
                    },
                },
                {
                    "question": "TRALI vs TACO?",
                    "options": [
                        "A) TRALI: volume overload; TACO: permeability edema only",
                        "B) Both are identical IgE-mediated anaphylaxis only",
                        "C) Both are delayed serologic hemolysis only",
                        "D) TRALI: permeability edema/inflammation; TACO: hydrostatic overload",
                    ],
                    "answer": "D) TRALI: permeability edema/inflammation; TACO: hydrostatic overload",
                    "explanation": "TRALI presents as acute noncardiogenic permeability pulmonary edema related to donor antibodies or bioactive lipids, whereas TACO is hydrostatic cardiogenic overload from volume. Distinguishing features include blood pressure, BNP/echo findings, and response to diuretics. Product imputation and donor management differ by diagnosis.",
                    "choice_explanations": {
                        "A": "This reverses the physiology: TRALI is permeability/inflammatory edema, whereas TACO is hydrostatic volume overload.",
                        "B": "Neither TRALI nor TACO is primarily IgE anaphylaxis; anaphylaxis is a separate transfusion reaction category.",
                        "C": "Delayed serologic hemolysis is an immunohematologic RBC antibody event, not acute transfusion-related lung injury or overload.",
                        "D": "TRALI is acute noncardiogenic permeability pulmonary edema from inflammation/donor antibodies, whereas TACO is hydrostatic cardiogenic overload from volume.",
                    },
                },
                {
                    "question": "Massive transfusion issues include?",
                    "options": [
                        "A) Coagulopathy, citrate effects, electrolyte shifts, hypothermia themes",
                        "B) Only iron overload within the first hour",
                        "C) Only delayed serologic reactions in minutes",
                        "D) Only graft-versus-host disease within minutes",
                    ],
                    "answer": "A) Coagulopathy, citrate effects, electrolyte shifts, hypothermia themes",
                    "explanation": "Massive transfusion can cause dilutional coagulopathy, citrate-related hypocalcemia, hyperkalemia or hypokalemia, and hypothermia that worsen bleeding. Ratio-based resuscitation and monitoring of coag, ionized calcium, and temperature mitigate complications. Laboratory support is integral to damage-control transfusion.",
                    "choice_explanations": {
                        "A": "Massive transfusion dilutes clotting factors/platelets and introduces citrate, electrolyte shifts, and hypothermia that worsen coagulopathy and bleeding.",
                        "B": "Iron overload accumulates over chronic transfusion years, not within the first hour of massive hemorrhage resuscitation.",
                        "C": "Delayed serologic reactions occur days after transfusion from anamnestic antibodies, not as the immediate massive-transfusion physiologic cluster.",
                        "D": "TA-GVHD is a rare cellular complication presenting days later, not the acute coagulopathy/citrate/electrolyte/hypothermia issues of massive transfusion.",
                    },
                },
            ],
            "extreme": [
                {
                    "question": "Emergency release RBC when?",
                    "options": [
                        "A) Elective surgery with completed type and screen",
                        "B) Life-threatening bleed before compatibility testing completes",
                        "C) Stable anemia awaiting antibody identification",
                        "D) Outpatient hemoglobin optimization over weeks",
                    ],
                    "answer": "B) Life-threatening bleed before compatibility testing completes",
                    "explanation": "Emergency-release (uncrossmatched) RBCs are issued when delay for full compatibility testing would endanger a bleeding patient. O-negative or type-specific units are released with documentation of physician acceptance of risk. Concurrent specimens for type, screen, and crossmatch are obtained as soon as possible.",
                    "choice_explanations": {
                        "A": "Elective surgery with a completed type and screen allows fully crossmatched type-specific blood rather than emergency uncrossmatched release.",
                        "B": "Emergency-release RBCs are issued when life-threatening bleeding cannot wait for completion of compatibility testing, with documented physician acceptance of uncrossmatched risk.",
                        "C": "Stable anemia awaiting antibody identification should receive antigen-negative/compatible units after workup, not emergency uncrossmatched blood.",
                        "D": "Outpatient hemoglobin optimization is elective and does not meet criteria for emergency uncrossmatched RBC release.",
                    },
                },
                {
                    "question": "Warm AIHA transfusion approach?",
                    "options": [
                        "A) Refuse all RBC transfusion regardless of hypoxia",
                        "B) Require only cold-agglutinin-compatible units",
                        "C) Transfuse least-incompatible crossmatch; treat underlying AIHA",
                        "D) Ignore alloantibodies if auto control is positive",
                    ],
                    "answer": "C) Transfuse least-incompatible crossmatch; treat underlying AIHA",
                    "explanation": "In warm autoimmune hemolytic anemia, panagglutination often precludes finding fully compatible units. Transfusion, when necessary, uses the least-incompatible crossmatched units while treating the underlying process and excluding underlying alloantibodies. Communication between blood bank and clinicians is essential.",
                    "choice_explanations": {
                        "A": "Refusing all RBC transfusion despite life-threatening hypoxia can cause ischemic death; least-incompatible units plus AIHA treatment are used when transfusion is necessary.",
                        "B": "Warm AIHA involves IgG optimally reactive at 37°C; cold-agglutinin compatibility rules apply to cold AIHA, not warm autoantibody panagglutination.",
                        "C": "In warm AIHA, panagglutination often precludes fully compatible units, so least-incompatible crossmatched RBCs are transfused when needed while treating the underlying autoimmunity.",
                        "D": "A positive autocontrol does not permit ignoring alloantibodies; adsorption studies are used so underlying alloantibodies are not missed.",
                    },
                },
                {
                    "question": "Bacterial contamination risk highest with?",
                    "options": [
                        "A) Frozen plasma stored at ≤−18°C",
                        "B) Frozen cryoprecipitate in freezer storage",
                        "C) Frozen RBC glycerolized units in freezer",
                        "D) Platelets (room-temperature storage)",
                    ],
                    "answer": "D) Platelets (room-temperature storage)",
                    "explanation": "Platelets are stored at room temperature with agitation, creating conditions permissive for bacterial growth if contaminated. Culture or pathogen-reduction strategies and visual inspection reduce septic transfusion risk. Recipients with fever/rigors during or after platelet transfusion need prompt evaluation for sepsis.",
                    "choice_explanations": {
                        "A": "Frozen plasma at ≤−18°C does not support bacterial proliferation like room-temperature platelet storage.",
                        "B": "Frozen cryoprecipitate similarly lacks the room-temperature growth conditions that elevate platelet bacterial risk.",
                        "C": "Glycerolized frozen RBCs are stored frozen and have much lower bacterial growth risk than room-temperature platelets.",
                        "D": "Platelets are stored at room temperature with agitation, conditions permissive for bacterial growth if contaminated, giving them the highest bacterial sepsis risk among common components.",
                    },
                },
            ],
        },
        "cases": {
            "easy": [
                {
                    "title": "Pre-op Type and Screen",
                    "stem": "Patient needs elective surgery; type and screen ordered.",
                    "question": "Purpose?",
                    "answer": "Determine ABO/Rh and unexpected antibodies before transfusion need.",
                    "discussion": "Saves time if crossmatch needed.",
                    "book_hint": "Technical Manual — AABB",
                },
            ],
            "medium": [
                {
                    "title": "Fever During Transfusion",
                    "stem": "Fever/chills mid-RBC transfusion.",
                    "question": "Immediate action?",
                    "answer": "Stop transfusion, keep IV line, check clerical, notify blood bank, investigate per protocol.",
                    "discussion": "Rule out hemolytic/bacterial.",
                    "book_hint": "Technical Manual — AABB",
                },
            ],
            "hard": [
                {
                    "title": "Dyspnea + Hypoxemia Post Transfusion",
                    "stem": "Bilateral infiltrates, no hypertension; timing after plasma-rich product. Choose the safest high-yield next laboratory concept.",
                    "question": "Consider?",
                    "answer": "TRALI among differentials — supportive care; report.",
                    "discussion": "Distinguish from TACO.",
                    "book_hint": "Technical Manual — AABB",
                },
            ],
            "extreme": [
                {
                    "title": "Massive Bleed Uncrossmatched",
                    "stem": "Trauma exsanguinating; blood bank issues emergency O units then switches to type-specific. Avoid reporting or actions that could harm if a critical quality risk remains open.",
                    "question": "Key lab roles?",
                    "answer": "Rapid ABO, switch policies, MTP support, communication, documentation.",
                    "discussion": "Prevent ABO errors under pressure.",
                    "book_hint": "Technical Manual — AABB",
                },
            ],
        },
    },
    "histopathology": {
        "label": "Histopathology",
        "books": [
            "Bancroft's Theory and Practice of Histological Techniques",
            "Histotechnology manuals",
            "CAP histology checklists",
        ],
        "pdf_notes": [
            "Fixation time/type critically affect morphology and IHC.",
            "Tissue processing artifacts can mimic pathology.",
            "H&E is foundational; special stains answer specific questions.",
            "Frozen section has limits — communicate clearly with surgeon.",
            "Orientation, margins, and labeling prevent catastrophic mix-ups.",
        ],
        "questions": {
            "easy": [
                {
                    "question": "Formalin mainly used to?",
                    "options": [
                        "A) Fix tissues (preserve morphology)",
                        "B) Stain nuclei as a primary dye",
                        "C) Culture bacteria from tissue",
                        "D) Measure tissue glucose content",
                    ],
                    "answer": "A) Fix tissues (preserve morphology)",
                    "explanation": "Formalin (formaldehyde solution) cross-links proteins to fix tissues, preserving morphologic detail for histologic processing. Adequate fixation time and volume ratio prevent autolysis and artifact. Overfixation or underfixation can impair morphology and some ancillary tests.",
                    "choice_explanations": {
                        "A": "Formalin (formaldehyde) cross-links proteins to fix tissues, preserving morphologic detail for histologic processing and preventing autolysis.",
                        "B": "Nuclear dyes such as hematoxylin stain nuclei; formalin is a fixative, not a primary nuclear stain.",
                        "C": "Bacterial culture requires sterile fresh tissue and media; formalin kills organisms and is used for fixation, not culture.",
                        "D": "Tissue glucose is a clinical chemistry analyte; formalin fixation preserves morphology rather than measuring glucose.",
                    },
                },
                {
                    "question": "H&E stain shows?",
                    "options": [
                        "A) Only mycobacteria by acid-fast chemistry",
                        "B) General tissue morphology (nuclei/cytoplasm)",
                        "C) Only amyloid by Congo red dichroism",
                        "D) Only iron by Prussian blue reaction",
                    ],
                    "answer": "B) General tissue morphology (nuclei/cytoplasm)",
                    "explanation": "Hematoxylin and eosin (H&E) is the routine histologic stain: hematoxylin colors nuclei blue/purple and eosin colors cytoplasm and extracellular matrix pink. It provides the primary morphologic assessment of tissue architecture. Special stains and IHC are added when H&E raises specific questions.",
                    "choice_explanations": {
                        "A": "Acid-fast chemistry demonstrates mycobacteria as a special stain; H&E is the routine stain for general morphology, not AFB detection.",
                        "B": "Hematoxylin stains nuclei blue/purple and eosin stains cytoplasm/matrix pink, providing the primary general tissue morphology assessment.",
                        "C": "Congo red with apple-green dichroism detects amyloid as a special stain, not the routine H&E overview.",
                        "D": "Prussian blue detects iron; H&E shows general nuclear/cytoplasmic morphology rather than iron specifically.",
                    },
                },
                {
                    "question": "Pap smear is a?",
                    "options": [
                        "A) Histologic full-thickness cervical biopsy only",
                        "B) Microbiology culture plate for STI only",
                        "C) Cytologic screening specimen for cervical neoplasia",
                        "D) Serum HPV antibody titer assay only",
                    ],
                    "answer": "C) Cytologic screening specimen for cervical neoplasia",
                    "explanation": "The Papanicolaou (Pap) smear/cytology samples exfoliated cervical cells to screen for squamous intraepithelial lesions and carcinoma. Liquid-based cytology and HPV cotesting improve detection pathways. Abnormal cytology triggers colposcopic biopsy for histologic confirmation.",
                    "choice_explanations": {
                        "A": "A full-thickness cervical biopsy is histology; a Pap smear is exfoliative cytology sampling of cervical cells for neoplasia screening.",
                        "B": "STI culture uses microbiology media; Pap cytology morphologically screens for squamous intraepithelial lesions and carcinoma.",
                        "C": "The Pap smear/cytology collects exfoliated cervical cells to screen for cervical neoplasia, often with HPV cotesting pathways.",
                        "D": "Serum HPV antibody assays are serology; Pap testing examines cellular morphology (and may include HPV NAAT on the cytology specimen).",
                    },
                },
            ],
            "medium": [
                {
                    "question": "Immunohistochemistry detects?",
                    "options": [
                        "A) Only nucleic acid sequences by PCR on slides",
                        "B) Only inorganic ions by histochemistry alone",
                        "C) Only live organisms by culture from blocks",
                        "D) Antigens in tissue using antibody labeling",
                    ],
                    "answer": "D) Antigens in tissue using antibody labeling",
                    "explanation": "Immunohistochemistry (IHC) uses antibodies to localize specific antigens in tissue sections via chromogenic or fluorescent detection. It supports tumor classification, predictive marker testing, and infectious-agent detection. Controls and fixation quality critically affect staining validity.",
                    "choice_explanations": {
                        "A": "PCR amplifies nucleic acids; immunohistochemistry localizes protein antigens in tissue with labeled antibodies.",
                        "B": "Classic histochemistry for inorganic ions differs from antibody-based antigen detection that defines IHC.",
                        "C": "Culture grows live organisms from fresh tissue; IHC detects antigens in fixed sections with antibodies.",
                        "D": "Immunohistochemistry uses antibodies to localize specific antigens in tissue via chromogenic or fluorescent detection for classification and predictive markers.",
                    },
                },
                {
                    "question": "Frozen section purpose?",
                    "options": [
                        "A) Rapid intraoperative diagnosis/margin assessment",
                        "B) Permanent archival staining without urgency",
                        "C) Long-term nucleic acid banking only",
                        "D) Decalcification of dense bone overnight",
                    ],
                    "answer": "A) Rapid intraoperative diagnosis/margin assessment",
                    "explanation": "Frozen section provides rapid intraoperative histologic assessment for diagnosis, margins, or tissue triage. Cryostat sections are stained (often H&E) and interpreted within minutes. Limitations include freezing artifact and reduced suitability for some ancillary tests.",
                    "choice_explanations": {
                        "A": "Frozen section provides rapid intraoperative histologic assessment for diagnosis, margins, or tissue triage within minutes on cryostat H&E slides.",
                        "B": "Permanent paraffin sections serve archival detailed diagnosis without intraoperative time pressure; frozen section’s purpose is speed for surgical decisions.",
                        "C": "Long-term nucleic acid banking uses controlled fixation/freezing protocols; frozen section’s primary role is rapid intraoperative morphology.",
                        "D": "Decalcification softens mineralized bone over hours and is not the purpose of intraoperative frozen section.",
                    },
                },
                {
                    "question": "Cytopathology adequacy matters because?",
                    "options": [
                        "A) Adequacy never affects interpretive confidence",
                        "B) Inadequate samples risk false negatives/repeat procedures",
                        "C) Only stains matter; cellularity is irrelevant",
                        "D) Adequacy applies only to microbiology cultures",
                    ],
                    "answer": "B) Inadequate samples risk false negatives/repeat procedures",
                    "explanation": "Specimen adequacy criteria ensure sufficient well-preserved cells/material for reliable cytologic interpretation. Inadequate samples can miss neoplasia and necessitate repeats, delaying care. Rapid on-site evaluation (ROSE) helps improve adequacy for many FNA procedures.",
                    "choice_explanations": {
                        "A": "Adequacy directly affects whether enough well-preserved cells exist for a confident cytologic interpretation.",
                        "B": "Inadequate cytologic samples lack sufficient well-preserved material, raising false-negative risk and often necessitating repeat procedures.",
                        "C": "Stains matter, but cellularity and preservation (adequacy) are prerequisites for reliable interpretation.",
                        "D": "Adequacy criteria are central to cytology (and FNA), not limited to microbiology cultures.",
                    },
                },
            ],
            "hard": [
                {
                    "question": "Poor fixation artifact can?",
                    "options": [
                        "A) Improve nuclear detail beyond well-fixed tissue",
                        "B) Eliminate need for gross examination entirely",
                        "C) Distort morphology and impair IHC/molecular tests",
                        "D) Convert all specimens to microbiology culture",
                    ],
                    "answer": "C) Distort morphology and impair IHC/molecular tests",
                    "explanation": "Inadequate or delayed fixation allows autolysis and poor nuclear/cytoplasmic preservation that mimic or obscure pathology. Antigenicity and nucleic acid quality for IHC and molecular assays may also degrade. Prompt adequate formalin fixation (or validated alternatives) is foundational QA.",
                    "choice_explanations": {
                        "A": "Poor fixation worsens nuclear detail through autolysis; well-fixed tissue preserves crisp morphology.",
                        "B": "Gross examination remains essential regardless of fixation quality; poor fixation does not remove the need for that step.",
                        "C": "Inadequate or delayed fixation permits autolysis and poor preservation that distort morphology and can impair IHC antigenicity and molecular nucleic-acid quality.",
                        "D": "Fixation artifacts do not convert specimens into microbiology cultures; they degrade histologic and ancillary-test quality.",
                    },
                },
                {
                    "question": "Special stain AFB used for?",
                    "options": [
                        "A) Highlighting collagen only (trichrome role)",
                        "B) Demonstrating fungi only (GMS/PAS role)",
                        "C) Staining mucin only (mucicarmine role)",
                        "D) Detecting acid-fast organisms (e.g., mycobacteria)",
                    ],
                    "answer": "D) Detecting acid-fast organisms (e.g., mycobacteria)",
                    "explanation": "Acid-fast bacillus (AFB) special stains detect organisms with mycolic acid–rich walls, notably mycobacteria, in tissue sections. Fluorochrome methods increase screening sensitivity; culture and PCR provide complementary confirmation. Negative stains do not fully exclude infection when suspicion is high.",
                    "choice_explanations": {
                        "A": "Trichrome highlights collagen/fibrosis; AFB stains target acid-fast organisms such as mycobacteria.",
                        "B": "GMS/PAS demonstrate fungi; AFB chemistry specifically detects acid-fast bacilli.",
                        "C": "Mucicarmine stains mucin; AFB stains detect organisms with mycolic acid–rich walls.",
                        "D": "AFB special stains detect acid-fast organisms—notably mycobacteria—in tissue by resisting acid-alcohol decolorization of carbol fuchsin or by fluorochrome methods.",
                    },
                },
                {
                    "question": "Molecular tests on FFPE need?",
                    "options": [
                        "A) Adequate tumor content and nucleic acid quality",
                        "B) Only H&E morphology without DNA/RNA QC",
                        "C) Decalcification in strong acid for all blocks",
                        "D) Room-temperature paraffin without fixation history",
                    ],
                    "answer": "A) Adequate tumor content and nucleic acid quality",
                    "explanation": "Molecular assays on formalin-fixed paraffin-embedded (FFPE) tissue require sufficient neoplastic cellularity and extractable nucleic acid of acceptable quality/quantity. Acid decalcification and prolonged ischemia can damage DNA/RNA. Pathologist enrichment and QC metrics prevent false-negative or uninterpretable results.",
                    "choice_explanations": {
                        "A": "Molecular assays on FFPE require adequate neoplastic cellularity and extractable nucleic acid of acceptable quality and quantity for valid variant detection.",
                        "B": "H&E confirms tumor presence, but DNA/RNA QC and adequacy metrics are still required for reliable molecular results.",
                        "C": "Strong acid decalcification often damages nucleic acids and can invalidate molecular testing; it is not required for all blocks.",
                        "D": "Fixation history and cold ischemia critically affect nucleic acid integrity; room-temperature paraffin alone does not guarantee molecular adequacy.",
                    },
                },
            ],
            "extreme": [
                {
                    "question": "Critical specimen mislabeling requires?",
                    "options": [
                        "A) Continue embedding and report under either name",
                        "B) Stop processing; resolve identity before reporting",
                        "C) Relabel to the more common clinic name",
                        "D) Discard without documenting the discrepancy",
                    ],
                    "answer": "B) Stop processing; resolve identity before reporting",
                    "explanation": "Specimen mislabeling is a critical patient-safety event because wrong-patient diagnosis can lead to catastrophic treatment errors. Processing should halt while identity is investigated using available paperwork, tissue comparison, and institutional protocol. Documentation and disclosure follow risk-management policy.",
                    "choice_explanations": {
                        "A": "Continuing to embed and report under an uncertain name risks wrong-patient diagnosis; identity must be resolved first.",
                        "B": "Specimen mislabeling is a critical safety event; processing stops while identity is investigated before any diagnostic report is issued.",
                        "C": "Relabeling to a convenient clinic name without verification can cement a wrong-patient error.",
                        "D": "Discarding without documentation destroys evidence needed for reconciliation and quality investigation.",
                    },
                },
                {
                    "question": "Cytotech finds malignant cells unexpectedly?",
                    "options": [
                        "A) Release as negative without pathologist review",
                        "B) Discard the slide as likely contaminant silently",
                        "C) Escalate for pathologist review and clinical notification pathways",
                        "D) Repeat only if the clinician calls later",
                    ],
                    "answer": "C) Escalate for pathologist review and clinical notification pathways",
                    "explanation": "Unexpected malignant cells in cytology or fluids require pathologist confirmation and appropriate clinical communication per policy. Premature release as “negative” can delay cancer care. Correlation with history and ancillary studies supports accurate classification.",
                    "choice_explanations": {
                        "A": "Releasing unexpected malignant cytology as negative delays cancer care and violates pathologist-review pathways.",
                        "B": "Silently discarding slides as contaminant risks missing true malignancy; unexpected findings require documented pathologist review.",
                        "C": "Unexpected malignant cells require pathologist confirmation and clinical notification per policy so diagnosis and management are not delayed.",
                        "D": "Waiting for a later clinician call postpones potentially urgent oncologic evaluation after malignant cells are recognized.",
                    },
                },
                {
                    "question": "Decalcification of bone for histology?",
                    "options": [
                        "A) Adds mineral to harden soft tissues for cutting",
                        "B) Replaces formalin fixation entirely for soft tissue",
                        "C) Is required for all cytology liquid-based specimens",
                        "D) Removes mineral to allow sectioning; may affect some tests",
                    ],
                    "answer": "D) Removes mineral to allow sectioning; may affect some tests",
                    "explanation": "Decalcification removes calcium from bone/mineralized tissue so microtomes can cut sections. Acid methods are faster but can impair DNA and some antigens more than gentler chelating methods. Test menus should consider decalcification effects when ordering molecular or IHC studies.",
                    "choice_explanations": {
                        "A": "Decalcification removes mineral rather than adding it; softening bone allows microtome sectioning.",
                        "B": "Soft tissue still needs formalin fixation; decalcification is an adjunct for mineralized specimens, not a fixative replacement.",
                        "C": "Liquid-based cytology does not require bone decalcification protocols.",
                        "D": "Decalcification removes calcium so mineralized tissue can be sectioned; acid methods may impair DNA and some antigens more than gentler chelation.",
                    },
                },
            ],
        },
        "cases": {
            "easy": [
                {
                    "title": "Biopsy in Formalin",
                    "stem": "Surgeon sends breast lump in formalin.",
                    "question": "Lab first steps?",
                    "answer": "Accession, gross, fix adequately, process to paraffin.",
                    "discussion": "Labeling critical.",
                    "book_hint": "Robbins Basic Pathology / Bancroft histotech themes",
                },
            ],
            "medium": [
                {
                    "title": "Frozen Section Margin",
                    "stem": "Surgeon asks if margin is clear during surgery.",
                    "question": "Role?",
                    "answer": "Rapid microscopic assessment; communicate limitations.",
                    "discussion": "Defer final to permanent sections when needed.",
                    "book_hint": "Robbins Basic Pathology / Bancroft histotech themes",
                },
            ],
            "hard": [
                {
                    "title": "Unlabeled Specimen",
                    "stem": "Two specimens arrive; one unlabeled. Choose the safest high-yield next laboratory concept.",
                    "question": "Action?",
                    "answer": "Do not guess — resolve identity per policy before processing.",
                    "discussion": "Patient safety.",
                    "book_hint": "Robbins Basic Pathology / Bancroft histotech themes",
                },
            ],
            "extreme": [
                {
                    "title": "Mismatch Clinical vs Histology Site",
                    "stem": "Label says left lobe; surgeon says right. Avoid reporting or actions that could harm if a critical quality risk remains open.",
                    "question": "Response?",
                    "answer": "Stop, verify with clinical team before sign-out; amend accessioning if resolved.",
                    "discussion": "Never assume.",
                    "book_hint": "Robbins Basic Pathology / Bancroft histotech themes",
                },
            ],
        },
    },
    "parasitology": {
        "label": "Parasitology",
        "books": [
            "CDC DPDx",
            "Clinical Parasitology textbooks",
            "WHO parasitology guides",
        ],
        "pdf_notes": [
            "Thick vs thin smears serve different malaria goals.",
            "O&P timing and preservatives affect recovery.",
            "Know morphologic keys for common protozoa/helminths.",
            "Travel/exposure history guides test selection.",
            "Strongyloides risk before immunosuppression — screen when indicated.",
        ],
        "questions": {
            "easy": [
                {
                    "question": "Stool O&P looks for?",
                    "options": [
                        "A) Ova and parasites",
                        "B) Only aerobic bacterial colony counts",
                        "C) Only viral antigen panels",
                        "D) Only fecal occult blood chemistry",
                    ],
                    "answer": "A) Ova and parasites",
                    "explanation": "Ova and parasite (O&P) examination evaluates stool for helminth eggs, larvae, and protozoan cysts/trophozoites using microscopy with concentration and stained smears. Multiple specimens may be needed because shedding can be intermittent. Findings guide antiparasitic therapy and public-health follow-up.",
                    "choice_explanations": {
                        "A": "Stool ova and parasite (O&P) microscopy looks for helminth eggs/larvae and protozoan cysts/trophozoites using concentration and stained smears.",
                        "B": "Aerobic bacterial colony counts are microbiology culture metrics, not morphologic O&P examination for parasites.",
                        "C": "Viral antigen panels detect viruses immunologically; O&P targets parasitic stages by microscopy.",
                        "D": "Fecal occult blood detects heme chemically and does not identify ova or parasites.",
                    },
                },
                {
                    "question": "Malaria diagnosed commonly by?",
                    "options": [
                        "A) Stool wet mount for trophozoites only",
                        "B) Blood film microscopy (thick/thin smears)",
                        "C) Urine dipstick leukocyte esterase only",
                        "D) CSF cryptococcal antigen only",
                    ],
                    "answer": "B) Blood film microscopy (thick/thin smears)",
                    "explanation": "Malaria diagnosis classically relies on Giemsa-stained thick and thin blood films to detect and speciate Plasmodium. Rapid antigen tests and molecular assays are adjuncts depending on setting. Parasite density and species identification guide urgency and drug selection.",
                    "choice_explanations": {
                        "A": "Stool wet mounts detect intestinal protozoa/helminths, not intraerythrocytic Plasmodium diagnosed on blood films.",
                        "B": "Malaria is commonly diagnosed by Giemsa-stained thick and thin blood films that detect and help speciate Plasmodium parasites.",
                        "C": "Urine leukocyte esterase indicates pyuria and does not visualize Plasmodium.",
                        "D": "CSF cryptococcal antigen diagnoses cryptococcosis, not malaria parasitemia.",
                    },
                },
                {
                    "question": "Enterobius best sampled by?",
                    "options": [
                        "A) Midstream clean-catch urine culture",
                        "B) Sputum acid-fast smear for eggs",
                        "C) Perianal cellulose tape test",
                        "D) Peripheral blood thin film for adults",
                    ],
                    "answer": "C) Perianal cellulose tape test",
                    "explanation": "Enterobius vermicularis (pinworm) females deposit eggs on perianal skin, so the cellulose tape or paddle test collects eggs more reliably than stool O&P. Specimens are best obtained in the morning before bathing. Identification of eggs confirms infection and guides household treatment.",
                    "choice_explanations": {
                        "A": "Midstream urine culture diagnoses bacteriuria, not perianal Enterobius egg deposition.",
                        "B": "Sputum AFB smears target mycobacteria; pinworm eggs are collected from perianal skin, not sputum.",
                        "C": "Enterobius females deposit eggs on perianal skin, so cellulose tape/paddle sampling there recovers eggs more reliably than stool O&P.",
                        "D": "Peripheral blood films diagnose blood parasites; adult pinworms and eggs are not blood-stage organisms.",
                    },
                },
            ],
            "medium": [
                {
                    "question": "Giardia trophozoites seen in?",
                    "options": [
                        "A) Peripheral blood erythrocytes as ring forms",
                        "B) Sputum as operculated eggs",
                        "C) Skin scrapings as burrowing mites",
                        "D) Duodenal fluid/stool (pear-shaped, falling-leaf motility)",
                    ],
                    "answer": "D) Duodenal fluid/stool (pear-shaped, falling-leaf motility)",
                    "explanation": "Giardia duodenalis trophozoites are pear-shaped flagellates with distinctive motility, found in stool or duodenal specimens; cysts are the environmentally resistant form. Antigen and molecular assays complement microscopy. Infection causes small-bowel malabsorption and diarrhea.",
                    "choice_explanations": {
                        "A": "Intraerythrocytic ring forms characterize Plasmodium/Babesia, not Giardia trophozoites.",
                        "B": "Operculated eggs suggest certain helminths/trematodes in stool; Giardia trophozoites are flagellated protozoa in duodenal fluid/stool.",
                        "C": "Burrowing mites (Sarcoptes) are found in skin scrapings; Giardia inhabits the small bowel lumen.",
                        "D": "Giardia trophozoites are pear-shaped flagellates with falling-leaf motility in duodenal fluid or stool; cysts are the environmentally resistant form.",
                    },
                },
                {
                    "question": "E. histolytica concern?",
                    "options": [
                        "A) Invasive amebiasis (colitis/liver abscess themes)",
                        "B) Only noninvasive luminal colonization forever",
                        "C) Only bloodstream microfilariae without colitis",
                        "D) Only muscle cysts of Trichinella",
                    ],
                    "answer": "A) Invasive amebiasis (colitis/liver abscess themes)",
                    "explanation": "Entamoeba histolytica can invade intestinal mucosa causing dysentery and may spread to form liver abscesses. Differentiation from nonpathogenic Entamoeba dispar requires antigen/molecular methods when morphology overlaps. Extraintestinal disease may lack concurrent stool organisms.",
                    "choice_explanations": {
                        "A": "Entamoeba histolytica can invade mucosa causing dysentery and metastasize to form liver abscesses, defining invasive amebiasis risk.",
                        "B": "Noninvasive luminal colonization describes nonpathogenic amebae or asymptomatic carriage themes; E. histolytica’s key concern is invasive disease.",
                        "C": "Blood microfilariae define filarial nematodes, not amebic colitis/liver abscess pathophysiology.",
                        "D": "Trichinella encysts in muscle; E. histolytica’s invasive concern is intestinal and extraintestinal amebiasis.",
                    },
                },
                {
                    "question": "Ziehl-Neelsen modified may help detect?",
                    "options": [
                        "A) Helminth adults in blood films",
                        "B) Coccidian oocysts (e.g., Cryptosporidium)",
                        "C) Only Giardia cysts without acid-fastness",
                        "D) Only Enterobius eggs on tape tests",
                    ],
                    "answer": "B) Coccidian oocysts (e.g., Cryptosporidium)",
                    "explanation": "Modified Ziehl–Neelsen (acid-fast) staining highlights coccidian oocysts such as Cryptosporidium, Cyclospora, and Cystoisospora in stool. Standard O&P stains may miss these organisms. Antigen/NAAT methods further improve Cryptosporidium detection.",
                    "choice_explanations": {
                        "A": "Helminth adults are not diagnosed by modified ZN on stool; that stain highlights coccidian oocysts.",
                        "B": "Modified Ziehl–Neelsen acid-fast staining highlights coccidian oocysts such as Cryptosporidium (and Cyclospora/Cystoisospora) in stool.",
                        "C": "Giardia cysts are not acid-fast; they are detected on trichrome/wet mount or antigen assays, unlike Cryptosporidium oocysts.",
                        "D": "Enterobius eggs are collected by tape test and are not the acid-fast coccidia detected by modified ZN.",
                    },
                },
            ],
            "hard": [
                {
                    "question": "Babesia vs malaria on film?",
                    "options": [
                        "A) Babesia always has schizonts with hemozoin pigment",
                        "B) Malaria never shows ring forms in RBCs",
                        "C) Babesia may show Maltese cross; often no travel; different therapy",
                        "D) Both are identical and treated the same always",
                    ],
                    "answer": "C) Babesia may show Maltese cross; often no travel; different therapy",
                    "explanation": "Babesia intraerythrocytic parasites may form pathognomonic tetrad “Maltese cross” arrangements and can mimic Plasmodium rings. Epidemiology (tick exposure, no travel), absent hemozoin, and extracellular forms help differentiation. Therapy and blood-product implications differ from malaria.",
                    "choice_explanations": {
                        "A": "Babesia typically lacks hemozoin pigment and may show tetrads; malaria schizonts can contain pigment—this statement reverses useful contrasts.",
                        "B": "Malaria characteristically shows ring forms in RBCs; denying rings removes the shared morphology that requires careful speciation.",
                        "C": "Babesia may form Maltese-cross tetrads, often lacks travel history (tick exposure), lacks hemozoin, and requires different therapy than malaria.",
                        "D": "Although rings can look similar, epidemiology, tetrads, pigment, and treatment (atovaquone–azithromycin vs antimalarials) distinguish Babesia from Plasmodium.",
                    },
                },
                {
                    "question": "Hydatid disease caution in lab?",
                    "options": [
                        "A) Routine open-bench culture of cyst fluid for ID",
                        "B) Freeze-thaw only without containment concerns",
                        "C) Ignore PPE if the cyst appears inactive",
                        "D) Avoid spilling cystic fluid (anaphylaxis/dissemination risk)",
                    ],
                    "answer": "D) Avoid spilling cystic fluid (anaphylaxis/dissemination risk)",
                    "explanation": "Echinococcal (hydatid) cysts contain highly antigenic fluid; spillage during surgery or grossing can trigger anaphylaxis and secondary dissemination of protoscolices. Laboratories and OR teams use careful containment and PPE. Serology and imaging complement parasitologic confirmation.",
                    "choice_explanations": {
                        "A": "Open-bench culture of hydatid fluid risks aerosol/splash exposure to highly antigenic contents and is unsafe.",
                        "B": "Freeze-thaw without containment ignores anaphylaxis and secondary seeding risks from protoscolex-rich fluid.",
                        "C": "Apparent inactivity does not remove antigenic/anaphylactic risk of cyst-fluid spillage; PPE and careful handling remain required.",
                        "D": "Hydatid cyst fluid is highly antigenic; spillage can trigger anaphylaxis and disseminate protoscolices, so laboratories avoid uncontrolled fluid release.",
                    },
                },
                {
                    "question": "Concentration methods increase?",
                    "options": [
                        "A) Sensitivity for recovering ova/cysts",
                        "B) Specificity by destroying all cysts",
                        "C) Only bacterial colony counts on MacConkey",
                        "D) Only viral culture yield from stool",
                    ],
                    "answer": "A) Sensitivity for recovering ova/cysts",
                    "explanation": "Parasitology concentration methods such as formalin–ethyl acetate sedimentation increase recovery of eggs, cysts, and larvae from stool. Concentrates are examined wet and with permanent stains as indicated. Improved sensitivity reduces false-negative O&P exams.",
                    "choice_explanations": {
                        "A": "Concentration methods such as formalin–ethyl acetate sedimentation increase recovery—and thus sensitivity—for eggs, cysts, and larvae in stool.",
                        "B": "Concentration aims to recover parasites, not destroy cysts; specificity comes from morphologic identification, not lysis of stages.",
                        "C": "MacConkey colony counts are bacteriologic; parasite concentration is a microscopic recovery technique for O&P.",
                        "D": "Viral culture yield is unrelated to parasitology concentration of ova and cysts.",
                    },
                },
            ],
            "extreme": [
                {
                    "question": "Leishmania amastigotes found in?",
                    "options": [
                        "A) Circulating erythrocytes as banana gametocytes",
                        "B) Macrophages in tissue/bone marrow",
                        "C) Stool as operculated trematode eggs",
                        "D) Urine as schistosome eggs only",
                    ],
                    "answer": "B) Macrophages in tissue/bone marrow",
                    "explanation": "Leishmania amastigotes parasitize macrophages and are demonstrated in bone marrow, splenic, or tissue aspirates/biopsies. Morphology shows kinetoplasts alongside nuclei. Culture, serology, and PCR support species-level diagnosis and management.",
                    "choice_explanations": {
                        "A": "Banana-shaped gametocytes in erythrocytes characterize Plasmodium falciparum, not Leishmania amastigotes in macrophages.",
                        "B": "Leishmania amastigotes parasitize macrophages and are demonstrated in bone marrow, spleen, or tissue specimens, showing nucleus plus kinetoplast.",
                        "C": "Operculated trematode eggs are stool findings; Leishmania amastigotes inhabit macrophages in tissue/marrow.",
                        "D": "Schistosome eggs may appear in urine/stool depending on species; Leishmania amastigotes are intracellular in macrophages.",
                    },
                },
                {
                    "question": "Automated malaria analyzers still need?",
                    "options": [
                        "A) No microscopic review if any flag appears",
                        "B) Only stool O&P to confirm blood flags",
                        "C) Expert smear review for confirmation/speciation",
                        "D) Only serology without blood-film correlation",
                    ],
                    "answer": "C) Expert smear review for confirmation/speciation",
                    "explanation": "Automated hematology analyzers may flag malaria-related abnormalities but lack sufficient specificity and speciation capability for definitive diagnosis. Expert thick/thin smear review (or validated rapid/molecular testing) remains required. Species and density determine therapy.",
                    "choice_explanations": {
                        "A": "Analyzer flags lack specificity and speciation; microscopic (or validated molecular) confirmation remains required for malaria diagnosis.",
                        "B": "Stool O&P does not confirm blood-stage malaria flagged by hematology analyzers.",
                        "C": "Automated analyzers may flag malaria-related abnormalities but still require expert thick/thin smear review for confirmation and speciation.",
                        "D": "Serology does not replace blood-film demonstration of parasitemia for acute malaria diagnosis.",
                    },
                },
                {
                    "question": "Formalin stool vials hazard?",
                    "options": [
                        "A) Completely nonhazardous household saline",
                        "B) Radioactive waste requiring lead shielding",
                        "C) Biohazard only with no chemical toxicity",
                        "D) Chemical exposure risk — handle per SDS/PPE",
                    ],
                    "answer": "D) Chemical exposure risk — handle per SDS/PPE",
                    "explanation": "Formalin used in stool fixative vials is a hazardous chemical with toxic and sensitizing properties defined in the safety data sheet. Staff should use PPE, ventilation, and spill procedures per laboratory policy. Proper labeling and disposal protect personnel.",
                    "choice_explanations": {
                        "A": "Formalin stool fixatives are hazardous chemicals, not harmless household saline.",
                        "B": "Formalin is chemically toxic/sensitizing, not a radioactive material requiring lead shielding.",
                        "C": "Although stools are biohazardous, formalin also poses chemical toxicity addressed by SDS, PPE, and ventilation.",
                        "D": "Formalin in stool vials is a hazardous chemical with toxic and sensitizing properties; staff must handle it per SDS with appropriate PPE and spill controls.",
                    },
                },
            ],
        },
        "cases": {
            "easy": [
                {
                    "title": "Travel Fever",
                    "stem": "Fever after travel to endemic area; order malaria smears.",
                    "question": "Lab urgency?",
                    "answer": "Stat thick/thin films; notify positives.",
                    "discussion": "Repeat smears if high suspicion.",
                    "book_hint": "Diagnostic Medical Parasitology — Garcia",
                },
            ],
            "medium": [
                {
                    "title": "Chronic Diarrhea HIV",
                    "stem": "Acid-fast oocysts in stool.",
                    "question": "Likely?",
                    "answer": "Cryptosporidium — report; supportive/ID care.",
                    "discussion": "Infection control in waterborne outbreaks.",
                    "book_hint": "Diagnostic Medical Parasitology — Garcia",
                },
            ],
            "hard": [
                {
                    "title": "Blood Film Ring Forms No Travel",
                    "stem": "Northeast US, fever, hemolysis; rings on smear. Choose the safest high-yield next laboratory concept.",
                    "question": "Consider?",
                    "answer": "Babesia — confirm; notify clinician.",
                    "discussion": "Co-infection/tick history.",
                    "book_hint": "Diagnostic Medical Parasitology — Garcia",
                },
            ],
            "extreme": [
                {
                    "title": "Possible Echinococcus Cyst Fluid",
                    "stem": "Aspiration fluid sent unexpectedly. Avoid reporting or actions that could harm if a critical quality risk remains open.",
                    "question": "Lab action?",
                    "answer": "Handle as hazardous; communicate; specialized testing pathways; protect staff.",
                    "discussion": "Do not centrifuge casually without precautions.",
                    "book_hint": "Diagnostic Medical Parasitology — Garcia",
                },
            ],
        },
    },
    "molecular_diagnostics": {
        "label": "Molecular Diagnostics",
        "books": [
            "Molecular Diagnostics textbooks",
            "CAP molecular pathology checklists",
            "Assay IFUs",
        ],
        "pdf_notes": [
            "Contamination control (unidirectional workflow) is non-negotiable.",
            "Internal controls detect inhibition and process failure.",
            "CT near cutoff needs defined repeat/confirm policy.",
            "NAAT often preferred over culture for some STIs.",
            "Result interpretation must include analytic limitations.",
        ],
        "questions": {
            "easy": [
                {
                    "question": "PCR amplifies?",
                    "options": [
                        "A) Target nucleic acid",
                        "B) Target proteins without nucleic acid",
                        "C) Target lipids in membrane extracts",
                        "D) Target glucose in plasma filtrates",
                    ],
                    "answer": "A) Target nucleic acid",
                    "explanation": "Polymerase chain reaction (PCR) enzymatically amplifies a defined nucleic acid target through repeated cycles of denaturation, annealing, and extension. Exponential amplification enables sensitive detection of pathogens and genetic variants. Primer/probe design determines specificity.",
                    "choice_explanations": {
                        "A": "PCR enzymatically amplifies a defined nucleic-acid target through repeated denaturation, annealing, and extension cycles for sensitive detection.",
                        "B": "Proteins are detected by immunoassays or mass spectrometry; PCR specifically amplifies nucleic acid, not protein.",
                        "C": "Lipid extracts are outside PCR chemistry, which copies DNA/RNA targets with polymerase.",
                        "D": "Plasma glucose is a chemistry analyte; PCR amplifies nucleic acid sequences, not sugars.",
                    },
                },
                {
                    "question": "Contamination control in PCR includes?",
                    "options": [
                        "A) Shared pipettes across pre- and post-PCR benches",
                        "B) Separate areas, unidirectional workflow, and controls",
                        "C) Open amplicon handling beside extraction",
                        "D) Skipping no-template controls to save wells",
                    ],
                    "answer": "B) Separate areas, unidirectional workflow, and controls",
                    "explanation": "PCR is highly susceptible to false positives from amplicon or specimen contamination. Laboratories use unidirectional workflow, physical separation of pre- and post-PCR areas, dedicated reagents, and negative controls. Environmental wipe testing helps detect covert contamination.",
                    "choice_explanations": {
                        "A": "Sharing pipettes across pre- and post-PCR areas moves amplicons backward and seeds false-positive contamination.",
                        "B": "Contamination control uses physically separate areas, unidirectional workflow, dedicated reagents, and no-template controls to prevent amplicon carryover false positives.",
                        "C": "Opening amplicons beside extraction directly contaminates incoming specimens with amplified product.",
                        "D": "No-template controls detect contamination; skipping them removes a key monitor for false-positive PCR.",
                    },
                },
                {
                    "question": "Viral load assays monitor?",
                    "options": [
                        "A) Only qualitative serology IgG presence",
                        "B) Only plaque morphology on culture plates",
                        "C) Quantity of viral nucleic acid",
                        "D) Only CD4 percentage without nucleic acid",
                    ],
                    "answer": "C) Quantity of viral nucleic acid",
                    "explanation": "Viral load assays quantify pathogen nucleic acid, typically as IU/mL or copies/mL, using calibrated real-time PCR or related methods. Serial results monitor treatment response in infections such as HIV, HBV, and HCV. Standardization and log-change interpretation guide clinical decisions.",
                    "choice_explanations": {
                        "A": "Qualitative IgG serology indicates past/present antibody response, not quantitative viral nucleic-acid burden used as viral load.",
                        "B": "Plaque morphology assesses cultured virus phenotypes; clinical viral load quantifies nucleic acid in patient plasma/blood.",
                        "C": "Viral load assays quantify pathogen nucleic acid (IU/mL or copies/mL), typically by calibrated real-time PCR, to monitor treatment response.",
                        "D": "CD4 percentage assesses immune status in HIV care but is not itself a nucleic-acid viral load measurement.",
                    },
                },
            ],
            "medium": [
                {
                    "question": "Ct value roughly relates to?",
                    "options": [
                        "A) Directly proportional to target amount always",
                        "B) Independent of template concentration always",
                        "C) Only to extraction volume, never template",
                        "D) Inversely to target amount (method-dependent)",
                    ],
                    "answer": "D) Inversely to target amount (method-dependent)",
                    "explanation": "In real-time PCR, the cycle threshold (Ct) is the cycle at which fluorescence exceeds a defined threshold. Lower Ct values generally indicate more starting target nucleic acid, though exact quantification requires a calibration curve. Assay design and efficiency affect the Ct–quantity relationship.",
                    "choice_explanations": {
                        "A": "Ct is not directly proportional to target amount; more target reaches threshold earlier, so Ct falls as template rises.",
                        "B": "Ct depends strongly on starting template concentration under efficient amplification; it is not independent of target amount.",
                        "C": "Extraction volume affects recovery, but Ct primarily tracks how much target entered the PCR, inversely under standard kinetics.",
                        "D": "In real-time PCR, cycle threshold is reached sooner when more target is present, so Ct relates inversely to starting target amount (method-dependent).",
                    },
                },
                {
                    "question": "Internal control failure suggests?",
                    "options": [
                        "A) Inhibition or extraction problem",
                        "B) Confirmed true-negative without caveats",
                        "C) Instrument optical failure only, never inhibition",
                        "D) Primer redesign is always required immediately",
                    ],
                    "answer": "A) Inhibition or extraction problem",
                    "explanation": "An internal control co-extracted and co-amplified with the patient specimen monitors extraction efficiency and PCR inhibition. Failure of the internal control invalidates a negative target result and prompts re-extraction or dilution studies. Valid controls are required before clinical reporting.",
                    "choice_explanations": {
                        "A": "Internal-control failure indicates extraction inefficiency or PCR inhibition, invalidating a negative target result until the problem is resolved.",
                        "B": "A failed internal control means a negative target cannot be trusted as a true negative because amplification/extraction may have failed.",
                        "C": "Although optics can fail, internal-control failure classically signals inhibition or extraction problems that must be investigated.",
                        "D": "Primer redesign is not the first response; troubleshoot inhibition, extraction, and reagents before redesigning primers.",
                    },
                },
                {
                    "question": "Genotyping may guide?",
                    "options": [
                        "A) Only specimen transport temperature logs",
                        "B) Therapy (resistance/pharmacogenetics themes)",
                        "C) Only centrifuge RPM validation schedules",
                        "D) Only pipette calibration intervals",
                    ],
                    "answer": "B) Therapy (resistance/pharmacogenetics themes)",
                    "explanation": "Genotyping identifies sequence variants that predict drug resistance or alter drug metabolism, as in HIV resistance testing or pharmacogenetic panels. Results help select effective therapy and dosing. Analytic validity and clinical annotation databases support interpretation.",
                    "choice_explanations": {
                        "A": "Transport temperature logs are preanalytic QA, not the therapeutic decision support provided by resistance or pharmacogenetic genotyping.",
                        "B": "Genotyping identifies variants that predict drug resistance or alter drug metabolism, guiding therapy selection and dosing.",
                        "C": "Centrifuge RPM validation is instrument QA, unrelated to patient genotype-guided therapy.",
                        "D": "Pipette calibration maintains volumetric accuracy but does not interpret resistance or pharmacogenetic genotypes.",
                    },
                },
            ],
            "hard": [
                {
                    "question": "NGS panels need?",
                    "options": [
                        "A) Wet-lab sequencing alone without analysis",
                        "B) Sanger confirmation of every wild-type base",
                        "C) Bioinformatic pipelines, QC metrics, and interpretation",
                        "D) No coverage thresholds for clinical reporting",
                    ],
                    "answer": "C) Bioinformatic pipelines, QC metrics, and interpretation",
                    "explanation": "Next-generation sequencing (NGS) panels generate massive parallel reads that require bioinformatic pipelines for alignment, variant calling, and annotation. Quality metrics (coverage, uniformity, contamination checks) gate reportability. Multidisciplinary interpretation links variants to clinical actionability.",
                    "choice_explanations": {
                        "A": "Wet-lab sequencing alone without bioinformatics cannot call, annotate, or QC clinically reportable variants from NGS data.",
                        "B": "Sanger confirmation policies are selective; requiring Sanger of every wild-type base is neither feasible nor the core NGS need.",
                        "C": "NGS panels require validated bioinformatic pipelines, coverage/quality metrics, and expert interpretation to turn reads into clinical variant reports.",
                        "D": "Coverage thresholds are essential QC; reporting without them risks missing variants in poorly covered regions.",
                    },
                },
                {
                    "question": "Minimal residual disease PCR detects?",
                    "options": [
                        "A) Only morphologic blast percentage above 5%",
                        "B) Only cytogenetic metaphases without DNA target",
                        "C) Only serum protein electrophoresis clones",
                        "D) Very low-level residual disease target",
                    ],
                    "answer": "D) Very low-level residual disease target",
                    "explanation": "MRD PCR assays amplify leukemia-specific targets such as fusion transcripts or clonal immunoglobulin/T-cell receptor rearrangements at high sensitivity. Detectable MRD after therapy informs relapse risk and consolidation decisions. Assay limit of detection must be validated and reported.",
                    "choice_explanations": {
                        "A": "Morphologic blast percentage above 5% defines morphologic disease, far coarser than MRD PCR’s deep molecular sensitivity.",
                        "B": "Cytogenetics examines metaphases at limited sensitivity; MRD PCR amplifies leukemia-specific nucleic-acid targets at much lower levels.",
                        "C": "Serum protein electrophoresis detects plasma-cell paraproteins, not leukemia-specific MRD nucleic-acid targets.",
                        "D": "MRD PCR amplifies leukemia-specific fusions or clonal receptor rearrangements to detect very low-level residual disease below morphologic thresholds.",
                    },
                },
                {
                    "question": "Sample swap detection uses?",
                    "options": [
                        "A) Identity checks/barcodes (± genetic ID strategies)",
                        "B) Ignoring identifiers if Ct values look expected",
                        "C) Relying only on handwritten first names",
                        "D) Skipping accession checks for add-on tests",
                    ],
                    "answer": "A) Identity checks/barcodes (± genetic ID strategies)",
                    "explanation": "Specimen identity errors can cause catastrophic molecular misdiagnosis. Laboratories use barcodes, chain-of-custody checks, and sometimes genetic identity markers to detect swaps. Discrepancies halt reporting until identity is resolved.",
                    "choice_explanations": {
                        "A": "Barcodes, accession checks, and sometimes genetic identity markers detect specimen swaps that would otherwise assign molecular results to the wrong patient.",
                        "B": "Expected Ct values cannot prove specimen identity; mix-ups can still produce plausible numeric results for the wrong person.",
                        "C": "Handwritten first names are weak identifiers and do not reliably detect swaps compared with barcodes and dual identifiers.",
                        "D": "Skipping accession checks for add-ons increases sample-swap risk precisely when identity verification is needed.",
                    },
                },
            ],
            "extreme": [
                {
                    "question": "Laboratory-developed tests require?",
                    "options": [
                        "A) Immediate patient reporting without performance data",
                        "B) Validation/verification per regulations before clinical use",
                        "C) Research-use-only reagents without local validation",
                        "D) Vendor marketing claims as sole acceptance criteria",
                    ],
                    "answer": "B) Validation/verification per regulations before clinical use",
                    "explanation": "Laboratory-developed tests (LDTs) must be validated or verified for accuracy, precision, reportable range, and other performance characteristics before clinical use per applicable regulations and accreditation standards. Documentation of acceptance criteria and limitations is mandatory. Ongoing QC sustains performance after go-live.",
                    "choice_explanations": {
                        "A": "Reporting LDT results without performance data skips required accuracy, precision, and reportable-range demonstration for clinical use.",
                        "B": "Laboratory-developed tests must be validated or verified for defined performance characteristics per regulations/accreditation before clinical patient testing.",
                        "C": "Research-use-only reagents still require local validation/verification before results are used clinically.",
                        "D": "Vendor marketing claims are not a substitute for laboratory-generated validation evidence under regulatory standards.",
                    },
                },
                {
                    "question": "Amplicon contamination outbreak presents as?",
                    "options": [
                        "A) Isolated true positives with epidemiologic links only",
                        "B) Only internal-control failures without positives",
                        "C) Clusters of unexpected positive PCR results",
                        "D) Only reagent lot shortages without result patterns",
                    ],
                    "answer": "C) Clusters of unexpected positive PCR results",
                    "explanation": "Amplicon contamination outbreaks produce clusters of unexpected positive PCR results, often with late Ct values or positives in negative controls. Immediate containment includes stopping testing, environmental cleaning, and root-cause investigation. Retesting from primary specimens after remediation confirms integrity.",
                    "choice_explanations": {
                        "A": "True epidemiologic clusters differ from contamination outbreaks that also spike negatives/controls with unexpected positives.",
                        "B": "Internal-control failures suggest inhibition; amplicon contamination typically presents as unexpected positive PCR clusters.",
                        "C": "Amplicon contamination outbreaks produce clusters of unexpected positive PCR results, often with late Ct values or positives in negative controls.",
                        "D": "Reagent shortages cause operational delays, not the patterned unexpected positives that mark amplicon contamination.",
                    },
                },
                {
                    "question": "Cell-free DNA assays challenges include?",
                    "options": [
                        "A) Abundant intact genomic DNA identical to tissue",
                        "B) No need for specialized blood-collection tubes",
                        "C) Stability for weeks at ambient temperature always",
                        "D) Low analyte levels, fragmentation, and preanalytics",
                    ],
                    "answer": "D) Low analyte levels, fragmentation, and preanalytics",
                    "explanation": "Circulating cell-free DNA assays measure fragmented extracellular DNA present at low concentrations in plasma. Preanalytic variables (tube type, time to spin, hemolysis) strongly affect yield and fragment profiles. Sensitive methods and careful controls are required for reliable detection.",
                    "choice_explanations": {
                        "A": "cfDNA is fragmented and present at low levels, unlike abundant intact genomic DNA from cells; that scarcity drives assay challenges.",
                        "B": "Specialized stabilizing blood-collection tubes are often required because ordinary tubes allow leukocyte DNA leakage that dilutes true cfDNA signals.",
                        "C": "cfDNA is unstable without proper tubes and timely processing; weeks at ambient temperature are not generally acceptable.",
                        "D": "Cell-free DNA assays contend with low analyte concentration, fragmentation, and stringent preanalytic variables that affect yield and variant detection.",
                    },
                },
            ],
        },
        "cases": {
            "easy": [
                {
                    "title": "COVID/Flu NAAT Order",
                    "stem": "Respiratory NAAT requested.",
                    "question": "Preanalytic key?",
                    "answer": "Correct swab/transport, labeling, avoid contamination.",
                    "discussion": "Invalid if poor collection.",
                    "book_hint": "Molecular Diagnostics texts / CAP molecular themes",
                },
            ],
            "medium": [
                {
                    "title": "Inhibited PCR",
                    "stem": "Patient negative but IC fails.",
                    "question": "Report?",
                    "answer": "Invalid/inhibited — do not call true negative; repeat.",
                    "discussion": "Communicate.",
                    "book_hint": "Molecular Diagnostics texts / CAP molecular themes",
                },
            ],
            "hard": [
                {
                    "title": "Unexpected Mutation Report",
                    "stem": "Pathogenic variant reported but clinical mismatch. Choose the safest high-yield next laboratory concept.",
                    "question": "Steps?",
                    "answer": "Confirm identity, review IGV/reads, orthogonal method, amend if needed.",
                    "discussion": "Patient impact huge.",
                    "book_hint": "Molecular Diagnostics texts / CAP molecular themes",
                },
            ],
            "extreme": [
                {
                    "title": "Wave of Weak Positives",
                    "stem": "Sudden rise in low-positive NAAT results after renovation near PCR room. Avoid reporting or actions that could harm if a critical quality risk remains open.",
                    "question": "Suspect?",
                    "answer": "Contamination — halt reporting, investigate environment/workflow, notify clinicians about possible false positives.",
                    "discussion": "Quality crisis management.",
                    "book_hint": "Molecular Diagnostics texts / CAP molecular themes",
                },
            ],
        },
    },
    "lab_qa": {
        "label": "Lab QA & Safety",
        "books": [
            "ISO 15189 overview materials",
            "CLSI quality documents",
            "Biosafety in Microbiological and Biomedical Laboratories",
        ],
        "pdf_notes": [
            "Do not release patient results when QC is out of control.",
            "Westgard rules help detect random vs systematic error.",
            "Needle-stick: wash, report, evaluate source, follow PEP policy.",
            "Document corrective actions and verify before resuming testing.",
            "Quality is a system: people, methods, reagents, equipment, IT.",
        ],
        "questions": {
            "easy": [
                {
                    "question": "QA means?",
                    "options": [
                        "A) Quality assurance — systems ensuring reliable results",
                        "B) Quick assay — fastest method regardless of QC",
                        "C) Quiet area — noise limits for analyzers only",
                        "D) Quarterly absence — staffing vacation tracking",
                    ],
                    "answer": "A) Quality assurance — systems ensuring reliable results",
                    "explanation": "Quality assurance (QA) encompasses the organized systems, policies, and monitoring activities that ensure laboratory results are reliable and fit for clinical use. QA spans preanalytic, analytic, and postanalytic phases. It is broader than daily QC and includes PT, document control, and continual improvement.",
                    "choice_explanations": {
                        "A": "Quality assurance encompasses organized systems, policies, and monitoring across preanalytic, analytic, and postanalytic phases to ensure results are reliable and clinically fit for use.",
                        "B": "Selecting the fastest method regardless of QC prioritizes speed over analytic validity and is not what QA means.",
                        "C": "Analyzer noise limits are environmental engineering details, not the systems definition of quality assurance.",
                        "D": "Staffing vacation tracking is workforce scheduling, unrelated to laboratory quality-assurance systems.",
                    },
                },
                {
                    "question": "QC monitors?",
                    "options": [
                        "A) Only clinician satisfaction survey scores",
                        "B) Analytic method performance over time",
                        "C) Only purchasing contract renewal dates",
                        "D) Only building temperature for HVAC billing",
                    ],
                    "answer": "B) Analytic method performance over time",
                    "explanation": "Quality control (QC) uses materials of known target values to monitor analytic method stability over time. Results are plotted and evaluated with rules to detect shifts, trends, and imprecision. QC failures trigger investigation before patient results are released.",
                    "choice_explanations": {
                        "A": "Clinician satisfaction surveys are service metrics; QC specifically monitors analytic method performance with known control materials over time.",
                        "B": "Quality control runs materials of known target values to monitor analytic accuracy, precision, shifts, and trends across time.",
                        "C": "Purchasing contract dates are administrative and do not assess method analytic performance.",
                        "D": "HVAC billing temperatures are facility costs, not QC charts of assay control results.",
                    },
                },
                {
                    "question": "SOP stands for?",
                    "options": [
                        "A) Selective optional protocol",
                        "B) Specimen overflow process",
                        "C) Standard operating procedure",
                        "D) Supervisor oral permission",
                    ],
                    "answer": "C) Standard operating procedure",
                    "explanation": "A standard operating procedure (SOP) is the controlled written instruction detailing how a method or process is performed. Staff must follow the current approved SOP version. Document control ensures obsolete instructions are removed from use.",
                    "choice_explanations": {
                        "A": "Selective optional protocol is not the controlled written method staff must follow; SOP means standard operating procedure.",
                        "B": "Specimen overflow process is informal wording; SOP denotes the approved standard operating procedure for a method.",
                        "C": "A standard operating procedure is the controlled written instruction detailing how a laboratory method or process is performed, kept under document control.",
                        "D": "Supervisor oral permission cannot replace the current approved written SOP as the procedural authority.",
                    },
                },
            ],
            "medium": [
                {
                    "question": "Westgard rules help detect?",
                    "options": [
                        "A) Only patient delta-check identity mismatches",
                        "B) Only proficiency shipping delays",
                        "C) Only critical-value phone read-back failures",
                        "D) Random and systematic error patterns in QC",
                    ],
                    "answer": "D) Random and systematic error patterns in QC",
                    "explanation": "Westgard multirule QC applies combinations of control rules (for example 1₃ₛ, 2₂ₛ, R₄ₛ) to distinguish random from systematic error. Rule violations prompt troubleshooting of reagents, calibration, and instrumentation. Appropriate rule selection balances error detection with false rejection.",
                    "choice_explanations": {
                        "A": "Delta checks compare patient results for identity/analytic anomalies; Westgard rules evaluate QC control data for random vs systematic error.",
                        "B": "Proficiency shipping delays are logistics issues, not the statistical QC-rule patterns Westgard detects.",
                        "C": "Critical-value read-back failures are communication defects; Westgard rules detect analytic QC error patterns.",
                        "D": "Westgard multirule QC applies combinations of control rules to distinguish random error from systematic error in QC data and trigger troubleshooting.",
                    },
                },
                {
                    "question": "Proficiency testing evaluates?",
                    "options": [
                        "A) Laboratory accuracy on external unknown specimens",
                        "B) Only internal QC means without peer comparison",
                        "C) Only employee continuing-education attendance",
                        "D) Only analyzer uptime percentage metrics",
                    ],
                    "answer": "A) Laboratory accuracy on external unknown specimens",
                    "explanation": "Proficiency testing (PT) submits blinded external specimens for analysis and compares laboratory results with peer or reference targets. Successful PT is an accreditation requirement demonstrating analytic accuracy. Failures require investigation and corrective action.",
                    "choice_explanations": {
                        "A": "Proficiency testing analyzes blinded external specimens and compares results with peer or reference targets to evaluate laboratory accuracy.",
                        "B": "Internal QC monitors day-to-day stability but lacks the external peer comparison that proficiency testing provides.",
                        "C": "CE attendance tracks education credits, not analytic accuracy on unknown external challenges.",
                        "D": "Analyzer uptime is operational availability, not accuracy versus external PT targets.",
                    },
                },
                {
                    "question": "Critical results require?",
                    "options": [
                        "A) Release into the chart without clinician contact",
                        "B) Timely notification with read-back and documentation",
                        "C) Notification only at the next shift change",
                        "D) Patient self-notification via portal only",
                    ],
                    "answer": "B) Timely notification with read-back and documentation",
                    "explanation": "Critical results are laboratory values that indicate potentially life-threatening conditions and require immediate clinical notification. Read-back verification and documentation complete the communication loop. Policies define analyte lists, timeframes, and escalation paths.",
                    "choice_explanations": {
                        "A": "Chart release without clinician contact fails the immediacy required for potentially life-threatening critical results.",
                        "B": "Critical results require timely clinician notification with read-back verification and documentation to ensure emergent clinical action.",
                        "C": "Deferring notification to the next shift delays treatment of life-threatening values and violates critical-result timelines.",
                        "D": "Patient portal self-notification does not replace direct communication with a responsible clinician for critical values.",
                    },
                },
            ],
            "hard": [
                {
                    "question": "Root cause analysis after error aims to?",
                    "options": [
                        "A) Punish the last person who touched the specimen",
                        "B) Hide the event from accreditation surveyors",
                        "C) Correct system causes, not only blame individuals",
                        "D) Rewrite QC data to erase the incident trail",
                    ],
                    "answer": "C) Correct system causes, not only blame individuals",
                    "explanation": "Root cause analysis after a laboratory error investigates underlying system failures such as process design, training gaps, and interface issues rather than stopping at individual blame. Effective CAPA addresses latent conditions that allowed the error. Sharing lessons learned prevents recurrence.",
                    "choice_explanations": {
                        "A": "Punishing the last person ignores latent system failures; root cause analysis seeks process causes that allow errors to recur.",
                        "B": "Hiding events from surveyors is unethical and prevents corrective learning; RCA documents and remediates system causes.",
                        "C": "Root cause analysis after laboratory error investigates and corrects underlying system causes—process design, training, interfaces—rather than stopping at individual blame.",
                        "D": "Rewriting QC data falsifies records and conceals failure; RCA requires honest investigation and system fixes.",
                    },
                },
                {
                    "question": "Document control ensures?",
                    "options": [
                        "A) Staff may keep personal unofficial binders",
                        "B) Obsolete SOPs remain at benches for reference",
                        "C) Draft procedures are used before approval",
                        "D) Only current approved SOPs are in use",
                    ],
                    "answer": "D) Only current approved SOPs are in use",
                    "explanation": "Document control ensures that only the current, approved version of each SOP, form, and policy is available at the point of use. Obsolete documents are removed or clearly archived. Version history and approval signatures support accreditation compliance.",
                    "choice_explanations": {
                        "A": "Personal unofficial binders risk obsolete instructions; document control centralizes only current approved documents at the bench.",
                        "B": "Leaving obsolete SOPs at benches invites use of outdated methods; controlled removal/archiving is required.",
                        "C": "Draft procedures lack approval and validation; only current approved SOPs may be used for patient testing.",
                        "D": "Document control ensures only the current approved version of each SOP, form, and policy is available at the point of use.",
                    },
                },
                {
                    "question": "Risk management in labs includes?",
                    "options": [
                        "A) Identifying failure modes and implementing mitigations",
                        "B) Waiting for patient harm before any review",
                        "C) Eliminating all QC to reduce false rejects",
                        "D) Outsourcing all critical-value calls permanently",
                    ],
                    "answer": "A) Identifying failure modes and implementing mitigations",
                    "explanation": "Laboratory risk management systematically identifies potential failure modes across testing pathways and implements mitigations proportional to severity and likelihood. Tools may include process mapping and failure mode effects analysis. Residual risk is monitored through QC, audits, and incident review.",
                    "choice_explanations": {
                        "A": "Laboratory risk management identifies failure modes across testing pathways and implements mitigations scaled to severity and likelihood.",
                        "B": "Waiting for patient harm is reactive; proactive failure-mode identification aims to prevent harm before it occurs.",
                        "C": "Removing all QC takes away the primary analytic monitor and increases undetected error risk rather than managing it.",
                        "D": "Outsourcing critical-value calls without a validated process can break notification reliability; risk management strengthens, not abandons, critical communication.",
                    },
                },
            ],
            "extreme": [
                {
                    "question": "Accreditation nonconformance demands?",
                    "options": [
                        "A) Verbal promise without documented CAPA",
                        "B) Corrective/preventive action with effectiveness evidence",
                        "C) Ignoring findings until the next survey cycle",
                        "D) Rewording the SOP title without process change",
                    ],
                    "answer": "B) Corrective/preventive action with effectiveness evidence",
                    "explanation": "Accreditation nonconformances require documented corrective and preventive action (CAPA) with evidence that the fix is effective. Root cause, implementation, and follow-up monitoring are assessed by surveyors. Timely closure protects patient safety and accreditation status.",
                    "choice_explanations": {
                        "A": "Verbal promises without documented CAPA do not satisfy accreditation requirements for evidenced corrective action.",
                        "B": "Accreditation nonconformances require documented corrective and preventive action with evidence that the remedy is effective, including follow-up monitoring.",
                        "C": "Ignoring findings until the next survey leaves patients exposed to the same failure mode and worsens accreditation outcomes.",
                        "D": "Rewording an SOP title without changing the failing process does not correct the root cause or demonstrate effectiveness.",
                    },
                },
                {
                    "question": "LIS downtime procedure must?",
                    "options": [
                        "A) Stop all testing until IT returns next week",
                        "B) Release results without patient identifiers",
                        "C) Maintain safe manual identification and reporting",
                        "D) Use informal texts as the permanent record only",
                    ],
                    "answer": "C) Maintain safe manual identification and reporting",
                    "explanation": "Laboratory information system (LIS) downtime procedures provide validated manual workflows for order entry, specimen identification, result recording, and reporting. Patient ID integrity and critical-value communication must continue. After recovery, data are entered and reconciled per protocol.",
                    "choice_explanations": {
                        "A": "Stopping all testing for a week can harm patients; downtime procedures sustain safe testing with manual identification and reporting.",
                        "B": "Releasing results without patient identifiers creates wrong-patient risk precisely when LIS safeguards are offline.",
                        "C": "LIS downtime procedures maintain validated manual workflows for identification, result recording, and reporting so patient ID integrity and critical communication continue.",
                        "D": "Informal texts are not a controlled permanent record; downtime documentation must be retrievable and attributable.",
                    },
                },
                {
                    "question": "Ethical reflex: altered QC to pass?",
                    "options": [
                        "A) Acceptable if patient results look plausible",
                        "B) Allowed when reagent costs are high that week",
                        "C) Required to keep turnaround time statistics green",
                        "D) Fraud — never alter QC; report integrity concerns",
                    ],
                    "answer": "D) Fraud — never alter QC; report integrity concerns",
                    "explanation": "Altering quality-control data to force a method to “pass” is scientific misconduct and endangers patients by concealing analytic failure. Staff must refuse falsification and escalate integrity concerns through proper channels. A culture of safety supports transparent troubleshooting.",
                    "choice_explanations": {
                        "A": "Altering QC because patient results look plausible conceals analytic failure and endangers subsequent patients.",
                        "B": "Reagent cost never justifies falsifying QC; integrity of control data is non-negotiable.",
                        "C": "Turnaround statistics must not be preserved by fabricating QC passes that hide method failure.",
                        "D": "Altering quality-control data to force a pass is scientific fraud that conceals analytic failure; staff must refuse falsification and escalate integrity concerns.",
                    },
                },
            ],
        },
        "cases": {
            "easy": [
                {
                    "title": "QC Out of Range",
                    "stem": "Daily QC fails.",
                    "question": "Action?",
                    "answer": "Do not report patient results until resolved per SOP.",
                    "discussion": "Troubleshoot then document.",
                    "book_hint": "Clinical Laboratory Management / CAP accreditation themes",
                },
            ],
            "medium": [
                {
                    "title": "PT Unsatisfactory",
                    "stem": "Proficiency testing fails for glucose.",
                    "question": "Next?",
                    "answer": "Investigate, corrective action, possible patient impact assessment.",
                    "discussion": "Document thoroughly.",
                    "book_hint": "Clinical Laboratory Management / CAP accreditation themes",
                },
            ],
            "hard": [
                {
                    "title": "Wrong Blood in Tube Event",
                    "stem": "WBIT discovered after delta check. Choose the safest high-yield next laboratory concept.",
                    "question": "Response?",
                    "answer": "Recall results, recollect, RCA, notify clinicians, systemic barcode/ID fixes.",
                    "discussion": "High-harm event.",
                    "book_hint": "Clinical Laboratory Management / CAP accreditation themes",
                },
            ],
            "extreme": [
                {
                    "title": "Systemic QC Falsification Allegation",
                    "stem": "Staff report that failing QC was rewritten as passing. Avoid reporting or actions that could harm if a critical quality risk remains open.",
                    "question": "Leadership action?",
                    "answer": "Immediate investigation, protect patients (result review), protect reporters, regulatory notification as required.",
                    "discussion": "Integrity crisis.",
                    "book_hint": "Clinical Laboratory Management / CAP accreditation themes",
                },
            ],
        },
    },
    "urinalysis": {
        "label": "Urinalysis & Body Fluids",
        "books": [
            "Urinalysis and Body Fluids — Strasinger",
            "Clinical microscopy manuals",
            "CLSI body fluid documents",
        ],
        "pdf_notes": [
            "Correlate dipstick with microscopy.",
            "RBC casts suggest glomerular disease themes.",
            "CSF: cell count, differential, culture, and timing matter.",
            "Crystal ID: polarization distinguishes MSU vs CPPD themes.",
            "Proper collection (midstream, timed) reduces false positives.",
        ],
        "questions": {
            "easy": [
                {
                    "question": "Urine dipstick blood may detect?",
                    "options": [
                        "A) Intact RBCs, free hemoglobin, or myoglobin",
                        "B) Glucose via glucose oxidase only",
                        "C) Ketones via nitroprusside only",
                        "D) Leukocyte esterase from WBC enzymes only",
                    ],
                    "answer": "A) Intact RBCs, free hemoglobin, or myoglobin",
                    "explanation": "Urine dipstick “blood” reagents detect heme’s peroxidase-like activity and therefore react with intact red cells, free hemoglobin, and myoglobin. Microscopy distinguishes hematuria from heme-positive pigmenturia. Clinical context separates hemoglobinuria from myoglobinuria.",
                    "choice_explanations": {
                        "A": "Dipstick blood reagents detect heme’s peroxidase-like activity, so intact RBCs, free hemoglobin, and myoglobin can all produce a positive blood pad.",
                        "B": "Glucose oxidase chemistry is on the glucose pad, not the blood pad that detects heme peroxidase activity.",
                        "C": "Nitroprusside ketone detection is a separate pad; blood positivity reflects heme, not acetoacetate.",
                        "D": "Leukocyte esterase detects WBC enzymes on its own pad and does not explain blood-pad reactivity to heme.",
                    },
                },
                {
                    "question": "Specific gravity estimates?",
                    "options": [
                        "A) Exact 24-hour protein excretion grams",
                        "B) Urine concentrating ability (relative density)",
                        "C) Bacterial species identification",
                        "D) Urine pH buffering capacity alone",
                    ],
                    "answer": "B) Urine concentrating ability (relative density)",
                    "explanation": "Urine specific gravity estimates the density of urine relative to water and reflects renal concentrating and diluting ability. Refractometer or reagent-strip methods are commonly used; osmolality is a related but distinct measure. Interpretation considers hydration status and interfering large molecules.",
                    "choice_explanations": {
                        "A": "Exact 24-hour protein excretion requires timed collection and quantification; specific gravity estimates relative density/concentrating ability.",
                        "B": "Urine specific gravity estimates density relative to water and thereby reflects renal concentrating and diluting ability.",
                        "C": "Bacterial species identification requires culture; specific gravity is a physical concentrating metric.",
                        "D": "Urine pH measures hydrogen-ion activity; specific gravity estimates relative density, not buffering capacity alone.",
                    },
                },
                {
                    "question": "CSF tube order typically?",
                    "options": [
                        "A) All tubes pooled into one chemistry cup",
                        "B) Only the first tube used for all testing",
                        "C) Allocated to chemistry, microbiology, and hematology per protocol",
                        "D) Random tube assignment without labeling",
                    ],
                    "answer": "C) Allocated to chemistry, microbiology, and hematology per protocol",
                    "explanation": "CSF is typically collected into sequentially numbered tubes allocated to chemistry, microbiology, and hematology per institutional protocol. Tube order reduces blood-contamination effects on selected tests. Clear labeling and prompt delivery preserve analytic integrity.",
                    "choice_explanations": {
                        "A": "Pooling all CSF tubes mixes compartments and defeats protocolized allocation that reduces contamination effects on selected tests.",
                        "B": "Using only the first tube for everything ignores that early tubes are more blood-contaminated; later tubes are preferred for some analyses.",
                        "C": "CSF is collected into sequentially numbered tubes allocated to chemistry, microbiology, and hematology per protocol to optimize each test’s preanalytics.",
                        "D": "Random unlabeled assignment destroys chain-of-custody and correct test routing for CSF.",
                    },
                },
            ],
            "medium": [
                {
                    "question": "RBC casts suggest?",
                    "options": [
                        "A) Lower-tract contamination without renal disease",
                        "B) Only pyelonephritis with WBC casts exclusively",
                        "C) Only nephrotic syndrome with fatty casts exclusively",
                        "D) Glomerular bleeding/disease",
                    ],
                    "answer": "D) Glomerular bleeding/disease",
                    "explanation": "Red blood cell casts form when RBCs are embedded in Tamm–Horsfall protein within renal tubules and indicate glomerular bleeding. They support diagnoses such as glomerulonephritis. Careful microscopy distinguishes true casts from look-alike artifacts.",
                    "choice_explanations": {
                        "A": "Lower-tract contamination may add free RBCs but does not form true RBC casts molded in renal tubules.",
                        "B": "WBC casts suggest renal parenchymal inflammation such as pyelonephritis; RBC casts specifically indicate glomerular bleeding.",
                        "C": "Fatty casts/oval fat bodies associate with nephrotic lipiduria; RBC casts indicate glomerular hemorrhage.",
                        "D": "RBC casts form when red cells embed in Tamm–Horsfall protein within tubules, indicating glomerular bleeding/disease such as glomerulonephritis.",
                    },
                },
                {
                    "question": "Oval fat bodies associate with?",
                    "options": [
                        "A) Nephrotic-range proteinuria/lipiduria themes",
                        "B) Isolated lower UTI without proteinuria",
                        "C) Acute cystitis with squamous cells only",
                        "D) Diabetes insipidus with dilute urine only",
                    ],
                    "answer": "A) Nephrotic-range proteinuria/lipiduria themes",
                    "explanation": "Oval fat bodies are renal tubular epithelial cells or macrophages laden with lipid, classically associated with heavy proteinuria of nephrotic syndrome. Polarized microscopy may show Maltese-cross fat droplets. Correlation with urine protein quantitation and serum albumin supports the diagnosis.",
                    "choice_explanations": {
                        "A": "Oval fat bodies are lipid-laden RTE cells or macrophages classically linked to heavy proteinuria/lipiduria of nephrotic syndrome, often with Maltese-cross fat under polarized light.",
                        "B": "Isolated lower UTI produces pyuria/bacteriuria without the lipiduria that yields oval fat bodies.",
                        "C": "Squamous cells suggest contamination or lower-tract shedding, not nephrotic lipid-laden oval fat bodies.",
                        "D": "Diabetes insipidus yields dilute urine from ADH deficiency/resistance without nephrotic-range lipiduria.",
                    },
                },
                {
                    "question": "Synovial fluid crystals: needle, strong negative birefringence?",
                    "options": [
                        "A) Calcium pyrophosphate (pseudogout) rhomboids",
                        "B) Monosodium urate (gout)",
                        "C) Cholesterol plates from chronic effusions only",
                        "D) Hydroxyapatite clumps without birefringence only",
                    ],
                    "answer": "B) Monosodium urate (gout)",
                    "explanation": "Monosodium urate crystals of gout are needle-shaped and show strong negative birefringence under compensated polarized light. Calcium pyrophosphate crystals of pseudogout are typically rhomboid/rod-shaped with weak positive birefringence. Correct crystal ID directs acute arthritis therapy.",
                    "choice_explanations": {
                        "A": "Calcium pyrophosphate crystals of pseudogout are typically rhomboid/rod-shaped with weak positive birefringence, not needles with strong negative birefringence.",
                        "B": "Monosodium urate crystals of gout are needle-shaped and show strong negative birefringence under compensated polarized light.",
                        "C": "Cholesterol plates appear in chronic effusions as flat parallelograms, not needles with strong negative birefringence.",
                        "D": "Hydroxyapatite is usually nonbirefringent by light microscopy and does not match needle-shaped strong negative birefringence.",
                    },
                },
            ],
            "hard": [
                {
                    "question": "Xanthochromia in CSF suggests?",
                    "options": [
                        "A) Only traumatic tap without pigment evaluation",
                        "B) Only bacterial meningitis without hemorrhage",
                        "C) Subarachnoid hemorrhage after excluding artifact",
                        "D) Only viral PCR positivity without color change",
                    ],
                    "answer": "C) Subarachnoid hemorrhage after excluding artifact",
                    "explanation": "Xanthochromia is yellowish CSF discoloration from bilirubin formed in situ after subarachnoid hemorrhage, appearing hours after onset. Spectrophotometry and timing help distinguish SAH from traumatic tap artifact. Immediate clinical notification is required when SAH is suspected.",
                    "choice_explanations": {
                        "A": "A traumatic tap introduces fresh blood; xanthochromia after appropriate timing/spectrophotometry supports in-vivo bilirubin from SAH rather than artifact alone.",
                        "B": "Bacterial meningitis may cloud CSF with neutrophils but does not define xanthochromia from bilirubin after hemorrhage.",
                        "C": "Xanthochromia reflects bilirubin formed in situ after subarachnoid hemorrhage; after excluding traumatic artifact by timing/spectrophotometry, it supports SAH.",
                        "D": "Viral PCR positivity diagnoses viral CNS infection and does not produce the bilirubin discoloration of xanthochromia.",
                    },
                },
                {
                    "question": "Myoglobin vs hemoglobin on dipstick?",
                    "options": [
                        "A) Dipstick distinguishes them by two separate pads",
                        "B) Myoglobin never reacts with the blood pad",
                        "C) Hemoglobinuria always shows clear plasma always",
                        "D) Both can read blood-positive; plasma/clinical clues differ",
                    ],
                    "answer": "D) Both can read blood-positive; plasma/clinical clues differ",
                    "explanation": "Dipstick blood pads cannot distinguish myoglobin from hemoglobin because both possess heme groups that catalyze the indicator reaction. Clear plasma with heme-positive urine suggests myoglobinuria; pink/red plasma supports hemoglobinuria. CK, clinical context, and microscopy refine the distinction.",
                    "choice_explanations": {
                        "A": "A single blood pad cannot separate myoglobin from hemoglobin because both heme proteins catalyze the indicator reaction.",
                        "B": "Myoglobin does react with the blood pad via heme peroxidase activity, just as hemoglobin does.",
                        "C": "Hemoglobinuria often accompanies pink/red plasma; clear plasma with heme-positive urine more suggests myoglobinuria—so plasma is not always clear in hemoglobinuria.",
                        "D": "Both myoglobin and hemoglobin can make the blood pad positive; plasma color and clinical context (rhabdomyolysis vs hemolysis) help distinguish them.",
                    },
                },
                {
                    "question": "Transudate vs exudate uses?",
                    "options": [
                        "A) Light’s criteria themes for pleural fluid",
                        "B) Only fluid color without chemistry comparison",
                        "C) Only Gram stain without protein/LDH ratios",
                        "D) Only cell count without serum correlation",
                    ],
                    "answer": "A) Light’s criteria themes for pleural fluid",
                    "explanation": "Light’s criteria compare pleural fluid and serum protein and LDH to classify effusions as exudates or transudates. Exudates suggest local pleural pathology; transudates suggest systemic hydrostatic/oncotic imbalance. Correct classification focuses subsequent workup.",
                    "choice_explanations": {
                        "A": "Light’s criteria compare pleural fluid and serum protein and LDH ratios to classify exudates versus transudates and suggest local versus systemic causes.",
                        "B": "Fluid color alone cannot reliably separate exudate from transudate without protein/LDH comparison to serum.",
                        "C": "Gram stain detects organisms but does not classify hydrostatic versus inflammatory fluid by Light’s chemistry ratios.",
                        "D": "Cell counts inform inflammation/infection risk but require serum-correlated protein/LDH criteria to define transudate vs exudate.",
                    },
                },
            ],
            "extreme": [
                {
                    "question": "Body fluid cell counts on automated analyzers need?",
                    "options": [
                        "A) No validation because blood modes always transfer",
                        "B) Validation plus smear review for atypical cells",
                        "C) Autorelease of blasts without morphologic review",
                        "D) Replacement of all microbiology Gram stains",
                    ],
                    "answer": "B) Validation plus smear review for atypical cells",
                    "explanation": "Automated body-fluid cell counts require method validation for each fluid type because matrices differ from blood. Smear review detects malignant or atypical cells that counters alone may misclassify. Flags and laboratory policy define when manual counts and pathologist review are required.",
                    "choice_explanations": {
                        "A": "Blood counting modes do not automatically transfer to body fluids; each fluid matrix needs validation because optical/impedance behavior differs.",
                        "B": "Automated body-fluid counts require method validation for each fluid type plus smear review to detect atypical or malignant cells counters may misclassify.",
                        "C": "Autoreleasing blast flags without morphology risks missing or misidentifying malignancy in fluids.",
                        "D": "Cell counts do not replace microbiology Gram stains for organism detection in body fluids.",
                    },
                },
                {
                    "question": "Critical CSF findings require?",
                    "options": [
                        "A) Batch reporting with next morning results",
                        "B) Chart release without verbal/read-back alert",
                        "C) Immediate clinician notification",
                        "D) Notification only if culture later turns positive",
                    ],
                    "answer": "C) Immediate clinician notification",
                    "explanation": "Critical CSF findings—such as organisms on Gram stain, marked neutrophilic pleocytosis, or xanthochromia suggestive of SAH—require immediate clinician notification. Delays can worsen meningitis or neurosurgical outcomes. Documentation of notification is mandatory.",
                    "choice_explanations": {
                        "A": "Batching critical CSF findings until morning delays treatment of meningitis or SAH and violates critical-notification expectations.",
                        "B": "Chart release without verbal/read-back alert fails immediate clinician communication required for critical CSF results.",
                        "C": "Critical CSF findings—organisms on Gram stain, marked neutrophilic pleocytosis, or xanthochromia suggesting SAH—require immediate clinician notification.",
                        "D": "Waiting for later culture positivity postpones action on already critical microscopic or pigment findings.",
                    },
                },
                {
                    "question": "Contaminated clean-catch clues?",
                    "options": [
                        "A) Pure single uropathogen ≥10^5 CFU/mL without squamous cells",
                        "B) WBC casts with hematuria indicating glomerulonephritis",
                        "C) Positive nitrite with few epithelial cells only",
                        "D) Many squamous epithelial cells with mixed flora",
                    ],
                    "answer": "D) Many squamous epithelial cells with mixed flora",
                    "explanation": "Clean-catch midstream urine contaminated by periurethral flora often shows abundant squamous epithelial cells and mixed organisms. True UTI more often shows pyuria with a predominant uropathogen. Recollection with better technique may be needed before treating mixed cultures.",
                    "choice_explanations": {
                        "A": "A pure uropathogen at ≥10^5 CFU/mL without squamous cells supports true bacteriuria more than contamination.",
                        "B": "WBC casts with hematuria suggest renal parenchymal/glomerular disease, not periurethral contamination of a clean-catch.",
                        "C": "Positive nitrite with few epithelial cells can support Enterobacterales UTI rather than heavy squamous contamination.",
                        "D": "Abundant squamous epithelial cells with mixed flora indicate periurethral/skin contamination of a clean-catch midstream urine specimen.",
                    },
                },
            ],
        },
        "cases": {
            "easy": [
                {
                    "title": "Dipstick Nitrite Positive",
                    "stem": "Dysuria; nitrite+/LE+.",
                    "question": "Suggests?",
                    "answer": "Possible UTI — correlate culture.",
                    "discussion": "Not all organisms reduce nitrate.",
                    "book_hint": "Urinalysis and Body Fluids — Strasinger",
                },
            ],
            "medium": [
                {
                    "title": "Tea-Colored Urine + RBC Casts",
                    "stem": "Hypertension, edema.",
                    "question": "Point to?",
                    "answer": "Glomerulonephritis workup — report casts clearly.",
                    "discussion": "Urgent clinical correlation.",
                    "book_hint": "Urinalysis and Body Fluids — Strasinger",
                },
            ],
            "hard": [
                {
                    "title": "Traumatic Tap vs SAH",
                    "stem": "CSF bloody; question xanthochromia. Choose the safest high-yield next laboratory concept.",
                    "question": "Approach?",
                    "answer": "Compare tubes, centrifuge supernatant, timing since onset; communicate uncertainty.",
                    "discussion": "Do not overcall.",
                    "book_hint": "Urinalysis and Body Fluids — Strasinger",
                },
            ],
            "extreme": [
                {
                    "title": "Unexpected Malignant Cells in Fluid",
                    "stem": "Cytotech sees atypical cells in pleural fluid count specimen. Avoid reporting or actions that could harm if a critical quality risk remains open.",
                    "question": "Action?",
                    "answer": "Flag for pathologist/cytology review urgently; notify clinical team per policy.",
                    "discussion": "Do not release as 'normal count' only.",
                    "book_hint": "Urinalysis and Body Fluids — Strasinger",
                },
            ],
        },
    },
}

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
    """Shuffle A–D so the correct letter is not predictable from position."""
    options = list(item.get("options") or [])
    if len(options) < 2:
        return dict(item)
    bodies = [_option_body(o) for o in options]
    correct_body = _option_body(item.get("answer", ""))
    order = list(range(len(bodies)))
    random.shuffle(order)
    letters = "ABCD"
    new_options = []
    new_answer = item.get("answer")
    for i, idx in enumerate(order):
        letter = letters[i]
        text = f"{letter}) {bodies[idx]}"
        new_options.append(text)
        if bodies[idx] == correct_body:
            new_answer = text
    out = dict(item)
    out["options"] = new_options
    out["answer"] = new_answer
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
