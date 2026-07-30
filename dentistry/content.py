"""Undergraduate dentistry study content by specialty and difficulty."""
from __future__ import annotations

import random

from quiz_bank import DIFFICULTIES, DIFFICULTY_LABELS, LABEL_TO_DIFFICULTY

SPECIALTY_ORDER = ['oral_surgery', 'orthodontics', 'periodontics', 'endodontics', 'prosthodontics', 'pediatric_dentistry', 'oral_medicine', 'restorative', 'oral_radiology', 'dental_anatomy']

SPECIALTIES: dict[str, dict] = {
 'oral_surgery': {
  'label': 'Oral Surgery',
  'books': ["Peterson's Principles of Oral and Maxillofacial Surgery", 'Contemporary Oral and Maxillofacial Surgery — Hupp', 'Local Anaesthesia in Dentistry'],
  'pdf_notes': ['IANB targets mandibular foramen region; know failure causes.', 'Dry socket: pain day 2-4, empty socket — irrigate + dressing.', 'Ludwig angina: airway first, urgent drainage/antibiotics.', 'Assess bleeding risk (anticoagulants) before surgery.', 'Impacted third molars: IAN/lingual nerve risk counseling.'],
  'questions': {
   'easy': [
    {
     'question': 'Which tooth is most frequently impacted in humans, and why does that pattern matter clinically?',
     'options': ['A) Mandibular third molar, which erupts last and often lacks adequate arch space', 'B) Maxillary central incisor, which erupts earliest and always has space', 'C) Mandibular first premolar, which rarely encounters eruption obstacles', 'D) Maxillary first molar, which erupts into a fully developed arch'],
     'answer': 'A) Mandibular third molar, which erupts last and often lacks adequate arch space',
     'explanation': 'Mandibular third molars erupt last and frequently meet insufficient posterior space, bone, or soft-tissue clearance, making them the most commonly impacted teeth. Clinically this drives the high rate of pericoronitis, caries of the distal second molar, and surgical removal. Maxillary canines are next most often impacted but far less often than lower wisdom teeth.',
     'choice_explanations': {'A': 'Third molars erupt last into a region with limited mandibular length; eruption failure from bone/soft tissue/adjacent tooth blockade defines impaction and explains their predominance.', 'B': 'Central incisors erupt early into ample anterior space; true bony impaction is uncommon compared with third molars.', 'C': 'First premolars usually erupt with adequate space; they are not the teeth most often impacted.', 'D': 'First molars erupt into a prepared arch and are rarely impacted relative to mandibular third molars.'}
    },
    {
     'question': 'For a classical inferior alveolar nerve block, anesthetic solution is deposited nearest which landmark?',
     'options': ['A) The mental foramen on the buccal mandibular body', 'B) The mandibular foramen on the medial surface of the ramus', 'C) The infraorbital foramen on the maxillary face', 'D) The greater palatine foramen on the hard palate'],
     'answer': 'B) The mandibular foramen on the medial surface of the ramus',
     'explanation': 'The inferior alveolar nerve enters the mandible at the mandibular foramen on the medial ramus. An IANB places local anesthetic near the lingula/foramen so the nerve is bathed before entering the canal. Accurate height and depth relative to this landmark determine success for ipsilateral mandibular teeth (except when accessory innervation intervenes).',
     'choice_explanations': {'A': 'The mental foramen transmits the mental nerve after the IAN has already entered the canal; it is not the IANB target.', 'B': 'IANB targets the IAN at the mandibular foramen/lingula on the medial ramus before the nerve enters the mandibular canal.', 'C': 'The infraorbital foramen is a maxillary midface landmark for infraorbital blocks, not mandibular anesthesia.', 'D': 'The greater palatine foramen anesthetizes posterior palatal mucosa, not the inferior alveolar nerve.'}
    },
    {
     'question': 'Alveolar osteitis (dry socket) is best explained by which pathophysiologic sequence after extraction?',
     'options': ['A) Immediate bacterial osteomyelitis of the entire mandible on day 0', 'B) Irreversible pulpitis confined to an unrestored adjacent premolar', 'C) Premature clot loss or fibrinolysis exposing bare alveolar bone, typically days 2–4', 'D) Acute maxillary sinusitis without any alveolar communication'],
     'answer': 'C) Premature clot loss or fibrinolysis exposing bare alveolar bone, typically days 2–4',
     'explanation': 'After extraction, a stable blood clot protects bone and initiates healing. Premature clot loss or fibrinolysis leaves exposed bone and inflammatory mediators, producing severe localized pain usually beginning 2–4 days later—classic dry socket, especially after difficult mandibular molar removal. Management centers on irrigation and soothing dressing rather than routine systemic antibiotics when infection is absent.',
     'choice_explanations': {'A': 'Diffuse osteomyelitis is infection of bone marrow with systemic signs; dry socket is localized clot failure without that picture.', 'B': 'Pulpitis is intrapulpal inflammation of a vital/diseased tooth, not an empty post-extraction socket.', 'C': 'Dry socket is fibrinolysis/clot loss with exposed socket bone and delayed severe pain, classically days 2–4 after traumatic lower molar extraction.', 'D': 'Sinusitis is antral mucosal inflammation and does not explain an empty mandibular extraction socket.'}
    },
   ],
   'medium': [
    {
     'question': 'A rapidly progressive floor-of-mouth infection with bilateral submandibular swelling and tongue elevation is managed first by addressing which priority?',
     'options': ['A) Elective root canal therapy alone without airway assessment', 'B) Observation for 72 hours before any antimicrobial therapy', 'C) Immediate full-mouth extraction under local anesthesia only', 'D) Airway security, then IV antibiotics and urgent surgical drainage of involved spaces'],
     'answer': 'D) Airway security, then IV antibiotics and urgent surgical drainage of involved spaces',
     'explanation': 'Ludwig angina is bilateral cellulitis of the submandibular, sublingual, and submental spaces that can rapidly compromise the airway by elevating the tongue and floor of mouth. Immediate priorities are airway assessment/protection, parenteral antibiotics covering odontogenic flora, and surgical drainage. Definitive dental source control follows once the patient is safe.',
     'choice_explanations': {'A': 'RCT addresses a dental source later but does not reverse acute airway-threatening cellulitis.', 'B': 'Delaying antibiotics in rapidly spreading deep-space infection risks airway obstruction and sepsis.', 'C': 'Multiple extractions under LA alone ignore airway risk and inadequate drainage of deep spaces.', 'D': 'Airway threat defines Ludwig angina urgency; secure airway, give IV antibiotics, and drain fascial spaces before elective dental procedures.'}
    },
    {
     'question': 'Before elective oral surgery in a patient taking warfarin, which laboratory parameter most directly guides bleeding-risk planning?',
     'options': ['A) INR (international normalized ratio)', 'B) HbA1c alone without coagulation data', 'C) Serum amylase alone', 'D) Fasting triglyceride level alone'],
     'answer': 'A) INR (international normalized ratio)',
     'explanation': 'Warfarin inhibits vitamin K–dependent clotting factors; therapeutic effect is monitored with INR. Knowing the current INR informs whether extraction can proceed with local hemostasis, whether physician coordination is needed, and how to plan packing/suturing. Metabolic labs such as HbA1c or lipids do not quantify warfarin anticoagulation.',
     'choice_explanations': {'A': 'INR quantifies warfarin’s anticoagulant effect and is the key pre-extraction bleeding-risk metric for warfarin users.', 'B': 'HbA1c reflects average glycemia, not vitamin K–dependent coagulation status.', 'C': 'Amylase assesses pancreatic/salivary enzyme activity, not warfarin intensity.', 'D': 'Triglycerides relate to lipid risk, not surgical hemostasis under warfarin.'}
    },
    {
     'question': 'Oroantral communication risk is highest when extracting which teeth, based on root–sinus anatomy?',
     'options': ['A) Mandibular central incisors remote from the antrum', 'B) Maxillary molars whose roots approximate or project into the sinus floor', 'C) Mandibular canines in the anterior mandible', 'D) Mandibular first premolars distant from the maxillary sinus'],
     'answer': 'B) Maxillary molars whose roots approximate or project into the sinus floor',
     'explanation': 'Maxillary molar (and often premolar) roots frequently lie close to or within the maxillary sinus floor. Traumatic elevation can tear thin bone or Schneiderian membrane, creating an oroantral communication. Mandibular teeth have no anatomic continuity with the maxillary antrum.',
     'choice_explanations': {'A': 'Mandibular incisor apices lie far from the maxillary sinus and do not create oroantral openings.', 'B': 'Proximity of maxillary molar roots to the antral floor explains the highest OAC risk during their extraction.', 'C': 'Mandibular canines occupy anterior mandibular bone without antral adjacency.', 'D': 'Mandibular premolars sit in the mandible and cannot open into the maxillary sinus.'}
    },
   ],
   'hard': [
    {
     'question': 'A 28-year-old needs removal of a mesioangular mandibular third molar. Panoramic and CBCT show darkening of the root, interruption of the white lines of the canal, and diversion of the inferior alveolar canal. Which intraoperative principle best reduces permanent neurosensory injury?',
     'options': ['A) Forceful elevator leverage directly toward the canal to speed removal', 'B) Ignore imaging and rely solely on clinical crown visibility', 'C) Use controlled sectioning and elevation away from the canal, with informed consent for IAN risk', 'D) Perform blind aggressive curettage of the entire canal contents'],
     'answer': 'C) Use controlled sectioning and elevation away from the canal, with informed consent for IAN risk',
     'explanation': 'Radiographic signs of intimate IAN–root relationship predict higher nerve injury risk. Risk reduction includes CBCT-informed planning, tooth sectioning to minimize apical force toward the canal, careful elevation vectors, and documented consent. Forceful blind leverage or canal curettage increases stretch, crush, or transection injury to the inferior alveolar nerve.',
     'choice_explanations': {'A': 'Levering toward the canal concentrates compressive/tensile force on the IAN and raises permanent paresthesia risk.', 'B': 'Ignoring high-risk imaging signs forfeits planning that prevents nerve injury.', 'C': 'When imaging shows canal–root intimacy, sectioning and controlled elevation away from the canal plus consent are the evidence-aligned safety approach.', 'D': 'Curettage inside the canal can directly transect or avulse the IAN.'}
    },
    {
     'question': 'Two days after difficult lower third-molar removal, a patient has severe localized socket pain, an empty socket with gray debris, no fever, and no fluctuance. Which management best matches the diagnosis?',
     'options': ['A) Start broad empiric IV antibiotics for presumed Ludwig angina', 'B) Immediate incision of the contralateral submandibular space', 'C) Urgent anticoagulation reversal for suspected hematoma alone', 'D) Irrigate gently and place a soothing medicated dressing; antibiotics are not first-line without infection'],
     'answer': 'D) Irrigate gently and place a soothing medicated dressing; antibiotics are not first-line without infection',
     'explanation': 'Empty painful socket at days 2–4 without systemic infection indicates alveolar osteitis. Standard care is irrigation of debris and a eugenol-containing or other soothing dressing with analgesia; antibiotics are reserved for true infection. Ludwig angina and hematoma present differently (bilateral floor swelling/airway threat or expanding bruise).',
     'choice_explanations': {'A': 'IV antibiotics target spreading infection; this presentation lacks systemic/space infection signs.', 'B': 'Contralateral space incision is for drained deep infection, not an empty extraction socket.', 'C': 'Anticoagulant reversal addresses bleeding risk, not fibrinolysis-related dry socket pain.', 'D': 'Classic dry socket is managed locally with irrigation and dressing; systemic antibiotics are unnecessary without cellulitis/fever/pus.'}
    },
    {
     'question': 'During extraction of an upper first molar, a 4 mm communication to the antrum is noted with a positive Valsalva bubble test. The patient is otherwise healthy. What is the most appropriate immediate management concept?',
     'options': ['A) Inform the patient, place a tension-free soft-tissue closure when feasible, prescribe sinus precautions, and arrange follow-up', 'B) Pack the antrum with nonresorbable cotton and discharge without advice', 'C) Ignore the finding because all communications close spontaneously without care', 'D) Perform immediate Caldwell–Luc antrostomy as routine first-line for every small OAC'],
     'answer': 'A) Inform the patient, place a tension-free soft-tissue closure when feasible, prescribe sinus precautions, and arrange follow-up',
     'explanation': 'Small intraoperative oroantral communications are managed by patient disclosure, primary soft-tissue closure when possible, sinus precautions (no nose-blowing/straws), and review. Persistent fistulae may need later layered closure ± buccal fat pad. Routine immediate Caldwell–Luc is not indicated for a small fresh communication, and leaving foreign packing in the antrum is harmful.',
     'choice_explanations': {'A': 'Fresh small OAC: close mucosa if possible, sinus precautions, follow-up; escalate surgery only if fistula persists.', 'B': 'Nonresorbable antral packing invites infection and does not constitute proper closure.', 'C': 'Not all OACs close reliably without mucosal management and precautions; disclosure is mandatory.', 'D': 'Caldwell–Luc is not first-line for a small fresh communication manageable with local closure.'}
    },
   ],
   'extreme': [
    {
     'question': 'A 62-year-old on warfarin for a mechanical mitral valve (INR 2.8 yesterday) needs urgent extraction of a fractured mandibular molar with continuous oozing. He reports prior TIA when warfarin was stopped elsewhere. There is no expanding hematoma or airway threat. Which management plan is most appropriate?',
     'options': ['A) Stop warfarin this morning unilaterally and restart in two weeks without physician input', 'B) Coordinate with the physician, generally continue warfarin at therapeutic INR for single extraction, and emphasize local hemostasis (sutures, packing, tranexamic rinse) rather than unilateral cessation', 'C) Refuse all dental care permanently because mechanical valves contraindicate extraction', 'D) Give high-dose vitamin K empirically in clinic without assessing thrombotic indication'],
     'answer': 'B) Coordinate with the physician, generally continue warfarin at therapeutic INR for single extraction, and emphasize local hemostasis (sutures, packing, tranexamic rinse) rather than unilateral cessation',
     'explanation': 'Patients with mechanical mitral valves have high thromboembolic risk if anticoagulation is interrupted. For most outpatient extractions, continuing warfarin within a therapeutic INR and using meticulous local hemostasis (sutures, collagen/oxidized cellulose, tranexamic acid mouthwash) is preferred, coordinated with the physician. Blind cessation or unsupervised vitamin K can precipitate stroke or valve thrombosis.',
     'choice_explanations': {'A': 'Unilateral prolonged cessation in mechanical mitral valve disease risks catastrophic thromboembolism.', 'B': 'High-thrombotic-risk anticoagulation should not be stopped unilaterally; continue when INR is acceptable and control bleeding locally with physician coordination.', 'C': 'Extractions can be performed safely with planning; lifelong refusal is not evidence-based.', 'D': 'Empiric vitamin K reverses warfarin unpredictably and may cause valve thrombosis without indication.'}
    },
    {
     'question': 'A 34-year-old develops progressive bilateral submandibular and submental swelling, dysphagia, and inability to protrude the tongue 24 hours after lower molar infection. SpO2 is 94% sitting forward. Which sequenced plan best reflects complication management?',
     'options': ['A) Prescribe oral antibiotics only and reassess in one week as an outpatient', 'B) Perform only pulp capping of the molar under rubber dam without airway planning', 'C) Emergent airway evaluation (often fiberoptic/awake strategies), IV broad-spectrum antibiotics, urgent incision and drainage of bilateral floor-of-mouth spaces, then source control', 'D) Start high-dose NSAIDs alone to reduce swelling while deferring drainage'],
     'answer': 'C) Emergent airway evaluation (often fiberoptic/awake strategies), IV broad-spectrum antibiotics, urgent incision and drainage of bilateral floor-of-mouth spaces, then source control',
     'explanation': 'This vignette is Ludwig angina with early airway compromise. Mortality risk is driven by asphyxia; therefore airway first, then parenteral antibiotics and wide drainage of the bilateral submandibular/sublingual/submental spaces, followed by elimination of the odontogenic source. Oral antibiotics alone, pulp therapy alone, or anti-inflammatory delay without drainage are dangerous near-misses.',
     'choice_explanations': {'A': 'Outpatient oral antibiotics cannot reverse airway-threatening deep neck infection.', 'B': 'Pulp procedures do not secure the airway or drain fascial cellulitis.', 'C': 'Ludwig angina with desaturation requires airway-first care, IV antibiotics, and urgent bilateral space drainage before definitive dentistry.', 'D': 'NSAIDs may ease pain but do not drain infection or protect the airway.'}
    },
    {
     'question': 'After surgical removal of a deeply impacted lower third molar, the patient awakens with complete anesthesia of the ipsilateral lower lip and chin. Intraoperatively the canal was visible and a root tip was elevated adjacent to it. Six hours later there is still dense anesthesia without dysesthesia. What is the best immediate counseling and next-step concept?',
     'options': ['A) Assure the patient that sensation always returns fully within 24 hours so no follow-up is needed', 'B) Perform immediate surgical resection of a segment of the inferior alveolar nerve', 'C) Start long-term high-dose opioids as the sole definitive nerve therapy', 'D) Document sensory mapping, explain possible neuropraxia versus more severe injury, avoid irreversible statements of permanence yet, arrange close neurosensory follow-up, and consider early specialist referral pathways used in your region'],
     'answer': 'D) Document sensory mapping, explain possible neuropraxia versus more severe injury, avoid irreversible statements of permanence yet, arrange close neurosensory follow-up, and consider early specialist referral pathways used in your region',
     'explanation': 'Postoperative complete lip/chin anesthesia after visible canal proximity suggests neurapraxia, axonotmesis, or neurotmesis of the IAN. Immediate priorities are honest documentation, baseline sensory testing, steroids/anti-inflammatory measures per protocol, and structured follow-up with timely referral if dense deficit persists—because timing affects microsurgical options. Guaranteeing full return, resecting nerve, or treating with opioids alone are incorrect.',
     'choice_explanations': {'A': 'Not all IAN injuries recover in 24 hours; failing follow-up risks missing repair windows.', 'B': 'Segmental nerve resection worsens deficit and is not acute management of suspected injury.', 'C': 'Opioids treat pain symptomatically but do not restore nerve continuity or guide repair timing.', 'D': 'IAN injury needs documented sensory exam, realistic counseling, surveillance, and timely specialist referral—not false reassurance or destructive/sole opioid care.'}
    },
   ],
  },
  'cases': {
   'easy': [
    {'title': 'Pain Day 3 After Extraction', 'stem': 'A 24-year-old has severe pain 3 days after lower wisdom tooth removal. Socket looks empty; no pus or fever.', 'question': 'Likely diagnosis?', 'answer': 'Alveolar osteitis (dry socket).', 'discussion': 'Irrigate, medicated dressing, analgesia; antibiotics usually not first-line if no infection.', 'book_hint': "Peterson's Principles of Oral and Maxillofacial Surgery"},
   ],
   'medium': [
    {'title': 'Fever + Floor of Mouth Swelling', 'stem': 'A patient after dental infection has bilateral floor-of-mouth swelling, drooling, and tongue elevation.', 'question': 'Emergency concern?', 'answer': 'Ludwig angina — secure airway and urgent surgical/medical care.', 'discussion': 'Do not delay for routine dental clinic care.', 'book_hint': "Peterson's Principles of Oral and Maxillofacial Surgery"},
   ],
   'hard': [
    {'title': 'Root Tip Disappears Upward', 'stem': 'During upper 6 extraction, a root tip vanishes and the patient feels air/fluid in the nose when drinking. Choose the safest high-yield next concept before definitive results.', 'question': 'What happened conceptually?', 'answer': 'Oroantral communication ± displaced root — stop forcing, assess, arrange appropriate closure/retrieval.', 'discussion': 'Sinus precautions and follow-up are essential.', 'book_hint': "Peterson's Principles of Oral and Maxillofacial Surgery"},
   ],
   'extreme': [
    {'title': 'Irradiated Jaw Needs Extraction', 'stem': 'A head-and-neck cancer survivor with prior radiotherapy needs a painful molar extraction in the irradiated field. Avoid harmful premature treatment while catastrophic differentials remain open.', 'question': 'Key concept?', 'answer': 'High ORN risk — specialist OMFS planning, atraumatic technique, infection control, and protocolized prevention.', 'discussion': 'Never treat as a routine extraction.', 'book_hint': "Peterson's Principles of Oral and Maxillofacial Surgery"},
   ],
  },
 },
 'orthodontics': {
  'label': 'Orthodontics',
  'books': ["Proffit's Contemporary Orthodontics", 'Graber Orthodontics', 'Handbook of Orthodontics — Cobourne'],
  'pdf_notes': ['Angle Class I/II/III molar relationships.', 'Overjet = horizontal; overbite = vertical.', 'Space maintainers after premature primary loss.', 'Retention is long-term; relapse is common without retainers.', 'Uncontrolled periodontitis: do not move teeth aggressively.'],
  'questions': {
   'easy': [
    {
     'question': 'Angle Class II division 1 occlusion is characterized by which anteroposterior molar/canine relationship with typical incisor feature?',
     'options': ['A) Distal molar relationship with proclined maxillary incisors and increased overjet', 'B) Mesial molar relationship with reverse overjet only', 'C) Class I molars with edge-to-edge incisors only', 'D) Complete absence of all first permanent molars'],
     'answer': 'A) Distal molar relationship with proclined maxillary incisors and increased overjet',
     'explanation': 'In Angle Class II, the mandibular first molar is distal to the maxillary first molar. Division 1 shows proclined upper incisors and often large overjet; division 2 shows retroclined upper centrals. This anteroposterior discrepancy guides growth modification or camouflage planning.',
     'choice_explanations': {'A': 'Class II div 1 = distal molar relation plus proclined upper incisors/increased overjet.', 'B': 'Mesial molar relation defines Class III, not Class II division 1.', 'C': 'Class I molars are not the Class II molar relationship.', 'D': 'Missing molars are not required to define Angle Class II division 1.'}
    },
    {
     'question': 'Which tissue remodeling concept primarily allows orthodontic tooth movement through alveolar bone?',
     'options': ['A) Enamel hyperplasia on the pressure side only', 'B) Pressure-side resorption and tension-side apposition of alveolar bone', 'C) Pulp stone formation as the main relocation mechanism', 'D) Cementum thickening that pushes the crown through mucosa'],
     'answer': 'B) Pressure-side resorption and tension-side apposition of alveolar bone',
     'explanation': 'Sustained force creates a pressure side where osteoclasts resorb alveolar bone and a tension side where osteoblasts deposit bone, allowing the tooth–PDL unit to relocate. Excess force can cause hyalinization and root resorption. Enamel, pulp stones, and cementum hyperplasia are not the primary relocation mechanism.',
     'choice_explanations': {'A': 'Enamel does not remodel to move teeth through bone.', 'B': 'Orthodontic movement depends on coupled pressure-side bone resorption and tension-side bone formation via the PDL.', 'C': 'Pulp stones are calcifications within pulp; they do not translate the tooth.', 'D': 'Cementum changes may accompany movement but do not drive alveolar relocation.'}
    },
    {
     'question': 'Anchorage in orthodontics refers primarily to which clinical concept?',
     'options': ['A) The brand name of a particular bracket prescription only', 'B) The color of elastomeric ligatures', 'C) Resistance to unwanted tooth movement used to support desired movement', 'D) The patient’s preferred toothpaste flavor'],
     'answer': 'C) Resistance to unwanted tooth movement used to support desired movement',
     'explanation': 'Anchorage is the resistance to reaction forces that would move nontarget teeth undesirably. Planning absolute, maximum, moderate, or minimum anchorage determines whether molars may move mesially during space closure. Temporary anchorage devices increase anchorage by recruiting bone rather than teeth alone.',
     'choice_explanations': {'A': 'Bracket prescription is a wire–bracket geometry system, not the definition of anchorage.', 'B': 'Ligature color is cosmetic and unrelated to anchorage biomechanics.', 'C': 'Anchorage means controlling reaction forces so supporting units resist unwanted movement while targets move.', 'D': 'Toothpaste flavor has no biomechanical anchorage meaning.'}
    },
   ],
   'medium': [
    {
     'question': 'A growing Class II patient with mandibular retrognathia and good compliance is being considered for functional appliance therapy. Which applied principle best matches indication?',
     'options': ['A) Wait until growth cessation then only do functional appliances', 'B) Extract all third molars as the sole Class II correction', 'C) Ignore skeletal pattern and treat only with bleaching', 'D) Use growth modification while the patient is still growing to advance mandibular posture/remodeling'],
     'answer': 'D) Use growth modification while the patient is still growing to advance mandibular posture/remodeling',
     'explanation': 'Functional appliances for Class II mandibular deficiency are most effective in growing patients because they can influence mandibular growth expression and dentoalveolar compensation. After growth cessation, skeletal change is limited and camouflage or orthognathic surgery become the main options. Extractions or bleaching alone do not correct the skeletal Class II pattern.',
     'choice_explanations': {'A': 'Functional appliances lose skeletal utility after growth completion.', 'B': 'Third-molar extraction does not correct Class II molar/skeletal relations by itself.', 'C': 'Bleaching changes tooth color, not occlusion or jaw relationship.', 'D': 'Growth modification for mandibular retrognathia is timed to remaining growth, not after growth ends.'}
    },
    {
     'question': 'During space closure on a continuous archwire, the posterior unit drifts mesially more than planned. Which applied diagnosis fits best?',
     'options': ['A) Anchorage loss from insufficient posterior resistance relative to anterior retraction force', 'B) Ideal absolute anchorage with zero molar movement', 'C) Only enamel fluorosis unrelated to mechanics', 'D) Successful torque without any reaction forces'],
     'answer': 'A) Anchorage loss from insufficient posterior resistance relative to anterior retraction force',
     'explanation': 'Newton’s third law means retracting anteriors produces equal opposite force on posteriors. If posterior anchorage is inadequate, molars mesialize (anchorage loss), consuming extraction space. Recognition prompts reinforcement (TADs, headgear, differential moments) rather than assuming forces act on one unit only.',
     'choice_explanations': {'A': 'Unplanned molar mesialization during retraction is classic anchorage loss from reaction forces.', 'B': 'Absolute anchorage implies negligible molar mesialization, opposite of this finding.', 'C': 'Fluorosis is a developmental enamel defect, not a space-closure mechanic diagnosis.', 'D': 'Every orthodontic force has an equal opposite reaction; zero reaction is physically false.'}
    },
    {
     'question': 'A patient presents with anterior open bite, tongue thrust habit, and increased lower face height. Which applied treatment concept is most coherent?',
     'options': ['A) Bond only lower lingual retainers and ignore the open bite', 'B) Address habit and vertical control; consider habit therapy, orthodontics, and possible surgical options if skeletal vertical excess persists', 'C) Prescribe antibiotics for the open bite', 'D) Extract maxillary laterals as first-line for all open bites'],
     'answer': 'B) Address habit and vertical control; consider habit therapy, orthodontics, and possible surgical options if skeletal vertical excess persists',
     'explanation': 'Anterior open bite often combines habit, airway/vertical skeletal factors, and dental compensations. Stable correction requires habit control, vertical mechanics or TADs, and sometimes orthognathic surgery for severe skeletal vertical excess. Antibiotics and unrelated extractions do not address etiology.',
     'choice_explanations': {'A': 'A retainer without bite correction leaves the functional and esthetic problem untreated.', 'B': 'Open-bite care targets habit and vertical skeletal/dental factors; retainers or antibiotics alone are insufficient.', 'C': 'Open bite is not an infection requiring antibiotics.', 'D': 'Routine lateral extraction is not a universal open-bite solution and may worsen esthetics.'}
    },
   ],
   'hard': [
    {
     'question': 'A 13-year-old has a unilateral posterior crossbite with functional shift of the mandible toward the crossbite side, asymmetric CO–CR, and a midline deviation that improves when the mandible is guided to CR. What is the most appropriate early management concept?',
     'options': ['A) Delay all treatment until age 25 because shifts always self-correct', 'B) Extract the shifting-side canine immediately as sole therapy', 'C) Correct the transverse discrepancy early (e.g., expansion) to eliminate the shift and reduce asymmetric growth risk', 'D) Place a high-pull headgear only without addressing the crossbite'],
     'answer': 'C) Correct the transverse discrepancy early (e.g., expansion) to eliminate the shift and reduce asymmetric growth risk',
     'explanation': 'A functional shift from unilateral crossbite can drive asymmetric condylar loading and facial growth. Early transverse correction removes the occlusal interference that causes the shift, allowing more symmetric growth. Waiting until adulthood, extracting a canine alone, or ignoring the crossbite with unrelated AP mechanics are near-miss strategies.',
     'choice_explanations': {'A': 'Functional shifts do not reliably self-correct and may worsen facial asymmetry with growth.', 'B': 'Canine extraction does not remove the transverse interference causing the shift.', 'C': 'Functional mandibular shifts from crossbite warrant early expansion/transverse correction to stop asymmetric guidance.', 'D': 'Headgear addresses AP/vertical anchorage, not the unilateral crossbite shift etiology.'}
    },
    {
     'question': 'An adult Class III patient shows edge-to-edge incisors in CR but clear reverse overjet in CO, with a large CO–CR discrepancy and dental compensations (proclined lower incisors). Which treatment-planning distinction is most critical?',
     'options': ['A) Assume every edge-to-edge bite is only enamel hypoplasia', 'B) Treat only with nightguard without occlusal diagnosis', 'C) Ignore CR records because CO is always identical to CR', 'D) Differentiate pseudo-Class III (functional shift) from true skeletal Class III before choosing camouflage versus surgery'],
     'answer': 'D) Differentiate pseudo-Class III (functional shift) from true skeletal Class III before choosing camouflage versus surgery',
     'explanation': 'Pseudo-Class III features an anterior shift into reverse overjet with a more favorable CR relationship, whereas true skeletal Class III remains Class III in CR. Discriminating these guides expansion/alignment versus orthognathic surgery. Dental compensations can mask severity; CR mountings/records prevent mis-planning.',
     'choice_explanations': {'A': 'Enamel hypoplasia is a developmental defect, not a sagittal classification tool.', 'B': 'A nightguard without diagnosing shift vs skeletal discrepancy misses definitive care.', 'C': 'CO and CR often differ in shift cases; ignoring CR risks wrong surgery/camouflage choice.', 'D': 'CO–CR analysis distinguishes functional pseudo-Class III from true skeletal Class III and changes the entire plan.'}
    },
    {
     'question': 'Mid-treatment, a patient on rectangular stainless steel wires develops increasing root resorption on maxillary incisors, short roots on start films, and heavy continuous forces historically used. Which multi-cue adjustment is most appropriate?',
     'options': ['A) Reduce force magnitude/duration, pause aggressive torque, reassess radiographs, and reconsider treatment goals', 'B) Increase continuous heavy force to finish faster despite resorption', 'C) Ignore resorption because orthodontics never affects roots', 'D) Switch solely to bleaching trays as root therapy'],
     'answer': 'A) Reduce force magnitude/duration, pause aggressive torque, reassess radiographs, and reconsider treatment goals',
     'explanation': 'External apical root resorption risk rises with heavy force, long treatment, torque, and pre-existing short roots. Prudent response is force reduction, possible treatment pause, radiographic monitoring, and goal modification. Accelerating with heavier force, denying risk, or bleaching does not manage biologic damage.',
     'choice_explanations': {'A': 'When resorption cues appear, lighten forces, limit torque/duration, monitor, and revise goals—do not escalate force.', 'B': 'Heavier continuous force worsens resorption risk and is contraindicated.', 'C': 'Orthodontic force can cause iatrogenic root resorption; denial is incorrect.', 'D': 'Bleaching does not treat or reverse root resorption.'}
    },
   ],
   'extreme': [
    {
     'question': 'A 16-year-old with severe Class II division 1, overjet 10 mm, incompetent lips, and a history of traumatic upper incisor fracture presents for comprehensive care. Growth charts suggest little remaining mandibular growth. Cephalometrics show marked mandibular retrognathia and upright lower incisors. Which decision pathway best balances occlusion, face, and trauma risk?',
     'options': ['A) Promise complete skeletal correction using only Class II elastics without surgery counseling', 'B) Discuss camouflage limits versus orthognathic advancement after growth completion, protect incisors meanwhile, and avoid promising full skeletal correction with elastics alone', 'C) Extract all remaining healthy teeth to eliminate overjet without prosthetic plan', 'D) Defer any trauma protection because large overjet never increases injury risk'],
     'answer': 'B) Discuss camouflage limits versus orthognathic advancement after growth completion, protect incisors meanwhile, and avoid promising full skeletal correction with elastics alone',
     'explanation': 'Large overjet with incompetent lips raises dental trauma risk and reflects skeletal Class II. With minimal residual growth, functional appliances will not deliver major mandibular advancement; camouflage has facial/periodontal limits, and orthognathic surgery may be required for ideal correction. Interim protection (mouthguard) and honest shared decision-making are essential; elastics alone cannot create adult mandibular length.',
     'choice_explanations': {'A': 'Elastics mainly move teeth; they cannot reliably create substantial adult mandibular skeletal advancement.', 'B': 'Post-growth severe skeletal Class II needs surgery-vs-camouflage counseling plus interim trauma protection—not elastics-only promises.', 'C': 'Extracting healthy dentition without reconstruction is mutilating and not a Class II solution.', 'D': 'Increased overjet is a documented trauma risk factor; protection should not be deferred.'}
    },
    {
     'question': 'An adult interdisciplinary case shows pathologic migration of upper incisors, 6 mm pocketing, reduced bone height, and a diastema increasing over 2 years. The patient wants braces immediately for esthetics. Periodontal charting and radiographs confirm uncontrolled inflammation. What is the most appropriate sequenced decision?',
     'options': ['A) Bond immediately with heavy continuous forces despite active periodontitis', 'B) Extract all periodontally involved teeth before any hygiene phase', 'C) Stabilize periodontal disease first (cause-related therapy ± surgery), then consider limited orthodontics with light forces and retention planning', 'D) Place veneers only over inflamed bleeding tissues without periodontal care'],
     'answer': 'C) Stabilize periodontal disease first (cause-related therapy ± surgery), then consider limited orthodontics with light forces and retention planning',
     'explanation': 'Orthodontic forces in uncontrolled periodontitis can accelerate attachment loss. Pathologic migration requires infection control, oral hygiene, and often regenerative/ resective periodontal therapy before tooth movement. Light forces and long-term retention follow once inflammation is controlled. Immediate heavy orthodontics or restorative cover-up without perio stability is a dangerous near-miss.',
     'choice_explanations': {'A': 'Moving teeth through inflamed periodontium risks rapid attachment destruction.', 'B': 'Extractions before hygiene assessment skip reversible disease control and informed planning.', 'C': 'Active periodontitis must be stabilized before orthodontics; then light-force movement and retention are considered.', 'D': 'Veneering inflamed tissues traps plaque and ignores biologic foundation.'}
    },
    {
     'question': 'During combined orthodontic–orthognathic planning for skeletal open bite, models show dental compensation with already proclined upper and lower incisors, narrow maxilla, and gummy smile from vertical maxillary excess. Which complication-aware plan is most coherent?',
     'options': ['A) Extrude molars further with continuous anterior elastics as sole adult skeletal cure', 'B) Expand only with rapid palatal expansion assuming adult midpalatal suture always opens like a child', 'C) Ignore vertical excess and finish with anterior bonding alone', 'D) Plan skeletal correction (often segmental maxillary surgery ± mandibular procedures) rather than further dental proclination that would decompensate poorly and relapse vertically'],
     'answer': 'D) Plan skeletal correction (often segmental maxillary surgery ± mandibular procedures) rather than further dental proclination that would decompensate poorly and relapse vertically',
     'explanation': 'Adult skeletal open bite with VME and maxillary constriction typically needs surgical (or skeletally anchored) correction; further dental extrusion/proclination worsens stability and periodontium. Adult RPE may fail if the suture is fused, favoring SARPE or bone-borne expansion. Bonding alone cannot correct VME or open bite skeletal pattern.',
     'choice_explanations': {'A': 'Molar extrusion increases vertical dimension and can worsen open bite; it is not an adult skeletal cure.', 'B': 'Adult midpalatal suture often resists classic RPE; assuming pediatric response risks failure/relapse.', 'C': 'Anterior bonding without vertical skeletal correction leaves gummy smile and open bite uncorrected.', 'D': 'True skeletal open bite/VME requires skeletal surgery or skeletal anchorage strategies—not more dental compensation.'}
    },
   ],
  },
  'cases': {
   'easy': [
    {'title': 'Crowding in Teen', 'stem': 'A 14-year-old has moderate crowding and Class I molars. Oral hygiene is good.', 'question': 'First planning idea?', 'answer': 'Comprehensive orthodontic assessment (records, growth, hygiene).', 'discussion': 'Treatment options depend on space analysis.', 'book_hint': "Proffit's Contemporary Orthodontics"},
   ],
   'medium': [
    {'title': 'Anterior Crossbite Child', 'stem': 'An 8-year-old has one upper incisor in crossbite with a shift on closing.', 'question': 'Concern?', 'answer': 'Functional shift from interference — early correction often indicated.', 'discussion': 'Prevent asymmetric growth habits.', 'book_hint': "Proffit's Contemporary Orthodontics"},
   ],
   'hard': [
    {'title': 'Adult Relapse After Retainers Lost', 'stem': 'A 28-year-old stopped wearing retainers and crowding returned. Choose the safest high-yield next concept before definitive results.', 'question': 'Teaching point?', 'answer': 'Relapse risk is lifelong for many; retention is part of treatment.', 'discussion': 'Discuss retreatment vs limited alignment.', 'book_hint': "Proffit's Contemporary Orthodontics"},
   ],
   'extreme': [
    {'title': 'Growing Class III with Functional Shift', 'stem': 'A child with developing Class III has an edge-to-edge bite and a shift. Parents want braces immediately. Avoid harmful premature treatment while catastrophic differentials remain open.', 'question': 'Concept?', 'answer': 'Distinguish pseudo-Class III / shift from true skeletal Class III; growth modification timing and differential diagnosis matter before irreversible camouflage.', 'discussion': 'Wrong early extraction plans can harm.', 'book_hint': "Proffit's Contemporary Orthodontics"},
   ],
  },
 },
 'periodontics': {
  'label': 'Periodontics',
  'books': ["Carranza's Clinical Periodontology", "Lindhe's Clinical Periodontology", 'Periodontology at a Glance'],
  'pdf_notes': ['Gingivitis reversible; periodontitis has attachment loss.', 'Biofilm disruption is the foundation of care.', 'Smoking increases severity and masks bleeding.', 'Re-evaluate after nonsurgical therapy.', 'NUG: pain, bleeding, necrosis of papillae.'],
  'questions': {
   'easy': [
    {
     'question': 'The primary microbial niche associated with initiation and progression of periodontitis is which biofilm location?',
     'options': ['A) Subgingival biofilm within the periodontal pocket', 'B) Sterile pulp tissue of intact virgin teeth only', 'C) Supragingival stain without living microorganisms', 'D) Keratinized palate remote from the gingival margin'],
     'answer': 'A) Subgingival biofilm within the periodontal pocket',
     'explanation': 'Periodontitis is a dysbiotic inflammatory disease driven largely by subgingival biofilm interacting with a susceptible host. Pocket microbiota sit against root cementum and ulcerated pocket epithelium, sustaining connective tissue and bone destruction. Supragingival stain alone or distant mucosa is not the primary pathogenic niche.',
     'choice_explanations': {'A': 'Subgingival biofilm in pockets is the key microbial driver of periodontitis alongside host response.', 'B': 'Intact pulp is not the periodontitis biofilm habitat.', 'C': 'Stain can be esthetic; living subgingival biofilm drives disease.', 'D': 'Palatal keratinized tissue away from the sulcus is not the pocket niche.'}
    },
    {
     'question': 'Clinical attachment loss is measured as which combination?',
     'options': ['A) Crown height alone without probing', 'B) Probing depth plus gingival recession relative to the cementoenamel junction (or equivalent landmark)', 'C) Only pulp vitality test scores', 'D) Only salivary flow rate in mL/min'],
     'answer': 'B) Probing depth plus gingival recession relative to the cementoenamel junction (or equivalent landmark)',
     'explanation': 'Clinical attachment level/loss references the CEJ: when recession is present, CAL ≈ probing depth + recession; when the gingival margin is coronal to the CEJ, the coronal tissue height is subtracted. CAL quantifies cumulative destruction better than probing depth alone. Vitality and saliva tests assess other domains.',
     'choice_explanations': {'A': 'Crown height does not measure periodontal attachment.', 'B': 'CAL integrates pocket depth and gingival margin position relative to the CEJ.', 'C': 'Pulp tests assess endodontic status, not attachment level.', 'D': 'Salivary flow assesses dry mouth risk, not CAL.'}
    },
    {
     'question': 'What is the principal goal of nonsurgical periodontal therapy (scaling and root planing)?',
     'options': ['A) Place porcelain veneers on inflamed anterior teeth first', 'B) Obliterate the entire alveolar process prophylactically', 'C) Disrupt and reduce subgingival biofilm and calculus to allow inflammation resolution', 'D) Replace all amalgams regardless of periodontal status'],
     'answer': 'C) Disrupt and reduce subgingival biofilm and calculus to allow inflammation resolution',
     'explanation': 'Cause-related nonsurgical therapy removes/disrupts biofilm and calculus, reduces pocket bacterial load, and enables healing with pocket reduction and attachment gain in many sites. Restorative cosmetics or unnecessary bone removal are not first-line periodontal goals.',
     'choice_explanations': {'A': 'Veneers on inflamed gingiva violate biologic and plaque-control principles.', 'B': 'Removing alveolar bone prophylactically is destructive, not therapeutic SRP.', 'C': 'SRP aims to control the subgingival biofilm/calculus load so inflammation can resolve.', 'D': 'Blanket amalgam replacement does not treat periodontitis etiology.'}
    },
   ],
   'medium': [
    {
     'question': 'A patient has bleeding on probing, 5–6 mm pockets, radiographic horizontal bone loss, and poor interdental cleaning. After oral hygiene instruction, what is the most appropriate next applied therapy?',
     'options': ['A) Immediate free gingival graft at every bleeding site before hygiene', 'B) Systemic antifungals as sole periodontitis therapy', 'C) Orthognathic surgery as first-line pocket therapy', 'D) Quadrant or full-mouth scaling and root planing with risk-factor counseling'],
     'answer': 'D) Quadrant or full-mouth scaling and root planing with risk-factor counseling',
     'explanation': 'After hygiene motivation, nonsurgical debridement remains first-line for periodontitis with residual pockets and calculus. Surgery (including grafts) is considered after cause-related therapy; antifungals treat Candida, not bacterial periodontitis; orthognathic surgery is unrelated to primary pocket therapy.',
     'choice_explanations': {'A': 'Soft-tissue grafting is not first-line for untreated plaque-induced pocketing.', 'B': 'Antifungals do not address bacterial dysbiosis of periodontitis.', 'C': 'Jaw surgery does not replace periodontal cause-related therapy.', 'D': 'Applied periodontitis care: OHI then SRP and risk-factor control before resective/regenerative surgery.'}
    },
    {
     'question': 'Which local anatomic factor most commonly perpetuates plaque retention and localized periodontal destruction adjacent to a restoration?',
     'options': ['A) Overhanging restoration margin that harbors biofilm', 'B) Perfectly polished supragingival margin flush with enamel', 'C) Absence of any restoration on a smooth virgin tooth', 'D) Well-contoured open embrasure allowing cleaning access'],
     'answer': 'A) Overhanging restoration margin that harbors biofilm',
     'explanation': 'Overhangs and open margins create plaque-retentive niches that sustain localized inflammation and bone loss. Corrective recontouring or replacement improves cleansability. Flush polished margins and accessible embrasures favor health.',
     'choice_explanations': {'A': 'Restorative overhangs are classic local plaque traps that worsen localized periodontitis.', 'B': 'Flush polished margins minimize retention rather than perpetuate disease.', 'C': 'Virgin smooth enamel lacks the overhang niche described.', 'D': 'Open cleansable embrasures facilitate hygiene rather than trap plaque.'}
    },
    {
     'question': 'In a medically controlled diabetic patient with periodontitis, which applied counseling point is most accurate?',
     'options': ['A) Diabetes never influences periodontal inflammation', 'B) Bidirectional link: poorly controlled diabetes worsens periodontitis; periodontitis can impair glycemic control', 'C) Periodontal therapy is contraindicated in all diabetics', 'D) Only type 1 diabetes matters; type 2 is irrelevant'],
     'answer': 'B) Bidirectional link: poorly controlled diabetes worsens periodontitis; periodontitis can impair glycemic control',
     'explanation': 'Hyperglycemia impairs neutrophil function and wound healing and amplifies inflammatory tissue destruction; periodontitis raises systemic inflammatory burden that can worsen glycemic control. Periodontal therapy is indicated with medical coordination; both diabetes types can affect risk.',
     'choice_explanations': {'A': 'Diabetes clearly modifies host response and periodontitis severity.', 'B': 'Diabetes and periodontitis interact bidirectionally; therapy plus glycemic control are both important.', 'C': 'Diabetics benefit from periodontal care with appropriate precautions.', 'D': 'Type 2 diabetes is a major periodontitis risk modifier.'}
    },
   ],
   'hard': [
    {
     'question': 'A 42-year-old nonsmoker shows molar deep vertical defects, first-molar furcation grade II, thin phenotype, and plaque scores improved after SRP but 7 mm residual vertical defects remain with bleeding. Which multi-cue next step is most rational?',
     'options': ['A) Repeat only coronal polishing indefinitely without reevaluation', 'B) Extract all molars immediately without regenerative assessment', 'C) Consider periodontal surgery, often regenerative approaches for contained vertical/furcation defects after inflammation control', 'D) Place a cantilever bridge from canine to second molar without perio stability'],
     'answer': 'C) Consider periodontal surgery, often regenerative approaches for contained vertical/furcation defects after inflammation control',
     'explanation': 'After adequate nonsurgical therapy, residual deep vertical defects and grade II furcations may benefit from surgical access and regenerative materials when anatomy is favorable. Indefinite polishing alone, automatic extraction, or prosthetic loading of unstable periodontium are near-misses.',
     'choice_explanations': {'A': 'Coronal polishing does not debride deep residual defects adequately.', 'B': 'Not all such molars require extraction; regeneration may save teeth.', 'C': 'Residual deep vertical/furcation defects after SRP often warrant regenerative or resective surgical evaluation.', 'D': 'Prostheses on unstable periodontium accelerate failure.'}
    },
    {
     'question': 'A pregnant patient in the second trimester has pregnancy-associated gingival enlargement, bleeding, and plaque. Radiographs (already available pre-pregnancy) show mild bone loss. Which management vignette is most appropriate?',
     'options': ['A) Prescribe tetracycline mouthwash as first-line in pregnancy', 'B) Extract all first molars prophylactically in the first trimester', 'C) Take a full new FMX every month throughout pregnancy', 'D) Reinforce plaque control, provide gentle debridement as needed, and defer elective surgery until after delivery unless severe'],
     'answer': 'D) Reinforce plaque control, provide gentle debridement as needed, and defer elective surgery until after delivery unless severe',
     'explanation': 'Pregnancy gingivitis responds primarily to plaque control and careful debridement; elective periodontal surgery is usually postponed. Tetracyclines are avoided in pregnancy; unnecessary extractions and repeated monthly full-mouth radiographs violate ALARA and obstetric prudence.',
     'choice_explanations': {'A': 'Tetracyclines risk fetal tooth discoloration and are avoided in pregnancy.', 'B': 'Prophylactic molar extractions are not indicated for pregnancy gingivitis.', 'C': 'Monthly FMX contradicts ALARA; use radiographs only when justified.', 'D': 'Pregnancy periodontal care prioritizes hygiene and gentle debridement; avoid tetracyclines, elective surgery, and excess radiation.'}
    },
    {
     'question': 'A patient on long-term calcium-channel blockers develops firm lobulated gingival overgrowth covering half the crowns, with pseudopockets and plaque. Blood pressure is stable. Which multi-cue plan fits best?',
     'options': ['A) Intensify hygiene, consult the physician about alternative antihypertensives, then consider gingivectomy if fibrous overgrowth persists', 'B) Ignore drug history and only bleach the covered teeth', 'C) Stop the antihypertensive unilaterally in the dental chair', 'D) Place orthodontic brackets under the overgrown tissue immediately'],
     'answer': 'A) Intensify hygiene, consult the physician about alternative antihypertensives, then consider gingivectomy if fibrous overgrowth persists',
     'explanation': 'Drug-influenced gingival enlargement (e.g., nifedipine) is plaque-modulated. Management combines meticulous hygiene, medical consultation for drug substitution when possible, and surgical excision of residual fibrotic tissue. Dentists should not unilaterally stop antihypertensives; bleaching or bracketing under overgrowth fails to address etiology.',
     'choice_explanations': {'A': 'Drug-related overgrowth: hygiene + physician-coordinated drug review ± gingivectomy—not unilateral drug cessation or cosmetic cover-up.', 'B': 'Bleaching ignores drug and plaque-driven soft-tissue pathology.', 'C': 'Stopping BP medication without physician coordination risks hypertensive crisis.', 'D': 'Orthodontics under uncleansable overgrowth worsens inflammation.'}
    },
   ],
   'extreme': [
    {
     'question': 'A 29-year-old presents with rapidly progressing attachment loss, sparse plaque relative to destruction, neutrophil dysfunction history, and angular bone defects around incisors and first molars. Family history is positive. Which differential-driven plan is most appropriate?',
     'options': ['A) Treat as simple pregnancy gingivitis despite male sex and bone loss pattern', 'B) Suspect historically termed aggressive/molar-incisor pattern periodontitis, perform microbial/host risk assessment as indicated, deliver intensive mechanical therapy ± adjunctive antimicrobials per protocol, and screen relatives', 'C) Assume trauma from occlusion alone explains angular defects without biofilm control', 'D) Provide only whitening trays because the chief complaint is esthetics'],
     'answer': 'B) Suspect historically termed aggressive/molar-incisor pattern periodontitis, perform microbial/host risk assessment as indicated, deliver intensive mechanical therapy ± adjunctive antimicrobials per protocol, and screen relatives',
     'explanation': 'Molar-incisor rapid destruction with discordant plaque and familial aggregation suggests a distinct host–microbe trajectory formerly called aggressive periodontitis. Intensive mechanical debridement, risk-factor management, selective systemic/local antimicrobials when indicated, and family screening are appropriate. Mislabeling as pregnancy gingivitis, ignoring biofilm for occlusal trauma alone, or whitening-only care mismanages a destructive disease.',
     'choice_explanations': {'A': 'Male patient with bone loss is not pregnancy gingivitis.', 'B': 'Rapid molar-incisor destruction with host clues needs intensive periodontal therapy and family risk awareness—not cosmetic-only care.', 'C': 'Occlusal trauma may cofactor but does not replace anti-infective therapy.', 'D': 'Whitening does not stop attachment loss or treat pathogenesis.'}
    },
    {
     'question': 'Three years after implant placement, a patient shows bleeding, 7 mm peri-implant probing, radiographic cratering around a screw-retained molar implant, excess cement history on the prior crown, and poor oral hygiene. The implant is still immobile. What complication-management sequence is best?',
     'options': ['A) Ignore bleeding because implants cannot develop inflammatory bone loss', 'B) Tighten the implant by further torque into infected bone as sole therapy', 'C) Diagnose peri-implantitis, remove cement/plaque retentive factors, perform nonsurgical then often surgical decontamination/regeneration or resective therapy, and intensify maintenance', 'D) Prescribe antifungals alone without debridement or prosthetic correction'],
     'answer': 'C) Diagnose peri-implantitis, remove cement/plaque retentive factors, perform nonsurgical then often surgical decontamination/regeneration or resective therapy, and intensify maintenance',
     'explanation': 'Peri-implantitis features peri-implant soft-tissue inflammation plus progressive bone loss. Cement remnants and plaque are common drivers. Management removes etiologic factors, debrides contaminated surfaces (often surgically), and establishes strict maintenance; mobility would imply failure. Denial, further torque into infection, or antifungals alone are incorrect.',
     'choice_explanations': {'A': 'Implants are susceptible to peri-implant mucositis and peri-implantitis.', 'B': 'Additional torque does not resolve infection and may damage bone–implant interface.', 'C': 'Peri-implantitis needs etiologic factor removal, decontamination (often surgical), and maintenance—not denial or antifungal-only care.', 'D': 'Bacterial biofilm/cement, not Candida alone, typically drive peri-implantitis.'}
    },
    {
     'question': 'A stage IV periodontitis patient needs replacement of failing upper molars. Residual ridges show severe vertical defects, sinus pneumatization, and uncontrolled interproximal plaque on abutments of an old bridge. The patient requests immediate full-arch fixed implants this week. Which decision is most defensible?',
     'options': ['A) Place implants immediately through active periodontal pockets without hygiene phase', 'B) Guarantee lifelong implant success regardless of maintenance', 'C) Leave the uncleanable bridge and add cantilever pontics over inflamed abutments', 'D) Control periodontal infection first, then stage ridge/sinus evaluation and implant planning; do not place implants into uncontrolled periodontitis and uncleanable prosthetic designs'],
     'answer': 'D) Control periodontal infection first, then stage ridge/sinus evaluation and implant planning; do not place implants into uncontrolled periodontitis and uncleanable prosthetic designs',
     'explanation': 'Implants in patients with active periodontitis and poor hygiene have higher peri-implantitis risk. Stage IV cases need infection control, prosthetic cleansability redesign, and often staged bone augmentation/sinus assessment before reconstruction. Immediate implant placement into uncontrolled disease with success guarantees is unethical near-miss planning.',
     'choice_explanations': {'A': 'Active periodontitis elevates peri-implant biologic complication risk.', 'B': 'No implant system guarantees lifelong success without maintenance.', 'C': 'Extending uncleanable inflamed bridgework worsens prognosis.', 'D': 'Stabilize periodontitis and plan staged reconstruction; implants require infection control and maintainable prostheses.'}
    },
   ],
  },
  'cases': {
   'easy': [
    {'title': 'Bleeding Gums', 'stem': 'A student has bleeding on brushing, soft swollen gingiva, no radiographic bone loss.', 'question': 'Diagnosis?', 'answer': 'Plaque-induced gingivitis.', 'discussion': 'OHI and prophylaxis; reversible.', 'book_hint': "Carranza's Clinical Periodontology"},
   ],
   'medium': [
    {'title': 'Deep Pockets Molars', 'stem': 'A 45-year-old smoker has 6–7 mm pockets on molars with horizontal bone loss.', 'question': 'Management pillars?', 'answer': 'Risk factor control, nonsurgical debridement, re-evaluation, surgery if indicated.', 'discussion': 'Smoking cessation counseling.', 'book_hint': "Carranza's Clinical Periodontology"},
   ],
   'hard': [
    {'title': 'Diabetic with Recurrent Abscesses', 'stem': 'Poorly controlled diabetes, multiple periodontal abscesses, deep pockets. Choose the safest high-yield next concept before definitive results.', 'question': 'Priority concept?', 'answer': 'Medical coordination for glycemic control + acute drainage/debridement + definitive perio plan.', 'discussion': 'Diabetes and perio bidirectionally interact.', 'book_hint': "Carranza's Clinical Periodontology"},
   ],
   'extreme': [
    {'title': 'NUG in Stressed Student', 'stem': 'A stressed young adult smoker has punched-out papillae, severe pain, and fetor oris. Avoid harmful premature treatment while catastrophic differentials remain open.', 'question': 'Diagnosis and first care?', 'answer': 'NUG — gentle debridement, OHI, antiseptics, address risk factors; antibiotics if systemic/immunocompromise.', 'discussion': 'Rule out HIV/other immunodeficiency when atypical.', 'book_hint': "Carranza's Clinical Periodontology"},
   ],
  },
 },
 'endodontics': {
  'label': 'Endodontics',
  'books': ["Cohen's Pathways of the Pulp", 'Endodontics — Torabinejad', "Ingle's Endodontics"],
  'pdf_notes': ['Rubber dam is standard isolation for RCT.', 'Lingering spontaneous pain suggests irreversible pulpitis.', 'NaOCl irrigates but extrusion is dangerous.', 'Missed canals (MB2) cause failure.', 'Follow IADT for traumatic dental injuries.'],
  'questions': {
   'easy': [
    {
     'question': 'Irreversible pulpitis is best distinguished clinically from reversible pulpitis by which symptom pattern?',
     'options': ['A) Spontaneous or lingering pain to thermal stimuli that persists after stimulus removal', 'B) Brief nonlingering sensitivity only to cold that resolves instantly', 'C) Complete absence of response to all vitality tests with no symptoms ever', 'D) Pain only on biting that disappears with a bite stick away from the tooth'],
     'answer': 'A) Spontaneous or lingering pain to thermal stimuli that persists after stimulus removal',
     'explanation': 'Reversible pulpitis produces brief, nonlingering thermal sensitivity. Irreversible pulpitis typically features spontaneous pain or lingering thermal pain after stimulus removal, reflecting inflamed pulp tissue unlikely to heal without endodontic therapy. Nonresponse suggests necrosis; bite pain alone more often indicates periapical/occlusal issues or cracked tooth.',
     'choice_explanations': {'A': 'Lingering/spontaneous thermal pain characterizes irreversible pulpitis versus brief reversible sensitivity.', 'B': 'Brief nonlingering cold sensitivity fits reversible pulpitis.', 'C': 'No response suggests necrosis/previously treated pulp, not irreversible pulpitis symptoms.', 'D': 'Isolated bite pain points more to periapical or crack phenomena than classic irreversible pulpitis.'}
    },
    {
     'question': 'The working length in root canal treatment is ideally determined to which apical reference concept?',
     'options': ['A) Several millimeters beyond the radiographic apex into bone routinely', 'B) Near the apical constriction / cemento-dentinal junction region short of overinstrumentation', 'C) Exactly at the midroot level for all teeth', 'D) Only to the pulp chamber floor without entering canals'],
     'answer': 'B) Near the apical constriction / cemento-dentinal junction region short of overinstrumentation',
     'explanation': 'Instrumentation and obturation aim for the apical constriction (near CDJ), usually 0.5–1 mm short of the radiographic apex, confirmed with an apex locator and radiograph. Overinstrumentation beyond the apex damages periapical tissues; stopping at midroot or chamber floor leaves untreated canal infection.',
     'choice_explanations': {'A': 'Routine overinstrumentation beyond the apex risks debris extrusion and periapical trauma.', 'B': 'Working length targets the apical constriction region, not beyond the apex or midroot.', 'C': 'Midroot length leaves apical canal untreated.', 'D': 'Chamber-only treatment is not root canal therapy of the canal system.'}
    },
    {
     'question': 'Sodium hypochlorite is used as an endodontic irrigant primarily because it provides which dual action?',
     'options': ['A) Permanent enamel remineralization like topical fluoride', 'B) Radiopaque obturation of the canal space', 'C) Tissue dissolution and antimicrobial activity within the canal system', 'D) Selective anesthesia of the inferior alveolar nerve'],
     'answer': 'C) Tissue dissolution and antimicrobial activity within the canal system',
     'explanation': 'NaOCl dissolves necrotic pulp tissue and kills a broad spectrum of canal microbes, making it the primary irrigant. It is not a fluoride remineralizer, not an obturation material, and not a nerve block agent. Care avoids extrusion beyond the apex.',
     'choice_explanations': {'A': 'Fluoride, not NaOCl, is used for enamel remineralization.', 'B': 'Gutta-percha/sealer provide obturation radiopacity, not irrigant NaOCl.', 'C': 'NaOCl’s key endodontic roles are dissolving organic tissue and disinfecting canals.', 'D': 'Local anesthetics—not irrigants—block peripheral nerves.'}
    },
   ],
   'medium': [
    {
     'question': 'A tooth with necrotic pulp, sinus tract, and periapical radiolucency is best managed by which applied endodontic approach when restorability is adequate?',
     'options': ['A) Antibiotics alone without canal debridement', 'B) Indirect pulp cap over necrotic pulp tissue', 'C) Only occlusal adjustment without endodontic therapy', 'D) Nonsurgical root canal treatment to eliminate intracanal infection, with restoration of the tooth'],
     'answer': 'D) Nonsurgical root canal treatment to eliminate intracanal infection, with restoration of the tooth',
     'explanation': 'Periapical periodontitis from canal infection requires chemomechanical debridement and obturation (or extraction if unrestorable). Antibiotics alone do not sterilize canals; pulp capping is for vital pulp therapy scenarios, not necrosis; occlusal adjustment may aid comfort but does not remove infection.',
     'choice_explanations': {'A': 'Systemic antibiotics do not substitute for intracanal disinfection.', 'B': 'Pulp capping targets vital inflamed pulp, not necrotic infected canals.', 'C': 'Occlusal adjustment alone leaves the infectious source untreated.', 'D': 'Necrotic infected canals need RCT (or extraction), not antibiotics/pulp caps alone.'}
    },
    {
     'question': 'During instrumentation of a curved mesial canal, a ledge forms and the file no longer reaches prior working length. What is the most appropriate applied next concept?',
     'options': ['A) Re-establish glide path carefully with small flexible files; avoid forcing large stiff instruments that worsen the ledge', 'B) Immediately force a large Gates Glidden past the ledge at full length', 'C) Obturate short of the ledge without attempting to regain patency if goals allow ignoring infection', 'D) Flood the canal with undiluted eugenol as the sole corrective step'],
     'answer': 'A) Re-establish glide path carefully with small flexible files; avoid forcing large stiff instruments that worsen the ledge',
     'explanation': 'Ledges divert instruments from the original canal path. Recovery uses precurved small files, patience, and sometimes bypass techniques; forcing large instruments increases perforation/transport risk. Eugenol is a sealer/component, not a ledge remedy. Deliberately leaving untreated apical infection is not ideal when patency can be regained safely.',
     'choice_explanations': {'A': 'Regain the pathway with small flexible files; do not force large instruments that create perforations.', 'B': 'Forcing large instruments deepens transportation/perforation risk.', 'C': 'Leaving infected apical canal untreated is not the preferred first strategy when bypass is possible.', 'D': 'Eugenol does not correct a mechanical ledge.'}
    },
    {
     'question': 'A previously treated tooth has persistent apical radiolucency, inadequate obturation density, and missed second mesiobuccal canal suspected on CBCT. Which applied retreatment concept fits?',
     'options': ['A) Ignore CBCT findings because missed canals never cause failure', 'B) Nonsurgical retreatment to remove old obturation, locate missed anatomy, disinfect, and re-obturate', 'C) Place a post and crown without addressing intracanal infection', 'D) Prescribe antifungals as definitive endodontic retreatment'],
     'answer': 'B) Nonsurgical retreatment to remove old obturation, locate missed anatomy, disinfect, and re-obturate',
     'explanation': 'Persistent disease after RCT often relates to missed canals, inadequate cleaning, or coronal leakage. Nonsurgical retreatment addresses these factors; surgery is considered if retreatment is infeasible. Crowning over untreated infection and antifungal-only care are near-misses.',
     'choice_explanations': {'A': 'Missed canals are a classic cause of post-treatment apical periodontitis.', 'B': 'Failed RCT with missed anatomy warrants nonsurgical retreatment to disinfect the full canal system.', 'C': 'Restoring without infection control seals in bacteria.', 'D': 'Endodontic failure is primarily bacterial, not treated by antifungals alone.'}
    },
   ],
   'hard': [
    {
     'question': 'A 45-year-old has severe lingering cold pain on a maxillary first molar, referred pain to the ear, hypersensitive MB cusp, and a recent deep composite near the pulp horn. Cold test lingers 20 seconds on that tooth only; percussion is mild. Which diagnosis and first definitive therapy align?',
     'options': ['A) Reversible pulpitis—only desensitizing toothpaste without further care', 'B) Chronic apical abscess—incise the palate as sole therapy', 'C) Symptomatic irreversible pulpitis—initiate root canal treatment (or extraction if unrestorable) after profound anesthesia', 'D) Myofascial pain—occlusal splint only without pulp testing correlation'],
     'answer': 'C) Symptomatic irreversible pulpitis—initiate root canal treatment (or extraction if unrestorable) after profound anesthesia',
     'explanation': 'Lingering cold response localized to one tooth after deep restoration indicates symptomatic irreversible pulpitis; mild percussion can coexist early. Definitive care is RCT or extraction. Reversible pulpitis lacks lingering pain; abscess incision without canal therapy is incomplete; myofascial pain would not yield a single-tooth lingering cold test.',
     'choice_explanations': {'A': 'Lingering pain exceeds reversible pulpitis criteria.', 'B': 'No fluctuant abscess is described; source control is endodontic, not palate incision alone.', 'C': 'Lingering localized cold pain after deep restoration = irreversible pulpitis → RCT/extraction.', 'D': 'Positive tooth-specific lingering cold test contradicts a purely myofascial diagnosis.'}
    },
    {
     'question': 'Mid-RCT on a mandibular molar, the patient suddenly tastes bleach, the cheek swells, and severe pain occurs after irrigant expression. Which multi-cue complication plan is correct?',
     'options': ["A) Continue forceful irrigation to 'wash out' tissues beyond the apex", 'B) Ignore swelling because hypochlorite is harmless extracanal', 'C) Perform immediate hemimandibulectomy as first-line care', 'D) Recognize NaOCl extrusion accident: stop irrigation, aspirate, cold compresses early, analgesia, follow-up, and complete RCT later when acute phase allows'],
     'answer': 'D) Recognize NaOCl extrusion accident: stop irrigation, aspirate, cold compresses early, analgesia, follow-up, and complete RCT later when acute phase allows',
     'explanation': 'NaOCl accidents follow apical extrusion with sudden pain, swelling, and sometimes ecchymosis/taste of bleach. Management is supportive: halt irrigation, aspirate/canal flush with saline, pain control, cold then warm compresses per stage, antibiotics only if secondary infection, and complete endodontics carefully later. Further forceful irrigation worsens injury; resection is absurd.',
     'choice_explanations': {'A': 'More forceful irrigation increases soft-tissue chemical injury.', 'B': 'Extracanal NaOCl causes significant tissue damage and must not be ignored.', 'C': 'Hemimandibulectomy is not treatment for an irrigant accident.', 'D': 'NaOCl extrusion is managed supportively with cessation of irrigation, symptom control, and delayed careful completion—not more extrusion.'}
    },
    {
     'question': 'A cracked tooth has pain on release of biting, occasional cold sensitivity, a visible fracture line staining with dye, and no deep probing defect. Radiograph is normal. Which multi-cue management direction is best?',
     'options': ['A) Confirm crack with transillumination/bite testing, remove diseased tissue, and provide cuspal coverage if the tooth is restorable and pulp status allows', 'B) Ignore the crack and place only a small occlusal amalgam without coverage', 'C) Extract immediately every tooth with any enamel craze line', 'D) Treat with topical fluoride varnish as definitive crack therapy'],
     'answer': 'A) Confirm crack with transillumination/bite testing, remove diseased tissue, and provide cuspal coverage if the tooth is restorable and pulp status allows',
     'explanation': 'Cracked tooth syndrome often shows pain on release and may progress to pulp/periodontal involvement. After diagnosis, remove the crack-associated diseased structure and protect cusps (onlay/crown) when restorable; endodontics is added if pulp becomes irreversible/necrotic. Tiny amalgams without coverage, extracting all craze lines, or fluoride alone are near-misses.',
     'choice_explanations': {'A': 'Restorable cracks need diagnosis, removal of pathology, and cuspal coverage—not inadequate fills or automatic extraction.', 'B': 'Unprotected cusps allow crack propagation under occlusal load.', 'C': 'Enamel craze lines are common and not automatic extraction criteria.', 'D': 'Fluoride does not stabilize a structural crack.'}
    },
   ],
   'extreme': [
    {
     'question': 'A maxillary lateral incisor has failed twice after RCT, a persistent sinus tract, and CBCT showing a missed lateral canal and apical transportation. The tooth has a short post and adequate ferrule. The patient wants to keep the tooth. Which complex decision is most appropriate?',
     'options': ['A) Place a longer post through the transportation into bone as primary therapy', 'B) Attempt thorough nonsurgical retreatment with magnification to address missed anatomy if feasible; if not, consider apical surgery after infection control counseling, versus extraction/implant if prognosis poor', 'C) Cure the sinus tract with topical steroids alone indefinitely', 'D) Guarantee success with antibiotics for 12 months without canal revision'],
     'answer': 'B) Attempt thorough nonsurgical retreatment with magnification to address missed anatomy if feasible; if not, consider apical surgery after infection control counseling, versus extraction/implant if prognosis poor',
     'explanation': 'Persistent disease with missed anatomy favors nonsurgical retreatment under magnification. Apical surgery is considered when orthograde access is limited or transportation prevents adequate cleaning. Extending posts into bone, steroid pastes on tracts, or long-term antibiotics without source control are incorrect. Shared decision-making includes extraction if the prognosis remains unfavorable.',
     'choice_explanations': {'A': 'Posts beyond the root into bone risk damage and do not disinfect canals.', 'B': 'Failed RCT with missed anatomy: retreatment ± apical surgery after counseling—not posts into bone or antibiotics alone.', 'C': 'Sinus tracts resolve only when canal/periapical infection is controlled.', 'D': 'Antibiotics cannot replace intracanal or surgical source control.'}
    },
    {
     'question': 'An immature permanent central incisor suffered intrusion trauma 8 weeks ago. The tooth is asymptomatic, radiograph shows early periapical change, pulp tests are negative, and apex is wide open. Which regenerative/apexification decision framework fits best?',
     'options': ['A) Perform immediate full coverage crown preparation destroying remaining thin dentin walls without endodontic plan', 'B) Assume vitality forever because the tooth is asymptomatic at one visit', 'C) Confirm pulp necrosis, then choose apexification (e.g., bioceramic barrier) or regenerative endodontic procedures based on protocols, stage of root development, and informed consent', 'D) Extract and place a malposed implant before skeletal growth completion routinely'],
     'answer': 'C) Confirm pulp necrosis, then choose apexification (e.g., bioceramic barrier) or regenerative endodontic procedures based on protocols, stage of root development, and informed consent',
     'explanation': 'Intrusion can sever apical vasculature in immature teeth, leading to necrosis with open apex. Options include revitalization/regenerative procedures to encourage continued root development or apexification with a bioceramic apical barrier and obturation. Premature crowns on thin walls risk fracture; asymptomatic status does not prove vitality; implants in growing patients are generally deferred.',
     'choice_explanations': {'A': 'Aggressive crown prep on immature thin roots risks catastrophic fracture.', 'B': 'Negative tests plus radiographic change indicate necrosis despite quiet symptoms.', 'C': 'Necrotic immature incisors need apexification or regenerative endodontics—not premature crowns or pediatric implants.', 'D': 'Implants before growth completion risk infraocclusion; growth status matters.'}
    },
    {
     'question': 'During retreatment, a separated NiTi fragment lodges in the apical third of a curved MB canal of a strategic molar abutment. The tooth is symptomatic with apical radiolucency. Retrieval attempts begin to remove excessive dentin. What is the best complication-management judgment?',
     'options': ['A) Continue removing dentin indefinitely until the fragment is retrieved at any structural cost', 'B) Leave symptomatic apical disease without any disinfection attempt around/bypass the fragment', 'C) Tell the patient separated instruments always require immediate extraction', 'D) Balance retrieval versus bypass versus surgical options against remaining dentin thickness; stop when further chasing risks perforation/fracture, and discuss prognosis honestly'],
     'answer': 'D) Balance retrieval versus bypass versus surgical options against remaining dentin thickness; stop when further chasing risks perforation/fracture, and discuss prognosis honestly',
     'explanation': 'Separated instruments are managed by retrieval, bypass, or careful obturation around a fragment when retrieval would destroy the tooth—guided by location, curvature, and symptoms. Apical disease still needs disinfection as feasible; surgery may follow. Sacrificing all dentin, ignoring infection, or mandatory extraction are poor extremes.',
     'choice_explanations': {'A': 'Unlimited dentin removal risks vertical root fracture and tooth loss.', 'B': 'Symptomatic apical periodontitis still requires disinfection strategy around the obstacle.', 'C': 'Many separated-instrument cases remain restorable without extraction.', 'D': 'Instrument separation demands risk–benefit judgment: retrieve/bypass/surgery without destroying restorable dentin.'}
    },
   ],
  },
  'cases': {
   'easy': [
    {'title': 'Night Pain Lower Molar', 'stem': 'Spontaneous night pain, lingering cold response, no periapical radiolucency yet.', 'question': 'Likely pulp status?', 'answer': 'Symptomatic irreversible pulpitis.', 'discussion': 'RCT or extraction after consent.', 'book_hint': "Cohen's Pathways of the Pulp"},
   ],
   'medium': [
    {'title': 'Sinus Tract on Gingiva', 'stem': 'Chronic draining sinus over apex of nonvital lateral; radiolucency present.', 'question': 'Treatment concept?', 'answer': 'Root canal therapy of the source tooth (+ restore).', 'discussion': 'Trace sinus with gutta-percha if needed.', 'book_hint': "Cohen's Pathways of the Pulp"},
   ],
   'hard': [
    {'title': 'RCT Done but Pain Persists', 'stem': 'Upper 6 had RCT; pain on biting persists; J-shaped lesion on root. Choose the safest high-yield next concept before definitive results.', 'question': 'Suspect?', 'answer': 'Vertical root fracture or missed canal / perio-endo complex — investigate carefully.', 'discussion': 'CBCT may help; avoid endless retreat without diagnosis.', 'book_hint': "Cohen's Pathways of the Pulp"},
   ],
   'extreme': [
    {'title': 'Avulsion on Sports Field', 'stem': 'A 12-year-old avulses a permanent central; tooth was dry in a napkin for 90 minutes. Avoid harmful premature treatment while catastrophic differentials remain open.', 'question': 'Guideline concept?', 'answer': 'Extraoral dry time long → poor PDL prognosis; still follow IADT: clean carefully, consider replantation/splinting protocols, antibiotics/tetanus as indicated, close follow-up.', 'discussion': 'Do not scrub the root PDL remnant.', 'book_hint': "Cohen's Pathways of the Pulp"},
   ],
  },
 },
 'prosthodontics': {
  'label': 'Prosthodontics',
  'books': ['Contemporary Fixed Prosthodontics — Rosenstiel', "McCracken's Removable Partial Prosthodontics", 'Complete Denture Prosthodontics texts'],
  'pdf_notes': ['Ferrule improves crowned endodontically treated teeth.', 'Respect biologic width / supracrestal tissues.', 'Kennedy classification guides RPD design.', 'Passive fit matters for implant frameworks.', 'Disease control before full-mouth reconstruction.'],
  'questions': {
   'easy': [
    {
     'question': 'A ferrule in crown preparation refers primarily to which structural concept?',
     'options': ['A) A band of sound tooth structure encircling the preparation that resists fracture under crown leverage', 'B) The shade tab selected for porcelain only', 'C) The brand of temporary cement exclusively', 'D) The patient’s preferred denture adhesive flavor'],
     'answer': 'A) A band of sound tooth structure encircling the preparation that resists fracture under crown leverage',
     'explanation': 'Ferrule effect describes a circumferential collar of remaining axial tooth structure (often ≥1.5–2 mm) engaged by the crown, improving resistance to fracture especially in endodontically treated teeth. Shade and cement brand are separate prosthetic choices.',
     'choice_explanations': {'A': 'Ferrule = circumferential sound tooth structure under the crown that resists fracture.', 'B': 'Shade selection is esthetic, not the ferrule definition.', 'C': 'Temporary cement brand is unrelated to ferrule anatomy.', 'D': 'Denture adhesive is irrelevant to crown ferrule.'}
    },
    {
     'question': 'What is the primary purpose of border molding when fabricating a complete denture impression?',
     'options': ['A) Select tooth shade for the anterior denture teeth', 'B) Record the functional depth and width of the vestibule for a peripheral seal', 'C) Determine the patient’s freeway space only', 'D) Replace the need for any occlusal vertical dimension record'],
     'answer': 'B) Record the functional depth and width of the vestibule for a peripheral seal',
     'explanation': 'Border molding shapes the impression periphery to the physiologic vestibule so the finished denture flanges achieve retention via peripheral seal. Shade, freeway space, and OVD are related but separate prosthodontic records.',
     'choice_explanations': {'A': 'Shade selection is not accomplished by border molding.', 'B': 'Border molding captures functional vestibular borders for denture peripheral seal/retention.', 'C': 'Freeway space is assessed with OVD/rest vertical dimension, not border molding alone.', 'D': 'OVD still must be established separately from impression border molding.'}
    },
    {
     'question': 'In fixed prosthodontics, a key biologic reason to respect biologic width (supracrestal tissue attachment) is to avoid which outcome?',
     'options': ['A) Improved gingival health from intentional deep margin violation', 'B) Automatic pulp regeneration after every crown', 'C) Chronic inflammation and bone loss from restoration margins invading the attachment apparatus', 'D) Elimination of the need for oral hygiene'],
     'answer': 'C) Chronic inflammation and bone loss from restoration margins invading the attachment apparatus',
     'explanation': 'Placing margins that encroach on the supracrestal tissue attachment provokes inflammation, pocketing, and bone remodeling. Crown lengthening or alternative margin placement preserves biologic width. Deep violation does not improve health; crowns do not regenerate pulp; hygiene remains essential.',
     'choice_explanations': {'A': 'Intentional biologic width violation harms, rather than helps, gingival health.', 'B': 'Crowns do not regenerate pulp tissue.', 'C': 'Invading biologic width causes peri-restoration inflammation and bone loss.', 'D': 'Hygiene remains mandatory regardless of margin design.'}
    },
   ],
   'medium': [
    {
     'question': 'A patient will receive an RPD replacing several posterior teeth. Which applied design principle best protects abutment teeth?',
     'options': ['A) Omit all rests so the prosthesis only clasps soft tissue', 'B) Use clasps that release during function with no reciprocal arms ever', 'C) Ignore guide planes and allow continuous abutment torque', 'D) Provide adequate rest seats so occlusal loads are directed along the long axis and bases are properly supported'],
     'answer': 'D) Provide adequate rest seats so occlusal loads are directed along the long axis and bases are properly supported',
     'explanation': 'Rests transmit occlusal force to abutment long axes and prevent soft-tissue-borne settling that torques clasps. Reciprocation and guide planes also control path of insertion and bracing. Omitting rests or reciprocation increases abutment trauma.',
     'choice_explanations': {'A': 'Clasping without rests lets the denture sink and lever abutments.', 'B': 'Unreciprocated clasps can torque abutments during removal/insertion/function.', 'C': 'Guide planes and controlled path reduce harmful abutment forces.', 'D': 'Rests and supportive design direct RPD loads axially and spare abutments from torque.'}
    },
    {
     'question': 'When selecting occlusal vertical dimension for a complete denture wearer with worn dentition history, which applied approach is sound?',
     'options': ['A) Combine clinical rest position, speech (sibilant), esthetics, and residual ridge comfort rather than a single arbitrary number', 'B) Always open OVD by 10 mm regardless of rest space', 'C) Set OVD solely by the shade of the pink acrylic', 'D) Ignore phonetics because speech never changes with OVD'],
     'answer': 'A) Combine clinical rest position, speech (sibilant), esthetics, and residual ridge comfort rather than a single arbitrary number',
     'explanation': 'OVD determination uses multiple correlates—physiologic rest with freeway space, phonetics, facial esthetics, and patient comfort—then verified with trial bases. Arbitrary large openings risk muscle fatigue and instability; acrylic shade is irrelevant; speech is a classic verification tool.',
     'choice_explanations': {'A': 'OVD is verified by rest space, phonetics, esthetics, and comfort—not arbitrary opening or acrylic color.', 'B': 'Blind 10 mm opening often exceeds freeway space and destabilizes dentures.', 'C': 'Acrylic shade does not encode vertical dimension.', 'D': 'Sibilant sounds are commonly used to verify OVD.'}
    },
    {
     'question': 'A survey crown is planned for an RPD abutment. Which applied feature must be incorporated into the crown contour?',
     'options': ['A) Random bulbous contours without a surveyed path of insertion', 'B) Surveyed guide planes, rest seats, and appropriate undercut for the chosen clasp assembly', 'C) Elimination of all axial walls to soft tissue only', 'D) Occlusal anatomy copied from a deciduous molar only'],
     'answer': 'B) Surveyed guide planes, rest seats, and appropriate undercut for the chosen clasp assembly',
     'explanation': 'Survey crowns are waxed/milled to provide planned guide planes, rest seats, and clasp undercuts consistent with the RPD design. Uncontrolled contours defeat the path of insertion and clasping. Soft-tissue-only abutments and deciduous anatomy are inappropriate.',
     'choice_explanations': {'A': 'Unsurveyed bulbous crowns prevent a controlled path and proper clasp engagement.', 'B': 'Survey crowns must include designed guide planes, rests, and clasp undercuts.', 'C': 'Eliminating axial tooth structure destroys the abutment.', 'D': 'Primary molar anatomy is not the design template for adult survey crowns.'}
    },
   ],
   'hard': [
    {
     'question': 'A mandibular Kennedy Class I RPD candidate has distal extension ridges, periodontally reduced canines as abutments, and a history of prior denture sore spots. Which multi-cue design emphasis is most appropriate?',
     'options': ['A) Make the denture entirely tooth-borne on the canines with rigid bilateral distal occlusal loading only', 'B) Eliminate all acrylic bases so clasps alone replace molars', 'C) Maximize support from the edentulous ridge (accurate base adaptation/impression technique), use flexible stress distribution concepts, and protect weakened abutments', 'D) Use a maxillary complete denture design on the mandible unchanged'],
     'answer': 'C) Maximize support from the edentulous ridge (accurate base adaptation/impression technique), use flexible stress distribution concepts, and protect weakened abutments',
     'explanation': 'Distal extension RPDs share load between teeth and residual ridges; altered-cast or careful selective-pressure impressions improve ridge support. Periodontally reduced abutments need stress-breaking/flexible designs and rests that avoid cantilever overload. Purely tooth-borne distal loading or clasps without bases are near-misses.',
     'choice_explanations': {'A': 'Rigid tooth-only distal loading overloads weakened canines.', 'B': 'Clasps without bases cannot replace masticatory support of molars.', 'C': 'Class I distal extensions need ridge support and abutment-protective stress distribution.', 'D': 'Maxillary complete-denture design principles do not transplant unchanged to a mandibular RPD.'}
    },
    {
     'question': 'An anterior single implant crown shows screw loosening twice, occlusal contacts heavier in excursive movements than adjacent teeth, and a shallow anterior guidance scheme. Which multi-cue correction is best?',
     'options': ["A) Increase excursive overload intentionally to 'seat' the screw", 'B) Ignore occlusion because implants have periodontal ligaments that buffer all forces', 'C) Cement a crown over a loose screw without retrieving and retorquing', 'D) Correct occlusal scheme to lighten implant excursive contacts, ensure proper torque/preload, and reassess abutment fit before repeated failure'],
     'answer': 'D) Correct occlusal scheme to lighten implant excursive contacts, ensure proper torque/preload, and reassess abutment fit before repeated failure',
     'explanation': 'Implants lack a PDL shock absorber; excursive overload and inadequate preload commonly loosen screws. Management recalibrates occlusion (often lighter contacts especially in excursions), verifies component fit, and applies correct torque. Cementing over a loose screw traps the problem.',
     'choice_explanations': {'A': 'Increasing overload worsens screw joint failure.', 'B': 'Osseointegrated implants lack a PDL; they transmit force rigidly.', 'C': 'Cementing over a loose screw fails to restore preload and fit.', 'D': 'Recurrent implant screw loosening needs occlusal correction and proper torque—not added overload.'}
    },
    {
     'question': 'A patient with a high smile line needs a maxillary central crown. Preparation reveals a dark subgingival ferrule, thin biotype, and the patient refuses surgery. Which multi-cue prosthetic strategy is most coherent?',
     'options': ['A) Use opaque/masking strategies or material layering carefully, discuss gingival display limits, and consider conservative margin placement without violating biologic width', 'B) Place the margin deep into bone to hide color without counseling biologic width risk', 'C) Promise perfect pink esthetics identical to virgin teeth without material limits', 'D) Bleach the metal post through opaque porcelain by using water alone'],
     'answer': 'A) Use opaque/masking strategies or material layering carefully, discuss gingival display limits, and consider conservative margin placement without violating biologic width',
     'explanation': 'Dark substrates and thin biotypes challenge esthetics, especially with high smile lines. Options include opaque zirconia/core masking, opaque cements, or accepting slight compromise when crown lengthening/soft-tissue grafting is refused. Deep biologic width invasion risks chronic inflammation; water cannot bleach a metal post through ceramics.',
     'choice_explanations': {'A': 'Mask dark substrates within biologic width limits and set realistic high-smile-line expectations.', 'B': 'Deep bony margin placement violates attachment and invites chronic inflammation.', 'C': 'Material physics and soft tissue set limits; overpromising harms consent quality.', 'D': 'Water does not opacify metal show-through under porcelain.'}
    },
   ],
   'extreme': [
    {
     'question': "A completely edentulous patient with severely resorbed mandible, history of denture instability, and xerostomia from polypharmacy requests 'teeth in a day' fixed full-arch implants. CBCT shows limited anterior bone and proximity of the inferior alveolar nerves bilaterally. Which decision pathway is most responsible?",
     'options': ['A) Place posterior implants into the mandibular canals to gain AP spread at any neurologic cost', 'B) Explain anatomic limits, discuss implant-retained overdenture versus extensive grafting/alternative tilt strategies with realistic timelines, optimize saliva/prosthetic soft-tissue health, and avoid promising immediate fixed teeth when bone and soft tissue are inadequate', 'C) Guarantee fixed same-day teeth without imaging because resin bases always suffice', 'D) Ignore xerostomia because saliva never affects denture or peri-implant comfort'],
     'answer': 'B) Explain anatomic limits, discuss implant-retained overdenture versus extensive grafting/alternative tilt strategies with realistic timelines, optimize saliva/prosthetic soft-tissue health, and avoid promising immediate fixed teeth when bone and soft tissue are inadequate',
     'explanation': 'Severely resorbed mandibles constrain implant length/position; nerve injury risk precludes canal penetration. Two-implant overdentures often transform stability with less morbidity than full-arch fixed when bone is limited. Xerostomia worsens comfort and candidiasis risk. Immediate fixed full-arch promises without bone are unethical near-misses.',
     'choice_explanations': {'A': 'Implants in the IAN canal risk permanent neurosensory injury.', 'B': 'Limited mandibular bone and xerostomia favor honest alternatives (e.g., overdenture) over nerve-risking immediate fixed arches.', 'C': 'CBCT planning is mandatory; resin denture history does not prove implant bone adequacy.', 'D': 'Hyposalivation strongly affects prosthesis comfort and mucosal health.'}
    },
    {
     'question': 'An FPD from canine to second molar failed after the canine abutment split vertically. The premolars are missing; the molar has short clinical crown and short roots. The patient wants another five-unit bridge immediately. What complex prosthetic judgment is best?',
     'options': ['A) Recement the split canine fragments under a new longer cantilever bridge without addressing structure', 'B) Use the fractured canine indefinitely as a lone abutment for a distal cantilever to the molar', 'C) Recognize long-span FPD with poor abutments as high failure risk; consider implant replacement of missing units or removable options after extracting the fractured canine and evaluating the molar’s true abutment value', 'D) Promise that any span length is equally successful if porcelain is layered thickly'],
     'answer': 'C) Recognize long-span FPD with poor abutments as high failure risk; consider implant replacement of missing units or removable options after extracting the fractured canine and evaluating the molar’s true abutment value',
     'explanation': 'Ante’s law and biomechanics caution against long spans on compromised abutments; a vertically fractured canine is unrestorable as an abutment. Implants to replace missing premolars (or an RPD) after removing the fractured tooth usually outperform repeating a doomed FPD. Cantilevering from a fractured root or claiming porcelain thickness overcomes span physics is incorrect.',
     'choice_explanations': {'A': 'Split roots cannot be reliably recombined as abutments under load.', 'B': 'Cantilevers from hopeless roots accelerate failure.', 'C': 'Failed long-span FPD with fractured abutment needs redesign (implants/RPD), not another overloaded bridge.', 'D': 'Porcelain thickness does not compensate for inadequate abutment support.'}
    },
    {
     'question': 'A maxillary complete denture opposes a Kennedy Class I RPD. The patient develops combination syndrome features: flabby anterior maxilla, papillary hyperplasia, mandibular posterior ridge resorption, and overgrown tuberosities. Which complication-management plan is most coherent?',
     'options': ["A) Add more anterior maxillary occlusal contact exclusively to 'stabilize' the denture", 'B) Ignore flabby tissue and take a single heavy pressure impression that displaces it maximally without relief', 'C) Extract the mandibular residual ridge prophylactically to match the maxilla', 'D) Correct occlusal plane/posterior support, consider surgical management of hyperplasia/flabby tissue as needed, reline or remake prostheses, and educate about leaving dentures out at night'],
     'answer': 'D) Correct occlusal plane/posterior support, consider surgical management of hyperplasia/flabby tissue as needed, reline or remake prostheses, and educate about leaving dentures out at night',
     'explanation': 'Combination syndrome stems from lack of mandibular posterior support and excessive anterior maxillary loading. Therapy restores posterior occlusion, manages hyperplastic/flabby tissues (often with surgery or specialized impressions), and remakes/relines prostheses. Increasing anterior contacts worsens the syndrome; amputating ridges is not therapy.',
     'choice_explanations': {'A': 'Anterior-only contacts drive further maxillary flabby change and bone loss.', 'B': 'Unrelieved heavy displacement of flabby tissue yields unstable denture bases.', 'C': 'Resecting mandibular ridges destroys support needed for the RPD.', 'D': 'Combination syndrome needs posterior support restoration and soft-tissue/prosthesis correction—not more anterior loading.'}
    },
   ],
  },
  'cases': {
   'easy': [
    {'title': 'Broken Molar Crown', 'stem': 'A patient wants a crown on a root-filled molar with adequate ferrule.', 'question': 'Plan outline?', 'answer': 'Assess restorability, post if needed, core, crown.', 'discussion': 'Extract if unrestorable.', 'book_hint': 'Contemporary Fixed Prosthodontics — Rosenstiel'},
   ],
   'medium': [
    {'title': 'Distal Extension RPD Rocks', 'stem': 'Kennedy I lower RPD rocks and sore spots on ridge.', 'question': 'Likely issue?', 'answer': 'Support/retention/occlusion imbalance on distal extension — adjust base, rests, occlusion.', 'discussion': 'Tissue-borne areas need careful loading.', 'book_hint': 'Contemporary Fixed Prosthodontics — Rosenstiel'},
   ],
   'hard': [
    {'title': 'Deep Margin Near Bone', 'stem': 'Crown prep finish line violates biologic width with persistent bleeding. Choose the safest high-yield next concept before definitive results.', 'question': 'Options?', 'answer': 'Crown lengthening or orthodontic extrusion before final restoration.', 'discussion': 'Do not cement and hope.', 'book_hint': 'Contemporary Fixed Prosthodontics — Rosenstiel'},
   ],
   'extreme': [
    {'title': 'Failing Full Arch Hybrids', 'stem': 'Multiple implant prostheses with screw loosening, misfit, and peri-implant bone loss. Avoid harmful premature treatment while catastrophic differentials remain open.', 'question': 'Concept?', 'answer': 'Remove/replace passive fit, control occlusion, treat peri-implant disease, reassess biomechanics.', 'discussion': 'Do not keep tightening screws blindly.', 'book_hint': 'Contemporary Fixed Prosthodontics — Rosenstiel'},
   ],
  },
 },
 'pediatric_dentistry': {
  'label': 'Pediatric Dentistry',
  'books': ["McDonald and Avery's Dentistry for the Child and Adolescent", 'Paediatric Dentistry — Welbury', 'Clinical Cases in Pediatric Dentistry'],
  'pdf_notes': ['20 primary teeth; first permanent molar about age 6.', 'ECC often affects maxillary anteriors with bottle habits.', 'SSC common for multi-surface primary molar caries.', 'Generally do not replant avulsed primary teeth.', 'Safeguarding: inconsistent injury histories.'],
  'questions': {
   'easy': [
    {
     'question': 'The first permanent tooth to erupt in most children is which tooth?',
     'options': ['A) Mandibular first permanent molar', 'B) Maxillary permanent canine', 'C) Mandibular permanent third molar', 'D) Maxillary permanent lateral incisor exclusively before all others in every child'],
     'answer': 'A) Mandibular first permanent molar',
     'explanation': 'The mandibular first permanent molar typically erupts around age 6 and is often the first permanent tooth, erupting distal to the primary second molar. Canines and third molars erupt much later; lateral incisors are not universally first.',
     'choice_explanations': {'A': 'Mandibular first permanent molars usually erupt first among permanent teeth (~age 6).', 'B': 'Permanent canines erupt later in the mixed dentition sequence.', 'C': 'Third molars erupt in late adolescence/early adulthood.', 'D': 'Lateral incisors are not the first permanent teeth in the usual sequence.'}
    },
    {
     'question': 'A primary molar with a deep carious lesion is asymptomatic, has a healthy permanent successor, and more than a year before exfoliation. When pulp is exposed but vital and inflammation is limited to the coronal pulp, which therapy is most appropriate?',
     'options': ['A) Immediate orthodontic extraction of all permanent successors', 'B) Pulpotomy with suitable medicament and a sealed restoration', 'C) Adult-length cast post and core as first-line', 'D) No restoration after leaving carious exposure open to saliva'],
     'answer': 'B) Pulpotomy with suitable medicament and a sealed restoration',
     'explanation': 'Vital primary molar pulpotomy removes inflamed coronal pulp, preserves radicular pulp, and maintains the tooth until exfoliation when criteria are met. Adult posts are inappropriate in primary teeth; open exposures invite infection; extracting permanent successors is harmful.',
     'choice_explanations': {'A': 'Permanent successors should be preserved, not electively extracted.', 'B': 'Vital primary molar with coronal pulp inflammation often receives pulpotomy plus sealed restoration.', 'C': 'Cast posts are adult restorative concepts unsuitable as primary pulp therapy.', 'D': 'Leaving exposures open risks pulp necrosis and infection.'}
    },
    {
     'question': 'Topical fluoride varnish is used in children primarily to achieve which effect?',
     'options': ['A) Replace the need for any dietary counseling forever', 'B) Anesthetize the inferior alveolar nerve for extractions', 'C) Promote remineralization and reduce caries incidence/progression on enamel', 'D) Bleach tetracycline-stained dentin permanently in one visit'],
     'answer': 'C) Promote remineralization and reduce caries incidence/progression on enamel',
     'explanation': 'Fluoride varnish delivers high-concentration fluoride that favors remineralization and caries prevention, especially in high-risk children. It does not replace diet advice, produce nerve blocks, or permanently bleach tetracycline stains in one application.',
     'choice_explanations': {'A': 'Diet and hygiene counseling remain essential alongside fluoride.', 'B': 'Local anesthetics—not fluoride—provide nerve block anesthesia.', 'C': 'Fluoride varnish aids enamel remineralization and caries prevention.', 'D': 'Tetracycline staining is not reliably erased by a single varnish visit.'}
    },
   ],
   'medium': [
    {
     'question': 'A 4-year-old sustains lateral luxation of a primary maxillary incisor with occlusal interference. The permanent successor bud is not apparently intruded on radiograph. Which applied management is most appropriate?',
     'options': ['A) Perform apexification with a long post in the primary root', 'B) Always leave interfering luxated primary teeth untreated regardless of bite trauma', 'C) Place an implant immediately in the 4-year-old socket', 'D) Reposition if needed for function/esthetics or extract if the tooth poses aspiration risk or interferes severely; avoid rigid prolonged immobilization typical of some permanent-tooth protocols'],
     'answer': 'D) Reposition if needed for function/esthetics or extract if the tooth poses aspiration risk or interferes severely; avoid rigid prolonged immobilization typical of some permanent-tooth protocols',
     'explanation': 'Primary luxation management prioritizes the permanent successor and airway safety. Mild cases may be observed; interfering or severely displaced teeth are repositioned carefully or extracted. Prolonged rigid splinting and adult endodontic/implant approaches are inappropriate in preschoolers.',
     'choice_explanations': {'A': 'Apexification posts are not used as routine primary luxation care.', 'B': 'Occlusal interference can traumatize tissues and needs management.', 'C': 'Implants are contraindicated in growing preschool children for such injuries.', 'D': 'Primary luxation: careful reposition or extract if interfering/unsafe—avoid adult implant/post protocols.'}
    },
    {
     'question': 'Space maintenance after early loss of a primary second molar is most critical to prevent which applied consequence?',
     'options': ['A) Mesial drift of the first permanent molar with loss of leeway/arch space', 'B) Immediate fusion of the maxillary tuberosities', 'C) Mandatory agenesis of the permanent successor', 'D) Spontaneous formation of a new primary tooth'],
     'answer': 'A) Mesial drift of the first permanent molar with loss of leeway/arch space',
     'explanation': 'Early loss of primary second molars allows first permanent molars to drift mesially, consuming space for premolars and risking crowding/impaction. Space maintainers preserve that dimension until the successor erupts. Loss does not cause tuberosity fusion, agenesis, or new primary tooth formation.',
     'choice_explanations': {'A': 'Space maintainers prevent mesial molar drift and space loss after early primary second molar loss.', 'B': 'Tuberosity fusion is not the consequence prevented by space maintenance.', 'C': 'Successor agenesis is genetic/developmental, not caused by space loss alone.', 'D': 'Humans do not regenerate a new primary tooth after loss.'}
    },
    {
     'question': 'A child with early childhood caries needs multiple extractions under general anesthesia. Which applied preoperative principle is essential?',
     'options': ['A) Feed a large meal immediately before induction to keep energy up', 'B) Medical history/NPO status review, informed consent including risks, and a comprehensive restorative/extraction plan to minimize repeat anesthesia', 'C) Skip consent because the child cannot legally understand anything', 'D) Plan only one tooth per GA session intentionally for many repeats'],
     'answer': 'B) Medical history/NPO status review, informed consent including risks, and a comprehensive restorative/extraction plan to minimize repeat anesthesia',
     'explanation': 'Pediatric GA dentistry requires medical assessment, strict NPO, parental consent/assent as appropriate, and ideally complete treatment in one session to avoid repeated anesthetic exposures. Feeding before induction risks aspiration; skipping consent is unethical; intentionally fragmenting care increases anesthetic risk.',
     'choice_explanations': {'A': 'Pre-induction feeding violates NPO and risks aspiration.', 'B': 'Pediatric dental GA needs NPO/medical clearance, consent, and comprehensive single-session planning.', 'C': 'Parents/guardians must consent; children are still owed age-appropriate explanation.', 'D': 'Minimizing repeat GA is a core pediatric anesthesia safety principle.'}
    },
   ],
   'hard': [
    {
     'question': 'An 8-year-old has an avulsed permanent central incisor with 45 minutes dry extraoral time, an open apex, and the tooth brought in milk after an initial dry period. Which multi-cue replantation decision is best?',
     'options': ['A) Scrub the root vigorously with bleach and leave the tooth out overnight', 'B) Discard the permanent incisor because open apex teeth never reattach', 'C) Replant after gentle cleaning as indicated, flexible splint, pulp management strategy for open apex (often revascularization attempt vs endodontics timing per guidelines), and tetanus/antibiotics consideration per protocol', 'D) Replant and perform immediate complete root resection to the CEJ'],
     'answer': 'C) Replant after gentle cleaning as indicated, flexible splint, pulp management strategy for open apex (often revascularization attempt vs endodontics timing per guidelines), and tetanus/antibiotics consideration per protocol',
     'explanation': 'Avulsed permanent teeth should be replanted ASAP; storage medium and dry time affect PDL survival. Open-apex teeth may attempt revascularization; endodontic timing differs from closed apex. Vigorous scrubbing, delayed discard, or resecting to CEJ are incorrect. Follow IADT-aligned splinting and follow-up.',
     'choice_explanations': {'A': 'Bleach scrubbing kills PDL cells needed for reattachment.', 'B': 'Open-apex teeth can reattach and sometimes revascularize; they should not be discarded routinely.', 'C': 'Avulsed permanent incisors: replant, flexible splint, and stage pulp care—especially considering open apex biology.', 'D': 'Resection to CEJ destroys the tooth rather than managing avulsion.'}
    },
    {
     'question': 'A 6-year-old with a deep carious primary second molar shows furcation radiolucency, mobility, and night pain. The permanent premolar is present. Which multi-cue therapy is most appropriate?',
     'options': ['A) Attempt direct pulp capping of necrotic furcation disease as definitive care', 'B) Perform adult molar uprighting with heavy orthodontic forces immediately', 'C) Ignore infection because primary teeth cannot affect permanent successors', 'D) Extract the primary molar and place a space maintainer if the successor will not erupt imminently'],
     'answer': 'D) Extract the primary molar and place a space maintainer if the successor will not erupt imminently',
     'explanation': 'Furcation involvement and mobility with symptoms indicate infection beyond vital pulp therapy criteria for primary molars—extraction is indicated. Space maintenance prevents mesial drift of the first permanent molar. Pulp capping fails in necrotic infected primary molars; infection can damage successors.',
     'choice_explanations': {'A': 'Pulp capping is inappropriate for necrotic infected primary molars with furcation pathosis.', 'B': 'Heavy adult ortho forces are not the acute infection treatment.', 'C': 'Primary molar infection can damage developing premolar follicles.', 'D': 'Infected nonrestorable primary molar with furcation disease → extract ± space maintainer.'}
    },
    {
     'question': 'A child with special healthcare needs has moderate caries, limited cooperative ability, and takes medication causing xerostomia. Behavioral attempts fail for quadrant dentistry. Which multi-cue plan is most appropriate?',
     'options': ['A) Use medical consultation as needed, consider sedation/GA pathways with caries-risk control (fluoride, diet, saliva substitutes), and prioritize infection control', 'B) Withhold all fluoride because special needs children never get caries', 'C) Force lengthy chair treatment without consent while ignoring medical meds', 'D) Assume xerostomia medications are irrelevant to caries risk'],
     'answer': 'A) Use medical consultation as needed, consider sedation/GA pathways with caries-risk control (fluoride, diet, saliva substitutes), and prioritize infection control',
     'explanation': 'SHCN children often need advanced behavior guidance/sedation/GA plus aggressive prevention because xerostomia and hygiene limits raise caries risk. Treatment planning integrates medical status and prevention. Withholding fluoride, forcing care without consent, or ignoring xerostomia are near-misses.',
     'choice_explanations': {'A': 'SHCN dentistry combines prevention, medical coordination, and appropriate sedation/GA—not forced unsafe care.', 'B': 'SHCN populations often have higher caries risk; fluoride is important.', 'C': 'Consent and medical awareness are mandatory; forced care is unethical/unsafe.', 'D': 'Xerostomia markedly elevates caries risk and needs management.'}
    },
   ],
   'extreme': [
    {
     'question': 'A 9-year-old with hemophilia A (moderate factor VIII deficiency) needs extraction of an abscessed primary molar. The child is otherwise stable; local swelling is mild. Which complex perioperative decision is best?',
     'options': ['A) Extract in office without hematology contact because primary teeth never bleed', 'B) Coordinate with hematology for factor replacement/hemostatic plan, use atraumatic technique and local hemostatic measures, and avoid unsupervised NSAID overuse; do not extract without hematologic planning', 'C) Give intramuscular aspirin for pain control before surgery', 'D) Perform elective full-mouth prophylaxis surgery under no hemostatic cover for efficiency'],
     'answer': 'B) Coordinate with hematology for factor replacement/hemostatic plan, use atraumatic technique and local hemostatic measures, and avoid unsupervised NSAID overuse; do not extract without hematologic planning',
     'explanation': 'Hemophilia requires specialty coordination for factor coverage or other hemostatic regimens before invasive dental surgery. Local measures (sutures, oxidized cellulose, tranexamic acid) complement systemic planning. Aspirin/NSAIDs can worsen bleeding; unsupervised extraction risks prolonged hemorrhage.',
     'choice_explanations': {'A': 'Primary tooth extractions can bleed substantially in coagulopathy.', 'B': 'Hemophilia extractions need hematology-coordinated factor/hemostasis plans plus local measures—not aspirin or blind surgery.', 'C': 'Aspirin impairs platelets and is inappropriate peri-extraction analgesia here.', 'D': 'Elective extensive surgery without hemostatic cover is dangerous.'}
    },
    {
     'question': 'After avulsion replantation of a permanent central with prolonged dry time, follow-up radiographs at 8 months show progressive replacement resorption (ankylosis) and infraocclusion in a growing child. Which long-term complication-management concept is most appropriate?',
     'options': ['A) Guarantee the ankylosed tooth will erupt normally with the jaw forever', 'B) Orthodontically extrude heavily against ankylosis as if the PDL were normal', 'C) Counsel about inevitable progressive infraocclusion/replacement resorption, plan decoronation or timed extraction with space maintenance/prosthetic transition to preserve alveolar ridge for future implant after growth', 'D) Place an immediate adult-length implant and porcelain crown in the 9-year-old'],
     'answer': 'C) Counsel about inevitable progressive infraocclusion/replacement resorption, plan decoronation or timed extraction with space maintenance/prosthetic transition to preserve alveolar ridge for future implant after growth',
     'explanation': 'Replacement resorption after severe PDL damage ankyloses the tooth, which then infraoccludes as the alveolus grows. Decoronation can preserve ridge height until growth completion for later implant. Guaranteeing eruption, forcing ortho against ankylosis, or pediatric implants with adult crowns are incorrect.',
     'choice_explanations': {'A': 'Ankylosed teeth do not erupt with vertical alveolar growth.', 'B': 'Orthodontic extrusion fails when PDL is replaced by bone (ankylosis).', 'C': 'Ankylosis/infraocclusion in growers needs decoronation/space planning for future implants—not forced eruption or child implants.', 'D': 'Implants before growth completion infraocclude relative to adjacent erupting teeth.'}
    },
    {
     'question': 'A 3-year-old with severe early childhood caries, failure-to-thrive concerns, facial swelling from a lower molar, and fever presents late Friday. Parents refuse hospital referral hoping for only antibiotics at home. Which decision prioritizes safety?',
     'options': ['A) Agree that antibiotics alone always cure pediatric fascial infections without drainage', 'B) Discharge without safety-net advice because fever is protective', 'C) Extract teeth in an uncooperative septic toddler in a non-airway-ready setting against best judgment', 'D) Explain odontogenic infection with systemic signs needs urgent source control and possible hospital IV care; do not rely on oral antibiotics alone, and document informed refusal if they decline after clear risk discussion'],
     'answer': 'D) Explain odontogenic infection with systemic signs needs urgent source control and possible hospital IV care; do not rely on oral antibiotics alone, and document informed refusal if they decline after clear risk discussion',
     'explanation': 'Pediatric odontogenic infections with fever/swelling can progress rapidly; antibiotics without source control are insufficient, and airway-capable settings may be required. Clear counseling and urgent referral are mandatory; unsafe office extraction under sepsis without airway support risks catastrophe. Document refusal if parents decline recommended care.',
     'choice_explanations': {'A': 'Antibiotics without drainage/extraction often fail in established abscesses.', 'B': 'Fever with facial swelling warrants safety-netting and often escalation, not casual discharge.', 'C': 'Septic uncooperative children need controlled settings, not heroic unsafe extractions.', 'D': 'Systemically ill children with dental abscesses need urgent source control/hospital pathways—not home antibiotics alone.'}
    },
   ],
  },
  'cases': {
   'easy': [
    {'title': 'Carious Primary Molar', 'stem': 'A 5-year-old has a deep cavity in a primary molar, no mobility, restorable.', 'question': 'Options concept?', 'answer': 'Restore ± pulp therapy if indicated; space importance.', 'discussion': 'Extraction needs space management plan.', 'book_hint': "McDonald and Avery's Dentistry for the Child and Adolescent"},
   ],
   'medium': [
    {'title': 'Bottle Caries', 'stem': 'A 3-year-old sleeps with a juice bottle; upper incisors carious.', 'question': 'Diagnosis theme?', 'answer': 'Early childhood caries — stop habit, restore/prevent, fluoride, diet counseling.', 'discussion': 'Lower incisors often relatively spared.', 'book_hint': "McDonald and Avery's Dentistry for the Child and Adolescent"},
   ],
   'hard': [
    {'title': 'Intruded Primary Incisor', 'stem': 'A 4-year-old intrudes a primary central after a fall; tooth appears missing clinically. Choose the safest high-yield next concept before definitive results.', 'question': 'Concern?', 'answer': 'Possible displacement toward permanent bud — radiograph, careful monitoring, avoid aggressive replantation of primary.', 'discussion': 'Watch permanent successor.', 'book_hint': "McDonald and Avery's Dentistry for the Child and Adolescent"},
   ],
   'extreme': [
    {'title': 'Unexplained Torn Frenum Toddler', 'stem': 'A toddler has a torn labial frenum and bruises of different ages; story keeps changing. Avoid harmful premature treatment while catastrophic differentials remain open.', 'question': 'Action concept?', 'answer': 'Consider non-accidental injury — document, treat dental needs, follow safeguarding protocols.', 'discussion': 'Do not discharge without appropriate pathway.', 'book_hint': "McDonald and Avery's Dentistry for the Child and Adolescent"},
   ],
  },
 },
 'oral_medicine': {
  'label': 'Oral Medicine & Pathology',
  'books': ['Oral and Maxillofacial Pathology — Neville', "Cawson's Essentials of Oral Pathology", 'Oral Medicine — Odell'],
  'pdf_notes': ['Aphthae on non-keratinized mucosa; HSV often keratinized.', 'Leukoplakia: non-wipeable white patch — risk stratify/biopsy.', 'Tobacco + alcohol raise SCC risk.', 'Nonhealing ulcer >2 weeks needs biopsy.', 'Candida: look for risk factors and wipeable plaques.'],
  'questions': {
   'easy': [
    {
     'question': 'Oral candidiasis (thrush) is most often associated with overgrowth of which organism in predisposed hosts?',
     'options': ['A) Candida albicans', 'B) Streptococcus mutans exclusively as a fungal pathogen', 'C) Herpes simplex virus type 1 as a yeast', 'D) Porphyromonas gingivalis as the cause of white scrapable plaques only'],
     'answer': 'A) Candida albicans',
     'explanation': 'Candida albicans is the predominant yeast causing oral candidiasis, especially with xerostomia, antibiotics, steroids, dentures, or immunosuppression. S. mutans is cariogenic bacteria; HSV is viral; P. gingivalis is periodontal, not the classic thrush organism.',
     'choice_explanations': {'A': 'Oral thrush is most often Candida albicans overgrowth in a predisposed host.', 'B': 'S. mutans is a bacterium linked to caries, not a fungus causing thrush.', 'C': 'HSV causes viral ulcerations, not yeast plaques.', 'D': 'P. gingivalis is associated with periodontitis, not classic scrapable candidal plaques.'}
    },
    {
     'question': 'Recurrent herpes labialis lesions are driven by reactivation of which virus typically latent in which ganglion?',
     'options': ['A) HIV latent only in salivary duct epithelium as the sole mechanism', 'B) HSV-1 latent in the trigeminal ganglion', 'C) HPV-16 latent in the geniculate ganglion causing cold sores', 'D) Epstein–Barr virus latent in the dorsal root ganglion causing lip vesicles'],
     'answer': 'B) HSV-1 latent in the trigeminal ganglion',
     'explanation': 'HSV-1 establishes latency in trigeminal sensory ganglia and reactivates along nerve distributions to produce herpes labialis. HIV, oncogenic HPV, and EBV have different clinical oral patterns and latency sites.',
     'choice_explanations': {'A': 'HIV does not explain classic recurrent herpes labialis latency biology.', 'B': 'Herpes labialis: HSV-1 reactivation from trigeminal ganglion latency.', 'C': 'HPV-16 is linked to oropharyngeal cancer risk, not typical cold-sore vesicles from geniculate latency.', 'D': 'EBV is linked to hairy leukoplakia/other disease, not classic herpes labialis from DRG.'}
    },
    {
     'question': 'A white patch that cannot be wiped off and is not clinically diagnostic as another disease is termed which clinical lesion pending diagnosis?',
     'options': ['A) Geographic tongue with migrating red patches only', 'B) Linea alba as an obligatory carcinoma', 'C) Leukoplakia (a clinical term requiring risk assessment and often biopsy)', 'D) Scrapable candidal pseudomembrane that wipes clean leaving normal mucosa'],
     'answer': 'C) Leukoplakia (a clinical term requiring risk assessment and often biopsy)',
     'explanation': 'Leukoplakia is a clinical diagnosis of exclusion for a persistent white patch that cannot be scraped off; histopathology determines dysplasia/risk. Geographic tongue, linea alba, and wipeable thrush are different entities.',
     'choice_explanations': {'A': 'Geographic tongue features migrating depapillated areas, not fixed nonwipeable leukoplakia.', 'B': 'Linea alba is a benign frictional line, not obligatory cancer.', 'C': 'Nonwipeable undiagnosed white patch = clinical leukoplakia until proven otherwise by assessment/biopsy.', 'D': 'Wipeable white plaques suggest pseudomembranous candidiasis, not leukoplakia.'}
    },
   ],
   'medium': [
    {
     'question': 'A patient with Sjögren syndrome reports dry mouth and rampant caries at cervical margins. Which applied dental management emphasis is most appropriate?',
     'options': ['A) Discourage fluoride because enamel is unaffected by hyposalivation', 'B) Prescribe anticholinergics to further reduce saliva', 'C) Ignore caries risk because autoimmune disease protects enamel', 'D) Salivary substitutes/stimulants as indicated, meticulous hygiene, high-fluoride regimens, and frequent recall'],
     'answer': 'D) Salivary substitutes/stimulants as indicated, meticulous hygiene, high-fluoride regimens, and frequent recall',
     'explanation': 'Hyposalivation from Sjögren markedly elevates caries risk. Management includes saliva support, dietary counseling, topical fluorides, and close surveillance. Anticholinergics worsen dryness; fluoride is essential, not contraindicated.',
     'choice_explanations': {'A': 'Hyposalivation increases—not decreases—need for fluoride protection.', 'B': 'Anticholinergics exacerbate xerostomia and caries risk.', 'C': 'Autoimmune hyposalivation increases caries risk rather than protecting enamel.', 'D': 'Sjögren xerostomia needs saliva support, fluoride, hygiene, and frequent recall.'}
    },
    {
     'question': 'A middle-aged patient presents with bilateral white reticular buccal striae without ulceration and is otherwise comfortable. Which applied working diagnosis is most likely?',
     'options': ['A) Oral lichen planus (reticular form)', 'B) Acute necrotizing ulcerative gingivitis as the first diagnosis', 'C) Traumatic fibroma of the buccal mucosa exclusively', 'D) Periapical abscess of a molar without dental findings'],
     'answer': 'A) Oral lichen planus (reticular form)',
     'explanation': 'Reticular oral lichen planus classically shows bilateral Wickham-like striae on buccal mucosa and may be asymptomatic. ANUG features painful necrotic interdental papillae; fibromas are focal nodules; periapical abscess is odontogenic and localized.',
     'choice_explanations': {'A': 'Bilateral reticular buccal striae are classic for reticular oral lichen planus.', 'B': 'ANUG presents with painful punched-out papillae and fetor, not bilateral reticular striae.', 'C': 'Fibroma is a localized reactive nodule, not bilateral striae.', 'D': 'Periapical abscess requires an odontogenic source and focal signs.'}
    },
    {
     'question': 'Before prescribing systemic ketoconazole for suspected oral Candida in an older patient on multiple drugs, which applied precaution is most relevant?',
     'options': ['A) Assume no azole interacts with any hepatic cytochrome pathways', 'B) Review drug interactions and consider topical antifungals first when disease is limited', 'C) Give triple the dose if the patient takes warfarin without monitoring', 'D) Ignore liver disease history for oral systemic azoles'],
     'answer': 'B) Review drug interactions and consider topical antifungals first when disease is limited',
     'explanation': 'Systemic azoles have significant CYP-mediated interactions (including with warfarin) and hepatic risks. Limited oral candidiasis often responds to topical nystatin/clotrimazole, which is safer first-line in many cases. Dose escalation without monitoring is dangerous.',
     'choice_explanations': {'A': 'Azoles have well-known CYP interactions.', 'B': 'Prefer topical antifungals for limited disease and screen azole interactions/liver risk before systemic use.', 'C': 'Warfarin–azole interactions can potentiate anticoagulation dangerously.', 'D': 'Liver disease is a key caution for systemic azoles.'}
    },
   ],
   'hard': [
    {
     'question': 'A 58-year-old smoker has a speckled red-white patch on the lateral tongue that persists 4 weeks after removing a sharp cusp and treating Candida. The area is firm and nonwipeable. Which multi-cue next step is most appropriate?',
     'options': ['A) Reassure that all tongue patches are geographic tongue without exam correlation', 'B) Cauterize empirically with phenol indefinitely without diagnosis', 'C) Biopsy to rule out epithelial dysplasia or carcinoma; persistent speculative lesions need histopathology', 'D) Treat with systemic antibiotics for 6 months as definitive care'],
     'answer': 'C) Biopsy to rule out epithelial dysplasia or carcinoma; persistent speculative lesions need histopathology',
     'explanation': 'Speckled leukoplakia/erythroleukoplakia on the lateral tongue in a smoker is high-risk. Failure to resolve after removing local irritants and candidiasis mandates biopsy. Geographic tongue has a different migrating pattern; empiric caustics or long antibiotics without diagnosis are unsafe near-misses.',
     'choice_explanations': {'A': 'Geographic tongue migrates and is not a firm fixed speckled high-risk patch.', 'B': 'Empiric caustic destruction without diagnosis can mask carcinoma.', 'C': 'Persistent high-risk red-white tongue lesions require biopsy after reversible causes are addressed.', 'D': 'Antibiotics do not treat dysplasia/neoplasia.'}
    },
    {
     'question': 'A patient develops acute onset unilateral facial vesicles on an erythematous base along a dermatome with severe burning pain, including intraoral ulcers on the same side. Which multi-cue diagnosis and care concept fit?',
     'options': ['A) Bilateral angular cheilitis from Candida only', 'B) Aphthous stomatitis confined to nonkeratinized mucosa as the full explanation of dermatomal skin vesicles', 'C) Allergic contact dermatitis from toothpaste affecting only the contralateral face', 'D) Herpes zoster (varicella-zoster reactivation)—early antiviral therapy and pain control; watch ocular involvement if V1'],
     'answer': 'D) Herpes zoster (varicella-zoster reactivation)—early antiviral therapy and pain control; watch ocular involvement if V1',
     'explanation': 'Zoster produces unilateral dermatomal vesicles and pain from VZV reactivation; oral mucosa can be involved in the same distribution. Early antivirals reduce complications; V1 disease needs eye evaluation. Aphthae lack cutaneous dermatomal vesicles; angular cheilitis is commissural; contralateral allergic patterns do not match.',
     'choice_explanations': {'A': 'Angular cheilitis is localized to commissures, not a dermatomal vesicular eruption.', 'B': 'Aphthae do not produce cutaneous dermatomal vesicles.', 'C': 'Contralateral toothpaste allergy does not explain ipsilateral dermatomal zoster.', 'D': 'Unilateral dermatomal vesicles ± oral ulcers = zoster; treat early with antivirals and protect the eye if V1.'}
    },
    {
     'question': 'A patient on methotrexate for rheumatoid arthritis develops painful oral ulcers, pancytopenia on recent labs, and fever. Which multi-cue oral medicine action is most urgent?',
     'options': ['A) Urgent medical/rheumatology coordination for possible methotrexate toxicity/infection risk; do not attribute ulcers to simple aphthae alone', 'B) Increase methotrexate dose empirically to treat mouth ulcers', 'C) Start ototoxic high-dose aspirin only and discharge', 'D) Perform elective soft-tissue grafts under pancytopenia'],
     'answer': 'A) Urgent medical/rheumatology coordination for possible methotrexate toxicity/infection risk; do not attribute ulcers to simple aphthae alone',
     'explanation': 'Methotrexate toxicity can cause severe mucositis with bone marrow suppression and infection risk. Dental clinicians should recognize red flags and coordinate urgent medical care/folinic acid rescue as physicians direct. Increasing MTX, elective surgery under pancytopenia, or ignoring systemic toxicity is dangerous.',
     'choice_explanations': {'A': 'Oral ulcers with pancytopenia on MTX suggest toxicity—urgent medical coordination, not more MTX or elective surgery.', 'B': 'Increasing MTX worsens toxicity.', 'C': 'Aspirin alone does not manage MTX marrow toxicity.', 'D': 'Elective surgery under pancytopenia risks hemorrhage/infection.'}
    },
   ],
   'extreme': [
    {
     'question': 'A 65-year-old with recent weight loss has a nonhealing indurated ulcer on the lateral tongue for 3 months, ipsilateral ear pain, tobacco/alcohol history, and a firm upper cervical node. Which differential-driven management pathway is correct?',
     'options': ['A) Treat with topical antifungals for 6 months before any consideration of cancer', 'B) Urgent referral for oncology workup of suspected oral squamous cell carcinoma (biopsy/imaging/neck evaluation); do not trial months of empiric mouthwash alone', 'C) Assume traumatic ulcer forever despite induration and lymphadenopathy', 'D) Extract all contralateral teeth as definitive therapy for the tongue ulcer'],
     'answer': 'B) Urgent referral for oncology workup of suspected oral squamous cell carcinoma (biopsy/imaging/neck evaluation); do not trial months of empiric mouthwash alone',
     'explanation': 'Chronic indurated tongue ulcer with referred otalgia and cervical lymphadenopathy in a patient with tobacco/alcohol exposure is carcinoma until proven otherwise. Delay with prolonged empiric therapy worsens stage. Traumatic ulcers lack progressive firm nodes; extracting unrelated teeth does not treat cancer.',
     'choice_explanations': {'A': 'Prolonged antifungal trials delay cancer diagnosis when features are neoplastic.', 'B': 'High-risk nonhealing indurated tongue ulcer ± nodes needs urgent cancer referral/biopsy—not months of empiric rinses.', 'C': 'Induration plus lymphadenopathy contradicts simple chronic trauma.', 'D': 'Contralateral extractions do not address tongue malignancy.'}
    },
    {
     'question': 'A patient with mucocutaneous blistering, desquamative gingivitis, and a positive Nikolsky sign has oral lesions that heal with scarring. Direct immunofluorescence is pending. Which complex differential management stance is best while awaiting results?',
     'options': ['A) Scale aggressively under loose epithelium without soft-tissue precautions', 'B) Guarantee that all blistering diseases are recurrent aphthae', 'C) Differentiate pemphigus vulgaris vs mucous membrane pemphigoid (and others), avoid high-trauma dental care, coordinate dermatology/oral medicine immunosuppression planning, and protect the eyes if MMP suspected', 'D) Start random systemic chemotherapy in the dental chair without diagnosis'],
     'answer': 'C) Differentiate pemphigus vulgaris vs mucous membrane pemphigoid (and others), avoid high-trauma dental care, coordinate dermatology/oral medicine immunosuppression planning, and protect the eyes if MMP suspected',
     'explanation': 'Pemphigus and mucous membrane pemphigoid both blister but differ in immunofluorescence targets and scarring/ocular risk (especially MMP). Management is multidisciplinary immunosuppression after diagnosis; interim care minimizes trauma. Aggressive scaling under fragile epithelium and empiric chemo are incorrect.',
     'choice_explanations': {'A': 'Trauma to loose epithelium extends erosions.', 'B': 'Aphthae are not scarring autoimmune blistering diseases with Nikolsky sign.', 'C': 'Desquamative blistering disease needs DIF-guided diagnosis, gentle dental care, and specialty immunosuppression—plus eye vigilance for MMP.', 'D': 'Chemotherapy without diagnosis is inappropriate dental-chair practice.'}
    },
    {
     'question': 'An HIV-positive patient with low CD4 count presents with extensive oral candidiasis, hairy leukoplakia, and a purple palatal nodule suggestive of Kaposi sarcoma. He has stopped antiretroviral therapy. Which integrated decision is most appropriate?',
     'options': ['A) Treat only with bleaching trays because purple lesions are always hematomas', 'B) Advise permanent cessation of all medical care to let immunity rest', 'C) Excise the entire hard palate in office under LA as first-line KS cure without medical staging', 'D) Coordinate urgent medical restart/optimization of ART, manage opportunistic oral infections, and refer the palatal lesion for definitive KS evaluation/treatment'],
     'answer': 'D) Coordinate urgent medical restart/optimization of ART, manage opportunistic oral infections, and refer the palatal lesion for definitive KS evaluation/treatment',
     'explanation': 'Oral opportunistic diseases reflect systemic immunosuppression; ART optimization is foundational. Candidiasis and hairy leukoplakia are managed locally/systemically as indicated, while suspected KS needs medical oncology/infectious disease staging—not office palatectomy or denial. Bleaching is irrelevant.',
     'choice_explanations': {'A': 'Purple palatal nodules in advanced HIV raise KS concern, not routine hematoma/bleaching care.', 'B': 'Stopping medical care worsens opportunistic disease.', 'C': 'KS needs staging/systemic planning; blind total palatectomy under LA is not first-line.', 'D': 'HIV-related oral opportunistic disease requires ART coordination plus targeted local therapy and KS referral—not denial or mutilating office surgery.'}
    },
   ],
  },
  'cases': {
   'easy': [
    {'title': 'Recurrent Mouth Ulcers', 'stem': 'Healthy teen gets painful ulcers on buccal mucosa lasting a week, then heal.', 'question': 'Likely?', 'answer': 'Recurrent aphthous stomatitis.', 'discussion': 'Symptomatic care; investigate if complex.', 'book_hint': 'Oral and Maxillofacial Pathology — Neville'},
   ],
   'medium': [
    {'title': 'White Patch Floor of Mouth', 'stem': 'A 60-year-old smoker has a non-wipeable white patch on floor of mouth.', 'question': 'Next concept?', 'answer': 'Treat as leukoplakia — specialist referral/biopsy risk stratification.', 'discussion': 'Floor of mouth is high-risk site.', 'book_hint': 'Oral and Maxillofacial Pathology — Neville'},
   ],
   'hard': [
    {'title': 'Desquamative Gingivitis', 'stem': 'Painful peeling gingiva, nikolsky-positive areas, no response to cleaning alone. Choose the safest high-yield next concept before definitive results.', 'question': 'Workup?', 'answer': 'Consider vesiculobullous disease — biopsy for histopathology + DIF.', 'discussion': 'Do not keep scaling without diagnosis.', 'book_hint': 'Oral and Maxillofacial Pathology — Neville'},
   ],
   'extreme': [
    {'title': 'Nonhealing Lateral Tongue Ulcer', 'stem': 'A 55-year-old heavy smoker/drinker has a firm nonhealing ulcer on lateral tongue for 6 weeks with lymphadenopathy. Avoid harmful premature treatment while catastrophic differentials remain open.', 'question': 'Action?', 'answer': 'Urgent biopsy/OMFS-oncology referral for suspected SCC.', 'discussion': 'Do not treat empirically for months.', 'book_hint': 'Oral and Maxillofacial Pathology — Neville'},
   ],
  },
 },
 'restorative': {
  'label': 'Restorative Dentistry',
  'books': ["Sturdevant's Art and Science of Operative Dentistry", "Summitt's Fundamentals of Operative Dentistry", "Pickard's Guide to Minimally Invasive Operative Dentistry"],
  'pdf_notes': ['Black classification still useful for cavity location.', 'Adhesion needs etch/bond protocol and isolation.', 'High C-factor increases polymerization stress.', 'Selective caries removal can avoid pulp exposure.', 'Prevention first in rampant caries.'],
  'questions': {
   'easy': [
    {
     'question': 'The smear layer on instrumented dentin is best described as which layer?',
     'options': ['A) A layer of cutting debris that can occlude dentinal tubules and affect bonding/sealing', 'B) A pure hydroxyapatite crystal growth identical to enamel rods', 'C) A sterile rubber dam sheet bonded to enamel', 'D) The pulp chamber roof exclusively'],
     'answer': 'A) A layer of cutting debris that can occlude dentinal tubules and affect bonding/sealing',
     'explanation': 'Rotary/hand instrumentation creates a smear layer of debris that plugs tubules. Etching or conditioners modify/remove it depending on the adhesive strategy. It is not enamel rod architecture, rubber dam, or anatomic pulp roof.',
     'choice_explanations': {'A': 'Smear layer = instrumentation debris affecting tubule patency and adhesive behavior.', 'B': 'Smear layer is debris, not organized enamel rod structure.', 'C': 'Rubber dam is isolation equipment, not a tooth surface layer.', 'D': 'Pulp chamber roof is anatomy, not smear debris.'}
    },
    {
     'question': 'Which property most directly explains why enamel etchant (phosphoric acid) improves micromechanical retention for resin bonding?',
     'options': ['A) Complete obliteration of all enamel organic matrix permanently without resin', 'B) Selective demineralization creating microporosities for resin tag formation', 'C) Conversion of enamel into gutta-percha', 'D) Anesthetizing odontoblasts chemically'],
     'answer': 'B) Selective demineralization creating microporosities for resin tag formation',
     'explanation': 'Acid etching demineralizes enamel prismatically/interprismatically, creating a high-energy microporous surface that allows resin penetration and micromechanical interlocking. It does not turn enamel into GP or anesthetize pulp.',
     'choice_explanations': {'A': 'Bonding requires resin infiltration into etched porosities, not acid alone as the restoration.', 'B': 'Etching creates enamel microporosities for micromechanical resin bonding.', 'C': 'Gutta-percha is an endodontic obturant, not etched enamel.', 'D': 'Etchant is not a local anesthetic for odontoblasts.'}
    },
    {
     'question': 'Caries excavation ideally aims to remove which tissue while preserving maximally reparable dentin near the pulp when doing selective removal in deep lesions?',
     'options': ['A) All dentin until pulp exposure is mandatory in every deep lesion', 'B) Only extrinsic stain on intact enamel without assessing hardness', 'C) Soft, highly infected dentin while retaining firm, remineralizable dentin when indicated', 'D) Healthy enamel rods far from the lesion as first priority'],
     'answer': 'C) Soft, highly infected dentin while retaining firm, remineralizable dentin when indicated',
     'explanation': 'Modern deep-caries protocols often selectively remove soft infected dentin and leave firm affected dentin to avoid pulp exposure, then seal. Mandatory exposure of every pulp, ignoring hardness, or removing healthy distant enamel first are incorrect.',
     'choice_explanations': {'A': 'Pulp exposure is not mandatory if sealed selective removal can avoid it.', 'B': 'Stain alone is not the excavation criterion; hardness/texture matter.', 'C': 'Selective caries removal targets soft infected dentin and preserves reparable firm dentin when appropriate.', 'D': 'Healthy distant enamel is not the primary tissue to excavate.'}
    },
   ],
   'medium': [
    {
     'question': 'A Class II composite keeps failing with proximal contact loss and food impaction. Which applied corrective principle is most important?',
     'options': ['A) Cure without a matrix because composites expand to form contacts', 'B) Always leave a large open gingival embrasure for self-cleaning with packing food', 'C) Ignore wedge adaptation because gingival overhangs prevent failure', 'D) Use proper matrix/wedge technique to establish tight anatomic contact before curing'],
     'answer': 'D) Use proper matrix/wedge technique to establish tight anatomic contact before curing',
     'explanation': 'Composite does not push the matrix like amalgam; sectional matrices and wedges are required to create contact and seal the gingival margin. Curing without a matrix or accepting open contacts invites impaction and periodontal harm.',
     'choice_explanations': {'A': 'Composite polymerization does not create contacts without a contoured matrix.', 'B': 'Open contacts cause food impaction, not beneficial self-cleaning.', 'C': 'Overhangs trap plaque and worsen gingival outcomes.', 'D': 'Reliable Class II contacts require matrix and wedge systems before light-curing.'}
    },
    {
     'question': 'Postoperative sensitivity after a posterior composite is most often linked clinically to which applied factors?',
     'options': ['A) Occlusal prematurities, polymerization stress, or incomplete sealing of dentin', 'B) Excessive fluoride varnish placed on the tongue only', 'C) Choosing a shade that is slightly too light esthetically', 'D) Using rubber dam isolation during placement'],
     'answer': 'A) Occlusal prematurities, polymerization stress, or incomplete sealing of dentin',
     'explanation': 'Common causes of post-composite sensitivity include hyperocclusion, C-factor stress/gaps, and imperfect dentin seal. Rubber dam usually improves outcomes; shade and tongue varnish are unrelated primary causes.',
     'choice_explanations': {'A': 'Check occlusion, bonding/seal, and stress management when composites cause sensitivity.', 'B': 'Tongue varnish does not explain tooth-specific postoperative bite sensitivity.', 'C': 'Shade mismatch is esthetic, not a sensitivity mechanism.', 'D': 'Rubber dam reduces contamination and typically helps bonding success.'}
    },
    {
     'question': 'When restoring a deep proximal box near the pulp with composite, which applied liner/base concept is most coherent with modern adhesive dentistry?',
     'options': ['A) Place a thick unsealed cotton pellet permanently under composite', 'B) Consider a thin bioactive/glass-ionomer or calcium silicate liner on the deepest dentin when indicated, then adhesive composite', 'C) Never seal dentin because tubules must remain widely open to saliva', 'D) Use zinc oxide–eugenol directly under all resins as the preferred bonding primer'],
     'answer': 'B) Consider a thin bioactive/glass-ionomer or calcium silicate liner on the deepest dentin when indicated, then adhesive composite',
     'explanation': 'Deep areas may receive a selective liner (GI/calcium silicate) for sealing/biocompatibility, then adhesive restoration. Permanent cotton under composite fails; open salivary contamination of tubules harms pulp; eugenol can inhibit resin polymerization.',
     'choice_explanations': {'A': 'Cotton pellets are temporary coverage, not permanent bases under composite.', 'B': 'Deep dentin may get a compatible liner then adhesive composite—not cotton, open tubules, or eugenol under resin.', 'C': 'Dentin should be sealed from bacterial/salivary contamination.', 'D': 'Eugenol can interfere with resin polymerization.'}
    },
   ],
   'hard': [
    {
     'question': 'A premolar has an old MOD amalgam with a cracked marginal ridge, bite pain on release, and a hairline crack staining toward the pulp on removal of the restoration. Pulp tests are normal lingering-free. Which multi-cue restorative plan fits?',
     'options': ['A) Place a small occlusal preventive resin only and ignore the crack line', 'B) Proceed straight to extraction without assessing restorable structure', 'C) Protect cusps with an onlay/crown after confirming restorable crack extent and vitality; do not place another large amalgam without cuspal coverage', 'D) Apply bleaching gel into the crack as definitive structural therapy'],
     'answer': 'C) Protect cusps with an onlay/crown after confirming restorable crack extent and vitality; do not place another large amalgam without cuspal coverage',
     'explanation': 'Cracks through marginal ridges under large restorations often need cuspal coverage to prevent propagation. Vital teeth without irreversible pulpitis may avoid RCT initially. Tiny unbonded resins, automatic extraction, or bleach do not stabilize structure.',
     'choice_explanations': {'A': 'Small occlusal resins do not brace cusps against crack propagation.', 'B': 'Many cracked teeth are restorable with coverage; extraction is not automatic.', 'C': 'Restorable cracked premolars after large MOD failure typically need cuspal coverage restorations.', 'D': 'Bleach does not provide structural reinforcement.'}
    },
    {
     'question': 'A cervical noncarious lesion on a canine shows abfraction-type morphology, heavy occlusal interferences, and gingival recession with sensitivity. Which multi-cue approach is most rational?',
     'options': ['A) Ignore occlusion and place a rigid thick porcelain inlay into the cervical defect routinely', 'B) Prescribe antibiotics for abfraction', 'C) Extract the canine as first-line for sensitivity', 'D) Adjust occlusal prematurities as indicated, counsel on brushing technique, and restore with an appropriate flexible adhesive material if indicated for sensitivity/esthetics/plaque control'],
     'answer': 'D) Adjust occlusal prematurities as indicated, counsel on brushing technique, and restore with an appropriate flexible adhesive material if indicated for sensitivity/esthetics/plaque control',
     'explanation': 'Cervical lesions often combine stress, abrasion, and erosion. Managing occlusal load and hygiene technique plus adhesive restoration (often GI/composite) addresses etiology and symptoms. Antibiotics and extraction are near-misses; bulky rigid ceramics are rarely first-line cervically.',
     'choice_explanations': {'A': 'Rigid cervical porcelains without occlusal management often fail mechanically.', 'B': 'Abfraction/abrasion lesions are not treated with antibiotics.', 'C': 'Extraction is not first-line for cervical sensitivity.', 'D': 'Manage occlusal and habit factors and restore cervically with suitable adhesive materials when needed.'}
    },
    {
     'question': 'During deep caries removal on a vital molar, a pinpoint pulp exposure occurs with bright red hemorrhage that stops within 1–2 minutes. The tooth had no lingering spontaneous pain. Which multi-cue vital pulp therapy choice is most appropriate?',
     'options': ['A) Direct pulp cap or partial pulpotomy with hydraulic calcium silicate cement and immediate well-sealed restoration', 'B) Leave the exposure open to saliva for two weeks before sealing', 'C) Extract immediately without discussing vital pulp therapy options', 'D) Apply arsenical paste to mummify the entire pulp as modern standard care'],
     'answer': 'A) Direct pulp cap or partial pulpotomy with hydraulic calcium silicate cement and immediate well-sealed restoration',
     'explanation': 'Traumatic/mechanical pinpoint exposures in teeth without irreversible pulpitis symptoms can succeed with direct pulp capping or partial pulpotomy using MTA/bioceramics and an excellent seal. Salivary contamination, automatic extraction, or archaic arsenicals are incorrect.',
     'choice_explanations': {'A': 'Controlled vital exposures without irreversible symptoms warrant bioceramic pulp capping/partial pulpotomy plus seal.', 'B': 'Salivary contamination of exposures drastically reduces vital pulp therapy success.', 'C': 'Many exposures are manageable with vital pulp therapy; extraction is not automatic.', 'D': 'Arsenical pulp mummification is obsolete and unsafe by modern standards.'}
    },
   ],
   'extreme': [
    {
     'question': 'A strategic maxillary canine abutment for an RPD has deep distal caries under an old crown, questionable remaining ferrule after excavation, lingering cold pain, and a patient who refuses implants. Which complex restorative–endodontic decision is best?',
     'options': ['A) Recement the old crown over soft caries and irreversible pulpitis symptoms', 'B) Assess restorability after caries control; if inadequate ferrule, discuss crown-lengthening/orthodontic extrusion versus extraction; if irreversible pulpitis and restorable, RCT plus core/crown with planned surveyed contours', 'C) Promise a veneer alone will replace missing ferrule and endodontic need', 'D) Ignore RPD survey requirements when rebuilding the abutment contour'],
     'answer': 'B) Assess restorability after caries control; if inadequate ferrule, discuss crown-lengthening/orthodontic extrusion versus extraction; if irreversible pulpitis and restorable, RCT plus core/crown with planned surveyed contours',
     'explanation': 'Restorability (ferrule, ferrule-effect, remaining walls) gates whether RCT/crown can succeed for a strategic abutment. Irreversible pulpitis needs endodontics if saving the tooth. Crown lengthening/extrusion may create ferrule; otherwise extraction/RPD redesign is wiser. Recementing over caries/pulpitis or veneers without structure fails.',
     'choice_explanations': {'A': 'Cementing over caries and pulpitis fails biologically and mechanically.', 'B': 'Strategic abutments need honest ferrule/restorability assessment, then RCT/crown or extraction pathways—not recementing over disease.', 'C': 'Veneers do not create ferrule or treat irreversible pulpitis.', 'D': 'Surveyed contours are essential if the tooth remains an RPD abutment.'}
    },
    {
     'question': 'A patient develops severe biting pain one week after a large MOD composite on a molar. The restoration has a high centric stop, a hairline crack is now visible under magnification, and cold lingers mildly. Which complication-management sequence is most appropriate?',
     'options': ['A) Add more composite bulk on the occlusal to strengthen without adjusting the high spot', 'B) Prescribe long-term opioids as the only intervention', 'C) Immediately adjust occlusion, reassess pulp status, consider cuspal coverage or endodontics if pulp becomes irreversible, and replace the structurally inadequate restoration design', 'D) Assume symptoms are normal for 12 months without reevaluation'],
     'answer': 'C) Immediately adjust occlusion, reassess pulp status, consider cuspal coverage or endodontics if pulp becomes irreversible, and replace the structurally inadequate restoration design',
     'explanation': 'Hyperocclusion can crack teeth and inflame pulp. Prompt occlusal correction is mandatory; structural redesign (onlay/crown) may be required; endodontics follows if irreversible pulpitis develops. Adding bulk to a high restoration, opioids alone, or year-long neglect worsen outcomes.',
     'choice_explanations': {'A': 'Adding composite to a high restoration increases load and crack risk.', 'B': 'Opioids mask pain without correcting occlusion or structure.', 'C': 'Post-restoration bite pain with crack signs: adjust occlusion, reassess pulp, and redesign for cuspal protection as needed.', 'D': 'Progressive crack/pulp symptoms need timely reevaluation.'}
    },
    {
     'question': 'An extensive posterior composite shows recurrent caries at the gingival margin, open contact, and radiographic crestal bone loss localized to that interproximal. The patient wants just polish and bleach. Which decision is ethically and clinically correct?',
     'options': ['A) Polish and bleach only as requested without discussing disease findings', 'B) Ignore localized bone loss because composites cannot affect periodontium', 'C) Place a permanent post into the pulp chamber empirically without diagnosis', 'D) Explain that recurrent caries and periodontal harm require replacing the restoration with proper contact/contour and addressing hygiene; bleaching/polishing alone is insufficient'],
     'answer': 'D) Explain that recurrent caries and periodontal harm require replacing the restoration with proper contact/contour and addressing hygiene; bleaching/polishing alone is insufficient',
     'explanation': 'Open contacts and overhanging/open gingival margins drive caries and localized periodontitis. Standard of care is replacement with correct matrix contact and periodontal co-therapy as needed. Cosmetic-only care without disclosing disease violates informed consent; posts without endodontic indication are harmful.',
     'choice_explanations': {'A': 'Withholding diagnosis to satisfy a cosmetic request is unethical and leaves disease active.', 'B': 'Defective restorations commonly cause localized periodontal destruction.', 'C': 'Empiric posts without endodontic need violate tooth structure without benefit.', 'D': 'Recurrent caries + open contact + local bone loss require restorative replacement and perio attention—not bleach-only care.'}
    },
   ],
  },
  'cases': {
   'easy': [
    {'title': 'Occlusal Caries Molar', 'stem': 'A deep fissure stains; bitewing shows enamel-dentin caries; tooth vital asymptomatic.', 'question': 'Plan?', 'answer': 'Restore with appropriate material after caries removal.', 'discussion': 'Consider sealant for non-cavitated elsewhere.', 'book_hint': 'Art and Science of Operative Dentistry — Sturdevant'},
   ],
   'medium': [
    {'title': 'Failed Composite Margin', 'stem': 'Staining and catch at cervical margin of Class V composite; sensitivity to cold brief.', 'question': 'Likely?', 'answer': 'Marginal leakage/secondary caries or bond failure — replace after diagnosis.', 'discussion': 'Isolate well on redo.', 'book_hint': 'Art and Science of Operative Dentistry — Sturdevant'},
   ],
   'hard': [
    {'title': 'Deep Caries Near Pulp', 'stem': 'Young adult molar, deep caries, asymptomatic, remaining dentin thin on radiograph. Choose the safest high-yield next concept before definitive results.', 'question': 'Strategy concept?', 'answer': 'Consider stepwise/selective excavation, pulp protection, well-sealed restoration; monitor vitality.', 'discussion': 'Avoid unnecessary exposure.', 'book_hint': 'Art and Science of Operative Dentistry — Sturdevant'},
   ],
   'extreme': [
    {'title': 'Rampant Caries Head-Neck Radiation', 'stem': 'Patient post-radiotherapy has rampant caries and xerostomia. Avoid harmful premature treatment while catastrophic differentials remain open.', 'question': 'Plan pillars?', 'answer': 'Aggressive prevention (fluoride, saliva management), restore strategically, avoid extractions in irradiated bone when possible via specialist pathways.', 'discussion': 'ORN risk changes extraction decisions.', 'book_hint': 'Art and Science of Operative Dentistry — Sturdevant'},
   ],
  },
 },
 'oral_radiology': {
  'label': 'Oral Radiology',
  'books': ["White and Pharoah's Oral Radiology", 'Essentials of Dental Radiography', 'Oral Radiology principles texts'],
  'pdf_notes': ['ALARA: justify and optimize every exposure.', 'Bitewings for interproximal caries.', 'Periapicals for full root/periapex.', 'CBCT only when 2D is insufficient.', 'Ill-defined destructive lesions need urgent workup.'],
  'questions': {
   'easy': [
    {
     'question': 'The ALARA principle in dental radiology means which practice philosophy?',
     'options': ['A) Keep radiation exposure as low as reasonably achievable while obtaining necessary diagnostic information', 'B) Always take the maximum number of films possible for every visit', 'C) Avoid radiographs even when they would change urgent treatment', 'D) Use radiation for tooth bleaching activation routinely'],
     'answer': 'A) Keep radiation exposure as low as reasonably achievable while obtaining necessary diagnostic information',
     'explanation': 'ALARA balances diagnostic yield with dose minimization via selection criteria, collimation, sensors, and shielding. It does not mean infinite films, refusing indicated imaging, or using x-rays to bleach teeth.',
     'choice_explanations': {'A': 'ALARA = necessary diagnostic images at the lowest reasonable dose.', 'B': 'Unnecessary maximal film counts violate ALARA.', 'C': 'Indicated radiographs that alter care should not be withheld out of misunderstanding ALARA.', 'D': 'Ionizing dental x-rays are not a bleaching modality.'}
    },
    {
     'question': 'A periapical radiograph primarily images which structures?',
     'options': ['A) Only the soft tissue of the cheek in profile', 'B) The full tooth length including crown, root, and surrounding periapical bone', 'C) Only the mandibular condyle in motion', 'D) Only the skin surface without teeth'],
     'answer': 'B) The full tooth length including crown, root, and surrounding periapical bone',
     'explanation': 'Periapical radiographs are designed to show the entire tooth and adjacent bone for caries depth, root morphology, and periapical pathosis. Soft-tissue profile, condylar motion, and skin imaging use other modalities.',
     'choice_explanations': {'A': 'Cheek soft tissue is not the PA target.', 'B': 'Periapicals capture whole-tooth and periapical bone detail.', 'C': 'Condylar dynamics need TMJ-specific imaging, not standard PA.', 'D': 'Skin surface is not imaged for dental diagnosis on PA films.'}
    },
    {
     'question': 'Increasing the source-to-object distance while using proper collimation generally has which effect on image sharpness, all else equal?',
     'options': ['A) Always eliminates the need for any receptor', 'B) Guarantees twice the patient dose automatically without exposure compensation', 'C) Improves sharpness by reducing geometric penumbra (magnification of the focal spot blur)', 'D) Converts the image into a CT volumetric dataset'],
     'answer': 'C) Improves sharpness by reducing geometric penumbra (magnification of the focal spot blur)',
     'explanation': 'Geometric unsharpness decreases as source-to-object distance increases (and object-to-receptor decreases). Dose and exposure factors must be managed separately; a 2D receptor still acquires a projection, not a CT volume.',
     'choice_explanations': {'A': 'A receptor is still required to capture the image.', 'B': 'Dose depends on exposure settings; distance changes require technique compensation.', 'C': 'Greater source-to-object distance reduces penumbra and can sharpen projection images.', 'D': 'CT requires specialized rotational/volumetric acquisition, not merely moving the tube farther.'}
    },
   ],
   'medium': [
    {
     'question': 'A bitewing radiograph is most appropriately selected for which applied diagnostic task?',
     'options': ['A) Diagnosing fracture of the mandibular condylar neck exclusively', 'B) Mapping the full extent of a large odontogenic sinus cyst alone', 'C) Replacing all need for clinical probing of periodontal pockets', 'D) Detecting interproximal caries and evaluating crestal bone height between posterior teeth'],
     'answer': 'D) Detecting interproximal caries and evaluating crestal bone height between posterior teeth',
     'explanation': 'Bitewings excel for posterior interproximal caries and crestal bone assessment. Condylar fractures and large sinus lesions need panoramic/CBCT/other views; radiographs complement but do not replace periodontal probing.',
     'choice_explanations': {'A': 'Condylar neck fractures need dedicated mandibular/TMJ imaging.', 'B': 'Large antral lesions need wider field imaging than bitewings.', 'C': 'Probing depths remain a clinical measurement; radiographs assist bone assessment.', 'D': 'Bitewings are for interproximal caries and posterior crestal bone evaluation.'}
    },
    {
     'question': 'Cervical burnout on a periapical radiograph is an applied optical/anatomic phenomenon that can mimic which disease?',
     'options': ['A) Root caries or radiolucent cervical lesions near the CEJ', 'B) Pulp stones exclusively', 'C) Condensing osteitis only', 'D) Impacted third molar follicle exclusively'],
     'answer': 'A) Root caries or radiolucent cervical lesions near the CEJ',
     'explanation': 'Cervical burnout is a radiolucent artifact at the cervical tooth region from x-ray geometry and anatomic thinness, potentially mimicking caries. Clinical examination distinguishes true cavitation. Pulp stones and condensing osteitis are radiopaque phenomena; follicles relate to unerupted teeth.',
     'choice_explanations': {'A': 'Cervical burnout can mimic cervical/root caries; confirm clinically.', 'B': 'Pulp stones are intracoronal radiopacities, not cervical burnout mimics.', 'C': 'Condensing osteitis is a periapical radiopacity, not a cervical radiolucent artifact.', 'D': 'Follicular spaces surround crowns of unerupted teeth, a different entity.'}
    },
    {
     'question': 'Compared with film, a well-exposed digital sensor system typically allows which applied dose advantage when used correctly?',
     'options': ['A) Unlimited retakes without any dose concern', 'B) Lower dose per image with comparable diagnostic task performance for many indications', 'C) Complete immunity of digital images to positioning errors', 'D) Elimination of the need for clinical indications'],
     'answer': 'B) Lower dose per image with comparable diagnostic task performance for many indications',
     'explanation': 'Digital receptors are more dose-efficient than film for many tasks, supporting ALARA—but retakes still add dose, positioning still matters, and selection criteria remain mandatory.',
     'choice_explanations': {'A': 'Each retake adds patient dose despite digital capture.', 'B': 'Digital radiography often reduces dose per image but does not excuse retakes or unjustified imaging.', 'C': 'Geometry/positioning errors still degrade digital images.', 'D': 'Clinical indications still govern when to expose.'}
    },
   ],
   'hard': [
    {
     'question': 'A panoramic radiograph shows a well-defined radiolucency at the mandibular angle with a radiopaque impacted third molar crown and a corticated follicular space greater than 5 mm. The patient has no caries in the tooth. Which multi-cue interpretation is most likely?',
     'options': ['A) Normal follicular space of 1 mm without pathology', 'B) Periapical cemento-osseous dysplasia of a vital central incisor', 'C) Dentigerous (follicular) cyst associated with the unerupted third molar until proven otherwise', 'D) Sialolith in the submandibular duct exclusively'],
     'answer': 'C) Dentigerous (follicular) cyst associated with the unerupted third molar until proven otherwise',
     'explanation': 'Follicular spaces greater than about 5 mm around an unerupted crown suggest dentigerous cyst. Normal follicles are a few millimeters. PCOD relates to vital mandibular anteriors’ periapices; sialoliths are ductal radiopacities, not pericoronal lucencies.',
     'choice_explanations': {'A': 'A greater-than-5 mm corticated pericoronal lucency exceeds normal follicle size.', 'B': 'PCOD is a periapical radiopaque/mixed lesion of anterior vital teeth, not third-molar follicles.', 'C': 'Enlarged pericoronal radiolucency on an impacted molar suggests dentigerous cyst.', 'D': 'Sialoliths are calcifications in salivary ducts, not pericoronal cysts.'}
    },
    {
     'question': 'A patient has a suspected vertical root fracture in an endodontically treated premolar with a narrow deep probing defect and a J-shaped radiolucency, but the 2D image is equivocal. Which multi-cue imaging decision is best?',
     'options': ['A) Take weekly full-head medical CT for six months routinely', 'B) Never use any further imaging even if extraction vs save decisions hinge on it', 'C) Diagnose fracture solely from bitewing caries depth without clinical signs', 'D) Consider limited-field CBCT when it may change management, accepting higher dose only if justified after clinical correlation'],
     'answer': 'D) Consider limited-field CBCT when it may change management, accepting higher dose only if justified after clinical correlation',
     'explanation': 'Vertical root fracture diagnosis combines clinical signs (deep narrow pocket, sinus tract) with imaging; CBCT can help when justified. Routine repeated medical CT is excessive; refusing any imaging when decisions depend on it is unhelpful; bitewings alone do not diagnose VRF.',
     'choice_explanations': {'A': 'Weekly full-head CT violates ALARA dramatically.', 'B': 'Indicated adjunctive imaging can be appropriate when treatment hinges on it.', 'C': 'Bitewings assess caries/bone, not definitive VRF diagnosis alone.', 'D': 'Justify limited CBCT for suspected VRF when 2D is equivocal and management would change.'}
    },
    {
     'question': 'On a periapical image, the zygomatic process of the maxilla obscures the roots of upper molars. Which multi-cue technique adjustment often helps?',
     'options': ['A) Change receptor placement/angulation (e.g., more distal/vertical adjustments) or use a different projection to move the zygoma shadow off the roots', 'B) Increase patient dose arbitrarily without changing geometry', 'C) Ask for a mandibular occlusal film as the only view of maxillary molar roots', 'D) Interpret obscured roots as always missing without trying another angle'],
     'answer': 'A) Change receptor placement/angulation (e.g., more distal/vertical adjustments) or use a different projection to move the zygoma shadow off the roots',
     'explanation': 'Superimposition of the zygomatic process is a common maxillary molar PA problem corrected by angulation/placement changes or alternate views. Dose escalation alone without geometry change fails; mandibular occlusals do not depict maxillary roots; assuming agenesis from one obscured image is incorrect.',
     'choice_explanations': {'A': 'Reangle/reposition to move zygomatic superimposition off maxillary molar roots.', 'B': 'Dose increases without geometric change still leave the zygoma superimposed.', 'C': 'Mandibular occlusal projections do not image maxillary molar roots.', 'D': 'One obscured projection is insufficient to diagnose missing roots.'}
    },
   ],
   'extreme': [
    {
     'question': 'A 55-year-old with prior head/neck radiation for cancer needs extractions of periodontally hopeless teeth in the irradiated mandible field. Orthopantomogram shows mixed sclerosis. He asks for simple forceps removal today. Which complex risk-management decision is correct?',
     'options': ['A) Extract immediately with maximal flap reflection and bone removal without counseling ORN risk', 'B) Recognize osteoradionecrosis risk; coordinate oncology/OMFS, consider hyperbaric protocols where used, prefer atraumatic/surgical planning, and avoid casual extractions without risk counseling', 'C) Assure that radiated bone never develops healing complications', 'D) Order monthly whole-body PET-CT solely to plan a simple extraction'],
     'answer': 'B) Recognize osteoradionecrosis risk; coordinate oncology/OMFS, consider hyperbaric protocols where used, prefer atraumatic/surgical planning, and avoid casual extractions without risk counseling',
     'explanation': 'Irradiated jaws have lifelong osteoradionecrosis risk after trauma/extraction. Management may include antibiotic coverage, atraumatic technique, HBO in selected protocols, and specialist coordination. Denying risk or ordering irrelevant monthly PET for simple dental planning are near-misses.',
     'choice_explanations': {'A': 'Aggressive surgery without ORN counseling increases harm risk.', 'B': 'Post-radiation extractions need ORN risk counseling and specialist-coordinated atraumatic planning—not casual surgery.', 'C': 'Radiation-damaged bone has impaired healing and ORN risk.', 'D': 'Monthly whole-body PET is not the ALARA-appropriate planner for routine extraction geometry.'}
    },
    {
     'question': 'CBCT ordered for implant planning incidentally shows a well-circumscribed radiopaque mass in the mandibular canal region with expansion, and the patient has lip paresthesia. Which differential-driven next step is most appropriate?',
     'options': ['A) Proceed with freehand implant drilling through the radiopaque canal mass', 'B) Ignore paresthesia because CBCT artifacts always cause numbness', 'C) Stop routine implant drilling plans; refer for specialist evaluation of a possible benign neural tumor/other canal lesion before any implant osteotomy', 'D) Diagnose the finding as cervical burnout of a molar crown'],
     'answer': 'C) Stop routine implant drilling plans; refer for specialist evaluation of a possible benign neural tumor/other canal lesion before any implant osteotomy',
     'explanation': 'Canal-centered radiopaque expanding lesions with paresthesia raise concern for benign neural tumors (e.g., schwannoma/neurofibroma) or other pathology. Implant osteotomy through such lesions risks catastrophic nerve injury. Cervical burnout is a tooth-cervix artifact, unrelated.',
     'choice_explanations': {'A': 'Drilling through a canal mass can transect the IAN and worsen deficit.', 'B': 'True paresthesia is a clinical neurologic finding, not a CBCT software illusion.', 'C': 'Incidental canal lesion + paresthesia mandates specialist workup before any implant osteotomy.', 'D': 'Cervical burnout occurs at tooth necks, not as expanding canal masses.'}
    },
    {
     'question': 'A pregnant patient in the first trimester has acute pulpal pain and suspected periapical pathology on a lower molar. She fears any radiographs. Which decision balances fetal concerns with dental diagnosis?',
     'options': ['A) Refuse all imaging forever and also refuse emergency dental treatment', 'B) Take a full-mouth series plus CBCT of both jaws just in case without indications', 'C) Use medical abdominal CT instead of a dental periapical for the tooth', 'D) Explain that with proper shielding and modern receptors, a necessary periapical has very low fetal dose and is justified when it changes urgent care; do not withhold indicated imaging that prevents infection progression'],
     'answer': 'D) Explain that with proper shielding and modern receptors, a necessary periapical has very low fetal dose and is justified when it changes urgent care; do not withhold indicated imaging that prevents infection progression',
     'explanation': 'Indicated dental radiographs with thyroid/abdominal shielding and digital sensors pose minimal fetal risk and are acceptable when needed for emergency care. Blanket refusal can allow infection to worsen; unjustified FMX/CBCT and abdominal CT violate ALARA far more than a single PA.',
     'choice_explanations': {'A': 'Denying both diagnosis and emergency care risks maternal infection harm.', 'B': 'Unindicated full-mouth + CBCT contradicts ALARA in pregnancy.', 'C': 'Abdominal CT delivers far higher dose and does not image teeth usefully.', 'D': 'Necessary shielded dental radiographs for acute care are appropriate in pregnancy; avoid both neglect and over-imaging.'}
    },
   ],
  },
  'cases': {
   'easy': [
    {'title': 'Suspected Interproximal Caries', 'stem': 'Tight contacts, clinical doubt on upper premolars.', 'question': 'Image of choice first?', 'answer': 'Bitewings.', 'discussion': 'Then restore if confirmed.', 'book_hint': "White and Pharoah's Oral Radiology"},
   ],
   'medium': [
    {'title': 'Impacted Canine Localization', 'stem': 'Need to know buccal/palatal position of impacted canine.', 'question': 'Options?', 'answer': 'Parallax technique or CBCT when justified.', 'discussion': 'Avoid unnecessary high-dose imaging.', 'book_hint': "White and Pharoah's Oral Radiology"},
   ],
   'hard': [
    {'title': 'Unilocular Radiolucency Angle of Mandible', 'stem': 'Impacted wisdom tooth with radiolucency around crown in a young adult. Choose the safest high-yield next concept before definitive results.', 'question': 'Differential includes?', 'answer': 'Dentigerous cyst among others — remove/investigate histologically as indicated.', 'discussion': 'Do not ignore enlarging lesions.', 'book_hint': "White and Pharoah's Oral Radiology"},
   ],
   'extreme': [
    {'title': 'Ill-defined Mandibular Destruction', 'stem': 'A rapidly enlarging numb chin, loose teeth, and moth-eaten bone on radiograph. Avoid harmful premature treatment while catastrophic differentials remain open.', 'question': 'Action?', 'answer': 'Urgent biopsy/OMFS-oncology workup for possible malignancy.', 'discussion': 'Do not schedule elective cleaning only.', 'book_hint': "White and Pharoah's Oral Radiology"},
   ],
  },
 },
 'dental_anatomy': {
  'label': 'Dental Anatomy',
  'books': ["Wheeler's Dental Anatomy, Physiology and Occlusion", "Ash & Nelson's Dental Anatomy", 'Dental Anatomy review guides'],
  'pdf_notes': ['32 permanent teeth; 20 primary.', 'Know root/canal morphology for endo success.', 'Carabelli trait on maxillary first molar.', 'High pulp horns in young teeth.', 'Anomalies (dens invaginatus, dilaceration) change plans.'],
  'questions': {
   'easy': [
    {
     'question': 'Which permanent tooth typically has the longest root?',
     'options': ['A) Maxillary canine', 'B) Mandibular central incisor', 'C) Maxillary third molar', 'D) Mandibular lateral incisor'],
     'answer': 'A) Maxillary canine',
     'explanation': 'The maxillary canine usually possesses the longest root of the permanent dentition, providing strong anchorage. Mandibular incisors have shorter single roots; third molars are variable and often shorter/fused.',
     'choice_explanations': {'A': 'Maxillary canines characteristically have the longest roots among permanent teeth.', 'B': 'Mandibular central roots are comparatively short and narrow.', 'C': 'Third molar roots are often short, fused, or variable—not the longest on average.', 'D': 'Mandibular lateral roots are shorter than maxillary canine roots.'}
    },
    {
     'question': 'The cusp of Carabelli is most frequently associated with which tooth surface?',
     'options': ['A) Distobuccal cusp of the mandibular first premolar', 'B) Mesiolingual cusp region of the maxillary first molar', 'C) Incisal edge of the mandibular central incisor', 'D) Buccal pit of the mandibular canine'],
     'answer': 'B) Mesiolingual cusp region of the maxillary first molar',
     'explanation': 'An accessory cusp of Carabelli (when present) arises on the mesiolingual aspect of maxillary first molars (sometimes seconds). It is not an incisor or canine feature and is not the mandibular first premolar’s main identifying cusp anatomy.',
     'choice_explanations': {'A': 'Mandibular first premolars are identified by a large buccal cusp, not Carabelli.', 'B': 'Cusp of Carabelli appears on the mesiolingual of maxillary first molars when present.', 'C': 'Incisors lack Carabelli cusps.', 'D': 'Canines do not bear a Carabelli cusp on a buccal pit.'}
    },
    {
     'question': 'Which primary tooth is most likely to exhibit a prominent mesial cervical crown bulge and a unique occlusal anatomy among primary molars commonly tested?',
     'options': ['A) Permanent mandibular third molar exclusively', 'B) Permanent maxillary central incisor exclusively', 'C) Primary maxillary first molar (distinct from permanent premolar form)', 'D) Primary mandibular central incisor exclusively as a molar form'],
     'answer': 'C) Primary maxillary first molar (distinct from permanent premolar form)',
     'explanation': 'Primary maxillary first molars have unique morphology (often compared loosely to premolars yet distinct), with a prominent buccal cervical ridge. Permanent third molars and permanent centrals are not primary molars; primary mandibular centrals are incisors.',
     'choice_explanations': {'A': 'Permanent third molars are not primary teeth.', 'B': 'Permanent central incisors are not primary molars.', 'C': 'Primary maxillary first molars have distinctive molar form with marked cervical bulge features emphasized in anatomy courses.', 'D': 'Primary mandibular centrals are incisors, not molars.'}
    },
   ],
   'medium': [
    {
     'question': 'Which applied anatomic feature of mandibular first molars most influences periodontal instrument adaptation buccally?',
     'options': ['A) Presence of a cusp of Carabelli on the buccal surface', 'B) A single conical root like a primary incisor always', 'C) Complete absence of a buccal groove in all individuals', 'D) The cervical enamel contour and root trunk with possible buccal furcation involvement'],
     'answer': 'D) The cervical enamel contour and root trunk with possible buccal furcation involvement',
     'explanation': 'Mandibular first molars have two roots and a buccal groove/furcation anatomy that guides scaling adaptation. Carabelli is a maxillary trait; these molars are not single-rooted like primary incisors; buccal grooves are typical.',
     'choice_explanations': {'A': 'Cusp of Carabelli is maxillary first molar mesiolingual, not mandibular buccal.', 'B': 'Mandibular first molars normally have two roots, not a single conical root.', 'C': 'A buccal groove is a standard landmark of mandibular first molars.', 'D': 'Mandibular first molar cervical/furcation anatomy guides buccal periodontal instrumentation.'}
    },
    {
     'question': 'For endodontic access, which applied pulp-chamber landmark relationship is most reliable in mature maxillary first molars?',
     'options': ['A) Pulp chamber floor is at the level of the CEJ region with canal orifices arranged accordingly (often MB, DB, P; MB2 common)', 'B) All canal orifices always exit through the incisal edge', 'C) There is never more than one canal in any maxillary molar', 'D) Pulp horns are absent in all maxillary first molars'],
     'answer': 'A) Pulp chamber floor is at the level of the CEJ region with canal orifices arranged accordingly (often MB, DB, P; MB2 common)',
     'explanation': 'In mature molars the chamber floor approximates CEJ level, and maxillary first molars commonly have three roots with four canals (MB2 frequent). Incisal access applies to anteriors; pulp horns exist especially in young teeth.',
     'choice_explanations': {'A': 'Maxillary first molar access uses CEJ-level chamber floor landmarks and anticipates MB2.', 'B': 'Molar orifices are on the chamber floor, not the incisal edge.', 'C': 'MB2 is common; assuming only one canal is a frequent cause of failure.', 'D': 'Pulp horns are present, notably in younger teeth.'}
    },
    {
     'question': 'Occlusal contact on a maxillary premolar is applied clinically when adjusting a crown. Which anatomic feature primarily guides buccal cusp placement in the fossae of the antagonist?',
     'options': ['A) The pulp chamber height alone without occlusal anatomy', 'B) The supporting cusp relationship into opposing fossae/marginal ridge areas within the occlusal scheme', 'C) The color of the shade tab under metamerism only', 'D) The length of the patient’s hair'],
     'answer': 'B) The supporting cusp relationship into opposing fossae/marginal ridge areas within the occlusal scheme',
     'explanation': 'In occlusal schemes, supporting cusps contact opposing fossae or marginal ridges. Crown adjustment references these contacts, not pulp chamber height, shade metamerism, or irrelevant patient features.',
     'choice_explanations': {'A': 'Pulp chamber height does not set occlusal contact points.', 'B': 'Supporting cusp–fossa/marginal ridge relations guide premolar occlusal adjustment.', 'C': 'Shade selection is esthetic, not cusp–fossa anatomy.', 'D': 'Hair length is unrelated to occlusion.'}
    },
   ],
   'hard': [
    {
     'question': 'A radiograph of a mandibular second premolar suggests a single root, but the patient has persistent symptoms after apparent one-canal RCT. Clinically the crown has a large lingual cusp almost equal to the buccal. Which multi-cue anatomic suspicion is strongest?',
     'options': ['A) Assume mandibular second premolars never have anatomic variation', 'B) Diagnose only sinus disease without rechecking the tooth', 'C) Possible second canal/root variation—reassess anatomy with angled radiographs or CBCT and revise treatment', 'D) Conclude the equal lingual cusp proves enamel hypoplasia as the pain source'],
     'answer': 'C) Possible second canal/root variation—reassess anatomy with angled radiographs or CBCT and revise treatment',
     'explanation': 'Mandibular premolars may have canal bifurcations despite a seemingly single root. A well-developed lingual cusp can correlate with more complex pulp anatomy. Persistent symptoms warrant anatomic re-evaluation rather than assuming zero variation or unrelated sinus disease alone.',
     'choice_explanations': {'A': 'Anatomic variation in mandibular premolars is well documented.', 'B': 'Tooth-driven symptoms require dental re-evaluation before attributing solely to sinus disease.', 'C': 'Symptomatic premolars after one-canal RCT need search for missed canal anatomy, especially with suggestive crown form.', 'D': 'Cusp size relates to morphologic type, not enamel hypoplasia as the pain explanation.'}
    },
    {
     'question': 'During extraction planning, a maxillary first molar shows three divergent roots on CBCT with the palatal root into the sinus floor and closely approximated MB/DB roots. Which multi-cue anatomic implication is most important?',
     'options': ['A) Use uncontrolled force assuming all maxillary molars are fused single cones', 'B) Ignore sinus proximity because molars never communicate with the antrum', 'C) Extract via the nasal cavity as the standard first approach', 'D) Plan sectioning to reduce oroantral and root-fracture risk given divergence and sinus proximity'],
     'answer': 'D) Plan sectioning to reduce oroantral and root-fracture risk given divergence and sinus proximity',
     'explanation': 'Divergent maxillary molar roots and sinus approximation raise fracture and oroantral communication risk; sectioning reduces force. Fused-cone assumptions, denying sinus risk, or transnasal extraction are incorrect.',
     'choice_explanations': {'A': 'Uncontrolled force on divergent roots fractures tips and tears sinus membrane.', 'B': 'Maxillary molar roots commonly approximate the sinus.', 'C': 'Transnasal extraction is not a dental standard approach for molars.', 'D': 'Divergent sinus-approximating maxillary molar roots favor controlled sectioning to prevent OAC/fracture.'}
    },
    {
     'question': 'A student identifies a tooth with two roots (buccal and lingual), a mesial marginal ridge more cervical than distal, and a large buccal cusp with a nonfunctioning lingual cusp. Which multi-cue identification is most accurate?',
     'options': ['A) Maxillary first premolar', 'B) Mandibular canine', 'C) Maxillary central incisor', 'D) Mandibular second molar with five cusps'],
     'answer': 'A) Maxillary first premolar',
     'explanation': 'Maxillary first premolars commonly have two roots (buccal/lingual) and characteristic mesial anatomy with a dominant buccal cusp. Mandibular canines are typically single-rooted; centrals are incisors; mandibular second molars are multi-cusped molars, not this premolar pattern.',
     'choice_explanations': {'A': 'Two-rooted premolar with dominant buccal cusp and characteristic mesial anatomy = maxillary first premolar.', 'B': 'Mandibular canines are usually single-rooted anterior teeth.', 'C': 'Maxillary centrals are single-rooted incisors without buccal/lingual premolar cusps.', 'D': 'Mandibular second molars have molar occlusal schemes, not this premolar root/cusp pattern.'}
    },
   ],
   'extreme': [
    {
     'question': 'An extracted maxillary molar teaching specimen shows three roots, but the MB root has two canal orifices and a fin connecting to a second MB canal that joins near midroot. Clinically this pattern most informs which complex endodontic decision concept on a vital inflamed maxillary first molar?',
     'options': ['A) Assume MB roots never contain more than one canal in first molars', 'B) Access and instrumentation must actively negotiate MB2 anatomy; missing the second mesiobuccal canal is a common cause of persistent disease despite three canals filled', 'C) Obturate only the palatal canal because MB anatomy is irrelevant to symptoms', 'D) Treat the tooth as a mandibular canine based on root count alone'],
     'answer': 'B) Access and instrumentation must actively negotiate MB2 anatomy; missing the second mesiobuccal canal is a common cause of persistent disease despite three canals filled',
     'explanation': 'Maxillary first molars frequently have MB2 canals that may join or remain separate. Failure to locate MB2 leaves infected tissue and explains post-treatment disease. Root count alone does not reclassify the tooth as a canine; all canals need disinfection.',
     'choice_explanations': {'A': 'MB2 prevalence is high; assuming a single MB canal is a classic error.', 'B': 'MB2 is a critical anatomic complexity in maxillary first molars; missing it risks failure.', 'C': 'MB canal infection can maintain symptoms even if the palatal canal is filled.', 'D': 'Three molar roots do not make the tooth a mandibular canine.'}
    },
    {
     'question': 'A trauma case shows a horizontal root fracture in the apical third of a maxillary central with displaced coronal fragment. Anatomy of the pulp and periodontal ligament attachment informs which complex management differential?',
     'options': ['A) Always perform immediate RCT of both apical and coronal segments through the fracture without repositioning', 'B) Extract immediately every apical-third root fracture without reposition attempt', 'C) Reposition and flexible splint; pulp may survive especially with apical fractures; monitor vitality and consider endodontics of the coronal segment only if necrosis develops', 'D) Ignore PDL anatomy and rigidly fixate for six months without follow-up vitality tests'],
     'answer': 'C) Reposition and flexible splint; pulp may survive especially with apical fractures; monitor vitality and consider endodontics of the coronal segment only if necrosis develops',
     'explanation': 'Apical-third root fractures often have better pulp survival prognosis after repositioning and short-term flexible splinting. Endodontics, if needed, usually addresses the coronal segment when pulp necroses. Immediate RCT of both segments, automatic extraction, or prolonged rigid fixation without monitoring are near-misses.',
     'choice_explanations': {'A': 'Routine immediate RCT of apical and coronal segments is not first-line when pulp may recover.', 'B': 'Many apical-third fractures can be saved with repositioning/splinting.', 'C': 'Apical root fractures: reposition, flexible splint, monitor; RCT coronal segment only if necrosis occurs.', 'D': 'Rigid prolonged fixation and neglected vitality follow-up worsen outcomes.'}
    },
    {
     'question': 'In planning a surgical endodontic approach to a palatal root of a maxillary first molar, the surgeon notes on CBCT that the root apex is enveloped by sinus membrane and a large greater palatine vessel canal is nearby. Which anatomy-driven complication plan is most appropriate?',
     'options': ['A) Curette aggressively through the sinus and greater palatine canal without planning', 'B) Assume palatal roots never relate to the maxillary sinus', 'C) Use a standard buccal-only approach and guarantee easy access to every palatal apex', 'D) Modify flap design and apex location strategy to avoid sinus perforation and vascular injury; consider intentional replantation or orthograde options if surgical risk outweighs benefit'],
     'answer': 'D) Modify flap design and apex location strategy to avoid sinus perforation and vascular injury; consider intentional replantation or orthograde options if surgical risk outweighs benefit',
     'explanation': 'Palatal apices may project into the sinus, and palatal surgery risks greater palatine neurovascular injury. CBCT guides whether surgery, orthograde revision, or intentional replantation is safer. Aggressive curettage through sinus/vessels and denying sinus relationships are dangerous; buccal approaches often cannot reach palatal apices easily.',
     'choice_explanations': {'A': 'Aggressive sinus/vessel violation risks hemorrhage and oroantral complications.', 'B': 'Palatal roots commonly approximate or enter the sinus.', 'C': 'Buccal surgery frequently provides poor direct access to palatal apices.', 'D': 'Sinus- and vessel-aware planning may lead to altered surgery or alternative treatment for palatal apices.'}
    },
   ],
  },
  'cases': {
   'easy': [
    {'title': 'Identify Tooth', 'stem': 'A tooth has 3 roots and a Carabelli cusp trait.', 'question': 'Most likely?', 'answer': 'Maxillary first molar.', 'discussion': 'Know morphology for endo/restorative.', 'book_hint': "Wheeler's Dental Anatomy, Physiology and Occlusion"},
   ],
   'medium': [
    {'title': 'Endo Access Planning', 'stem': 'Upper first premolar needs RCT.', 'question': 'Anatomy alert?', 'answer': 'Often two canals — search carefully.', 'discussion': 'Missed canal → failure.', 'book_hint': "Wheeler's Dental Anatomy, Physiology and Occlusion"},
   ],
   'hard': [
    {'title': 'Young Tooth Prep Exposure Risk', 'stem': 'A teenager needs a deep occlusal restoration on a newly erupted molar. Choose the safest high-yield next concept before definitive results.', 'question': 'Anatomy concern?', 'answer': 'High pulp horns — careful depth, consider indirect pulp strategies.', 'discussion': 'Avoid iatrogenic exposure.', 'book_hint': "Wheeler's Dental Anatomy, Physiology and Occlusion"},
   ],
   'extreme': [
    {'title': 'Bizarre Root Morphology Pre-Extract', 'stem': 'A curved dilacerated premolar needs extraction under LA. Avoid harmful premature treatment while catastrophic differentials remain open.', 'question': 'Plan?', 'answer': 'Radiograph assessment, surgical sectioning readiness, avoid blind force.', 'discussion': 'Prevent root fracture/displacement.', 'book_hint': "Wheeler's Dental Anatomy, Physiology and Occlusion"},
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
