"""Undergraduate dentistry study content by specialty and difficulty."""
from __future__ import annotations

import random

from quiz_bank import DIFFICULTIES, DIFFICULTY_LABELS, LABEL_TO_DIFFICULTY

SPECIALTY_ORDER = ['oral_surgery', 'orthodontics', 'periodontics', 'endodontics', 'prosthodontics', 'pediatric_dentistry', 'oral_medicine', 'restorative', 'oral_radiology', 'dental_anatomy']

SPECIALTIES: dict[str, dict] = {
 'oral_surgery': {
  'label': 'Oral Surgery',
  'books': [
   "Peterson's Principles of Oral and Maxillofacial Surgery",
   'Contemporary Oral and Maxillofacial Surgery — Hupp',
   'Local Anaesthesia in Dentistry'
  ],
  'pdf_notes': [
   'IANB targets mandibular foramen region; know failure causes.',
   'Dry socket: pain day 2-4, empty socket — irrigate + dressing.',
   'Ludwig angina: airway first, urgent drainage/antibiotics.',
   'Assess bleeding risk (anticoagulants) before surgery.',
   'Impacted third molars: IAN/lingual nerve risk counseling.'
  ],
  'questions': {
   'easy': [
    {
     'question': 'Most common impacted tooth?',
     'options': [
      'A) Maxillary canine',
      'B) Mandibular third molar',
      'C) Maxillary lateral incisor',
      'D) Mandibular first premolar'
     ],
     'answer': 'B) Mandibular third molar',
     'explanation': 'Mandibular third molars are the teeth most frequently impacted because they erupt last and often lack adequate space in the dental arch. Impaction occurs when eruption is blocked by bone, soft tissue, or an adjacent tooth. Maxillary canines are the next most commonly impacted teeth, but far less often than lower wisdom teeth.',
     'choice_explanations': {
      'A': 'The maxillary canine is a long-erupting anterior tooth and the second most commonly impacted tooth. Mandibular third molars are the teeth most frequently impacted because they erupt last and often lack adequate space in the dental arch.',
      'B': 'Mandibular third molars are the teeth most frequently impacted because they erupt last and often lack adequate space in the dental arch. Impaction occurs when eruption is blocked by bone, soft tissue, or an adjacent tooth.',
      'C': 'The maxillary lateral incisor is a single-rooted anterior tooth; true bony impaction is uncommon versus agenesis. Mandibular third molars are the teeth most frequently impacted because they erupt last and often lack adequate space in the dental arch.',
      'D': 'The mandibular first premolar is a bicuspid that usually erupts with space and is rarely fully impacted. Mandibular third molars are the teeth most frequently impacted because they erupt last and often lack adequate space in the dental arch.'
     }
    },
    {
     'question': 'Local anesthetic for an inferior alveolar nerve block typically targets which anatomic region?',
     'options': [
      'A) Mental foramen on the buccal mandible',
      'B) Infraorbital foramen on the maxilla',
      'C) Mandibular foramen on the medial ramus',
      'D) Greater palatine foramen on the hard palate'
     ],
     'answer': 'C) Mandibular foramen on the medial ramus',
     'explanation': 'The inferior alveolar nerve enters the mandible at the mandibular foramen on the medial ramus. An inferior alveolar nerve block deposits anesthetic near this foramen so the solution bathes the nerve before it enters the mandibular canal. Successful anesthesia therefore depends on accurate needle placement relative to the lingula and mandibular foramen.',
     'choice_explanations': {
      'A': 'The mental foramen transmits the mental nerve onto the buccal mandibular premolar region. The inferior alveolar nerve enters the mandible at the mandibular foramen on the medial ramus.',
      'B': 'The infraorbital foramen on the maxilla transmits the infraorbital nerve to midface soft tissues. The inferior alveolar nerve enters the mandible at the mandibular foramen on the medial ramus.',
      'C': 'The inferior alveolar nerve enters the mandible at the mandibular foramen on the medial ramus. An inferior alveolar nerve block deposits anesthetic near this foramen so the solution bathes the nerve before it enters the mandibular canal.',
      'D': 'The greater palatine foramen transmits the greater palatine nerve to posterior hard-palate mucosa. The inferior alveolar nerve enters the mandible at the mandibular foramen on the medial ramus.'
     }
    },
    {
     'question': 'Alveolar osteitis (dry socket) most commonly follows which clinical situation?',
     'options': [
      'A) Difficult mandibular molar extraction with clot loss',
      'B) Routine fluoride varnish application',
      'C) Supragingival scaling without extraction',
      'D) Orthodontic bracket bonding alone'
     ],
     'answer': 'A) Difficult mandibular molar extraction with clot loss',
     'explanation': 'Alveolar osteitis (dry socket) follows premature loss or lysis of the blood clot that normally protects the extraction socket. Exposed bone and inflammatory mediators produce severe pain, typically beginning two to four days after a difficult mandibular molar extraction. Risk rises with traumatic extraction, smoking, and poor clot stability.',
     'choice_explanations': {
      'A': 'Alveolar osteitis (dry socket) follows premature loss or lysis of the blood clot that normally protects the extraction socket. Exposed bone and inflammatory mediators produce severe pain, typically beginning two to four days after a difficult mandibular molar extraction.',
      'B': 'Fluoride varnish deposits high-concentration fluoride on enamel to favor remineralization. Alveolar osteitis (dry socket) follows premature loss or lysis of the blood clot that normally protects the extraction socket.',
      'C': 'Supragingival scaling mechanically removes coronal calculus/biofilm without creating a socket. Alveolar osteitis (dry socket) follows premature loss or lysis of the blood clot that normally protects the extraction socket.',
      'D': 'Orthodontic bonding adhesively fixes brackets to enamel without opening alveolar bone. Alveolar osteitis (dry socket) follows premature loss or lysis of the blood clot that normally protects the extraction socket.'
     }
    }
   ],
   'medium': [
    {
     'question': 'Ludwig angina is best described as infection involving which spaces?',
     'options': [
      'A) Temporomandibular joint capsule alone',
      'B) Unilateral maxillary sinus alone',
      'C) Pulp chamber and root canals only',
      'D) Bilateral submandibular, sublingual, and submental spaces'
     ],
     'answer': 'D) Bilateral submandibular, sublingual, and submental spaces',
     'explanation': 'Ludwig angina is a rapidly spreading bilateral cellulitis of the submandibular, sublingual, and submental spaces, usually from an odontogenic source. Edema elevates the floor of the mouth and tongue, threatening the airway. Urgent airway management, intravenous antibiotics, and surgical drainage are required.',
     'choice_explanations': {
      'A': 'The TMJ capsule is the synovial envelope of the condyle–temporal joint, not floor-of-mouth spaces. Ludwig angina is a rapidly spreading bilateral cellulitis of the submandibular, sublingual, and submental spaces, usually from an odontogenic source.',
      'B': 'Isolated maxillary sinus disease is confined to one antrum and is not bilateral floor-of-mouth cellulitis. Ludwig angina is a rapidly spreading bilateral cellulitis of the submandibular, sublingual, and submental spaces, usually from an odontogenic source.',
      'C': 'The pulp chamber and canals contain dental pulp within tooth structure, not cervical fascial spaces. Ludwig angina is a rapidly spreading bilateral cellulitis of the submandibular, sublingual, and submental spaces, usually from an odontogenic source.',
      'D': 'Ludwig angina is a rapidly spreading bilateral cellulitis of the submandibular, sublingual, and submental spaces, usually from an odontogenic source. Edema elevates the floor of the mouth and tongue, threatening the airway.'
     }
    },
    {
     'question': 'Which laboratory measure is most relevant before oral surgery in a patient taking warfarin?',
     'options': [
      'A) HbA1c only',
      'B) INR (international normalized ratio)',
      'C) Serum amylase only',
      'D) Fasting lipid panel only'
     ],
     'answer': 'B) INR (international normalized ratio)',
     'explanation': 'Warfarin inhibits vitamin K–dependent clotting factors and is monitored with the international normalized ratio (INR). Before invasive oral surgery, the INR helps estimate bleeding risk so hemostasis planning and any physician-coordinated dose adjustment can be made appropriately.',
     'choice_explanations': {
      'A': 'HbA1c averages glycemia over ~3 months and does not quantify warfarin anticoagulation. Warfarin inhibits vitamin K–dependent clotting factors and is monitored with the international normalized ratio (INR).',
      'B': 'Warfarin inhibits vitamin K–dependent clotting factors and is monitored with the international normalized ratio (INR). Before invasive oral surgery, the INR helps estimate bleeding risk so hemostasis planning and any physician-coordinated dose adjustment can be made appropriately.',
      'C': 'Serum amylase is a pancreatic/salivary enzyme marker, mainly for pancreatitis assessment. Warfarin inhibits vitamin K–dependent clotting factors and is monitored with the international normalized ratio (INR).',
      'D': 'A fasting lipid panel quantifies cholesterol/triglycerides for cardiovascular risk, not bleeding risk. Warfarin inhibits vitamin K–dependent clotting factors and is monitored with the international normalized ratio (INR).'
     }
    },
    {
     'question': 'Oroantral communication risk is highest when extracting which teeth?',
     'options': [
      'A) Mandibular incisors',
      'B) Mandibular canines',
      'C) Mandibular premolars',
      'D) Maxillary molars'
     ],
     'answer': 'D) Maxillary molars',
     'explanation': 'Maxillary molar roots often lie close to, or project into, the maxillary sinus floor. Extraction can tear the thin antral bone or sinus membrane and create an oroantral communication. Mandibular teeth do not communicate with the maxillary sinus.',
     'choice_explanations': {
      'A': 'Mandibular incisor apices lie in anterior mandibular bone remote from the maxillary sinus. Maxillary molar roots often lie close to, or project into, the maxillary sinus floor.',
      'B': 'Mandibular canine roots occupy the anterior mandible and do not abut the maxillary antrum. Maxillary molar roots often lie close to, or project into, the maxillary sinus floor.',
      'C': 'Mandibular premolars sit in the posterior mandible, distant from the maxillary sinus floor. Maxillary molar roots often lie close to, or project into, the maxillary sinus floor.',
      'D': 'Maxillary molar roots often lie close to, or project into, the maxillary sinus floor. Extraction can tear the thin antral bone or sinus membrane and create an oroantral communication.'
     }
    }
   ],
   'hard': [
    {
     'question': 'Which nerve is at notable injury risk during mandibular third molar surgery near the canal?',
     'options': [
      'A) Lingual nerve far from the lingual plate',
      'B) Facial nerve within the parotid gland',
      'C) Inferior alveolar nerve',
      'D) Hypoglossal nerve in the posterior triangle'
     ],
     'answer': 'C) Inferior alveolar nerve',
     'explanation': 'The inferior alveolar nerve runs in the mandibular canal and may lie immediately adjacent to mandibular third molar roots. Surgical elevation or sectioning of the tooth can stretch, crush, or transect the nerve, causing altered lip and chin sensation. Preoperative imaging and informed consent address this risk.',
     'choice_explanations': {
      'A': 'The lingual nerve carries tongue sensation/taste and runs near the lingual plate in the third-molar area. The inferior alveolar nerve runs in the mandibular canal and may lie immediately adjacent to mandibular third molar roots.',
      'B': 'The facial nerve (CN VII) traverses the parotid gland to motorize muscles of facial expression. The inferior alveolar nerve runs in the mandibular canal and may lie immediately adjacent to mandibular third molar roots.',
      'C': 'The inferior alveolar nerve runs in the mandibular canal and may lie immediately adjacent to mandibular third molar roots. Surgical elevation or sectioning of the tooth can stretch, crush, or transect the nerve, causing altered lip and chin sensation.',
      'D': 'The hypoglossal nerve (CN XII) motorizes tongue muscles in the neck, remote from the mandibular canal. The inferior alveolar nerve runs in the mandibular canal and may lie immediately adjacent to mandibular third molar roots.'
     }
    },
    {
     'question': 'Medication-related osteonecrosis of the jaw risk rises most with which scenario?',
     'options': [
      'A) Placement of removable orthodontic retainers',
      'B) Topical fluoride varnish alone',
      'C) Routine dental prophylaxis without mucosal trauma',
      'D) Invasive dental surgery in patients on antiresorptive therapy'
     ],
     'answer': 'D) Invasive dental surgery in patients on antiresorptive therapy',
     'explanation': 'Medication-related osteonecrosis of the jaw (MRONJ) is exposed necrotic bone associated with antiresorptive or antiangiogenic drugs. Invasive procedures such as extractions disrupt oral mucosa and bone healing in susceptible patients, elevating MRONJ risk compared with noninvasive care.',
     'choice_explanations': {
      'A': 'Removable retainers stabilize tooth position without surgically disrupting jaw mucosa or bone. Medication-related osteonecrosis of the jaw (MRONJ) is exposed necrotic bone associated with antiresorptive or antiangiogenic drugs.',
      'B': 'Fluoride varnish deposits high-concentration fluoride on enamel to favor remineralization. Medication-related osteonecrosis of the jaw (MRONJ) is exposed necrotic bone associated with antiresorptive or antiangiogenic drugs.',
      'C': 'Atraumatic prophylaxis does not create the mucosal/osseous wound that precipitates MRONJ. Medication-related osteonecrosis of the jaw (MRONJ) is exposed necrotic bone associated with antiresorptive or antiangiogenic drugs.',
      'D': 'Medication-related osteonecrosis of the jaw (MRONJ) is exposed necrotic bone associated with antiresorptive or antiangiogenic drugs. Invasive procedures such as extractions disrupt oral mucosa and bone healing in susceptible patients, elevating MRONJ risk compared with noninvasive care.'
     }
    },
    {
     'question': 'A root tip displaced into the maxillary sinus during extraction most appropriately requires?',
     'options': [
      'A) Immediate root canal treatment of the adjacent vital tooth only',
      'B) Retrieval strategy with sinus precautions and possible referral',
      'C) Observation indefinitely without imaging or follow-up',
      'D) Chlorhexidine rinse alone as definitive management'
     ],
     'answer': 'B) Retrieval strategy with sinus precautions and possible referral',
     'explanation': 'A root tip displaced into the maxillary sinus can act as a foreign body, promoting sinusitis or sustaining an oroantral fistula. Management requires retrieval when indicated, closure of any communication, sinus precautions, and specialist referral if needed.',
     'choice_explanations': {
      'A': 'RCT disinfects and obturates pulp space; it cannot retrieve a foreign body from the sinus. A root tip displaced into the maxillary sinus can act as a foreign body, promoting sinusitis or sustaining an oroantral fistula.',
      'B': 'A root tip displaced into the maxillary sinus can act as a foreign body, promoting sinusitis or sustaining an oroantral fistula. Management requires retrieval when indicated, closure of any communication, sinus precautions, and specialist referral if needed.',
      'C': 'Indefinite observation without imaging ignores foreign-body sinusitis and oroantral fistula risk. A root tip displaced into the maxillary sinus can act as a foreign body, promoting sinusitis or sustaining an oroantral fistula.',
      'D': 'Chlorhexidine is an antimicrobial rinse and does not remove a root tip from the antrum. A root tip displaced into the maxillary sinus can act as a foreign body, promoting sinusitis or sustaining an oroantral fistula.'
     }
    }
   ],
   'extreme': [
    {
     'question': 'An anticoagulated patient needs urgent extraction with elevated bleeding risk. Best management concept?',
     'options': [
      'A) Stop all anticoagulants unilaterally the morning of surgery',
      'B) Refuse extraction under every circumstance',
      'C) Give vitamin K routinely without assessing the indication',
      'D) Coordinate physician guidance; use local hemostasis; avoid blind anticoagulant cessation'
     ],
     'answer': 'D) Coordinate physician guidance; use local hemostasis; avoid blind anticoagulant cessation',
     'explanation': 'Therapeutic anticoagulation reduces thromboembolic risk; abrupt cessation can precipitate stroke or venous thrombosis. For most dental extractions, continuing anticoagulation with meticulous local hemostasis is preferred, coordinated with the prescribing physician when risk is high.',
     'choice_explanations': {
      'A': 'Abrupt anticoagulant cessation restores thrombotic risk (stroke/VTE) by removing pathway inhibition. Therapeutic anticoagulation reduces thromboembolic risk; abrupt cessation can precipitate stroke or venous thrombosis.',
      'B': 'Blanket refusal ignores that many extractions proceed safely with local hemostasis on anticoagulation. Therapeutic anticoagulation reduces thromboembolic risk; abrupt cessation can precipitate stroke or venous thrombosis.',
      'C': 'Vitamin K repletes cofactors II/VII/IX/X and reverses warfarin only when clinically indicated. Therapeutic anticoagulation reduces thromboembolic risk; abrupt cessation can precipitate stroke or venous thrombosis.',
      'D': 'Therapeutic anticoagulation reduces thromboembolic risk; abrupt cessation can precipitate stroke or venous thrombosis. For most dental extractions, continuing anticoagulation with meticulous local hemostasis is preferred, coordinated with the prescribing physician when risk is high.'
     }
    },
    {
     'question': 'Postoperative expanding neck hematoma with stridor most urgently indicates?',
     'options': [
      'A) Airway emergency management first',
      'B) Home antibiotics and routine review next week',
      'C) Overnight observation without airway assessment',
      'D) Ice packs alone without clinical evaluation'
     ],
     'answer': 'A) Airway emergency management first',
     'explanation': 'An expanding neck hematoma after surgery can compress the airway, producing stridor, dyspnea, and rapid desaturation. Airway establishment takes absolute priority over investigating the bleeding source or prescribing outpatient measures.',
     'choice_explanations': {
      'A': 'An expanding neck hematoma after surgery can compress the airway, producing stridor, dyspnea, and rapid desaturation. Airway establishment takes absolute priority over investigating the bleeding source or prescribing outpatient measures.',
      'B': 'Outpatient antibiotics do not secure an airway threatened by expanding hematoma. An expanding neck hematoma after surgery can compress the airway, producing stridor, dyspnea, and rapid desaturation.',
      'C': 'Observation without airway assessment leaves progressive airway compression untreated. An expanding neck hematoma after surgery can compress the airway, producing stridor, dyspnea, and rapid desaturation.',
      'D': 'Ice packs do not relieve mechanical airway obstruction from expanding hematoma. An expanding neck hematoma after surgery can compress the airway, producing stridor, dyspnea, and rapid desaturation.'
     }
    },
    {
     'question': 'Osteoradionecrosis risk is most strongly linked to which situation?',
     'options': [
      'A) Natural exfoliation of primary teeth',
      'B) Placement of pit-and-fissure sealants',
      'C) Extractions in previously irradiated jaws',
      'D) Use of at-home whitening trays'
     ],
     'answer': 'C) Extractions in previously irradiated jaws',
     'explanation': 'High-dose radiotherapy damages bone vasculature and cellularity in the jaws, impairing healing after trauma. Extractions in irradiated bone therefore carry a recognized risk of osteoradionecrosis. Preventive dental care before radiotherapy reduces later extraction need.',
     'choice_explanations': {
      'A': 'Physiologic primary exfoliation is not radiotherapy-related osteoradionecrosis risk. High-dose radiotherapy damages bone vasculature and cellularity in the jaws, impairing healing after trauma.',
      'B': 'Sealants are preventive resin coatings of pits/fissures without irradiated-bone trauma. High-dose radiotherapy damages bone vasculature and cellularity in the jaws, impairing healing after trauma.',
      'C': 'High-dose radiotherapy damages bone vasculature and cellularity in the jaws, impairing healing after trauma. Extractions in irradiated bone therefore carry a recognized risk of osteoradionecrosis.',
      'D': 'Whitening trays deliver peroxide to enamel and do not create ORN-level osseous injury. High-dose radiotherapy damages bone vasculature and cellularity in the jaws, impairing healing after trauma.'
     }
    }
   ]
  },
  'cases': {
   'easy': [
    {
     'title': 'Pain Day 3 After Extraction',
     'stem': 'A 24-year-old has severe pain 3 days after lower wisdom tooth removal. Socket looks empty; no pus or fever.',
     'question': 'Likely diagnosis?',
     'answer': 'Alveolar osteitis (dry socket).',
     'discussion': 'Irrigate, medicated dressing, analgesia; antibiotics usually not first-line if no infection.',
     'book_hint': "Peterson's Principles of Oral and Maxillofacial Surgery"
    }
   ],
   'medium': [
    {
     'title': 'Fever + Floor of Mouth Swelling',
     'stem': 'A patient after dental infection has bilateral floor-of-mouth swelling, drooling, and tongue elevation.',
     'question': 'Emergency concern?',
     'answer': 'Ludwig angina — secure airway and urgent surgical/medical care.',
     'discussion': 'Do not delay for routine dental clinic care.',
     'book_hint': "Peterson's Principles of Oral and Maxillofacial Surgery"
    }
   ],
   'hard': [
    {
     'title': 'Root Tip Disappears Upward',
     'stem': 'During upper 6 extraction, a root tip vanishes and the patient feels air/fluid in the nose when drinking. Choose the safest high-yield next concept before definitive results.',
     'question': 'What happened conceptually?',
     'answer': 'Oroantral communication ± displaced root — stop forcing, assess, arrange appropriate closure/retrieval.',
     'discussion': 'Sinus precautions and follow-up are essential.',
     'book_hint': "Peterson's Principles of Oral and Maxillofacial Surgery"
    }
   ],
   'extreme': [
    {
     'title': 'Irradiated Jaw Needs Extraction',
     'stem': 'A head-and-neck cancer survivor with prior radiotherapy needs a painful molar extraction in the irradiated field. Avoid harmful premature treatment while catastrophic differentials remain open.',
     'question': 'Key concept?',
     'answer': 'High ORN risk — specialist OMFS planning, atraumatic technique, infection control, and protocolized prevention.',
     'discussion': 'Never treat as a routine extraction.',
     'book_hint': "Peterson's Principles of Oral and Maxillofacial Surgery"
    }
   ]
  }
 },
 'orthodontics': {
  'label': 'Orthodontics',
  'books': [
   "Proffit's Contemporary Orthodontics",
   'Graber Orthodontics',
   'Handbook of Orthodontics — Cobourne'
  ],
  'pdf_notes': [
   'Angle Class I/II/III molar relationships.',
   'Overjet = horizontal; overbite = vertical.',
   'Space maintainers after premature primary loss.',
   'Retention is long-term; relapse is common without retainers.',
   'Uncontrolled periodontitis: do not move teeth aggressively.'
  ],
  'questions': {
   'easy': [
    {
     'question': 'Angle Class II molar relation means?',
     'options': [
      'A) Mandibular first molar distal relative to the maxillary first molar',
      'B) Mandibular first molar mesial relative to Class I',
      'C) Anterior open bite without molar discrepancy',
      'D) Bilateral posterior crossbite without anteroposterior change'
     ],
     'answer': 'A) Mandibular first molar distal relative to the maxillary first molar',
     'explanation': 'In Angle’s classification, Class II molar occlusion means the mandibular first molar is positioned distal to its normal relation with the maxillary first molar. Clinically, the mesiobuccal cusp of the upper first molar occludes mesial to the buccal groove of the lower first molar.',
     'choice_explanations': {
      'A': 'In Angle’s classification, Class II molar occlusion means the mandibular first molar is positioned distal to its normal relation with the maxillary first molar. Clinically, the mesiobuccal cusp of the upper first molar occludes mesial to the buccal groove of the lower first molar.',
      'B': 'Mesial mandibular molar position relative to Class I defines Angle Class III, not Class II. In Angle’s classification, Class II molar occlusion means the mandibular first molar is positioned distal to its normal relation with the maxillary first molar.',
      'C': 'Anterior open bite is a vertical discrepancy and does not define Class II molar occlusion. In Angle’s classification, Class II molar occlusion means the mandibular first molar is positioned distal to its normal relation with the maxillary first molar.',
      'D': 'Posterior crossbite is transverse and does not define Class II anteroposterior molar relation. In Angle’s classification, Class II molar occlusion means the mandibular first molar is positioned distal to its normal relation with the maxillary first molar.'
     }
    },
    {
     'question': 'Overjet describes which relationship?',
     'options': [
      'A) Vertical overlap of the incisors only',
      'B) Horizontal overlap of the incisors',
      'C) Torque of molar crowns only',
      'D) Arch-length discrepancy only'
     ],
     'answer': 'B) Horizontal overlap of the incisors',
     'explanation': 'Overjet is the horizontal distance between the labial surface of the mandibular incisors and the incisal edges of the maxillary incisors. Overbite, by contrast, measures vertical overlap of the incisors.',
     'choice_explanations': {
      'A': 'Vertical incisor overlap is overbite, a different dimension from horizontal overjet. Overjet is the horizontal distance between the labial surface of the mandibular incisors and the incisal edges of the maxillary incisors.',
      'B': 'Overjet is the horizontal distance between the labial surface of the mandibular incisors and the incisal edges of the maxillary incisors. Overbite, by contrast, measures vertical overlap of the incisors.',
      'C': 'Molar torque is buccolingual crown inclination, not horizontal incisor overlap. Overjet is the horizontal distance between the labial surface of the mandibular incisors and the incisal edges of the maxillary incisors.',
      'D': 'Arch-length discrepancy compares total tooth size with available arch perimeter. Overjet is the horizontal distance between the labial surface of the mandibular incisors and the incisal edges of the maxillary incisors.'
     }
    },
    {
     'question': 'A space maintainer is indicated when?',
     'options': [
      'A) Adult chronic periodontitis needs temporary splinting only',
      'B) Vital bleaching requires tray retention',
      'C) Premature loss of a primary tooth risks space loss for the successor',
      'D) Direct pulp capping is planned on a permanent molar'
     ],
     'answer': 'C) Premature loss of a primary tooth risks space loss for the successor',
     'explanation': 'Early loss of a primary tooth allows adjacent teeth to drift into the edentulous space, shortening arch length and risking impaction or crowding of the successor. A space maintainer holds the mesiodistal dimension until the permanent tooth erupts.',
     'choice_explanations': {
      'A': 'Periodontal splinting stabilizes mobile adult teeth; it does not preserve successor space. Early loss of a primary tooth allows adjacent teeth to drift into the edentulous space, shortening arch length and risking impaction or crowding of the successor.',
      'B': 'Bleaching trays hold peroxide gel and do not maintain mesiodistal arch length. Early loss of a primary tooth allows adjacent teeth to drift into the edentulous space, shortening arch length and risking impaction or crowding of the successor.',
      'C': 'Early loss of a primary tooth allows adjacent teeth to drift into the edentulous space, shortening arch length and risking impaction or crowding of the successor. A space maintainer holds the mesiodistal dimension until the permanent tooth erupts.',
      'D': 'Direct pulp capping treats pulp exposure with a biocompatible dressing; it is not space maintenance. Early loss of a primary tooth allows adjacent teeth to drift into the edentulous space, shortening arch length and risking impaction or crowding of the successor.'
     }
    }
   ],
   'medium': [
    {
     'question': 'A unilateral posterior crossbite with a functional mandibular shift most suggests?',
     'options': [
      'A) Isolated random oral habit without occlusal cause',
      'B) Fluorosis mottling as the primary etiology',
      'C) Interproximal caries alone without occlusal interference',
      'D) Premature contact or occlusal interference deflecting closure'
     ],
     'answer': 'D) Premature contact or occlusal interference deflecting closure',
     'explanation': 'A unilateral posterior crossbite with a mandibular functional shift often results from a premature occlusal contact that deflects the mandible on closure. The shift can produce asymmetric growth and must be distinguished from a true skeletal asymmetry.',
     'choice_explanations': {
      'A': 'Habits alone do not explain a unilateral crossbite with a reproducible functional mandibular shift. A unilateral posterior crossbite with a mandibular functional shift often results from a premature occlusal contact that deflects the mandible on closure.',
      'B': 'Fluorosis is enamel hypomineralization from excess fluoride intake during formation. A unilateral posterior crossbite with a mandibular functional shift often results from a premature occlusal contact that deflects the mandible on closure.',
      'C': 'Interproximal caries without premature contacts does not deflect mandibular closure. A unilateral posterior crossbite with a mandibular functional shift often results from a premature occlusal contact that deflects the mandible on closure.',
      'D': 'A unilateral posterior crossbite with a mandibular functional shift often results from a premature occlusal contact that deflects the mandible on closure. The shift can produce asymmetric growth and must be distinguished from a true skeletal asymmetry.'
     }
    },
    {
     'question': 'Anchorage in orthodontics means?',
     'options': [
      'A) Wire cross-section dimension alone',
      'B) Resistance to unwanted reciprocal tooth movement',
      'C) Bracket ceramic shade selection',
      'D) Elastomeric ligature flavor preference'
     ],
     'answer': 'B) Resistance to unwanted reciprocal tooth movement',
     'explanation': 'Anchorage is the resistance to unwanted reciprocal tooth movement that Newton’s third law would otherwise produce during orthodontic force application. Without adequate anchorage, active teeth move as intended but reactive units drift undesirably.',
     'choice_explanations': {
      'A': 'Wire cross-section determines stiffness and force delivery, not the definition of anchorage. Anchorage is the resistance to unwanted reciprocal tooth movement that Newton’s third law would otherwise produce during orthodontic force application.',
      'B': 'Anchorage is the resistance to unwanted reciprocal tooth movement that Newton’s third law would otherwise produce during orthodontic force application. Without adequate anchorage, active teeth move as intended but reactive units drift undesirably.',
      'C': 'Ceramic shade is an esthetic selection unrelated to reciprocal-force resistance. Anchorage is the resistance to unwanted reciprocal tooth movement that Newton’s third law would otherwise produce during orthodontic force application.',
      'D': 'Ligature flavor is patient preference and has no biomechanical anchorage meaning. Anchorage is the resistance to unwanted reciprocal tooth movement that Newton’s third law would otherwise produce during orthodontic force application.'
     }
    },
    {
     'question': 'Prolonged thumb sucking in the mixed dentition most commonly contributes to?',
     'options': [
      'A) Bilateral mandibular tori',
      'B) Dens invaginatus of lateral incisors',
      'C) Enamel pearl formation at furcations',
      'D) Anterior open bite and proclined maxillary incisors'
     ],
     'answer': 'D) Anterior open bite and proclined maxillary incisors',
     'explanation': 'Prolonged non-nutritive sucking generates forward and intrusive forces on the maxillary incisors and impedes normal eruption of the anteriors. The resulting dentoalveolar changes commonly include anterior open bite and proclined upper incisors.',
     'choice_explanations': {
      'A': 'Mandibular tori are benign lingual bony exostoses unrelated to digit-habit vectors. Prolonged non-nutritive sucking generates forward and intrusive forces on the maxillary incisors and impedes normal eruption of the anteriors.',
      'B': 'Dens invaginatus is an enamel-organ infolding that can channel bacteria toward the pulp. Prolonged non-nutritive sucking generates forward and intrusive forces on the maxillary incisors and impedes normal eruption of the anteriors.',
      'C': 'Enamel pearls are ectopic enamel droplets on root surfaces, often near furcations. Prolonged non-nutritive sucking generates forward and intrusive forces on the maxillary incisors and impedes normal eruption of the anteriors.',
      'D': 'Prolonged non-nutritive sucking generates forward and intrusive forces on the maxillary incisors and impedes normal eruption of the anteriors. The resulting dentoalveolar changes commonly include anterior open bite and proclined upper incisors.'
     }
    }
   ],
   'hard': [
    {
     'question': 'External apical root resorption risk during orthodontics increases most with?',
     'options': [
      'A) Alcohol-free mouthwash use',
      'B) Choice of toothpaste brand',
      'C) Daily flossing technique alone',
      'D) Heavy prolonged forces and certain root morphologies'
     ],
     'answer': 'D) Heavy prolonged forces and certain root morphologies',
     'explanation': 'Orthodontic tooth movement depends on controlled periodontal ligament stress; heavy or prolonged forces can trigger sterile inflammation and clastic activity on the root surface. External apical root resorption risk also rises with pipette-shaped roots and prior trauma.',
     'choice_explanations': {
      'A': 'Mouthwash formulation does not generate the PDL stress that drives orthodontic root resorption. Orthodontic tooth movement depends on controlled periodontal ligament stress; heavy or prolonged forces can trigger sterile inflammation and clastic activity on the root surface.',
      'B': 'Dentifrice brand does not determine sterile clastic activity on the root surface. Orthodontic tooth movement depends on controlled periodontal ligament stress; heavy or prolonged forces can trigger sterile inflammation and clastic activity on the root surface.',
      'C': 'Flossing does not create the heavy prolonged orthodontic forces linked to apical resorption. Orthodontic tooth movement depends on controlled periodontal ligament stress; heavy or prolonged forces can trigger sterile inflammation and clastic activity on the root surface.',
      'D': 'Orthodontic tooth movement depends on controlled periodontal ligament stress; heavy or prolonged forces can trigger sterile inflammation and clastic activity on the root surface. External apical root resorption risk also rises with pipette-shaped roots and prior trauma.'
     }
    },
    {
     'question': 'Serial extraction in orthodontics refers to?',
     'options': [
      'A) Extraction of all third molars as a sole protocol',
      'B) A guided sequence of primary then selected permanent extractions for severe crowding',
      'C) A series of nonsurgical root canal treatments',
      'D) Repeated full-mouth scaling appointments only'
     ],
     'answer': 'B) A guided sequence of primary then selected permanent extractions for severe crowding',
     'explanation': 'Serial extraction is a planned sequence of primary and then selected permanent tooth removals in the mixed dentition when severe crowding is inevitable. The goal is to guide eruption into a more favorable alignment and reduce later mechanotherapy complexity.',
     'choice_explanations': {
      'A': 'Third-molar removal alone is not the guided mixed-dentition sequence called serial extraction. Serial extraction is a planned sequence of primary and then selected permanent tooth removals in the mixed dentition when severe crowding is inevitable.',
      'B': 'Serial extraction is a planned sequence of primary and then selected permanent tooth removals in the mixed dentition when severe crowding is inevitable. The goal is to guide eruption into a more favorable alignment and reduce later mechanotherapy complexity.',
      'C': 'Endodontic therapy treats pulp/periapex and is not orthodontic serial extraction. Serial extraction is a planned sequence of primary and then selected permanent tooth removals in the mixed dentition when severe crowding is inevitable.',
      'D': 'Scaling removes biofilm/calculus; it is not a guided extraction protocol for crowding. Serial extraction is a planned sequence of primary and then selected permanent tooth removals in the mixed dentition when severe crowding is inevitable.'
     }
    },
    {
     'question': 'Temporary anchorage devices (TADs) primarily provide?',
     'options': [
      'A) Sustained fluoride release into enamel',
      'B) Chairside vital bleaching activation',
      'C) Skeletal anchorage independent of reciprocal tooth support',
      'D) Local anesthetic depot for soft tissue'
     ],
     'answer': 'C) Skeletal anchorage independent of reciprocal tooth support',
     'explanation': 'Temporary anchorage devices (TADs) are mini-implants or plates fixed to bone to provide absolute or near-absolute anchorage. Because they do not rely on reciprocal tooth support, they allow force systems that would otherwise tip or move anchor teeth.',
     'choice_explanations': {
      'A': 'Fluoride-releasing materials remineralize enamel; that is not the function of TADs. Temporary anchorage devices (TADs) are mini-implants or plates fixed to bone to provide absolute or near-absolute anchorage.',
      'B': 'Bleaching activates peroxide on enamel and is unrelated to skeletal anchorage. Temporary anchorage devices (TADs) are mini-implants or plates fixed to bone to provide absolute or near-absolute anchorage.',
      'C': 'Temporary anchorage devices (TADs) are mini-implants or plates fixed to bone to provide absolute or near-absolute anchorage. Because they do not rely on reciprocal tooth support, they allow force systems that would otherwise tip or move anchor teeth.',
      'D': 'Local anesthetics block nerve conduction; TADs are not soft-tissue drug depots. Temporary anchorage devices (TADs) are mini-implants or plates fixed to bone to provide absolute or near-absolute anchorage.'
     }
    }
   ],
   'extreme': [
    {
     'question': 'Orthodontic treatment in a patient with severe periodontitis most appropriately requires?',
     'options': [
      'A) Immediate heavy rapid maxillary expansion regardless of inflammation',
      'B) Ignoring radiographic bone levels during force application',
      'C) Extracting all remaining teeth before any orthodontics',
      'D) Periodontal disease control first, light forces, and perio co-management'
     ],
     'answer': 'D) Periodontal disease control first, light forces, and perio co-management',
     'explanation': 'Periodontitis involves plaque-driven inflammation and progressive attachment loss; orthodontic forces applied through an inflamed periodontium can accelerate destruction. Disease control (biofilm management and inflammation resolution) must precede carefully monitored light forces with periodontal co-management.',
     'choice_explanations': {
      'A': 'Heavy forces through inflamed periodontium can accelerate attachment loss. Periodontitis involves plaque-driven inflammation and progressive attachment loss; orthodontic forces applied through an inflamed periodontium can accelerate destruction.',
      'B': 'Ignoring bone levels risks loading an unsupported periodontium and worsening destruction. Periodontitis involves plaque-driven inflammation and progressive attachment loss; orthodontic forces applied through an inflamed periodontium can accelerate destruction.',
      'C': 'Pan-extraction is not required; controlled orthodontics after perio therapy can be appropriate. Periodontitis involves plaque-driven inflammation and progressive attachment loss; orthodontic forces applied through an inflamed periodontium can accelerate destruction.',
      'D': 'Periodontitis involves plaque-driven inflammation and progressive attachment loss; orthodontic forces applied through an inflamed periodontium can accelerate destruction. Disease control (biofilm management and inflammation resolution) must precede carefully monitored light forces with periodontal co-management.'
     }
    },
    {
     'question': 'An ectopically erupting maxillary canine close to adjacent roots most threatens?',
     'options': [
      'A) Root resorption of adjacent incisors',
      'B) Cutaneous freckling of the facial skin',
      'C) Geographic tongue on the dorsum',
      'D) Hairy tongue from papilla elongation'
     ],
     'answer': 'A) Root resorption of adjacent incisors',
     'explanation': 'An ectopically erupting maxillary canine can physically resorb the roots of adjacent lateral or central incisors through direct contact and pressure. The risk rises when the canine crown overlies the incisor roots on imaging and warrants timely interceptive management.',
     'choice_explanations': {
      'A': 'An ectopically erupting maxillary canine can physically resorb the roots of adjacent lateral or central incisors through direct contact and pressure. The risk rises when the canine crown overlies the incisor roots on imaging and warrants timely interceptive management.',
      'B': 'Facial freckling is melanocytic pigmentation unrelated to ectopic canine mechanics. An ectopically erupting maxillary canine can physically resorb the roots of adjacent lateral or central incisors through direct contact and pressure.',
      'C': 'Geographic tongue is benign migratory glossitis with migrating filiform-papilla atrophy. An ectopically erupting maxillary canine can physically resorb the roots of adjacent lateral or central incisors through direct contact and pressure.',
      'D': 'Hairy tongue is elongated filiform papillae with retained debris, unrelated to canine ectopia. An ectopically erupting maxillary canine can physically resorb the roots of adjacent lateral or central incisors through direct contact and pressure.'
     }
    },
    {
     'question': 'Choosing surgical orthodontics versus camouflage for skeletal Class III most weighs?',
     'options': [
      'A) Bracket brand and prescription alone',
      'B) Archwire alloy metallurgy alone',
      'C) Growth status, severity, facial profile, and occlusal discrepancy',
      'D) Length of each appointment slot alone'
     ],
     'answer': 'C) Growth status, severity, facial profile, and occlusal discrepancy',
     'explanation': 'Class III malocclusion may be dental, skeletal, or combined; treatment choice depends on remaining growth, skeletal severity, soft-tissue profile, and occlusal discrepancy. Mild dental Class III may be camouflaged, whereas severe skeletal discrepancies often need orthognathic surgery after growth assessment.',
     'choice_explanations': {
      'A': 'Bracket prescription affects mechanics but does not decide surgical vs camouflage Class III. Class III malocclusion may be dental, skeletal, or combined; treatment choice depends on remaining growth, skeletal severity, soft-tissue profile, and occlusal discrepancy.',
      'B': 'Wire alloy affects force delivery, not skeletal severity/profile criteria for Class III surgery. Class III malocclusion may be dental, skeletal, or combined; treatment choice depends on remaining growth, skeletal severity, soft-tissue profile, and occlusal discrepancy.',
      'C': 'Class III malocclusion may be dental, skeletal, or combined; treatment choice depends on remaining growth, skeletal severity, soft-tissue profile, and occlusal discrepancy. Mild dental Class III may be camouflaged, whereas severe skeletal discrepancies often need orthognathic surgery after growth assessment.',
      'D': 'Appointment length is logistical and unrelated to skeletal Class III treatment choice. Class III malocclusion may be dental, skeletal, or combined; treatment choice depends on remaining growth, skeletal severity, soft-tissue profile, and occlusal discrepancy.'
     }
    }
   ]
  },
  'cases': {
   'easy': [
    {
     'title': 'Crowding in Teen',
     'stem': 'A 14-year-old has moderate crowding and Class I molars. Oral hygiene is good.',
     'question': 'First planning idea?',
     'answer': 'Comprehensive orthodontic assessment (records, growth, hygiene).',
     'discussion': 'Treatment options depend on space analysis.',
     'book_hint': "Proffit's Contemporary Orthodontics"
    }
   ],
   'medium': [
    {
     'title': 'Anterior Crossbite Child',
     'stem': 'An 8-year-old has one upper incisor in crossbite with a shift on closing.',
     'question': 'Concern?',
     'answer': 'Functional shift from interference — early correction often indicated.',
     'discussion': 'Prevent asymmetric growth habits.',
     'book_hint': "Proffit's Contemporary Orthodontics"
    }
   ],
   'hard': [
    {
     'title': 'Adult Relapse After Retainers Lost',
     'stem': 'A 28-year-old stopped wearing retainers and crowding returned. Choose the safest high-yield next concept before definitive results.',
     'question': 'Teaching point?',
     'answer': 'Relapse risk is lifelong for many; retention is part of treatment.',
     'discussion': 'Discuss retreatment vs limited alignment.',
     'book_hint': "Proffit's Contemporary Orthodontics"
    }
   ],
   'extreme': [
    {
     'title': 'Growing Class III with Functional Shift',
     'stem': 'A child with developing Class III has an edge-to-edge bite and a shift. Parents want braces immediately. Avoid harmful premature treatment while catastrophic differentials remain open.',
     'question': 'Concept?',
     'answer': 'Distinguish pseudo-Class III / shift from true skeletal Class III; growth modification timing and differential diagnosis matter before irreversible camouflage.',
     'discussion': 'Wrong early extraction plans can harm.',
     'book_hint': "Proffit's Contemporary Orthodontics"
    }
   ]
  }
 },
 'periodontics': {
  'label': 'Periodontics',
  'books': [
   "Carranza's Clinical Periodontology",
   "Lindhe's Clinical Periodontology",
   'Periodontology at a Glance'
  ],
  'pdf_notes': [
   'Gingivitis reversible; periodontitis has attachment loss.',
   'Biofilm disruption is the foundation of care.',
   'Smoking increases severity and masks bleeding.',
   'Re-evaluate after nonsurgical therapy.',
   'NUG: pain, bleeding, necrosis of papillae.'
  ],
  'questions': {
   'easy': [
    {
     'question': 'Main cause of plaque-induced gingivitis?',
     'options': [
      'A) Dental biofilm at the gingival margin',
      'B) Angle Class II malocclusion alone',
      'C) Dens evaginatus of premolars',
      'D) Torus palatinus presence'
     ],
     'answer': 'A) Dental biofilm at the gingival margin',
     'explanation': 'Plaque-induced gingivitis is an inflammatory response of the gingiva to accumulation of dental biofilm at the gingival margin. Microbial products trigger vascular dilation, leukocyte infiltration, and clinical erythema and bleeding that reverse with effective plaque control.',
     'choice_explanations': {
      'A': 'Plaque-induced gingivitis is an inflammatory response of the gingiva to accumulation of dental biofilm at the gingival margin. Microbial products trigger vascular dilation, leukocyte infiltration, and clinical erythema and bleeding that reverse with effective plaque control.',
      'B': 'Class II molar relation is occlusal discrepancy and does not by itself cause plaque gingivitis. Plaque-induced gingivitis is an inflammatory response of the gingiva to accumulation of dental biofilm at the gingival margin.',
      'C': 'Dens evaginatus is an occlusal enamel tubercle that can pulp-expose with wear/fracture. Plaque-induced gingivitis is an inflammatory response of the gingiva to accumulation of dental biofilm at the gingival margin.',
      'D': 'Torus palatinus is a benign midline palatal exostosis unrelated to plaque gingivitis. Plaque-induced gingivitis is an inflammatory response of the gingiva to accumulation of dental biofilm at the gingival margin.'
     }
    },
    {
     'question': 'Clinical hallmark distinguishing periodontitis from gingivitis?',
     'options': [
      'A) Reversible marginal redness without attachment loss',
      'B) Clinical attachment loss and alveolar bone loss',
      'C) Extrinsic stain without inflammation',
      'D) Calculus deposits without any inflammatory response'
     ],
     'answer': 'B) Clinical attachment loss and alveolar bone loss',
     'explanation': 'Gingivitis is inflammation confined to the soft tissue, whereas periodontitis is defined by destruction of the periodontal ligament and alveolar bone, measured as clinical attachment loss. Pocketing and radiographic bone loss corroborate the diagnosis.',
     'choice_explanations': {
      'A': 'Marginal redness without attachment loss defines gingivitis, not periodontitis. Gingivitis is inflammation confined to the soft tissue, whereas periodontitis is defined by destruction of the periodontal ligament and alveolar bone, measured as clinical attachment loss.',
      'B': 'Gingivitis is inflammation confined to the soft tissue, whereas periodontitis is defined by destruction of the periodontal ligament and alveolar bone, measured as clinical attachment loss. Pocketing and radiographic bone loss corroborate the diagnosis.',
      'C': 'Extrinsic stain is surface pigment and does not define periodontitis. Gingivitis is inflammation confined to the soft tissue, whereas periodontitis is defined by destruction of the periodontal ligament and alveolar bone, measured as clinical attachment loss.',
      'D': 'Calculus harbors biofilm but periodontitis requires inflammatory attachment/bone loss. Gingivitis is inflammation confined to the soft tissue, whereas periodontitis is defined by destruction of the periodontal ligament and alveolar bone, measured as clinical attachment loss.'
     }
    },
    {
     'question': 'Best foundation for daily plaque control?',
     'options': [
      'A) Whitening strips as the sole hygiene method',
      'B) Chewing ice to abrade plaque',
      'C) Toothbrushing with interdental cleaning',
      'D) Charcoal powder alone without brushing technique'
     ],
     'answer': 'C) Toothbrushing with interdental cleaning',
     'explanation': 'Dental biofilm must be disrupted mechanically because saliva and rinses alone do not remove adherent plaque from tooth surfaces. Toothbrushing cleans facial and lingual surfaces; interdental aids clean proximal niches where periodontitis often begins.',
     'choice_explanations': {
      'A': 'Whitening strips deliver peroxide for stain and do not adequately disrupt interdental biofilm. Dental biofilm must be disrupted mechanically because saliva and rinses alone do not remove adherent plaque from tooth surfaces.',
      'B': 'Chewing ice risks dental injury and is not an effective plaque-control method. Dental biofilm must be disrupted mechanically because saliva and rinses alone do not remove adherent plaque from tooth surfaces.',
      'C': 'Dental biofilm must be disrupted mechanically because saliva and rinses alone do not remove adherent plaque from tooth surfaces. Toothbrushing cleans facial and lingual surfaces; interdental aids clean proximal niches where periodontitis often begins.',
      'D': 'Charcoal powder lacks proven mechanical biofilm control and may abrade tissues/restorations. Dental biofilm must be disrupted mechanically because saliva and rinses alone do not remove adherent plaque from tooth surfaces.'
     }
    }
   ],
   'medium': [
    {
     'question': 'Furcation involvement is assessed on which teeth?',
     'options': [
      'A) Maxillary central incisors',
      'B) Mandibular canines',
      'C) Primary lateral incisors',
      'D) Multirooted teeth such as molars'
     ],
     'answer': 'D) Multirooted teeth such as molars',
     'explanation': 'Furcation involvement is pathologic bone loss between the roots of multirooted teeth, exposing the furcation entrance. Single-rooted teeth lack furcations, so this assessment applies to molars and some premolars with bifurcated roots.',
     'choice_explanations': {
      'A': 'Maxillary central incisors are single-rooted and have no furcation to probe. Furcation involvement is pathologic bone loss between the roots of multirooted teeth, exposing the furcation entrance.',
      'B': 'Mandibular canine roots occupy the anterior mandible and do not abut the maxillary antrum. Furcation involvement is pathologic bone loss between the roots of multirooted teeth, exposing the furcation entrance.',
      'C': 'Primary lateral incisors are single-rooted and lack furcations. Furcation involvement is pathologic bone loss between the roots of multirooted teeth, exposing the furcation entrance.',
      'D': 'Furcation involvement is pathologic bone loss between the roots of multirooted teeth, exposing the furcation entrance. Single-rooted teeth lack furcations, so this assessment applies to molars and some premolars with bifurcated roots.'
     }
    },
    {
     'question': 'How does smoking typically affect periodontitis?',
     'options': [
      'A) Protects clinical attachment indefinitely',
      'B) Increases risk and severity while masking bleeding',
      'C) Naturally whitens roots without tissue effect',
      'D) Has no measurable effect on periodontal disease'
     ],
     'answer': 'B) Increases risk and severity while masking bleeding',
     'explanation': 'Tobacco smoking impairs neutrophil function, reduces gingival blood flow, and alters cytokine responses, increasing periodontitis risk and severity. Reduced vascularity also masks gingival bleeding, so disease may look less inflamed than it is.',
     'choice_explanations': {
      'A': 'Smoking does not protect attachment; it impairs host response and worsens periodontitis. Tobacco smoking impairs neutrophil function, reduces gingival blood flow, and alters cytokine responses, increasing periodontitis risk and severity.',
      'B': 'Tobacco smoking impairs neutrophil function, reduces gingival blood flow, and alters cytokine responses, increasing periodontitis risk and severity. Reduced vascularity also masks gingival bleeding, so disease may look less inflamed than it is.',
      'C': 'Smoking does not therapeutically whiten roots or spare periodontal tissues. Tobacco smoking impairs neutrophil function, reduces gingival blood flow, and alters cytokine responses, increasing periodontitis risk and severity.',
      'D': 'Smoking has a documented adverse effect on periodontitis risk and healing. Tobacco smoking impairs neutrophil function, reduces gingival blood flow, and alters cytokine responses, increasing periodontitis risk and severity.'
     }
    },
    {
     'question': 'Rapidly progressive periodontitis in a young patient historically associated with which theme?',
     'options': [
      'A) Cervical abrasion from brushing alone',
      'B) Enamel fluorosis without attachment change',
      'C) Occlusal attrition as the sole cause of bone loss',
      'D) Severe attachment loss out of proportion to deposits, with A. actinomycetemcomitans often discussed'
     ],
     'answer': 'D) Severe attachment loss out of proportion to deposits, with A. actinomycetemcomitans often discussed',
     'explanation': 'Rapidly progressive periodontitis in young patients (historically localized aggressive periodontitis) features severe attachment loss out of proportion to local deposits. Aggregatibacter actinomycetemcomitans has been classically associated in many cases, though staging/grading frameworks now emphasize rate and risk factors.',
     'choice_explanations': {
      'A': 'Cervical abrasion is mechanical tooth wear, not aggressive periodontitis attachment loss. Rapidly progressive periodontitis in young patients (historically localized aggressive periodontitis) features severe attachment loss out of proportion to local deposits.',
      'B': 'Fluorosis is enamel hypomineralization without periodontal attachment loss. Rapidly progressive periodontitis in young patients (historically localized aggressive periodontitis) features severe attachment loss out of proportion to local deposits.',
      'C': 'Attrition alone does not produce plaque-associated rapid attachment-loss patterns. Rapidly progressive periodontitis in young patients (historically localized aggressive periodontitis) features severe attachment loss out of proportion to local deposits.',
      'D': 'Rapidly progressive periodontitis in young patients (historically localized aggressive periodontitis) features severe attachment loss out of proportion to local deposits. Aggregatibacter actinomycetemcomitans has been classically associated in many cases, though staging/grading frameworks now emphasize rate and risk factors.'
     }
    }
   ],
   'hard': [
    {
     'question': 'Urgent care of a periodontal abscess most appropriately includes?',
     'options': [
      'A) Drainage and debridement, with antimicrobials if systemic signs',
      'B) Home bleaching tray use alone',
      'C) Orthodontic wax over the gingival margin',
      'D) Lifelong nightguard wear without local therapy'
     ],
     'answer': 'A) Drainage and debridement, with antimicrobials if systemic signs',
     'explanation': 'A periodontal abscess is a localized purulent infection within a periodontal pocket or furcation. Drainage of pus, debridement of the pocket, and systemic antimicrobials when there are fever or spreading infection constitute appropriate urgent care.',
     'choice_explanations': {
      'A': 'A periodontal abscess is a localized purulent infection within a periodontal pocket or furcation. Drainage of pus, debridement of the pocket, and systemic antimicrobials when there are fever or spreading infection constitute appropriate urgent care.',
      'B': 'Bleaching trays do not drain pocket pus or debride a periodontal abscess. A periodontal abscess is a localized purulent infection within a periodontal pocket or furcation.',
      'C': 'Orthodontic wax shields mucosa from brackets; it does not treat periodontal abscess. A periodontal abscess is a localized purulent infection within a periodontal pocket or furcation.',
      'D': 'A nightguard modifies occlusal load but does not drain or debride acute abscess. A periodontal abscess is a localized purulent infection within a periodontal pocket or furcation.'
     }
    },
    {
     'question': 'Peri-implantitis is characterized by?',
     'options': [
      'A) Soft-tissue inflammation without progressive bone loss (mucositis only)',
      'B) Food impaction without any inflammatory signs',
      'C) Inflammation plus progressive crestal bone loss around an implant',
      'D) Crown shade mismatch without biologic change'
     ],
     'answer': 'C) Inflammation plus progressive crestal bone loss around an implant',
     'explanation': 'Peri-implant mucositis is reversible soft-tissue inflammation around an implant without progressive bone loss. Peri-implantitis adds progressive crestal bone loss to inflammation and probing changes, threatening implant survival.',
     'choice_explanations': {
      'A': 'Peri-implant mucositis is soft-tissue inflammation without progressive crestal bone loss. Peri-implant mucositis is reversible soft-tissue inflammation around an implant without progressive bone loss.',
      'B': 'Food impaction alone without inflammation/bone loss does not define peri-implantitis. Peri-implant mucositis is reversible soft-tissue inflammation around an implant without progressive bone loss.',
      'C': 'Peri-implant mucositis is reversible soft-tissue inflammation around an implant without progressive bone loss. Peri-implantitis adds progressive crestal bone loss to inflammation and probing changes, threatening implant survival.',
      'D': 'Shade mismatch is esthetic and not a biologic peri-implant disease definition. Peri-implant mucositis is reversible soft-tissue inflammation around an implant without progressive bone loss.'
     }
    },
    {
     'question': 'Occlusal trauma alone, without plaque-driven inflammation, most accurately?',
     'options': [
      'A) Initiates periodontitis even in a plaque-free mouth',
      'B) Resolves existing periodontal pockets without debridement',
      'C) Substitutes for mechanical plaque control',
      'D) Does not initiate the plaque-induced periodontitis pathway'
     ],
     'answer': 'D) Does not initiate the plaque-induced periodontitis pathway',
     'explanation': 'Occlusal trauma produces adaptive or pathologic changes in the periodontium from excessive occlusal load, but it does not initiate the plaque-induced inflammatory pathway of periodontitis. When inflammation is present, trauma can worsen attachment loss patterns.',
     'choice_explanations': {
      'A': 'Occlusal trauma alone does not initiate the plaque-driven periodontitis pathway. Occlusal trauma produces adaptive or pathologic changes in the periodontium from excessive occlusal load, but it does not initiate the plaque-induced inflammatory pathway of periodontitis.',
      'B': 'Occlusal therapy does not replace biofilm debridement needed for inflammatory pockets. Occlusal trauma produces adaptive or pathologic changes in the periodontium from excessive occlusal load, but it does not initiate the plaque-induced inflammatory pathway of periodontitis.',
      'C': 'Occlusal adjustment cannot substitute for mechanical disruption of pathogenic biofilm. Occlusal trauma produces adaptive or pathologic changes in the periodontium from excessive occlusal load, but it does not initiate the plaque-induced inflammatory pathway of periodontitis.',
      'D': 'Occlusal trauma produces adaptive or pathologic changes in the periodontium from excessive occlusal load, but it does not initiate the plaque-induced inflammatory pathway of periodontitis. When inflammation is present, trauma can worsen attachment loss patterns.'
     }
    }
   ],
   'extreme': [
    {
     'question': 'Classic clinical triad of necrotizing ulcerative gingivitis includes?',
     'options': [
      'A) Peg lateral morphology alone',
      'B) Asymptomatic extrinsic stain alone',
      'C) Dens in dente without soft-tissue change',
      'D) Pain, bleeding, and interdental papillary necrosis with fetor'
     ],
     'answer': 'D) Pain, bleeding, and interdental papillary necrosis with fetor',
     'explanation': 'Necrotizing ulcerative gingivitis presents with painful punched-out interdental papillae, spontaneous bleeding, and often fetor oris. Fusospirochetal overgrowth in a host compromised by stress, smoking, or immunosuppression underlies the syndrome.',
     'choice_explanations': {
      'A': 'Peg laterals are a crown-form anomaly, not the NUG clinical triad. Necrotizing ulcerative gingivitis presents with painful punched-out interdental papillae, spontaneous bleeding, and often fetor oris.',
      'B': 'Extrinsic stain without necrosis/pain is not necrotizing ulcerative gingivitis. Necrotizing ulcerative gingivitis presents with painful punched-out interdental papillae, spontaneous bleeding, and often fetor oris.',
      'C': 'Dens in dente is a developmental invagination, not NUG soft-tissue necrosis. Necrotizing ulcerative gingivitis presents with painful punched-out interdental papillae, spontaneous bleeding, and often fetor oris.',
      'D': 'Necrotizing ulcerative gingivitis presents with painful punched-out interdental papillae, spontaneous bleeding, and often fetor oris. Fusospirochetal overgrowth in a host compromised by stress, smoking, or immunosuppression underlies the syndrome.'
     }
    },
    {
     'question': 'A pregnancy epulis is best described as?',
     'options': [
      'A) Malignant melanoma until proven otherwise in every case',
      'B) A pyogenic granuloma variant that often regresses postpartum',
      'C) A primary osteosarcoma of the alveolar ridge',
      'D) An odontogenic caries lesion of enamel'
     ],
     'answer': 'B) A pyogenic granuloma variant that often regresses postpartum',
     'explanation': 'A pregnancy epulis is a pyogenic granuloma arising from gingiva under the influence of elevated pregnancy hormones and local irritants. It is a reactive vascular lesion, not a true neoplasm, and frequently regresses after delivery once irritants are controlled.',
     'choice_explanations': {
      'A': 'Pregnancy epulis is a reactive vascular lesion, not melanoma by default. A pregnancy epulis is a pyogenic granuloma arising from gingiva under the influence of elevated pregnancy hormones and local irritants.',
      'B': 'A pregnancy epulis is a pyogenic granuloma arising from gingiva under the influence of elevated pregnancy hormones and local irritants. It is a reactive vascular lesion, not a true neoplasm, and frequently regresses after delivery once irritants are controlled.',
      'C': 'Osteosarcoma is a malignant bone neoplasm, not a reactive gingival pregnancy epulis. A pregnancy epulis is a pyogenic granuloma arising from gingiva under the influence of elevated pregnancy hormones and local irritants.',
      'D': 'Caries is demineralization of tooth hard tissue, not a soft-tissue epulis. A pregnancy epulis is a pyogenic granuloma arising from gingiva under the influence of elevated pregnancy hormones and local irritants.'
     }
    },
    {
     'question': 'Guided tissue regeneration aims primarily for?',
     'options': [
      'A) Extrinsic stain removal from enamel',
      'B) Enamel microabrasion for white-spot lesions',
      'C) Regeneration of a new periodontal attachment apparatus',
      'D) Vital bleaching of the clinical crown'
     ],
     'answer': 'C) Regeneration of a new periodontal attachment apparatus',
     'explanation': 'Guided tissue regeneration uses a barrier membrane to exclude gingival epithelium and connective tissue from the periodontal defect, allowing periodontal ligament and bone cells to repopulate the root surface and form new cementum, PDL, and bone.',
     'choice_explanations': {
      'A': 'Stain removal is prophylaxis/polishing, not regeneration of periodontal attachment. Guided tissue regeneration uses a barrier membrane to exclude gingival epithelium and connective tissue from the periodontal defect, allowing periodontal ligament and bone cells to repopulate the root surface and form new cementum, PDL, and bone.',
      'B': 'Microabrasion removes superficial enamel defects; it does not regenerate PDL/bone/cementum. Guided tissue regeneration uses a barrier membrane to exclude gingival epithelium and connective tissue from the periodontal defect, allowing periodontal ligament and bone cells to repopulate the root surface and form new cementum, PDL, and bone.',
      'C': 'Guided tissue regeneration uses a barrier membrane to exclude gingival epithelium and connective tissue from the periodontal defect, allowing periodontal ligament and bone cells to repopulate the root surface and form new cementum, PDL, and bone.',
      'D': 'Bleaching oxidizes chromogens in enamel/dentin and does not regenerate attachment. Guided tissue regeneration uses a barrier membrane to exclude gingival epithelium and connective tissue from the periodontal defect, allowing periodontal ligament and bone cells to repopulate the root surface and form new cementum, PDL, and bone.'
     }
    }
   ]
  },
  'cases': {
   'easy': [
    {
     'title': 'Bleeding Gums',
     'stem': 'A student has bleeding on brushing, soft swollen gingiva, no radiographic bone loss.',
     'question': 'Diagnosis?',
     'answer': 'Plaque-induced gingivitis.',
     'discussion': 'OHI and prophylaxis; reversible.',
     'book_hint': "Carranza's Clinical Periodontology"
    }
   ],
   'medium': [
    {
     'title': 'Deep Pockets Molars',
     'stem': 'A 45-year-old smoker has 6–7 mm pockets on molars with horizontal bone loss.',
     'question': 'Management pillars?',
     'answer': 'Risk factor control, nonsurgical debridement, re-evaluation, surgery if indicated.',
     'discussion': 'Smoking cessation counseling.',
     'book_hint': "Carranza's Clinical Periodontology"
    }
   ],
   'hard': [
    {
     'title': 'Diabetic with Recurrent Abscesses',
     'stem': 'Poorly controlled diabetes, multiple periodontal abscesses, deep pockets. Choose the safest high-yield next concept before definitive results.',
     'question': 'Priority concept?',
     'answer': 'Medical coordination for glycemic control + acute drainage/debridement + definitive perio plan.',
     'discussion': 'Diabetes and perio bidirectionally interact.',
     'book_hint': "Carranza's Clinical Periodontology"
    }
   ],
   'extreme': [
    {
     'title': 'NUG in Stressed Student',
     'stem': 'A stressed young adult smoker has punched-out papillae, severe pain, and fetor oris. Avoid harmful premature treatment while catastrophic differentials remain open.',
     'question': 'Diagnosis and first care?',
     'answer': 'NUG — gentle debridement, OHI, antiseptics, address risk factors; antibiotics if systemic/immunocompromise.',
     'discussion': 'Rule out HIV/other immunodeficiency when atypical.',
     'book_hint': "Carranza's Clinical Periodontology"
    }
   ]
  }
 },
 'endodontics': {
  'label': 'Endodontics',
  'books': [
   "Cohen's Pathways of the Pulp",
   'Endodontics — Torabinejad',
   "Ingle's Endodontics"
  ],
  'pdf_notes': [
   'Rubber dam is standard isolation for RCT.',
   'Lingering spontaneous pain suggests irreversible pulpitis.',
   'NaOCl irrigates but extrusion is dangerous.',
   'Missed canals (MB2) cause failure.',
   'Follow IADT for traumatic dental injuries.'
  ],
  'questions': {
   'easy': [
    {
     'question': 'Symptomatic irreversible pulpitis pain is characteristically?',
     'options': [
      'A) Spontaneous and lingering to cold stimuli',
      'B) Brief thermal sensitivity that resolves immediately after stimulus removal',
      'C) Limited to mucosal itching without thermal change',
      'D) Identical to a reciprocal TMJ click on opening'
     ],
     'answer': 'A) Spontaneous and lingering to cold stimuli',
     'explanation': 'Symptomatic irreversible pulpitis reflects vital pulp tissue with inflammation severe enough that it cannot resolve even after removal of the irritant. C-fiber–mediated pain is often spontaneous and lingers after cold is removed, guiding pulp therapy decisions.',
     'choice_explanations': {
      'A': 'Symptomatic irreversible pulpitis reflects vital pulp tissue with inflammation severe enough that it cannot resolve even after removal of the irritant. C-fiber–mediated pain is often spontaneous and lingers after cold is removed, guiding pulp therapy decisions.',
      'B': 'Brief non-lingering thermal pain characterizes reversible pulpitis. Symptomatic irreversible pulpitis reflects vital pulp tissue with inflammation severe enough that it cannot resolve even after removal of the irritant.',
      'C': 'Mucosal itching is not the C-fiber thermal pain pattern of irreversible pulpitis. Symptomatic irreversible pulpitis reflects vital pulp tissue with inflammation severe enough that it cannot resolve even after removal of the irritant.',
      'D': 'A reciprocal TMJ click indicates disc displacement with reduction, not pulpitis. Symptomatic irreversible pulpitis reflects vital pulp tissue with inflammation severe enough that it cannot resolve even after removal of the irritant.'
     }
    },
    {
     'question': 'Best isolation method for root canal treatment?',
     'options': [
      'A) Cotton rolls alone for the entire procedure',
      'B) Rubber dam isolation of the operating field',
      'C) No isolation if suction is available',
      'D) Cheek retractor alone without a dam'
     ],
     'answer': 'B) Rubber dam isolation of the operating field',
     'explanation': 'A rubber dam isolates the tooth from saliva and oral microbes, preventing contamination of the root canal system during instrumentation and obturation. It also protects the airway from instruments and irrigants.',
     'choice_explanations': {
      'A': 'Cotton rolls reduce local moisture but cannot reliably isolate canals from saliva/microbes. A rubber dam isolates the tooth from saliva and oral microbes, preventing contamination of the root canal system during instrumentation and obturation.',
      'B': 'A rubber dam isolates the tooth from saliva and oral microbes, preventing contamination of the root canal system during instrumentation and obturation. It also protects the airway from instruments and irrigants.',
      'C': 'Suction alone does not prevent salivary contamination of open canals. A rubber dam isolates the tooth from saliva and oral microbes, preventing contamination of the root canal system during instrumentation and obturation.',
      'D': 'Cheek retractors improve access but do not seal oral fluids from the canal system. A rubber dam isolates the tooth from saliva and oral microbes, preventing contamination of the root canal system during instrumentation and obturation.'
     }
    },
    {
     'question': 'Working length for canal preparation is ideally set near?',
     'options': [
      'A) Beyond the cortical plate into the maxillary sinus',
      'B) The pulp horn only',
      'C) The cementoenamel junction only',
      'D) The apical constriction / near radiographic apex per protocol'
     ],
     'answer': 'D) The apical constriction / near radiographic apex per protocol',
     'explanation': 'The apical constriction is the narrowest point of the canal near the cementoenamel or cementodentinal junction and is the usual physiologic terminus for canal preparation. Working length is set to this region using electronic apex location and radiographic confirmation.',
     'choice_explanations': {
      'A': 'Instrumentation beyond the apex into sinus/bone risks extrusion injury, not physiologic working length. The apical constriction is the narrowest point of the canal near the cementoenamel or cementodentinal junction and is the usual physiologic terminus for canal preparation.',
      'B': 'Pulp horns are coronal extensions; working length is measured to the apical canal terminus. The apical constriction is the narrowest point of the canal near the cementoenamel or cementodentinal junction and is the usual physiologic terminus for canal preparation.',
      'C': 'CEJ is a coronal landmark, not the apical constriction used for working length. The apical constriction is the narrowest point of the canal near the cementoenamel or cementodentinal junction and is the usual physiologic terminus for canal preparation.',
      'D': 'The apical constriction is the narrowest point of the canal near the cementoenamel or cementodentinal junction and is the usual physiologic terminus for canal preparation. Working length is set to this region using electronic apex location and radiographic confirmation.'
     }
    }
   ],
   'medium': [
    {
     'question': 'A necrotic pulp with an apical radiolucency most strongly suggests?',
     'options': [
      'A) Reversible pulpitis without apical change',
      'B) Apical periodontitis',
      'C) Enamel hypoplasia of the crown',
      'D) Dental fluorosis mottling'
     ],
     'answer': 'B) Apical periodontitis',
     'explanation': 'Pulp necrosis allows bacteria and their toxins to exit through apical foramina into the periodontal ligament and bone. The resulting inflammatory bone resorption appears as a periapical radiolucency and defines apical periodontitis.',
     'choice_explanations': {
      'A': 'Reversible pulpitis lacks apical radiolucency; necrosis plus lucency indicates apical periodontitis. Pulp necrosis allows bacteria and their toxins to exit through apical foramina into the periodontal ligament and bone.',
      'B': 'Pulp necrosis allows bacteria and their toxins to exit through apical foramina into the periodontal ligament and bone. The resulting inflammatory bone resorption appears as a periapical radiolucency and defines apical periodontitis.',
      'C': 'Enamel hypoplasia is a developmental crown defect, not a periapical radiolucency. Pulp necrosis allows bacteria and their toxins to exit through apical foramina into the periodontal ligament and bone.',
      'D': 'Fluorosis is enamel hypomineralization from excess fluoride intake during formation. Pulp necrosis allows bacteria and their toxins to exit through apical foramina into the periodontal ligament and bone.'
     }
    },
    {
     'question': 'Sodium hypochlorite is used in endodontics primarily as?',
     'options': [
      'A) An obturation sealer cement',
      'B) A temporary coronal filling material',
      'C) An irrigant with tissue-dissolving and antimicrobial action',
      'D) A local anesthetic solution'
     ],
     'answer': 'C) An irrigant with tissue-dissolving and antimicrobial action',
     'explanation': 'Sodium hypochlorite dissolves necrotic pulp tissue and has broad antimicrobial activity against canal flora, making it the primary endodontic irrigant. Its cytotoxicity means extrusion beyond the apex must be avoided.',
     'choice_explanations': {
      'A': 'Sealers fill obturation interfaces; NaOCl is a tissue-dissolving canal irrigant, not a sealer. Sodium hypochlorite dissolves necrotic pulp tissue and has broad antimicrobial activity against canal flora, making it the primary endodontic irrigant.',
      'B': 'Temporary fillings seal access cavities; NaOCl is used as irrigant during instrumentation. Sodium hypochlorite dissolves necrotic pulp tissue and has broad antimicrobial activity against canal flora, making it the primary endodontic irrigant.',
      'C': 'Sodium hypochlorite dissolves necrotic pulp tissue and has broad antimicrobial activity against canal flora, making it the primary endodontic irrigant. Its cytotoxicity means extrusion beyond the apex must be avoided.',
      'D': 'Local anesthetics block nerve conduction; NaOCl is a cytotoxic irrigant, not an anesthetic. Sodium hypochlorite dissolves necrotic pulp tissue and has broad antimicrobial activity against canal flora, making it the primary endodontic irrigant.'
     }
    },
    {
     'question': 'Cracked-tooth pain is characteristically elicited on?',
     'options': [
      'A) Percussion of an adjacent unrestored tooth only',
      'B) Hot liquids alone without any bite loading',
      'C) Supine posture alone without occlusal contact',
      'D) Release of biting pressure on the affected cusp'
     ],
     'answer': 'D) Release of biting pressure on the affected cusp',
     'explanation': 'In a cracked tooth, occlusal load briefly separates the crack walls and stimulates the pulp or periodontal ligament; pain is characteristically sharp on release of biting pressure as the segments snap back together.',
     'choice_explanations': {
      'A': 'Pain limited to an adjacent intact tooth does not define cracked-tooth bite-release pain. In a cracked tooth, occlusal load briefly separates the crack walls and stimulates the pulp or periodontal ligament; pain is characteristically sharp on release of biting pressure as the segments snap back together.',
      'B': 'Thermal pulpitis pain differs from the occlusal bite-release pattern of a cracked tooth. In a cracked tooth, occlusal load briefly separates the crack walls and stimulates the pulp or periodontal ligament; pain is characteristically sharp on release of biting pressure as the segments snap back together.',
      'C': 'Posture without occlusal loading does not elicit classic cracked-tooth pain. In a cracked tooth, occlusal load briefly separates the crack walls and stimulates the pulp or periodontal ligament; pain is characteristically sharp on release of biting pressure as the segments snap back together.',
      'D': 'In a cracked tooth, occlusal load briefly separates the crack walls and stimulates the pulp or periodontal ligament; pain is characteristically sharp on release of biting pressure as the segments snap back together.'
     }
    }
   ],
   'hard': [
    {
     'question': 'A sodium hypochlorite extrusion accident typically presents with?',
     'options': [
      'A) Mild extrinsic enamel stain without soft-tissue change',
      'B) Gradual low-grade pulpitis symptoms over weeks',
      'C) Isolated taste alteration without pain or swelling',
      'D) Sudden severe pain, swelling, and ecchymosis after irrigation'
     ],
     'answer': 'D) Sudden severe pain, swelling, and ecchymosis after irrigation',
     'explanation': 'Forceful extrusion of sodium hypochlorite into periapical tissues causes immediate chemical burns of soft tissue and vessels. Patients experience sudden severe pain, rapid swelling, and often ecchymosis; management is supportive with monitoring for airway compromise.',
     'choice_explanations': {
      'A': 'Enamel stain is not the acute soft-tissue chemical burn of NaOCl extrusion. Forceful extrusion of sodium hypochlorite into periapical tissues causes immediate chemical burns of soft tissue and vessels.',
      'B': 'NaOCl extrusion accidents are immediate, not gradual week-scale pulpitis. Forceful extrusion of sodium hypochlorite into periapical tissues causes immediate chemical burns of soft tissue and vessels.',
      'C': 'Taste change alone does not describe acute pain/swelling/ecchymosis of NaOCl extrusion. Forceful extrusion of sodium hypochlorite into periapical tissues causes immediate chemical burns of soft tissue and vessels.',
      'D': 'Forceful extrusion of sodium hypochlorite into periapical tissues causes immediate chemical burns of soft tissue and vessels. Patients experience sudden severe pain, rapid swelling, and often ecchymosis; management is supportive with monitoring for airway compromise.'
     }
    },
    {
     'question': 'Missing a second mesiobuccal canal (MB2) in a maxillary molar most often leads to?',
     'options': [
      'A) Improved long-term prognosis in all cases',
      'B) Persistent infection and treatment failure risk',
      'C) Cutaneous facial color change',
      'D) Drug-induced gingival hyperplasia'
     ],
     'answer': 'B) Persistent infection and treatment failure risk',
     'explanation': 'Maxillary molars frequently have a second mesiobuccal canal (MB2) that branches within the mesiobuccal root. If untreated, residual bacteria in MB2 sustain periapical inflammation and cause post-treatment disease.',
     'choice_explanations': {
      'A': 'Missing MB2 leaves untreated canal infection and worsens prognosis. Maxillary molars frequently have a second mesiobuccal canal (MB2) that branches within the mesiobuccal root.',
      'B': 'Maxillary molars frequently have a second mesiobuccal canal (MB2) that branches within the mesiobuccal root. If untreated, residual bacteria in MB2 sustain periapical inflammation and cause post-treatment disease.',
      'C': 'Facial skin color change is unrelated to missed MB2 canal infection. Maxillary molars frequently have a second mesiobuccal canal (MB2) that branches within the mesiobuccal root.',
      'D': 'Drug-induced gingival overgrowth is a soft-tissue drug effect, not a missed-MB2 sequela. Maxillary molars frequently have a second mesiobuccal canal (MB2) that branches within the mesiobuccal root.'
     }
    },
    {
     'question': 'Prognosis of a complete vertical root fracture is often?',
     'options': [
      'A) Excellent healing with nonsurgical RCT alone',
      'B) Observation without intervention indefinitely',
      'C) Poor, with extraction commonly required',
      'D) Resolved by internal bleaching alone'
     ],
     'answer': 'C) Poor, with extraction commonly required',
     'explanation': 'A complete vertical root fracture separates the root along its long axis, creating a pathway for bacteria from the oral cavity into the periodontium. The resulting localized deep pocket and bone loss rarely heal with root canal therapy alone; extraction is often necessary.',
     'choice_explanations': {
      'A': 'Complete VRF opens a bacterial pathway that nonsurgical RCT alone rarely heals. A complete vertical root fracture separates the root along its long axis, creating a pathway for bacteria from the oral cavity into the periodontium.',
      'B': 'Indefinite observation leaves fracture-associated periodontal destruction progressive. A complete vertical root fracture separates the root along its long axis, creating a pathway for bacteria from the oral cavity into the periodontium.',
      'C': 'A complete vertical root fracture separates the root along its long axis, creating a pathway for bacteria from the oral cavity into the periodontium. The resulting localized deep pocket and bone loss rarely heal with root canal therapy alone; extraction is often necessary.',
      'D': 'Internal bleaching treats intrinsic discoloration and does not repair a fractured root. A complete vertical root fracture separates the root along its long axis, creating a pathway for bacteria from the oral cavity into the periodontium.'
     }
    }
   ],
   'extreme': [
    {
     'question': 'An avulsed permanent tooth with extraoral dry time greater than 60 minutes most implies?',
     'options': [
      'A) Excellent PDL viability and unchanged prognosis',
      'B) That dry time is irrelevant if the tooth is replanted',
      'C) Identical management rules as for primary teeth',
      'D) Poor PDL viability and worsened prognosis; manage per trauma guidelines'
     ],
     'answer': 'D) Poor PDL viability and worsened prognosis; manage per trauma guidelines',
     'explanation': 'Periodontal ligament cells on an avulsed tooth die progressively with extraoral dry time; beyond about 60 minutes of dry storage, PDL viability is severely compromised. Replantation may still be attempted after surface management, but ankylosis and replacement resorption risks are high.',
     'choice_explanations': {
      'A': 'PDL cells die with prolonged dry time; >60 min dry storage means poor viability. Periodontal ligament cells on an avulsed tooth die progressively with extraoral dry time; beyond about 60 minutes of dry storage, PDL viability is severely compromised.',
      'B': 'Extraoral dry time critically determines PDL cell survival and avulsion prognosis. Periodontal ligament cells on an avulsed tooth die progressively with extraoral dry time; beyond about 60 minutes of dry storage, PDL viability is severely compromised.',
      'C': 'Permanent avulsion protocols differ from primary teeth, which are generally not replanted. Periodontal ligament cells on an avulsed tooth die progressively with extraoral dry time; beyond about 60 minutes of dry storage, PDL viability is severely compromised.',
      'D': 'Periodontal ligament cells on an avulsed tooth die progressively with extraoral dry time; beyond about 60 minutes of dry storage, PDL viability is severely compromised. Replantation may still be attempted after surface management, but ankylosis and replacement resorption risks are high.'
     }
    },
    {
     'question': 'A true combined perio-endo lesion most appropriately requires?',
     'options': [
      'A) Addressing both endodontic and periodontal infection pathways',
      'B) Scaling alone without pulp testing',
      'C) Orthodontic alignment as sole therapy',
      'D) Vital tooth whitening as definitive care'
     ],
     'answer': 'A) Addressing both endodontic and periodontal infection pathways',
     'explanation': 'Combined perio-endo lesions involve communication between pulpal and periodontal infection pathways, so both niches must be disinfected for healing. When the primary source is endodontic, root canal treatment often precedes definitive periodontal therapy.',
     'choice_explanations': {
      'A': 'Combined perio-endo lesions involve communication between pulpal and periodontal infection pathways, so both niches must be disinfected for healing. When the primary source is endodontic, root canal treatment often precedes definitive periodontal therapy.',
      'B': 'Scaling alone ignores a pulpal source when a true combined lesion exists. Combined perio-endo lesions involve communication between pulpal and periodontal infection pathways, so both niches must be disinfected for healing.',
      'C': 'Alignment does not disinfect pulpal or periodontal infection pathways. Combined perio-endo lesions involve communication between pulpal and periodontal infection pathways, so both niches must be disinfected for healing.',
      'D': 'Whitening does not treat perio-endo infection. Combined perio-endo lesions involve communication between pulpal and periodontal infection pathways, so both niches must be disinfected for healing.'
     }
    },
    {
     'question': 'Internal versus external root resorption is distinguished clinically because?',
     'options': [
      'A) They share identical radiographic outlines and identical treatment',
      'B) Both resolve spontaneously without intervention',
      'C) Radiographic and clinical patterns differ and treatment differs',
      'D) Extraction is required before any imaging or vitality testing'
     ],
     'answer': 'C) Radiographic and clinical patterns differ and treatment differs',
     'explanation': 'Internal resorption begins within the pulp chamber or canal from inflamed pulp tissue and appears as a ballooned canal outline that moves with tube shift less than external defects. External cervical resorption begins on the root surface; diagnosis directs whether pulp therapy, repair, or extraction is indicated.',
     'choice_explanations': {
      'A': 'Internal and external resorption differ radiographically and require different treatment. Internal resorption begins within the pulp chamber or canal from inflamed pulp tissue and appears as a ballooned canal outline that moves with tube shift less than external defects.',
      'B': 'Pathologic root resorption generally progresses without appropriate intervention. Internal resorption begins within the pulp chamber or canal from inflamed pulp tissue and appears as a ballooned canal outline that moves with tube shift less than external defects.',
      'C': 'Internal resorption begins within the pulp chamber or canal from inflamed pulp tissue and appears as a ballooned canal outline that moves with tube shift less than external defects. External cervical resorption begins on the root surface; diagnosis directs whether pulp therapy, repair, or extraction is indicated.',
      'D': 'Diagnosis requires imaging and vitality testing before deciding extraction. Internal resorption begins within the pulp chamber or canal from inflamed pulp tissue and appears as a ballooned canal outline that moves with tube shift less than external defects.'
     }
    }
   ]
  },
  'cases': {
   'easy': [
    {
     'title': 'Night Pain Lower Molar',
     'stem': 'Spontaneous night pain, lingering cold response, no periapical radiolucency yet.',
     'question': 'Likely pulp status?',
     'answer': 'Symptomatic irreversible pulpitis.',
     'discussion': 'RCT or extraction after consent.',
     'book_hint': "Cohen's Pathways of the Pulp"
    }
   ],
   'medium': [
    {
     'title': 'Sinus Tract on Gingiva',
     'stem': 'Chronic draining sinus over apex of nonvital lateral; radiolucency present.',
     'question': 'Treatment concept?',
     'answer': 'Root canal therapy of the source tooth (+ restore).',
     'discussion': 'Trace sinus with gutta-percha if needed.',
     'book_hint': "Cohen's Pathways of the Pulp"
    }
   ],
   'hard': [
    {
     'title': 'RCT Done but Pain Persists',
     'stem': 'Upper 6 had RCT; pain on biting persists; J-shaped lesion on root. Choose the safest high-yield next concept before definitive results.',
     'question': 'Suspect?',
     'answer': 'Vertical root fracture or missed canal / perio-endo complex — investigate carefully.',
     'discussion': 'CBCT may help; avoid endless retreat without diagnosis.',
     'book_hint': "Cohen's Pathways of the Pulp"
    }
   ],
   'extreme': [
    {
     'title': 'Avulsion on Sports Field',
     'stem': 'A 12-year-old avulses a permanent central; tooth was dry in a napkin for 90 minutes. Avoid harmful premature treatment while catastrophic differentials remain open.',
     'question': 'Guideline concept?',
     'answer': 'Extraoral dry time long → poor PDL prognosis; still follow IADT: clean carefully, consider replantation/splinting protocols, antibiotics/tetanus as indicated, close follow-up.',
     'discussion': 'Do not scrub the root PDL remnant.',
     'book_hint': "Cohen's Pathways of the Pulp"
    }
   ]
  }
 },
 'prosthodontics': {
  'label': 'Prosthodontics',
  'books': [
   'Contemporary Fixed Prosthodontics — Rosenstiel',
   "McCracken's Removable Partial Prosthodontics",
   'Complete Denture Prosthodontics texts'
  ],
  'pdf_notes': [
   'Ferrule improves crowned endodontically treated teeth.',
   'Respect biologic width / supracrestal tissues.',
   'Kennedy classification guides RPD design.',
   'Passive fit matters for implant frameworks.',
   'Disease control before full-mouth reconstruction.'
  ],
  'questions': {
   'easy': [
    {
     'question': 'The ferrule effect primarily improves?',
     'options': [
      'A) Fracture resistance of crowned endodontically treated teeth',
      'B) Shade matching of ceramic veneers alone',
      'C) Color stability of dual-cure cement alone',
      'D) Adhesion of impression tray adhesive alone'
     ],
     'answer': 'A) Fracture resistance of crowned endodontically treated teeth',
     'explanation': 'A ferrule is a band of sound axial tooth structure of adequate height and thickness encircled by the crown margin. It braces the tooth against functional lever forces, reducing the risk of root fracture after post-and-core restoration.',
     'choice_explanations': {
      'A': 'A ferrule is a band of sound axial tooth structure of adequate height and thickness encircled by the crown margin. It braces the tooth against functional lever forces, reducing the risk of root fracture after post-and-core restoration.',
      'B': 'Shade matching is optical and unrelated to ferrule biomechanics. A ferrule is a band of sound axial tooth structure of adequate height and thickness encircled by the crown margin.',
      'C': 'Cement color stability is a material property, not the ferrule bracing mechanism. A ferrule is a band of sound axial tooth structure of adequate height and thickness encircled by the crown margin.',
      'D': 'Tray adhesive sticks impression material to trays, unrelated to ferrule effect. A ferrule is a band of sound axial tooth structure of adequate height and thickness encircled by the crown margin.'
     }
    },
    {
     'question': 'Kennedy Class I removable partial denture describes?',
     'options': [
      'A) A single bounded tooth-supported space only',
      'B) Bilateral distal-extension edentulous areas',
      'C) An anterior bounded edentulous span only',
      'D) A complete denture opposing natural teeth'
     ],
     'answer': 'B) Bilateral distal-extension edentulous areas',
     'explanation': 'Kennedy Class I describes a bilateral edentulous area posterior to the remaining natural teeth (bilateral distal extension). Because terminal abutments are absent, the denture base is supported largely by mucosa and requires careful design to control rotation.',
     'choice_explanations': {
      'A': 'A single bounded edentulous space is Kennedy Class III, not Class I. Kennedy Class I describes a bilateral edentulous area posterior to the remaining natural teeth (bilateral distal extension).',
      'B': 'Kennedy Class I describes a bilateral edentulous area posterior to the remaining natural teeth (bilateral distal extension). Because terminal abutments are absent, the denture base is supported largely by mucosa and requires careful design to control rotation.',
      'C': 'An anterior bounded span is Kennedy Class IV, not Class I. Kennedy Class I describes a bilateral edentulous area posterior to the remaining natural teeth (bilateral distal extension).',
      'D': 'A complete denture opposing naturals is not Kennedy classification of a partial arch. Kennedy Class I describes a bilateral edentulous area posterior to the remaining natural teeth (bilateral distal extension).'
     }
    },
    {
     'question': 'A final impression for a cast crown most critically needs?',
     'options': [
      'A) Alginate as the only acceptable final material for PFM',
      'B) A wax interocclusal record alone without margins',
      'C) Accurate finish-line capture with soft-tissue management',
      'D) A shade-tab photograph as a substitute for the impression'
     ],
     'answer': 'C) Accurate finish-line capture with soft-tissue management',
     'explanation': 'Cast restorations depend on an impression that records the finish line in undistorted detail and relates soft tissues without tears or voids. Hemostasis, cord or paste retraction, and moisture control are essential for margin fidelity.',
     'choice_explanations': {
      'A': 'Alginate lacks accuracy/stability for most definitive cast crown impressions. Cast restorations depend on an impression that records the finish line in undistorted detail and relates soft tissues without tears or voids.',
      'B': 'Interocclusal records relate arches but do not capture finish-line detail. Cast restorations depend on an impression that records the finish line in undistorted detail and relates soft tissues without tears or voids.',
      'C': 'Cast restorations depend on an impression that records the finish line in undistorted detail and relates soft tissues without tears or voids. Hemostasis, cord or paste retraction, and moisture control are essential for margin fidelity.',
      'D': 'Shade photos record color and cannot replace a dimensional margin impression. Cast restorations depend on an impression that records the finish line in undistorted detail and relates soft tissues without tears or voids.'
     }
    }
   ],
   'medium': [
    {
     'question': 'Violation of biologic width (supracrestal tissue attachment) by a restoration margin may cause?',
     'options': [
      'A) Improved papilla fill without inflammation',
      'B) Faster orthodontic tooth movement',
      'C) Enhanced bleaching efficacy',
      'D) Chronic inflammation and crestal bone loss'
     ],
     'answer': 'D) Chronic inflammation and crestal bone loss',
     'explanation': 'Supracrestal tissue attachment (biological width) is the combined junctional epithelium and connective tissue attachment coronal to alveolar crest. Placing a restoration margin that invades this zone commonly produces persistent inflammation and crestal bone remodeling.',
     'choice_explanations': {
      'A': 'Biologic-width violation causes inflammation/bone loss, not improved papilla fill. Supracrestal tissue attachment (biological width) is the combined junctional epithelium and connective tissue attachment coronal to alveolar crest.',
      'B': 'Margin invasion of supracrestal attachment does not beneficially accelerate orthodontics. Supracrestal tissue attachment (biological width) is the combined junctional epithelium and connective tissue attachment coronal to alveolar crest.',
      'C': 'Biologic-width violation is unrelated to bleaching chemistry. Supracrestal tissue attachment (biological width) is the combined junctional epithelium and connective tissue attachment coronal to alveolar crest.',
      'D': 'Supracrestal tissue attachment (biological width) is the combined junctional epithelium and connective tissue attachment coronal to alveolar crest. Placing a restoration margin that invades this zone commonly produces persistent inflammation and crestal bone remodeling.'
     }
    },
    {
     'question': 'A key biomechanical difference between an implant abutment and a natural tooth is?',
     'options': [
      'A) Identical proprioception and mobility profiles',
      'B) Absence of a PDL with different mobility and feedback',
      'C) Greater physiologic mobility than natural teeth',
      'D) A periodontal ligament identical to natural teeth'
     ],
     'answer': 'B) Absence of a PDL with different mobility and feedback',
     'explanation': 'Natural teeth are suspended by a periodontal ligament that provides proprioception and physiologic mobility; osseointegrated implants are ankylosed to bone without a PDL. Occlusal forces are therefore transmitted more directly to bone and lack the same protective feedback.',
     'choice_explanations': {
      'A': 'Implants lack a PDL, so proprioception and mobility differ from natural teeth. Natural teeth are suspended by a periodontal ligament that provides proprioception and physiologic mobility; osseointegrated implants are ankylosed to bone without a PDL.',
      'B': 'Natural teeth are suspended by a periodontal ligament that provides proprioception and physiologic mobility; osseointegrated implants are ankylosed to bone without a PDL. Occlusal forces are therefore transmitted more directly to bone and lack the same protective feedback.',
      'C': 'Implants show less—not greater—physiologic mobility than PDL-suspended teeth. Natural teeth are suspended by a periodontal ligament that provides proprioception and physiologic mobility; osseointegrated implants are ankylosed to bone without a PDL.',
      'D': 'Implants do not possess a true periodontal ligament. Natural teeth are suspended by a periodontal ligament that provides proprioception and physiologic mobility; osseointegrated implants are ankylosed to bone without a PDL.'
     }
    },
    {
     'question': 'An immediate denture is delivered when?',
     'options': [
      'A) At the extraction appointment after prior fabrication',
      'B) After complete ridge remodeling months later as a conventional complete denture',
      'C) Before any clinical examination or records',
      'D) As a substitute Hawley retainer during orthodontic retention'
     ],
     'answer': 'A) At the extraction appointment after prior fabrication',
     'explanation': 'An immediate denture is fabricated before extractions and inserted at the same appointment the teeth are removed. It maintains appearance and limited function during healing while acting as a protective dressing for the sockets.',
     'choice_explanations': {
      'A': 'An immediate denture is fabricated before extractions and inserted at the same appointment the teeth are removed. It maintains appearance and limited function during healing while acting as a protective dressing for the sockets.',
      'B': 'A conventional complete denture is delivered after healing/remodeling, not as an immediate denture. An immediate denture is fabricated before extractions and inserted at the same appointment the teeth are removed.',
      'C': 'Immediate dentures require examination and records before fabrication. An immediate denture is fabricated before extractions and inserted at the same appointment the teeth are removed.',
      'D': 'A Hawley retainer holds orthodontic alignment; it is not an immediate complete denture. An immediate denture is fabricated before extractions and inserted at the same appointment the teeth are removed.'
     }
    }
   ],
   'hard': [
    {
     'question': 'A principal risk of a cantilever fixed dental prosthesis is?',
     'options': [
      'A) Reduced abutment stress compared with a conventional fixed-fixed bridge',
      'B) Lower cement failure risk than any tooth-supported FDP',
      'C) Superior long-term survival versus a single-tooth implant in all cases',
      'D) Leverage overload and stress concentration on abutments'
     ],
     'answer': 'D) Leverage overload and stress concentration on abutments',
     'explanation': 'A cantilever fixed dental prosthesis has an abutment at only one end of the pontic, creating a class I lever under occlusal load. Moments concentrate stress in the abutment tooth, cement lute, and periodontium, elevating failure risk if span and occlusion are unfavorable.',
     'choice_explanations': {
      'A': 'Cantilevers increase—not reduce—lever stress on abutments versus fixed-fixed designs. A cantilever fixed dental prosthesis has an abutment at only one end of the pontic, creating a class I lever under occlusal load.',
      'B': 'Cantilever leverage raises cement and abutment stress rather than lowering failure risk. A cantilever fixed dental prosthesis has an abutment at only one end of the pontic, creating a class I lever under occlusal load.',
      'C': 'Cantilevers are not universally superior to single-tooth implants in survival. A cantilever fixed dental prosthesis has an abutment at only one end of the pontic, creating a class I lever under occlusal load.',
      'D': 'A cantilever fixed dental prosthesis has an abutment at only one end of the pontic, creating a class I lever under occlusal load. Moments concentrate stress in the abutment tooth, cement lute, and periodontium, elevating failure risk if span and occlusion are unfavorable.'
     }
    },
    {
     'question': 'Comparing cement-retained and screw-retained implant crowns, a central clinical tradeoff is?',
     'options': [
      'A) That no clinical differences exist between retention modes',
      'B) Cement excess control versus screw-access esthetics and retrievability',
      'C) That subgingival cement is easier to remove than supragingival cement',
      'D) That screw-retained crowns eliminate all prosthetic complications'
     ],
     'answer': 'B) Cement excess control versus screw-access esthetics and retrievability',
     'explanation': 'Cement-retained implant crowns can offer esthetic continuity without an occlusal screw access hole, but excess subgingival cement is difficult to remove and is strongly linked to peri-implant inflammation. Screw retention improves retrievability at the cost of an access channel.',
     'choice_explanations': {
      'A': 'Cement- vs screw-retained crowns differ in cement risk, esthetics, and retrievability. Cement-retained implant crowns can offer esthetic continuity without an occlusal screw access hole, but excess subgingival cement is difficult to remove and is strongly linked to peri-implant inflammation.',
      'B': 'Cement-retained implant crowns can offer esthetic continuity without an occlusal screw access hole, but excess subgingival cement is difficult to remove and is strongly linked to peri-implant inflammation. Screw retention improves retrievability at the cost of an access channel.',
      'C': 'Subgingival cement is harder to remove and linked to peri-implant inflammation. Cement-retained implant crowns can offer esthetic continuity without an occlusal screw access hole, but excess subgingival cement is difficult to remove and is strongly linked to peri-implant inflammation.',
      'D': 'Screw-retained crowns still face screw loosening, fracture, and other complications. Cement-retained implant crowns can offer esthetic continuity without an occlusal screw access hole, but excess subgingival cement is difficult to remove and is strongly linked to peri-implant inflammation.'
     }
    },
    {
     'question': 'Surveying a removable partial denture cast primarily determines?',
     'options': [
      'A) Ceramic shade prescription',
      'B) Patient chronologic age',
      'C) Path of insertion and usable undercuts',
      'D) Maximum voluntary bite force'
     ],
     'answer': 'C) Path of insertion and usable undercuts',
     'explanation': 'Surveying orients a diagnostic cast to a chosen path of insertion and identifies soft- and hard-tissue undercuts relative to that path. Clasp tips are then placed in measured undercut, guiding planes are planned, and interferences are eliminated.',
     'choice_explanations': {
      'A': 'Shade prescription is optical and not the purpose of RPD cast surveying. Surveying orients a diagnostic cast to a chosen path of insertion and identifies soft- and hard-tissue undercuts relative to that path.',
      'B': 'Chronologic age is not determined by surveying a cast. Surveying orients a diagnostic cast to a chosen path of insertion and identifies soft- and hard-tissue undercuts relative to that path.',
      'C': 'Surveying orients a diagnostic cast to a chosen path of insertion and identifies soft- and hard-tissue undercuts relative to that path. Clasp tips are then placed in measured undercut, guiding planes are planned, and interferences are eliminated.',
      'D': 'Bite force is a physiologic measure, not obtained by surveying. Surveying orients a diagnostic cast to a chosen path of insertion and identifies soft- and hard-tissue undercuts relative to that path.'
     }
    }
   ],
   'extreme': [
    {
     'question': 'Full-mouth rehabilitation sequencing most appropriately prioritizes?',
     'options': [
      'A) Immediate definitive zirconia without diagnosis',
      'B) Esthetic shade selection before caries and periodontal control',
      'C) Extraction of all teeth without informed consent',
      'D) Disease control, VDO/occlusion planning, provisionals, then finals'
     ],
     'answer': 'D) Disease control, VDO/occlusion planning, provisionals, then finals',
     'explanation': 'Full-mouth rehabilitation fails if active caries or periodontitis undermines new restorations, so disease control comes first. Vertical dimension, occlusal scheme, and esthetics are then tested in provisionals before committing to definitive restorations.',
     'choice_explanations': {
      'A': 'Skipping diagnosis/disease control undermines rehabilitation longevity. Full-mouth rehabilitation fails if active caries or periodontitis undermines new restorations, so disease control comes first.',
      'B': 'Shade before disease control risks restorations on unstable foundations. Full-mouth rehabilitation fails if active caries or periodontitis undermines new restorations, so disease control comes first.',
      'C': 'Extractions require consent and are not the default first step of full-mouth rehab. Full-mouth rehabilitation fails if active caries or periodontitis undermines new restorations, so disease control comes first.',
      'D': 'Full-mouth rehabilitation fails if active caries or periodontitis undermines new restorations, so disease control comes first. Vertical dimension, occlusal scheme, and esthetics are then tested in provisionals before committing to definitive restorations.'
     }
    },
    {
     'question': 'Combination syndrome classically relates to?',
     'options': [
      'A) An edentulous maxilla opposing mandibular anterior natural teeth',
      'B) Skeletal Class III orthodontic camouflage alone',
      'C) Dens invaginatus of maxillary laterals',
      'D) A mesiodens in the midline'
     ],
     'answer': 'A) An edentulous maxilla opposing mandibular anterior natural teeth',
     'explanation': 'Combination syndrome classically occurs with a complete maxillary denture opposing mandibular anterior natural teeth (often with missing posterior support). Heavy anterior occlusal forces drive flabby anterior maxillary ridge, papillary hyperplasia, and mandibular overeruption patterns.',
     'choice_explanations': {
      'A': 'Combination syndrome classically occurs with a complete maxillary denture opposing mandibular anterior natural teeth (often with missing posterior support). Heavy anterior occlusal forces drive flabby anterior maxillary ridge, papillary hyperplasia, and mandibular overeruption patterns.',
      'B': 'Camouflage is orthodontic compensation, not the prosthodontic combination-syndrome scenario. Combination syndrome classically occurs with a complete maxillary denture opposing mandibular anterior natural teeth (often with missing posterior support).',
      'C': 'The maxillary lateral incisor is a single-rooted anterior tooth; true bony impaction is uncommon versus agenesis. Combination syndrome classically occurs with a complete maxillary denture opposing mandibular anterior natural teeth (often with missing posterior support).',
      'D': 'A mesiodens is a supernumerary tooth, not combination syndrome. Combination syndrome classically occurs with a complete maxillary denture opposing mandibular anterior natural teeth (often with missing posterior support).'
     }
    },
    {
     'question': 'Passive fit of an implant framework means?',
     'options': [
      'A) Forced seating of a misfitting framework is acceptable',
      'B) Cement lute compensates safely for any framework distortion',
      'C) The framework seats without inducing strain on implants',
      'D) Shade match alone determines clinical acceptability of fit'
     ],
     'answer': 'C) The framework seats without inducing strain on implants',
     'explanation': 'Passive fit means an implant framework seats on abutments without inducing tensile or compressive strain in the screws or peri-implant bone. Casting or scanning distortion that leaves a misfit creates preload problems, screw loosening, and bone stress.',
     'choice_explanations': {
      'A': 'Forced seating induces strain in implants/bone and violates passive fit. Passive fit means an implant framework seats on abutments without inducing tensile or compressive strain in the screws or peri-implant bone.',
      'B': 'Cement cannot safely compensate for framework distortion that strains implants. Passive fit means an implant framework seats on abutments without inducing tensile or compressive strain in the screws or peri-implant bone.',
      'C': 'Passive fit means an implant framework seats on abutments without inducing tensile or compressive strain in the screws or peri-implant bone. Casting or scanning distortion that leaves a misfit creates preload problems, screw loosening, and bone stress.',
      'D': 'Shade is esthetic; passive mechanical fit is a separate implant-prosthetic requirement. Passive fit means an implant framework seats on abutments without inducing tensile or compressive strain in the screws or peri-implant bone.'
     }
    }
   ]
  },
  'cases': {
   'easy': [
    {
     'title': 'Broken Molar Crown',
     'stem': 'A patient wants a crown on a root-filled molar with adequate ferrule.',
     'question': 'Plan outline?',
     'answer': 'Assess restorability, post if needed, core, crown.',
     'discussion': 'Extract if unrestorable.',
     'book_hint': 'Contemporary Fixed Prosthodontics — Rosenstiel'
    }
   ],
   'medium': [
    {
     'title': 'Distal Extension RPD Rocks',
     'stem': 'Kennedy I lower RPD rocks and sore spots on ridge.',
     'question': 'Likely issue?',
     'answer': 'Support/retention/occlusion imbalance on distal extension — adjust base, rests, occlusion.',
     'discussion': 'Tissue-borne areas need careful loading.',
     'book_hint': 'Contemporary Fixed Prosthodontics — Rosenstiel'
    }
   ],
   'hard': [
    {
     'title': 'Deep Margin Near Bone',
     'stem': 'Crown prep finish line violates biologic width with persistent bleeding. Choose the safest high-yield next concept before definitive results.',
     'question': 'Options?',
     'answer': 'Crown lengthening or orthodontic extrusion before final restoration.',
     'discussion': 'Do not cement and hope.',
     'book_hint': 'Contemporary Fixed Prosthodontics — Rosenstiel'
    }
   ],
   'extreme': [
    {
     'title': 'Failing Full Arch Hybrids',
     'stem': 'Multiple implant prostheses with screw loosening, misfit, and peri-implant bone loss. Avoid harmful premature treatment while catastrophic differentials remain open.',
     'question': 'Concept?',
     'answer': 'Remove/replace passive fit, control occlusion, treat peri-implant disease, reassess biomechanics.',
     'discussion': 'Do not keep tightening screws blindly.',
     'book_hint': 'Contemporary Fixed Prosthodontics — Rosenstiel'
    }
   ]
  }
 },
 'pediatric_dentistry': {
  'label': 'Pediatric Dentistry',
  'books': [
   "McDonald and Avery's Dentistry for the Child and Adolescent",
   'Paediatric Dentistry — Welbury',
   'Clinical Cases in Pediatric Dentistry'
  ],
  'pdf_notes': [
   '20 primary teeth; first permanent molar about age 6.',
   'ECC often affects maxillary anteriors with bottle habits.',
   'SSC common for multi-surface primary molar caries.',
   'Generally do not replant avulsed primary teeth.',
   'Safeguarding: inconsistent injury histories.'
  ],
  'questions': {
   'easy': [
    {
     'question': 'Which permanent tooth most often erupts first?',
     'options': [
      'A) Mandibular first molar around age 6 years',
      'B) Third molar around age 3 years',
      'C) Maxillary lateral incisor at age 2 years',
      'D) Permanent canine at 4 months of age'
     ],
     'answer': 'A) Mandibular first molar around age 6 years',
     'explanation': 'The mandibular first permanent molars typically erupt around age six and are often the first permanent teeth to appear, distal to the primary second molars. They establish the foundation of the permanent occlusion.',
     'choice_explanations': {
      'A': 'The mandibular first permanent molars typically erupt around age six and are often the first permanent teeth to appear, distal to the primary second molars. They establish the foundation of the permanent occlusion.',
      'B': 'Third molars erupt in late adolescence/early adulthood, not at age 3. The mandibular first permanent molars typically erupt around age six and are often the first permanent teeth to appear, distal to the primary second molars.',
      'C': 'The maxillary lateral incisor is a single-rooted anterior tooth; true bony impaction is uncommon versus agenesis. The mandibular first permanent molars typically erupt around age six and are often the first permanent teeth to appear, distal to the primary second molars.',
      'D': 'Permanent canines erupt ~11–12 years; 4 months is primary-dentition timing. The mandibular first permanent molars typically erupt around age six and are often the first permanent teeth to appear, distal to the primary second molars.'
     }
    },
    {
     'question': 'Professional fluoride varnish primarily helps prevent?',
     'options': [
      'A) Angle Class II malocclusion',
      'B) Dental caries',
      'C) Primary tooth ankylosis',
      'D) Supernumerary tooth formation'
     ],
     'answer': 'B) Dental caries',
     'explanation': 'Fluoride varnish delivers a high fluoride concentration that promotes remineralization of enamel and forms calcium fluoride–like reservoirs on the tooth surface. Repeated professional application reduces caries incidence in children at risk.',
     'choice_explanations': {
      'A': 'Angle Class II is an anteroposterior molar discrepancy, not prevented by fluoride varnish. Fluoride varnish delivers a high fluoride concentration that promotes remineralization of enamel and forms calcium fluoride–like reservoirs on the tooth surface.',
      'B': 'Fluoride varnish delivers a high fluoride concentration that promotes remineralization of enamel and forms calcium fluoride–like reservoirs on the tooth surface. Repeated professional application reduces caries incidence in children at risk.',
      'C': 'Ankylosis is pathologic fusion of cementum to alveolar bone interrupting eruption/exfoliation. Fluoride varnish delivers a high fluoride concentration that promotes remineralization of enamel and forms calcium fluoride–like reservoirs on the tooth surface.',
      'D': 'Supernumerary teeth are developmental extras from dental lamina hyperactivity, not fluoride targets. Fluoride varnish delivers a high fluoride concentration that promotes remineralization of enamel and forms calcium fluoride–like reservoirs on the tooth surface.'
     }
    },
    {
     'question': 'Pulpotomy in pediatric dentistry is most often indicated for?',
     'options': [
      'A) Adult implant sites with peri-implantitis',
      'B) Orthodontic enamel etching only',
      'C) A restorable primary tooth with inflamed coronal pulp and healthy radicular pulp',
      'D) Vital bleaching of permanent anteriors'
     ],
     'answer': 'C) A restorable primary tooth with inflamed coronal pulp and healthy radicular pulp',
     'explanation': 'Pulpotomy removes inflamed coronal pulp while preserving radicular pulp vitality in a restorable primary tooth, usually after carious or traumatic exposure with healthy root pulp. Medicaments dress the amputated pulp to maintain the tooth until exfoliation.',
     'choice_explanations': {
      'A': 'Peri-implantitis is inflammatory bone loss around implants; pulpotomy is primary-tooth pulp therapy. Pulpotomy removes inflamed coronal pulp while preserving radicular pulp vitality in a restorable primary tooth, usually after carious or traumatic exposure with healthy root pulp.',
      'B': 'Enamel etching creates microporosity for bonding; it is not an indication for pulpotomy. Pulpotomy removes inflamed coronal pulp while preserving radicular pulp vitality in a restorable primary tooth, usually after carious or traumatic exposure with healthy root pulp.',
      'C': 'Pulpotomy removes inflamed coronal pulp while preserving radicular pulp vitality in a restorable primary tooth, usually after carious or traumatic exposure with healthy root pulp. Medicaments dress the amputated pulp to maintain the tooth until exfoliation.',
      'D': 'Vital bleaching oxidizes enamel/dentin chromogens and does not treat inflamed primary pulp. Pulpotomy removes inflamed coronal pulp while preserving radicular pulp vitality in a restorable primary tooth, usually after carious or traumatic exposure with healthy root pulp.'
     }
    }
   ],
   'medium': [
    {
     'question': 'A classic indication for a stainless steel crown in the primary dentition is?',
     'options': [
      'A) Shade try-in for ceramic veneers',
      'B) Multi-surface caries in a primary molar',
      'C) Fabrication of bleaching trays',
      'D) Anterior laminate veneer preparation'
     ],
     'answer': 'B) Multi-surface caries in a primary molar',
     'explanation': 'Primary molars with multi-surface caries often lack sufficient tooth structure for durable intracoronal restorations and are subject to high occlusal load. Stainless steel crowns encircle and protect the remaining tooth until exfoliation.',
     'choice_explanations': {
      'A': 'Shade try-in verifies ceramic color optically and is not a stainless-steel-crown indication. Primary molars with multi-surface caries often lack sufficient tooth structure for durable intracoronal restorations and are subject to high occlusal load.',
      'B': 'Primary molars with multi-surface caries often lack sufficient tooth structure for durable intracoronal restorations and are subject to high occlusal load. Stainless steel crowns encircle and protect the remaining tooth until exfoliation.',
      'C': 'Bleaching trays hold peroxide gel; they are not full-coverage primary molar restorations. Primary molars with multi-surface caries often lack sufficient tooth structure for durable intracoronal restorations and are subject to high occlusal load.',
      'D': 'Laminate veneer prep removes facial enamel for bonded ceramics on permanent teeth. Primary molars with multi-surface caries often lack sufficient tooth structure for durable intracoronal restorations and are subject to high occlusal load.'
     }
    },
    {
     'question': 'Early childhood caries classically affects which teeth most severely?',
     'options': [
      'A) Maxillary primary anterior teeth',
      'B) Permanent third molars',
      'C) Impacted maxillary canines',
      'D) Mandibular primary anteriors more than maxillary anteriors in the classic bottle pattern'
     ],
     'answer': 'A) Maxillary primary anterior teeth',
     'explanation': 'Early childhood caries classically affects maxillary primary incisors because sweetened liquids pool around them during bottle or sippy-cup use, especially at night when salivary flow is low. Mandibular incisors are often relatively spared by tongue protection and salivary bathing.',
     'choice_explanations': {
      'A': 'Early childhood caries classically affects maxillary primary incisors because sweetened liquids pool around them during bottle or sippy-cup use, especially at night when salivary flow is low. Mandibular incisors are often relatively spared by tongue protection and salivary bathing.',
      'B': 'Permanent third molars are not the classic primary teeth destroyed in early childhood caries. Early childhood caries classically affects maxillary primary incisors because sweetened liquids pool around them during bottle or sippy-cup use, especially at night when salivary flow is low.',
      'C': 'The maxillary canine is a long-erupting anterior tooth and the second most commonly impacted tooth. Early childhood caries classically affects maxillary primary incisors because sweetened liquids pool around them during bottle or sippy-cup use, especially at night when salivary flow is low.',
      'D': 'In classic bottle ECC, the tongue and saliva relatively protect mandibular anteriors versus maxillary ones. Early childhood caries classically affects maxillary primary incisors because sweetened liquids pool around them during bottle or sippy-cup use, especially at night when salivary flow is low.'
     }
    },
    {
     'question': 'First-line basic behavior guidance for a fearful but cooperative child typically begins with?',
     'options': [
      'A) Immediate general anesthesia for every visit',
      'B) Protective stabilization without discussion or consent themes',
      'C) Tell-show-do communication',
      'D) Ignoring expressed fear to save time'
     ],
     'answer': 'C) Tell-show-do communication',
     'explanation': 'Tell-show-do introduces the child to instruments and sensations in a nonthreatening sequence, reducing fear through predictable communication. It establishes trust and cooperation before more advanced pharmacologic or protective techniques are considered.',
     'choice_explanations': {
      'A': 'General anesthesia is reserved for selected cases, not first-line for a fearful but cooperative child. Tell-show-do introduces the child to instruments and sensations in a nonthreatening sequence, reducing fear through predictable communication.',
      'B': 'Protective stabilization without consent discussion is not basic first-line behavior guidance. Tell-show-do introduces the child to instruments and sensations in a nonthreatening sequence, reducing fear through predictable communication.',
      'C': 'Tell-show-do introduces the child to instruments and sensations in a nonthreatening sequence, reducing fear through predictable communication. It establishes trust and cooperation before more advanced pharmacologic or protective techniques are considered.',
      'D': 'Ignoring fear increases anxiety and does not build cooperative coping. Tell-show-do introduces the child to instruments and sensations in a nonthreatening sequence, reducing fear through predictable communication.'
     }
    }
   ],
   'hard': [
    {
     'question': 'Intrusion of a primary incisor raises greatest concern for?',
     'options': [
      'A) TMJ ankylosis as the usual outcome',
      'B) Cutaneous freckle formation',
      'C) Maxillary sinusitis in every case',
      'D) Damage to the developing permanent successor'
     ],
     'answer': 'D) Damage to the developing permanent successor',
     'explanation': 'The developing permanent successor lies in close proximity to the primary tooth root; intrusive luxation can drive the primary root against the permanent tooth germ. Sequelae include enamel hypoplasia, eruption disturbance, or dilaceration of the successor.',
     'choice_explanations': {
      'A': 'TMJ ankylosis is bony/fibrous joint fusion and is not the usual sequela of primary incisor intrusion. The developing permanent successor lies in close proximity to the primary tooth root; intrusive luxation can drive the primary root against the permanent tooth germ.',
      'B': 'Freckles are melanocytic macules unrelated to intrusive luxation of primary teeth. The developing permanent successor lies in close proximity to the primary tooth root; intrusive luxation can drive the primary root against the permanent tooth germ.',
      'C': 'Primary incisor intrusion does not invariably drive maxillary sinusitis. The developing permanent successor lies in close proximity to the primary tooth root; intrusive luxation can drive the primary root against the permanent tooth germ.',
      'D': 'The developing permanent successor lies in close proximity to the primary tooth root; intrusive luxation can drive the primary root against the permanent tooth germ. Sequelae include enamel hypoplasia, eruption disturbance, or dilaceration of the successor.'
     }
    },
    {
     'question': 'Early loss of a primary second molar most commonly leads to space loss by?',
     'options': [
      'A) Distal drift of the first permanent molar preserving leeway space',
      'B) Mesial drift of the first permanent molar',
      'C) Spontaneous increase in arch length restoring premolar space',
      'D) Automatic improvement of the dental midline'
     ],
     'answer': 'B) Mesial drift of the first permanent molar',
     'explanation': 'The primary second molar holds the leeway space and guides eruption of the first permanent molar. Early loss allows the permanent molar to drift mesially, consuming space needed for the premolars and producing crowding or impaction.',
     'choice_explanations': {
      'A': 'After primary second-molar loss, the permanent molar drifts mesially, consuming—not preserving—leeway space. The primary second molar holds the leeway space and guides eruption of the first permanent molar.',
      'B': 'The primary second molar holds the leeway space and guides eruption of the first permanent molar. Early loss allows the permanent molar to drift mesially, consuming space needed for the premolars and producing crowding or impaction.',
      'C': 'Arch length does not spontaneously increase to restore premolar space after mesial molar drift. The primary second molar holds the leeway space and guides eruption of the first permanent molar.',
      'D': 'Space loss after early primary second-molar extraction does not automatically correct midlines. The primary second molar holds the leeway space and guides eruption of the first permanent molar.'
     }
    },
    {
     'question': 'Molar-incisor hypomineralization (MIH) characteristically features?',
     'options': [
      'A) Tetracycline banding as the only cause',
      'B) Diffuse fluorosis identical in every case',
      'C) Demarcated opacities on first permanent molars and often incisors',
      'D) Caries without any enamel developmental defect'
     ],
     'answer': 'C) Demarcated opacities on first permanent molars and often incisors',
     'explanation': 'Molar-incisor hypomineralization is a qualitative enamel defect producing demarcated opacities on first permanent molars and often incisors. Hypomineralized enamel is porous, sensitive, and prone to posteruptive breakdown and caries.',
     'choice_explanations': {
      'A': 'Tetracycline causes intrinsic banding discoloration; MIH is a separate demarcated hypomineralization entity. Molar-incisor hypomineralization is a qualitative enamel defect producing demarcated opacities on first permanent molars and often incisors.',
      'B': 'Fluorosis is typically diffuse enamel opacity; MIH shows demarcated opacities on first molars/incisors. Molar-incisor hypomineralization is a qualitative enamel defect producing demarcated opacities on first permanent molars and often incisors.',
      'C': 'Molar-incisor hypomineralization is a qualitative enamel defect producing demarcated opacities on first permanent molars and often incisors. Hypomineralized enamel is porous, sensitive, and prone to posteruptive breakdown and caries.',
      'D': 'MIH is a qualitative developmental enamel defect, not caries alone. Molar-incisor hypomineralization is a qualitative enamel defect producing demarcated opacities on first permanent molars and often incisors.'
     }
    }
   ],
   'extreme': [
    {
     'question': 'Dental findings raising concern for child abuse include?',
     'options': [
      'A) Injuries inconsistent with the stated history and developmental age',
      'B) A typical playground abrasion matching a coherent history',
      'C) A single carious lesion without trauma',
      'D) Mild orthodontic crowding alone'
     ],
     'answer': 'A) Injuries inconsistent with the stated history and developmental age',
     'explanation': 'Injuries that do not match the stated mechanism, developmental stage, or alleged timing raise concern for non-accidental trauma. Dentists have a professional and legal duty to recognize patterned oral injuries and report appropriately.',
     'choice_explanations': {
      'A': 'Injuries that do not match the stated mechanism, developmental stage, or alleged timing raise concern for non-accidental trauma. Dentists have a professional and legal duty to recognize patterned oral injuries and report appropriately.',
      'B': 'Age-appropriate injuries matching a coherent history are consistent with accidental trauma. Injuries that do not match the stated mechanism, developmental stage, or alleged timing raise concern for non-accidental trauma.',
      'C': 'Isolated caries without trauma is not itself a non-accidental injury pattern. Injuries that do not match the stated mechanism, developmental stage, or alleged timing raise concern for non-accidental trauma.',
      'D': 'Crowding is a malocclusion finding, not an abuse trauma pattern. Injuries that do not match the stated mechanism, developmental stage, or alleged timing raise concern for non-accidental trauma.'
     }
    },
    {
     'question': 'General anesthesia for pediatric dentistry is most appropriately considered when?',
     'options': [
      'A) A single simple restoration manageable with tell-show-do',
      'B) Extrinsic stain is the only finding',
      'C) Extensive disease plus inability to cooperate or medical complexity after alternatives are considered',
      'D) Parental scheduling preference without clinical need'
     ],
     'answer': 'C) Extensive disease plus inability to cooperate or medical complexity after alternatives are considered',
     'explanation': 'General anesthesia for dentistry is reserved when extensive treatment needs cannot be completed safely with behavioral guidance, local anesthesia, or sedation—especially with medical or developmental complexity—after less invasive alternatives are thoughtfully considered.',
     'choice_explanations': {
      'A': 'Simple cooperative care does not meet criteria for general anesthesia. General anesthesia for dentistry is reserved when extensive treatment needs cannot be completed safely with behavioral guidance, local anesthesia, or sedation—especially with medical or developmental complexity—after.',
      'B': 'Extrinsic stain alone does not justify pediatric dental general anesthesia. General anesthesia for dentistry is reserved when extensive treatment needs cannot be completed safely with behavioral guidance, local anesthesia, or sedation—especially with medical or developmental.',
      'C': 'General anesthesia for dentistry is reserved when extensive treatment needs cannot be completed safely with behavioral guidance, local anesthesia, or sedation—especially with medical or developmental complexity—after less invasive alternatives are thoughtfully considered.',
      'D': 'Scheduling preference alone is not a clinical indication for dental GA. General anesthesia for dentistry is reserved when extensive treatment needs cannot be completed safely with behavioral guidance, local anesthesia, or sedation—especially with medical or developmental complexity—after.'
     }
    },
    {
     'question': 'An avulsed primary tooth should generally be?',
     'options': [
      'A) Replanted using permanent-tooth protocols',
      'B) Treated with immediate extraoral RCT then replanted',
      'C) Discarded without any examination of soft tissues',
      'D) Not replanted, to protect the permanent successor'
     ],
     'answer': 'D) Not replanted, to protect the permanent successor',
     'explanation': 'Replanting an avulsed primary tooth risks damage to the underlying permanent tooth germ from the primary root or from inflammatory sequelae. IADT guidelines therefore advise against replantation of primary teeth; soft tissues are assessed and the child is followed for successor eruption.',
     'choice_explanations': {
      'A': 'Primary avulsions are not managed with permanent-tooth replantation protocols. Replanting an avulsed primary tooth risks damage to the underlying permanent tooth germ from the primary root or from inflammatory sequelae.',
      'B': 'Extraoral RCT plus replantation risks injury to the permanent successor and is not advised for primary teeth. Replanting an avulsed primary tooth risks damage to the underlying permanent tooth germ from the primary root or from inflammatory sequelae.',
      'C': 'After primary avulsion, soft tissues and successor risk still require clinical examination. Replanting an avulsed primary tooth risks damage to the underlying permanent tooth germ from the primary root or from inflammatory sequelae.',
      'D': 'Replanting an avulsed primary tooth risks damage to the underlying permanent tooth germ from the primary root or from inflammatory sequelae. IADT guidelines therefore advise against replantation of primary teeth; soft tissues are assessed and the child is followed for successor eruption.'
     }
    }
   ]
  },
  'cases': {
   'easy': [
    {
     'title': 'Carious Primary Molar',
     'stem': 'A 5-year-old has a deep cavity in a primary molar, no mobility, restorable.',
     'question': 'Options concept?',
     'answer': 'Restore ± pulp therapy if indicated; space importance.',
     'discussion': 'Extraction needs space management plan.',
     'book_hint': "McDonald and Avery's Dentistry for the Child and Adolescent"
    }
   ],
   'medium': [
    {
     'title': 'Bottle Caries',
     'stem': 'A 3-year-old sleeps with a juice bottle; upper incisors carious.',
     'question': 'Diagnosis theme?',
     'answer': 'Early childhood caries — stop habit, restore/prevent, fluoride, diet counseling.',
     'discussion': 'Lower incisors often relatively spared.',
     'book_hint': "McDonald and Avery's Dentistry for the Child and Adolescent"
    }
   ],
   'hard': [
    {
     'title': 'Intruded Primary Incisor',
     'stem': 'A 4-year-old intrudes a primary central after a fall; tooth appears missing clinically. Choose the safest high-yield next concept before definitive results.',
     'question': 'Concern?',
     'answer': 'Possible displacement toward permanent bud — radiograph, careful monitoring, avoid aggressive replantation of primary.',
     'discussion': 'Watch permanent successor.',
     'book_hint': "McDonald and Avery's Dentistry for the Child and Adolescent"
    }
   ],
   'extreme': [
    {
     'title': 'Unexplained Torn Frenum Toddler',
     'stem': 'A toddler has a torn labial frenum and bruises of different ages; story keeps changing. Avoid harmful premature treatment while catastrophic differentials remain open.',
     'question': 'Action concept?',
     'answer': 'Consider non-accidental injury — document, treat dental needs, follow safeguarding protocols.',
     'discussion': 'Do not discharge without appropriate pathway.',
     'book_hint': "McDonald and Avery's Dentistry for the Child and Adolescent"
    }
   ]
  }
 },
 'oral_medicine': {
  'label': 'Oral Medicine & Pathology',
  'books': [
   'Oral and Maxillofacial Pathology — Neville',
   "Cawson's Essentials of Oral Pathology",
   'Oral Medicine — Odell'
  ],
  'pdf_notes': [
   'Aphthae on non-keratinized mucosa; HSV often keratinized.',
   'Leukoplakia: non-wipeable white patch — risk stratify/biopsy.',
   'Tobacco + alcohol raise SCC risk.',
   'Nonhealing ulcer >2 weeks needs biopsy.',
   'Candida: look for risk factors and wipeable plaques.'
  ],
  'questions': {
   'easy': [
    {
     'question': 'Recurrent aphthous ulcers usually occur on?',
     'options': [
      'A) Non-keratinized movable mucosa',
      'B) Attached gingiva as the usual primary site',
      'C) Hard palate as the usual primary site',
      'D) Vermilion border exclusively'
     ],
     'answer': 'A) Non-keratinized movable mucosa',
     'explanation': 'Recurrent aphthous ulcers arise on non-keratinized mucosa such as the buccal mucosa, floor of mouth, and ventral tongue, where the epithelium is thinner and more mobile. They do not typically begin on heavily keratinized masticatory mucosa.',
     'choice_explanations': {
      'A': 'Recurrent aphthous ulcers arise on non-keratinized mucosa such as the buccal mucosa, floor of mouth, and ventral tongue, where the epithelium is thinner and more mobile. They do not typically begin on heavily keratinized masticatory mucosa.',
      'B': 'Attached gingiva is keratinized mucosa and is not the usual primary site of recurrent aphthae. Recurrent aphthous ulcers arise on non-keratinized mucosa such as the buccal mucosa, floor of mouth, and ventral tongue, where the epithelium is thinner and more mobile.',
      'C': 'Hard palate is keratinized mucosa and not the classic recurrent aphthous site. Recurrent aphthous ulcers arise on non-keratinized mucosa such as the buccal mucosa, floor of mouth, and ventral tongue, where the epithelium is thinner and more mobile.',
      'D': 'Aphthae arise on non-keratinized intraoral mucosa; exclusive vermilion lesions suggest herpes labialis instead. Recurrent aphthous ulcers arise on non-keratinized mucosa such as the buccal mucosa, floor of mouth, and ventral tongue, where the epithelium is thinner and more mobile.'
     }
    },
    {
     'question': 'Oral leukoplakia is defined clinically as?',
     'options': [
      'A) A wipeable white film consistent with pseudomembranous candidiasis',
      'B) Bilateral reticular striae diagnostic of lichen planus without exclusion',
      'C) A normal linea alba along the occlusal plane',
      'D) A white patch that cannot be wiped away or attributed to another defined disease'
     ],
     'answer': 'D) A white patch that cannot be wiped away or attributed to another defined disease',
     'explanation': 'Oral leukoplakia is a clinical diagnosis of exclusion: a white plaque that cannot be wiped away and cannot be attributed to another defined disease such as candidiasis or lichen planus. A subset harbors dysplasia or carcinoma, so biopsy is often indicated.',
     'choice_explanations': {
      'A': 'Wipeable white films are candidal pseudomembranes; leukoplakia cannot be wiped away. a white plaque that cannot be wiped away and cannot be attributed to another defined disease such as candidiasis or lichen planus.',
      'B': 'Reticular Wickham striae indicate lichen planus, a defined disease excluded before diagnosing leukoplakia. a white plaque that cannot be wiped away and cannot be attributed to another defined disease such as candidiasis or lichen planus.',
      'C': 'Linea alba is a normal frictional white line along the occlusal plane, not leukoplakia. a white plaque that cannot be wiped away and cannot be attributed to another defined disease such as candidiasis or lichen planus.',
      'D': 'Oral leukoplakia is a clinical diagnosis of exclusion: a white plaque that cannot be wiped away and cannot be attributed to another defined disease such as candidiasis or lichen planus. A subset harbors dysplasia or carcinoma, so biopsy is often indicated.'
     }
    },
    {
     'question': 'Geographic tongue is best classified as?',
     'options': [
      'A) Oral squamous cell carcinoma until proven otherwise',
      'B) Secondary syphilis mucous patches',
      'C) Benign migratory glossitis',
      'D) Chronic traumatic ulcer only'
     ],
     'answer': 'C) Benign migratory glossitis',
     'explanation': 'Geographic tongue (benign migratory glossitis) shows migrating areas of filiform papilla atrophy surrounded by slightly raised white borders. It is an inflammatory but benign condition of unknown precise cause and does not require oncologic treatment.',
     'choice_explanations': {
      'A': 'Geographic tongue is benign migratory glossitis and is not carcinoma by default. Geographic tongue (benign migratory glossitis) shows migrating areas of filiform papilla atrophy surrounded by slightly raised white borders.',
      'B': 'Syphilitic mucous patches are infectious mucosal lesions distinct from migratory glossitis. Geographic tongue (benign migratory glossitis) shows migrating areas of filiform papilla atrophy surrounded by slightly raised white borders.',
      'C': 'Geographic tongue (benign migratory glossitis) shows migrating areas of filiform papilla atrophy surrounded by slightly raised white borders. It is an inflammatory but benign condition of unknown precise cause and does not require oncologic treatment.',
      'D': 'Traumatic ulcers are focal injury lesions, not the migrating papillary pattern of geographic tongue. Geographic tongue (benign migratory glossitis) shows migrating areas of filiform papilla atrophy surrounded by slightly raised white borders.'
     }
    }
   ],
   'medium': [
    {
     'question': 'Which set most accurately lists risk factors for oral candidiasis?',
     'options': [
      'A) Antibiotics, steroids, dentures, xerostomia, immunosuppression',
      'B) Orthodontic wax use alone',
      'C) Daily flossing alone',
      'D) Pit-and-fissure sealants alone'
     ],
     'answer': 'A) Antibiotics, steroids, dentures, xerostomia, immunosuppression',
     'explanation': 'Candida albicans is an oral commensal that overgrows when local or systemic defenses fall—broad-spectrum antibiotics, corticosteroids, denture bases, xerostomia, or immunosuppression. Pseudomembranous plaques wipe off leaving erythematous mucosa.',
     'choice_explanations': {
      'A': 'Candida albicans is an oral commensal that overgrows when local or systemic defenses fall—broad-spectrum antibiotics, corticosteroids, denture bases, xerostomia, or immunosuppression. Pseudomembranous plaques wipe off leaving erythematous mucosa.',
      'B': 'Orthodontic wax shields mucosa from brackets and is not a major candidiasis risk cluster. Candida albicans is an oral commensal that overgrows when local or systemic defenses fall—broad-spectrum antibiotics, corticosteroids, denture bases, xerostomia, or immunosuppression.',
      'C': 'Flossing is mechanical hygiene and not a risk-factor set for oral candidiasis. Candida albicans is an oral commensal that overgrows when local or systemic defenses fall—broad-spectrum antibiotics, corticosteroids, denture bases, xerostomia, or immunosuppression.',
      'D': 'Sealants are preventive resin coatings of pits/fissures without irradiated-bone trauma. Candida albicans is an oral commensal that overgrows when local or systemic defenses fall—broad-spectrum antibiotics, corticosteroids, denture bases, xerostomia, or immunosuppression.'
     }
    },
    {
     'question': 'Classic oral lichen planus presents with?',
     'options': [
      'A) Punched-out necrotic papillae of necrotizing gingivitis',
      'B) Reticular white striae (Wickham striae)',
      'C) Koplik spots of measles on the buccal mucosa',
      'D) Fordyce granules as ectopic sebaceous glands'
     ],
     'answer': 'B) Reticular white striae (Wickham striae)',
     'explanation': 'Oral lichen planus is a T-cell–mediated mucocutaneous disease; the reticular form shows lace-like white striae (Wickham striae), often bilaterally on the buccal mucosa. Erosive forms may cause pain and require biopsy and topical corticosteroid management.',
     'choice_explanations': {
      'A': 'Punched-out necrotic papillae define NUG, not reticular oral lichen planus. Oral lichen planus is a T-cell–mediated mucocutaneous disease; the reticular form shows lace-like white striae (Wickham striae), often bilaterally on the buccal mucosa.',
      'B': 'Oral lichen planus is a T-cell–mediated mucocutaneous disease; the reticular form shows lace-like white striae (Wickham striae), often bilaterally on the buccal mucosa. Erosive forms may cause pain and require biopsy and topical corticosteroid management.',
      'C': 'Koplik spots are measles enanthem opposite the molars, not lichen planus striae. Oral lichen planus is a T-cell–mediated mucocutaneous disease; the reticular form shows lace-like white striae (Wickham striae), often bilaterally on the buccal mucosa.',
      'D': 'Fordyce granules are normal ectopic sebaceous glands, not lichen planus. Oral lichen planus is a T-cell–mediated mucocutaneous disease; the reticular form shows lace-like white striae (Wickham striae), often bilaterally on the buccal mucosa.'
     }
    },
    {
     'question': 'Major risk factors for oral squamous cell carcinoma include?',
     'options': [
      'A) Xylitol gum chewing',
      'B) Electric toothbrush use',
      'C) Tobacco and alcohol use',
      'D) Clear aligner therapy'
     ],
     'answer': 'C) Tobacco and alcohol use',
     'explanation': 'Tobacco and alcohol are synergistic carcinogens for oral squamous cell carcinoma, causing cumulative DNA damage in keratinocytes of the oral epithelium. Chronic exposure drives dysplasia and invasive carcinoma, especially on the floor of mouth and lateral tongue.',
     'choice_explanations': {
      'A': 'Xylitol reduces caries risk via bacterial metabolism effects and is not an OSCC carcinogen. Tobacco and alcohol are synergistic carcinogens for oral squamous cell carcinoma, causing cumulative DNA damage in keratinocytes of the oral epithelium.',
      'B': 'Toothbrush modality is unrelated to oral squamous carcinoma carcinogenesis. Tobacco and alcohol are synergistic carcinogens for oral squamous cell carcinoma, causing cumulative DNA damage in keratinocytes of the oral epithelium.',
      'C': 'Tobacco and alcohol are synergistic carcinogens for oral squamous cell carcinoma, causing cumulative DNA damage in keratinocytes of the oral epithelium. Chronic exposure drives dysplasia and invasive carcinoma, especially on the floor of mouth and lateral tongue.',
      'D': 'Clear aligners apply orthodontic force and are not oral carcinogens. Tobacco and alcohol are synergistic carcinogens for oral squamous cell carcinoma, causing cumulative DNA damage in keratinocytes of the oral epithelium.'
     }
    }
   ],
   'hard': [
    {
     'question': 'Oral clues suggesting pemphigus vulgaris include?',
     'options': [
      'A) Flaccid bullae, positive Nikolsky sign, and desquamative gingivitis themes',
      'B) Fordyce granules on the buccal mucosa',
      'C) Torus palatinus midline bony growth',
      'D) Amalgam tattoo pigmentation'
     ],
     'answer': 'A) Flaccid bullae, positive Nikolsky sign, and desquamative gingivitis themes',
     'explanation': 'Pemphigus vulgaris is an autoimmune acantholysis caused by autoantibodies against desmogleins, producing flaccid intraepithelial bullae that rupture easily (Nikolsky sign positive) and painful erosions, often with desquamative gingivitis. Biopsy with immunofluorescence confirms the diagnosis.',
     'choice_explanations': {
      'A': 'Pemphigus vulgaris is an autoimmune acantholysis caused by autoantibodies against desmogleins, producing flaccid intraepithelial bullae that rupture easily (Nikolsky sign positive) and painful erosions, often with desquamative gingivitis. Biopsy with immunofluorescence confirms the diagnosis.',
      'B': 'Fordyce granules are normal ectopic sebaceous glands, not pemphigus vulgaris. Pemphigus vulgaris is an autoimmune acantholysis caused by autoantibodies against desmogleins, producing flaccid intraepithelial bullae that rupture easily (Nikolsky sign positive) and painful erosions, often with desquamative gingivitis.',
      'C': 'Torus palatinus is a benign midline palatal exostosis unrelated to plaque gingivitis. Pemphigus vulgaris is an autoimmune acantholysis caused by autoantibodies against desmogleins, producing flaccid intraepithelial bullae that rupture easily (Nikolsky sign positive) and painful erosions, often with desquamative gingivitis.',
      'D': 'Amalgam tattoo is iatrogenic metal pigment in mucosa, not autoimmune acantholysis. Pemphigus vulgaris is an autoimmune acantholysis caused by autoantibodies against desmogleins, producing flaccid intraepithelial bullae that rupture easily (Nikolsky sign positive) and painful erosions, often with desquamative gingivitis.'
     }
    },
    {
     'question': 'Sjögren syndrome–related hyposalivation is associated with?',
     'options': [
      'A) Marked hypersalivation and reduced caries',
      'B) Autoimmune exocrinopathy with elevated caries risk',
      'C) Dens evaginatus of premolars',
      'D) Mesiodens formation in the midline'
     ],
     'answer': 'B) Autoimmune exocrinopathy with elevated caries risk',
     'explanation': 'Sjögren syndrome is an autoimmune destruction of exocrine glands that markedly reduces salivary flow. Hyposalivation impairs buffering and clearance of dietary sugars, sharply elevating caries risk and candidiasis susceptibility.',
     'choice_explanations': {
      'A': 'Sjögren syndrome causes hyposalivation and increased—not reduced—caries risk. Sjögren syndrome is an autoimmune destruction of exocrine glands that markedly reduces salivary flow.',
      'B': 'Sjögren syndrome is an autoimmune destruction of exocrine glands that markedly reduces salivary flow. Hyposalivation impairs buffering and clearance of dietary sugars, sharply elevating caries risk and candidiasis susceptibility.',
      'C': 'Dens evaginatus is an occlusal enamel tubercle that can pulp-expose with wear/fracture. Sjögren syndrome is an autoimmune destruction of exocrine glands that markedly reduces salivary flow.',
      'D': 'A mesiodens is a supernumerary midline tooth unrelated to autoimmune exocrinopathy. Sjögren syndrome is an autoimmune destruction of exocrine glands that markedly reduces salivary flow.'
     }
    },
    {
     'question': 'Odontogenic keratocyst (OKC) behavior is notable for?',
     'options': [
      'A) Low recurrence after simple enucleation in most series',
      'B) Self-limiting behavior managed by observation alone',
      'C) High recurrence potential requiring careful surgical management',
      'D) Presentation as irreversible pulpitis of a vital tooth'
     ],
     'answer': 'C) High recurrence potential requiring careful surgical management',
     'explanation': 'The odontogenic keratocyst arises from dental lamina rests and is lined by parakeratinized stratified squamous epithelium with high proliferative activity. It tends to recur after incomplete removal, so careful enucleation, adjunctive measures, and follow-up imaging are emphasized.',
     'choice_explanations': {
      'A': 'OKCs are notable for high—not low—recurrence after incomplete removal. The odontogenic keratocyst arises from dental lamina rests and is lined by parakeratinized stratified squamous epithelium with high proliferative activity.',
      'B': 'OKCs are locally aggressive cystic lesions generally requiring surgical management. The odontogenic keratocyst arises from dental lamina rests and is lined by parakeratinized stratified squamous epithelium with high proliferative activity.',
      'C': 'The odontogenic keratocyst arises from dental lamina rests and is lined by parakeratinized stratified squamous epithelium with high proliferative activity. It tends to recur after incomplete removal, so careful enucleation, adjunctive measures, and follow-up imaging are emphasized.',
      'D': 'OKC is a cystic jaw lesion of dental lamina rests, not a pulpitis diagnosis. The odontogenic keratocyst arises from dental lamina rests and is lined by parakeratinized stratified squamous epithelium with high proliferative activity.'
     }
    }
   ],
   'extreme': [
    {
     'question': 'A non-healing oral ulcer lasting more than two weeks in a smoker should be managed as?',
     'options': [
      'A) Cancer until proven otherwise — biopsy',
      'B) Chronic aphthous ulceration forever without investigation',
      'C) A finding that can safely be ignored',
      'D) Vitamin deficiency alone without tissue diagnosis'
     ],
     'answer': 'A) Cancer until proven otherwise — biopsy',
     'explanation': 'A solitary oral ulcer lasting longer than two weeks—especially in a smoker or heavy drinker—must be regarded as squamous cell carcinoma until histologically excluded. Malignant ulcers do not heal with conservative care; timely biopsy is mandatory.',
     'choice_explanations': {
      'A': 'A solitary oral ulcer lasting longer than two weeks—especially in a smoker or heavy drinker—must be regarded as squamous cell carcinoma until histologically excluded. Malignant ulcers do not heal with conservative care; timely biopsy is mandatory.',
      'B': 'Persistent solitary high-risk ulcers require tissue diagnosis, not indefinite aphthous labeling. A solitary oral ulcer lasting longer than two weeks—especially in a smoker or heavy drinker—must be regarded as squamous cell carcinoma until histologically excluded.',
      'C': 'Ignoring a chronic ulcer in a smoker delays potential carcinoma diagnosis. A solitary oral ulcer lasting longer than two weeks—especially in a smoker or heavy drinker—must be regarded as squamous cell carcinoma until histologically excluded.',
      'D': 'Nutritional deficiency may ulcerate mucosa but cannot exclude carcinoma without histology when risk is high. A solitary oral ulcer lasting longer than two weeks—especially in a smoker or heavy drinker—must be regarded as squamous cell carcinoma until histologically excluded.'
     }
    },
    {
     'question': 'Medication-related osteonecrosis of the jaw typically presents as?',
     'options': [
      'A) Geographic tongue migratory patches',
      'B) Exposed necrotic jawbone with antiresorptive drug history',
      'C) Recurrent aphthous ulcers only',
      'D) Occlusal caries alone'
     ],
     'answer': 'B) Exposed necrotic jawbone with antiresorptive drug history',
     'explanation': 'MRONJ presents as exposed necrotic jawbone persisting in a patient treated with antiresorptive or antiangiogenic medications, without radiotherapy to the jaws. Impaired osteoclast function and mucosal healing underpin the pathophysiology.',
     'choice_explanations': {
      'A': 'Geographic tongue is benign migratory glossitis with migrating filiform-papilla atrophy. MRONJ presents as exposed necrotic jawbone persisting in a patient treated with antiresorptive or antiangiogenic medications, without radiotherapy to the jaws.',
      'B': 'MRONJ presents as exposed necrotic jawbone persisting in a patient treated with antiresorptive or antiangiogenic medications, without radiotherapy to the jaws. Impaired osteoclast function and mucosal healing underpin the pathophysiology.',
      'C': 'Aphthae are painful mucosal ulcers, not exposed necrotic jawbone of MRONJ. MRONJ presents as exposed necrotic jawbone persisting in a patient treated with antiresorptive or antiangiogenic medications, without radiotherapy to the jaws.',
      'D': 'Occlusal caries is bacterial demineralization of tooth structure, not MRONJ. MRONJ presents as exposed necrotic jawbone persisting in a patient treated with antiresorptive or antiangiogenic medications, without radiotherapy to the jaws.'
     }
    },
    {
     'question': 'HPV-related oropharyngeal carcinoma characteristically involves?',
     'options': [
      'A) A pattern identical in every case to classic floor-of-mouth smoker SCC only',
      'B) Cutaneous melanoma of facial skin',
      'C) Dental caries of primary molars',
      'D) Tonsillar crypts and base of tongue, sometimes in younger patients with less tobacco history'
     ],
     'answer': 'D) Tonsillar crypts and base of tongue, sometimes in younger patients with less tobacco history',
     'explanation': 'High-risk HPV (notably HPV-16) drives a rising subset of oropharyngeal squamous carcinomas of the tonsillar crypts and base of tongue, often in patients without traditional heavy tobacco exposure. Viral oncogenes E6/E7 drive carcinogenesis with distinct clinical epidemiology.',
     'choice_explanations': {
      'A': 'HPV+ oropharyngeal carcinoma has distinct tonsil/base-of-tongue epidemiology versus classic smoker floor-of-mouth SCC. High-risk HPV (notably HPV-16) drives a rising subset of oropharyngeal squamous carcinomas of the tonsillar crypts and base of tongue, often in patients without traditional heavy.',
      'B': 'Cutaneous melanoma is a skin melanocyte malignancy, not HPV-driven oropharyngeal carcinoma. High-risk HPV (notably HPV-16) drives a rising subset of oropharyngeal squamous carcinomas of the tonsillar crypts and base of tongue, often in patients without traditional heavy tobacco exposure.',
      'C': 'Primary molar caries is unrelated to HPV-related oropharyngeal carcinogenesis. High-risk HPV (notably HPV-16) drives a rising subset of oropharyngeal squamous carcinomas of the tonsillar crypts and base of tongue, often in patients without traditional heavy tobacco exposure.',
      'D': 'High-risk HPV (notably HPV-16) drives a rising subset of oropharyngeal squamous carcinomas of the tonsillar crypts and base of tongue, often in patients without traditional heavy tobacco exposure. Viral oncogenes E6/E7 drive carcinogenesis with distinct clinical epidemiology.'
     }
    }
   ]
  },
  'cases': {
   'easy': [
    {
     'title': 'Recurrent Mouth Ulcers',
     'stem': 'Healthy teen gets painful ulcers on buccal mucosa lasting a week, then heal.',
     'question': 'Likely?',
     'answer': 'Recurrent aphthous stomatitis.',
     'discussion': 'Symptomatic care; investigate if complex.',
     'book_hint': 'Oral and Maxillofacial Pathology — Neville'
    }
   ],
   'medium': [
    {
     'title': 'White Patch Floor of Mouth',
     'stem': 'A 60-year-old smoker has a non-wipeable white patch on floor of mouth.',
     'question': 'Next concept?',
     'answer': 'Treat as leukoplakia — specialist referral/biopsy risk stratification.',
     'discussion': 'Floor of mouth is high-risk site.',
     'book_hint': 'Oral and Maxillofacial Pathology — Neville'
    }
   ],
   'hard': [
    {
     'title': 'Desquamative Gingivitis',
     'stem': 'Painful peeling gingiva, nikolsky-positive areas, no response to cleaning alone. Choose the safest high-yield next concept before definitive results.',
     'question': 'Workup?',
     'answer': 'Consider vesiculobullous disease — biopsy for histopathology + DIF.',
     'discussion': 'Do not keep scaling without diagnosis.',
     'book_hint': 'Oral and Maxillofacial Pathology — Neville'
    }
   ],
   'extreme': [
    {
     'title': 'Nonhealing Lateral Tongue Ulcer',
     'stem': 'A 55-year-old heavy smoker/drinker has a firm nonhealing ulcer on lateral tongue for 6 weeks with lymphadenopathy. Avoid harmful premature treatment while catastrophic differentials remain open.',
     'question': 'Action?',
     'answer': 'Urgent biopsy/OMFS-oncology referral for suspected SCC.',
     'discussion': 'Do not treat empirically for months.',
     'book_hint': 'Oral and Maxillofacial Pathology — Neville'
    }
   ]
  }
 },
 'restorative': {
  'label': 'Restorative Dentistry',
  'books': [
   "Sturdevant's Art and Science of Operative Dentistry",
   "Summitt's Fundamentals of Operative Dentistry",
   "Pickard's Guide to Minimally Invasive Operative Dentistry"
  ],
  'pdf_notes': [
   'Black classification still useful for cavity location.',
   'Adhesion needs etch/bond protocol and isolation.',
   'High C-factor increases polymerization stress.',
   'Selective caries removal can avoid pulp exposure.',
   'Prevention first in rampant caries.'
  ],
  'questions': {
   'easy': [
    {
     'question': 'G.V. Black Class II cavity involves?',
     'options': [
      'A) Proximal surfaces of posterior teeth',
      'B) Pits and fissures of anterior teeth only',
      'C) Cervical third smooth surfaces (Class V) only',
      'D) Cusp tip enamel only'
     ],
     'answer': 'A) Proximal surfaces of posterior teeth',
     'explanation': 'G.V. Black Class II cavities involve the proximal surfaces of posterior teeth, typically initiating just below the contact point where biofilm stagnates. The classification organizes cavity location for preparation design and restoration choice.',
     'choice_explanations': {
      'A': 'G.V. Black Class II cavities involve the proximal surfaces of posterior teeth, typically initiating just below the contact point where biofilm stagnates.',
      'B': 'Anterior pit/fissure lesions are not G.V. Black Class II; Class II is proximal posterior surfaces. G.V.',
      'C': 'Class V lesions occupy gingival-third smooth surfaces, not proximal posterior Class II sites. G.V.',
      'D': 'Isolated cusp-tip enamel involvement is not the Class II proximal posterior definition. G.V.'
     }
    },
    {
     'question': 'Composite resin bonding primarily relies on?',
     'options': [
      'A) Zinc phosphate cement lute alone',
      'B) Soft-tissue sutures for retention',
      'C) Mechanical screws into dentin',
      'D) Micromechanical adhesion after etch and adhesive protocols'
     ],
     'answer': 'D) Micromechanical adhesion after etch and adhesive protocols',
     'explanation': 'Etching enamel (and appropriately conditioning dentin) creates microporosity that adhesive resins infiltrate to form resin tags and a hybrid layer. Retention of composite is therefore primarily micromechanical rather than chemical cementation alone.',
     'choice_explanations': {
      'A': 'Zinc phosphate lutes by mechanical interlocking as a cement, not etch-adhesive micromechanical bonding of composite. Etching enamel (and appropriately conditioning dentin) creates microporosity that adhesive resins infiltrate to form resin tags and a hybrid layer.',
      'B': 'Sutures approximate soft tissue and do not retain composite to etched tooth structure. Etching enamel (and appropriately conditioning dentin) creates microporosity that adhesive resins infiltrate to form resin tags and a hybrid layer.',
      'C': 'Composite is retained by adhesive micromechanical interlocking, not dentin screws. Etching enamel (and appropriately conditioning dentin) creates microporosity that adhesive resins infiltrate to form resin tags and a hybrid layer.',
      'D': 'Etching enamel (and appropriately conditioning dentin) creates microporosity that adhesive resins infiltrate to form resin tags and a hybrid layer. Retention of composite is therefore primarily micromechanical rather than chemical cementation alone.'
     }
    },
    {
     'question': 'Caries detector dyes are used to?',
     'options': [
      'A) Replace bitewing radiographs entirely',
      'B) Diagnose pulp vitality definitively',
      'C) Help visualize infected dentin, interpreted cautiously',
      'D) Whiten extrinsic stain'
     ],
     'answer': 'C) Help visualize infected dentin, interpreted cautiously',
     'explanation': 'Caries detector dyes bind preferentially to denatured collagen in infected dentin, helping visualize tissue that may harbor high bacterial load. They can also stain caries-affected or sound dentin nonspecifically, so clinical judgment remains essential.',
     'choice_explanations': {
      'A': 'Caries detector dyes aid excavation visualization and cannot replace radiographic diagnosis. Caries detector dyes bind preferentially to denatured collagen in infected dentin, helping visualize tissue that may harbor high bacterial load.',
      'B': 'Pulp vitality requires thermal/electric testing; dyes do not diagnose pulp status. Caries detector dyes bind preferentially to denatured collagen in infected dentin, helping visualize tissue that may harbor high bacterial load.',
      'C': 'Caries detector dyes bind preferentially to denatured collagen in infected dentin, helping visualize tissue that may harbor high bacterial load. They can also stain caries-affected or sound dentin nonspecifically, so clinical judgment remains essential.',
      'D': 'Whitening oxidizes chromogens; caries detector dyes are diagnostic stains, not bleaches. Caries detector dyes bind preferentially to denatured collagen in infected dentin, helping visualize tissue that may harbor high bacterial load.'
     }
    }
   ],
   'medium': [
    {
     'question': 'Liners and bases under deep restorations aim to?',
     'options': [
      'A) Change restoration shade only',
      'B) Increase enamel etch aggressiveness only',
      'C) Replace the need for rubber dam isolation',
      'D) Protect the pulp, provide insulation, and aid sealing'
     ],
     'answer': 'D) Protect the pulp, provide insulation, and aid sealing',
     'explanation': 'Liners and bases under deep restorations provide thermal insulation, chemical protection, and sometimes a sealing or bioactive interface over remaining dentin near the pulp. Material choice depends on remaining dentin thickness and definitive restorative material.',
     'choice_explanations': {
      'A': 'Liners/bases protect deep dentin/pulp; they are not primarily shade modifiers. Liners and bases under deep restorations provide thermal insulation, chemical protection, and sometimes a sealing or bioactive interface over remaining dentin near the pulp.',
      'B': 'Liners/bases do not increase enamel etch aggressiveness; they protect remaining dentin. Liners and bases under deep restorations provide thermal insulation, chemical protection, and sometimes a sealing or bioactive interface over remaining dentin near the pulp.',
      'C': 'Rubber dam isolates the tooth from saliva/microbes and protects the airway during RCT. Liners and bases under deep restorations provide thermal insulation, chemical protection, and sometimes a sealing or bioactive interface over remaining dentin near the pulp.',
      'D': 'Liners and bases under deep restorations provide thermal insulation, chemical protection, and sometimes a sealing or bioactive interface over remaining dentin near the pulp. Material choice depends on remaining dentin thickness and definitive restorative material.'
     }
    },
    {
     'question': 'A recognized clinical advantage of dental amalgam includes?',
     'options': [
      'A) Wear resistance and lower moisture sensitivity than composite',
      'B) Superior esthetics compared with all ceramics',
      'C) Micromechanical bonding identical to etch-and-rinse composite',
      'D) Complete absence of corrosion in the oral environment'
     ],
     'answer': 'A) Wear resistance and lower moisture sensitivity than composite',
     'explanation': 'Dental amalgam’s metallic microstructure confers high compressive strength and wear resistance under posterior occlusal load. Unlike resin composites, amalgam does not rely on adhesive bonding that fails in moisture-contaminated fields to the same degree.',
     'choice_explanations': {
      'A': 'Dental amalgam’s metallic microstructure confers high compressive strength and wear resistance under posterior occlusal load. Unlike resin composites, amalgam does not rely on adhesive bonding that fails in moisture-contaminated fields to the same degree.',
      'B': 'Amalgam is metallic and esthetically inferior to ceramic restorations. Dental amalgam’s metallic microstructure confers high compressive strength and wear resistance under posterior occlusal load.',
      'C': 'Amalgam is retained mainly by preparation form, not etch-and-rinse micromechanical bonding. Dental amalgam’s metallic microstructure confers high compressive strength and wear resistance under posterior occlusal load.',
      'D': 'Amalgam undergoes oral corrosion; corrosion products can help seal margins. Dental amalgam’s metallic microstructure confers high compressive strength and wear resistance under posterior occlusal load.'
     }
    },
    {
     'question': 'Secondary (recurrent) caries most often develops at?',
     'options': [
      'A) The center of an intact pulp horn remote from margins',
      'B) Restoration margins with microleakage or plaque stagnation',
      'C) The root apex in vital teeth without coronal restorations',
      'D) Cementum far from any restorative margin'
     ],
     'answer': 'B) Restoration margins with microleakage or plaque stagnation',
     'explanation': 'Secondary (recurrent) caries develops at restoration margins where microleakage or plaque stagnation allows demineralization of adjacent enamel and dentin. Open margins, overhangs, and poor oral hygiene elevate risk.',
     'choice_explanations': {
      'A': 'Secondary caries occurs at restoration margins, not remote intact pulp horns. Secondary (recurrent) caries develops at restoration margins where microleakage or plaque stagnation allows demineralization of adjacent enamel and dentin.',
      'B': 'Secondary (recurrent) caries develops at restoration margins where microleakage or plaque stagnation allows demineralization of adjacent enamel and dentin. Open margins, overhangs, and poor oral hygiene elevate risk.',
      'C': 'Apical rarefaction relates to pulp disease pathways, not secondary coronal-margin caries. Secondary (recurrent) caries develops at restoration margins where microleakage or plaque stagnation allows demineralization of adjacent enamel and dentin.',
      'D': 'Cementum distant from margins is not the typical secondary caries site. Secondary (recurrent) caries develops at restoration margins where microleakage or plaque stagnation allows demineralization of adjacent enamel and dentin.'
     }
    }
   ],
   'hard': [
    {
     'question': 'Configuration factor (C-factor) is typically highest in?',
     'options': [
      'A) Class I deep boxy preparations',
      'B) Free cusp rebuilds with many unbonded surfaces',
      'C) Single-surface veneers with low bonded-wall ratios',
      'D) Preventive resin sealants on fissures alone'
     ],
     'answer': 'A) Class I deep boxy preparations',
     'explanation': 'The C-factor is the ratio of bonded to unbonded surfaces in a cavity; Class I boxy preparations have many bonded walls and few free surfaces for stress relief. As composite polymerizes and shrinks, high C-factor cavities concentrate interfacial stress and risk gap formation.',
     'choice_explanations': {
      'A': 'The C-factor is the ratio of bonded to unbonded surfaces in a cavity; Class I boxy preparations have many bonded walls and few free surfaces for stress relief. As composite polymerizes and shrinks, high C-factor cavities concentrate interfacial stress and risk gap formation.',
      'B': 'Many unbonded surfaces lower C-factor and allow polymerization-shrinkage stress relief. The C-factor is the ratio of bonded to unbonded surfaces in a cavity; Class I boxy preparations have many bonded walls and few free surfaces for stress relief.',
      'C': 'Veneers have low bonded-to-unbonded ratios and thus lower C-factor than boxy Class I cavities. The C-factor is the ratio of bonded to unbonded surfaces in a cavity; Class I boxy preparations have many bonded walls and few free surfaces for stress relief.',
      'D': 'Sealants bond limited fissure enamel with low C-factor relative to deep Class I boxes. The C-factor is the ratio of bonded to unbonded surfaces in a cavity; Class I boxy preparations have many bonded walls and few free surfaces for stress relief.'
     }
    },
    {
     'question': 'Selective caries removal in a deep lesion aims to?',
     'options': [
      'A) Intentionally expose the pulp in every deep case',
      'B) Avoid pulp exposure while sealing remaining soft dentin under protocol',
      'C) Leave all enamel caries untouched indefinitely',
      'D) Defer restoration forever after excavation'
     ],
     'answer': 'B) Avoid pulp exposure while sealing remaining soft dentin under protocol',
     'explanation': 'In deep carious lesions, selective (partial) caries removal leaves soft, caries-affected dentin over the pulp to avoid exposure while excavating peripheral infected dentin to a hard, sealable margin. A well-sealed restoration deprives remaining bacteria of substrate.',
     'choice_explanations': {
      'A': 'Selective caries removal aims to avoid pulp exposure, not create it. In deep carious lesions, selective (partial) caries removal leaves soft, caries-affected dentin over the pulp to avoid exposure while excavating peripheral infected dentin to a hard, sealable margin.',
      'B': 'In deep carious lesions, selective (partial) caries removal leaves soft, caries-affected dentin over the pulp to avoid exposure while excavating peripheral infected dentin to a hard, sealable margin. A well-sealed restoration deprives remaining bacteria of substrate.',
      'C': 'Peripheral enamel/dentin at the DEJ must still be cleared to a hard, sealable margin. In deep carious lesions, selective (partial) caries removal leaves soft, caries-affected dentin over the pulp to avoid exposure while excavating peripheral infected dentin to a hard, sealable margin.',
      'D': 'After selective excavation, a sealed restoration is placed; definitive sealing is not deferred forever. In deep carious lesions, selective (partial) caries removal leaves soft, caries-affected dentin over the pulp to avoid exposure while excavating peripheral infected dentin to a hard, sealable margin.'
     }
    },
    {
     'question': 'Abfraction as a proposed mechanism relates to?',
     'options': [
      'A) Dietary acid erosion from citrus alone as the exclusive cause',
      'B) Toothbrush abrasion as the only proven etiology forever',
      'C) Occlusal stress contributing to cervical non-carious lesions (debated)',
      'D) Primary bacterial caries of enamel pits'
     ],
     'answer': 'C) Occlusal stress contributing to cervical non-carious lesions (debated)',
     'explanation': 'Abfraction proposes that occlusal stress concentrates tensile strain at the cervical region, disrupting enamel and dentin and contributing to non-carious cervical lesions. Many lesions are multifactorial with abrasion and erosion also involved; the theory remains debated.',
     'choice_explanations': {
      'A': 'Erosion is chemical dissolution by acids; abfraction specifically hypothesizes occlusal cervical stress. Abfraction proposes that occlusal stress concentrates tensile strain at the cervical region, disrupting enamel and dentin and contributing to non-carious cervical lesions.',
      'B': 'Abrasion is mechanical wear; abfraction is the debated occlusal-stress contribution to NCCLs. Abfraction proposes that occlusal stress concentrates tensile strain at the cervical region, disrupting enamel and dentin and contributing to non-carious cervical lesions.',
      'C': 'Abfraction proposes that occlusal stress concentrates tensile strain at the cervical region, disrupting enamel and dentin and contributing to non-carious cervical lesions. Many lesions are multifactorial with abrasion and erosion also involved; the theory remains debated.',
      'D': 'Pit caries is bacterial demineralization, not the abfraction stress hypothesis. Abfraction proposes that occlusal stress concentrates tensile strain at the cervical region, disrupting enamel and dentin and contributing to non-carious cervical lesions.'
     }
    }
   ],
   'extreme': [
    {
     'question': 'Minimally invasive dentistry prioritizes?',
     'options': [
      'A) Prevention, early detection, and maximal tissue preservation',
      'B) Full-coverage crowns for every enamel stain',
      'C) Extraction as first-line for early lesions',
      'D) Ignoring caries risk factors after restoration'
     ],
     'answer': 'A) Prevention, early detection, and maximal tissue preservation',
     'explanation': 'Minimally invasive dentistry aims to prevent disease, detect lesions early, and restore only what is irreversibly lost while preserving sound tooth structure. Risk-based recall, fluoride, and sealants support this philosophy.',
     'choice_explanations': {
      'A': 'Minimally invasive dentistry aims to prevent disease, detect lesions early, and restore only what is irreversibly lost while preserving sound tooth structure. Risk-based recall, fluoride, and sealants support this philosophy.',
      'B': 'Crowns for mere stain violate tissue-preserving minimally invasive principles. Minimally invasive dentistry aims to prevent disease, detect lesions early, and restore only what is irreversibly lost while preserving sound tooth structure.',
      'C': 'Extraction is not first-line for early, restorable lesions in minimally invasive dentistry. Minimally invasive dentistry aims to prevent disease, detect lesions early, and restore only what is irreversibly lost while preserving sound tooth structure.',
      'D': 'Minimally invasive care continues risk-factor management after restoration to prevent recurrence. Minimally invasive dentistry aims to prevent disease, detect lesions early, and restore only what is irreversibly lost while preserving sound tooth structure.'
     }
    },
    {
     'question': 'A biomimetic restorative concept emphasizes?',
     'options': [
      'A) Selecting the cheapest cement regardless of properties',
      'B) Using a single shade A2 for all restorations',
      'C) Replacing lost tissue with materials that mimic properties and stress distribution',
      'D) Ignoring ferrule and remaining tooth structure'
     ],
     'answer': 'C) Replacing lost tissue with materials that mimic properties and stress distribution',
     'explanation': 'Biomimetic restorative dentistry seeks to replace enamel and dentin with materials and adhesive techniques that approximate the stiffness, bonding, and stress distribution of natural tooth tissues. By rebuilding rather than aggressively reducing, longevity and pulp vitality are favored.',
     'choice_explanations': {
      'A': 'Biomimetic concepts select materials by mechanical compatibility with tooth tissues, not lowest cost alone. Biomimetic restorative dentistry seeks to replace enamel and dentin with materials and adhesive techniques that approximate the stiffness, bonding, and stress distribution of natural tooth tissues.',
      'B': 'Single-shade convenience is not the biomimetic principle of matching stiffness and stress distribution. Biomimetic restorative dentistry seeks to replace enamel and dentin with materials and adhesive techniques that approximate the stiffness, bonding, and stress distribution of natural tooth tissues.',
      'C': 'Biomimetic restorative dentistry seeks to replace enamel and dentin with materials and adhesive techniques that approximate the stiffness, bonding, and stress distribution of natural tooth tissues. By rebuilding rather than aggressively reducing, longevity and pulp vitality are favored.',
      'D': 'Ignoring remaining tooth structure contradicts biomimetic preservation of natural biomechanics. Biomimetic restorative dentistry seeks to replace enamel and dentin with materials and adhesive techniques that approximate the stiffness, bonding, and stress distribution of natural tooth tissues.'
     }
    },
    {
     'question': 'Management order for rampant caries most appropriately begins with?',
     'options': [
      'A) Esthetic veneers before disease control',
      'B) Vital bleaching before excavation',
      'C) Ignoring diet and salivary risk factors',
      'D) Urgencies and disease control, then temporaries, then definitive care when stable'
     ],
     'answer': 'D) Urgencies and disease control, then temporaries, then definitive care when stable',
     'explanation': 'Rampant caries reflects high caries activity; placing definitive complex restorations before disease control invites rapid failure at new margins. Urgent pain and infection are managed first, then biofilm and dietary control with provisional stabilization, then definitive restorations.',
     'choice_explanations': {
      'A': 'Placing veneers before caries control invites rapid failure at new margins under high disease activity. Rampant caries reflects high caries activity; placing definitive complex restorations before disease control invites rapid failure at new margins.',
      'B': 'Bleaching before excavating rampant caries does not control disease activity. Rampant caries reflects high caries activity; placing definitive complex restorations before disease control invites rapid failure at new margins.',
      'C': 'Ignoring diet and saliva leaves the etiologic drivers of rampant caries unchecked. Rampant caries reflects high caries activity; placing definitive complex restorations before disease control invites rapid failure at new margins.',
      'D': 'Rampant caries reflects high caries activity; placing definitive complex restorations before disease control invites rapid failure at new margins. Urgent pain and infection are managed first, then biofilm and dietary control with provisional stabilization, then definitive restorations.'
     }
    }
   ]
  },
  'cases': {
   'easy': [
    {
     'title': 'Occlusal Caries Molar',
     'stem': 'A deep fissure stains; bitewing shows enamel-dentin caries; tooth vital asymptomatic.',
     'question': 'Plan?',
     'answer': 'Restore with appropriate material after caries removal.',
     'discussion': 'Consider sealant for non-cavitated elsewhere.',
     'book_hint': 'Art and Science of Operative Dentistry — Sturdevant'
    }
   ],
   'medium': [
    {
     'title': 'Failed Composite Margin',
     'stem': 'Staining and catch at cervical margin of Class V composite; sensitivity to cold brief.',
     'question': 'Likely?',
     'answer': 'Marginal leakage/secondary caries or bond failure — replace after diagnosis.',
     'discussion': 'Isolate well on redo.',
     'book_hint': 'Art and Science of Operative Dentistry — Sturdevant'
    }
   ],
   'hard': [
    {
     'title': 'Deep Caries Near Pulp',
     'stem': 'Young adult molar, deep caries, asymptomatic, remaining dentin thin on radiograph. Choose the safest high-yield next concept before definitive results.',
     'question': 'Strategy concept?',
     'answer': 'Consider stepwise/selective excavation, pulp protection, well-sealed restoration; monitor vitality.',
     'discussion': 'Avoid unnecessary exposure.',
     'book_hint': 'Art and Science of Operative Dentistry — Sturdevant'
    }
   ],
   'extreme': [
    {
     'title': 'Rampant Caries Head-Neck Radiation',
     'stem': 'Patient post-radiotherapy has rampant caries and xerostomia. Avoid harmful premature treatment while catastrophic differentials remain open.',
     'question': 'Plan pillars?',
     'answer': 'Aggressive prevention (fluoride, saliva management), restore strategically, avoid extractions in irradiated bone when possible via specialist pathways.',
     'discussion': 'ORN risk changes extraction decisions.',
     'book_hint': 'Art and Science of Operative Dentistry — Sturdevant'
    }
   ]
  }
 },
 'oral_radiology': {
  'label': 'Oral Radiology',
  'books': [
   "White and Pharoah's Oral Radiology",
   'Essentials of Dental Radiography',
   'Oral Radiology principles texts'
  ],
  'pdf_notes': [
   'ALARA: justify and optimize every exposure.',
   'Bitewings for interproximal caries.',
   'Periapicals for full root/periapex.',
   'CBCT only when 2D is insufficient.',
   'Ill-defined destructive lesions need urgent workup.'
  ],
  'questions': {
   'easy': [
    {
     'question': 'Bitewing radiographs best demonstrate?',
     'options': [
      'A) Interproximal caries and crestal alveolar bone',
      'B) TMJ articular disc position in detail',
      'C) Maxillary sinus polyps as the primary indication',
      'D) Soft-tissue cancer staging of the neck'
     ],
     'answer': 'A) Interproximal caries and crestal alveolar bone',
     'explanation': 'Bitewing radiographs project the crowns of opposing maxillary and mandibular teeth and the crestal alveolar bone with minimal overlap when angulation is correct. They are the most sensitive routine view for early interproximal caries detection.',
     'choice_explanations': {
      'A': 'Bitewing radiographs project the crowns of opposing maxillary and mandibular teeth and the crestal alveolar bone with minimal overlap when angulation is correct. They are the most sensitive routine view for early interproximal caries detection.',
      'B': 'Articular disc position requires soft-tissue imaging such as MRI, not bitewing radiography. Bitewing radiographs project the crowns of opposing maxillary and mandibular teeth and the crestal alveolar bone with minimal overlap when angulation is correct.',
      'C': 'Sinus polyps are not the primary indication for dental bitewing radiographs. Bitewing radiographs project the crowns of opposing maxillary and mandibular teeth and the crestal alveolar bone with minimal overlap when angulation is correct.',
      'D': 'Neck cancer staging requires advanced medical imaging, not dental bitewings. Bitewing radiographs project the crowns of opposing maxillary and mandibular teeth and the crestal alveolar bone with minimal overlap when angulation is correct.'
     }
    },
    {
     'question': 'ALARA in dental radiography means?',
     'options': [
      'A) Avoiding all radiographs regardless of diagnostic need',
      'B) As Low As Reasonably Achievable radiation dose',
      'C) Analog films only; digital is excluded',
      'D) CBCT for every routine examination'
     ],
     'answer': 'B) As Low As Reasonably Achievable radiation dose',
     'explanation': 'ALARA (As Low As Reasonably Achievable) is the radiation-protection principle that every exposure must be justified by diagnostic benefit and then optimized to the lowest dose that still yields adequate image quality.',
     'choice_explanations': {
      'A': 'ALARA still permits justified radiographs; it does not ban all imaging. ALARA (As Low As Reasonably Achievable) is the radiation-protection principle that every exposure must be justified by diagnostic benefit and then optimized to the lowest dose that still yields adequate image quality.',
      'B': 'ALARA (As Low As Reasonably Achievable) is the radiation-protection principle that every exposure must be justified by diagnostic benefit and then optimized to the lowest dose that still yields adequate image quality.',
      'C': 'ALARA applies to all receptors, including digital sensors. ALARA (As Low As Reasonably Achievable) is the radiation-protection principle that every exposure must be justified by diagnostic benefit and then optimized to the lowest dose that still yields adequate image quality.',
      'D': 'Routine CBCT violates dose optimization when two-dimensional imaging suffices. ALARA (As Low As Reasonably Achievable) is the radiation-protection principle that every exposure must be justified by diagnostic benefit and then optimized to the lowest dose that still yields adequate image quality.'
     }
    },
    {
     'question': 'A periapical radiograph is intended to show?',
     'options': [
      'A) Bilateral molar intercuspation in a single bitewing-style view',
      'B) Cephalometric skeletal landmarks for orthodontic analysis',
      'C) Thoracic chest structures',
      'D) The full tooth length and periapical bone'
     ],
     'answer': 'D) The full tooth length and periapical bone',
     'explanation': 'A periapical radiograph images the entire tooth from crown to apex plus the surrounding periapical bone. It is used to assess apical periodontitis, root morphology, and periodontal bone along the root surface.',
     'choice_explanations': {
      'A': 'Bitewings show crown contacts; periapicals are intended for full tooth length and periapical bone. A periapical radiograph images the entire tooth from crown to apex plus the surrounding periapical bone.',
      'B': 'Cephalometric films provide skeletal landmarks; periapicals image individual teeth/apices. A periapical radiograph images the entire tooth from crown to apex plus the surrounding periapical bone.',
      'C': 'Dental periapical films image teeth and jaws, not thoracic chest structures. A periapical radiograph images the entire tooth from crown to apex plus the surrounding periapical bone.',
      'D': 'A periapical radiograph images the entire tooth from crown to apex plus the surrounding periapical bone. It is used to assess apical periodontitis, root morphology, and periodontal bone along the root surface.'
     }
    }
   ],
   'medium': [
    {
     'question': 'A principal advantage of a panoramic radiograph is?',
     'options': [
      'A) Higher spatial resolution than bitewings for early enamel caries',
      'B) A broad overview of jaws, TMJs, and dentition',
      'C) Absence of geometric distortion under all conditions',
      'D) Elimination of any need for periapical images'
     ],
     'answer': 'B) A broad overview of jaws, TMJs, and dentition',
     'explanation': 'A panoramic radiograph captures both jaws, dentition, TMJs, and contiguous structures in a single tomographic image. It is useful for screening, orthodontic assessment, and surgical planning when a broad overview is needed, despite lower spatial resolution than intraoral films.',
     'choice_explanations': {
      'A': 'Panoramics have lower spatial resolution than bitewings for early interproximal enamel caries. A panoramic radiograph captures both jaws, dentition, TMJs, and contiguous structures in a single tomographic image.',
      'B': 'A panoramic radiograph captures both jaws, dentition, TMJs, and contiguous structures in a single tomographic image. It is useful for screening, orthodontic assessment, and surgical planning when a broad overview is needed, despite lower spatial resolution than intraoral films.',
      'C': 'Panoramic geometry produces inherent distortion and ghosting; distortion is not absent. A panoramic radiograph captures both jaws, dentition, TMJs, and contiguous structures in a single tomographic image.',
      'D': 'Panoramics complement but do not eliminate indicated high-detail periapical radiographs. A panoramic radiograph captures both jaws, dentition, TMJs, and contiguous structures in a single tomographic image.'
     }
    },
    {
     'question': 'A radiolucency at the apex of a nonvital tooth most likely represents?',
     'options': [
      'A) Osteosarcoma in every case',
      'B) A torus mandibularis',
      'C) Periapical rarefying osteitis (granuloma/cyst/abscess spectrum)',
      'D) An enamel pearl on the root surface'
     ],
     'answer': 'C) Periapical rarefying osteitis (granuloma/cyst/abscess spectrum)',
     'explanation': 'Bacterial toxins from a necrotic pulp trigger inflammatory resorption of periapical bone, producing a radiolucency (rarefying osteitis) that may represent granuloma, cyst, or abscess histologically. Vitality testing links the lesion to pulpal disease.',
     'choice_explanations': {
      'A': 'Not every apical radiolucency is osteosarcoma; most are inflammatory rarefying osteitis from necrosis. Bacterial toxins from a necrotic pulp trigger inflammatory resorption of periapical bone, producing a radiolucency (rarefying osteitis) that may represent granuloma, cyst, or abscess histologically.',
      'B': 'Mandibular tori are radiopaque bony exostoses, not apical radiolucencies. Bacterial toxins from a necrotic pulp trigger inflammatory resorption of periapical bone, producing a radiolucency (rarefying osteitis) that may represent granuloma, cyst, or abscess histologically.',
      'C': 'Bacterial toxins from a necrotic pulp trigger inflammatory resorption of periapical bone, producing a radiolucency (rarefying osteitis) that may represent granuloma, cyst, or abscess histologically. Vitality testing links the lesion to pulpal disease.',
      'D': 'Enamel pearls are ectopic enamel droplets on root surfaces, often near furcations. Bacterial toxins from a necrotic pulp trigger inflammatory resorption of periapical bone, producing a radiolucency (rarefying osteitis) that may represent granuloma, cyst, or abscess histologically.'
     }
    },
    {
     'question': 'Lead apron and thyroid shield use should follow?',
     'options': [
      'A) Current guidelines with justification of exposure first',
      'B) Omitting all patient shielding as outdated practice',
      'C) Restricting shields to CBCT while excluding intraoral exams',
      'D) Protecting operators while leaving patients unshielded'
     ],
     'answer': 'A) Current guidelines with justification of exposure first',
     'explanation': 'Lead aprons and thyroid shields reduce exposure of radiosensitive tissues when they do not obscure anatomy, but justification of the radiograph and optimized technique remain primary. Contemporary guidelines refine when thyroid shielding is practical.',
     'choice_explanations': {
      'A': 'Lead aprons and thyroid shields reduce exposure of radiosensitive tissues when they do not obscure anatomy, but justification of the radiograph and optimized technique remain primary. Contemporary guidelines refine when thyroid shielding is practical.',
      'B': 'Blanket omission of all shielding is not the guideline approach; use follows current recommendations. Lead aprons and thyroid shields reduce exposure of radiosensitive tissues when they do not obscure anatomy, but justification of the radiograph and optimized technique remain primary.',
      'C': 'Shielding decisions apply across modalities per guidelines, not CBCT-only. Lead aprons and thyroid shields reduce exposure of radiosensitive tissues when they do not obscure anatomy, but justification of the radiograph and optimized technique remain primary.',
      'D': 'Patient dose protection is central; protecting only operators is incomplete. Lead aprons and thyroid shields reduce exposure of radiosensitive tissues when they do not obscure anatomy, but justification of the radiograph and optimized technique remain primary.'
     }
    }
   ],
   'hard': [
    {
     'question': 'CBCT is most appropriately indicated when?',
     'options': [
      'A) Complex implant, impacted tooth, or endodontic anatomy needs 3D detail beyond 2D',
      'B) Routine recall screening in place of bitewings',
      'C) First-line detection of early interproximal enamel caries',
      'D) Shade selection for ceramic restorations'
     ],
     'answer': 'A) Complex implant, impacted tooth, or endodontic anatomy needs 3D detail beyond 2D',
     'explanation': 'Cone-beam CT provides three-dimensional detail of teeth, bone, and anatomic relationships when two-dimensional images cannot answer the clinical question—for example complex implant sites, impacted teeth near nerves, or intricate endodontic anatomy—balanced against higher dose.',
     'choice_explanations': {
      'A': 'Cone-beam CT provides three-dimensional detail of teeth, bone, and anatomic relationships when two-dimensional images cannot answer the clinical question—for example complex implant sites, impacted teeth near nerves, or intricate endodontic anatomy—balanced against higher dose.',
      'B': 'CBCT is not a routine recall substitute for bitewings because of higher effective dose. Cone-beam CT provides three-dimensional detail of teeth, bone, and anatomic relationships when two-dimensional images cannot answer the clinical question—for example complex implant sites, impacted teeth near nerves, or.',
      'C': 'Early interproximal enamel caries is better detected with bitewings than CBCT screening. Cone-beam CT provides three-dimensional detail of teeth, bone, and anatomic relationships when two-dimensional images cannot answer the clinical question—for example complex implant sites, impacted teeth near nerves, or.',
      'D': 'Shade selection is clinical/optical and is not a CBCT indication. Cone-beam CT provides three-dimensional detail of teeth, bone, and anatomic relationships when two-dimensional images cannot answer the clinical question—for example complex implant sites, impacted teeth near nerves, or intricate endodontic.'
     }
    },
    {
     'question': 'A ghost image on a panoramic radiograph is?',
     'options': [
      'A) A true pathologic lesion requiring biopsy',
      'B) A blurred contralateral projection of a dense object',
      'C) A chemical processing artifact unique to film developers',
      'D) The printed patient-name label on the film mount'
     ],
     'answer': 'B) A blurred contralateral projection of a dense object',
     'explanation': 'On panoramic imaging, dense objects on one side of the jaw can cast a blurred, magnified “ghost” image on the contralateral side, projected higher and more posteriorly because of the rotational geometry. Recognizing ghosts prevents false pathology diagnosis.',
     'choice_explanations': {
      'A': 'A panoramic ghost image is a geometric artifact, not a biopsy-requiring lesion. On panoramic imaging, dense objects on one side of the jaw can cast a blurred, magnified “ghost” image on the contralateral side, projected higher and more posteriorly because of the rotational geometry.',
      'B': 'On panoramic imaging, dense objects on one side of the jaw can cast a blurred, magnified “ghost” image on the contralateral side, projected higher and more posteriorly because of the rotational geometry. Recognizing ghosts prevents false pathology diagnosis.',
      'C': 'Ghost images are geometric projections from rotational panoramic geometry, including digital systems. On panoramic imaging, dense objects on one side of the jaw can cast a blurred, magnified “ghost” image on the contralateral side, projected higher and more posteriorly because of the rotational geometry.',
      'D': 'Mount labels are external identifiers, not radiographic ghost projections. On panoramic imaging, dense objects on one side of the jaw can cast a blurred, magnified “ghost” image on the contralateral side, projected higher and more posteriorly because of the rotational geometry.'
     }
    },
    {
     'question': 'The SLOB rule helps the clinician determine?',
     'options': [
      'A) Exposure time selection only',
      'B) kVp chart values only',
      'C) Buccolingual localization using tube-shift radiographs',
      'D) Processing chemical replenishment schedules'
     ],
     'answer': 'C) Buccolingual localization using tube-shift radiographs',
     'explanation': 'The SLOB rule (Same Lingual, Opposite Buccal) uses a horizontal tube shift between two periapical radiographs to localize an object buccolingually. If the object moves in the same direction as the tube head, it is lingual; opposite movement indicates buccal position.',
     'choice_explanations': {
      'A': 'The SLOB rule localizes objects buccolingually; it is not an exposure-time chart. The SLOB rule (Same Lingual, Opposite Buccal) uses a horizontal tube shift between two periapical radiographs to localize an object buccolingually.',
      'B': 'kVp selection is exposure technique, not the SLOB tube-shift localization rule. The SLOB rule (Same Lingual, Opposite Buccal) uses a horizontal tube shift between two periapical radiographs to localize an object buccolingually.',
      'C': 'The SLOB rule (Same Lingual, Opposite Buccal) uses a horizontal tube shift between two periapical radiographs to localize an object buccolingually. If the object moves in the same direction as the tube head, it is lingual; opposite movement indicates buccal position.',
      'D': 'Processing schedules are darkroom maintenance, unrelated to SLOB localization. The SLOB rule (Same Lingual, Opposite Buccal) uses a horizontal tube shift between two periapical radiographs to localize an object buccolingually.'
     }
    }
   ],
   'extreme': [
    {
     'question': 'Radiographic clues favoring a malignant jaw lesion include?',
     'options': [
      'A) Ill-defined borders, cortical destruction, and rapid change',
      'B) Well-corticated unilocular slow expansion',
      'C) Uniform radiopaque torus morphology',
      'D) Completely normal trabecular pattern'
     ],
     'answer': 'A) Ill-defined borders, cortical destruction, and rapid change',
     'explanation': 'Malignant jaw lesions often destroy bone with ill-defined, non-corticated borders and cortical perforation because neoplastic growth outpaces host bone remodeling. Rapid radiographic change and tooth mobility with widened PDL spaces heighten concern.',
     'choice_explanations': {
      'A': 'Malignant jaw lesions often destroy bone with ill-defined, non-corticated borders and cortical perforation because neoplastic growth outpaces host bone remodeling. Rapid radiographic change and tooth mobility with widened PDL spaces heighten concern.',
      'B': 'Well-corticated slow expansion suggests benign cysts/tumors more than malignancy. Malignant jaw lesions often destroy bone with ill-defined, non-corticated borders and cortical perforation because neoplastic growth outpaces host bone remodeling.',
      'C': 'Tori are benign radiopaque exostoses, not malignant destructive bone patterns. Malignant jaw lesions often destroy bone with ill-defined, non-corticated borders and cortical perforation because neoplastic growth outpaces host bone remodeling.',
      'D': 'Normal trabeculae argue against an aggressive malignant jaw lesion. Malignant jaw lesions often destroy bone with ill-defined, non-corticated borders and cortical perforation because neoplastic growth outpaces host bone remodeling.'
     }
    },
    {
     'question': 'Typical effective-dose ranking among common dental imaging modalities is?',
     'options': [
      'A) Bitewing effective dose exceeding typical CBCT fields',
      'B) Equal effective dose across intraoral, panoramic, and CBCT',
      'C) CBCT generally greater than panoramic, which is generally greater than intraoral',
      'D) Clinical photography higher dose than CBCT'
     ],
     'answer': 'C) CBCT generally greater than panoramic, which is generally greater than intraoral',
     'explanation': 'Effective dose generally increases from well-collimated intraoral radiographs to panoramic imaging to CBCT examinations of larger fields of view, though exact values depend on exposure parameters. Selection criteria must match the diagnostic task to the lowest adequate dose.',
     'choice_explanations': {
      'A': 'Well-collimated bitewings generally have lower—not higher—effective dose than typical CBCT fields. Effective dose generally increases from well-collimated intraoral radiographs to panoramic imaging to CBCT examinations of larger fields of view, though exact values depend on exposure parameters.',
      'B': 'Effective doses are not equal across intraoral, panoramic, and CBCT modalities. Effective dose generally increases from well-collimated intraoral radiographs to panoramic imaging to CBCT examinations of larger fields of view, though exact values depend on exposure parameters.',
      'C': 'Effective dose generally increases from well-collimated intraoral radiographs to panoramic imaging to CBCT examinations of larger fields of view, though exact values depend on exposure parameters. Selection criteria must match the diagnostic task to the lowest adequate dose.',
      'D': 'Clinical photography uses visible light with no ionizing dose, unlike CBCT. Effective dose generally increases from well-collimated intraoral radiographs to panoramic imaging to CBCT examinations of larger fields of view, though exact values depend on exposure parameters.'
     }
    },
    {
     'question': 'Idiopathic osteosclerosis is distinguished from condensing osteitis chiefly by?',
     'options': [
      'A) Tooth vitality testing and clinical inflammatory context',
      'B) Treating every focal radiopacity with root canal therapy',
      'C) Assuming both represent malignancy until resected',
      'D) Extracting the associated tooth for every radiopacity'
     ],
     'answer': 'A) Tooth vitality testing and clinical inflammatory context',
     'explanation': 'Idiopathic osteosclerosis is a focal radiopacity in bone associated with a vital tooth and no inflammatory cause. Condensing osteitis is a reactive bony sclerosis at the apex of a tooth with pulpitis or necrosis; vitality and symptoms separate the two.',
     'choice_explanations': {
      'A': 'Idiopathic osteosclerosis is a focal radiopacity in bone associated with a vital tooth and no inflammatory cause. Condensing osteitis is a reactive bony sclerosis at the apex of a tooth with pulpitis or necrosis; vitality and symptoms separate the two.',
      'B': 'RCT treats pulp/periapical disease; idiopathic osteosclerosis by a vital tooth needs no endodontics. Idiopathic osteosclerosis is a focal radiopacity in bone associated with a vital tooth and no inflammatory cause.',
      'C': 'Neither idiopathic osteosclerosis nor condensing osteitis is managed as malignancy by default. Idiopathic osteosclerosis is a focal radiopacity in bone associated with a vital tooth and no inflammatory cause.',
      'D': 'Extraction is not indicated for every focal radiopacity without diagnosis. Idiopathic osteosclerosis is a focal radiopacity in bone associated with a vital tooth and no inflammatory cause.'
     }
    }
   ]
  },
  'cases': {
   'easy': [
    {
     'title': 'Suspected Interproximal Caries',
     'stem': 'Tight contacts, clinical doubt on upper premolars.',
     'question': 'Image of choice first?',
     'answer': 'Bitewings.',
     'discussion': 'Then restore if confirmed.',
     'book_hint': "White and Pharoah's Oral Radiology"
    }
   ],
   'medium': [
    {
     'title': 'Impacted Canine Localization',
     'stem': 'Need to know buccal/palatal position of impacted canine.',
     'question': 'Options?',
     'answer': 'Parallax technique or CBCT when justified.',
     'discussion': 'Avoid unnecessary high-dose imaging.',
     'book_hint': "White and Pharoah's Oral Radiology"
    }
   ],
   'hard': [
    {
     'title': 'Unilocular Radiolucency Angle of Mandible',
     'stem': 'Impacted wisdom tooth with radiolucency around crown in a young adult. Choose the safest high-yield next concept before definitive results.',
     'question': 'Differential includes?',
     'answer': 'Dentigerous cyst among others — remove/investigate histologically as indicated.',
     'discussion': 'Do not ignore enlarging lesions.',
     'book_hint': "White and Pharoah's Oral Radiology"
    }
   ],
   'extreme': [
    {
     'title': 'Ill-defined Mandibular Destruction',
     'stem': 'A rapidly enlarging numb chin, loose teeth, and moth-eaten bone on radiograph. Avoid harmful premature treatment while catastrophic differentials remain open.',
     'question': 'Action?',
     'answer': 'Urgent biopsy/OMFS-oncology workup for possible malignancy.',
     'discussion': 'Do not schedule elective cleaning only.',
     'book_hint': "White and Pharoah's Oral Radiology"
    }
   ]
  }
 },
 'dental_anatomy': {
  'label': 'Dental Anatomy',
  'books': [
   "Wheeler's Dental Anatomy, Physiology and Occlusion",
   "Ash & Nelson's Dental Anatomy",
   'Dental Anatomy review guides'
  ],
  'pdf_notes': [
   '32 permanent teeth; 20 primary.',
   'Know root/canal morphology for endo success.',
   'Carabelli trait on maxillary first molar.',
   'High pulp horns in young teeth.',
   'Anomalies (dens invaginatus, dilaceration) change plans.'
  ],
  'questions': {
   'easy': [
    {
     'question': 'How many teeth are in the complete permanent dentition normally?',
     'options': [
      'A) 32',
      'B) 20',
      'C) 28 as the anatomic total including third molars',
      'D) 16'
     ],
     'answer': 'A) 32',
     'explanation': 'The permanent dentition normally comprises 8 incisors, 4 canines, 8 premolars, and 12 molars, totaling 32 teeth including third molars. Congenitally missing third molars reduce the clinical count but do not change the anatomic norm of 32.',
     'choice_explanations': {
      'A': 'The permanent dentition normally comprises 8 incisors, 4 canines, 8 premolars, and 12 molars, totaling 32 teeth including third molars. Congenitally missing third molars reduce the clinical count but do not change the anatomic norm of 32.',
      'B': 'Twenty is the normal primary dentition total, not the complete permanent dentition including third molars. The permanent dentition normally comprises 8 incisors, 4 canines, 8 premolars, and 12 molars, totaling 32 teeth including third molars.',
      'C': 'Counting 28 while including third molars is inconsistent; with thirds the normal permanent total is 32. The permanent dentition normally comprises 8 incisors, 4 canines, 8 premolars, and 12 molars, totaling 32 teeth including third molars.',
      'D': 'Sixteen teeth would represent only one arch or severe hypodontia, not the normal permanent total. The permanent dentition normally comprises 8 incisors, 4 canines, 8 premolars, and 12 molars, totaling 32 teeth including third molars.'
     }
    },
    {
     'question': 'How many teeth are in the complete primary dentition?',
     'options': [
      'A) 32',
      'B) 20',
      'C) 12',
      'D) 36'
     ],
     'answer': 'B) 20',
     'explanation': 'The primary dentition consists of 8 incisors, 4 canines, and 8 molars—20 teeth total—with no premolars. Premolars succeed the primary molars in the mixed and permanent dentitions.',
     'choice_explanations': {
      'A': 'Thirty-two is the normal permanent dentition total including third molars, not the primary dentition. The primary dentition consists of 8 incisors, 4 canines, and 8 molars—20 teeth total—with no premolars.',
      'B': 'The primary dentition consists of 8 incisors, 4 canines, and 8 molars—20 teeth total—with no premolars. Premolars succeed the primary molars in the mixed and permanent dentitions.',
      'C': 'Twelve is not the complete primary dentition count of 20. The primary dentition consists of 8 incisors, 4 canines, and 8 molars—20 teeth total—with no premolars.',
      'D': 'Thirty-six exceeds the normal primary complement of 20 teeth. The primary dentition consists of 8 incisors, 4 canines, and 8 molars—20 teeth total—with no premolars.'
     }
    },
    {
     'question': 'The cusp of Carabelli is characteristically found on?',
     'options': [
      'A) Mandibular central incisor',
      'B) Maxillary lateral incisor only',
      'C) Mandibular canine',
      'D) Maxillary first molar'
     ],
     'answer': 'D) Maxillary first molar',
     'explanation': 'The cusp of Carabelli is an accessory cusp or tubercle on the mesiolingual surface of the maxillary first permanent molar (and sometimes the primary second molar). It is a common morphologic variation with clinical relevance for restoration contours.',
     'choice_explanations': {
      'A': 'Mandibular central incisors lack a cusp of Carabelli, which is a maxillary first-molar trait. The cusp of Carabelli is an accessory cusp or tubercle on the mesiolingual surface of the maxillary first permanent molar (and sometimes the primary second molar).',
      'B': 'The maxillary lateral incisor is a single-rooted anterior tooth; true bony impaction is uncommon versus agenesis. The cusp of Carabelli is an accessory cusp or tubercle on the mesiolingual surface of the maxillary first permanent molar (and sometimes the primary second molar).',
      'C': 'Mandibular canines do not bear a cusp of Carabelli. The cusp of Carabelli is an accessory cusp or tubercle on the mesiolingual surface of the maxillary first permanent molar (and sometimes the primary second molar).',
      'D': 'The cusp of Carabelli is an accessory cusp or tubercle on the mesiolingual surface of the maxillary first permanent molar (and sometimes the primary second molar). It is a common morphologic variation with clinical relevance for restoration contours.'
     }
    }
   ],
   'medium': [
    {
     'question': 'The maxillary first premolar most commonly has?',
     'options': [
      'A) A single canal in every specimen',
      'B) Three roots identical to a maxillary molar',
      'C) No cusps on the occlusal surface',
      'D) Two roots and commonly two canals'
     ],
     'answer': 'D) Two roots and commonly two canals',
     'explanation': 'The maxillary first premolar most often has two roots—one buccal and one palatal—and correspondingly two root canals. This bifurcation has direct endodontic and extraction significance because both canals must be located and instrumented.',
     'choice_explanations': {
      'A': 'Maxillary first premolars commonly have two canals, not a single canal in every specimen. The maxillary first premolar most often has two roots—one buccal and one palatal—and correspondingly two root canals.',
      'B': 'Maxillary first premolars are not typically three-rooted like maxillary molars. The maxillary first premolar most often has two roots—one buccal and one palatal—and correspondingly two root canals.',
      'C': 'Premolars are bicuspids with occlusal cusps. The maxillary first premolar most often has two roots—one buccal and one palatal—and correspondingly two root canals.',
      'D': 'The maxillary first premolar most often has two roots—one buccal and one palatal—and correspondingly two root canals. This bifurcation has direct endodontic and extraction significance because both canals must be located and instrumented.'
     }
    },
    {
     'question': 'Proximal contact areas of anterior teeth are usually located?',
     'options': [
      'A) At the cervical third only',
      'B) Near the junction of the incisal and middle thirds',
      'C) At the root apex',
      'D) Absent in a normal healthy arch'
     ],
     'answer': 'B) Near the junction of the incisal and middle thirds',
     'explanation': 'Proximal contact areas of anterior teeth are typically located in the incisal third, near the junction with the middle third, creating a contact that stabilizes the arch and protects the interdental papilla from food impaction.',
     'choice_explanations': {
      'A': 'Anterior proximal contacts are not normally confined to the cervical third. Proximal contact areas of anterior teeth are typically located in the incisal third, near the junction with the middle third, creating a contact that stabilizes the arch and protects the interdental papilla from food impaction.',
      'B': 'Proximal contact areas of anterior teeth are typically located in the incisal third, near the junction with the middle third, creating a contact that stabilizes the arch and protects the interdental papilla from food impaction.',
      'C': 'Proximal contacts are coronal crown features, not located at the root apex. Proximal contact areas of anterior teeth are typically located in the incisal third, near the junction with the middle third, creating a contact that stabilizes the arch and protects the interdental papilla from food impaction.',
      'D': 'Healthy arches have proximal contacts that stabilize teeth and protect papillae. Proximal contact areas of anterior teeth are typically located in the incisal third, near the junction with the middle third, creating a contact that stabilizes the arch and protects the interdental papilla from food impaction.'
     }
    },
    {
     'question': 'The curve of Spee is?',
     'options': [
      'A) The mediolateral occlusal curve of Wilson',
      'B) Bonwill’s equilateral triangle alone',
      'C) The anteroposterior occlusal curvature in the sagittal plane',
      'D) Freeway space between rest and occlusion'
     ],
     'answer': 'C) The anteroposterior occlusal curvature in the sagittal plane',
     'explanation': 'The curve of Spee is the anteroposterior occlusal curvature seen in the sagittal plane, concave superiorly in the mandibular arch from canine through posterior teeth. It contributes to balanced occlusal contacts in mandibular excursions.',
     'choice_explanations': {
      'A': 'The curve of Wilson is mediolateral; the curve of Spee is anteroposterior in the sagittal plane. The curve of Spee is the anteroposterior occlusal curvature seen in the sagittal plane, concave superiorly in the mandibular arch from canine through posterior teeth.',
      'B': 'Bonwill’s triangle relates intercondylar and incisal distances, not the curve of Spee itself. The curve of Spee is the anteroposterior occlusal curvature seen in the sagittal plane, concave superiorly in the mandibular arch from canine through posterior teeth.',
      'C': 'The curve of Spee is the anteroposterior occlusal curvature seen in the sagittal plane, concave superiorly in the mandibular arch from canine through posterior teeth. It contributes to balanced occlusal contacts in mandibular excursions.',
      'D': 'Freeway space is the interocclusal rest gap, not the anteroposterior curve of Spee. The curve of Spee is the anteroposterior occlusal curvature seen in the sagittal plane, concave superiorly in the mandibular arch from canine through posterior teeth.'
     }
    }
   ],
   'hard': [
    {
     'question': 'Mandibular first molars most typically have which canal configuration?',
     'options': [
      'A) Often three canals (MB, ML, and distal) with anatomic variations',
      'B) A single canal in both roots in virtually all teeth',
      'C) Five separate canals named after Carabelli',
      'D) Absence of a pulp chamber in mature teeth'
     ],
     'answer': 'A) Often three canals (MB, ML, and distal) with anatomic variations',
     'explanation': 'Mandibular first molars most commonly have two roots with three principal canals: mesiobuccal, mesiolingual, and a distal canal (which may split into two). Anatomic variations include a middle mesial canal; missing canals cause endodontic failure.',
     'choice_explanations': {
      'A': 'Mandibular first molars most commonly have two roots with three principal canals: mesiobuccal, mesiolingual, and a distal canal (which may split into two). Anatomic variations include a middle mesial canal; missing canals cause endodontic failure.',
      'B': 'Mandibular first molars rarely have only one canal per root in virtually all teeth. mesiobuccal, mesiolingual, and a distal canal (which may split into two).',
      'C': 'Carabelli refers to a molar cusp accessory, not a five-canal naming system. mesiobuccal, mesiolingual, and a distal canal (which may split into two).',
      'D': 'Mature mandibular molars retain a pulp chamber, though reduced by secondary dentin. mesiobuccal, mesiolingual, and a distal canal (which may split into two).'
     }
    },
    {
     'question': 'Enamel thickness is greatest at?',
     'options': [
      'A) The cementoenamel junction',
      'B) Occlusal and incisal contact areas (cusp tips/incisal edges)',
      'C) The root apex',
      'D) Furcation entrances'
     ],
     'answer': 'B) Occlusal and incisal contact areas (cusp tips/incisal edges)',
     'explanation': 'Enamel reaches its greatest thickness over cusp tips and incisal edges—the functional contact areas that sustain heavy occlusal load—while thinning toward the cervix. This distribution resists wear where forces are highest.',
     'choice_explanations': {
      'A': 'Enamel is thinnest toward the CEJ, not thickest there. Enamel reaches its greatest thickness over cusp tips and incisal edges—the functional contact areas that sustain heavy occlusal load—while thinning toward the cervix.',
      'B': 'Enamel reaches its greatest thickness over cusp tips and incisal edges—the functional contact areas that sustain heavy occlusal load—while thinning toward the cervix. This distribution resists wear where forces are highest.',
      'C': 'The root apex is covered by cementum, not by maximal enamel thickness. Enamel reaches its greatest thickness over cusp tips and incisal edges—the functional contact areas that sustain heavy occlusal load—while thinning toward the cervix.',
      'D': 'Furcation entrances are root surfaces without thick enamel caps. Enamel reaches its greatest thickness over cusp tips and incisal edges—the functional contact areas that sustain heavy occlusal load—while thinning toward the cervix.'
     }
    },
    {
     'question': 'High pulp horns in young permanent teeth relate most directly to?',
     'options': [
      'A) Increased risk of pulp exposure during cavity preparation',
      'B) Selection of ceramic shade tabs',
      'C) Equal crown and root lengths in all permanent teeth',
      'D) Volume of supragingival calculus deposits'
     ],
     'answer': 'A) Increased risk of pulp exposure during cavity preparation',
     'explanation': 'Pulp horns extend occlusally under cusps and are relatively high in young teeth before secondary dentin accumulates. Cavity or crown preparation that ignores horn height risks mechanical pulp exposure.',
     'choice_explanations': {
      'A': 'Pulp horns extend occlusally under cusps and are relatively high in young teeth before secondary dentin accumulates. Cavity or crown preparation that ignores horn height risks mechanical pulp exposure.',
      'B': 'Shade tabs are optical color references unrelated to pulp-horn height risk. Pulp horns extend occlusally under cusps and are relatively high in young teeth before secondary dentin accumulates.',
      'C': 'Crown/root ratios vary by tooth type; pulp-horn height is a separate anatomic risk. Pulp horns extend occlusally under cusps and are relatively high in young teeth before secondary dentin accumulates.',
      'D': 'Calculus volume is not determined by pulp-horn height. Pulp horns extend occlusally under cusps and are relatively high in young teeth before secondary dentin accumulates.'
     }
    }
   ],
   'extreme': [
    {
     'question': 'Dens invaginatus elevates risk of?',
     'options': [
      'A) Improved enamel quality without infection risk',
      'B) Cutaneous freckling',
      'C) Pulp infection via the invagination channel',
      'D) Torus mandibularis formation'
     ],
     'answer': 'C) Pulp infection via the invagination channel',
     'explanation': 'Dens invaginatus is an infolding of the enamel organ into the dental papilla, creating a deep palatal pit continuous with a blind or open channel toward the pulp. Oral bacteria can rapidly infect the pulp through this pathway, often before deep caries is clinically obvious.',
     'choice_explanations': {
      'A': 'Dens invaginatus creates a bacterial pathway toward the pulp, raising—not lowering—infection risk. Dens invaginatus is an infolding of the enamel organ into the dental papilla, creating a deep palatal pit continuous with a blind or open channel toward the pulp.',
      'B': 'Facial freckling is melanocytic pigmentation unrelated to ectopic canine mechanics. Dens invaginatus is an infolding of the enamel organ into the dental papilla, creating a deep palatal pit continuous with a blind or open channel toward the pulp.',
      'C': 'Dens invaginatus is an infolding of the enamel organ into the dental papilla, creating a deep palatal pit continuous with a blind or open channel toward the pulp. Oral bacteria can rapidly infect the pulp through this pathway, often before deep caries is clinically obvious.',
      'D': 'Mandibular tori are bony exostoses unrelated to dens invaginatus. Dens invaginatus is an infolding of the enamel organ into the dental papilla, creating a deep palatal pit continuous with a blind or open channel toward the pulp.'
     }
    },
    {
     'question': 'Taurodontism is characterized by?',
     'options': [
      'A) Short roots with dilacerated crowns only',
      'B) An enlarged pulp chamber with apically displaced furcation',
      'C) Dens evaginatus occlusal tubercles',
      'D) Enamel pearls at furcation entrances only'
     ],
     'answer': 'B) An enlarged pulp chamber with apically displaced furcation',
     'explanation': 'Taurodontism features an enlarged pulp chamber with apical displacement of the root furcation, producing short roots relative to crown–body height. The altered chamber morphology complicates canal location and increases risk of perforation during endodontic access.',
     'choice_explanations': {
      'A': 'Taurodontism is defined by enlarged chamber and apical furcation shift, not simply dilacerated crowns. Taurodontism features an enlarged pulp chamber with apical displacement of the root furcation, producing short roots relative to crown–body height.',
      'B': 'Taurodontism features an enlarged pulp chamber with apical displacement of the root furcation, producing short roots relative to crown–body height. The altered chamber morphology complicates canal location and increases risk of perforation during endodontic access.',
      'C': 'Dens evaginatus is an occlusal enamel tubercle that can pulp-expose with wear/fracture. Taurodontism features an enlarged pulp chamber with apical displacement of the root furcation, producing short roots relative to crown–body height.',
      'D': 'Enamel pearls are ectopic enamel droplets on root surfaces, often near furcations. Taurodontism features an enlarged pulp chamber with apical displacement of the root furcation, producing short roots relative to crown–body height.'
     }
    },
    {
     'question': 'Root dilaceration most complicates?',
     'options': [
      'A) Shade selection for composite only',
      'B) Routine flossing effectiveness',
      'C) Rubber dam clamp color coding',
      'D) Extraction path and endodontic access'
     ],
     'answer': 'D) Extraction path and endodontic access',
     'explanation': 'Dilaceration is a sharp bend in the root or crown, usually from trauma to the developing tooth germ. The angulation impedes straight-line endodontic access and increases risk of root fracture or incomplete removal during extraction.',
     'choice_explanations': {
      'A': 'Root dilaceration complicates extraction path and endodontic access, not shade selection. Dilaceration is a sharp bend in the root or crown, usually from trauma to the developing tooth germ.',
      'B': 'Flossing efficacy is unrelated to the surgical/endodontic complications of root dilaceration. Dilaceration is a sharp bend in the root or crown, usually from trauma to the developing tooth germ.',
      'C': 'Clamp color coding is inventory convenience, not affected by dilaceration biomechanics. Dilaceration is a sharp bend in the root or crown, usually from trauma to the developing tooth germ.',
      'D': 'Dilaceration is a sharp bend in the root or crown, usually from trauma to the developing tooth germ. The angulation impedes straight-line endodontic access and increases risk of root fracture or incomplete removal during extraction.'
     }
    }
   ]
  },
  'cases': {
   'easy': [
    {
     'title': 'Identify Tooth',
     'stem': 'A tooth has 3 roots and a Carabelli cusp trait.',
     'question': 'Most likely?',
     'answer': 'Maxillary first molar.',
     'discussion': 'Know morphology for endo/restorative.',
     'book_hint': "Wheeler's Dental Anatomy, Physiology and Occlusion"
    }
   ],
   'medium': [
    {
     'title': 'Endo Access Planning',
     'stem': 'Upper first premolar needs RCT.',
     'question': 'Anatomy alert?',
     'answer': 'Often two canals — search carefully.',
     'discussion': 'Missed canal → failure.',
     'book_hint': "Wheeler's Dental Anatomy, Physiology and Occlusion"
    }
   ],
   'hard': [
    {
     'title': 'Young Tooth Prep Exposure Risk',
     'stem': 'A teenager needs a deep occlusal restoration on a newly erupted molar. Choose the safest high-yield next concept before definitive results.',
     'question': 'Anatomy concern?',
     'answer': 'High pulp horns — careful depth, consider indirect pulp strategies.',
     'discussion': 'Avoid iatrogenic exposure.',
     'book_hint': "Wheeler's Dental Anatomy, Physiology and Occlusion"
    }
   ],
   'extreme': [
    {
     'title': 'Bizarre Root Morphology Pre-Extract',
     'stem': 'A curved dilacerated premolar needs extraction under LA. Avoid harmful premature treatment while catastrophic differentials remain open.',
     'question': 'Plan?',
     'answer': 'Radiograph assessment, surgical sectioning readiness, avoid blind force.',
     'discussion': 'Prevent root fracture/displacement.',
     'book_hint': "Wheeler's Dental Anatomy, Physiology and Occlusion"
    }
   ]
  }
 }
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
