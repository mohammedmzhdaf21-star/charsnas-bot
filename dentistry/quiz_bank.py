"""Difficulty-tiered MCQs and cases for undergraduate dentistry specialties."""
from __future__ import annotations

DIFFICULTIES = ["easy", "medium", "hard", "extreme"]

DIFFICULTY_LABELS = {
    "easy": "Easy",
    "medium": "Medium",
    "hard": "Hard",
    "extreme": "Extreme",
}

LABEL_TO_DIFFICULTY = {v: k for k, v in DIFFICULTY_LABELS.items()}

QUIZ_BANK: dict[str, dict] = {'oral_surgery': {'easy': {'questions': [{'question': 'Most common impacted tooth?',
                                          'options': ['A) Maxillary canine',
                                                      'B) Mandibular third molar',
                                                      'C) Lateral incisor',
                                                      'D) First premolar'],
                                          'answer': 'B) Mandibular third molar',
                                          'explanation': 'Wisdom teeth are most often impacted.'},
                                         {'question': 'Local anesthetic for inferior alveolar '
                                                      'nerve typically targets?',
                                          'options': ['A) Mental foramen only',
                                                      'B) Mandibular foramen region',
                                                      'C) Infraorbital foramen only',
                                                      'D) Greater palatine only'],
                                          'answer': 'B) Mandibular foramen region',
                                          'explanation': 'IANB near mandibular foramen.'},
                                         {'question': 'Dry socket usually occurs after?',
                                          'options': ['A) Difficult extraction, especially lower '
                                                      'molars',
                                                      'B) Only fluoride varnish',
                                                      'C) Only scaling',
                                                      'D) Orthodontic bonding'],
                                          'answer': 'A) Difficult extraction, especially lower '
                                                    'molars',
                                          'explanation': 'Alveolar osteitis after clot loss.'}],
                           'cases': [{'title': 'Pain Day 3 After Extraction',
                                      'stem': 'A 24-year-old has severe pain 3 days after lower '
                                              'wisdom tooth removal. Socket looks empty; no pus or '
                                              'fever.',
                                      'question': 'Likely diagnosis?',
                                      'answer': 'Alveolar osteitis (dry socket).',
                                      'discussion': 'Irrigate, medicated dressing, analgesia; '
                                                    'antibiotics usually not first-line if no '
                                                    'infection.',
                                      'book_hint': "Peterson's Principles of Oral and "
                                                   'Maxillofacial Surgery'}]},
                  'medium': {'questions': [{'question': 'Ludwig angina is infection of?',
                                            'options': ['A) Bilateral '
                                                        'submandibular/sublingual/submental spaces',
                                                        'B) Only maxillary sinus',
                                                        'C) Only pulp chamber',
                                                        'D) Only TMJ capsule'],
                                            'answer': 'A) Bilateral '
                                                      'submandibular/sublingual/submental spaces',
                                            'explanation': 'Airway-threatening floor-of-mouth '
                                                           'infection.'},
                                           {'question': 'INR is most relevant before surgery in '
                                                        'patients on?',
                                            'options': ['A) Warfarin',
                                                        'B) Amoxicillin only',
                                                        'C) Paracetamol only',
                                                        'D) Chlorhexidine only'],
                                            'answer': 'A) Warfarin',
                                            'explanation': 'Check coagulation risk with '
                                                           'anticoagulant therapy.'},
                                           {'question': 'Oroantral communication risk is highest '
                                                        'extracting?',
                                            'options': ['A) Maxillary molars',
                                                        'B) Lower incisors',
                                                        'C) Mandibular canines',
                                                        'D) Lower premolars always'],
                                            'answer': 'A) Maxillary molars',
                                            'explanation': 'Close relation to maxillary sinus.'}],
                             'cases': [{'title': 'Fever + Floor of Mouth Swelling',
                                        'stem': 'A patient after dental infection has bilateral '
                                                'floor-of-mouth swelling, drooling, and tongue '
                                                'elevation.',
                                        'question': 'Emergency concern?',
                                        'answer': 'Ludwig angina — secure airway and urgent '
                                                  'surgical/medical care.',
                                        'discussion': 'Do not delay for routine dental clinic '
                                                      'care.',
                                        'book_hint': "Peterson's Principles of Oral and "
                                                     'Maxillofacial Surgery'}]},
                  'hard': {'questions': [{'question': 'A junior colleague asks for the single best '
                                                      'answer. Which nerve injury risk is notable '
                                                      'in third molar surgery near the canal? '
                                                      'Beware of near-miss distractors.',
                                          'options': ['A) Inferior alveolar nerve',
                                                      'B) Optic nerve',
                                                      'C) Phrenic nerve',
                                                      'D) Recurrent laryngeal only'],
                                          'answer': 'A) Inferior alveolar nerve',
                                          'explanation': 'CBCT/risk assessment when indicated.'},
                                         {'question': 'A junior colleague asks for the single best '
                                                      'answer. Bisphosphonate-related '
                                                      'osteonecrosis risk rises with? Beware of '
                                                      'near-miss distractors.',
                                          'options': ['A) Invasive dental surgery in at-risk '
                                                      'patients',
                                                      'B) Topical fluoride alone',
                                                      'C) Routine prophylaxis always',
                                                      'D) Orthodontic retainers only'],
                                          'answer': 'A) Invasive dental surgery in at-risk '
                                                    'patients',
                                          'explanation': 'MRONJ risk counseling.'},
                                         {'question': 'A junior colleague asks for the single best '
                                                      'answer. Displaced root into sinus needs? '
                                                      'Beware of near-miss distractors.',
                                          'options': ['A) Retrieval strategy ± sinus '
                                                      'precautions/referral',
                                                      'B) Ignore forever',
                                                      'C) Only mouth rinse',
                                                      'D) Immediate RCT of adjacent tooth only'],
                                          'answer': 'A) Retrieval strategy ± sinus '
                                                    'precautions/referral',
                                          'explanation': 'Prevent sinusitis/oroantral fistula.'}],
                           'cases': [{'title': 'Root Tip Disappears Upward',
                                      'stem': 'During upper 6 extraction, a root tip vanishes and '
                                              'the patient feels air/fluid in the nose when '
                                              'drinking. Choose the safest high-yield next concept '
                                              'before definitive results.',
                                      'question': 'What happened conceptually?',
                                      'answer': 'Oroantral communication ± displaced root — stop '
                                                'forcing, assess, arrange appropriate '
                                                'closure/retrieval.',
                                      'discussion': 'Sinus precautions and follow-up are '
                                                    'essential.',
                                      'book_hint': "Peterson's Principles of Oral and "
                                                   'Maxillofacial Surgery'}]},
                  'extreme': {'questions': [{'question': 'In a high-stakes clinic scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? A anticoagulated patient needs '
                                                         'urgent extraction with high bleed risk. '
                                                         'Best concept? Avoid therapies that could '
                                                         'harm if a critical differential remains '
                                                         'open.',
                                             'options': ['A) Coordinate physician guidance; local '
                                                         'hemostasis measures; do not stop '
                                                         'anticoagulants blindly',
                                                         'B) Always stop all anticoagulants '
                                                         'yourself without advice',
                                                         'C) Never extract under any circumstance',
                                                         'D) Only give vitamin K routinely without '
                                                         'assessment'],
                                             'answer': 'A) Coordinate physician guidance; local '
                                                       'hemostasis measures; do not stop '
                                                       'anticoagulants blindly',
                                             'explanation': 'Balance thrombosis vs bleeding.'},
                                            {'question': 'In a high-stakes clinic scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? Post-op expanding neck hematoma '
                                                         'with stridor means? Avoid therapies that '
                                                         'could harm if a critical differential '
                                                         'remains open.',
                                             'options': ['A) Airway emergency first',
                                                         'B) Only prescribe antibiotics at home',
                                                         'C) Wait overnight always',
                                                         'D) Only ice and observe without '
                                                         'assessment'],
                                             'answer': 'A) Airway emergency first',
                                             'explanation': 'Return to theater/emergency pathway.'},
                                            {'question': 'In a high-stakes clinic scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? Osteoradionecrosis risk is '
                                                         'linked to? Avoid therapies that could '
                                                         'harm if a critical differential remains '
                                                         'open.',
                                             'options': ['A) Extractions in previously irradiated '
                                                         'jaws',
                                                         'B) Only deciduous exfoliation',
                                                         'C) Only sealants',
                                                         'D) Only whitening trays'],
                                             'answer': 'A) Extractions in previously irradiated '
                                                       'jaws',
                                             'explanation': 'Specialist pathways / HBO discussions '
                                                            'vary by protocol.'}],
                              'cases': [{'title': 'Irradiated Jaw Needs Extraction',
                                         'stem': 'A head-and-neck cancer survivor with prior '
                                                 'radiotherapy needs a painful molar extraction in '
                                                 'the irradiated field. Avoid harmful premature '
                                                 'treatment while catastrophic differentials '
                                                 'remain open.',
                                         'question': 'Key concept?',
                                         'answer': 'High ORN risk — specialist OMFS planning, '
                                                   'atraumatic technique, infection control, and '
                                                   'protocolized prevention.',
                                         'discussion': 'Never treat as a routine extraction.',
                                         'book_hint': "Peterson's Principles of Oral and "
                                                      'Maxillofacial Surgery'}]}},
 'orthodontics': {'easy': {'questions': [{'question': 'Angle Class II molar relation means?',
                                          'options': ['A) Lower molar distal to normal vs upper',
                                                      'B) Lower molar mesial to Class I',
                                                      'C) Only open bite',
                                                      'D) Only crossbite'],
                                          'answer': 'A) Lower molar distal to normal vs upper',
                                          'explanation': 'Class II: mesiobuccal cusp of upper 6 '
                                                         'ahead relative to lower groove.'},
                                         {'question': 'Overjet describes?',
                                          'options': ['A) Horizontal overlap of incisors',
                                                      'B) Vertical overlap only',
                                                      'C) Only molar torque',
                                                      'D) Only arch length'],
                                          'answer': 'A) Horizontal overlap of incisors',
                                          'explanation': 'Overbite is vertical.'},
                                         {'question': 'Space maintainer is used when?',
                                          'options': ['A) Premature loss of primary teeth risks '
                                                      'space loss',
                                                      'B) Only adult periodontitis',
                                                      'C) Only bleaching',
                                                      'D) Only pulp capping'],
                                          'answer': 'A) Premature loss of primary teeth risks '
                                                    'space loss',
                                          'explanation': 'Preserve arch length.'}],
                           'cases': [{'title': 'Crowding in Teen',
                                      'stem': 'A 14-year-old has moderate crowding and Class I '
                                              'molars. Oral hygiene is good.',
                                      'question': 'First planning idea?',
                                      'answer': 'Comprehensive orthodontic assessment (records, '
                                                'growth, hygiene).',
                                      'discussion': 'Treatment options depend on space analysis.',
                                      'book_hint': "Proffit's Contemporary Orthodontics"}]},
                  'medium': {'questions': [{'question': 'Crossbite with functional shift suggests?',
                                            'options': ['A) Possible premature contact / occlusal '
                                                        'interference',
                                                        'B) Only random habit',
                                                        'C) Only caries',
                                                        'D) Only fluorosis'],
                                            'answer': 'A) Possible premature contact / occlusal '
                                                      'interference',
                                            'explanation': 'Eliminate interference early when '
                                                           'indicated.'},
                                           {'question': 'Anchorage in ortho means?',
                                            'options': ['A) Resistance to unwanted tooth movement',
                                                        'B) Only wire size',
                                                        'C) Only bracket color',
                                                        'D) Only elastic flavor'],
                                            'answer': 'A) Resistance to unwanted tooth movement',
                                            'explanation': 'Critical for controlled mechanics.'},
                                           {'question': 'Thumb sucking prolonged may cause?',
                                            'options': ['A) Open bite / proclined upper incisors',
                                                        'B) Only dens invaginatus',
                                                        'C) Only enamel pearl',
                                                        'D) Only tori'],
                                            'answer': 'A) Open bite / proclined upper incisors',
                                            'explanation': 'Habit counseling timing matters.'}],
                             'cases': [{'title': 'Anterior Crossbite Child',
                                        'stem': 'An 8-year-old has one upper incisor in crossbite '
                                                'with a shift on closing.',
                                        'question': 'Concern?',
                                        'answer': 'Functional shift from interference — early '
                                                  'correction often indicated.',
                                        'discussion': 'Prevent asymmetric growth habits.',
                                        'book_hint': "Proffit's Contemporary Orthodontics"}]},
                  'hard': {'questions': [{'question': 'A junior colleague asks for the single best '
                                                      'answer. Root resorption risk in ortho '
                                                      'increases with? Beware of near-miss '
                                                      'distractors.',
                                          'options': ['A) Heavy prolonged forces / certain tooth '
                                                      'vulnerabilities',
                                                      'B) Only toothpaste brand',
                                                      'C) Only flossing',
                                                      'D) Only mouthwash'],
                                          'answer': 'A) Heavy prolonged forces / certain tooth '
                                                    'vulnerabilities',
                                          'explanation': 'Monitor radiographically as indicated.'},
                                         {'question': 'A junior colleague asks for the single best '
                                                      'answer. Serial extraction concept is? '
                                                      'Beware of near-miss distractors.',
                                          'options': ['A) Guided extraction sequence in severe '
                                                      'crowding mixed dentition',
                                                      'B) Extracting all wisdom teeth only',
                                                      'C) Only RCT series',
                                                      'D) Only scaling sessions'],
                                          'answer': 'A) Guided extraction sequence in severe '
                                                    'crowding mixed dentition',
                                          'explanation': 'Specialist decision.'},
                                         {'question': 'A junior colleague asks for the single best '
                                                      'answer. TADs provide? Beware of near-miss '
                                                      'distractors.',
                                          'options': ['A) Skeletal anchorage',
                                                      'B) Only fluoride release',
                                                      'C) Only bleaching',
                                                      'D) Only anesthesia'],
                                          'answer': 'A) Skeletal anchorage',
                                          'explanation': 'Temporary anchorage devices.'}],
                           'cases': [{'title': 'Adult Relapse After Retainers Lost',
                                      'stem': 'A 28-year-old stopped wearing retainers and '
                                              'crowding returned. Choose the safest high-yield '
                                              'next concept before definitive results.',
                                      'question': 'Teaching point?',
                                      'answer': 'Relapse risk is lifelong for many; retention is '
                                                'part of treatment.',
                                      'discussion': 'Discuss retreatment vs limited alignment.',
                                      'book_hint': "Proffit's Contemporary Orthodontics"}]},
                  'extreme': {'questions': [{'question': 'In a high-stakes clinic scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? Ortho in severe periodontitis '
                                                         'patient requires? Avoid therapies that '
                                                         'could harm if a critical differential '
                                                         'remains open.',
                                             'options': ['A) Disease control first; light forces; '
                                                         'perio co-management',
                                                         'B) Immediate heavy expansion always',
                                                         'C) Ignore bone levels',
                                                         'D) Only extract all teeth first always'],
                                             'answer': 'A) Disease control first; light forces; '
                                                       'perio co-management',
                                             'explanation': 'Moving teeth in uncontrolled perio '
                                                            'worsens attachment loss.'},
                                            {'question': 'In a high-stakes clinic scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? Impacted canine close to roots '
                                                         '— risk of? Avoid therapies that could '
                                                         'harm if a critical differential remains '
                                                         'open.',
                                             'options': ['A) Root resorption of adjacent incisors',
                                                         'B) Only freckles',
                                                         'C) Only geographic tongue',
                                                         'D) Only hairy tongue'],
                                             'answer': 'A) Root resorption of adjacent incisors',
                                             'explanation': 'CBCT when indicated; timely '
                                                            'exposure/traction.'},
                                            {'question': 'In a high-stakes clinic scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? Surgical vs camouflage Class '
                                                         'III decision weighs? Avoid therapies '
                                                         'that could harm if a critical '
                                                         'differential remains open.',
                                             'options': ['A) Growth status, severity, profile, '
                                                         'occlusion',
                                                         'B) Only bracket brand',
                                                         'C) Only wire alloy',
                                                         'D) Only appointment time'],
                                             'answer': 'A) Growth status, severity, profile, '
                                                       'occlusion',
                                             'explanation': 'Orthognathic pathway when skeletal '
                                                            'severe.'}],
                              'cases': [{'title': 'Growing Class III with Functional Shift',
                                         'stem': 'A child with developing Class III has an '
                                                 'edge-to-edge bite and a shift. Parents want '
                                                 'braces immediately. Avoid harmful premature '
                                                 'treatment while catastrophic differentials '
                                                 'remain open.',
                                         'question': 'Concept?',
                                         'answer': 'Distinguish pseudo-Class III / shift from true '
                                                   'skeletal Class III; growth modification timing '
                                                   'and differential diagnosis matter before '
                                                   'irreversible camouflage.',
                                         'discussion': 'Wrong early extraction plans can harm.',
                                         'book_hint': "Proffit's Contemporary Orthodontics"}]}},
 'periodontics': {'easy': {'questions': [{'question': 'Main cause of plaque-induced gingivitis?',
                                          'options': ['A) Dental biofilm',
                                                      'B) Only malocclusion',
                                                      'C) Only dens evaginatus',
                                                      'D) Only torus palatinus'],
                                          'answer': 'A) Dental biofilm',
                                          'explanation': 'Remove plaque → gingivitis resolves.'},
                                         {'question': 'Clinical hallmark of periodontitis vs '
                                                      'gingivitis?',
                                          'options': ['A) Clinical attachment loss / bone loss',
                                                      'B) Only reversible redness forever without '
                                                      'loss',
                                                      'C) Only stain',
                                                      'D) Only calculus without inflammation ever'],
                                          'answer': 'A) Clinical attachment loss / bone loss',
                                          'explanation': 'True periodontitis destroys attachment.'},
                                         {'question': 'Best daily plaque control tool foundation?',
                                          'options': ['A) Toothbrushing ± interdental cleaning',
                                                      'B) Only whitening strips',
                                                      'C) Only chewing ice',
                                                      'D) Only charcoal powder alone'],
                                          'answer': 'A) Toothbrushing ± interdental cleaning',
                                          'explanation': 'Mechanical disruption of biofilm.'}],
                           'cases': [{'title': 'Bleeding Gums',
                                      'stem': 'A student has bleeding on brushing, soft swollen '
                                              'gingiva, no radiographic bone loss.',
                                      'question': 'Diagnosis?',
                                      'answer': 'Plaque-induced gingivitis.',
                                      'discussion': 'OHI and prophylaxis; reversible.',
                                      'book_hint': "Carranza's Clinical Periodontology"}]},
                  'medium': {'questions': [{'question': 'Furcation involvement is assessed on?',
                                            'options': ['A) Multirooted teeth',
                                                        'B) Only incisors',
                                                        'C) Only canines',
                                                        'D) Only primary laterals'],
                                            'answer': 'A) Multirooted teeth',
                                            'explanation': 'Nabers probe themes.'},
                                           {'question': 'Smoking effect on perio?',
                                            'options': ['A) Increases risk/severity; masks '
                                                        'bleeding',
                                                        'B) Protects attachment always',
                                                        'C) Only whitens naturally',
                                                        'D) No effect'],
                                            'answer': 'A) Increases risk/severity; masks bleeding',
                                            'explanation': 'Major modifiable risk.'},
                                           {'question': 'Aggressive/grade C young patient theme '
                                                        'includes?',
                                            'options': ['A) Rapid attachment loss often with A. '
                                                        'actinomycetemcomitans historically '
                                                        'discussed',
                                                        'B) Only fluorosis',
                                                        'C) Only attrition',
                                                        'D) Only abrasion'],
                                            'answer': 'A) Rapid attachment loss often with A. '
                                                      'actinomycetemcomitans historically '
                                                      'discussed',
                                            'explanation': 'Early diagnosis critical.'}],
                             'cases': [{'title': 'Deep Pockets Molars',
                                        'stem': 'A 45-year-old smoker has 6–7 mm pockets on molars '
                                                'with horizontal bone loss.',
                                        'question': 'Management pillars?',
                                        'answer': 'Risk factor control, nonsurgical debridement, '
                                                  're-evaluation, surgery if indicated.',
                                        'discussion': 'Smoking cessation counseling.',
                                        'book_hint': "Carranza's Clinical Periodontology"}]},
                  'hard': {'questions': [{'question': 'A junior colleague asks for the single best '
                                                      'answer. Periodontal abscess urgent care '
                                                      'includes? Beware of near-miss distractors.',
                                          'options': ['A) Drainage + debridement + antimicrobials '
                                                      'if systemic signs',
                                                      'B) Only bleach tray',
                                                      'C) Only ortho wax',
                                                      'D) Only nightguard forever'],
                                          'answer': 'A) Drainage + debridement + antimicrobials if '
                                                    'systemic signs',
                                          'explanation': 'Relieve acute infection.'},
                                         {'question': 'A junior colleague asks for the single best '
                                                      'answer. Implant peri-implantitis features? '
                                                      'Beware of near-miss distractors.',
                                          'options': ['A) Inflammation + progressive bone loss '
                                                      'around implant',
                                                      'B) Only soft tissue blush without bone loss '
                                                      'always mucositis',
                                                      'C) Only food impaction without inflammation',
                                                      'D) Only shade mismatch'],
                                          'answer': 'A) Inflammation + progressive bone loss '
                                                    'around implant',
                                          'explanation': 'Different from mucositis.'},
                                         {'question': 'A junior colleague asks for the single best '
                                                      'answer. Occlusal trauma alone without '
                                                      'inflammation? Beware of near-miss '
                                                      'distractors.',
                                          'options': ['A) Does not initiate periodontitis plaque '
                                                      'pathway',
                                                      'B) Always causes vertical defects alone as '
                                                      'sole cause',
                                                      'C) Cures pockets',
                                                      'D) Replaces brushing'],
                                          'answer': 'A) Does not initiate periodontitis plaque '
                                                    'pathway',
                                          'explanation': 'Co-destructive when inflammation '
                                                         'present.'}],
                           'cases': [{'title': 'Diabetic with Recurrent Abscesses',
                                      'stem': 'Poorly controlled diabetes, multiple periodontal '
                                              'abscesses, deep pockets. Choose the safest '
                                              'high-yield next concept before definitive results.',
                                      'question': 'Priority concept?',
                                      'answer': 'Medical coordination for glycemic control + acute '
                                                'drainage/debridement + definitive perio plan.',
                                      'discussion': 'Diabetes and perio bidirectionally interact.',
                                      'book_hint': "Carranza's Clinical Periodontology"}]},
                  'extreme': {'questions': [{'question': 'In a high-stakes clinic scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? Necrotizing ulcerative '
                                                         'gingivitis classic triad? Avoid '
                                                         'therapies that could harm if a critical '
                                                         'differential remains open.',
                                             'options': ['A) Pain, bleeding, interdental necrosis '
                                                         '± fetor',
                                                         'B) Only asymptomatic stain',
                                                         'C) Only dens in dente',
                                                         'D) Only peg laterals'],
                                             'answer': 'A) Pain, bleeding, interdental necrosis ± '
                                                       'fetor',
                                             'explanation': 'Stress/smoking/immunodeficiency '
                                                            'associations.'},
                                            {'question': 'In a high-stakes clinic scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? Pregnancy epulis is? Avoid '
                                                         'therapies that could harm if a critical '
                                                         'differential remains open.',
                                             'options': ['A) Pyogenic granuloma variant; often '
                                                         'regresses postpartum',
                                                         'B) Always malignant melanoma',
                                                         'C) Always needs radiation',
                                                         'D) Always caries'],
                                             'answer': 'A) Pyogenic granuloma variant; often '
                                                       'regresses postpartum',
                                             'explanation': 'Manage gently; definitive if needed.'},
                                            {'question': 'In a high-stakes clinic scenario with '
                                                         'incomplete data, which statement is MOST '
                                                         'correct? Guided tissue regeneration aims '
                                                         'for? Avoid therapies that could harm if '
                                                         'a critical differential remains open.',
                                             'options': ['A) New attachment apparatus regeneration',
                                                         'B) Only stain removal',
                                                         'C) Only enamel microabrasion',
                                                         'D) Only bleaching'],
                                             'answer': 'A) New attachment apparatus regeneration',
                                             'explanation': 'Membrane/barrier concepts.'}],
                              'cases': [{'title': 'NUG in Stressed Student',
                                         'stem': 'A stressed young adult smoker has punched-out '
                                                 'papillae, severe pain, and fetor oris. Avoid '
                                                 'harmful premature treatment while catastrophic '
                                                 'differentials remain open.',
                                         'question': 'Diagnosis and first care?',
                                         'answer': 'NUG — gentle debridement, OHI, antiseptics, '
                                                   'address risk factors; antibiotics if '
                                                   'systemic/immunocompromise.',
                                         'discussion': 'Rule out HIV/other immunodeficiency when '
                                                       'atypical.',
                                         'book_hint': "Carranza's Clinical Periodontology"}]}},
 'endodontics': {'easy': {'questions': [{'question': 'Irreversible pulpitis pain is often?',
                                         'options': ['A) Spontaneous / lingering to cold',
                                                     'B) Only brief to sweet always reversible',
                                                     'C) Only itching',
                                                     'D) Only TMJ click'],
                                         'answer': 'A) Spontaneous / lingering to cold',
                                         'explanation': 'Classic symptomatic irreversible '
                                                        'pulpitis.'},
                                        {'question': 'Best isolation for RCT?',
                                         'options': ['A) Rubber dam',
                                                     'B) Cotton only forever',
                                                     'C) No isolation',
                                                     'D) Only cheek retractor'],
                                         'answer': 'A) Rubber dam',
                                         'explanation': 'Standard of care.'},
                                        {'question': 'Working length aims to prepare to?',
                                         'options': ['A) Near apical constriction / radiographic '
                                                     'apex protocols',
                                                     'B) Beyond bone into sinus always',
                                                     'C) Only to pulp horn',
                                                     'D) Only CEJ'],
                                         'answer': 'A) Near apical constriction / radiographic '
                                                   'apex protocols',
                                         'explanation': 'Avoid overinstrumentation.'}],
                          'cases': [{'title': 'Night Pain Lower Molar',
                                     'stem': 'Spontaneous night pain, lingering cold response, no '
                                             'periapical radiolucency yet.',
                                     'question': 'Likely pulp status?',
                                     'answer': 'Symptomatic irreversible pulpitis.',
                                     'discussion': 'RCT or extraction after consent.',
                                     'book_hint': "Cohen's Pathways of the Pulp"}]},
                 'medium': {'questions': [{'question': 'Necrotic pulp with apical radiolucency '
                                                       'suggests?',
                                           'options': ['A) Apical periodontitis',
                                                       'B) Only reversible pulpitis',
                                                       'C) Only enamel hypoplasia',
                                                       'D) Only fluorosis'],
                                           'answer': 'A) Apical periodontitis',
                                           'explanation': 'Endodontic infection pathway.'},
                                          {'question': 'NaOCl is used as?',
                                           'options': ['A) Irrigant with '
                                                       'tissue-dissolving/antimicrobial action',
                                                       'B) Obturation sealer only',
                                                       'C) Temporary filling only',
                                                       'D) Local anesthetic'],
                                           'answer': 'A) Irrigant with '
                                                     'tissue-dissolving/antimicrobial action',
                                           'explanation': 'Careful to avoid extrusion.'},
                                          {'question': 'Cracked tooth pain often on?',
                                           'options': ['A) Release of biting pressure',
                                                       'B) Only hot coffee forever without bite',
                                                       'C) Only when lying flat without bite',
                                                       'D) Only to percussion of adjacent tooth '
                                                       'always'],
                                           'answer': 'A) Release of biting pressure',
                                           'explanation': 'Bite test helpful.'}],
                            'cases': [{'title': 'Sinus Tract on Gingiva',
                                       'stem': 'Chronic draining sinus over apex of nonvital '
                                               'lateral; radiolucency present.',
                                       'question': 'Treatment concept?',
                                       'answer': 'Root canal therapy of the source tooth (+ '
                                                 'restore).',
                                       'discussion': 'Trace sinus with gutta-percha if needed.',
                                       'book_hint': "Cohen's Pathways of the Pulp"}]},
                 'hard': {'questions': [{'question': 'A junior colleague asks for the single best '
                                                     'answer. NaOCl accident presents with? Beware '
                                                     'of near-miss distractors.',
                                         'options': ['A) Sudden pain, swelling, ecchymosis after '
                                                     'irrigation',
                                                     'B) Only mild stain',
                                                     'C) Only temporary numbness forever benign '
                                                     'always',
                                                     'D) Only taste change'],
                                         'answer': 'A) Sudden pain, swelling, ecchymosis after '
                                                   'irrigation',
                                         'explanation': 'Stop, cold packs, steroids/analgesia '
                                                        'pathways, follow closely.'},
                                        {'question': 'A junior colleague asks for the single best '
                                                     'answer. Missed second mesiobuccal canal '
                                                     '(MB2) in upper molars causes? Beware of '
                                                     'near-miss distractors.',
                                         'options': ['A) Persistent infection/failure risk',
                                                     'B) Only better prognosis always',
                                                     'C) Only color change of face',
                                                     'D) Only gingival hyperplasia'],
                                         'answer': 'A) Persistent infection/failure risk',
                                         'explanation': 'Know MB2 prevalence.'},
                                        {'question': 'A junior colleague asks for the single best '
                                                     'answer. Vertical root fracture prognosis is '
                                                     'often? Beware of near-miss distractors.',
                                         'options': ['A) Poor; extraction commonly',
                                                     'B) Always heal with RCT alone',
                                                     'C) Always ignore',
                                                     'D) Always bleach'],
                                         'answer': 'A) Poor; extraction commonly',
                                         'explanation': 'Especially if complete VRF.'}],
                          'cases': [{'title': 'RCT Done but Pain Persists',
                                     'stem': 'Upper 6 had RCT; pain on biting persists; J-shaped '
                                             'lesion on root. Choose the safest high-yield next '
                                             'concept before definitive results.',
                                     'question': 'Suspect?',
                                     'answer': 'Vertical root fracture or missed canal / '
                                               'perio-endo complex — investigate carefully.',
                                     'discussion': 'CBCT may help; avoid endless retreat without '
                                                   'diagnosis.',
                                     'book_hint': "Cohen's Pathways of the Pulp"}]},
                 'extreme': {'questions': [{'question': 'In a high-stakes clinic scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Avulsed permanent tooth '
                                                        'extraoral dry time >60 min concept? Avoid '
                                                        'therapies that could harm if a critical '
                                                        'differential remains open.',
                                            'options': ['A) Poor PDL viability; prognosis '
                                                        'worsened; manage per guidelines',
                                                        'B) Perfect prognosis always',
                                                        'C) Replant never considered',
                                                        'D) Only primary tooth rules identical '
                                                        'always'],
                                            'answer': 'A) Poor PDL viability; prognosis worsened; '
                                                      'manage per guidelines',
                                            'explanation': 'Follow IADT guidelines.'},
                                           {'question': 'In a high-stakes clinic scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Combined perio-endo lesion '
                                                        'needs? Avoid therapies that could harm if '
                                                        'a critical differential remains open.',
                                            'options': ['A) Address both endodontic and '
                                                        'periodontal components',
                                                        'B) Only scaling forever without pulp test',
                                                        'C) Only ortho',
                                                        'D) Only whitening'],
                                            'answer': 'A) Address both endodontic and periodontal '
                                                      'components',
                                            'explanation': 'Sequence often endo first if primary '
                                                           'endo.'},
                                           {'question': 'In a high-stakes clinic scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Internal resorption vs external? '
                                                        'Avoid therapies that could harm if a '
                                                        'critical differential remains open.',
                                            'options': ['A) Different radiographic/clinical '
                                                        'patterns; treatment differs',
                                                        'B) Always same disease',
                                                        'C) Always ignore',
                                                        'D) Always extract without diagnosis'],
                                            'answer': 'A) Different radiographic/clinical '
                                                      'patterns; treatment differs',
                                            'explanation': 'CBCT useful.'}],
                             'cases': [{'title': 'Avulsion on Sports Field',
                                        'stem': 'A 12-year-old avulses a permanent central; tooth '
                                                'was dry in a napkin for 90 minutes. Avoid harmful '
                                                'premature treatment while catastrophic '
                                                'differentials remain open.',
                                        'question': 'Guideline concept?',
                                        'answer': 'Extraoral dry time long → poor PDL prognosis; '
                                                  'still follow IADT: clean carefully, consider '
                                                  'replantation/splinting protocols, '
                                                  'antibiotics/tetanus as indicated, close '
                                                  'follow-up.',
                                        'discussion': 'Do not scrub the root PDL remnant.',
                                        'book_hint': "Cohen's Pathways of the Pulp"}]}},
 'prosthodontics': {'easy': {'questions': [{'question': 'Ferrule effect improves?',
                                            'options': ['A) Fracture resistance of crowned '
                                                        'endodontically treated teeth',
                                                        'B) Only shade matching',
                                                        'C) Only cement color',
                                                        'D) Only tray adhesive'],
                                            'answer': 'A) Fracture resistance of crowned '
                                                      'endodontically treated teeth',
                                            'explanation': '2 mm ferrule ideal theme.'},
                                           {'question': 'Kennedy Class I RPD is?',
                                            'options': ['A) Bilateral distal extension',
                                                        'B) Single tooth gap only',
                                                        'C) Only anterior bounded',
                                                        'D) Only full denture'],
                                            'answer': 'A) Bilateral distal extension',
                                            'explanation': 'Support differs from tooth-borne.'},
                                           {'question': 'Impression for crowns needs?',
                                            'options': ['A) Accurate margins and soft tissue '
                                                        'management',
                                                        'B) Only alginate always for final PFM',
                                                        'C) Only wax bite forever',
                                                        'D) Only shade tab photo'],
                                            'answer': 'A) Accurate margins and soft tissue '
                                                      'management',
                                            'explanation': 'Quality impression = quality crown.'}],
                             'cases': [{'title': 'Broken Molar Crown',
                                        'stem': 'A patient wants a crown on a root-filled molar '
                                                'with adequate ferrule.',
                                        'question': 'Plan outline?',
                                        'answer': 'Assess restorability, post if needed, core, '
                                                  'crown.',
                                        'discussion': 'Extract if unrestorable.',
                                        'book_hint': 'Contemporary Fixed Prosthodontics — '
                                                     'Rosenstiel'}]},
                    'medium': {'questions': [{'question': 'Biological width violation may cause?',
                                              'options': ['A) Chronic inflammation / bone loss',
                                                          'B) Only better papilla',
                                                          'C) Only faster ortho',
                                                          'D) Only whitening'],
                                              'answer': 'A) Chronic inflammation / bone loss',
                                              'explanation': 'Respect supracrestal tissues.'},
                                             {'question': 'Implant vs tooth abutment key '
                                                          'difference?',
                                              'options': ['A) No PDL proprioception/same mobility '
                                                          'profile',
                                                          'B) Identical biomechanics always',
                                                          'C) Implants never fail',
                                                          'D) Teeth never fail'],
                                              'answer': 'A) No PDL proprioception/same mobility '
                                                        'profile',
                                              'explanation': 'Occlusion planning differs.'},
                                             {'question': 'Immediate denture is delivered?',
                                              'options': ['A) At extraction appointment',
                                                          'B) Only after 2 years always',
                                                          'C) Only before any exam',
                                                          'D) Only for orthodontics'],
                                              'answer': 'A) At extraction appointment',
                                              'explanation': 'Interim esthetics/function.'}],
                               'cases': [{'title': 'Distal Extension RPD Rocks',
                                          'stem': 'Kennedy I lower RPD rocks and sore spots on '
                                                  'ridge.',
                                          'question': 'Likely issue?',
                                          'answer': 'Support/retention/occlusion imbalance on '
                                                    'distal extension — adjust base, rests, '
                                                    'occlusion.',
                                          'discussion': 'Tissue-borne areas need careful loading.',
                                          'book_hint': 'Contemporary Fixed Prosthodontics — '
                                                       'Rosenstiel'}]},
                    'hard': {'questions': [{'question': 'A junior colleague asks for the single '
                                                        'best answer. Cantilever bridge risks? '
                                                        'Beware of near-miss distractors.',
                                            'options': ['A) Leverage overload of abutments',
                                                        'B) Always safest design',
                                                        'C) Never fails',
                                                        'D) Only better than implants always'],
                                            'answer': 'A) Leverage overload of abutments',
                                            'explanation': 'Use cautiously.'},
                                           {'question': 'A junior colleague asks for the single '
                                                        'best answer. Retrievable cement-retained '
                                                        'implant crown advantage? Beware of '
                                                        'near-miss distractors.',
                                            'options': ['A) Cement margin control issues vs screw '
                                                        'access esthetics tradeoffs',
                                                        'B) No differences exist',
                                                        'C) Cement never excesses',
                                                        'D) Screw retained never loosens'],
                                            'answer': 'A) Cement margin control issues vs screw '
                                                      'access esthetics tradeoffs',
                                            'explanation': 'Excess cement → peri-implantitis '
                                                           'risk.'},
                                           {'question': 'A junior colleague asks for the single '
                                                        'best answer. Surveying an RPD cast '
                                                        'determines? Beware of near-miss '
                                                        'distractors.',
                                            'options': ['A) Path of insertion and undercuts',
                                                        'B) Only shade',
                                                        'C) Only patient age',
                                                        'D) Only bite force'],
                                            'answer': 'A) Path of insertion and undercuts',
                                            'explanation': 'Design clasps accordingly.'}],
                             'cases': [{'title': 'Deep Margin Near Bone',
                                        'stem': 'Crown prep finish line violates biologic width '
                                                'with persistent bleeding. Choose the safest '
                                                'high-yield next concept before definitive '
                                                'results.',
                                        'question': 'Options?',
                                        'answer': 'Crown lengthening or orthodontic extrusion '
                                                  'before final restoration.',
                                        'discussion': 'Do not cement and hope.',
                                        'book_hint': 'Contemporary Fixed Prosthodontics — '
                                                     'Rosenstiel'}]},
                    'extreme': {'questions': [{'question': 'In a high-stakes clinic scenario with '
                                                           'incomplete data, which statement is '
                                                           'MOST correct? Full-mouth rehab '
                                                           'sequence prioritizes? Avoid therapies '
                                                           'that could harm if a critical '
                                                           'differential remains open.',
                                               'options': ['A) Disease control, VDO/occlusion '
                                                           'plan, provisionalization, finals',
                                                           'B) Jump to zirconia without diagnosis',
                                                           'C) Only bleach first always',
                                                           'D) Extract all without consent'],
                                               'answer': 'A) Disease control, VDO/occlusion plan, '
                                                         'provisionalization, finals',
                                               'explanation': 'Provisional trial is critical.'},
                                              {'question': 'In a high-stakes clinic scenario with '
                                                           'incomplete data, which statement is '
                                                           'MOST correct? Combination syndrome '
                                                           'relates to? Avoid therapies that could '
                                                           'harm if a critical differential '
                                                           'remains open.',
                                               'options': ['A) Edentulous maxilla opposing '
                                                           'anterior mandibular teeth',
                                                           'B) Only Class III ortho',
                                                           'C) Only dens invaginatus',
                                                           'D) Only mesiodens'],
                                               'answer': 'A) Edentulous maxilla opposing anterior '
                                                         'mandibular teeth',
                                               'explanation': 'Bone resorption patterns.'},
                                              {'question': 'In a high-stakes clinic scenario with '
                                                           'incomplete data, which statement is '
                                                           'MOST correct? Passive fit of implant '
                                                           'framework means? Avoid therapies that '
                                                           'could harm if a critical differential '
                                                           'remains open.',
                                               'options': ['A) Seats without strain on implants',
                                                           'B) Forced seating is fine always',
                                                           'C) Only cement hides misfit forever '
                                                           'safely',
                                                           'D) Only shade matters'],
                                               'answer': 'A) Seats without strain on implants',
                                               'explanation': 'Misfit → screw/bone problems.'}],
                                'cases': [{'title': 'Failing Full Arch Hybrids',
                                           'stem': 'Multiple implant prostheses with screw '
                                                   'loosening, misfit, and peri-implant bone loss. '
                                                   'Avoid harmful premature treatment while '
                                                   'catastrophic differentials remain open.',
                                           'question': 'Concept?',
                                           'answer': 'Remove/replace passive fit, control '
                                                     'occlusion, treat peri-implant disease, '
                                                     'reassess biomechanics.',
                                           'discussion': 'Do not keep tightening screws blindly.',
                                           'book_hint': 'Contemporary Fixed Prosthodontics — '
                                                        'Rosenstiel'}]}},
 'pediatric_dentistry': {'easy': {'questions': [{'question': 'First permanent tooth often '
                                                             'erupting?',
                                                 'options': ['A) Mandibular first molar ~6 years',
                                                             'B) Wisdom tooth at 3 years',
                                                             'C) Maxillary lateral at 2 years '
                                                             'always',
                                                             'D) Canine at 4 months'],
                                                 'answer': 'A) Mandibular first molar ~6 years',
                                                 'explanation': 'Six-year molar.'},
                                                {'question': 'Fluoride varnish helps prevent?',
                                                 'options': ['A) Caries',
                                                             'B) Only malocclusion',
                                                             'C) Only ankylosis',
                                                             'D) Only supernumerary teeth'],
                                                 'answer': 'A) Caries',
                                                 'explanation': 'Evidence-based prevention.'},
                                                {'question': 'Pulpotomy is often for?',
                                                 'options': ['A) Primary teeth with coronal '
                                                             'pulpitis and restorable tooth',
                                                             'B) Only adult implants',
                                                             'C) Only ortho',
                                                             'D) Only bleaching'],
                                                 'answer': 'A) Primary teeth with coronal pulpitis '
                                                           'and restorable tooth',
                                                 'explanation': 'Preserve tooth till '
                                                                'exfoliation.'}],
                                  'cases': [{'title': 'Carious Primary Molar',
                                             'stem': 'A 5-year-old has a deep cavity in a primary '
                                                     'molar, no mobility, restorable.',
                                             'question': 'Options concept?',
                                             'answer': 'Restore ± pulp therapy if indicated; space '
                                                       'importance.',
                                             'discussion': 'Extraction needs space management '
                                                           'plan.',
                                             'book_hint': "McDonald and Avery's Dentistry for the "
                                                          'Child and Adolescent'}]},
                         'medium': {'questions': [{'question': 'SSC (stainless steel crown) '
                                                               'indication classic?',
                                                   'options': ['A) Multi-surface caries in primary '
                                                               'molars',
                                                               'B) Only shade try-in',
                                                               'C) Only veneers',
                                                               'D) Only bleaching trays'],
                                                   'answer': 'A) Multi-surface caries in primary '
                                                             'molars',
                                                   'explanation': 'Durable pediatric restoration.'},
                                                  {'question': 'Early childhood caries pattern '
                                                               'often?',
                                                   'options': ['A) Maxillary anterior teeth',
                                                               'B) Only lower anteriors protected '
                                                               'by tongue sometimes relatively '
                                                               'spared',
                                                               'C) Only third molars',
                                                               'D) Only impacted canines'],
                                                   'answer': 'A) Maxillary anterior teeth',
                                                   'explanation': 'Bottle/sippy habits.'},
                                                  {'question': 'Behavior guidance basic first '
                                                               'line?',
                                                   'options': ['A) Tell-show-do / communication',
                                                               'B) Always immediate GA',
                                                               'C) Always papoose without consent '
                                                               'themes',
                                                               'D) Ignore fear'],
                                                   'answer': 'A) Tell-show-do / communication',
                                                   'explanation': 'Build trust.'}],
                                    'cases': [{'title': 'Bottle Caries',
                                               'stem': 'A 3-year-old sleeps with a juice bottle; '
                                                       'upper incisors carious.',
                                               'question': 'Diagnosis theme?',
                                               'answer': 'Early childhood caries — stop habit, '
                                                         'restore/prevent, fluoride, diet '
                                                         'counseling.',
                                               'discussion': 'Lower incisors often relatively '
                                                             'spared.',
                                               'book_hint': "McDonald and Avery's Dentistry for "
                                                            'the Child and Adolescent'}]},
                         'hard': {'questions': [{'question': 'A junior colleague asks for the '
                                                             'single best answer. Intrusion of '
                                                             'primary tooth concern? Beware of '
                                                             'near-miss distractors.',
                                                 'options': ['A) Damage to permanent successor',
                                                             'B) Only freckle',
                                                             'C) Only sinusitis always',
                                                             'D) Only TMJ ankylosis always'],
                                                 'answer': 'A) Damage to permanent successor',
                                                 'explanation': 'Monitor eruption of permanent.'},
                                                {'question': 'A junior colleague asks for the '
                                                             'single best answer. Space loss after '
                                                             'early primary second molar loss? '
                                                             'Beware of near-miss distractors.',
                                                 'options': ['A) Mesial drift of first permanent '
                                                             'molar',
                                                             'B) No effect ever',
                                                             'C) Only distalization always helpful '
                                                             'without appliance',
                                                             'D) Only midline improves'],
                                                 'answer': 'A) Mesial drift of first permanent '
                                                           'molar',
                                                 'explanation': 'Space maintainer consideration.'},
                                                {'question': 'A junior colleague asks for the '
                                                             'single best answer. Molar-incisor '
                                                             'hypomineralization (MIH) features? '
                                                             'Beware of near-miss distractors.',
                                                 'options': ['A) Demarcated opacities on first '
                                                             'permanent molars/incisors',
                                                             'B) Only tetracycline bands only '
                                                             'cause',
                                                             'C) Only fluorosis diffuse always '
                                                             'same',
                                                             'D) Only caries without enamel '
                                                             'defect'],
                                                 'answer': 'A) Demarcated opacities on first '
                                                           'permanent molars/incisors',
                                                 'explanation': 'Sensitivity and breakdown risk.'}],
                                  'cases': [{'title': 'Intruded Primary Incisor',
                                             'stem': 'A 4-year-old intrudes a primary central '
                                                     'after a fall; tooth appears missing '
                                                     'clinically. Choose the safest high-yield '
                                                     'next concept before definitive results.',
                                             'question': 'Concern?',
                                             'answer': 'Possible displacement toward permanent bud '
                                                       '— radiograph, careful monitoring, avoid '
                                                       'aggressive replantation of primary.',
                                             'discussion': 'Watch permanent successor.',
                                             'book_hint': "McDonald and Avery's Dentistry for the "
                                                          'Child and Adolescent'}]},
                         'extreme': {'questions': [{'question': 'In a high-stakes clinic scenario '
                                                                'with incomplete data, which '
                                                                'statement is MOST correct? Child '
                                                                'abuse dental red flags include? '
                                                                'Avoid therapies that could harm '
                                                                'if a critical differential '
                                                                'remains open.',
                                                    'options': ['A) Injuries inconsistent with '
                                                                'history/age',
                                                                'B) Typical playground abrasion '
                                                                'with matching story',
                                                                'C) Only one cavity',
                                                                'D) Only orthodontic crowding'],
                                                    'answer': 'A) Injuries inconsistent with '
                                                              'history/age',
                                                    'explanation': 'Safeguarding duty.'},
                                                   {'question': 'In a high-stakes clinic scenario '
                                                                'with incomplete data, which '
                                                                'statement is MOST correct? GA '
                                                                'dentistry indications include? '
                                                                'Avoid therapies that could harm '
                                                                'if a critical differential '
                                                                'remains open.',
                                                    'options': ['A) Extensive disease + '
                                                                'uncooperative/medical complexity '
                                                                'after alternatives considered',
                                                                'B) Single easy restoration always',
                                                                'C) Only stain',
                                                                'D) Parental convenience alone '
                                                                'always ethical'],
                                                    'answer': 'A) Extensive disease + '
                                                              'uncooperative/medical complexity '
                                                              'after alternatives considered',
                                                    'explanation': 'Risk-benefit consent.'},
                                                   {'question': 'In a high-stakes clinic scenario '
                                                                'with incomplete data, which '
                                                                'statement is MOST correct? '
                                                                'Avulsed primary tooth should? '
                                                                'Avoid therapies that could harm '
                                                                'if a critical differential '
                                                                'remains open.',
                                                    'options': ['A) Generally not be replanted',
                                                                'B) Always replant like permanent',
                                                                'C) Always RCT immediately '
                                                                'extraoral',
                                                                'D) Always discard without exam'],
                                                    'answer': 'A) Generally not be replanted',
                                                    'explanation': 'IADT primary vs permanent '
                                                                   'differ.'}],
                                     'cases': [{'title': 'Unexplained Torn Frenum Toddler',
                                                'stem': 'A toddler has a torn labial frenum and '
                                                        'bruises of different ages; story keeps '
                                                        'changing. Avoid harmful premature '
                                                        'treatment while catastrophic '
                                                        'differentials remain open.',
                                                'question': 'Action concept?',
                                                'answer': 'Consider non-accidental injury — '
                                                          'document, treat dental needs, follow '
                                                          'safeguarding protocols.',
                                                'discussion': 'Do not discharge without '
                                                              'appropriate pathway.',
                                                'book_hint': "McDonald and Avery's Dentistry for "
                                                             'the Child and Adolescent'}]}},
 'oral_medicine': {'easy': {'questions': [{'question': 'Aphthous ulcers usually occur on?',
                                           'options': ['A) Non-keratinized mucosa',
                                                       'B) Only attached gingiva always',
                                                       'C) Only hard palate always',
                                                       'D) Only vermilion only always'],
                                           'answer': 'A) Non-keratinized mucosa',
                                           'explanation': 'Unlike HSV often on keratinized.'},
                                          {'question': 'Leukoplakia definition theme?',
                                           'options': ['A) White patch that cannot be wiped or '
                                                       'diagnosed as another disease',
                                                       'B) Always candidiasis wipeable',
                                                       'C) Always lichen planus certain',
                                                       'D) Always normal linea alba'],
                                           'answer': 'A) White patch that cannot be wiped or '
                                                     'diagnosed as another disease',
                                           'explanation': 'Risk of dysplasia.'},
                                          {'question': 'Geographic tongue is?',
                                           'options': ['A) Benign migratory glossitis',
                                                       'B) Always cancer',
                                                       'C) Always syphilis',
                                                       'D) Always trauma only'],
                                           'answer': 'A) Benign migratory glossitis',
                                           'explanation': 'Reassure often.'}],
                            'cases': [{'title': 'Recurrent Mouth Ulcers',
                                       'stem': 'Healthy teen gets painful ulcers on buccal mucosa '
                                               'lasting a week, then heal.',
                                       'question': 'Likely?',
                                       'answer': 'Recurrent aphthous stomatitis.',
                                       'discussion': 'Symptomatic care; investigate if complex.',
                                       'book_hint': 'Oral and Maxillofacial Pathology — Neville'}]},
                   'medium': {'questions': [{'question': 'Oral candidiasis risk factor?',
                                             'options': ['A) Antibiotics / steroids / dentures / '
                                                         'xerostomia / immunosuppression',
                                                         'B) Only orthodontic wax',
                                                         'C) Only flossing',
                                                         'D) Only sealants'],
                                             'answer': 'A) Antibiotics / steroids / dentures / '
                                                       'xerostomia / immunosuppression',
                                             'explanation': 'Treat cause + antifungal.'},
                                            {'question': 'Lichen planus oral classic?',
                                             'options': ['A) Reticular white striae (Wickham)',
                                                         'B) Only punched necrotic papillae of NUG',
                                                         'C) Only measles Koplik always',
                                                         'D) Only Fordyce granules'],
                                             'answer': 'A) Reticular white striae (Wickham)',
                                             'explanation': 'Biopsy if uncertain/erosive.'},
                                            {'question': 'SCC risk factors include?',
                                             'options': ['A) Tobacco and alcohol',
                                                         'B) Only xylitol gum',
                                                         'C) Only electric toothbrush',
                                                         'D) Only aligners'],
                                             'answer': 'A) Tobacco and alcohol',
                                             'explanation': 'Biopsy suspicious lesions.'}],
                              'cases': [{'title': 'White Patch Floor of Mouth',
                                         'stem': 'A 60-year-old smoker has a non-wipeable white '
                                                 'patch on floor of mouth.',
                                         'question': 'Next concept?',
                                         'answer': 'Treat as leukoplakia — specialist '
                                                   'referral/biopsy risk stratification.',
                                         'discussion': 'Floor of mouth is high-risk site.',
                                         'book_hint': 'Oral and Maxillofacial Pathology — '
                                                      'Neville'}]},
                   'hard': {'questions': [{'question': 'A junior colleague asks for the single '
                                                       'best answer. Pemphigus vulgaris oral clue? '
                                                       'Beware of near-miss distractors.',
                                           'options': ['A) Flaccid bullae / positive Nikolsky / '
                                                       'desquamative gingivitis themes',
                                                       'B) Only Fordyce',
                                                       'C) Only torus',
                                                       'D) Only amalgam tattoo'],
                                           'answer': 'A) Flaccid bullae / positive Nikolsky / '
                                                     'desquamative gingivitis themes',
                                           'explanation': 'Biopsy + immunofluorescence.'},
                                          {'question': 'A junior colleague asks for the single '
                                                       'best answer. Sjögren dry mouth '
                                                       'association? Beware of near-miss '
                                                       'distractors.',
                                           'options': ['A) Autoimmune exocrinopathy; caries risk '
                                                       'high',
                                                       'B) Only hyper salivation',
                                                       'C) Only dens evaginatus',
                                                       'D) Only mesiodens'],
                                           'answer': 'A) Autoimmune exocrinopathy; caries risk '
                                                     'high',
                                           'explanation': 'Preventive dentistry critical.'},
                                          {'question': 'A junior colleague asks for the single '
                                                       'best answer. OKC (odontogenic keratocyst) '
                                                       'behavior? Beware of near-miss distractors.',
                                           'options': ['A) High recurrence; careful surgical '
                                                       'management',
                                                       'B) Never recurs',
                                                       'C) Always leaves alone',
                                                       'D) Always pulpitis'],
                                           'answer': 'A) High recurrence; careful surgical '
                                                     'management',
                                           'explanation': 'Radiolucent jaw lesion differential.'}],
                            'cases': [{'title': 'Desquamative Gingivitis',
                                       'stem': 'Painful peeling gingiva, nikolsky-positive areas, '
                                               'no response to cleaning alone. Choose the safest '
                                               'high-yield next concept before definitive results.',
                                       'question': 'Workup?',
                                       'answer': 'Consider vesiculobullous disease — biopsy for '
                                                 'histopathology + DIF.',
                                       'discussion': 'Do not keep scaling without diagnosis.',
                                       'book_hint': 'Oral and Maxillofacial Pathology — Neville'}]},
                   'extreme': {'questions': [{'question': 'In a high-stakes clinic scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Non-healing ulcer >2 '
                                                          'weeks in smoker? Avoid therapies that '
                                                          'could harm if a critical differential '
                                                          'remains open.',
                                              'options': ['A) Cancer until proven otherwise — '
                                                          'biopsy',
                                                          'B) Always aphthous forever',
                                                          'C) Always ignore',
                                                          'D) Always only vitamins'],
                                              'answer': 'A) Cancer until proven otherwise — biopsy',
                                              'explanation': 'No endless observation.'},
                                             {'question': 'In a high-stakes clinic scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? Medication-related '
                                                          'osteonecrosis presentation? Avoid '
                                                          'therapies that could harm if a critical '
                                                          'differential remains open.',
                                              'options': ['A) Exposed bone in jaws with '
                                                          'antiresorptive history',
                                                          'B) Only geographic tongue',
                                                          'C) Only aphthae',
                                                          'D) Only caries'],
                                              'answer': 'A) Exposed bone in jaws with '
                                                        'antiresorptive history',
                                              'explanation': 'MRONJ pathways.'},
                                             {'question': 'In a high-stakes clinic scenario with '
                                                          'incomplete data, which statement is '
                                                          'MOST correct? HPV-related oropharyngeal '
                                                          'cancer theme? Avoid therapies that '
                                                          'could harm if a critical differential '
                                                          'remains open.',
                                              'options': ['A) Increasing in younger non-smokers '
                                                          'sometimes; base of tongue/tonsillar',
                                                          'B) Only always identical to classic '
                                                          'floor-of-mouth smoker pattern',
                                                          'C) Only skin melanoma',
                                                          'D) Only caries'],
                                              'answer': 'A) Increasing in younger non-smokers '
                                                        'sometimes; base of tongue/tonsillar',
                                              'explanation': 'Referral awareness.'}],
                               'cases': [{'title': 'Nonhealing Lateral Tongue Ulcer',
                                          'stem': 'A 55-year-old heavy smoker/drinker has a firm '
                                                  'nonhealing ulcer on lateral tongue for 6 weeks '
                                                  'with lymphadenopathy. Avoid harmful premature '
                                                  'treatment while catastrophic differentials '
                                                  'remain open.',
                                          'question': 'Action?',
                                          'answer': 'Urgent biopsy/OMFS-oncology referral for '
                                                    'suspected SCC.',
                                          'discussion': 'Do not treat empirically for months.',
                                          'book_hint': 'Oral and Maxillofacial Pathology — '
                                                       'Neville'}]}},
 'restorative': {'easy': {'questions': [{'question': 'G.V. Black Class II is?',
                                         'options': ['A) Proximal surfaces of posteriors',
                                                     'B) Only pits of anteriors',
                                                     'C) Only cervical thirds always Class V',
                                                     'D) Only cusp tip'],
                                         'answer': 'A) Proximal surfaces of posteriors',
                                         'explanation': 'Classic classification.'},
                                        {'question': 'Composite bonding relies on?',
                                         'options': ['A) Micromechanical adhesion after '
                                                     'etch/adhesive protocols',
                                                     'B) Only zinc phosphate always',
                                                     'C) Only screws',
                                                     'D) Only sutures'],
                                         'answer': 'A) Micromechanical adhesion after '
                                                   'etch/adhesive protocols',
                                         'explanation': 'Isolation critical.'},
                                        {'question': 'Caries detector dyes help?',
                                         'options': ['A) Visualize infected dentin cautiously',
                                                     'B) Replace radiographs always',
                                                     'C) Diagnose pulp vitality',
                                                     'D) Whiten teeth'],
                                         'answer': 'A) Visualize infected dentin cautiously',
                                         'explanation': 'Do not over-rely.'}],
                          'cases': [{'title': 'Occlusal Caries Molar',
                                     'stem': 'A deep fissure stains; bitewing shows enamel-dentin '
                                             'caries; tooth vital asymptomatic.',
                                     'question': 'Plan?',
                                     'answer': 'Restore with appropriate material after caries '
                                               'removal.',
                                     'discussion': 'Consider sealant for non-cavitated elsewhere.',
                                     'book_hint': 'Art and Science of Operative Dentistry — '
                                                  'Sturdevant'}]},
                 'medium': {'questions': [{'question': 'Liners/bases under deep restorations aim '
                                                       'to?',
                                           'options': ['A) Protect pulp / thermal insulation / '
                                                       'seal',
                                                       'B) Only change shade',
                                                       'C) Only etch enamel more',
                                                       'D) Only replace rubber dam'],
                                           'answer': 'A) Protect pulp / thermal insulation / seal',
                                           'explanation': 'Material choice depends on remaining '
                                                          'dentin.'},
                                          {'question': 'Amalgam advantage includes?',
                                           'options': ['A) Wear resistance / less technique '
                                                       'sensitivity to moisture than composite',
                                                       'B) Always superior esthetics',
                                                       'C) Bonds micromechanically identical to '
                                                       'etch-and-rinse composite',
                                                       'D) Never corrodes'],
                                           'answer': 'A) Wear resistance / less technique '
                                                     'sensitivity to moisture than composite',
                                           'explanation': 'Still technique and indications '
                                                          'matter.'},
                                          {'question': 'Secondary caries often at?',
                                           'options': ['A) Margins of restorations',
                                                       'B) Only pulp horn center always',
                                                       'C) Only apex',
                                                       'D) Only cementum only far from margins'],
                                           'answer': 'A) Margins of restorations',
                                           'explanation': 'Check seal and plaque control.'}],
                            'cases': [{'title': 'Failed Composite Margin',
                                       'stem': 'Staining and catch at cervical margin of Class V '
                                               'composite; sensitivity to cold brief.',
                                       'question': 'Likely?',
                                       'answer': 'Marginal leakage/secondary caries or bond '
                                                 'failure — replace after diagnosis.',
                                       'discussion': 'Isolate well on redo.',
                                       'book_hint': 'Art and Science of Operative Dentistry — '
                                                    'Sturdevant'}]},
                 'hard': {'questions': [{'question': 'A junior colleague asks for the single best '
                                                     'answer. C-factor high in? Beware of '
                                                     'near-miss distractors.',
                                         'options': ['A) Class I deep boxy preparations',
                                                     'B) Only free cusp rebuild always low',
                                                     'C) Only veneers on one surface always lowest '
                                                     'issue',
                                                     'D) Only sealants'],
                                         'answer': 'A) Class I deep boxy preparations',
                                         'explanation': 'Polymerization stress risk.'},
                                        {'question': 'A junior colleague asks for the single best '
                                                     'answer. Selective caries removal deep lesion '
                                                     'aims to? Beware of near-miss distractors.',
                                         'options': ['A) Avoid pulp exposure while sealing '
                                                     'remaining soft dentin under protocol',
                                                     'B) Always expose pulp',
                                                     'C) Always leave all enamel caries',
                                                     'D) Never restore'],
                                         'answer': 'A) Avoid pulp exposure while sealing remaining '
                                                   'soft dentin under protocol',
                                         'explanation': 'Evidence-based stepwise approaches.'},
                                        {'question': 'A junior colleague asks for the single best '
                                                     'answer. Abfraction theory relates to? Beware '
                                                     'of near-miss distractors.',
                                         'options': ['A) Occlusal stress cervical lesions debated '
                                                     'etiology',
                                                     'B) Only erosion from lemon',
                                                     'C) Only abrasion from brush only proven '
                                                     'forever',
                                                     'D) Only caries'],
                                         'answer': 'A) Occlusal stress cervical lesions debated '
                                                   'etiology',
                                         'explanation': 'Multifactorial NCCLs.'}],
                          'cases': [{'title': 'Deep Caries Near Pulp',
                                     'stem': 'Young adult molar, deep caries, asymptomatic, '
                                             'remaining dentin thin on radiograph. Choose the '
                                             'safest high-yield next concept before definitive '
                                             'results.',
                                     'question': 'Strategy concept?',
                                     'answer': 'Consider stepwise/selective excavation, pulp '
                                               'protection, well-sealed restoration; monitor '
                                               'vitality.',
                                     'discussion': 'Avoid unnecessary exposure.',
                                     'book_hint': 'Art and Science of Operative Dentistry — '
                                                  'Sturdevant'}]},
                 'extreme': {'questions': [{'question': 'In a high-stakes clinic scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Minimally invasive dentistry '
                                                        'prioritizes? Avoid therapies that could '
                                                        'harm if a critical differential remains '
                                                        'open.',
                                            'options': ['A) Prevention, early detection, maximal '
                                                        'tissue preservation',
                                                        'B) Full coverage for every stain',
                                                        'C) Extract first always',
                                                        'D) Ignore risk factors'],
                                            'answer': 'A) Prevention, early detection, maximal '
                                                      'tissue preservation',
                                            'explanation': 'ICDAS/risk-based care.'},
                                           {'question': 'In a high-stakes clinic scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Biomimetic restorative concept '
                                                        'emphasizes? Avoid therapies that could '
                                                        'harm if a critical differential remains '
                                                        'open.',
                                            'options': ['A) Replacing tissue with materials '
                                                        'mimicking properties/stress distribution',
                                                        'B) Only cheapest cement always',
                                                        'C) Only one shade A2 always',
                                                        'D) Ignoring ferrule'],
                                            'answer': 'A) Replacing tissue with materials '
                                                      'mimicking properties/stress distribution',
                                            'explanation': 'Adhesive protocols central.'},
                                           {'question': 'In a high-stakes clinic scenario with '
                                                        'incomplete data, which statement is MOST '
                                                        'correct? Rampant caries management order? '
                                                        'Avoid therapies that could harm if a '
                                                        'critical differential remains open.',
                                            'options': ['A) Urgencies, disease control, '
                                                        'temporaries, definitive when stable',
                                                        'B) Only esthetic veneers first',
                                                        'C) Only bleaching first',
                                                        'D) Ignore diet'],
                                            'answer': 'A) Urgencies, disease control, temporaries, '
                                                      'definitive when stable',
                                            'explanation': 'Stabilize before expensive finals.'}],
                             'cases': [{'title': 'Rampant Caries Head-Neck Radiation',
                                        'stem': 'Patient post-radiotherapy has rampant caries and '
                                                'xerostomia. Avoid harmful premature treatment '
                                                'while catastrophic differentials remain open.',
                                        'question': 'Plan pillars?',
                                        'answer': 'Aggressive prevention (fluoride, saliva '
                                                  'management), restore strategically, avoid '
                                                  'extractions in irradiated bone when possible '
                                                  'via specialist pathways.',
                                        'discussion': 'ORN risk changes extraction decisions.',
                                        'book_hint': 'Art and Science of Operative Dentistry — '
                                                     'Sturdevant'}]}},
 'oral_radiology': {'easy': {'questions': [{'question': 'Bitewing radiographs best show?',
                                            'options': ['A) Interproximal caries and crestal bone',
                                                        'B) Only TMJ disk',
                                                        'C) Only sinus polyps always',
                                                        'D) Only soft tissue cancer staging'],
                                            'answer': 'A) Interproximal caries and crestal bone',
                                            'explanation': 'Workhorse for caries.'},
                                           {'question': 'ALARA means?',
                                            'options': ['A) As Low As Reasonably Achievable '
                                                        'radiation',
                                                        'B) Always Lowest And Rarely Any '
                                                        'radiograph never',
                                                        'C) Only analog films',
                                                        'D) Only CBCT for all exams'],
                                            'answer': 'A) As Low As Reasonably Achievable '
                                                      'radiation',
                                            'explanation': 'Justification + optimization.'},
                                           {'question': 'Periapical radiograph shows?',
                                            'options': ['A) Full tooth and periapical bone',
                                                        'B) Only bite relationship of all molars '
                                                        'both sides always',
                                                        'C) Only cephalometric landmarks',
                                                        'D) Only chest'],
                                            'answer': 'A) Full tooth and periapical bone',
                                            'explanation': 'Endo/periapical assessment.'}],
                             'cases': [{'title': 'Suspected Interproximal Caries',
                                        'stem': 'Tight contacts, clinical doubt on upper '
                                                'premolars.',
                                        'question': 'Image of choice first?',
                                        'answer': 'Bitewings.',
                                        'discussion': 'Then restore if confirmed.',
                                        'book_hint': "White and Pharoah's Oral Radiology"}]},
                    'medium': {'questions': [{'question': 'Panoramic radiograph advantage?',
                                              'options': ['A) Broad overview of jaws/TMJ/teeth',
                                                          'B) Highest resolution for early enamel '
                                                          'caries always better than bitewing',
                                                          'C) Zero distortion ever',
                                                          'D) Replaces all PAs always'],
                                              'answer': 'A) Broad overview of jaws/TMJ/teeth',
                                              'explanation': 'Screening/ortho/surgery planning.'},
                                             {'question': 'Radiolucent lesion at apex of nonvital '
                                                          'tooth likely?',
                                              'options': ['A) Periapical rarefying osteitis / '
                                                          'granuloma/cyst spectrum',
                                                          'B) Always osteosarcoma',
                                                          'C) Always torus',
                                                          'D) Always enamel pearl'],
                                              'answer': 'A) Periapical rarefying osteitis / '
                                                        'granuloma/cyst spectrum',
                                              'explanation': 'Correlate vitality.'},
                                             {'question': 'Lead apron/thyroid shield use follows?',
                                              'options': ['A) Current guidelines; justification '
                                                          'first',
                                                          'B) Never used historically considered',
                                                          'C) Only for CBCT never for bitewings '
                                                          'ever universally',
                                                          'D) Only for staff not patients'],
                                              'answer': 'A) Current guidelines; justification '
                                                        'first',
                                              'explanation': 'Protocols evolve — follow '
                                                             'local/current.'}],
                               'cases': [{'title': 'Impacted Canine Localization',
                                          'stem': 'Need to know buccal/palatal position of '
                                                  'impacted canine.',
                                          'question': 'Options?',
                                          'answer': 'Parallax technique or CBCT when justified.',
                                          'discussion': 'Avoid unnecessary high-dose imaging.',
                                          'book_hint': "White and Pharoah's Oral Radiology"}]},
                    'hard': {'questions': [{'question': 'A junior colleague asks for the single '
                                                        'best answer. CBCT indications include? '
                                                        'Beware of near-miss distractors.',
                                            'options': ['A) Complex implant/impacted '
                                                        'tooth/endodontic anatomy when 2D '
                                                        'insufficient',
                                                        'B) Routine checkup replacing bitewings '
                                                        'always',
                                                        'C) Only caries detection first-line '
                                                        'always',
                                                        'D) Only shade selection'],
                                            'answer': 'A) Complex implant/impacted '
                                                      'tooth/endodontic anatomy when 2D '
                                                      'insufficient',
                                            'explanation': 'Higher dose — justify.'},
                                           {'question': 'A junior colleague asks for the single '
                                                        'best answer. Ghost image on panoramic is? '
                                                        'Beware of near-miss distractors.',
                                            'options': ['A) Blurred contralateral dense object '
                                                        'projection',
                                                        'B) Always pathology',
                                                        'C) Always processing error only',
                                                        'D) Always patient name'],
                                            'answer': 'A) Blurred contralateral dense object '
                                                      'projection',
                                            'explanation': 'Recognize artifacts.'},
                                           {'question': 'A junior colleague asks for the single '
                                                        'best answer. SLOB rule helps? Beware of '
                                                        'near-miss distractors.',
                                            'options': ['A) Buccolingual localization with tube '
                                                        'shift',
                                                        'B) Only exposure time',
                                                        'C) Only kVp charts',
                                                        'D) Only processing chemicals'],
                                            'answer': 'A) Buccolingual localization with tube '
                                                      'shift',
                                            'explanation': 'Same Lingual Opposite Buccal.'}],
                             'cases': [{'title': 'Unilocular Radiolucency Angle of Mandible',
                                        'stem': 'Impacted wisdom tooth with radiolucency around '
                                                'crown in a young adult. Choose the safest '
                                                'high-yield next concept before definitive '
                                                'results.',
                                        'question': 'Differential includes?',
                                        'answer': 'Dentigerous cyst among others — '
                                                  'remove/investigate histologically as indicated.',
                                        'discussion': 'Do not ignore enlarging lesions.',
                                        'book_hint': "White and Pharoah's Oral Radiology"}]},
                    'extreme': {'questions': [{'question': 'In a high-stakes clinic scenario with '
                                                           'incomplete data, which statement is '
                                                           'MOST correct? Malignant lesion '
                                                           'radiographic clues? Avoid therapies '
                                                           'that could harm if a critical '
                                                           'differential remains open.',
                                               'options': ['A) Ill-defined borders, cortical '
                                                           'destruction, rapid change',
                                                           'B) Always corticated unilocular slow',
                                                           'C) Always radiopaque torus',
                                                           'D) Always normal trabeculation'],
                                               'answer': 'A) Ill-defined borders, cortical '
                                                         'destruction, rapid change',
                                               'explanation': 'Urgent referral.'},
                                              {'question': 'In a high-stakes clinic scenario with '
                                                           'incomplete data, which statement is '
                                                           'MOST correct? Radiation dose concern '
                                                           'ranking theme? Avoid therapies that '
                                                           'could harm if a critical differential '
                                                           'remains open.',
                                               'options': ['A) CBCT generally > panoramic > '
                                                           'intraoral typically',
                                                           'B) Bitewing always highest',
                                                           'C) All equal always',
                                                           'D) Clinical photo higher than CBCT'],
                                               'answer': 'A) CBCT generally > panoramic > '
                                                         'intraoral typically',
                                               'explanation': 'Select wisely.'},
                                              {'question': 'In a high-stakes clinic scenario with '
                                                           'incomplete data, which statement is '
                                                           'MOST correct? Idiopathic '
                                                           'osteosclerosis vs condensing osteitis? '
                                                           'Avoid therapies that could harm if a '
                                                           'critical differential remains open.',
                                               'options': ['A) Vitality and clinical context '
                                                           'distinguish',
                                                           'B) Always identical disease needing '
                                                           'RCT',
                                                           'C) Always malignancy',
                                                           'D) Always extract'],
                                               'answer': 'A) Vitality and clinical context '
                                                         'distinguish',
                                               'explanation': 'Condensing osteitis linked to pulp '
                                                              'pathosis.'}],
                                'cases': [{'title': 'Ill-defined Mandibular Destruction',
                                           'stem': 'A rapidly enlarging numb chin, loose teeth, '
                                                   'and moth-eaten bone on radiograph. Avoid '
                                                   'harmful premature treatment while catastrophic '
                                                   'differentials remain open.',
                                           'question': 'Action?',
                                           'answer': 'Urgent biopsy/OMFS-oncology workup for '
                                                     'possible malignancy.',
                                           'discussion': 'Do not schedule elective cleaning only.',
                                           'book_hint': "White and Pharoah's Oral Radiology"}]}},
 'dental_anatomy': {'easy': {'questions': [{'question': 'How many permanent teeth normally?',
                                            'options': ['A) 32',
                                                        'B) 20',
                                                        'C) 28 always excluding wisdom never vary',
                                                        'D) 16'],
                                            'answer': 'A) 32',
                                            'explanation': 'Including third molars.'},
                                           {'question': 'Primary dentition count?',
                                            'options': ['A) 20', 'B) 32', 'C) 12', 'D) 36'],
                                            'answer': 'A) 20',
                                            'explanation': 'No premolars in primary.'},
                                           {'question': 'Cusp of Carabelli is on?',
                                            'options': ['A) Maxillary first molar',
                                                        'B) Mandibular central',
                                                        'C) Maxillary lateral only',
                                                        'D) Mandibular canine'],
                                            'answer': 'A) Maxillary first molar',
                                            'explanation': 'Mesiolingual aspect variation.'}],
                             'cases': [{'title': 'Identify Tooth',
                                        'stem': 'A tooth has 3 roots and a Carabelli cusp trait.',
                                        'question': 'Most likely?',
                                        'answer': 'Maxillary first molar.',
                                        'discussion': 'Know morphology for endo/restorative.',
                                        'book_hint': "Wheeler's Dental Anatomy, Physiology and "
                                                     'Occlusion'}]},
                    'medium': {'questions': [{'question': 'Maxillary first premolar often has?',
                                              'options': ['A) Two roots / two canals commonly',
                                                          'B) Always one canal only',
                                                          'C) Always three roots like upper molar',
                                                          'D) No cusps'],
                                              'answer': 'A) Two roots / two canals commonly',
                                              'explanation': 'Endodontic relevance.'},
                                             {'question': 'Contact point of anteriors is usually?',
                                              'options': ['A) Incisal third to middle third '
                                                          'junction themes',
                                                          'B) Always at cervix only',
                                                          'C) Always at root apex',
                                                          'D) No contacts normal'],
                                              'answer': 'A) Incisal third to middle third junction '
                                                        'themes',
                                              'explanation': 'Protects papilla.'},
                                             {'question': 'Curve of Spee is?',
                                              'options': ['A) Anteroposterior occlusal curvature',
                                                          'B) Only mediolateral Wilson',
                                                          'C) Only Bonwill triangle only',
                                                          'D) Only freeway space'],
                                              'answer': 'A) Anteroposterior occlusal curvature',
                                              'explanation': 'Occlusion concepts.'}],
                               'cases': [{'title': 'Endo Access Planning',
                                          'stem': 'Upper first premolar needs RCT.',
                                          'question': 'Anatomy alert?',
                                          'answer': 'Often two canals — search carefully.',
                                          'discussion': 'Missed canal → failure.',
                                          'book_hint': "Wheeler's Dental Anatomy, Physiology and "
                                                       'Occlusion'}]},
                    'hard': {'questions': [{'question': 'A junior colleague asks for the single '
                                                        'best answer. Mandibular first molar '
                                                        'typically canals? Beware of near-miss '
                                                        'distractors.',
                                            'options': ['A) Often 3 canals (MB, ML, D) with '
                                                        'variations',
                                                        'B) Always exactly one',
                                                        'C) Always five named Carabelli canals',
                                                        'D) No pulp'],
                                            'answer': 'A) Often 3 canals (MB, ML, D) with '
                                                      'variations',
                                            'explanation': 'Middle mesial possible.'},
                                           {'question': 'A junior colleague asks for the single '
                                                        'best answer. Enamel is thickest at? '
                                                        'Beware of near-miss distractors.',
                                            'options': ['A) Occlusal/incisal contact areas themes',
                                                        'B) CEJ always thickest',
                                                        'C) Apex',
                                                        'D) Furcation'],
                                            'answer': 'A) Occlusal/incisal contact areas themes',
                                            'explanation': 'Hardest tissue.'},
                                           {'question': 'A junior colleague asks for the single '
                                                        'best answer. Pulp horn height relates to? '
                                                        'Beware of near-miss distractors.',
                                            'options': ['A) Risk of exposure in prep of young '
                                                        'teeth',
                                                        'B) Only shade',
                                                        'C) Only root length always equal',
                                                        'D) Only calculus'],
                                            'answer': 'A) Risk of exposure in prep of young teeth',
                                            'explanation': 'Conservative prep.'}],
                             'cases': [{'title': 'Young Tooth Prep Exposure Risk',
                                        'stem': 'A teenager needs a deep occlusal restoration on a '
                                                'newly erupted molar. Choose the safest high-yield '
                                                'next concept before definitive results.',
                                        'question': 'Anatomy concern?',
                                        'answer': 'High pulp horns — careful depth, consider '
                                                  'indirect pulp strategies.',
                                        'discussion': 'Avoid iatrogenic exposure.',
                                        'book_hint': "Wheeler's Dental Anatomy, Physiology and "
                                                     'Occlusion'}]},
                    'extreme': {'questions': [{'question': 'In a high-stakes clinic scenario with '
                                                           'incomplete data, which statement is '
                                                           'MOST correct? Dens invaginatus risk? '
                                                           'Avoid therapies that could harm if a '
                                                           'critical differential remains open.',
                                               'options': ['A) Pulp infection via invagination',
                                                           'B) Only better enamel',
                                                           'C) Only freckles',
                                                           'D) Only torus'],
                                               'answer': 'A) Pulp infection via invagination',
                                               'explanation': 'Early sealing/endo awareness.'},
                                              {'question': 'In a high-stakes clinic scenario with '
                                                           'incomplete data, which statement is '
                                                           'MOST correct? Taurodontism features? '
                                                           'Avoid therapies that could harm if a '
                                                           'critical differential remains open.',
                                               'options': ['A) Enlarged pulp chamber / apically '
                                                           'displaced furcation',
                                                           'B) Only short roots always dilacerated '
                                                           'crowns',
                                                           'C) Only dens evaginatus',
                                                           'D) Only enamel pearl only'],
                                               'answer': 'A) Enlarged pulp chamber / apically '
                                                         'displaced furcation',
                                               'explanation': 'Endodontic complexity.'},
                                              {'question': 'In a high-stakes clinic scenario with '
                                                           'incomplete data, which statement is '
                                                           'MOST correct? Dilaceration '
                                                           'complicates? Avoid therapies that '
                                                           'could harm if a critical differential '
                                                           'remains open.',
                                               'options': ['A) Extraction and endodontics',
                                                           'B) Only shade selection',
                                                           'C) Only flossing forever easy',
                                                           'D) Only rubber dam clamp color'],
                                               'answer': 'A) Extraction and endodontics',
                                               'explanation': 'Radiograph before surgery.'}],
                                'cases': [{'title': 'Bizarre Root Morphology Pre-Extract',
                                           'stem': 'A curved dilacerated premolar needs extraction '
                                                   'under LA. Avoid harmful premature treatment '
                                                   'while catastrophic differentials remain open.',
                                           'question': 'Plan?',
                                           'answer': 'Radiograph assessment, surgical sectioning '
                                                     'readiness, avoid blind force.',
                                           'discussion': 'Prevent root fracture/displacement.',
                                           'book_hint': "Wheeler's Dental Anatomy, Physiology and "
                                                        'Occlusion'}]}}}
