"""Undergraduate dentistry study content by specialty and difficulty."""
from __future__ import annotations

import random

from quiz_bank import DIFFICULTIES, DIFFICULTY_LABELS, LABEL_TO_DIFFICULTY

SPECIALTY_ORDER = ['oral_surgery', 'orthodontics', 'periodontics', 'endodontics', 'prosthodontics', 'pediatric_dentistry', 'oral_medicine', 'restorative', 'oral_radiology', 'dental_anatomy']

SPECIALTIES: dict[str, dict] = {'oral_surgery': {'label': 'Oral Surgery',
                  'books': ["Peterson's Principles of Oral and Maxillofacial Surgery",
                            'Contemporary Oral and Maxillofacial Surgery — Hupp',
                            'Local Anaesthesia in Dentistry'],
                  'pdf_notes': ['IANB targets mandibular foramen region; know failure causes.',
                                'Dry socket: pain day 2-4, empty socket — irrigate + dressing.',
                                'Ludwig angina: airway first, urgent drainage/antibiotics.',
                                'Assess bleeding risk (anticoagulants) before surgery.',
                                'Impacted third molars: IAN/lingual nerve risk counseling.'],
                  'questions': {'easy': [{'question': 'Most common impacted tooth?',
                                          'options': ['A) Maxillary canine',
                                                      'B) Mandibular third molar',
                                                      'C) Maxillary lateral incisor',
                                                      'D) Mandibular first premolar'],
                                          'answer': 'B) Mandibular third molar',
                                          'explanation': 'Mandibular third molars are the teeth '
                                                         'most frequently impacted because they '
                                                         'erupt last and often lack adequate space '
                                                         'in the dental arch. Impaction occurs '
                                                         'when eruption is blocked by bone, soft '
                                                         'tissue, or an adjacent tooth. Maxillary '
                                                         'canines are the next most commonly '
                                                         'impacted teeth, but far less often than '
                                                         'lower wisdom teeth.'},
                                         {'question': 'Local anesthetic for an inferior alveolar '
                                                      'nerve block typically targets which '
                                                      'anatomic region?',
                                          'options': ['A) Mental foramen on the buccal mandible',
                                                      'B) Infraorbital foramen on the maxilla',
                                                      'C) Mandibular foramen on the medial ramus',
                                                      'D) Greater palatine foramen on the hard '
                                                      'palate'],
                                          'answer': 'C) Mandibular foramen on the medial ramus',
                                          'explanation': 'The inferior alveolar nerve enters the '
                                                         'mandible at the mandibular foramen on '
                                                         'the medial ramus. An inferior alveolar '
                                                         'nerve block deposits anesthetic near '
                                                         'this foramen so the solution bathes the '
                                                         'nerve before it enters the mandibular '
                                                         'canal. Successful anesthesia therefore '
                                                         'depends on accurate needle placement '
                                                         'relative to the lingula and mandibular '
                                                         'foramen.'},
                                         {'question': 'Alveolar osteitis (dry socket) most '
                                                      'commonly follows which clinical situation?',
                                          'options': ['A) Difficult mandibular molar extraction '
                                                      'with clot loss',
                                                      'B) Routine fluoride varnish application',
                                                      'C) Supragingival scaling without extraction',
                                                      'D) Orthodontic bracket bonding alone'],
                                          'answer': 'A) Difficult mandibular molar extraction with '
                                                    'clot loss',
                                          'explanation': 'Alveolar osteitis (dry socket) follows '
                                                         'premature loss or lysis of the blood '
                                                         'clot that normally protects the '
                                                         'extraction socket. Exposed bone and '
                                                         'inflammatory mediators produce severe '
                                                         'pain, typically beginning two to four '
                                                         'days after a difficult mandibular molar '
                                                         'extraction. Risk rises with traumatic '
                                                         'extraction, smoking, and poor clot '
                                                         'stability.'}],
                                'medium': [{'question': 'Ludwig angina is best described as '
                                                        'infection involving which spaces?',
                                            'options': ['A) Temporomandibular joint capsule alone',
                                                        'B) Unilateral maxillary sinus alone',
                                                        'C) Pulp chamber and root canals only',
                                                        'D) Bilateral submandibular, sublingual, '
                                                        'and submental spaces'],
                                            'answer': 'D) Bilateral submandibular, sublingual, and '
                                                      'submental spaces',
                                            'explanation': 'Ludwig angina is a rapidly spreading '
                                                           'bilateral cellulitis of the '
                                                           'submandibular, sublingual, and '
                                                           'submental spaces, usually from an '
                                                           'odontogenic source. Edema elevates the '
                                                           'floor of the mouth and tongue, '
                                                           'threatening the airway. Urgent airway '
                                                           'management, intravenous antibiotics, '
                                                           'and surgical drainage are required.'},
                                           {'question': 'Which laboratory measure is most relevant '
                                                        'before oral surgery in a patient taking '
                                                        'warfarin?',
                                            'options': ['A) HbA1c only',
                                                        'B) INR (international normalized ratio)',
                                                        'C) Serum amylase only',
                                                        'D) Fasting lipid panel only'],
                                            'answer': 'B) INR (international normalized ratio)',
                                            'explanation': 'Warfarin inhibits vitamin K–dependent '
                                                           'clotting factors and is monitored with '
                                                           'the international normalized ratio '
                                                           '(INR). Before invasive oral surgery, '
                                                           'the INR helps estimate bleeding risk '
                                                           'so hemostasis planning and any '
                                                           'physician-coordinated dose adjustment '
                                                           'can be made appropriately.'},
                                           {'question': 'Oroantral communication risk is highest '
                                                        'when extracting which teeth?',
                                            'options': ['A) Mandibular incisors',
                                                        'B) Mandibular canines',
                                                        'C) Mandibular premolars',
                                                        'D) Maxillary molars'],
                                            'answer': 'D) Maxillary molars',
                                            'explanation': 'Maxillary molar roots often lie close '
                                                           'to, or project into, the maxillary '
                                                           'sinus floor. Extraction can tear the '
                                                           'thin antral bone or sinus membrane and '
                                                           'create an oroantral communication. '
                                                           'Mandibular teeth do not communicate '
                                                           'with the maxillary sinus.'}],
                                'hard': [{'question': 'Which nerve is at notable injury risk '
                                                      'during mandibular third molar surgery near '
                                                      'the canal?',
                                          'options': ['A) Optic nerve',
                                                      'B) Phrenic nerve',
                                                      'C) Inferior alveolar nerve',
                                                      'D) Recurrent laryngeal nerve'],
                                          'answer': 'C) Inferior alveolar nerve',
                                          'explanation': 'The inferior alveolar nerve runs in the '
                                                         'mandibular canal and may lie immediately '
                                                         'adjacent to mandibular third molar '
                                                         'roots. Surgical elevation or sectioning '
                                                         'of the tooth can stretch, crush, or '
                                                         'transect the nerve, causing altered lip '
                                                         'and chin sensation. Preoperative imaging '
                                                         'and informed consent address this risk.'},
                                         {'question': 'Medication-related osteonecrosis of the jaw '
                                                      'risk rises most with which scenario?',
                                          'options': ['A) Placement of removable orthodontic '
                                                      'retainers',
                                                      'B) Topical fluoride varnish alone',
                                                      'C) Routine dental prophylaxis without '
                                                      'mucosal trauma',
                                                      'D) Invasive dental surgery in patients on '
                                                      'antiresorptive therapy'],
                                          'answer': 'D) Invasive dental surgery in patients on '
                                                    'antiresorptive therapy',
                                          'explanation': 'Medication-related osteonecrosis of the '
                                                         'jaw (MRONJ) is exposed necrotic bone '
                                                         'associated with antiresorptive or '
                                                         'antiangiogenic drugs. Invasive '
                                                         'procedures such as extractions disrupt '
                                                         'oral mucosa and bone healing in '
                                                         'susceptible patients, elevating MRONJ '
                                                         'risk compared with noninvasive care.'},
                                         {'question': 'A root tip displaced into the maxillary '
                                                      'sinus during extraction most appropriately '
                                                      'requires?',
                                          'options': ['A) Immediate root canal treatment of the '
                                                      'adjacent vital tooth only',
                                                      'B) Retrieval strategy with sinus '
                                                      'precautions and possible referral',
                                                      'C) Observation indefinitely without imaging '
                                                      'or follow-up',
                                                      'D) Chlorhexidine rinse alone as definitive '
                                                      'management'],
                                          'answer': 'B) Retrieval strategy with sinus precautions '
                                                    'and possible referral',
                                          'explanation': 'A root tip displaced into the maxillary '
                                                         'sinus can act as a foreign body, '
                                                         'promoting sinusitis or sustaining an '
                                                         'oroantral fistula. Management requires '
                                                         'retrieval when indicated, closure of any '
                                                         'communication, sinus precautions, and '
                                                         'specialist referral if needed.'}],
                                'extreme': [{'question': 'An anticoagulated patient needs urgent '
                                                         'extraction with elevated bleeding risk. '
                                                         'Best management concept?',
                                             'options': ['A) Stop all anticoagulants unilaterally '
                                                         'the morning of surgery',
                                                         'B) Refuse extraction under every '
                                                         'circumstance',
                                                         'C) Give vitamin K routinely without '
                                                         'assessing the indication',
                                                         'D) Coordinate physician guidance; use '
                                                         'local hemostasis; avoid blind '
                                                         'anticoagulant cessation'],
                                             'answer': 'D) Coordinate physician guidance; use '
                                                       'local hemostasis; avoid blind '
                                                       'anticoagulant cessation',
                                             'explanation': 'Therapeutic anticoagulation reduces '
                                                            'thromboembolic risk; abrupt cessation '
                                                            'can precipitate stroke or venous '
                                                            'thrombosis. For most dental '
                                                            'extractions, continuing '
                                                            'anticoagulation with meticulous local '
                                                            'hemostasis is preferred, coordinated '
                                                            'with the prescribing physician when '
                                                            'risk is high.'},
                                            {'question': 'Postoperative expanding neck hematoma '
                                                         'with stridor most urgently indicates?',
                                             'options': ['A) Airway emergency management first',
                                                         'B) Home antibiotics and routine review '
                                                         'next week',
                                                         'C) Overnight observation without airway '
                                                         'assessment',
                                                         'D) Ice packs alone without clinical '
                                                         'evaluation'],
                                             'answer': 'A) Airway emergency management first',
                                             'explanation': 'An expanding neck hematoma after '
                                                            'surgery can compress the airway, '
                                                            'producing stridor, dyspnea, and rapid '
                                                            'desaturation. Airway establishment '
                                                            'takes absolute priority over '
                                                            'investigating the bleeding source or '
                                                            'prescribing outpatient measures.'},
                                            {'question': 'Osteoradionecrosis risk is most strongly '
                                                         'linked to which situation?',
                                             'options': ['A) Natural exfoliation of primary teeth',
                                                         'B) Placement of pit-and-fissure sealants',
                                                         'C) Extractions in previously irradiated '
                                                         'jaws',
                                                         'D) Use of at-home whitening trays'],
                                             'answer': 'C) Extractions in previously irradiated '
                                                       'jaws',
                                             'explanation': 'High-dose radiotherapy damages bone '
                                                            'vasculature and cellularity in the '
                                                            'jaws, impairing healing after trauma. '
                                                            'Extractions in irradiated bone '
                                                            'therefore carry a recognized risk of '
                                                            'osteoradionecrosis. Preventive dental '
                                                            'care before radiotherapy reduces '
                                                            'later extraction need.'}]},
                  'cases': {'easy': [{'title': 'Pain Day 3 After Extraction',
                                      'stem': 'A 24-year-old has severe pain 3 days after lower '
                                              'wisdom tooth removal. Socket looks empty; no pus or '
                                              'fever.',
                                      'question': 'Likely diagnosis?',
                                      'answer': 'Alveolar osteitis (dry socket).',
                                      'discussion': 'Irrigate, medicated dressing, analgesia; '
                                                    'antibiotics usually not first-line if no '
                                                    'infection.',
                                      'book_hint': "Peterson's Principles of Oral and "
                                                   'Maxillofacial Surgery'}],
                            'medium': [{'title': 'Fever + Floor of Mouth Swelling',
                                        'stem': 'A patient after dental infection has bilateral '
                                                'floor-of-mouth swelling, drooling, and tongue '
                                                'elevation.',
                                        'question': 'Emergency concern?',
                                        'answer': 'Ludwig angina — secure airway and urgent '
                                                  'surgical/medical care.',
                                        'discussion': 'Do not delay for routine dental clinic '
                                                      'care.',
                                        'book_hint': "Peterson's Principles of Oral and "
                                                     'Maxillofacial Surgery'}],
                            'hard': [{'title': 'Root Tip Disappears Upward',
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
                                                   'Maxillofacial Surgery'}],
                            'extreme': [{'title': 'Irradiated Jaw Needs Extraction',
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
 'orthodontics': {'label': 'Orthodontics',
                  'books': ["Proffit's Contemporary Orthodontics",
                            'Graber Orthodontics',
                            'Handbook of Orthodontics — Cobourne'],
                  'pdf_notes': ['Angle Class I/II/III molar relationships.',
                                'Overjet = horizontal; overbite = vertical.',
                                'Space maintainers after premature primary loss.',
                                'Retention is long-term; relapse is common without retainers.',
                                'Uncontrolled periodontitis: do not move teeth aggressively.'],
                  'questions': {'easy': [{'question': 'Angle Class II molar relation means?',
                                          'options': ['A) Mandibular first molar distal relative '
                                                      'to the maxillary first molar',
                                                      'B) Mandibular first molar mesial relative '
                                                      'to Class I',
                                                      'C) Anterior open bite without molar '
                                                      'discrepancy',
                                                      'D) Bilateral posterior crossbite without '
                                                      'anteroposterior change'],
                                          'answer': 'A) Mandibular first molar distal relative to '
                                                    'the maxillary first molar',
                                          'explanation': 'In Angle’s classification, Class II '
                                                         'molar occlusion means the mandibular '
                                                         'first molar is positioned distal to its '
                                                         'normal relation with the maxillary first '
                                                         'molar. Clinically, the mesiobuccal cusp '
                                                         'of the upper first molar occludes mesial '
                                                         'to the buccal groove of the lower first '
                                                         'molar.'},
                                         {'question': 'Overjet describes which relationship?',
                                          'options': ['A) Vertical overlap of the incisors only',
                                                      'B) Horizontal overlap of the incisors',
                                                      'C) Torque of molar crowns only',
                                                      'D) Arch-length discrepancy only'],
                                          'answer': 'B) Horizontal overlap of the incisors',
                                          'explanation': 'Overjet is the horizontal distance '
                                                         'between the labial surface of the '
                                                         'mandibular incisors and the incisal '
                                                         'edges of the maxillary incisors. '
                                                         'Overbite, by contrast, measures vertical '
                                                         'overlap of the incisors.'},
                                         {'question': 'A space maintainer is indicated when?',
                                          'options': ['A) Adult chronic periodontitis needs '
                                                      'temporary splinting only',
                                                      'B) Vital bleaching requires tray retention',
                                                      'C) Premature loss of a primary tooth risks '
                                                      'space loss for the successor',
                                                      'D) Direct pulp capping is planned on a '
                                                      'permanent molar'],
                                          'answer': 'C) Premature loss of a primary tooth risks '
                                                    'space loss for the successor',
                                          'explanation': 'Early loss of a primary tooth allows '
                                                         'adjacent teeth to drift into the '
                                                         'edentulous space, shortening arch length '
                                                         'and risking impaction or crowding of the '
                                                         'successor. A space maintainer holds the '
                                                         'mesiodistal dimension until the '
                                                         'permanent tooth erupts.'}],
                                'medium': [{'question': 'A unilateral posterior crossbite with a '
                                                        'functional mandibular shift most '
                                                        'suggests?',
                                            'options': ['A) Isolated random oral habit without '
                                                        'occlusal cause',
                                                        'B) Fluorosis mottling as the primary '
                                                        'etiology',
                                                        'C) Interproximal caries alone without '
                                                        'occlusal interference',
                                                        'D) Premature contact or occlusal '
                                                        'interference deflecting closure'],
                                            'answer': 'D) Premature contact or occlusal '
                                                      'interference deflecting closure',
                                            'explanation': 'A unilateral posterior crossbite with '
                                                           'a mandibular functional shift often '
                                                           'results from a premature occlusal '
                                                           'contact that deflects the mandible on '
                                                           'closure. The shift can produce '
                                                           'asymmetric growth and must be '
                                                           'distinguished from a true skeletal '
                                                           'asymmetry.'},
                                           {'question': 'Anchorage in orthodontics means?',
                                            'options': ['A) Wire cross-section dimension alone',
                                                        'B) Resistance to unwanted reciprocal '
                                                        'tooth movement',
                                                        'C) Bracket ceramic shade selection',
                                                        'D) Elastomeric ligature flavor '
                                                        'preference'],
                                            'answer': 'B) Resistance to unwanted reciprocal tooth '
                                                      'movement',
                                            'explanation': 'Anchorage is the resistance to '
                                                           'unwanted reciprocal tooth movement '
                                                           'that Newton’s third law would '
                                                           'otherwise produce during orthodontic '
                                                           'force application. Without adequate '
                                                           'anchorage, active teeth move as '
                                                           'intended but reactive units drift '
                                                           'undesirably.'},
                                           {'question': 'Prolonged thumb sucking in the mixed '
                                                        'dentition most commonly contributes to?',
                                            'options': ['A) Bilateral mandibular tori',
                                                        'B) Dens invaginatus of lateral incisors',
                                                        'C) Enamel pearl formation at furcations',
                                                        'D) Anterior open bite and proclined '
                                                        'maxillary incisors'],
                                            'answer': 'D) Anterior open bite and proclined '
                                                      'maxillary incisors',
                                            'explanation': 'Prolonged non-nutritive sucking '
                                                           'generates forward and intrusive forces '
                                                           'on the maxillary incisors and impedes '
                                                           'normal eruption of the anteriors. The '
                                                           'resulting dentoalveolar changes '
                                                           'commonly include anterior open bite '
                                                           'and proclined upper incisors.'}],
                                'hard': [{'question': 'External apical root resorption risk during '
                                                      'orthodontics increases most with?',
                                          'options': ['A) Alcohol-free mouthwash use',
                                                      'B) Choice of toothpaste brand',
                                                      'C) Daily flossing technique alone',
                                                      'D) Heavy prolonged forces and certain root '
                                                      'morphologies'],
                                          'answer': 'D) Heavy prolonged forces and certain root '
                                                    'morphologies',
                                          'explanation': 'Orthodontic tooth movement depends on '
                                                         'controlled periodontal ligament stress; '
                                                         'heavy or prolonged forces can trigger '
                                                         'sterile inflammation and clastic '
                                                         'activity on the root surface. External '
                                                         'apical root resorption risk also rises '
                                                         'with pipette-shaped roots and prior '
                                                         'trauma.'},
                                         {'question': 'Serial extraction in orthodontics refers '
                                                      'to?',
                                          'options': ['A) Extraction of all third molars as a sole '
                                                      'protocol',
                                                      'B) A guided sequence of primary then '
                                                      'selected permanent extractions for severe '
                                                      'crowding',
                                                      'C) A series of nonsurgical root canal '
                                                      'treatments',
                                                      'D) Repeated full-mouth scaling appointments '
                                                      'only'],
                                          'answer': 'B) A guided sequence of primary then selected '
                                                    'permanent extractions for severe crowding',
                                          'explanation': 'Serial extraction is a planned sequence '
                                                         'of primary and then selected permanent '
                                                         'tooth removals in the mixed dentition '
                                                         'when severe crowding is inevitable. The '
                                                         'goal is to guide eruption into a more '
                                                         'favorable alignment and reduce later '
                                                         'mechanotherapy complexity.'},
                                         {'question': 'Temporary anchorage devices (TADs) '
                                                      'primarily provide?',
                                          'options': ['A) Sustained fluoride release into enamel',
                                                      'B) Chairside vital bleaching activation',
                                                      'C) Skeletal anchorage independent of '
                                                      'reciprocal tooth support',
                                                      'D) Local anesthetic depot for soft tissue'],
                                          'answer': 'C) Skeletal anchorage independent of '
                                                    'reciprocal tooth support',
                                          'explanation': 'Temporary anchorage devices (TADs) are '
                                                         'mini-implants or plates fixed to bone to '
                                                         'provide absolute or near-absolute '
                                                         'anchorage. Because they do not rely on '
                                                         'reciprocal tooth support, they allow '
                                                         'force systems that would otherwise tip '
                                                         'or move anchor teeth.'}],
                                'extreme': [{'question': 'Orthodontic treatment in a patient with '
                                                         'severe periodontitis most appropriately '
                                                         'requires?',
                                             'options': ['A) Immediate heavy rapid maxillary '
                                                         'expansion regardless of inflammation',
                                                         'B) Ignoring radiographic bone levels '
                                                         'during force application',
                                                         'C) Extracting all remaining teeth before '
                                                         'any orthodontics',
                                                         'D) Periodontal disease control first, '
                                                         'light forces, and perio co-management'],
                                             'answer': 'D) Periodontal disease control first, '
                                                       'light forces, and perio co-management',
                                             'explanation': 'Periodontitis involves plaque-driven '
                                                            'inflammation and progressive '
                                                            'attachment loss; orthodontic forces '
                                                            'applied through an inflamed '
                                                            'periodontium can accelerate '
                                                            'destruction. Disease control (biofilm '
                                                            'management and inflammation '
                                                            'resolution) must precede carefully '
                                                            'monitored light forces with '
                                                            'periodontal co-management.'},
                                            {'question': 'An ectopically erupting maxillary canine '
                                                         'close to adjacent roots most threatens?',
                                             'options': ['A) Root resorption of adjacent incisors',
                                                         'B) Cutaneous freckling of the facial '
                                                         'skin',
                                                         'C) Geographic tongue on the dorsum',
                                                         'D) Hairy tongue from papilla elongation'],
                                             'answer': 'A) Root resorption of adjacent incisors',
                                             'explanation': 'An ectopically erupting maxillary '
                                                            'canine can physically resorb the '
                                                            'roots of adjacent lateral or central '
                                                            'incisors through direct contact and '
                                                            'pressure. The risk rises when the '
                                                            'canine crown overlies the incisor '
                                                            'roots on imaging and warrants timely '
                                                            'interceptive management.'},
                                            {'question': 'Choosing surgical orthodontics versus '
                                                         'camouflage for skeletal Class III most '
                                                         'weighs?',
                                             'options': ['A) Bracket brand and prescription alone',
                                                         'B) Archwire alloy metallurgy alone',
                                                         'C) Growth status, severity, facial '
                                                         'profile, and occlusal discrepancy',
                                                         'D) Length of each appointment slot '
                                                         'alone'],
                                             'answer': 'C) Growth status, severity, facial '
                                                       'profile, and occlusal discrepancy',
                                             'explanation': 'Class III malocclusion may be dental, '
                                                            'skeletal, or combined; treatment '
                                                            'choice depends on remaining growth, '
                                                            'skeletal severity, soft-tissue '
                                                            'profile, and occlusal discrepancy. '
                                                            'Mild dental Class III may be '
                                                            'camouflaged, whereas severe skeletal '
                                                            'discrepancies often need orthognathic '
                                                            'surgery after growth assessment.'}]},
                  'cases': {'easy': [{'title': 'Crowding in Teen',
                                      'stem': 'A 14-year-old has moderate crowding and Class I '
                                              'molars. Oral hygiene is good.',
                                      'question': 'First planning idea?',
                                      'answer': 'Comprehensive orthodontic assessment (records, '
                                                'growth, hygiene).',
                                      'discussion': 'Treatment options depend on space analysis.',
                                      'book_hint': "Proffit's Contemporary Orthodontics"}],
                            'medium': [{'title': 'Anterior Crossbite Child',
                                        'stem': 'An 8-year-old has one upper incisor in crossbite '
                                                'with a shift on closing.',
                                        'question': 'Concern?',
                                        'answer': 'Functional shift from interference — early '
                                                  'correction often indicated.',
                                        'discussion': 'Prevent asymmetric growth habits.',
                                        'book_hint': "Proffit's Contemporary Orthodontics"}],
                            'hard': [{'title': 'Adult Relapse After Retainers Lost',
                                      'stem': 'A 28-year-old stopped wearing retainers and '
                                              'crowding returned. Choose the safest high-yield '
                                              'next concept before definitive results.',
                                      'question': 'Teaching point?',
                                      'answer': 'Relapse risk is lifelong for many; retention is '
                                                'part of treatment.',
                                      'discussion': 'Discuss retreatment vs limited alignment.',
                                      'book_hint': "Proffit's Contemporary Orthodontics"}],
                            'extreme': [{'title': 'Growing Class III with Functional Shift',
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
 'periodontics': {'label': 'Periodontics',
                  'books': ["Carranza's Clinical Periodontology",
                            "Lindhe's Clinical Periodontology",
                            'Periodontology at a Glance'],
                  'pdf_notes': ['Gingivitis reversible; periodontitis has attachment loss.',
                                'Biofilm disruption is the foundation of care.',
                                'Smoking increases severity and masks bleeding.',
                                'Re-evaluate after nonsurgical therapy.',
                                'NUG: pain, bleeding, necrosis of papillae.'],
                  'questions': {'easy': [{'question': 'Main cause of plaque-induced gingivitis?',
                                          'options': ['A) Dental biofilm at the gingival margin',
                                                      'B) Angle Class II malocclusion alone',
                                                      'C) Dens evaginatus of premolars',
                                                      'D) Torus palatinus presence'],
                                          'answer': 'A) Dental biofilm at the gingival margin',
                                          'explanation': 'Plaque-induced gingivitis is an '
                                                         'inflammatory response of the gingiva to '
                                                         'accumulation of dental biofilm at the '
                                                         'gingival margin. Microbial products '
                                                         'trigger vascular dilation, leukocyte '
                                                         'infiltration, and clinical erythema and '
                                                         'bleeding that reverse with effective '
                                                         'plaque control.'},
                                         {'question': 'Clinical hallmark distinguishing '
                                                      'periodontitis from gingivitis?',
                                          'options': ['A) Reversible marginal redness without '
                                                      'attachment loss',
                                                      'B) Clinical attachment loss and alveolar '
                                                      'bone loss',
                                                      'C) Extrinsic stain without inflammation',
                                                      'D) Calculus deposits without any '
                                                      'inflammatory response'],
                                          'answer': 'B) Clinical attachment loss and alveolar bone '
                                                    'loss',
                                          'explanation': 'Gingivitis is inflammation confined to '
                                                         'the soft tissue, whereas periodontitis '
                                                         'is defined by destruction of the '
                                                         'periodontal ligament and alveolar bone, '
                                                         'measured as clinical attachment loss. '
                                                         'Pocketing and radiographic bone loss '
                                                         'corroborate the diagnosis.'},
                                         {'question': 'Best foundation for daily plaque control?',
                                          'options': ['A) Whitening strips as the sole hygiene '
                                                      'method',
                                                      'B) Chewing ice to abrade plaque',
                                                      'C) Toothbrushing with interdental cleaning',
                                                      'D) Charcoal powder alone without brushing '
                                                      'technique'],
                                          'answer': 'C) Toothbrushing with interdental cleaning',
                                          'explanation': 'Dental biofilm must be disrupted '
                                                         'mechanically because saliva and rinses '
                                                         'alone do not remove adherent plaque from '
                                                         'tooth surfaces. Toothbrushing cleans '
                                                         'facial and lingual surfaces; interdental '
                                                         'aids clean proximal niches where '
                                                         'periodontitis often begins.'}],
                                'medium': [{'question': 'Furcation involvement is assessed on '
                                                        'which teeth?',
                                            'options': ['A) Maxillary central incisors',
                                                        'B) Mandibular canines',
                                                        'C) Primary lateral incisors',
                                                        'D) Multirooted teeth such as molars'],
                                            'answer': 'D) Multirooted teeth such as molars',
                                            'explanation': 'Furcation involvement is pathologic '
                                                           'bone loss between the roots of '
                                                           'multirooted teeth, exposing the '
                                                           'furcation entrance. Single-rooted '
                                                           'teeth lack furcations, so this '
                                                           'assessment applies to molars and some '
                                                           'premolars with bifurcated roots.'},
                                           {'question': 'How does smoking typically affect '
                                                        'periodontitis?',
                                            'options': ['A) Protects clinical attachment '
                                                        'indefinitely',
                                                        'B) Increases risk and severity while '
                                                        'masking bleeding',
                                                        'C) Naturally whitens roots without tissue '
                                                        'effect',
                                                        'D) Has no measurable effect on '
                                                        'periodontal disease'],
                                            'answer': 'B) Increases risk and severity while '
                                                      'masking bleeding',
                                            'explanation': 'Tobacco smoking impairs neutrophil '
                                                           'function, reduces gingival blood flow, '
                                                           'and alters cytokine responses, '
                                                           'increasing periodontitis risk and '
                                                           'severity. Reduced vascularity also '
                                                           'masks gingival bleeding, so disease '
                                                           'may look less inflamed than it is.'},
                                           {'question': 'Rapidly progressive periodontitis in a '
                                                        'young patient historically associated '
                                                        'with which theme?',
                                            'options': ['A) Cervical abrasion from brushing alone',
                                                        'B) Enamel fluorosis without attachment '
                                                        'change',
                                                        'C) Occlusal attrition as the sole cause '
                                                        'of bone loss',
                                                        'D) Severe attachment loss out of '
                                                        'proportion to deposits, with A. '
                                                        'actinomycetemcomitans often discussed'],
                                            'answer': 'D) Severe attachment loss out of proportion '
                                                      'to deposits, with A. actinomycetemcomitans '
                                                      'often discussed',
                                            'explanation': 'Rapidly progressive periodontitis in '
                                                           'young patients (historically localized '
                                                           'aggressive periodontitis) features '
                                                           'severe attachment loss out of '
                                                           'proportion to local deposits. '
                                                           'Aggregatibacter actinomycetemcomitans '
                                                           'has been classically associated in '
                                                           'many cases, though staging/grading '
                                                           'frameworks now emphasize rate and risk '
                                                           'factors.'}],
                                'hard': [{'question': 'Urgent care of a periodontal abscess most '
                                                      'appropriately includes?',
                                          'options': ['A) Drainage and debridement, with '
                                                      'antimicrobials if systemic signs',
                                                      'B) Home bleaching tray use alone',
                                                      'C) Orthodontic wax over the gingival margin',
                                                      'D) Lifelong nightguard wear without local '
                                                      'therapy'],
                                          'answer': 'A) Drainage and debridement, with '
                                                    'antimicrobials if systemic signs',
                                          'explanation': 'A periodontal abscess is a localized '
                                                         'purulent infection within a periodontal '
                                                         'pocket or furcation. Drainage of pus, '
                                                         'debridement of the pocket, and systemic '
                                                         'antimicrobials when there are fever or '
                                                         'spreading infection constitute '
                                                         'appropriate urgent care.'},
                                         {'question': 'Peri-implantitis is characterized by?',
                                          'options': ['A) Soft-tissue inflammation without '
                                                      'progressive bone loss (mucositis only)',
                                                      'B) Food impaction without any inflammatory '
                                                      'signs',
                                                      'C) Inflammation plus progressive crestal '
                                                      'bone loss around an implant',
                                                      'D) Crown shade mismatch without biologic '
                                                      'change'],
                                          'answer': 'C) Inflammation plus progressive crestal bone '
                                                    'loss around an implant',
                                          'explanation': 'Peri-implant mucositis is reversible '
                                                         'soft-tissue inflammation around an '
                                                         'implant without progressive bone loss. '
                                                         'Peri-implantitis adds progressive '
                                                         'crestal bone loss to inflammation and '
                                                         'probing changes, threatening implant '
                                                         'survival.'},
                                         {'question': 'Occlusal trauma alone, without '
                                                      'plaque-driven inflammation, most '
                                                      'accurately?',
                                          'options': ['A) Initiates periodontitis even in a '
                                                      'plaque-free mouth',
                                                      'B) Resolves existing periodontal pockets '
                                                      'without debridement',
                                                      'C) Substitutes for mechanical plaque '
                                                      'control',
                                                      'D) Does not initiate the plaque-induced '
                                                      'periodontitis pathway'],
                                          'answer': 'D) Does not initiate the plaque-induced '
                                                    'periodontitis pathway',
                                          'explanation': 'Occlusal trauma produces adaptive or '
                                                         'pathologic changes in the periodontium '
                                                         'from excessive occlusal load, but it '
                                                         'does not initiate the plaque-induced '
                                                         'inflammatory pathway of periodontitis. '
                                                         'When inflammation is present, trauma can '
                                                         'worsen attachment loss patterns.'}],
                                'extreme': [{'question': 'Classic clinical triad of necrotizing '
                                                         'ulcerative gingivitis includes?',
                                             'options': ['A) Peg lateral morphology alone',
                                                         'B) Asymptomatic extrinsic stain alone',
                                                         'C) Dens in dente without soft-tissue '
                                                         'change',
                                                         'D) Pain, bleeding, and interdental '
                                                         'papillary necrosis with fetor'],
                                             'answer': 'D) Pain, bleeding, and interdental '
                                                       'papillary necrosis with fetor',
                                             'explanation': 'Necrotizing ulcerative gingivitis '
                                                            'presents with painful punched-out '
                                                            'interdental papillae, spontaneous '
                                                            'bleeding, and often fetor oris. '
                                                            'Fusospirochetal overgrowth in a host '
                                                            'compromised by stress, smoking, or '
                                                            'immunosuppression underlies the '
                                                            'syndrome.'},
                                            {'question': 'A pregnancy epulis is best described as?',
                                             'options': ['A) Malignant melanoma until proven '
                                                         'otherwise in every case',
                                                         'B) A pyogenic granuloma variant that '
                                                         'often regresses postpartum',
                                                         'C) A primary osteosarcoma of the '
                                                         'alveolar ridge',
                                                         'D) An odontogenic caries lesion of '
                                                         'enamel'],
                                             'answer': 'B) A pyogenic granuloma variant that often '
                                                       'regresses postpartum',
                                             'explanation': 'A pregnancy epulis is a pyogenic '
                                                            'granuloma arising from gingiva under '
                                                            'the influence of elevated pregnancy '
                                                            'hormones and local irritants. It is a '
                                                            'reactive vascular lesion, not a true '
                                                            'neoplasm, and frequently regresses '
                                                            'after delivery once irritants are '
                                                            'controlled.'},
                                            {'question': 'Guided tissue regeneration aims '
                                                         'primarily for?',
                                             'options': ['A) Extrinsic stain removal from enamel',
                                                         'B) Enamel microabrasion for white-spot '
                                                         'lesions',
                                                         'C) Regeneration of a new periodontal '
                                                         'attachment apparatus',
                                                         'D) Vital bleaching of the clinical '
                                                         'crown'],
                                             'answer': 'C) Regeneration of a new periodontal '
                                                       'attachment apparatus',
                                             'explanation': 'Guided tissue regeneration uses a '
                                                            'barrier membrane to exclude gingival '
                                                            'epithelium and connective tissue from '
                                                            'the periodontal defect, allowing '
                                                            'periodontal ligament and bone cells '
                                                            'to repopulate the root surface and '
                                                            'form new cementum, PDL, and bone.'}]},
                  'cases': {'easy': [{'title': 'Bleeding Gums',
                                      'stem': 'A student has bleeding on brushing, soft swollen '
                                              'gingiva, no radiographic bone loss.',
                                      'question': 'Diagnosis?',
                                      'answer': 'Plaque-induced gingivitis.',
                                      'discussion': 'OHI and prophylaxis; reversible.',
                                      'book_hint': "Carranza's Clinical Periodontology"}],
                            'medium': [{'title': 'Deep Pockets Molars',
                                        'stem': 'A 45-year-old smoker has 6–7 mm pockets on molars '
                                                'with horizontal bone loss.',
                                        'question': 'Management pillars?',
                                        'answer': 'Risk factor control, nonsurgical debridement, '
                                                  're-evaluation, surgery if indicated.',
                                        'discussion': 'Smoking cessation counseling.',
                                        'book_hint': "Carranza's Clinical Periodontology"}],
                            'hard': [{'title': 'Diabetic with Recurrent Abscesses',
                                      'stem': 'Poorly controlled diabetes, multiple periodontal '
                                              'abscesses, deep pockets. Choose the safest '
                                              'high-yield next concept before definitive results.',
                                      'question': 'Priority concept?',
                                      'answer': 'Medical coordination for glycemic control + acute '
                                                'drainage/debridement + definitive perio plan.',
                                      'discussion': 'Diabetes and perio bidirectionally interact.',
                                      'book_hint': "Carranza's Clinical Periodontology"}],
                            'extreme': [{'title': 'NUG in Stressed Student',
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
 'endodontics': {'label': 'Endodontics',
                 'books': ["Cohen's Pathways of the Pulp",
                           'Endodontics — Torabinejad',
                           "Ingle's Endodontics"],
                 'pdf_notes': ['Rubber dam is standard isolation for RCT.',
                               'Lingering spontaneous pain suggests irreversible pulpitis.',
                               'NaOCl irrigates but extrusion is dangerous.',
                               'Missed canals (MB2) cause failure.',
                               'Follow IADT for traumatic dental injuries.'],
                 'questions': {'easy': [{'question': 'Symptomatic irreversible pulpitis pain is '
                                                     'characteristically?',
                                         'options': ['A) Spontaneous and lingering to cold stimuli',
                                                     'B) Brief thermal sensitivity that resolves '
                                                     'immediately after stimulus removal',
                                                     'C) Limited to mucosal itching without '
                                                     'thermal change',
                                                     'D) Identical to a reciprocal TMJ click on '
                                                     'opening'],
                                         'answer': 'A) Spontaneous and lingering to cold stimuli',
                                         'explanation': 'Symptomatic irreversible pulpitis '
                                                        'reflects vital pulp tissue with '
                                                        'inflammation severe enough that it cannot '
                                                        'resolve even after removal of the '
                                                        'irritant. C-fiber–mediated pain is often '
                                                        'spontaneous and lingers after cold is '
                                                        'removed, guiding pulp therapy decisions.'},
                                        {'question': 'Best isolation method for root canal '
                                                     'treatment?',
                                         'options': ['A) Cotton rolls alone for the entire '
                                                     'procedure',
                                                     'B) Rubber dam isolation of the operating '
                                                     'field',
                                                     'C) No isolation if suction is available',
                                                     'D) Cheek retractor alone without a dam'],
                                         'answer': 'B) Rubber dam isolation of the operating field',
                                         'explanation': 'A rubber dam isolates the tooth from '
                                                        'saliva and oral microbes, preventing '
                                                        'contamination of the root canal system '
                                                        'during instrumentation and obturation. It '
                                                        'also protects the airway from instruments '
                                                        'and irrigants.'},
                                        {'question': 'Working length for canal preparation is '
                                                     'ideally set near?',
                                         'options': ['A) Beyond the cortical plate into the '
                                                     'maxillary sinus',
                                                     'B) The pulp horn only',
                                                     'C) The cementoenamel junction only',
                                                     'D) The apical constriction / near '
                                                     'radiographic apex per protocol'],
                                         'answer': 'D) The apical constriction / near radiographic '
                                                   'apex per protocol',
                                         'explanation': 'The apical constriction is the narrowest '
                                                        'point of the canal near the cementoenamel '
                                                        'or cementodentinal junction and is the '
                                                        'usual physiologic terminus for canal '
                                                        'preparation. Working length is set to '
                                                        'this region using electronic apex '
                                                        'location and radiographic confirmation.'}],
                               'medium': [{'question': 'A necrotic pulp with an apical '
                                                       'radiolucency most strongly suggests?',
                                           'options': ['A) Reversible pulpitis without apical '
                                                       'change',
                                                       'B) Apical periodontitis',
                                                       'C) Enamel hypoplasia of the crown',
                                                       'D) Dental fluorosis mottling'],
                                           'answer': 'B) Apical periodontitis',
                                           'explanation': 'Pulp necrosis allows bacteria and their '
                                                          'toxins to exit through apical foramina '
                                                          'into the periodontal ligament and bone. '
                                                          'The resulting inflammatory bone '
                                                          'resorption appears as a periapical '
                                                          'radiolucency and defines apical '
                                                          'periodontitis.'},
                                          {'question': 'Sodium hypochlorite is used in endodontics '
                                                       'primarily as?',
                                           'options': ['A) An obturation sealer cement',
                                                       'B) A temporary coronal filling material',
                                                       'C) An irrigant with tissue-dissolving and '
                                                       'antimicrobial action',
                                                       'D) A local anesthetic solution'],
                                           'answer': 'C) An irrigant with tissue-dissolving and '
                                                     'antimicrobial action',
                                           'explanation': 'Sodium hypochlorite dissolves necrotic '
                                                          'pulp tissue and has broad antimicrobial '
                                                          'activity against canal flora, making it '
                                                          'the primary endodontic irrigant. Its '
                                                          'cytotoxicity means extrusion beyond the '
                                                          'apex must be avoided.'},
                                          {'question': 'Cracked-tooth pain is characteristically '
                                                       'elicited on?',
                                           'options': ['A) Percussion of an adjacent unrestored '
                                                       'tooth only',
                                                       'B) Hot liquids alone without any bite '
                                                       'loading',
                                                       'C) Supine posture alone without occlusal '
                                                       'contact',
                                                       'D) Release of biting pressure on the '
                                                       'affected cusp'],
                                           'answer': 'D) Release of biting pressure on the '
                                                     'affected cusp',
                                           'explanation': 'In a cracked tooth, occlusal load '
                                                          'briefly separates the crack walls and '
                                                          'stimulates the pulp or periodontal '
                                                          'ligament; pain is characteristically '
                                                          'sharp on release of biting pressure as '
                                                          'the segments snap back together.'}],
                               'hard': [{'question': 'A sodium hypochlorite extrusion accident '
                                                     'typically presents with?',
                                         'options': ['A) Mild extrinsic enamel stain without '
                                                     'soft-tissue change',
                                                     'B) Gradual low-grade pulpitis symptoms over '
                                                     'weeks',
                                                     'C) Isolated taste alteration without pain or '
                                                     'swelling',
                                                     'D) Sudden severe pain, swelling, and '
                                                     'ecchymosis after irrigation'],
                                         'answer': 'D) Sudden severe pain, swelling, and '
                                                   'ecchymosis after irrigation',
                                         'explanation': 'Forceful extrusion of sodium hypochlorite '
                                                        'into periapical tissues causes immediate '
                                                        'chemical burns of soft tissue and '
                                                        'vessels. Patients experience sudden '
                                                        'severe pain, rapid swelling, and often '
                                                        'ecchymosis; management is supportive with '
                                                        'monitoring for airway compromise.'},
                                        {'question': 'Missing a second mesiobuccal canal (MB2) in '
                                                     'a maxillary molar most often leads to?',
                                         'options': ['A) Improved long-term prognosis in all cases',
                                                     'B) Persistent infection and treatment '
                                                     'failure risk',
                                                     'C) Cutaneous facial color change',
                                                     'D) Drug-induced gingival hyperplasia'],
                                         'answer': 'B) Persistent infection and treatment failure '
                                                   'risk',
                                         'explanation': 'Maxillary molars frequently have a second '
                                                        'mesiobuccal canal (MB2) that branches '
                                                        'within the mesiobuccal root. If '
                                                        'untreated, residual bacteria in MB2 '
                                                        'sustain periapical inflammation and cause '
                                                        'post-treatment disease.'},
                                        {'question': 'Prognosis of a complete vertical root '
                                                     'fracture is often?',
                                         'options': ['A) Excellent healing with nonsurgical RCT '
                                                     'alone',
                                                     'B) Observation without intervention '
                                                     'indefinitely',
                                                     'C) Poor, with extraction commonly required',
                                                     'D) Resolved by internal bleaching alone'],
                                         'answer': 'C) Poor, with extraction commonly required',
                                         'explanation': 'A complete vertical root fracture '
                                                        'separates the root along its long axis, '
                                                        'creating a pathway for bacteria from the '
                                                        'oral cavity into the periodontium. The '
                                                        'resulting localized deep pocket and bone '
                                                        'loss rarely heal with root canal therapy '
                                                        'alone; extraction is often necessary.'}],
                               'extreme': [{'question': 'An avulsed permanent tooth with extraoral '
                                                        'dry time greater than 60 minutes most '
                                                        'implies?',
                                            'options': ['A) Excellent PDL viability and unchanged '
                                                        'prognosis',
                                                        'B) That dry time is irrelevant if the '
                                                        'tooth is replanted',
                                                        'C) Identical management rules as for '
                                                        'primary teeth',
                                                        'D) Poor PDL viability and worsened '
                                                        'prognosis; manage per trauma guidelines'],
                                            'answer': 'D) Poor PDL viability and worsened '
                                                      'prognosis; manage per trauma guidelines',
                                            'explanation': 'Periodontal ligament cells on an '
                                                           'avulsed tooth die progressively with '
                                                           'extraoral dry time; beyond about 60 '
                                                           'minutes of dry storage, PDL viability '
                                                           'is severely compromised. Replantation '
                                                           'may still be attempted after surface '
                                                           'management, but ankylosis and '
                                                           'replacement resorption risks are '
                                                           'high.'},
                                           {'question': 'A true combined perio-endo lesion most '
                                                        'appropriately requires?',
                                            'options': ['A) Addressing both endodontic and '
                                                        'periodontal infection pathways',
                                                        'B) Scaling alone without pulp testing',
                                                        'C) Orthodontic alignment as sole therapy',
                                                        'D) Vital tooth whitening as definitive '
                                                        'care'],
                                            'answer': 'A) Addressing both endodontic and '
                                                      'periodontal infection pathways',
                                            'explanation': 'Combined perio-endo lesions involve '
                                                           'communication between pulpal and '
                                                           'periodontal infection pathways, so '
                                                           'both niches must be disinfected for '
                                                           'healing. When the primary source is '
                                                           'endodontic, root canal treatment often '
                                                           'precedes definitive periodontal '
                                                           'therapy.'},
                                           {'question': 'Internal versus external root resorption '
                                                        'is distinguished clinically because?',
                                            'options': ['A) They share identical radiographic '
                                                        'outlines and identical treatment',
                                                        'B) Both resolve spontaneously without '
                                                        'intervention',
                                                        'C) Radiographic and clinical patterns '
                                                        'differ and treatment differs',
                                                        'D) Extraction is required before any '
                                                        'imaging or vitality testing'],
                                            'answer': 'C) Radiographic and clinical patterns '
                                                      'differ and treatment differs',
                                            'explanation': 'Internal resorption begins within the '
                                                           'pulp chamber or canal from inflamed '
                                                           'pulp tissue and appears as a ballooned '
                                                           'canal outline that moves with tube '
                                                           'shift less than external defects. '
                                                           'External cervical resorption begins on '
                                                           'the root surface; diagnosis directs '
                                                           'whether pulp therapy, repair, or '
                                                           'extraction is indicated.'}]},
                 'cases': {'easy': [{'title': 'Night Pain Lower Molar',
                                     'stem': 'Spontaneous night pain, lingering cold response, no '
                                             'periapical radiolucency yet.',
                                     'question': 'Likely pulp status?',
                                     'answer': 'Symptomatic irreversible pulpitis.',
                                     'discussion': 'RCT or extraction after consent.',
                                     'book_hint': "Cohen's Pathways of the Pulp"}],
                           'medium': [{'title': 'Sinus Tract on Gingiva',
                                       'stem': 'Chronic draining sinus over apex of nonvital '
                                               'lateral; radiolucency present.',
                                       'question': 'Treatment concept?',
                                       'answer': 'Root canal therapy of the source tooth (+ '
                                                 'restore).',
                                       'discussion': 'Trace sinus with gutta-percha if needed.',
                                       'book_hint': "Cohen's Pathways of the Pulp"}],
                           'hard': [{'title': 'RCT Done but Pain Persists',
                                     'stem': 'Upper 6 had RCT; pain on biting persists; J-shaped '
                                             'lesion on root. Choose the safest high-yield next '
                                             'concept before definitive results.',
                                     'question': 'Suspect?',
                                     'answer': 'Vertical root fracture or missed canal / '
                                               'perio-endo complex — investigate carefully.',
                                     'discussion': 'CBCT may help; avoid endless retreat without '
                                                   'diagnosis.',
                                     'book_hint': "Cohen's Pathways of the Pulp"}],
                           'extreme': [{'title': 'Avulsion on Sports Field',
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
 'prosthodontics': {'label': 'Prosthodontics',
                    'books': ['Contemporary Fixed Prosthodontics — Rosenstiel',
                              "McCracken's Removable Partial Prosthodontics",
                              'Complete Denture Prosthodontics texts'],
                    'pdf_notes': ['Ferrule improves crowned endodontically treated teeth.',
                                  'Respect biologic width / supracrestal tissues.',
                                  'Kennedy classification guides RPD design.',
                                  'Passive fit matters for implant frameworks.',
                                  'Disease control before full-mouth reconstruction.'],
                    'questions': {'easy': [{'question': 'The ferrule effect primarily improves?',
                                            'options': ['A) Fracture resistance of crowned '
                                                        'endodontically treated teeth',
                                                        'B) Shade matching of ceramic veneers '
                                                        'alone',
                                                        'C) Color stability of dual-cure cement '
                                                        'alone',
                                                        'D) Adhesion of impression tray adhesive '
                                                        'alone'],
                                            'answer': 'A) Fracture resistance of crowned '
                                                      'endodontically treated teeth',
                                            'explanation': 'A ferrule is a band of sound axial '
                                                           'tooth structure of adequate height and '
                                                           'thickness encircled by the crown '
                                                           'margin. It braces the tooth against '
                                                           'functional lever forces, reducing the '
                                                           'risk of root fracture after '
                                                           'post-and-core restoration.'},
                                           {'question': 'Kennedy Class I removable partial denture '
                                                        'describes?',
                                            'options': ['A) A single bounded tooth-supported space '
                                                        'only',
                                                        'B) Bilateral distal-extension edentulous '
                                                        'areas',
                                                        'C) An anterior bounded edentulous span '
                                                        'only',
                                                        'D) A complete denture opposing natural '
                                                        'teeth'],
                                            'answer': 'B) Bilateral distal-extension edentulous '
                                                      'areas',
                                            'explanation': 'Kennedy Class I describes a bilateral '
                                                           'edentulous area posterior to the '
                                                           'remaining natural teeth (bilateral '
                                                           'distal extension). Because terminal '
                                                           'abutments are absent, the denture base '
                                                           'is supported largely by mucosa and '
                                                           'requires careful design to control '
                                                           'rotation.'},
                                           {'question': 'A final impression for a cast crown most '
                                                        'critically needs?',
                                            'options': ['A) Alginate as the only acceptable final '
                                                        'material for PFM',
                                                        'B) A wax interocclusal record alone '
                                                        'without margins',
                                                        'C) Accurate finish-line capture with '
                                                        'soft-tissue management',
                                                        'D) A shade-tab photograph as a substitute '
                                                        'for the impression'],
                                            'answer': 'C) Accurate finish-line capture with '
                                                      'soft-tissue management',
                                            'explanation': 'Cast restorations depend on an '
                                                           'impression that records the finish '
                                                           'line in undistorted detail and relates '
                                                           'soft tissues without tears or voids. '
                                                           'Hemostasis, cord or paste retraction, '
                                                           'and moisture control are essential for '
                                                           'margin fidelity.'}],
                                  'medium': [{'question': 'Violation of biologic width '
                                                          '(supracrestal tissue attachment) by a '
                                                          'restoration margin may cause?',
                                              'options': ['A) Improved papilla fill without '
                                                          'inflammation',
                                                          'B) Faster orthodontic tooth movement',
                                                          'C) Enhanced bleaching efficacy',
                                                          'D) Chronic inflammation and crestal '
                                                          'bone loss'],
                                              'answer': 'D) Chronic inflammation and crestal bone '
                                                        'loss',
                                              'explanation': 'Supracrestal tissue attachment '
                                                             '(biological width) is the combined '
                                                             'junctional epithelium and connective '
                                                             'tissue attachment coronal to '
                                                             'alveolar crest. Placing a '
                                                             'restoration margin that invades this '
                                                             'zone commonly produces persistent '
                                                             'inflammation and crestal bone '
                                                             'remodeling.'},
                                             {'question': 'A key biomechanical difference between '
                                                          'an implant abutment and a natural tooth '
                                                          'is?',
                                              'options': ['A) Identical proprioception and '
                                                          'mobility profiles',
                                                          'B) Absence of a PDL with different '
                                                          'mobility and feedback',
                                                          'C) Greater physiologic mobility than '
                                                          'natural teeth',
                                                          'D) A periodontal ligament identical to '
                                                          'natural teeth'],
                                              'answer': 'B) Absence of a PDL with different '
                                                        'mobility and feedback',
                                              'explanation': 'Natural teeth are suspended by a '
                                                             'periodontal ligament that provides '
                                                             'proprioception and physiologic '
                                                             'mobility; osseointegrated implants '
                                                             'are ankylosed to bone without a PDL. '
                                                             'Occlusal forces are therefore '
                                                             'transmitted more directly to bone '
                                                             'and lack the same protective '
                                                             'feedback.'},
                                             {'question': 'An immediate denture is delivered when?',
                                              'options': ['A) At the extraction appointment after '
                                                          'prior fabrication',
                                                          'B) After complete ridge remodeling '
                                                          'months later as a conventional complete '
                                                          'denture',
                                                          'C) Before any clinical examination or '
                                                          'records',
                                                          'D) As a substitute Hawley retainer '
                                                          'during orthodontic retention'],
                                              'answer': 'A) At the extraction appointment after '
                                                        'prior fabrication',
                                              'explanation': 'An immediate denture is fabricated '
                                                             'before extractions and inserted at '
                                                             'the same appointment the teeth are '
                                                             'removed. It maintains appearance and '
                                                             'limited function during healing '
                                                             'while acting as a protective '
                                                             'dressing for the sockets.'}],
                                  'hard': [{'question': 'A principal risk of a cantilever fixed '
                                                        'dental prosthesis is?',
                                            'options': ['A) Reduced abutment stress compared with '
                                                        'a conventional fixed-fixed bridge',
                                                        'B) Lower cement failure risk than any '
                                                        'tooth-supported FDP',
                                                        'C) Superior long-term survival versus a '
                                                        'single-tooth implant in all cases',
                                                        'D) Leverage overload and stress '
                                                        'concentration on abutments'],
                                            'answer': 'D) Leverage overload and stress '
                                                      'concentration on abutments',
                                            'explanation': 'A cantilever fixed dental prosthesis '
                                                           'has an abutment at only one end of the '
                                                           'pontic, creating a class I lever under '
                                                           'occlusal load. Moments concentrate '
                                                           'stress in the abutment tooth, cement '
                                                           'lute, and periodontium, elevating '
                                                           'failure risk if span and occlusion are '
                                                           'unfavorable.'},
                                           {'question': 'Comparing cement-retained and '
                                                        'screw-retained implant crowns, a central '
                                                        'clinical tradeoff is?',
                                            'options': ['A) That no clinical differences exist '
                                                        'between retention modes',
                                                        'B) Cement excess control versus '
                                                        'screw-access esthetics and retrievability',
                                                        'C) That subgingival cement is easier to '
                                                        'remove than supragingival cement',
                                                        'D) That screw-retained crowns eliminate '
                                                        'all prosthetic complications'],
                                            'answer': 'B) Cement excess control versus '
                                                      'screw-access esthetics and retrievability',
                                            'explanation': 'Cement-retained implant crowns can '
                                                           'offer esthetic continuity without an '
                                                           'occlusal screw access hole, but excess '
                                                           'subgingival cement is difficult to '
                                                           'remove and is strongly linked to '
                                                           'peri-implant inflammation. Screw '
                                                           'retention improves retrievability at '
                                                           'the cost of an access channel.'},
                                           {'question': 'Surveying a removable partial denture '
                                                        'cast primarily determines?',
                                            'options': ['A) Ceramic shade prescription',
                                                        'B) Patient chronologic age',
                                                        'C) Path of insertion and usable undercuts',
                                                        'D) Maximum voluntary bite force'],
                                            'answer': 'C) Path of insertion and usable undercuts',
                                            'explanation': 'Surveying orients a diagnostic cast to '
                                                           'a chosen path of insertion and '
                                                           'identifies soft- and hard-tissue '
                                                           'undercuts relative to that path. Clasp '
                                                           'tips are then placed in measured '
                                                           'undercut, guiding planes are planned, '
                                                           'and interferences are eliminated.'}],
                                  'extreme': [{'question': 'Full-mouth rehabilitation sequencing '
                                                           'most appropriately prioritizes?',
                                               'options': ['A) Immediate definitive zirconia '
                                                           'without diagnosis',
                                                           'B) Esthetic shade selection before '
                                                           'caries and periodontal control',
                                                           'C) Extraction of all teeth without '
                                                           'informed consent',
                                                           'D) Disease control, VDO/occlusion '
                                                           'planning, provisionals, then finals'],
                                               'answer': 'D) Disease control, VDO/occlusion '
                                                         'planning, provisionals, then finals',
                                               'explanation': 'Full-mouth rehabilitation fails if '
                                                              'active caries or periodontitis '
                                                              'undermines new restorations, so '
                                                              'disease control comes first. '
                                                              'Vertical dimension, occlusal '
                                                              'scheme, and esthetics are then '
                                                              'tested in provisionals before '
                                                              'committing to definitive '
                                                              'restorations.'},
                                              {'question': 'Combination syndrome classically '
                                                           'relates to?',
                                               'options': ['A) An edentulous maxilla opposing '
                                                           'mandibular anterior natural teeth',
                                                           'B) Skeletal Class III orthodontic '
                                                           'camouflage alone',
                                                           'C) Dens invaginatus of maxillary '
                                                           'laterals',
                                                           'D) A mesiodens in the midline'],
                                               'answer': 'A) An edentulous maxilla opposing '
                                                         'mandibular anterior natural teeth',
                                               'explanation': 'Combination syndrome classically '
                                                              'occurs with a complete maxillary '
                                                              'denture opposing mandibular '
                                                              'anterior natural teeth (often with '
                                                              'missing posterior support). Heavy '
                                                              'anterior occlusal forces drive '
                                                              'flabby anterior maxillary ridge, '
                                                              'papillary hyperplasia, and '
                                                              'mandibular overeruption patterns.'},
                                              {'question': 'Passive fit of an implant framework '
                                                           'means?',
                                               'options': ['A) Forced seating of a misfitting '
                                                           'framework is acceptable',
                                                           'B) Cement lute compensates safely for '
                                                           'any framework distortion',
                                                           'C) The framework seats without '
                                                           'inducing strain on implants',
                                                           'D) Shade match alone determines '
                                                           'clinical acceptability of fit'],
                                               'answer': 'C) The framework seats without inducing '
                                                         'strain on implants',
                                               'explanation': 'Passive fit means an implant '
                                                              'framework seats on abutments '
                                                              'without inducing tensile or '
                                                              'compressive strain in the screws or '
                                                              'peri-implant bone. Casting or '
                                                              'scanning distortion that leaves a '
                                                              'misfit creates preload problems, '
                                                              'screw loosening, and bone '
                                                              'stress.'}]},
                    'cases': {'easy': [{'title': 'Broken Molar Crown',
                                        'stem': 'A patient wants a crown on a root-filled molar '
                                                'with adequate ferrule.',
                                        'question': 'Plan outline?',
                                        'answer': 'Assess restorability, post if needed, core, '
                                                  'crown.',
                                        'discussion': 'Extract if unrestorable.',
                                        'book_hint': 'Contemporary Fixed Prosthodontics — '
                                                     'Rosenstiel'}],
                              'medium': [{'title': 'Distal Extension RPD Rocks',
                                          'stem': 'Kennedy I lower RPD rocks and sore spots on '
                                                  'ridge.',
                                          'question': 'Likely issue?',
                                          'answer': 'Support/retention/occlusion imbalance on '
                                                    'distal extension — adjust base, rests, '
                                                    'occlusion.',
                                          'discussion': 'Tissue-borne areas need careful loading.',
                                          'book_hint': 'Contemporary Fixed Prosthodontics — '
                                                       'Rosenstiel'}],
                              'hard': [{'title': 'Deep Margin Near Bone',
                                        'stem': 'Crown prep finish line violates biologic width '
                                                'with persistent bleeding. Choose the safest '
                                                'high-yield next concept before definitive '
                                                'results.',
                                        'question': 'Options?',
                                        'answer': 'Crown lengthening or orthodontic extrusion '
                                                  'before final restoration.',
                                        'discussion': 'Do not cement and hope.',
                                        'book_hint': 'Contemporary Fixed Prosthodontics — '
                                                     'Rosenstiel'}],
                              'extreme': [{'title': 'Failing Full Arch Hybrids',
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
 'pediatric_dentistry': {'label': 'Pediatric Dentistry',
                         'books': ["McDonald and Avery's Dentistry for the Child and Adolescent",
                                   'Paediatric Dentistry — Welbury',
                                   'Clinical Cases in Pediatric Dentistry'],
                         'pdf_notes': ['20 primary teeth; first permanent molar about age 6.',
                                       'ECC often affects maxillary anteriors with bottle habits.',
                                       'SSC common for multi-surface primary molar caries.',
                                       'Generally do not replant avulsed primary teeth.',
                                       'Safeguarding: inconsistent injury histories.'],
                         'questions': {'easy': [{'question': 'Which permanent tooth most often '
                                                             'erupts first?',
                                                 'options': ['A) Mandibular first molar around age '
                                                             '6 years',
                                                             'B) Third molar around age 3 years',
                                                             'C) Maxillary lateral incisor at age '
                                                             '2 years',
                                                             'D) Permanent canine at 4 months of '
                                                             'age'],
                                                 'answer': 'A) Mandibular first molar around age 6 '
                                                           'years',
                                                 'explanation': 'The mandibular first permanent '
                                                                'molars typically erupt around age '
                                                                'six and are often the first '
                                                                'permanent teeth to appear, distal '
                                                                'to the primary second molars. '
                                                                'They establish the foundation of '
                                                                'the permanent occlusion.'},
                                                {'question': 'Professional fluoride varnish '
                                                             'primarily helps prevent?',
                                                 'options': ['A) Angle Class II malocclusion',
                                                             'B) Dental caries',
                                                             'C) Primary tooth ankylosis',
                                                             'D) Supernumerary tooth formation'],
                                                 'answer': 'B) Dental caries',
                                                 'explanation': 'Fluoride varnish delivers a high '
                                                                'fluoride concentration that '
                                                                'promotes remineralization of '
                                                                'enamel and forms calcium '
                                                                'fluoride–like reservoirs on the '
                                                                'tooth surface. Repeated '
                                                                'professional application reduces '
                                                                'caries incidence in children at '
                                                                'risk.'},
                                                {'question': 'Pulpotomy in pediatric dentistry is '
                                                             'most often indicated for?',
                                                 'options': ['A) Adult implant sites with '
                                                             'peri-implantitis',
                                                             'B) Orthodontic enamel etching only',
                                                             'C) A restorable primary tooth with '
                                                             'inflamed coronal pulp and healthy '
                                                             'radicular pulp',
                                                             'D) Vital bleaching of permanent '
                                                             'anteriors'],
                                                 'answer': 'C) A restorable primary tooth with '
                                                           'inflamed coronal pulp and healthy '
                                                           'radicular pulp',
                                                 'explanation': 'Pulpotomy removes inflamed '
                                                                'coronal pulp while preserving '
                                                                'radicular pulp vitality in a '
                                                                'restorable primary tooth, usually '
                                                                'after carious or traumatic '
                                                                'exposure with healthy root pulp. '
                                                                'Medicaments dress the amputated '
                                                                'pulp to maintain the tooth until '
                                                                'exfoliation.'}],
                                       'medium': [{'question': 'A classic indication for a '
                                                               'stainless steel crown in the '
                                                               'primary dentition is?',
                                                   'options': ['A) Shade try-in for ceramic '
                                                               'veneers',
                                                               'B) Multi-surface caries in a '
                                                               'primary molar',
                                                               'C) Fabrication of bleaching trays',
                                                               'D) Anterior laminate veneer '
                                                               'preparation'],
                                                   'answer': 'B) Multi-surface caries in a primary '
                                                             'molar',
                                                   'explanation': 'Primary molars with '
                                                                  'multi-surface caries often lack '
                                                                  'sufficient tooth structure for '
                                                                  'durable intracoronal '
                                                                  'restorations and are subject to '
                                                                  'high occlusal load. Stainless '
                                                                  'steel crowns encircle and '
                                                                  'protect the remaining tooth '
                                                                  'until exfoliation.'},
                                                  {'question': 'Early childhood caries classically '
                                                               'affects which teeth most severely?',
                                                   'options': ['A) Maxillary primary anterior '
                                                               'teeth',
                                                               'B) Permanent third molars',
                                                               'C) Impacted maxillary canines',
                                                               'D) Mandibular primary anteriors '
                                                               'more than maxillary anteriors in '
                                                               'the classic bottle pattern'],
                                                   'answer': 'A) Maxillary primary anterior teeth',
                                                   'explanation': 'Early childhood caries '
                                                                  'classically affects maxillary '
                                                                  'primary incisors because '
                                                                  'sweetened liquids pool around '
                                                                  'them during bottle or sippy-cup '
                                                                  'use, especially at night when '
                                                                  'salivary flow is low. '
                                                                  'Mandibular incisors are often '
                                                                  'relatively spared by tongue '
                                                                  'protection and salivary '
                                                                  'bathing.'},
                                                  {'question': 'First-line basic behavior guidance '
                                                               'for a fearful but cooperative '
                                                               'child typically begins with?',
                                                   'options': ['A) Immediate general anesthesia '
                                                               'for every visit',
                                                               'B) Protective stabilization '
                                                               'without discussion or consent '
                                                               'themes',
                                                               'C) Tell-show-do communication',
                                                               'D) Ignoring expressed fear to save '
                                                               'time'],
                                                   'answer': 'C) Tell-show-do communication',
                                                   'explanation': 'Tell-show-do introduces the '
                                                                  'child to instruments and '
                                                                  'sensations in a nonthreatening '
                                                                  'sequence, reducing fear through '
                                                                  'predictable communication. It '
                                                                  'establishes trust and '
                                                                  'cooperation before more '
                                                                  'advanced pharmacologic or '
                                                                  'protective techniques are '
                                                                  'considered.'}],
                                       'hard': [{'question': 'Intrusion of a primary incisor '
                                                             'raises greatest concern for?',
                                                 'options': ['A) TMJ ankylosis as the usual '
                                                             'outcome',
                                                             'B) Cutaneous freckle formation',
                                                             'C) Maxillary sinusitis in every case',
                                                             'D) Damage to the developing '
                                                             'permanent successor'],
                                                 'answer': 'D) Damage to the developing permanent '
                                                           'successor',
                                                 'explanation': 'The developing permanent '
                                                                'successor lies in close proximity '
                                                                'to the primary tooth root; '
                                                                'intrusive luxation can drive the '
                                                                'primary root against the '
                                                                'permanent tooth germ. Sequelae '
                                                                'include enamel hypoplasia, '
                                                                'eruption disturbance, or '
                                                                'dilaceration of the successor.'},
                                                {'question': 'Early loss of a primary second molar '
                                                             'most commonly leads to space loss '
                                                             'by?',
                                                 'options': ['A) Distal drift of the first '
                                                             'permanent molar preserving leeway '
                                                             'space',
                                                             'B) Mesial drift of the first '
                                                             'permanent molar',
                                                             'C) Spontaneous increase in arch '
                                                             'length restoring premolar space',
                                                             'D) Automatic improvement of the '
                                                             'dental midline'],
                                                 'answer': 'B) Mesial drift of the first permanent '
                                                           'molar',
                                                 'explanation': 'The primary second molar holds '
                                                                'the leeway space and guides '
                                                                'eruption of the first permanent '
                                                                'molar. Early loss allows the '
                                                                'permanent molar to drift '
                                                                'mesially, consuming space needed '
                                                                'for the premolars and producing '
                                                                'crowding or impaction.'},
                                                {'question': 'Molar-incisor hypomineralization '
                                                             '(MIH) characteristically features?',
                                                 'options': ['A) Tetracycline banding as the only '
                                                             'cause',
                                                             'B) Diffuse fluorosis identical in '
                                                             'every case',
                                                             'C) Demarcated opacities on first '
                                                             'permanent molars and often incisors',
                                                             'D) Caries without any enamel '
                                                             'developmental defect'],
                                                 'answer': 'C) Demarcated opacities on first '
                                                           'permanent molars and often incisors',
                                                 'explanation': 'Molar-incisor hypomineralization '
                                                                'is a qualitative enamel defect '
                                                                'producing demarcated opacities on '
                                                                'first permanent molars and often '
                                                                'incisors. Hypomineralized enamel '
                                                                'is porous, sensitive, and prone '
                                                                'to posteruptive breakdown and '
                                                                'caries.'}],
                                       'extreme': [{'question': 'Dental findings raising concern '
                                                                'for child abuse include?',
                                                    'options': ['A) Injuries inconsistent with the '
                                                                'stated history and developmental '
                                                                'age',
                                                                'B) A typical playground abrasion '
                                                                'matching a coherent history',
                                                                'C) A single carious lesion '
                                                                'without trauma',
                                                                'D) Mild orthodontic crowding '
                                                                'alone'],
                                                    'answer': 'A) Injuries inconsistent with the '
                                                              'stated history and developmental '
                                                              'age',
                                                    'explanation': 'Injuries that do not match the '
                                                                   'stated mechanism, '
                                                                   'developmental stage, or '
                                                                   'alleged timing raise concern '
                                                                   'for non-accidental trauma. '
                                                                   'Dentists have a professional '
                                                                   'and legal duty to recognize '
                                                                   'patterned oral injuries and '
                                                                   'report appropriately.'},
                                                   {'question': 'General anesthesia for pediatric '
                                                                'dentistry is most appropriately '
                                                                'considered when?',
                                                    'options': ['A) A single simple restoration '
                                                                'manageable with tell-show-do',
                                                                'B) Extrinsic stain is the only '
                                                                'finding',
                                                                'C) Extensive disease plus '
                                                                'inability to cooperate or medical '
                                                                'complexity after alternatives are '
                                                                'considered',
                                                                'D) Parental scheduling preference '
                                                                'without clinical need'],
                                                    'answer': 'C) Extensive disease plus inability '
                                                              'to cooperate or medical complexity '
                                                              'after alternatives are considered',
                                                    'explanation': 'General anesthesia for '
                                                                   'dentistry is reserved when '
                                                                   'extensive treatment needs '
                                                                   'cannot be completed safely '
                                                                   'with behavioral guidance, '
                                                                   'local anesthesia, or '
                                                                   'sedation—especially with '
                                                                   'medical or developmental '
                                                                   'complexity—after less invasive '
                                                                   'alternatives are thoughtfully '
                                                                   'considered.'},
                                                   {'question': 'An avulsed primary tooth should '
                                                                'generally be?',
                                                    'options': ['A) Replanted using '
                                                                'permanent-tooth protocols',
                                                                'B) Treated with immediate '
                                                                'extraoral RCT then replanted',
                                                                'C) Discarded without any '
                                                                'examination of soft tissues',
                                                                'D) Not replanted, to protect the '
                                                                'permanent successor'],
                                                    'answer': 'D) Not replanted, to protect the '
                                                              'permanent successor',
                                                    'explanation': 'Replanting an avulsed primary '
                                                                   'tooth risks damage to the '
                                                                   'underlying permanent tooth '
                                                                   'germ from the primary root or '
                                                                   'from inflammatory sequelae. '
                                                                   'IADT guidelines therefore '
                                                                   'advise against replantation of '
                                                                   'primary teeth; soft tissues '
                                                                   'are assessed and the child is '
                                                                   'followed for successor '
                                                                   'eruption.'}]},
                         'cases': {'easy': [{'title': 'Carious Primary Molar',
                                             'stem': 'A 5-year-old has a deep cavity in a primary '
                                                     'molar, no mobility, restorable.',
                                             'question': 'Options concept?',
                                             'answer': 'Restore ± pulp therapy if indicated; space '
                                                       'importance.',
                                             'discussion': 'Extraction needs space management '
                                                           'plan.',
                                             'book_hint': "McDonald and Avery's Dentistry for the "
                                                          'Child and Adolescent'}],
                                   'medium': [{'title': 'Bottle Caries',
                                               'stem': 'A 3-year-old sleeps with a juice bottle; '
                                                       'upper incisors carious.',
                                               'question': 'Diagnosis theme?',
                                               'answer': 'Early childhood caries — stop habit, '
                                                         'restore/prevent, fluoride, diet '
                                                         'counseling.',
                                               'discussion': 'Lower incisors often relatively '
                                                             'spared.',
                                               'book_hint': "McDonald and Avery's Dentistry for "
                                                            'the Child and Adolescent'}],
                                   'hard': [{'title': 'Intruded Primary Incisor',
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
                                                          'Child and Adolescent'}],
                                   'extreme': [{'title': 'Unexplained Torn Frenum Toddler',
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
 'oral_medicine': {'label': 'Oral Medicine & Pathology',
                   'books': ['Oral and Maxillofacial Pathology — Neville',
                             "Cawson's Essentials of Oral Pathology",
                             'Oral Medicine — Odell'],
                   'pdf_notes': ['Aphthae on non-keratinized mucosa; HSV often keratinized.',
                                 'Leukoplakia: non-wipeable white patch — risk stratify/biopsy.',
                                 'Tobacco + alcohol raise SCC risk.',
                                 'Nonhealing ulcer >2 weeks needs biopsy.',
                                 'Candida: look for risk factors and wipeable plaques.'],
                   'questions': {'easy': [{'question': 'Recurrent aphthous ulcers usually occur '
                                                       'on?',
                                           'options': ['A) Non-keratinized movable mucosa',
                                                       'B) Attached gingiva as the usual primary '
                                                       'site',
                                                       'C) Hard palate as the usual primary site',
                                                       'D) Vermilion border exclusively'],
                                           'answer': 'A) Non-keratinized movable mucosa',
                                           'explanation': 'Recurrent aphthous ulcers arise on '
                                                          'non-keratinized mucosa such as the '
                                                          'buccal mucosa, floor of mouth, and '
                                                          'ventral tongue, where the epithelium is '
                                                          'thinner and more mobile. They do not '
                                                          'typically begin on heavily keratinized '
                                                          'masticatory mucosa.'},
                                          {'question': 'Oral leukoplakia is defined clinically as?',
                                           'options': ['A) A wipeable white film consistent with '
                                                       'pseudomembranous candidiasis',
                                                       'B) Bilateral reticular striae diagnostic '
                                                       'of lichen planus without exclusion',
                                                       'C) A normal linea alba along the occlusal '
                                                       'plane',
                                                       'D) A white patch that cannot be wiped away '
                                                       'or attributed to another defined disease'],
                                           'answer': 'D) A white patch that cannot be wiped away '
                                                     'or attributed to another defined disease',
                                           'explanation': 'Oral leukoplakia is a clinical '
                                                          'diagnosis of exclusion: a white plaque '
                                                          'that cannot be wiped away and cannot be '
                                                          'attributed to another defined disease '
                                                          'such as candidiasis or lichen planus. A '
                                                          'subset harbors dysplasia or carcinoma, '
                                                          'so biopsy is often indicated.'},
                                          {'question': 'Geographic tongue is best classified as?',
                                           'options': ['A) Oral squamous cell carcinoma until '
                                                       'proven otherwise',
                                                       'B) Secondary syphilis mucous patches',
                                                       'C) Benign migratory glossitis',
                                                       'D) Chronic traumatic ulcer only'],
                                           'answer': 'C) Benign migratory glossitis',
                                           'explanation': 'Geographic tongue (benign migratory '
                                                          'glossitis) shows migrating areas of '
                                                          'filiform papilla atrophy surrounded by '
                                                          'slightly raised white borders. It is an '
                                                          'inflammatory but benign condition of '
                                                          'unknown precise cause and does not '
                                                          'require oncologic treatment.'}],
                                 'medium': [{'question': 'Which set most accurately lists risk '
                                                         'factors for oral candidiasis?',
                                             'options': ['A) Antibiotics, steroids, dentures, '
                                                         'xerostomia, immunosuppression',
                                                         'B) Orthodontic wax use alone',
                                                         'C) Daily flossing alone',
                                                         'D) Pit-and-fissure sealants alone'],
                                             'answer': 'A) Antibiotics, steroids, dentures, '
                                                       'xerostomia, immunosuppression',
                                             'explanation': 'Candida albicans is an oral commensal '
                                                            'that overgrows when local or systemic '
                                                            'defenses fall—broad-spectrum '
                                                            'antibiotics, corticosteroids, denture '
                                                            'bases, xerostomia, or '
                                                            'immunosuppression. Pseudomembranous '
                                                            'plaques wipe off leaving erythematous '
                                                            'mucosa.'},
                                            {'question': 'Classic oral lichen planus presents '
                                                         'with?',
                                             'options': ['A) Punched-out necrotic papillae of '
                                                         'necrotizing gingivitis',
                                                         'B) Reticular white striae (Wickham '
                                                         'striae)',
                                                         'C) Koplik spots of measles on the buccal '
                                                         'mucosa',
                                                         'D) Fordyce granules as ectopic sebaceous '
                                                         'glands'],
                                             'answer': 'B) Reticular white striae (Wickham striae)',
                                             'explanation': 'Oral lichen planus is a '
                                                            'T-cell–mediated mucocutaneous '
                                                            'disease; the reticular form shows '
                                                            'lace-like white striae (Wickham '
                                                            'striae), often bilaterally on the '
                                                            'buccal mucosa. Erosive forms may '
                                                            'cause pain and require biopsy and '
                                                            'topical corticosteroid management.'},
                                            {'question': 'Major risk factors for oral squamous '
                                                         'cell carcinoma include?',
                                             'options': ['A) Xylitol gum chewing',
                                                         'B) Electric toothbrush use',
                                                         'C) Tobacco and alcohol use',
                                                         'D) Clear aligner therapy'],
                                             'answer': 'C) Tobacco and alcohol use',
                                             'explanation': 'Tobacco and alcohol are synergistic '
                                                            'carcinogens for oral squamous cell '
                                                            'carcinoma, causing cumulative DNA '
                                                            'damage in keratinocytes of the oral '
                                                            'epithelium. Chronic exposure drives '
                                                            'dysplasia and invasive carcinoma, '
                                                            'especially on the floor of mouth and '
                                                            'lateral tongue.'}],
                                 'hard': [{'question': 'Oral clues suggesting pemphigus vulgaris '
                                                       'include?',
                                           'options': ['A) Flaccid bullae, positive Nikolsky sign, '
                                                       'and desquamative gingivitis themes',
                                                       'B) Fordyce granules on the buccal mucosa',
                                                       'C) Torus palatinus midline bony growth',
                                                       'D) Amalgam tattoo pigmentation'],
                                           'answer': 'A) Flaccid bullae, positive Nikolsky sign, '
                                                     'and desquamative gingivitis themes',
                                           'explanation': 'Pemphigus vulgaris is an autoimmune '
                                                          'acantholysis caused by autoantibodies '
                                                          'against desmogleins, producing flaccid '
                                                          'intraepithelial bullae that rupture '
                                                          'easily (Nikolsky sign positive) and '
                                                          'painful erosions, often with '
                                                          'desquamative gingivitis. Biopsy with '
                                                          'immunofluorescence confirms the '
                                                          'diagnosis.'},
                                          {'question': 'Sjögren syndrome–related hyposalivation is '
                                                       'associated with?',
                                           'options': ['A) Marked hypersalivation and reduced '
                                                       'caries',
                                                       'B) Autoimmune exocrinopathy with elevated '
                                                       'caries risk',
                                                       'C) Dens evaginatus of premolars',
                                                       'D) Mesiodens formation in the midline'],
                                           'answer': 'B) Autoimmune exocrinopathy with elevated '
                                                     'caries risk',
                                           'explanation': 'Sjögren syndrome is an autoimmune '
                                                          'destruction of exocrine glands that '
                                                          'markedly reduces salivary flow. '
                                                          'Hyposalivation impairs buffering and '
                                                          'clearance of dietary sugars, sharply '
                                                          'elevating caries risk and candidiasis '
                                                          'susceptibility.'},
                                          {'question': 'Odontogenic keratocyst (OKC) behavior is '
                                                       'notable for?',
                                           'options': ['A) Low recurrence after simple enucleation '
                                                       'in most series',
                                                       'B) Self-limiting behavior managed by '
                                                       'observation alone',
                                                       'C) High recurrence potential requiring '
                                                       'careful surgical management',
                                                       'D) Presentation as irreversible pulpitis '
                                                       'of a vital tooth'],
                                           'answer': 'C) High recurrence potential requiring '
                                                     'careful surgical management',
                                           'explanation': 'The odontogenic keratocyst arises from '
                                                          'dental lamina rests and is lined by '
                                                          'parakeratinized stratified squamous '
                                                          'epithelium with high proliferative '
                                                          'activity. It tends to recur after '
                                                          'incomplete removal, so careful '
                                                          'enucleation, adjunctive measures, and '
                                                          'follow-up imaging are emphasized.'}],
                                 'extreme': [{'question': 'A non-healing oral ulcer lasting more '
                                                          'than two weeks in a smoker should be '
                                                          'managed as?',
                                              'options': ['A) Cancer until proven otherwise — '
                                                          'biopsy',
                                                          'B) Chronic aphthous ulceration forever '
                                                          'without investigation',
                                                          'C) A finding that can safely be ignored',
                                                          'D) Vitamin deficiency alone without '
                                                          'tissue diagnosis'],
                                              'answer': 'A) Cancer until proven otherwise — biopsy',
                                              'explanation': 'A solitary oral ulcer lasting longer '
                                                             'than two weeks—especially in a '
                                                             'smoker or heavy drinker—must be '
                                                             'regarded as squamous cell carcinoma '
                                                             'until histologically excluded. '
                                                             'Malignant ulcers do not heal with '
                                                             'conservative care; timely biopsy is '
                                                             'mandatory.'},
                                             {'question': 'Medication-related osteonecrosis of the '
                                                          'jaw typically presents as?',
                                              'options': ['A) Geographic tongue migratory patches',
                                                          'B) Exposed necrotic jawbone with '
                                                          'antiresorptive drug history',
                                                          'C) Recurrent aphthous ulcers only',
                                                          'D) Occlusal caries alone'],
                                              'answer': 'B) Exposed necrotic jawbone with '
                                                        'antiresorptive drug history',
                                              'explanation': 'MRONJ presents as exposed necrotic '
                                                             'jawbone persisting in a patient '
                                                             'treated with antiresorptive or '
                                                             'antiangiogenic medications, without '
                                                             'radiotherapy to the jaws. Impaired '
                                                             'osteoclast function and mucosal '
                                                             'healing underpin the '
                                                             'pathophysiology.'},
                                             {'question': 'HPV-related oropharyngeal carcinoma '
                                                          'characteristically involves?',
                                              'options': ['A) A pattern identical in every case to '
                                                          'classic floor-of-mouth smoker SCC only',
                                                          'B) Cutaneous melanoma of facial skin',
                                                          'C) Dental caries of primary molars',
                                                          'D) Tonsillar crypts and base of tongue, '
                                                          'sometimes in younger patients with less '
                                                          'tobacco history'],
                                              'answer': 'D) Tonsillar crypts and base of tongue, '
                                                        'sometimes in younger patients with less '
                                                        'tobacco history',
                                              'explanation': 'High-risk HPV (notably HPV-16) '
                                                             'drives a rising subset of '
                                                             'oropharyngeal squamous carcinomas of '
                                                             'the tonsillar crypts and base of '
                                                             'tongue, often in patients without '
                                                             'traditional heavy tobacco exposure. '
                                                             'Viral oncogenes E6/E7 drive '
                                                             'carcinogenesis with distinct '
                                                             'clinical epidemiology.'}]},
                   'cases': {'easy': [{'title': 'Recurrent Mouth Ulcers',
                                       'stem': 'Healthy teen gets painful ulcers on buccal mucosa '
                                               'lasting a week, then heal.',
                                       'question': 'Likely?',
                                       'answer': 'Recurrent aphthous stomatitis.',
                                       'discussion': 'Symptomatic care; investigate if complex.',
                                       'book_hint': 'Oral and Maxillofacial Pathology — Neville'}],
                             'medium': [{'title': 'White Patch Floor of Mouth',
                                         'stem': 'A 60-year-old smoker has a non-wipeable white '
                                                 'patch on floor of mouth.',
                                         'question': 'Next concept?',
                                         'answer': 'Treat as leukoplakia — specialist '
                                                   'referral/biopsy risk stratification.',
                                         'discussion': 'Floor of mouth is high-risk site.',
                                         'book_hint': 'Oral and Maxillofacial Pathology — '
                                                      'Neville'}],
                             'hard': [{'title': 'Desquamative Gingivitis',
                                       'stem': 'Painful peeling gingiva, nikolsky-positive areas, '
                                               'no response to cleaning alone. Choose the safest '
                                               'high-yield next concept before definitive results.',
                                       'question': 'Workup?',
                                       'answer': 'Consider vesiculobullous disease — biopsy for '
                                                 'histopathology + DIF.',
                                       'discussion': 'Do not keep scaling without diagnosis.',
                                       'book_hint': 'Oral and Maxillofacial Pathology — Neville'}],
                             'extreme': [{'title': 'Nonhealing Lateral Tongue Ulcer',
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
 'restorative': {'label': 'Restorative Dentistry',
                 'books': ["Sturdevant's Art and Science of Operative Dentistry",
                           "Summitt's Fundamentals of Operative Dentistry",
                           "Pickard's Guide to Minimally Invasive Operative Dentistry"],
                 'pdf_notes': ['Black classification still useful for cavity location.',
                               'Adhesion needs etch/bond protocol and isolation.',
                               'High C-factor increases polymerization stress.',
                               'Selective caries removal can avoid pulp exposure.',
                               'Prevention first in rampant caries.'],
                 'questions': {'easy': [{'question': 'G.V. Black Class II cavity involves?',
                                         'options': ['A) Proximal surfaces of posterior teeth',
                                                     'B) Pits and fissures of anterior teeth only',
                                                     'C) Cervical third smooth surfaces (Class V) '
                                                     'only',
                                                     'D) Cusp tip enamel only'],
                                         'answer': 'A) Proximal surfaces of posterior teeth',
                                         'explanation': 'G.V. Black Class II cavities involve the '
                                                        'proximal surfaces of posterior teeth, '
                                                        'typically initiating just below the '
                                                        'contact point where biofilm stagnates. '
                                                        'The classification organizes cavity '
                                                        'location for preparation design and '
                                                        'restoration choice.'},
                                        {'question': 'Composite resin bonding primarily relies on?',
                                         'options': ['A) Zinc phosphate cement lute alone',
                                                     'B) Soft-tissue sutures for retention',
                                                     'C) Mechanical screws into dentin',
                                                     'D) Micromechanical adhesion after etch and '
                                                     'adhesive protocols'],
                                         'answer': 'D) Micromechanical adhesion after etch and '
                                                   'adhesive protocols',
                                         'explanation': 'Etching enamel (and appropriately '
                                                        'conditioning dentin) creates '
                                                        'microporosity that adhesive resins '
                                                        'infiltrate to form resin tags and a '
                                                        'hybrid layer. Retention of composite is '
                                                        'therefore primarily micromechanical '
                                                        'rather than chemical cementation alone.'},
                                        {'question': 'Caries detector dyes are used to?',
                                         'options': ['A) Replace bitewing radiographs entirely',
                                                     'B) Diagnose pulp vitality definitively',
                                                     'C) Help visualize infected dentin, '
                                                     'interpreted cautiously',
                                                     'D) Whiten extrinsic stain'],
                                         'answer': 'C) Help visualize infected dentin, interpreted '
                                                   'cautiously',
                                         'explanation': 'Caries detector dyes bind preferentially '
                                                        'to denatured collagen in infected dentin, '
                                                        'helping visualize tissue that may harbor '
                                                        'high bacterial load. They can also stain '
                                                        'caries-affected or sound dentin '
                                                        'nonspecifically, so clinical judgment '
                                                        'remains essential.'}],
                               'medium': [{'question': 'Liners and bases under deep restorations '
                                                       'aim to?',
                                           'options': ['A) Change restoration shade only',
                                                       'B) Increase enamel etch aggressiveness '
                                                       'only',
                                                       'C) Replace the need for rubber dam '
                                                       'isolation',
                                                       'D) Protect the pulp, provide insulation, '
                                                       'and aid sealing'],
                                           'answer': 'D) Protect the pulp, provide insulation, and '
                                                     'aid sealing',
                                           'explanation': 'Liners and bases under deep '
                                                          'restorations provide thermal '
                                                          'insulation, chemical protection, and '
                                                          'sometimes a sealing or bioactive '
                                                          'interface over remaining dentin near '
                                                          'the pulp. Material choice depends on '
                                                          'remaining dentin thickness and '
                                                          'definitive restorative material.'},
                                          {'question': 'A recognized clinical advantage of dental '
                                                       'amalgam includes?',
                                           'options': ['A) Wear resistance and lower moisture '
                                                       'sensitivity than composite',
                                                       'B) Superior esthetics compared with all '
                                                       'ceramics',
                                                       'C) Micromechanical bonding identical to '
                                                       'etch-and-rinse composite',
                                                       'D) Complete absence of corrosion in the '
                                                       'oral environment'],
                                           'answer': 'A) Wear resistance and lower moisture '
                                                     'sensitivity than composite',
                                           'explanation': 'Dental amalgam’s metallic '
                                                          'microstructure confers high compressive '
                                                          'strength and wear resistance under '
                                                          'posterior occlusal load. Unlike resin '
                                                          'composites, amalgam does not rely on '
                                                          'adhesive bonding that fails in '
                                                          'moisture-contaminated fields to the '
                                                          'same degree.'},
                                          {'question': 'Secondary (recurrent) caries most often '
                                                       'develops at?',
                                           'options': ['A) The center of an intact pulp horn '
                                                       'remote from margins',
                                                       'B) Restoration margins with microleakage '
                                                       'or plaque stagnation',
                                                       'C) The root apex in vital teeth without '
                                                       'coronal restorations',
                                                       'D) Cementum far from any restorative '
                                                       'margin'],
                                           'answer': 'B) Restoration margins with microleakage or '
                                                     'plaque stagnation',
                                           'explanation': 'Secondary (recurrent) caries develops '
                                                          'at restoration margins where '
                                                          'microleakage or plaque stagnation '
                                                          'allows demineralization of adjacent '
                                                          'enamel and dentin. Open margins, '
                                                          'overhangs, and poor oral hygiene '
                                                          'elevate risk.'}],
                               'hard': [{'question': 'Configuration factor (C-factor) is typically '
                                                     'highest in?',
                                         'options': ['A) Class I deep boxy preparations',
                                                     'B) Free cusp rebuilds with many unbonded '
                                                     'surfaces',
                                                     'C) Single-surface veneers with low '
                                                     'bonded-wall ratios',
                                                     'D) Preventive resin sealants on fissures '
                                                     'alone'],
                                         'answer': 'A) Class I deep boxy preparations',
                                         'explanation': 'The C-factor is the ratio of bonded to '
                                                        'unbonded surfaces in a cavity; Class I '
                                                        'boxy preparations have many bonded walls '
                                                        'and few free surfaces for stress relief. '
                                                        'As composite polymerizes and shrinks, '
                                                        'high C-factor cavities concentrate '
                                                        'interfacial stress and risk gap '
                                                        'formation.'},
                                        {'question': 'Selective caries removal in a deep lesion '
                                                     'aims to?',
                                         'options': ['A) Intentionally expose the pulp in every '
                                                     'deep case',
                                                     'B) Avoid pulp exposure while sealing '
                                                     'remaining soft dentin under protocol',
                                                     'C) Leave all enamel caries untouched '
                                                     'indefinitely',
                                                     'D) Defer restoration forever after '
                                                     'excavation'],
                                         'answer': 'B) Avoid pulp exposure while sealing remaining '
                                                   'soft dentin under protocol',
                                         'explanation': 'In deep carious lesions, selective '
                                                        '(partial) caries removal leaves soft, '
                                                        'caries-affected dentin over the pulp to '
                                                        'avoid exposure while excavating '
                                                        'peripheral infected dentin to a hard, '
                                                        'sealable margin. A well-sealed '
                                                        'restoration deprives remaining bacteria '
                                                        'of substrate.'},
                                        {'question': 'Abfraction as a proposed mechanism relates '
                                                     'to?',
                                         'options': ['A) Dietary acid erosion from citrus alone as '
                                                     'the exclusive cause',
                                                     'B) Toothbrush abrasion as the only proven '
                                                     'etiology forever',
                                                     'C) Occlusal stress contributing to cervical '
                                                     'non-carious lesions (debated)',
                                                     'D) Primary bacterial caries of enamel pits'],
                                         'answer': 'C) Occlusal stress contributing to cervical '
                                                   'non-carious lesions (debated)',
                                         'explanation': 'Abfraction proposes that occlusal stress '
                                                        'concentrates tensile strain at the '
                                                        'cervical region, disrupting enamel and '
                                                        'dentin and contributing to non-carious '
                                                        'cervical lesions. Many lesions are '
                                                        'multifactorial with abrasion and erosion '
                                                        'also involved; the theory remains '
                                                        'debated.'}],
                               'extreme': [{'question': 'Minimally invasive dentistry prioritizes?',
                                            'options': ['A) Prevention, early detection, and '
                                                        'maximal tissue preservation',
                                                        'B) Full-coverage crowns for every enamel '
                                                        'stain',
                                                        'C) Extraction as first-line for early '
                                                        'lesions',
                                                        'D) Ignoring caries risk factors after '
                                                        'restoration'],
                                            'answer': 'A) Prevention, early detection, and maximal '
                                                      'tissue preservation',
                                            'explanation': 'Minimally invasive dentistry aims to '
                                                           'prevent disease, detect lesions early, '
                                                           'and restore only what is irreversibly '
                                                           'lost while preserving sound tooth '
                                                           'structure. Risk-based recall, '
                                                           'fluoride, and sealants support this '
                                                           'philosophy.'},
                                           {'question': 'A biomimetic restorative concept '
                                                        'emphasizes?',
                                            'options': ['A) Selecting the cheapest cement '
                                                        'regardless of properties',
                                                        'B) Using a single shade A2 for all '
                                                        'restorations',
                                                        'C) Replacing lost tissue with materials '
                                                        'that mimic properties and stress '
                                                        'distribution',
                                                        'D) Ignoring ferrule and remaining tooth '
                                                        'structure'],
                                            'answer': 'C) Replacing lost tissue with materials '
                                                      'that mimic properties and stress '
                                                      'distribution',
                                            'explanation': 'Biomimetic restorative dentistry seeks '
                                                           'to replace enamel and dentin with '
                                                           'materials and adhesive techniques that '
                                                           'approximate the stiffness, bonding, '
                                                           'and stress distribution of natural '
                                                           'tooth tissues. By rebuilding rather '
                                                           'than aggressively reducing, longevity '
                                                           'and pulp vitality are favored.'},
                                           {'question': 'Management order for rampant caries most '
                                                        'appropriately begins with?',
                                            'options': ['A) Esthetic veneers before disease '
                                                        'control',
                                                        'B) Vital bleaching before excavation',
                                                        'C) Ignoring diet and salivary risk '
                                                        'factors',
                                                        'D) Urgencies and disease control, then '
                                                        'temporaries, then definitive care when '
                                                        'stable'],
                                            'answer': 'D) Urgencies and disease control, then '
                                                      'temporaries, then definitive care when '
                                                      'stable',
                                            'explanation': 'Rampant caries reflects high caries '
                                                           'activity; placing definitive complex '
                                                           'restorations before disease control '
                                                           'invites rapid failure at new margins. '
                                                           'Urgent pain and infection are managed '
                                                           'first, then biofilm and dietary '
                                                           'control with provisional '
                                                           'stabilization, then definitive '
                                                           'restorations.'}]},
                 'cases': {'easy': [{'title': 'Occlusal Caries Molar',
                                     'stem': 'A deep fissure stains; bitewing shows enamel-dentin '
                                             'caries; tooth vital asymptomatic.',
                                     'question': 'Plan?',
                                     'answer': 'Restore with appropriate material after caries '
                                               'removal.',
                                     'discussion': 'Consider sealant for non-cavitated elsewhere.',
                                     'book_hint': 'Art and Science of Operative Dentistry — '
                                                  'Sturdevant'}],
                           'medium': [{'title': 'Failed Composite Margin',
                                       'stem': 'Staining and catch at cervical margin of Class V '
                                               'composite; sensitivity to cold brief.',
                                       'question': 'Likely?',
                                       'answer': 'Marginal leakage/secondary caries or bond '
                                                 'failure — replace after diagnosis.',
                                       'discussion': 'Isolate well on redo.',
                                       'book_hint': 'Art and Science of Operative Dentistry — '
                                                    'Sturdevant'}],
                           'hard': [{'title': 'Deep Caries Near Pulp',
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
                                                  'Sturdevant'}],
                           'extreme': [{'title': 'Rampant Caries Head-Neck Radiation',
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
 'oral_radiology': {'label': 'Oral Radiology',
                    'books': ["White and Pharoah's Oral Radiology",
                              'Essentials of Dental Radiography',
                              'Oral Radiology principles texts'],
                    'pdf_notes': ['ALARA: justify and optimize every exposure.',
                                  'Bitewings for interproximal caries.',
                                  'Periapicals for full root/periapex.',
                                  'CBCT only when 2D is insufficient.',
                                  'Ill-defined destructive lesions need urgent workup.'],
                    'questions': {'easy': [{'question': 'Bitewing radiographs best demonstrate?',
                                            'options': ['A) Interproximal caries and crestal '
                                                        'alveolar bone',
                                                        'B) TMJ articular disc position in detail',
                                                        'C) Maxillary sinus polyps as the primary '
                                                        'indication',
                                                        'D) Soft-tissue cancer staging of the '
                                                        'neck'],
                                            'answer': 'A) Interproximal caries and crestal '
                                                      'alveolar bone',
                                            'explanation': 'Bitewing radiographs project the '
                                                           'crowns of opposing maxillary and '
                                                           'mandibular teeth and the crestal '
                                                           'alveolar bone with minimal overlap '
                                                           'when angulation is correct. They are '
                                                           'the most sensitive routine view for '
                                                           'early interproximal caries detection.'},
                                           {'question': 'ALARA in dental radiography means?',
                                            'options': ['A) Avoiding all radiographs regardless of '
                                                        'diagnostic need',
                                                        'B) As Low As Reasonably Achievable '
                                                        'radiation dose',
                                                        'C) Analog films only; digital is excluded',
                                                        'D) CBCT for every routine examination'],
                                            'answer': 'B) As Low As Reasonably Achievable '
                                                      'radiation dose',
                                            'explanation': 'ALARA (As Low As Reasonably '
                                                           'Achievable) is the '
                                                           'radiation-protection principle that '
                                                           'every exposure must be justified by '
                                                           'diagnostic benefit and then optimized '
                                                           'to the lowest dose that still yields '
                                                           'adequate image quality.'},
                                           {'question': 'A periapical radiograph is intended to '
                                                        'show?',
                                            'options': ['A) Bilateral molar intercuspation in a '
                                                        'single bitewing-style view',
                                                        'B) Cephalometric skeletal landmarks for '
                                                        'orthodontic analysis',
                                                        'C) Thoracic chest structures',
                                                        'D) The full tooth length and periapical '
                                                        'bone'],
                                            'answer': 'D) The full tooth length and periapical '
                                                      'bone',
                                            'explanation': 'A periapical radiograph images the '
                                                           'entire tooth from crown to apex plus '
                                                           'the surrounding periapical bone. It is '
                                                           'used to assess apical periodontitis, '
                                                           'root morphology, and periodontal bone '
                                                           'along the root surface.'}],
                                  'medium': [{'question': 'A principal advantage of a panoramic '
                                                          'radiograph is?',
                                              'options': ['A) Higher spatial resolution than '
                                                          'bitewings for early enamel caries',
                                                          'B) A broad overview of jaws, TMJs, and '
                                                          'dentition',
                                                          'C) Absence of geometric distortion '
                                                          'under all conditions',
                                                          'D) Elimination of any need for '
                                                          'periapical images'],
                                              'answer': 'B) A broad overview of jaws, TMJs, and '
                                                        'dentition',
                                              'explanation': 'A panoramic radiograph captures both '
                                                             'jaws, dentition, TMJs, and '
                                                             'contiguous structures in a single '
                                                             'tomographic image. It is useful for '
                                                             'screening, orthodontic assessment, '
                                                             'and surgical planning when a broad '
                                                             'overview is needed, despite lower '
                                                             'spatial resolution than intraoral '
                                                             'films.'},
                                             {'question': 'A radiolucency at the apex of a '
                                                          'nonvital tooth most likely represents?',
                                              'options': ['A) Osteosarcoma in every case',
                                                          'B) A torus mandibularis',
                                                          'C) Periapical rarefying osteitis '
                                                          '(granuloma/cyst/abscess spectrum)',
                                                          'D) An enamel pearl on the root surface'],
                                              'answer': 'C) Periapical rarefying osteitis '
                                                        '(granuloma/cyst/abscess spectrum)',
                                              'explanation': 'Bacterial toxins from a necrotic '
                                                             'pulp trigger inflammatory resorption '
                                                             'of periapical bone, producing a '
                                                             'radiolucency (rarefying osteitis) '
                                                             'that may represent granuloma, cyst, '
                                                             'or abscess histologically. Vitality '
                                                             'testing links the lesion to pulpal '
                                                             'disease.'},
                                             {'question': 'Lead apron and thyroid shield use '
                                                          'should follow?',
                                              'options': ['A) Current guidelines with '
                                                          'justification of exposure first',
                                                          'B) Omitting all patient shielding as '
                                                          'outdated practice',
                                                          'C) Restricting shields to CBCT while '
                                                          'excluding intraoral exams',
                                                          'D) Protecting operators while leaving '
                                                          'patients unshielded'],
                                              'answer': 'A) Current guidelines with justification '
                                                        'of exposure first',
                                              'explanation': 'Lead aprons and thyroid shields '
                                                             'reduce exposure of radiosensitive '
                                                             'tissues when they do not obscure '
                                                             'anatomy, but justification of the '
                                                             'radiograph and optimized technique '
                                                             'remain primary. Contemporary '
                                                             'guidelines refine when thyroid '
                                                             'shielding is practical.'}],
                                  'hard': [{'question': 'CBCT is most appropriately indicated '
                                                        'when?',
                                            'options': ['A) Complex implant, impacted tooth, or '
                                                        'endodontic anatomy needs 3D detail beyond '
                                                        '2D',
                                                        'B) Routine recall screening in place of '
                                                        'bitewings',
                                                        'C) First-line detection of early '
                                                        'interproximal enamel caries',
                                                        'D) Shade selection for ceramic '
                                                        'restorations'],
                                            'answer': 'A) Complex implant, impacted tooth, or '
                                                      'endodontic anatomy needs 3D detail beyond '
                                                      '2D',
                                            'explanation': 'Cone-beam CT provides '
                                                           'three-dimensional detail of teeth, '
                                                           'bone, and anatomic relationships when '
                                                           'two-dimensional images cannot answer '
                                                           'the clinical question—for example '
                                                           'complex implant sites, impacted teeth '
                                                           'near nerves, or intricate endodontic '
                                                           'anatomy—balanced against higher dose.'},
                                           {'question': 'A ghost image on a panoramic radiograph '
                                                        'is?',
                                            'options': ['A) A true pathologic lesion requiring '
                                                        'biopsy',
                                                        'B) A blurred contralateral projection of '
                                                        'a dense object',
                                                        'C) A chemical processing artifact unique '
                                                        'to film developers',
                                                        'D) The printed patient-name label on the '
                                                        'film mount'],
                                            'answer': 'B) A blurred contralateral projection of a '
                                                      'dense object',
                                            'explanation': 'On panoramic imaging, dense objects on '
                                                           'one side of the jaw can cast a '
                                                           'blurred, magnified “ghost” image on '
                                                           'the contralateral side, projected '
                                                           'higher and more posteriorly because of '
                                                           'the rotational geometry. Recognizing '
                                                           'ghosts prevents false pathology '
                                                           'diagnosis.'},
                                           {'question': 'The SLOB rule helps the clinician '
                                                        'determine?',
                                            'options': ['A) Exposure time selection only',
                                                        'B) kVp chart values only',
                                                        'C) Buccolingual localization using '
                                                        'tube-shift radiographs',
                                                        'D) Processing chemical replenishment '
                                                        'schedules'],
                                            'answer': 'C) Buccolingual localization using '
                                                      'tube-shift radiographs',
                                            'explanation': 'The SLOB rule (Same Lingual, Opposite '
                                                           'Buccal) uses a horizontal tube shift '
                                                           'between two periapical radiographs to '
                                                           'localize an object buccolingually. If '
                                                           'the object moves in the same direction '
                                                           'as the tube head, it is lingual; '
                                                           'opposite movement indicates buccal '
                                                           'position.'}],
                                  'extreme': [{'question': 'Radiographic clues favoring a '
                                                           'malignant jaw lesion include?',
                                               'options': ['A) Ill-defined borders, cortical '
                                                           'destruction, and rapid change',
                                                           'B) Well-corticated unilocular slow '
                                                           'expansion',
                                                           'C) Uniform radiopaque torus morphology',
                                                           'D) Completely normal trabecular '
                                                           'pattern'],
                                               'answer': 'A) Ill-defined borders, cortical '
                                                         'destruction, and rapid change',
                                               'explanation': 'Malignant jaw lesions often destroy '
                                                              'bone with ill-defined, '
                                                              'non-corticated borders and cortical '
                                                              'perforation because neoplastic '
                                                              'growth outpaces host bone '
                                                              'remodeling. Rapid radiographic '
                                                              'change and tooth mobility with '
                                                              'widened PDL spaces heighten '
                                                              'concern.'},
                                              {'question': 'Typical effective-dose ranking among '
                                                           'common dental imaging modalities is?',
                                               'options': ['A) Bitewing effective dose exceeding '
                                                           'typical CBCT fields',
                                                           'B) Equal effective dose across '
                                                           'intraoral, panoramic, and CBCT',
                                                           'C) CBCT generally greater than '
                                                           'panoramic, which is generally greater '
                                                           'than intraoral',
                                                           'D) Clinical photography higher dose '
                                                           'than CBCT'],
                                               'answer': 'C) CBCT generally greater than '
                                                         'panoramic, which is generally greater '
                                                         'than intraoral',
                                               'explanation': 'Effective dose generally increases '
                                                              'from well-collimated intraoral '
                                                              'radiographs to panoramic imaging to '
                                                              'CBCT examinations of larger fields '
                                                              'of view, though exact values depend '
                                                              'on exposure parameters. Selection '
                                                              'criteria must match the diagnostic '
                                                              'task to the lowest adequate dose.'},
                                              {'question': 'Idiopathic osteosclerosis is '
                                                           'distinguished from condensing osteitis '
                                                           'chiefly by?',
                                               'options': ['A) Tooth vitality testing and clinical '
                                                           'inflammatory context',
                                                           'B) Treating every focal radiopacity '
                                                           'with root canal therapy',
                                                           'C) Assuming both represent malignancy '
                                                           'until resected',
                                                           'D) Extracting the associated tooth for '
                                                           'every radiopacity'],
                                               'answer': 'A) Tooth vitality testing and clinical '
                                                         'inflammatory context',
                                               'explanation': 'Idiopathic osteosclerosis is a '
                                                              'focal radiopacity in bone '
                                                              'associated with a vital tooth and '
                                                              'no inflammatory cause. Condensing '
                                                              'osteitis is a reactive bony '
                                                              'sclerosis at the apex of a tooth '
                                                              'with pulpitis or necrosis; vitality '
                                                              'and symptoms separate the two.'}]},
                    'cases': {'easy': [{'title': 'Suspected Interproximal Caries',
                                        'stem': 'Tight contacts, clinical doubt on upper '
                                                'premolars.',
                                        'question': 'Image of choice first?',
                                        'answer': 'Bitewings.',
                                        'discussion': 'Then restore if confirmed.',
                                        'book_hint': "White and Pharoah's Oral Radiology"}],
                              'medium': [{'title': 'Impacted Canine Localization',
                                          'stem': 'Need to know buccal/palatal position of '
                                                  'impacted canine.',
                                          'question': 'Options?',
                                          'answer': 'Parallax technique or CBCT when justified.',
                                          'discussion': 'Avoid unnecessary high-dose imaging.',
                                          'book_hint': "White and Pharoah's Oral Radiology"}],
                              'hard': [{'title': 'Unilocular Radiolucency Angle of Mandible',
                                        'stem': 'Impacted wisdom tooth with radiolucency around '
                                                'crown in a young adult. Choose the safest '
                                                'high-yield next concept before definitive '
                                                'results.',
                                        'question': 'Differential includes?',
                                        'answer': 'Dentigerous cyst among others — '
                                                  'remove/investigate histologically as indicated.',
                                        'discussion': 'Do not ignore enlarging lesions.',
                                        'book_hint': "White and Pharoah's Oral Radiology"}],
                              'extreme': [{'title': 'Ill-defined Mandibular Destruction',
                                           'stem': 'A rapidly enlarging numb chin, loose teeth, '
                                                   'and moth-eaten bone on radiograph. Avoid '
                                                   'harmful premature treatment while catastrophic '
                                                   'differentials remain open.',
                                           'question': 'Action?',
                                           'answer': 'Urgent biopsy/OMFS-oncology workup for '
                                                     'possible malignancy.',
                                           'discussion': 'Do not schedule elective cleaning only.',
                                           'book_hint': "White and Pharoah's Oral Radiology"}]}},
 'dental_anatomy': {'label': 'Dental Anatomy',
                    'books': ["Wheeler's Dental Anatomy, Physiology and Occlusion",
                              "Ash & Nelson's Dental Anatomy",
                              'Dental Anatomy review guides'],
                    'pdf_notes': ['32 permanent teeth; 20 primary.',
                                  'Know root/canal morphology for endo success.',
                                  'Carabelli trait on maxillary first molar.',
                                  'High pulp horns in young teeth.',
                                  'Anomalies (dens invaginatus, dilaceration) change plans.'],
                    'questions': {'easy': [{'question': 'How many teeth are in the complete '
                                                        'permanent dentition normally?',
                                            'options': ['A) 32',
                                                        'B) 20',
                                                        'C) 28 as the anatomic total including '
                                                        'third molars',
                                                        'D) 16'],
                                            'answer': 'A) 32',
                                            'explanation': 'The permanent dentition normally '
                                                           'comprises 8 incisors, 4 canines, 8 '
                                                           'premolars, and 12 molars, totaling 32 '
                                                           'teeth including third molars. '
                                                           'Congenitally missing third molars '
                                                           'reduce the clinical count but do not '
                                                           'change the anatomic norm of 32.'},
                                           {'question': 'How many teeth are in the complete '
                                                        'primary dentition?',
                                            'options': ['A) 32', 'B) 20', 'C) 12', 'D) 36'],
                                            'answer': 'B) 20',
                                            'explanation': 'The primary dentition consists of 8 '
                                                           'incisors, 4 canines, and 8 molars—20 '
                                                           'teeth total—with no premolars. '
                                                           'Premolars succeed the primary molars '
                                                           'in the mixed and permanent '
                                                           'dentitions.'},
                                           {'question': 'The cusp of Carabelli is '
                                                        'characteristically found on?',
                                            'options': ['A) Mandibular central incisor',
                                                        'B) Maxillary lateral incisor only',
                                                        'C) Mandibular canine',
                                                        'D) Maxillary first molar'],
                                            'answer': 'D) Maxillary first molar',
                                            'explanation': 'The cusp of Carabelli is an accessory '
                                                           'cusp or tubercle on the mesiolingual '
                                                           'surface of the maxillary first '
                                                           'permanent molar (and sometimes the '
                                                           'primary second molar). It is a common '
                                                           'morphologic variation with clinical '
                                                           'relevance for restoration contours.'}],
                                  'medium': [{'question': 'The maxillary first premolar most '
                                                          'commonly has?',
                                              'options': ['A) A single canal in every specimen',
                                                          'B) Three roots identical to a maxillary '
                                                          'molar',
                                                          'C) No cusps on the occlusal surface',
                                                          'D) Two roots and commonly two canals'],
                                              'answer': 'D) Two roots and commonly two canals',
                                              'explanation': 'The maxillary first premolar most '
                                                             'often has two roots—one buccal and '
                                                             'one palatal—and correspondingly two '
                                                             'root canals. This bifurcation has '
                                                             'direct endodontic and extraction '
                                                             'significance because both canals '
                                                             'must be located and instrumented.'},
                                             {'question': 'Proximal contact areas of anterior '
                                                          'teeth are usually located?',
                                              'options': ['A) At the cervical third only',
                                                          'B) Near the junction of the incisal and '
                                                          'middle thirds',
                                                          'C) At the root apex',
                                                          'D) Absent in a normal healthy arch'],
                                              'answer': 'B) Near the junction of the incisal and '
                                                        'middle thirds',
                                              'explanation': 'Proximal contact areas of anterior '
                                                             'teeth are typically located in the '
                                                             'incisal third, near the junction '
                                                             'with the middle third, creating a '
                                                             'contact that stabilizes the arch and '
                                                             'protects the interdental papilla '
                                                             'from food impaction.'},
                                             {'question': 'The curve of Spee is?',
                                              'options': ['A) The mediolateral occlusal curve of '
                                                          'Wilson',
                                                          'B) Bonwill’s equilateral triangle alone',
                                                          'C) The anteroposterior occlusal '
                                                          'curvature in the sagittal plane',
                                                          'D) Freeway space between rest and '
                                                          'occlusion'],
                                              'answer': 'C) The anteroposterior occlusal curvature '
                                                        'in the sagittal plane',
                                              'explanation': 'The curve of Spee is the '
                                                             'anteroposterior occlusal curvature '
                                                             'seen in the sagittal plane, concave '
                                                             'superiorly in the mandibular arch '
                                                             'from canine through posterior teeth. '
                                                             'It contributes to balanced occlusal '
                                                             'contacts in mandibular excursions.'}],
                                  'hard': [{'question': 'Mandibular first molars most typically '
                                                        'have which canal configuration?',
                                            'options': ['A) Often three canals (MB, ML, and '
                                                        'distal) with anatomic variations',
                                                        'B) A single canal in both roots in '
                                                        'virtually all teeth',
                                                        'C) Five separate canals named after '
                                                        'Carabelli',
                                                        'D) Absence of a pulp chamber in mature '
                                                        'teeth'],
                                            'answer': 'A) Often three canals (MB, ML, and distal) '
                                                      'with anatomic variations',
                                            'explanation': 'Mandibular first molars most commonly '
                                                           'have two roots with three principal '
                                                           'canals: mesiobuccal, mesiolingual, and '
                                                           'a distal canal (which may split into '
                                                           'two). Anatomic variations include a '
                                                           'middle mesial canal; missing canals '
                                                           'cause endodontic failure.'},
                                           {'question': 'Enamel thickness is greatest at?',
                                            'options': ['A) The cementoenamel junction',
                                                        'B) Occlusal and incisal contact areas '
                                                        '(cusp tips/incisal edges)',
                                                        'C) The root apex',
                                                        'D) Furcation entrances'],
                                            'answer': 'B) Occlusal and incisal contact areas (cusp '
                                                      'tips/incisal edges)',
                                            'explanation': 'Enamel reaches its greatest thickness '
                                                           'over cusp tips and incisal edges—the '
                                                           'functional contact areas that sustain '
                                                           'heavy occlusal load—while thinning '
                                                           'toward the cervix. This distribution '
                                                           'resists wear where forces are '
                                                           'highest.'},
                                           {'question': 'High pulp horns in young permanent teeth '
                                                        'relate most directly to?',
                                            'options': ['A) Increased risk of pulp exposure during '
                                                        'cavity preparation',
                                                        'B) Selection of ceramic shade tabs',
                                                        'C) Equal crown and root lengths in all '
                                                        'permanent teeth',
                                                        'D) Volume of supragingival calculus '
                                                        'deposits'],
                                            'answer': 'A) Increased risk of pulp exposure during '
                                                      'cavity preparation',
                                            'explanation': 'Pulp horns extend occlusally under '
                                                           'cusps and are relatively high in young '
                                                           'teeth before secondary dentin '
                                                           'accumulates. Cavity or crown '
                                                           'preparation that ignores horn height '
                                                           'risks mechanical pulp exposure.'}],
                                  'extreme': [{'question': 'Dens invaginatus elevates risk of?',
                                               'options': ['A) Improved enamel quality without '
                                                           'infection risk',
                                                           'B) Cutaneous freckling',
                                                           'C) Pulp infection via the invagination '
                                                           'channel',
                                                           'D) Torus mandibularis formation'],
                                               'answer': 'C) Pulp infection via the invagination '
                                                         'channel',
                                               'explanation': 'Dens invaginatus is an infolding of '
                                                              'the enamel organ into the dental '
                                                              'papilla, creating a deep palatal '
                                                              'pit continuous with a blind or open '
                                                              'channel toward the pulp. Oral '
                                                              'bacteria can rapidly infect the '
                                                              'pulp through this pathway, often '
                                                              'before deep caries is clinically '
                                                              'obvious.'},
                                              {'question': 'Taurodontism is characterized by?',
                                               'options': ['A) Short roots with dilacerated crowns '
                                                           'only',
                                                           'B) An enlarged pulp chamber with '
                                                           'apically displaced furcation',
                                                           'C) Dens evaginatus occlusal tubercles',
                                                           'D) Enamel pearls at furcation '
                                                           'entrances only'],
                                               'answer': 'B) An enlarged pulp chamber with '
                                                         'apically displaced furcation',
                                               'explanation': 'Taurodontism features an enlarged '
                                                              'pulp chamber with apical '
                                                              'displacement of the root furcation, '
                                                              'producing short roots relative to '
                                                              'crown–body height. The altered '
                                                              'chamber morphology complicates '
                                                              'canal location and increases risk '
                                                              'of perforation during endodontic '
                                                              'access.'},
                                              {'question': 'Root dilaceration most complicates?',
                                               'options': ['A) Shade selection for composite only',
                                                           'B) Routine flossing effectiveness',
                                                           'C) Rubber dam clamp color coding',
                                                           'D) Extraction path and endodontic '
                                                           'access'],
                                               'answer': 'D) Extraction path and endodontic access',
                                               'explanation': 'Dilaceration is a sharp bend in the '
                                                              'root or crown, usually from trauma '
                                                              'to the developing tooth germ. The '
                                                              'angulation impedes straight-line '
                                                              'endodontic access and increases '
                                                              'risk of root fracture or incomplete '
                                                              'removal during extraction.'}]},
                    'cases': {'easy': [{'title': 'Identify Tooth',
                                        'stem': 'A tooth has 3 roots and a Carabelli cusp trait.',
                                        'question': 'Most likely?',
                                        'answer': 'Maxillary first molar.',
                                        'discussion': 'Know morphology for endo/restorative.',
                                        'book_hint': "Wheeler's Dental Anatomy, Physiology and "
                                                     'Occlusion'}],
                              'medium': [{'title': 'Endo Access Planning',
                                          'stem': 'Upper first premolar needs RCT.',
                                          'question': 'Anatomy alert?',
                                          'answer': 'Often two canals — search carefully.',
                                          'discussion': 'Missed canal → failure.',
                                          'book_hint': "Wheeler's Dental Anatomy, Physiology and "
                                                       'Occlusion'}],
                              'hard': [{'title': 'Young Tooth Prep Exposure Risk',
                                        'stem': 'A teenager needs a deep occlusal restoration on a '
                                                'newly erupted molar. Choose the safest high-yield '
                                                'next concept before definitive results.',
                                        'question': 'Anatomy concern?',
                                        'answer': 'High pulp horns — careful depth, consider '
                                                  'indirect pulp strategies.',
                                        'discussion': 'Avoid iatrogenic exposure.',
                                        'book_hint': "Wheeler's Dental Anatomy, Physiology and "
                                                     'Occlusion'}],
                              'extreme': [{'title': 'Bizarre Root Morphology Pre-Extract',
                                           'stem': 'A curved dilacerated premolar needs extraction '
                                                   'under LA. Avoid harmful premature treatment '
                                                   'while catastrophic differentials remain open.',
                                           'question': 'Plan?',
                                           'answer': 'Radiograph assessment, surgical sectioning '
                                                     'readiness, avoid blind force.',
                                           'discussion': 'Prevent root fracture/displacement.',
                                           'book_hint': "Wheeler's Dental Anatomy, Physiology and "
                                                        'Occlusion'}]}}}

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
        "🩺 *CharaNas Dentistry*\n"
        "Undergraduate Dentistry Department\n\n"
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
