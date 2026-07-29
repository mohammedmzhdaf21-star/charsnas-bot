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
                                                      'C) Lateral incisor',
                                                      'D) First premolar'],
                                          'answer': 'B) Mandibular third molar',
                                          'explanation': 'Mandibular third molars are the teeth most frequently impacted because they erupt last and often lack adequate space in the dental arch. Impaction occurs when eruption is blocked by bone, soft tissue, or an adjacent tooth. Maxillary canines are the next most commonly impacted teeth, but far less often than lower wisdom teeth.'},
                                         {'question': 'Local anesthetic for inferior alveolar '
                                                      'nerve typically targets?',
                                          'options': ['A) Mental foramen only',
                                                      'B) Mandibular foramen region',
                                                      'C) Infraorbital foramen only',
                                                      'D) Greater palatine only'],
                                          'answer': 'B) Mandibular foramen region',
                                          'explanation': 'The inferior alveolar nerve enters the mandible at the mandibular foramen on the medial ramus. An inferior alveolar nerve block deposits anesthetic near this foramen so the solution bathes the nerve before it enters the mandibular canal. Successful anesthesia therefore depends on accurate needle placement relative to the lingula and mandibular foramen.'},
                                         {'question': 'Dry socket usually occurs after?',
                                          'options': ['A) Difficult extraction, especially lower '
                                                      'molars',
                                                      'B) Only fluoride varnish',
                                                      'C) Only scaling',
                                                      'D) Orthodontic bonding'],
                                          'answer': 'A) Difficult extraction, especially lower '
                                                    'molars',
                                          'explanation': 'Alveolar osteitis (dry socket) follows premature loss or lysis of the blood clot that normally protects the extraction socket. Exposed bone and inflammatory mediators produce severe pain, typically beginning two to four days after a difficult mandibular molar extraction. Risk rises with traumatic extraction, smoking, and poor clot stability.'}],
                                'medium': [{'question': 'Ludwig angina is infection of?',
                                            'options': ['A) Bilateral '
                                                        'submandibular/sublingual/submental spaces',
                                                        'B) Only maxillary sinus',
                                                        'C) Only pulp chamber',
                                                        'D) Only TMJ capsule'],
                                            'answer': 'A) Bilateral '
                                                      'submandibular/sublingual/submental spaces',
                                            'explanation': 'Ludwig angina is a rapidly spreading bilateral cellulitis of the submandibular, sublingual, and submental spaces, usually from an odontogenic source. Edema elevates the floor of the mouth and tongue, threatening the airway. Management prioritizes airway security, surgical drainage, and systemic antibiotics.'},
                                           {'question': 'INR is most relevant before surgery in '
                                                        'patients on?',
                                            'options': ['A) Warfarin',
                                                        'B) Amoxicillin only',
                                                        'C) Paracetamol only',
                                                        'D) Chlorhexidine only'],
                                            'answer': 'A) Warfarin',
                                            'explanation': 'Warfarin inhibits vitamin K–dependent clotting factors and is monitored with the international normalized ratio (INR). Before invasive oral surgery, the INR helps estimate bleeding risk so hemostasis can be planned safely. Antiplatelet and direct oral anticoagulant regimens require different assessment approaches than INR.'},
                                           {'question': 'Oroantral communication risk is highest '
                                                        'extracting?',
                                            'options': ['A) Maxillary molars',
                                                        'B) Lower incisors',
                                                        'C) Mandibular canines',
                                                        'D) Lower premolars always'],
                                            'answer': 'A) Maxillary molars',
                                            'explanation': 'Maxillary molar roots often lie close to, or project into, the maxillary sinus floor. Extraction can tear the thin antral bone or sinus membrane and create an oroantral communication. Mandibular teeth do not border the maxillary sinus, so this complication is characteristic of upper posterior extractions.'}],
                                'hard': [{'question': 'A junior colleague asks for the single best '
                                                      'answer. Which nerve injury risk is notable '
                                                      'in third molar surgery near the canal? '
                                                      'Beware of near-miss distractors.',
                                          'options': ['A) Inferior alveolar nerve',
                                                      'B) Optic nerve',
                                                      'C) Phrenic nerve',
                                                      'D) Recurrent laryngeal only'],
                                          'answer': 'A) Inferior alveolar nerve',
                                          'explanation': 'The inferior alveolar nerve runs in the mandibular canal and may lie immediately adjacent to mandibular third molar roots. Surgical elevation or sectioning of the tooth can stretch, crush, or transect the nerve, causing lip and chin paresthesia or anesthesia. Preoperative imaging assesses canal proximity to guide risk discussion and technique.'},
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
                                          'explanation': 'Medication-related osteonecrosis of the jaw (MRONJ) is exposed necrotic bone associated with antiresorptive or antiangiogenic drugs. Invasive procedures such as extractions disrupt oral mucosa and bone in a hypovascular, remodeling-impaired jaw, increasing MRONJ risk. Noninvasive care and careful surgical planning reduce that risk in susceptible patients.'},
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
                                          'explanation': 'A root tip displaced into the maxillary sinus can act as a foreign body, promoting sinusitis or sustaining an oroantral fistula. Management requires retrieval when indicated, closure of any communication, and sinus precautions or specialist referral. Leaving the fragment indefinitely risks chronic antral infection.'}],
                                'extreme': [{'question': 'In a high-stakes clinic scenario with '
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
                                             'explanation': 'Therapeutic anticoagulation reduces thromboembolic risk; abrupt cessation can precipitate stroke or venous thrombosis. For most dental extractions, continuing anticoagulation with meticulous local hemostasis (pressure, packing, sutures, tranexamic acid) is safer than unsupervised drug interruption. Physician coordination is used when bleeding risk is unusually high or INR is outside the therapeutic range.'},
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
                                             'explanation': 'An expanding neck hematoma after surgery can compress the airway, producing stridor, dyspnea, and rapid desaturation. Airway establishment takes absolute priority over investigating the bleeding source in the chair. Once the airway is secure, urgent surgical exploration and hemostasis follow.'},
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
                                             'explanation': 'High-dose radiotherapy damages bone vasculature and cellularity in the jaws, impairing healing after trauma. Extractions in irradiated bone therefore carry a recognized risk of osteoradionecrosis. Prevention emphasizes atraumatic technique, optimal oral health before radiotherapy, and specialist pathways when extractions become necessary afterward.'}]},
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
                                          'options': ['A) Lower molar distal to normal vs upper',
                                                      'B) Lower molar mesial to Class I',
                                                      'C) Only open bite',
                                                      'D) Only crossbite'],
                                          'answer': 'A) Lower molar distal to normal vs upper',
                                          'explanation': 'In Angle’s classification, Class II molar occlusion means the mandibular first molar is positioned distal to its normal relation with the maxillary first molar. Clinically, the mesiobuccal cusp of the upper first molar occludes mesial to the buccal groove of the lower first molar. This describes a sagittal discrepancy of the buccal segment.'},
                                         {'question': 'Overjet describes?',
                                          'options': ['A) Horizontal overlap of incisors',
                                                      'B) Vertical overlap only',
                                                      'C) Only molar torque',
                                                      'D) Only arch length'],
                                          'answer': 'A) Horizontal overlap of incisors',
                                          'explanation': 'Overjet is the horizontal distance between the labial surface of the mandibular incisors and the incisal edges of the maxillary incisors. Overbite, by contrast, measures vertical overlap of the incisors. Distinguishing the two is fundamental to describing malocclusion in the anteroposterior and vertical planes.'},
                                         {'question': 'Space maintainer is used when?',
                                          'options': ['A) Premature loss of primary teeth risks '
                                                      'space loss',
                                                      'B) Only adult periodontitis',
                                                      'C) Only bleaching',
                                                      'D) Only pulp capping'],
                                          'answer': 'A) Premature loss of primary teeth risks '
                                                    'space loss',
                                          'explanation': 'Early loss of a primary tooth allows adjacent teeth to drift into the edentulous space, shortening arch length and risking impaction or crowding of the successor. A space maintainer holds the mesiodistal dimension until the permanent tooth erupts. Preserving arch perimeter avoids more complex interceptive or comprehensive orthodontics later.'}],
                                'medium': [{'question': 'Crossbite with functional shift suggests?',
                                            'options': ['A) Possible premature contact / occlusal '
                                                        'interference',
                                                        'B) Only random habit',
                                                        'C) Only caries',
                                                        'D) Only fluorosis'],
                                            'answer': 'A) Possible premature contact / occlusal '
                                                      'interference',
                                            'explanation': 'A unilateral posterior crossbite with a mandibular functional shift often results from a premature occlusal contact that deflects the mandible on closure. The shift can produce asymmetric growth and muscle activity if left untreated. Early removal of the interfering contact or expansion to eliminate the shift is therefore indicated when a functional component is present.'},
                                           {'question': 'Anchorage in ortho means?',
                                            'options': ['A) Resistance to unwanted tooth movement',
                                                        'B) Only wire size',
                                                        'C) Only bracket color',
                                                        'D) Only elastic flavor'],
                                            'answer': 'A) Resistance to unwanted tooth movement',
                                            'explanation': 'Anchorage is the resistance to unwanted reciprocal tooth movement that Newton’s third law would otherwise produce during orthodontic force application. Without adequate anchorage, active teeth move as planned while reactive units tip or drift undesirably. Anchorage may be dental, muscular, extraoral, or skeletal (for example, TADs).'},
                                           {'question': 'Thumb sucking prolonged may cause?',
                                            'options': ['A) Open bite / proclined upper incisors',
                                                        'B) Only dens invaginatus',
                                                        'C) Only enamel pearl',
                                                        'D) Only tori'],
                                            'answer': 'A) Open bite / proclined upper incisors',
                                            'explanation': 'Prolonged non-nutritive sucking generates forward and intrusive forces on the maxillary incisors and impedes normal eruption of the anteriors. The resulting dentoalveolar changes commonly include anterior open bite and proclined upper incisors, sometimes with a narrow upper arch. Habit cessation before skeletal and dental patterns become entrenched improves spontaneous improvement potential.'}],
                                'hard': [{'question': 'A junior colleague asks for the single best '
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
                                          'explanation': 'Orthodontic tooth movement depends on controlled periodontal ligament stress; heavy or prolonged forces can trigger sterile inflammation and clastic activity on the root surface. External apical root resorption is therefore more likely with excessive force magnitude or duration and in teeth with morphological vulnerability. Periodic radiographs help detect progressive resorption during treatment.'},
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
                                          'explanation': 'Serial extraction is a planned sequence of primary and then selected permanent tooth removals in the mixed dentition when severe crowding is inevitable. The goal is to guide eruption into a more favorable alignment and reduce later complex mechanics. It is not indiscriminate extraction; case selection and timing require orthodontic diagnosis of space deficiency and growth.'},
                                         {'question': 'A junior colleague asks for the single best '
                                                      'answer. TADs provide? Beware of near-miss '
                                                      'distractors.',
                                          'options': ['A) Skeletal anchorage',
                                                      'B) Only fluoride release',
                                                      'C) Only bleaching',
                                                      'D) Only anesthesia'],
                                          'answer': 'A) Skeletal anchorage',
                                          'explanation': 'Temporary anchorage devices (TADs) are mini-implants or plates fixed to bone to provide absolute or near-absolute anchorage. Because they do not rely on reciprocal tooth support, they allow force systems that would otherwise move anchor teeth. They are removed after the needed tooth movements are completed.'}],
                                'extreme': [{'question': 'In a high-stakes clinic scenario with '
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
                                             'explanation': 'Periodontitis involves plaque-driven inflammation and progressive attachment loss; orthodontic forces applied through an inflamed periodontium can accelerate destruction. Disease control (biofilm management and stable probing depths) must precede elective tooth movement. Light forces and periodontal co-management then minimize further attachment loss during alignment.'},
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
                                             'explanation': 'An ectopically erupting maxillary canine can physically resorb the roots of adjacent lateral or central incisors through direct contact and pressure. The risk rises when the canine crown overlies the incisor root on imaging. Timely localization, exposure, and traction—or extraction of the deciduous canine when indicated—reduces progressive resorption.'},
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
                                             'explanation': 'Class III malocclusion may be dental, skeletal, or combined; treatment choice depends on remaining growth, skeletal severity, soft-tissue profile, and occlusal discrepancy. Mild dental Class III may be camouflaged with tooth movement, whereas significant skeletal disharmony in a nongrowing patient often requires orthognathic surgery with orthodontics. Growth modification is considered only while clinically useful growth remains.'}]},
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
                                          'options': ['A) Dental biofilm',
                                                      'B) Only malocclusion',
                                                      'C) Only dens evaginatus',
                                                      'D) Only torus palatinus'],
                                          'answer': 'A) Dental biofilm',
                                          'explanation': 'Plaque-induced gingivitis is an inflammatory response of the gingiva to accumulation of dental biofilm at the gingival margin. Microbial products trigger vascular dilation, leukocyte infiltration, and clinical erythema and bleeding. When biofilm is disrupted by effective oral hygiene, the gingiva returns to health without irreversible attachment loss.'},
                                         {'question': 'Clinical hallmark of periodontitis vs '
                                                      'gingivitis?',
                                          'options': ['A) Clinical attachment loss / bone loss',
                                                      'B) Only reversible redness forever without '
                                                      'loss',
                                                      'C) Only stain',
                                                      'D) Only calculus without inflammation ever'],
                                          'answer': 'A) Clinical attachment loss / bone loss',
                                          'explanation': 'Gingivitis is inflammation confined to the soft tissue, whereas periodontitis is defined by destruction of the periodontal ligament and alveolar bone, measured as clinical attachment loss. Pocketing alone does not confirm periodontitis without attachment or bone loss. Distinguishing the two guides prognosis and the intensity of therapy.'},
                                         {'question': 'Best daily plaque control tool foundation?',
                                          'options': ['A) Toothbrushing ± interdental cleaning',
                                                      'B) Only whitening strips',
                                                      'C) Only chewing ice',
                                                      'D) Only charcoal powder alone'],
                                          'answer': 'A) Toothbrushing ± interdental cleaning',
                                          'explanation': 'Dental biofilm must be disrupted mechanically because saliva and rinses alone do not remove adherent plaque from tooth surfaces. Toothbrushing cleans facial and lingual surfaces; interdental aids clean contact areas where periodontitis often begins. Consistent mechanical plaque control is therefore the foundation of periodontal health.'}],
                                'medium': [{'question': 'Furcation involvement is assessed on?',
                                            'options': ['A) Multirooted teeth',
                                                        'B) Only incisors',
                                                        'C) Only canines',
                                                        'D) Only primary laterals'],
                                            'answer': 'A) Multirooted teeth',
                                            'explanation': 'Furcation involvement is pathologic bone loss between the roots of multirooted teeth, exposing the furcation entrance. Single-rooted teeth lack furcations, so this assessment applies to molars and some premolars. Nabers and curved probes help detect horizontal furcation invasion and grade its severity.'},
                                           {'question': 'Smoking effect on perio?',
                                            'options': ['A) Increases risk/severity; masks '
                                                        'bleeding',
                                                        'B) Protects attachment always',
                                                        'C) Only whitens naturally',
                                                        'D) No effect'],
                                            'answer': 'A) Increases risk/severity; masks bleeding',
                                            'explanation': 'Tobacco smoking impairs neutrophil function, reduces gingival blood flow, and alters cytokine responses, increasing periodontitis risk and severity. Reduced vascularity also masks gingival bleeding, so disease may appear less inflamed than it is. Smoking cessation is therefore a major modifiable factor in periodontal therapy outcomes.'},
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
                                            'explanation': 'Rapidly progressive periodontitis in young patients (historically localized aggressive periodontitis) features severe attachment loss out of proportion to local deposits. Aggregatibacter actinomycetemcomitans has been classically associated with the localized molar–incisor pattern. Early recognition allows intensive mechanical therapy and, when indicated, adjunctive antimicrobials.'}],
                                'hard': [{'question': 'A junior colleague asks for the single best '
                                                      'answer. Periodontal abscess urgent care '
                                                      'includes? Beware of near-miss distractors.',
                                          'options': ['A) Drainage + debridement + antimicrobials '
                                                      'if systemic signs',
                                                      'B) Only bleach tray',
                                                      'C) Only ortho wax',
                                                      'D) Only nightguard forever'],
                                          'answer': 'A) Drainage + debridement + antimicrobials if '
                                                    'systemic signs',
                                          'explanation': 'A periodontal abscess is a localized purulent infection within a periodontal pocket or furcation. Drainage of pus, debridement of the pocket, and systemic antimicrobials when there are fever or spreading signs reduce bacterial load and pressure. Addressing the underlying periodontitis prevents recurrence.'},
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
                                          'explanation': 'Peri-implant mucositis is reversible soft-tissue inflammation around an implant without progressive bone loss. Peri-implantitis adds progressive crestal bone loss to inflammation and probing changes, threatening implant stability. The distinction matters because bone loss requires more intensive anti-infective and often surgical management.'},
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
                                          'explanation': 'Occlusal trauma produces adaptive or pathologic changes in the periodontium from excessive occlusal load, but it does not initiate the plaque-induced inflammatory pathway of periodontitis. When inflammation is already present, trauma can act as a co-destructive factor accelerating attachment loss. Controlling biofilm remains essential; occlusal adjustment alone does not cure periodontitis.'}],
                                'extreme': [{'question': 'In a high-stakes clinic scenario with '
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
                                             'explanation': 'Necrotizing ulcerative gingivitis presents with painful punched-out interdental papillae, spontaneous bleeding, and often fetor oris. Fusospirochetal overgrowth in a host compromised by stress, smoking, or immunodeficiency drives superficial necrosis. Debridement, oral hygiene, and management of predisposing factors reverse the acute process.'},
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
                                             'explanation': 'A pregnancy epulis is a pyogenic granuloma arising from gingiva under the influence of elevated pregnancy hormones and local irritants. It is a reactive vascular lesion, not a true neoplasm, and frequently regresses after parturition. Persistent lesions may be excised if they interfere with function or hygiene.'},
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
                                             'explanation': 'Guided tissue regeneration uses a barrier membrane to exclude gingival epithelium and connective tissue from the periodontal defect, allowing periodontal ligament and bone cells to repopulate the root surface. The intended outcome is regeneration of cementum, periodontal ligament, and alveolar bone rather than repair by long junctional epithelium alone. Case selection favors contained infrabony defects.'}]},
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
                 'questions': {'easy': [{'question': 'Irreversible pulpitis pain is often?',
                                         'options': ['A) Spontaneous / lingering to cold',
                                                     'B) Only brief to sweet always reversible',
                                                     'C) Only itching',
                                                     'D) Only TMJ click'],
                                         'answer': 'A) Spontaneous / lingering to cold',
                                         'explanation': 'Symptomatic irreversible pulpitis reflects vital pulp tissue with inflammation severe enough that it cannot resolve even after removal of the irritant. C-fiber–mediated pain is often spontaneous and lingers after thermal stimulation, especially cold. Root canal treatment or extraction is required because the pulp will not heal.'},
                                        {'question': 'Best isolation for RCT?',
                                         'options': ['A) Rubber dam',
                                                     'B) Cotton only forever',
                                                     'C) No isolation',
                                                     'D) Only cheek retractor'],
                                         'answer': 'A) Rubber dam',
                                         'explanation': 'A rubber dam isolates the tooth from saliva and oral microbes, preventing contamination of the root canal system during instrumentation and obturation. It also protects the airway from instruments and irrigants. Isolation is therefore a standard infection-control and safety requirement for nonsurgical endodontics.'},
                                        {'question': 'Working length aims to prepare to?',
                                         'options': ['A) Near apical constriction / radiographic '
                                                     'apex protocols',
                                                     'B) Beyond bone into sinus always',
                                                     'C) Only to pulp horn',
                                                     'D) Only CEJ'],
                                         'answer': 'A) Near apical constriction / radiographic '
                                                   'apex protocols',
                                         'explanation': 'The apical constriction is the narrowest point of the canal near the cementoenamel or cementodentinal junction and is the usual physiologic terminus for canal preparation. Working length is set to this region (or per radiographic/electronic apex protocols) to clean the canal while limiting extrusion of debris and irrigant into periapical tissues. Overinstrumentation beyond the apex traumatizes the periodontium.'}],
                               'medium': [{'question': 'Necrotic pulp with apical radiolucency '
                                                       'suggests?',
                                           'options': ['A) Apical periodontitis',
                                                       'B) Only reversible pulpitis',
                                                       'C) Only enamel hypoplasia',
                                                       'D) Only fluorosis'],
                                           'answer': 'A) Apical periodontitis',
                                           'explanation': 'Pulp necrosis allows bacteria and their toxins to exit through apical foramina into the periodontal ligament and bone. The resulting inflammatory bone resorption appears as a periapical radiolucency and is diagnosed as apical periodontitis. Vitality testing correlates the radiographic finding with a nonvital pulp.'},
                                          {'question': 'NaOCl is used as?',
                                           'options': ['A) Irrigant with '
                                                       'tissue-dissolving/antimicrobial action',
                                                       'B) Obturation sealer only',
                                                       'C) Temporary filling only',
                                                       'D) Local anesthetic'],
                                           'answer': 'A) Irrigant with '
                                                     'tissue-dissolving/antimicrobial action',
                                           'explanation': 'Sodium hypochlorite dissolves necrotic pulp tissue and has broad antimicrobial activity against canal flora, making it the primary endodontic irrigant. Its cytotoxicity means extrusion beyond the apex can damage soft tissue. Careful irrigation technique and appropriate concentration reduce that risk while maintaining cleaning efficacy.'},
                                          {'question': 'Cracked tooth pain often on?',
                                           'options': ['A) Release of biting pressure',
                                                       'B) Only hot coffee forever without bite',
                                                       'C) Only when lying flat without bite',
                                                       'D) Only to percussion of adjacent tooth '
                                                       'always'],
                                           'answer': 'A) Release of biting pressure',
                                           'explanation': 'In a cracked tooth, occlusal load briefly separates the crack walls and stimulates the pulp or periodontal ligament; pain is characteristically sharp on release of biting pressure as the segments snap back. A bite test on individual cusps helps localize the crack. Early diagnosis guides cuspal coverage or endodontic therapy before the crack propagates.'}],
                               'hard': [{'question': 'A junior colleague asks for the single best '
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
                                         'explanation': 'Forceful extrusion of sodium hypochlorite into periapical tissues causes immediate chemical burns of soft tissue and vessels. Patients experience sudden severe pain, rapid swelling, and often ecchymosis or hemorrhage along fascial planes. Irrigation is stopped, supportive care is given, and the patient is monitored for airway and tissue sequelae.'},
                                        {'question': 'A junior colleague asks for the single best '
                                                     'answer. Missed second mesiobuccal canal '
                                                     '(MB2) in upper molars causes? Beware of '
                                                     'near-miss distractors.',
                                         'options': ['A) Persistent infection/failure risk',
                                                     'B) Only better prognosis always',
                                                     'C) Only color change of face',
                                                     'D) Only gingival hyperplasia'],
                                         'answer': 'A) Persistent infection/failure risk',
                                         'explanation': 'Maxillary molars frequently have a second mesiobuccal canal (MB2) that branches within the mesiobuccal root. If untreated, residual bacteria in MB2 sustain periapical inflammation and cause post-treatment disease. Magnification and careful troughing of the mesiobuccal groove improve MB2 detection.'},
                                        {'question': 'A junior colleague asks for the single best '
                                                     'answer. Vertical root fracture prognosis is '
                                                     'often? Beware of near-miss distractors.',
                                         'options': ['A) Poor; extraction commonly',
                                                     'B) Always heal with RCT alone',
                                                     'C) Always ignore',
                                                     'D) Always bleach'],
                                         'answer': 'A) Poor; extraction commonly',
                                         'explanation': 'A complete vertical root fracture separates the root along its long axis, creating a pathway for bacteria from the oral cavity into the periodontium. The resulting localized deep pocket and bone loss rarely heal with root canal therapy alone. Extraction (or root resection in selected multi-rooted teeth) is therefore commonly required.'}],
                               'extreme': [{'question': 'In a high-stakes clinic scenario with '
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
                                            'explanation': 'Periodontal ligament cells on an avulsed tooth die progressively with extraoral dry time; beyond about 60 minutes of dry storage, PDL viability is severely compromised. Replantation may still be attempted per IADT guidelines, but ankylosis and replacement resorption become likely. Immediate storage in appropriate media before arrival improves prognosis when dry time is shorter.'},
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
                                            'explanation': 'Combined perio-endo lesions involve communication between pulpal and periodontal infection pathways, so both niches must be disinfected for healing. When the primary source is endodontic, root canal treatment is usually completed first because it can resolve the periodontal component of a true combined lesion. Persistent periodontal pockets then receive definitive periodontal therapy.'},
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
                                            'explanation': 'Internal resorption begins within the pulp chamber or canal from inflamed pulp tissue and appears as a ballooned canal outline that moves with tube shift less than external defects. External cervical or apical resorption originates on the root surface and has different radiographic borders and treatment needs. Distinguishing them—often aided by CBCT—determines whether pulp therapy, root surface management, or extraction is appropriate.'}]},
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
                    'questions': {'easy': [{'question': 'Ferrule effect improves?',
                                            'options': ['A) Fracture resistance of crowned '
                                                        'endodontically treated teeth',
                                                        'B) Only shade matching',
                                                        'C) Only cement color',
                                                        'D) Only tray adhesive'],
                                            'answer': 'A) Fracture resistance of crowned '
                                                      'endodontically treated teeth',
                                            'explanation': 'A ferrule is a band of sound axial tooth structure of adequate height and thickness encircled by the crown margin. It braces the tooth against functional lever forces, reducing the risk of root fracture in endodontically treated, crowned teeth. Approximately 2 mm of circumferential ferrule is the classic biomechanical target when tooth structure allows.'},
                                           {'question': 'Kennedy Class I RPD is?',
                                            'options': ['A) Bilateral distal extension',
                                                        'B) Single tooth gap only',
                                                        'C) Only anterior bounded',
                                                        'D) Only full denture'],
                                            'answer': 'A) Bilateral distal extension',
                                            'explanation': 'Kennedy Class I describes a bilateral edentulous area posterior to the remaining natural teeth (bilateral distal extension). Because terminal abutments are absent, the denture base is supported largely by residual ridge mucosa under load. This support pattern differs from tooth-borne Kennedy Class III frameworks.'},
                                           {'question': 'Impression for crowns needs?',
                                            'options': ['A) Accurate margins and soft tissue '
                                                        'management',
                                                        'B) Only alginate always for final PFM',
                                                        'C) Only wax bite forever',
                                                        'D) Only shade tab photo'],
                                            'answer': 'A) Accurate margins and soft tissue '
                                                      'management',
                                            'explanation': 'Cast restorations depend on an impression that records the finish line in undistorted detail and relates soft tissues without tears or voids. Hemostasis, cord or paste retraction, and moisture control expose the margin so die accuracy is possible. An inaccurate margin recording produces open margins, overhangs, or ill-fitting crowns.'}],
                                  'medium': [{'question': 'Biological width violation may cause?',
                                              'options': ['A) Chronic inflammation / bone loss',
                                                          'B) Only better papilla',
                                                          'C) Only faster ortho',
                                                          'D) Only whitening'],
                                              'answer': 'A) Chronic inflammation / bone loss',
                                              'explanation': 'Supracrestal tissue attachment (biological width) is the combined junctional epithelium and connective tissue attachment coronal to alveolar crest. Placing a restoration margin that invades this zone chronically inflames the periodontium. The host response may produce persistent gingivitis or crestal bone loss until space for the attachment is reestablished.'},
                                             {'question': 'Implant vs tooth abutment key '
                                                          'difference?',
                                              'options': ['A) No PDL proprioception/same mobility '
                                                          'profile',
                                                          'B) Identical biomechanics always',
                                                          'C) Implants never fail',
                                                          'D) Teeth never fail'],
                                              'answer': 'A) No PDL proprioception/same mobility '
                                                        'profile',
                                              'explanation': 'Natural teeth are suspended by a periodontal ligament that provides proprioception and physiologic mobility; osseointegrated implants are ankylosed to bone without a PDL. Occlusal forces are therefore transmitted more rigidly to implant bone, and tactile feedback differs. Prosthetic occlusion is planned to respect these biomechanical differences and avoid overload.'},
                                             {'question': 'Immediate denture is delivered?',
                                              'options': ['A) At extraction appointment',
                                                          'B) Only after 2 years always',
                                                          'C) Only before any exam',
                                                          'D) Only for orthodontics'],
                                              'answer': 'A) At extraction appointment',
                                              'explanation': 'An immediate denture is fabricated before extractions and inserted at the same appointment the teeth are removed. It maintains appearance and limited function during healing while acting as a protective surgical dressing. Soft-tissue and ridge remodeling later necessitate relines or a definitive prosthesis.'}],
                                  'hard': [{'question': 'A junior colleague asks for the single '
                                                        'best answer. Cantilever bridge risks? '
                                                        'Beware of near-miss distractors.',
                                            'options': ['A) Leverage overload of abutments',
                                                        'B) Always safest design',
                                                        'C) Never fails',
                                                        'D) Only better than implants always'],
                                            'answer': 'A) Leverage overload of abutments',
                                            'explanation': 'A cantilever fixed dental prosthesis has an abutment at only one end of the pontic, creating a class I lever under occlusal load. Moments concentrate stress in the abutment tooth, cement lute, and periodontal support, raising risks of decementation, fracture, or periodontal injury. Indication is therefore limited and biomechanically cautious.'},
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
                                            'explanation': 'Cement-retained implant crowns can offer esthetic continuity without an occlusal screw access hole, but excess subgingival cement is difficult to remove and is strongly linked to peri-implant inflammation. Screw-retained designs trade that cement risk for a visible or restored access channel and easier retrievability. Choice balances retrievability, esthetics, and cement control.'},
                                           {'question': 'A junior colleague asks for the single '
                                                        'best answer. Surveying an RPD cast '
                                                        'determines? Beware of near-miss '
                                                        'distractors.',
                                            'options': ['A) Path of insertion and undercuts',
                                                        'B) Only shade',
                                                        'C) Only patient age',
                                                        'D) Only bite force'],
                                            'answer': 'A) Path of insertion and undercuts',
                                            'explanation': 'Surveying orients a diagnostic cast to a chosen path of insertion and identifies soft- and hard-tissue undercuts relative to that path. Clasp tips are then placed in measured undercut, guiding planes are planned, and interferences to insertion are eliminated. Without surveying, clasp retention and framework seating become unpredictable.'}],
                                  'extreme': [{'question': 'In a high-stakes clinic scenario with '
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
                                               'explanation': 'Full-mouth rehabilitation fails if active caries or periodontitis undermines new restorations, so disease control comes first. Vertical dimension, occlusal scheme, and esthetics are then tested in provisionals that allow neuromuscular and phonetic evaluation. Only after stability in provisionals are definitive restorations fabricated.'},
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
                                               'explanation': 'Combination syndrome classically occurs with a complete maxillary denture opposing mandibular anterior natural teeth (often with missing posterior support). Heavy anterior occlusal forces drive flabby anterior maxillary ridge resorption, papillary hyperplasia, and overeruption of mandibular anteriors with distal mandibular bone loss. Restoring posterior support and balancing occlusion mitigate the destructive pattern.'},
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
                                               'explanation': 'Passive fit means an implant framework seats on abutments without inducing tensile or compressive strain in the screws or peri-implant bone. Casting or scanning distortion that leaves a misfit creates constant preload stress, promoting screw loosening, component fracture, and bone microdamage. Verification of fit before final torque is therefore essential.'}]},
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
                         'questions': {'easy': [{'question': 'First permanent tooth often '
                                                             'erupting?',
                                                 'options': ['A) Mandibular first molar ~6 years',
                                                             'B) Wisdom tooth at 3 years',
                                                             'C) Maxillary lateral at 2 years '
                                                             'always',
                                                             'D) Canine at 4 months'],
                                                 'answer': 'A) Mandibular first molar ~6 years',
                                                 'explanation': 'The mandibular first permanent molars typically erupt around age six and are often the first permanent teeth to appear, distal to the primary second molars. They establish the foundation of the permanent occlusion. Their early eruption and deep pits make them important targets for sealants and caries prevention.'},
                                                {'question': 'Fluoride varnish helps prevent?',
                                                 'options': ['A) Caries',
                                                             'B) Only malocclusion',
                                                             'C) Only ankylosis',
                                                             'D) Only supernumerary teeth'],
                                                 'answer': 'A) Caries',
                                                 'explanation': 'Fluoride varnish delivers a high fluoride concentration that promotes remineralization of enamel and forms calcium fluoride–like reservoirs on the tooth surface. Repeated professional application reduces caries incidence in children at risk. It is a topical preventive measure, not a restorative treatment for cavitated lesions.'},
                                                {'question': 'Pulpotomy is often for?',
                                                 'options': ['A) Primary teeth with coronal '
                                                             'pulpitis and restorable tooth',
                                                             'B) Only adult implants',
                                                             'C) Only ortho',
                                                             'D) Only bleaching'],
                                                 'answer': 'A) Primary teeth with coronal pulpitis '
                                                           'and restorable tooth',
                                                 'explanation': 'Pulpotomy removes inflamed coronal pulp while preserving radicular pulp vitality in a restorable primary tooth, usually after carious or traumatic exposure with healthy root pulp. Medicaments dress the amputated pulp stumps to encourage healing or fixation. The tooth can then function until normal exfoliation if radicular pathology does not develop.'}],
                                       'medium': [{'question': 'SSC (stainless steel crown) '
                                                               'indication classic?',
                                                   'options': ['A) Multi-surface caries in primary '
                                                               'molars',
                                                               'B) Only shade try-in',
                                                               'C) Only veneers',
                                                               'D) Only bleaching trays'],
                                                   'answer': 'A) Multi-surface caries in primary '
                                                             'molars',
                                                   'explanation': 'Primary molars with multi-surface caries often lack sufficient tooth structure for durable intracoronal restorations and are subject to high occlusal load. Stainless steel crowns encircle and protect the remaining crown, providing full-coverage retention until exfoliation. They are the restoration of choice for extensive primary molar decay after appropriate pulp therapy when needed.'},
                                                  {'question': 'Early childhood caries pattern '
                                                               'often?',
                                                   'options': ['A) Maxillary anterior teeth',
                                                               'B) Only lower anteriors protected '
                                                               'by tongue sometimes relatively '
                                                               'spared',
                                                               'C) Only third molars',
                                                               'D) Only impacted canines'],
                                                   'answer': 'A) Maxillary anterior teeth',
                                                   'explanation': 'Early childhood caries classically affects maxillary primary incisors because sweetened liquids pool around them during bottle or sippy-cup use, especially at night when salivary flow is low. Mandibular incisors are partly protected by the tongue and saliva. The pattern reflects prolonged fermentable carbohydrate exposure on susceptible enamel.'},
                                                  {'question': 'Behavior guidance basic first '
                                                               'line?',
                                                   'options': ['A) Tell-show-do / communication',
                                                               'B) Always immediate GA',
                                                               'C) Always papoose without consent '
                                                               'themes',
                                                               'D) Ignore fear'],
                                                   'answer': 'A) Tell-show-do / communication',
                                                   'explanation': 'Tell-show-do introduces the child to instruments and sensations in a nonthreatening sequence, reducing fear through predictable communication. It establishes trust and cooperation before more advanced behavior guidance is considered. Basic communicative techniques are first-line for most pediatric dental visits.'}],
                                       'hard': [{'question': 'A junior colleague asks for the '
                                                             'single best answer. Intrusion of '
                                                             'primary tooth concern? Beware of '
                                                             'near-miss distractors.',
                                                 'options': ['A) Damage to permanent successor',
                                                             'B) Only freckle',
                                                             'C) Only sinusitis always',
                                                             'D) Only TMJ ankylosis always'],
                                                 'answer': 'A) Damage to permanent successor',
                                                 'explanation': 'The developing permanent successor lies in close proximity to the primary tooth root; intrusive luxation can drive the primary root against the permanent tooth germ. Sequelae include enamel hypoplasia, dilaceration, or eruption disturbance of the permanent tooth. Clinical and radiographic follow-up monitors the successor’s development.'},
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
                                                 'explanation': 'The primary second molar holds the leeway space and guides eruption of the first permanent molar. Early loss allows the permanent molar to drift mesially, consuming space needed for the premolars and causing crowding or impaction. A space maintainer is considered to preserve that arch length when indicated.'},
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
                                                 'explanation': 'Molar-incisor hypomineralization is a qualitative enamel defect producing demarcated opacities on first permanent molars and often incisors. Hypomineralized enamel is porous, sensitive, and prone to post-eruptive breakdown under mastication. Early diagnosis guides desensitizing care, sealants or restorations, and sometimes stainless steel crowns.'}],
                                       'extreme': [{'question': 'In a high-stakes clinic scenario '
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
                                                    'explanation': 'Injuries that do not match the stated mechanism, developmental stage, or alleged timing raise concern for non-accidental trauma. Dentists have a professional and legal duty to recognize patterned oral injuries and escalate safeguarding. Documentation and referral protect the child when abuse or neglect is suspected.'},
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
                                                    'explanation': 'General anesthesia for dentistry is reserved when extensive treatment needs cannot be completed safely with behavioral guidance, local anesthesia, or sedation—especially with medical or developmental complexity. It allows definitive care in one controlled episode but carries systemic risk that requires informed consent. Alternatives should be considered and documented first.'},
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
                                                    'explanation': 'Replanting an avulsed primary tooth risks damage to the underlying permanent tooth germ from the primary root or from inflammatory sequelae. IADT guidelines therefore advise against replantation of primary teeth, unlike many permanent-tooth avulsion protocols. Soft-tissue management and follow-up of the successor take priority.'}]},
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
                   'questions': {'easy': [{'question': 'Aphthous ulcers usually occur on?',
                                           'options': ['A) Non-keratinized mucosa',
                                                       'B) Only attached gingiva always',
                                                       'C) Only hard palate always',
                                                       'D) Only vermilion only always'],
                                           'answer': 'A) Non-keratinized mucosa',
                                           'explanation': 'Recurrent aphthous ulcers arise on non-keratinized mucosa such as the buccal mucosa, floor of mouth, and ventral tongue, where the epithelium is thinner and more mobile. They do not typically begin on attached gingiva or hard palate, sites more characteristic of recurrent herpes labialis/intraoral HSV. The anatomic pattern helps differentiate aphthae from herpetic lesions.'},
                                          {'question': 'Leukoplakia definition theme?',
                                           'options': ['A) White patch that cannot be wiped or '
                                                       'diagnosed as another disease',
                                                       'B) Always candidiasis wipeable',
                                                       'C) Always lichen planus certain',
                                                       'D) Always normal linea alba'],
                                           'answer': 'A) White patch that cannot be wiped or '
                                                     'diagnosed as another disease',
                                           'explanation': 'Oral leukoplakia is a clinical diagnosis of exclusion: a white plaque that cannot be wiped away and cannot be attributed to another defined disease such as candidiasis or lichen planus. A subset harbors dysplasia or carcinoma, so biopsy is required for definitive assessment. Risk correlates with tobacco use and lesion appearance.'},
                                          {'question': 'Geographic tongue is?',
                                           'options': ['A) Benign migratory glossitis',
                                                       'B) Always cancer',
                                                       'C) Always syphilis',
                                                       'D) Always trauma only'],
                                           'answer': 'A) Benign migratory glossitis',
                                           'explanation': 'Geographic tongue (benign migratory glossitis) shows migrating areas of filiform papilla atrophy surrounded by slightly raised white borders. It is an inflammatory but benign condition of unknown precise cause and often asymptomatic. Recognition avoids unnecessary biopsy when classic features are present and the patient can be reassured.'}],
                                 'medium': [{'question': 'Oral candidiasis risk factor?',
                                             'options': ['A) Antibiotics / steroids / dentures / '
                                                         'xerostomia / immunosuppression',
                                                         'B) Only orthodontic wax',
                                                         'C) Only flossing',
                                                         'D) Only sealants'],
                                             'answer': 'A) Antibiotics / steroids / dentures / '
                                                       'xerostomia / immunosuppression',
                                             'explanation': 'Candida albicans is an oral commensal that overgrows when local or systemic defenses fall—broad-spectrum antibiotics, corticosteroids, denture bases, xerostomia, or immunosuppression. Pseudomembranous or erythematous candidiasis results from this ecological shift. Therapy combines antifungal medication with correction of predisposing factors.'},
                                            {'question': 'Lichen planus oral classic?',
                                             'options': ['A) Reticular white striae (Wickham)',
                                                         'B) Only punched necrotic papillae of NUG',
                                                         'C) Only measles Koplik always',
                                                         'D) Only Fordyce granules'],
                                             'answer': 'A) Reticular white striae (Wickham)',
                                             'explanation': 'Oral lichen planus is a T-cell–mediated mucocutaneous disease; the reticular form shows lace-like white striae (Wickham striae), often bilaterally on the buccal mucosa. Erosive forms may cause pain and require distinction from other vesiculobullous diseases. Biopsy is indicated when the diagnosis is uncertain or dysplasia must be excluded.'},
                                            {'question': 'SCC risk factors include?',
                                             'options': ['A) Tobacco and alcohol',
                                                         'B) Only xylitol gum',
                                                         'C) Only electric toothbrush',
                                                         'D) Only aligners'],
                                             'answer': 'A) Tobacco and alcohol',
                                             'explanation': 'Tobacco and alcohol are synergistic carcinogens for oral squamous cell carcinoma, causing cumulative DNA damage in keratinocytes of the oral epithelium. Chronic exposure drives dysplasia and invasive carcinoma, especially on the lateral tongue and floor of mouth. Suspicious, persistent lesions require biopsy regardless of painlessness.'}],
                                 'hard': [{'question': 'A junior colleague asks for the single '
                                                       'best answer. Pemphigus vulgaris oral clue? '
                                                       'Beware of near-miss distractors.',
                                           'options': ['A) Flaccid bullae / positive Nikolsky / '
                                                       'desquamative gingivitis themes',
                                                       'B) Only Fordyce',
                                                       'C) Only torus',
                                                       'D) Only amalgam tattoo'],
                                           'answer': 'A) Flaccid bullae / positive Nikolsky / '
                                                     'desquamative gingivitis themes',
                                           'explanation': 'Pemphigus vulgaris is an autoimmune acantholysis caused by autoantibodies against desmogleins, producing flaccid intraepithelial bullae that rupture easily (Nikolsky sign positive) and painful erosions, including desquamative gingivitis. Oral lesions often precede skin disease. Definitive diagnosis uses histopathology plus direct immunofluorescence.'},
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
                                           'explanation': 'Sjögren syndrome is an autoimmune destruction of exocrine glands that markedly reduces salivary flow. Hyposalivation impairs buffering and clearance of dietary sugars, sharply elevating caries risk and candidiasis. Intensive fluoride, dietary counseling, and saliva management are essential dental care components.'},
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
                                           'explanation': 'The odontogenic keratocyst (keratocystic odontogenic tumor in older terminology) arises from dental lamina rests and is lined by parakeratinized stratified squamous epithelium with high proliferative activity. It tends to grow along medullary bone with relatively little cortical expansion and has a high recurrence rate after simple enucleation. Surgical planning accounts for this biological behavior.'}],
                                 'extreme': [{'question': 'In a high-stakes clinic scenario with '
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
                                              'explanation': 'A solitary oral ulcer lasting longer than two weeks—especially in a smoker or heavy drinker—must be regarded as squamous cell carcinoma until histologically excluded. Malignant ulcers do not heal with symptomatic rinses alone. Prompt biopsy and specialist referral avoid diagnostic delay.'},
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
                                              'explanation': 'MRONJ presents as exposed necrotic jawbone persisting in a patient treated with antiresorptive or antiangiogenic medications, without radiotherapy to the jaws. Impaired osteoclast function and mucosal healing allow infection and necrosis after trauma or spontaneously. Stage-based care ranges from antimicrobial rinses to surgical debridement in refractory disease.'},
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
                                              'explanation': 'High-risk HPV (notably HPV-16) drives a rising subset of oropharyngeal squamous carcinomas of the tonsillar crypts and base of tongue, often in patients without traditional heavy tobacco exposure. Viral oncogenes disrupt cell-cycle control in epithelia of these sites. Clinical awareness prompts appropriate referral for persistent unilateral throat or neck findings.'}]},
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
                 'questions': {'easy': [{'question': 'G.V. Black Class II is?',
                                         'options': ['A) Proximal surfaces of posteriors',
                                                     'B) Only pits of anteriors',
                                                     'C) Only cervical thirds always Class V',
                                                     'D) Only cusp tip'],
                                         'answer': 'A) Proximal surfaces of posteriors',
                                         'explanation': 'G.V. Black Class II cavities involve the proximal surfaces of posterior teeth, typically initiating just below the contact point where biofilm stagnates. The classification organizes cavity location for preparation design and matrix use. It does not by itself prescribe modern adhesive materials.'},
                                        {'question': 'Composite bonding relies on?',
                                         'options': ['A) Micromechanical adhesion after '
                                                     'etch/adhesive protocols',
                                                     'B) Only zinc phosphate always',
                                                     'C) Only screws',
                                                     'D) Only sutures'],
                                         'answer': 'A) Micromechanical adhesion after '
                                                   'etch/adhesive protocols',
                                         'explanation': 'Etching enamel (and appropriately conditioning dentin) creates microporosity that adhesive resins infiltrate to form resin tags and a hybrid layer. Retention of composite is therefore primarily micromechanical rather than chemical bonding to bulk tooth mineral alone. Moisture control is critical because contamination prevents resin infiltration.'},
                                        {'question': 'Caries detector dyes help?',
                                         'options': ['A) Visualize infected dentin cautiously',
                                                     'B) Replace radiographs always',
                                                     'C) Diagnose pulp vitality',
                                                     'D) Whiten teeth'],
                                         'answer': 'A) Visualize infected dentin cautiously',
                                         'explanation': 'Caries detector dyes bind preferentially to denatured collagen in infected dentin, helping visualize tissue that may harbor high bacterial load. They can also stain caries-affected or sound dentin nonspecifically, so dye uptake alone should not dictate aggressive excavation. Clinical hardness and knowledge of pulp proximity guide final removal.'}],
                               'medium': [{'question': 'Liners/bases under deep restorations aim '
                                                       'to?',
                                           'options': ['A) Protect pulp / thermal insulation / '
                                                       'seal',
                                                       'B) Only change shade',
                                                       'C) Only etch enamel more',
                                                       'D) Only replace rubber dam'],
                                           'answer': 'A) Protect pulp / thermal insulation / seal',
                                           'explanation': 'Liners and bases under deep restorations provide thermal insulation, chemical protection, and sometimes a sealing or bioactive interface over remaining dentin near the pulp. Material choice depends on remaining dentin thickness and whether a sedative, bioactive, or purely insulating layer is needed. They do not replace adequate caries removal and definitive sealing.'},
                                          {'question': 'Amalgam advantage includes?',
                                           'options': ['A) Wear resistance / less technique '
                                                       'sensitivity to moisture than composite',
                                                       'B) Always superior esthetics',
                                                       'C) Bonds micromechanically identical to '
                                                       'etch-and-rinse composite',
                                                       'D) Never corrodes'],
                                           'answer': 'A) Wear resistance / less technique '
                                                     'sensitivity to moisture than composite',
                                           'explanation': 'Dental amalgam’s metallic microstructure confers high compressive strength and wear resistance under posterior occlusal load. Unlike resin composites, amalgam does not rely on adhesive bonding that fails with moisture contamination during placement. Technique and cavity design still matter, but moisture tolerance is comparatively greater.'},
                                          {'question': 'Secondary caries often at?',
                                           'options': ['A) Margins of restorations',
                                                       'B) Only pulp horn center always',
                                                       'C) Only apex',
                                                       'D) Only cementum only far from margins'],
                                           'answer': 'A) Margins of restorations',
                                           'explanation': 'Secondary (recurrent) caries develops at restoration margins where microleakage or plaque stagnation allows demineralization of adjacent enamel and dentin. Open margins, overhangs, and poor oral hygiene are common contributors. Detecting and resealing or replacing defective margins interrupts this pathway.'}],
                               'hard': [{'question': 'A junior colleague asks for the single best '
                                                     'answer. C-factor high in? Beware of '
                                                     'near-miss distractors.',
                                         'options': ['A) Class I deep boxy preparations',
                                                     'B) Only free cusp rebuild always low',
                                                     'C) Only veneers on one surface always lowest '
                                                     'issue',
                                                     'D) Only sealants'],
                                         'answer': 'A) Class I deep boxy preparations',
                                         'explanation': 'The C-factor is the ratio of bonded to unbonded surfaces in a cavity; Class I boxy preparations have many bonded walls and few free surfaces for stress relief. As composite polymerizes and shrinks, high C-factor configurations concentrate polymerization stress at the bonded interface. Incremental placement and low-shrinkage techniques reduce gap formation risk.'},
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
                                         'explanation': 'In deep carious lesions, selective (partial) caries removal leaves soft, caries-affected dentin over the pulp to avoid exposure while excavating peripheral infected dentin to a hard, sealable margin. A well-sealed restoration deprives remaining bacteria of substrate, arresting the lesion. Stepwise excavation follows the same biological principle with a staged approach.'},
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
                                         'explanation': 'Abfraction proposes that occlusal stress concentrates tensile strain at the cervical region, disrupting enamel and dentin and contributing to non-carious cervical lesions. Many lesions are multifactorial, also involving abrasion and erosion. The theory remains debated, so management addresses occlusal factors and tooth-surface loss together.'}],
                               'extreme': [{'question': 'In a high-stakes clinic scenario with '
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
                                            'explanation': 'Minimally invasive dentistry aims to prevent disease, detect lesions early, and restore only what is irreversibly lost while preserving sound tooth structure. Risk-based recall, fluoride, and sealants support this philosophy alongside conservative cavity designs. Maximal tissue preservation improves long-term tooth strength.'},
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
                                            'explanation': 'Biomimetic restorative dentistry seeks to replace enamel and dentin with materials and adhesive techniques that approximate the stiffness, bonding, and stress distribution of natural tooth tissues. By bonding and covering cusps when indicated, the restored tooth behaves more like an intact tooth under load. Adhesive protocols and progressive build-ups are central to the approach.'},
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
                                            'explanation': 'Rampant caries reflects high caries activity; placing definitive complex restorations before disease control invites rapid failure at new margins. Urgent pain and infection are managed first, then biofilm and dietary drivers are controlled with temporaries and preventive care. Definitive rehabilitation proceeds once activity stabilizes.'}]},
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
                    'questions': {'easy': [{'question': 'Bitewing radiographs best show?',
                                            'options': ['A) Interproximal caries and crestal bone',
                                                        'B) Only TMJ disk',
                                                        'C) Only sinus polyps always',
                                                        'D) Only soft tissue cancer staging'],
                                            'answer': 'A) Interproximal caries and crestal bone',
                                            'explanation': 'Bitewing radiographs project the crowns of opposing maxillary and mandibular teeth and the crestal alveolar bone with minimal overlap when angulation is correct. They are the most sensitive routine view for detecting early interproximal caries and early horizontal bone loss. Periapicals alone often miss early proximal lesions because of geometric overlap.'},
                                           {'question': 'ALARA means?',
                                            'options': ['A) As Low As Reasonably Achievable '
                                                        'radiation',
                                                        'B) Always Lowest And Rarely Any '
                                                        'radiograph never',
                                                        'C) Only analog films',
                                                        'D) Only CBCT for all exams'],
                                            'answer': 'A) As Low As Reasonably Achievable '
                                                      'radiation',
                                            'explanation': 'ALARA (As Low As Reasonably Achievable) is the radiation-protection principle that every exposure must be justified by diagnostic benefit and then optimized to the lowest dose that still yields adequate image quality. Collimation, sensors, and selection criteria operationalize ALARA in dentistry. Unnecessary retakes violate the principle.'},
                                           {'question': 'Periapical radiograph shows?',
                                            'options': ['A) Full tooth and periapical bone',
                                                        'B) Only bite relationship of all molars '
                                                        'both sides always',
                                                        'C) Only cephalometric landmarks',
                                                        'D) Only chest'],
                                            'answer': 'A) Full tooth and periapical bone',
                                            'explanation': 'A periapical radiograph images the entire tooth from crown to apex plus the surrounding periapical bone. It is used to assess apical periodontitis, root morphology, and periodontal bone along the root. Bitewings do not reliably show the periapical region.'}],
                                  'medium': [{'question': 'Panoramic radiograph advantage?',
                                              'options': ['A) Broad overview of jaws/TMJ/teeth',
                                                          'B) Highest resolution for early enamel '
                                                          'caries always better than bitewing',
                                                          'C) Zero distortion ever',
                                                          'D) Replaces all PAs always'],
                                              'answer': 'A) Broad overview of jaws/TMJ/teeth',
                                              'explanation': 'A panoramic radiograph captures both jaws, dentition, TMJs, and contiguous structures in a single tomographic image. It is useful for screening, orthodontic assessment, and surgical planning when a broad anatomic overview is needed. Fine detail of early caries is inferior to intraoral radiographs.'},
                                             {'question': 'Radiolucent lesion at apex of nonvital '
                                                          'tooth likely?',
                                              'options': ['A) Periapical rarefying osteitis / '
                                                          'granuloma/cyst spectrum',
                                                          'B) Always osteosarcoma',
                                                          'C) Always torus',
                                                          'D) Always enamel pearl'],
                                              'answer': 'A) Periapical rarefying osteitis / '
                                                        'granuloma/cyst spectrum',
                                              'explanation': 'Bacterial toxins from a necrotic pulp trigger inflammatory resorption of periapical bone, producing a radiolucency (rarefying osteitis) that may represent granuloma, cyst, or abscess histologically. Radiographic appearance alone cannot distinguish these entities. Pulp vitality testing links the lesion to an endodontic source.'},
                                             {'question': 'Lead apron/thyroid shield use follows?',
                                              'options': ['A) Current guidelines; justification '
                                                          'first',
                                                          'B) Never used historically considered',
                                                          'C) Only for CBCT never for bitewings '
                                                          'ever universally',
                                                          'D) Only for staff not patients'],
                                              'answer': 'A) Current guidelines; justification '
                                                        'first',
                                              'explanation': 'Lead aprons and thyroid shields reduce exposure of radiosensitive tissues when they do not obscure anatomy, but justification of the radiograph and optimized technique remain primary. Contemporary guidelines emphasize thyroid protection especially in children and selection criteria over routine shielding rituals alone. Local protocols should follow current evidence-based recommendations.'}],
                                  'hard': [{'question': 'A junior colleague asks for the single '
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
                                            'explanation': 'Cone-beam CT provides three-dimensional detail of teeth, bone, and anatomic relationships when two-dimensional images cannot answer the clinical question—for example complex implant sites, impacted teeth near nerves, or atypical endodontic anatomy. Effective dose is generally higher than panoramic or intraoral imaging. Indication must therefore be specific and justified.'},
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
                                            'explanation': 'On panoramic imaging, dense objects on one side of the jaw can cast a blurred, magnified “ghost” image on the contralateral side, projected higher and more posteriorly because of the rotational geometry. Recognizing ghosts prevents misdiagnosis of pathology. Common sources include earrings, the contralateral mandible angle, and the cervical spine.'},
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
                                            'explanation': 'The SLOB rule (Same Lingual, Opposite Buccal) uses a horizontal tube shift between two periapical radiographs to localize an object buccolingually. If the object moves in the same direction as the tube head, it lies lingual; if opposite, it lies buccal. This parallax principle guides endodontic and surgical orientation.'}],
                                  'extreme': [{'question': 'In a high-stakes clinic scenario with '
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
                                               'explanation': 'Malignant jaw lesions often destroy bone with ill-defined, non-corticated borders and cortical perforation because neoplastic growth outpaces host bone remodeling. Rapid radiographic change and tooth mobility without periodontal explanation heighten suspicion. Such features warrant urgent specialist referral and biopsy rather than observation.'},
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
                                               'explanation': 'Effective dose generally increases from well-collimated intraoral radiographs to panoramic imaging to CBCT examinations of larger fields of view, though exact values depend on exposure parameters. Selecting the lowest-dose modality that answers the diagnostic question embodies ALARA. CBCT is not a routine substitute for bitewings or periapicals.'},
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
                                               'explanation': 'Idiopathic osteosclerosis is a focal radiopacity in bone associated with a vital tooth and no inflammatory cause. Condensing osteitis is a reactive bony sclerosis at the apex of a tooth with pulpitis or necrosis. Pulp testing and clinical history distinguish the two and determine whether endodontic treatment is needed.'}]},
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
                    'questions': {'easy': [{'question': 'How many permanent teeth normally?',
                                            'options': ['A) 32',
                                                        'B) 20',
                                                        'C) 28 always excluding wisdom never vary',
                                                        'D) 16'],
                                            'answer': 'A) 32',
                                            'explanation': 'The permanent dentition normally comprises 8 incisors, 4 canines, 8 premolars, and 12 molars, totaling 32 teeth including third molars. Congenitally missing third molars reduce the clinical count but do not change the anatomic norm. Primary teeth are fewer and lack premolars.'},
                                           {'question': 'Primary dentition count?',
                                            'options': ['A) 20', 'B) 32', 'C) 12', 'D) 36'],
                                            'answer': 'A) 20',
                                            'explanation': 'The primary dentition consists of 8 incisors, 4 canines, and 8 molars—20 teeth total—with no premolars. Premolars succeed the primary molars in the mixed and permanent dentitions. Knowing the count prevents misidentification during pediatric examination and space analysis.'},
                                           {'question': 'Cusp of Carabelli is on?',
                                            'options': ['A) Maxillary first molar',
                                                        'B) Mandibular central',
                                                        'C) Maxillary lateral only',
                                                        'D) Mandibular canine'],
                                            'answer': 'A) Maxillary first molar',
                                            'explanation': 'The cusp of Carabelli is an accessory cusp or tubercle on the mesiolingual surface of the maxillary first permanent molar (and sometimes the primary second molar). It is a common morphologic variation of phylogenetic interest. Its presence can affect sealant coverage and band adaptation.'}],
                                  'medium': [{'question': 'Maxillary first premolar often has?',
                                              'options': ['A) Two roots / two canals commonly',
                                                          'B) Always one canal only',
                                                          'C) Always three roots like upper molar',
                                                          'D) No cusps'],
                                              'answer': 'A) Two roots / two canals commonly',
                                              'explanation': 'The maxillary first premolar most often has two roots—one buccal and one palatal—and correspondingly two root canals. This bifurcation has direct endodontic and extraction significance because both canals must be located and instrumented. A minority of teeth present a single root with one or two canals.'},
                                             {'question': 'Contact point of anteriors is usually?',
                                              'options': ['A) Incisal third to middle third '
                                                          'junction themes',
                                                          'B) Always at cervix only',
                                                          'C) Always at root apex',
                                                          'D) No contacts normal'],
                                              'answer': 'A) Incisal third to middle third junction '
                                                        'themes',
                                              'explanation': 'Proximal contact areas of anterior teeth are typically located in the incisal third, near the junction with the middle third, creating a contact that stabilizes the arch and protects the interdental papilla from food impaction. Contacts placed too far gingivally or openly invite black triangles and periodontal irritation. Proper contact morphology is therefore both esthetic and biologic.'},
                                             {'question': 'Curve of Spee is?',
                                              'options': ['A) Anteroposterior occlusal curvature',
                                                          'B) Only mediolateral Wilson',
                                                          'C) Only Bonwill triangle only',
                                                          'D) Only freeway space'],
                                              'answer': 'A) Anteroposterior occlusal curvature',
                                              'explanation': 'The curve of Spee is the anteroposterior occlusal curvature seen in the sagittal plane, concave superiorly in the mandibular arch from canine through posterior teeth. It contributes to balanced occlusal contacts during function. Flattening or exaggeration of the curve is relevant in orthodontic and occlusal analysis.'}],
                                  'hard': [{'question': 'A junior colleague asks for the single '
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
                                            'explanation': 'Mandibular first molars most commonly have two roots with three principal canals: mesiobuccal, mesiolingual, and a distal canal (which may split into two). Anatomic variations include a middle mesial canal and two distal canals. Endodontic access and negotiation must anticipate these patterns to clean the entire system.'},
                                           {'question': 'A junior colleague asks for the single '
                                                        'best answer. Enamel is thickest at? '
                                                        'Beware of near-miss distractors.',
                                            'options': ['A) Occlusal/incisal contact areas themes',
                                                        'B) CEJ always thickest',
                                                        'C) Apex',
                                                        'D) Furcation'],
                                            'answer': 'A) Occlusal/incisal contact areas themes',
                                            'explanation': 'Enamel reaches its greatest thickness over cusp tips and incisal edges—the functional contact areas that sustain heavy occlusal load—while thinning toward the cervix. This distribution resists wear where forces concentrate. Enamel is the hardest tissue in the body because of its high mineral content.'},
                                           {'question': 'A junior colleague asks for the single '
                                                        'best answer. Pulp horn height relates to? '
                                                        'Beware of near-miss distractors.',
                                            'options': ['A) Risk of exposure in prep of young '
                                                        'teeth',
                                                        'B) Only shade',
                                                        'C) Only root length always equal',
                                                        'D) Only calculus'],
                                            'answer': 'A) Risk of exposure in prep of young teeth',
                                            'explanation': 'Pulp horns extend occlusally under cusps and are relatively high in young teeth before secondary dentin accumulates. Cavity or crown preparation that ignores horn height risks mechanical pulp exposure. Conservative occlusal reduction and knowledge of age-related pulp anatomy reduce that risk.'}],
                                  'extreme': [{'question': 'In a high-stakes clinic scenario with '
                                                           'incomplete data, which statement is '
                                                           'MOST correct? Dens invaginatus risk? '
                                                           'Avoid therapies that could harm if a '
                                                           'critical differential remains open.',
                                               'options': ['A) Pulp infection via invagination',
                                                           'B) Only better enamel',
                                                           'C) Only freckles',
                                                           'D) Only torus'],
                                               'answer': 'A) Pulp infection via invagination',
                                               'explanation': 'Dens invaginatus is an infolding of the enamel organ into the dental papilla, creating a deep palatal pit continuous with a blind or open channel toward the pulp. Oral bacteria can rapidly infect the pulp through this defect even in an apparently immature or minimally decayed tooth. Early fissure sealing or endodontic intervention addresses that pathway.'},
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
                                               'explanation': 'Taurodontism features an enlarged pulp chamber with apical displacement of the root furcation, producing short roots relative to crown–body height. The altered chamber morphology complicates canal location, instrumentation, and obturation. Recognition on radiographs prepares the clinician for endodontic difficulty.'},
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
                                               'explanation': 'Dilaceration is a sharp bend in the root or crown, usually from trauma to the developing tooth germ. The angulation impedes straight-line endodontic access and increases risk of root fracture or incomplete removal during extraction. Preoperative radiographs map the curvature so force direction can be planned.'}]},
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
        "🩺 *CharaNas Dentistry Bot*\n"
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
