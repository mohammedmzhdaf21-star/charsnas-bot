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
     'options': ['A) Mandibular third molar, which erupts last and often lacks adequate arch space', 'B) Maxillary canine, which is the next most commonly impacted tooth but still less frequent than lower third molars', 'C) Mandibular first premolar, which usually erupts with adequate arch space and is rarely impacted', 'D) Maxillary first molar, which erupts into a prepared arch and is seldom truly impacted'],
     'answer': 'A) Mandibular third molar, which erupts last and often lacks adequate arch space',
     'explanation': 'Mandibular third molars erupt last into limited posterior space and are the most frequently impacted teeth, driving pericoronitis, distal second-molar caries, and common surgical removal. Maxillary canines are a close second in impaction frequency but remain far less common than lower wisdom teeth. Premolars and first molars rarely meet comparable eruption blockade.',
     'choice_explanations': {'A': 'Third molars erupt last with limited mandibular length; bone/soft-tissue/adjacent-tooth blockade makes them the most common impactions.', 'B': 'Near-miss: maxillary canines are the next most often impacted tooth, but mandibular third molars still predominate clinically.', 'C': 'First premolars usually erupt with space and are not the teeth most often impacted.', 'D': 'First molars erupt into a prepared arch and are rarely impacted relative to third molars.'}
    },
        {
     'question': 'For a classical inferior alveolar nerve block, anesthetic solution is deposited nearest which landmark?',
     'options': ['A) The mental foramen on the buccal mandibular body, which transmits the mental nerve after canal entry', 'B) The mandibular foramen on the medial surface of the ramus', 'C) The greater palatine foramen on the hard palate used for palatal soft-tissue anesthesia', 'D) The infraorbital foramen on the maxillary midface used for maxillary blocks'],
     'answer': 'B) The mandibular foramen on the medial surface of the ramus',
     'explanation': 'An IANB deposits anesthetic near the mandibular foramen/lingula on the medial ramus so the inferior alveolar nerve is bathed before entering the canal. The mental foramen is a close mandibular landmark distractor but lies after the nerve has already entered the canal. Palatal and infraorbital foramina serve other blocks.',
     'choice_explanations': {'A': 'Near-miss: the mental foramen is a mandibular nerve landmark, but it is not the IANB target—the IAN has already entered the canal.', 'B': 'IANB targets the IAN at the mandibular foramen/lingula on the medial ramus before canal entry.', 'C': 'Greater palatine anesthesia numbs posterior palate, not the inferior alveolar nerve.', 'D': 'Infraorbital foramen anesthesia is a maxillary technique, not inferior alveolar blockade.'}
    },
        {
     'question': 'Alveolar osteitis (dry socket) is best explained by which pathophysiologic sequence after extraction?',
     'options': ['A) Localized alveolar osteomyelitis with marrow infection beginning on the day of extraction', 'B) Irreversible pulpitis confined to an unrestored adjacent premolar without socket changes', 'C) Premature clot loss or fibrinolysis exposing bare alveolar bone, typically days 2–4', 'D) Acute maxillary sinusitis without alveolar communication or socket involvement'],
     'answer': 'C) Premature clot loss or fibrinolysis exposing bare alveolar bone, typically days 2–4',
     'explanation': 'Dry socket follows premature clot loss/fibrinolysis with exposed bone and severe localized pain, classically days 2–4 after difficult mandibular molar extraction. Localized osteomyelitis is the overlapping infection near-miss but implies true bone infection with different clinical cues. Pulpitis and sinusitis are separate pain sources unrelated to an empty socket.',
     'choice_explanations': {'A': 'Near-miss: osteomyelitis is true bone infection; dry socket is localized clot failure/fibrinolysis without that marrow-infection picture.', 'B': 'Pulpitis is intrapulpal inflammation of another tooth, not an empty post-extraction socket.', 'C': 'Alveolar osteitis is premature clot loss/fibrinolysis with exposed socket bone and delayed severe pain (days 2–4).', 'D': 'Sinusitis does not explain an empty mandibular extraction socket.'}
    },
   ],
   'medium': [
        {
     'question': 'A rapidly progressive floor-of-mouth infection with bilateral submandibular swelling and tongue elevation is managed first by addressing which priority?',
     'options': ['A) Urgent pulp extirpation of the source tooth alone without airway assessment', 'B) Observation for 72 hours before any antimicrobial or surgical therapy', 'C) Immediate full-mouth extraction under local anesthesia without drainage planning', 'D) Airway security, then IV antibiotics and urgent surgical drainage of involved spaces'],
     'answer': 'D) Airway security, then IV antibiotics and urgent surgical drainage of involved spaces',
     'explanation': 'Ludwig angina threatens the airway; priorities are airway protection, parenteral antibiotics, and surgical drainage, then source control. Urgent dental source therapy alone is a near-miss that addresses etiology later but skips the life-threatening airway/space sequence. Delayed observation or extractions without airway/drainage planning are clearly unsafe.',
     'choice_explanations': {'A': 'Near-miss: source-tooth endodontics matters later but does not secure the airway or drain bilateral deep spaces.', 'B': 'Watchful waiting in rapidly spreading floor-of-mouth infection risks airway obstruction and sepsis.', 'C': 'Multiple extractions under LA ignore airway risk and fail to drain deep fascial spaces.', 'D': 'Ludwig angina: secure airway, give IV antibiotics, and drain involved spaces before elective dentistry.'}
    },
        {
     'question': 'Before elective oral surgery in a patient taking warfarin, which laboratory parameter most directly guides bleeding-risk planning?',
     'options': ['A) INR (international normalized ratio)', 'B) aPTT alone as the primary monitor of warfarin therapeutic intensity', 'C) Serum amylase as a surrogate for clotting-factor activity', 'D) Fasting triglyceride level as a surgical bleeding-risk index'],
     'answer': 'A) INR (international normalized ratio)',
     'explanation': 'Warfarin effect is monitored with INR, which guides extraction timing and local hemostasis planning. aPTT is a close coagulation near-miss more relevant to heparin/intrinsic-pathway monitoring, not standard warfarin intensity. Amylase and triglycerides do not quantify anticoagulation.',
     'choice_explanations': {'A': 'INR quantifies warfarin’s vitamin K–antagonist effect and is the key pre-extraction bleeding-risk metric.', 'B': 'Near-miss: aPTT is a real coagulation assay but is not the standard monitor of therapeutic warfarin intensity (INR is).', 'C': 'Amylase reflects pancreatic/salivary enzyme activity, not warfarin anticoagulation.', 'D': 'Triglycerides relate to lipid risk, not surgical hemostasis under warfarin.'}
    },
        {
     'question': 'Oroantral communication risk is highest when extracting which teeth, based on root–sinus anatomy?',
     'options': ['A) Maxillary premolars, which can approximate the sinus but less often than molars overall', 'B) Maxillary molars whose roots approximate or project into the sinus floor', 'C) Mandibular canines in the anterior mandible remote from the antrum', 'D) Mandibular first premolars distant from the maxillary sinus'],
     'answer': 'B) Maxillary molars whose roots approximate or project into the sinus floor',
     'explanation': 'Oroantral communication risk is highest with maxillary molars because roots frequently lie against or within the sinus floor. Maxillary premolars are a true anatomic near-miss with occasional sinus proximity, but molar extractions carry the highest OAC incidence. Mandibular teeth have no continuity with the maxillary antrum.',
     'choice_explanations': {'A': 'Near-miss: maxillary premolars may approach the sinus, yet molars still carry the highest oroantral communication risk.', 'B': 'Maxillary molar root–antrum proximity explains the highest OAC risk during extraction.', 'C': 'Mandibular canines have no anatomic path into the maxillary sinus.', 'D': 'Mandibular premolars cannot open into the maxillary antrum.'}
    },
   ],
   'hard': [
        {
     'question': 'A 28-year-old needs removal of a mesioangular mandibular third molar. Panoramic and CBCT show darkening of the root, interruption of the white lines of the canal, and diversion of the inferior alveolar canal. Which intraoperative principle best reduces permanent neurosensory injury?',
     'options': ['A) Coronectomy leaving the roots whenever any canal proximity is seen, without case selection or consent', 'B) Blind aggressive elevation toward the canal relying on crown visibility alone', 'C) Use controlled sectioning and elevation away from the canal, with informed consent for IAN risk', 'D) Perform blind curettage of canal contents to free the root tip'],
     'answer': 'C) Use controlled sectioning and elevation away from the canal, with informed consent for IAN risk',
     'explanation': 'High-risk IAN imaging signs call for CBCT-informed sectioning, elevation away from the canal, and consent. Coronectomy can be appropriate in selected intimate root–canal cases, making an unselective/unconsented coronectomy the overlapping near-miss. Blind leverage or canal curettage increases nerve injury.',
     'choice_explanations': {'A': 'Near-miss: coronectomy is a valid nerve-sparing option in selected cases, but not an automatic substitute for planning, sectioning judgment, and informed consent.', 'B': 'Ignoring imaging and forcing toward the canal raises crush/stretch injury risk.', 'C': 'With canal–root intimacy, controlled sectioning, elevation away from the canal, and consent best reduce permanent IAN injury.', 'D': 'Curettage inside the canal can directly injure the IAN.'}
    },
        {
     'question': 'Two days after difficult lower third-molar removal, a patient has severe localized socket pain, an empty socket with gray debris, no fever, and no fluctuance. Which management best matches the diagnosis?',
     'options': ['A) Start empiric antibiotics for presumed localized alveolar osteomyelitis without local socket care', 'B) Immediate incision of the contralateral submandibular space', 'C) Urgent anticoagulation reversal for suspected hematoma alone', 'D) Irrigate gently and place a soothing medicated dressing; antibiotics are not first-line without infection'],
     'answer': 'D) Irrigate gently and place a soothing medicated dressing; antibiotics are not first-line without infection',
     'explanation': 'Empty painful socket at days 2–4 without systemic infection is alveolar osteitis managed with irrigation and dressing. Presuming osteomyelitis and giving antibiotics without local care is the close infectious near-miss. Contralateral space incision and anticoagulation reversal address unrelated problems.',
     'choice_explanations': {'A': 'Near-miss: osteomyelitis can cause post-extraction pain, but this afebrile empty-socket picture is dry socket needing local toilette/dressing first—not antibiotics alone.', 'B': 'Contralateral space incision treats deep-space infection, not an empty socket.', 'C': 'Anticoagulant reversal addresses bleeding risk, not fibrinolysis-related dry socket.', 'D': 'Classic dry socket: irrigate, medicated dressing, analgesia; antibiotics only if true infection is present.'}
    },
        {
     'question': 'During extraction of an upper first molar, a 4 mm communication to the antrum is noted with a positive Valsalva bubble test. The patient is otherwise healthy. What is the most appropriate immediate management concept?',
     'options': ['A) Inform the patient, place a tension-free soft-tissue closure when feasible, prescribe sinus precautions, and arrange follow-up', 'B) Close immediately with buccal fat-pad advancement as mandatory first-line for every fresh 4 mm OAC', 'C) Pack the antrum with nonresorbable cotton and discharge without sinus advice', 'D) Perform immediate Caldwell–Luc antrostomy as routine first-line for every small OAC'],
     'answer': 'A) Inform the patient, place a tension-free soft-tissue closure when feasible, prescribe sinus precautions, and arrange follow-up',
     'explanation': 'Small fresh OACs are managed with disclosure, primary closure when possible, sinus precautions, and review. Immediate buccal fat-pad closure is a close surgical near-miss more often reserved for larger or persistent fistulae. Antral cotton packing and routine Caldwell–Luc are inappropriate first steps.',
     'choice_explanations': {'A': 'Fresh small OAC: close mucosa if feasible, sinus precautions, follow-up; escalate if a fistula persists.', 'B': 'Near-miss: buccal fat-pad/layered closure is valuable for larger or persistent OACs, not automatically mandatory for every small fresh communication.', 'C': 'Nonresorbable antral packing invites infection and is not proper closure.', 'D': 'Caldwell–Luc is not first-line for a small fresh communication manageable locally.'}
    },
   ],
   'extreme': [
        {
     'question': 'A 62-year-old on warfarin for a mechanical mitral valve (INR 2.8 yesterday) needs urgent extraction of a fractured mandibular molar with continuous oozing. He reports prior TIA when warfarin was stopped elsewhere. There is no expanding hematoma or airway threat. Which management plan is most appropriate?',
     'options': ['A) Stop warfarin and bridge with low-molecular-weight heparin unilaterally without physician input for this valve', 'B) Coordinate with the physician, generally continue warfarin at therapeutic INR for single extraction, and emphasize local hemostasis (sutures, packing, tranexamic rinse) rather than unilateral cessation', 'C) Refuse all dental care permanently because mechanical valves contraindicate extraction', 'D) Give high-dose vitamin K empirically in clinic without assessing thrombotic indication'],
     'answer': 'B) Coordinate with the physician, generally continue warfarin at therapeutic INR for single extraction, and emphasize local hemostasis (sutures, packing, tranexamic rinse) rather than unilateral cessation',
     'explanation': 'Mechanical mitral valves are high thrombotic risk; most single extractions proceed with therapeutic INR and local hemostasis under physician coordination. Unilateral stop/bridge strategies are a dangerous overlapping anticoagulation near-miss. Permanent refusal or empiric vitamin K without indication is incorrect.',
     'choice_explanations': {'A': 'Near-miss: bridging/cessation protocols exist for some surgeries but must not be started unilaterally in mechanical mitral valve disease—and are usually unnecessary for simple extraction.', 'B': 'Continue warfarin at acceptable INR with meticulous local hemostasis and physician coordination.', 'C': 'Extractions can be performed safely with planning; lifelong refusal is not evidence-based.', 'D': 'Empiric vitamin K can precipitate valve thrombosis and is not clinic first-line here.'}
    },
        {
     'question': 'A 34-year-old develops progressive bilateral submandibular and submental swelling, dysphagia, and inability to protrude the tongue 24 hours after lower molar infection. SpO2 is 94% sitting forward. Which sequenced plan best reflects complication management?',
     'options': ['A) Give IV antibiotics promptly but delay drainage for 48 hours of observation if the patient can still sit forward', 'B) Perform only pulp therapy of the molar under rubber dam without airway planning', 'C) Emergent airway evaluation (often fiberoptic/awake strategies), IV broad-spectrum antibiotics, urgent incision and drainage of bilateral floor-of-mouth spaces, then source control', 'D) Start high-dose NSAIDs alone to reduce swelling while deferring drainage'],
     'answer': 'C) Emergent airway evaluation (often fiberoptic/awake strategies), IV broad-spectrum antibiotics, urgent incision and drainage of bilateral floor-of-mouth spaces, then source control',
     'explanation': 'Ludwig angina with desaturation needs airway-first care, IV antibiotics, and urgent drainage, then source control. IV antibiotics with delayed drainage is a close medical near-miss once airway signs appear. Pulp therapy alone or NSAIDs alone are clearly inadequate.',
     'choice_explanations': {'A': 'Near-miss: IV antibiotics are necessary, but observation without urgent airway planning and drainage is unsafe once airway compromise begins.', 'B': 'Pulp procedures do not secure the airway or drain fascial cellulitis.', 'C': 'Airway first, then IV antibiotics and urgent bilateral space drainage, then dental source control.', 'D': 'NSAIDs may ease pain but do not drain infection or protect the airway.'}
    },
        {
     'question': 'After surgical removal of a deeply impacted lower third molar, the patient awakens with complete anesthesia of the ipsilateral lower lip and chin. Intraoperatively the canal was visible and a root tip was elevated adjacent to it. Six hours later there is still dense anesthesia without dysesthesia. What is the best immediate counseling and next-step concept?',
     'options': ['A) Reassure that dense anesthesia always resolves fully within 24 hours without documentation', 'B) Immediate microneurosurgical exploration the same evening for every dense deficit without baseline sensory mapping', 'C) Start long-term high-dose opioids as the sole definitive nerve therapy', 'D) Document sensory mapping, explain possible neuropraxia versus more severe injury, avoid irreversible statements of permanence yet, arrange close neurosensory follow-up, and consider early specialist referral pathways used in your region'],
     'answer': 'D) Document sensory mapping, explain possible neuropraxia versus more severe injury, avoid irreversible statements of permanence yet, arrange close neurosensory follow-up, and consider early specialist referral pathways used in your region',
     'explanation': 'Postoperative complete lip/chin anesthesia after canal proximity needs documented sensory testing, honest counseling, and structured follow-up/referral because timing affects repair options. Immediate mandatory exploration is a specialist near-miss—early referral pathways matter, but same-night surgery without baseline mapping is not automatic. False reassurance or opioids alone are wrong.',
     'choice_explanations': {'A': 'Not all IAN injuries recover in 24 hours; skipping follow-up may miss repair windows.', 'B': 'Near-miss: early microsurgical pathways can be indicated for persistent dense deficits, but immediate exploration at six hours without documentation/protocol is not blanket first-line.', 'C': 'Opioids do not restore nerve continuity or guide repair timing.', 'D': 'Map sensation, counsel carefully, follow closely, and use timely specialist referral—avoid false permanence claims.'}
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
     'options': ['A) Distal molar relationship with proclined maxillary incisors and increased overjet', 'B) Distal molar relationship with retroclined maxillary central incisors (Class II division 2 pattern)', 'C) Class I molar relationship with edge-to-edge incisors only', 'D) Mesial molar relationship with reverse overjet (Angle Class III)'],
     'answer': 'A) Distal molar relationship with proclined maxillary incisors and increased overjet',
     'explanation': 'Angle Class II means a distal mandibular molar relationship. Division 1 shows proclined upper incisors and increased overjet; division 2 (retroclined centrals) is the close overlapping near-miss within Class II. Class I and Class III describe different molar relationships.',
     'choice_explanations': {'A': 'Class II division 1 = distal molar relation plus proclined upper incisors/increased overjet.', 'B': 'Near-miss: Class II division 2 also has a distal molar relation, but incisors are retroclined rather than proclined with large overjet.', 'C': 'Class I molars are not the Class II molar relationship.', 'D': 'Mesial molar relation with reverse overjet defines Class III, not Class II division 1.'}
    },
        {
     'question': 'Which tissue remodeling concept primarily allows orthodontic tooth movement through alveolar bone?',
     'options': ['A) Pressure-side bone apposition and tension-side resorption as the primary couple', 'B) Pressure-side resorption and tension-side apposition of alveolar bone', 'C) Pulp-stone remodeling that translates the tooth through bone', 'D) Enamel hyperplasia on the pressure side that pushes the crown through mucosa'],
     'answer': 'B) Pressure-side resorption and tension-side apposition of alveolar bone',
     'explanation': 'Orthodontic movement depends on osteoclastic resorption on the pressure side and osteoblastic apposition on the tension side via the PDL. Reversing that couple is a classic overlapping biomechanics near-miss. Pulp stones and enamel hyperplasia do not relocate teeth through alveolus.',
     'choice_explanations': {'A': 'Near-miss: this reverses the correct pressure/tension bone responses; resorption is on the pressure side, apposition on tension.', 'B': 'Sustained force causes pressure-side resorption and tension-side bone formation, allowing tooth movement.', 'C': 'Pulp stones are intrapulpal calcifications and do not translate the tooth.', 'D': 'Enamel does not remodel to move teeth through alveolar bone.'}
    },
        {
     'question': 'Anchorage in orthodontics refers primarily to which clinical concept?',
     'options': ['A) The maximum force a nickel-titanium wire can deliver before permanent set', 'B) The reciprocal force magnitude on the active unit alone without considering support units', 'C) Resistance to unwanted tooth movement used to support desired movement', 'D) The bracket prescription torque value printed by the manufacturer'],
     'answer': 'C) Resistance to unwanted tooth movement used to support desired movement',
     'explanation': 'Anchorage is resistance of supporting units to unwanted reaction movement while desired teeth move. Confusing anchorage with active-unit force magnitude or wire properties is a close biomechanics near-miss. Bracket prescription labels torque/tip, not anchorage itself.',
     'choice_explanations': {'A': 'Wire elastic limits describe material properties, not the clinical definition of anchorage.', 'B': 'Near-miss: reaction force on the active unit is related, but anchorage specifically means resistance of support units to unwanted movement.', 'C': 'Anchorage = controlling reaction forces so supporting units resist unwanted movement while targets move.', 'D': 'Bracket prescription encodes tip/torque geometry, not anchorage planning.'}
    },
   ],
   'medium': [
        {
     'question': 'A growing Class II patient with mandibular retrognathia and good compliance is being considered for functional appliance therapy. Which applied principle best matches indication?',
     'options': ['A) Begin functional appliance therapy after radiographic confirmation of growth cessation', 'B) Extract all third molars as the sole Class II skeletal correction', 'C) Camouflage with anterior elastics only while ignoring remaining growth potential', 'D) Use growth modification while the patient is still growing to advance mandibular posture/remodeling'],
     'answer': 'D) Use growth modification while the patient is still growing to advance mandibular posture/remodeling',
     'explanation': 'Functional appliances for mandibular retrognathia are timed to remaining growth. Starting them after growth cessation is the overlapping timing near-miss—those patients need camouflage or surgery instead. Third-molar extraction or elastics-only plans do not produce meaningful skeletal Class II correction in this indication.',
     'choice_explanations': {'A': 'Near-miss: functional appliances lose skeletal utility after growth completion; timing while growing is the key indication.', 'B': 'Third-molar extraction does not correct Class II molar/skeletal relations by itself.', 'C': 'Elastics mainly move teeth and skip the growth-modification opportunity described.', 'D': 'Growth modification for mandibular retrognathia is indicated while growth remains.'}
    },
        {
     'question': 'During space closure on a continuous archwire, the posterior unit drifts mesially more than planned. Which applied diagnosis fits best?',
     'options': ['A) Anchorage loss from insufficient posterior resistance relative to anterior retraction force', 'B) Planned reciprocal space closure with intentional molar mesialization under maximum anchorage', 'C) Enamel fluorosis unrelated to space-closure mechanics', 'D) Frictionless ideal sliding with zero reaction force on the posterior unit'],
     'answer': 'A) Anchorage loss from insufficient posterior resistance relative to anterior retraction force',
     'explanation': 'Unplanned molar mesialization during retraction is anchorage loss from inadequate posterior resistance. Intentional molar mesialization under a planned anchorage scheme is the close mechanical near-miss—here the movement is more than planned, so it is loss, not prescribed reciprocity. Fluorosis and “zero reaction force” are not valid mechanic diagnoses.',
     'choice_explanations': {'A': 'Unplanned molar mesialization during retraction is classic anchorage loss.', 'B': 'Near-miss: intentional molar mesialization can be planned, but this stem describes drift more than planned (= anchorage loss).', 'C': 'Fluorosis is a developmental enamel defect, not a space-closure mechanic diagnosis.', 'D': 'Every orthodontic force has an equal opposite reaction; zero posterior reaction is physically false.'}
    },
        {
     'question': 'A patient presents with anterior open bite, tongue thrust habit, and increased lower face height. Which applied treatment concept is most coherent?',
     'options': ['A) Close the open bite with anterior vertical elastics alone without habit or vertical skeletal assessment', 'B) Address habit and vertical control; consider habit therapy, orthodontics, and possible surgical options if skeletal vertical excess persists', 'C) Prescribe antibiotics for the open bite as primary therapy', 'D) Extract maxillary laterals routinely as first-line for all open bites'],
     'answer': 'B) Address habit and vertical control; consider habit therapy, orthodontics, and possible surgical options if skeletal vertical excess persists',
     'explanation': 'Anterior open bite often combines habit and vertical skeletal/dental factors; stable care addresses habit and vertical control, with surgery for severe skeletal excess. Anterior vertical elastics alone are a close overlapping tactic that can help dental open bites but fail when habit/skeletal vertical excess dominate. Antibiotics and routine lateral extraction are clearly wrong.',
     'choice_explanations': {'A': 'Near-miss: anterior elastics may aid some dental open bites but omit habit control and skeletal vertical diagnosis required here.', 'B': 'Open-bite care targets habit and vertical skeletal/dental factors; surgery may be needed for true vertical excess.', 'C': 'Open bite is not an infection requiring antibiotics.', 'D': 'Routine lateral extraction is not a universal open-bite solution and may worsen esthetics.'}
    },
   ],
   'hard': [
        {
     'question': 'A 13-year-old has a unilateral posterior crossbite with functional shift of the mandible toward the crossbite side, asymmetric CO–CR, and a midline deviation that improves when the mandible is guided to CR. What is the most appropriate early management concept?',
     'options': ['A) Delay transverse correction until adulthood because functional shifts always self-correct', 'B) Correct the anteroposterior Class II first with headgear and ignore the crossbite shift', 'C) Correct the transverse discrepancy early (e.g., expansion) to eliminate the shift and reduce asymmetric growth risk', 'D) Extract the shifting-side canine immediately as sole therapy'],
     'answer': 'C) Correct the transverse discrepancy early (e.g., expansion) to eliminate the shift and reduce asymmetric growth risk',
     'explanation': 'A functional shift from unilateral crossbite warrants early transverse correction to stop asymmetric guidance. Prioritizing AP mechanics while leaving the crossbite is a close treatment-sequencing near-miss that fails to remove the shift etiology. Waiting for self-correction or extracting a canine alone is incorrect.',
     'choice_explanations': {'A': 'Functional shifts do not reliably self-correct and may worsen facial asymmetry with growth.', 'B': 'Near-miss: AP appliances may be part of care later, but the functional shift from crossbite should be corrected early first.', 'C': 'Early expansion/transverse correction eliminates the occlusal interference driving the mandibular shift.', 'D': 'Canine extraction does not remove the transverse interference causing the shift.'}
    },
        {
     'question': 'An adult Class III patient shows edge-to-edge incisors in CR but clear reverse overjet in CO, with a large CO–CR discrepancy and dental compensations (proclined lower incisors). Which treatment-planning distinction is most critical?',
     'options': ['A) Treat as true skeletal Class III needing orthognathic surgery based on CO alone without CR evaluation', 'B) Treat only with a nightguard without occlusal shift diagnosis', 'C) Ignore CR records because CO is always identical to CR', 'D) Differentiate pseudo-Class III (functional shift) from true skeletal Class III before choosing camouflage versus surgery'],
     'answer': 'D) Differentiate pseudo-Class III (functional shift) from true skeletal Class III before choosing camouflage versus surgery',
     'explanation': 'Edge-to-edge in CR with reverse overjet in CO suggests pseudo-Class III/functional shift until skeletal Class III is confirmed in CR. Jumping to surgery from CO alone is the overlapping planning near-miss. Nightguards or assuming CO=CR miss the diagnostic distinction.',
     'choice_explanations': {'A': 'Near-miss: true skeletal Class III may need surgery, but CO-only diagnosis without CR risks operating on a pseudo-Class III shift.', 'B': 'A nightguard without diagnosing shift vs skeletal discrepancy misses definitive care.', 'C': 'CO and CR often differ in shift cases; ignoring CR risks wrong surgery/camouflage choice.', 'D': 'CO–CR analysis distinguishes functional pseudo-Class III from true skeletal Class III and changes the plan.'}
    },
        {
     'question': 'Mid-treatment, a patient on rectangular stainless steel wires develops increasing root resorption on maxillary incisors, short roots on start films, and heavy continuous forces historically used. Which multi-cue adjustment is most appropriate?',
     'options': ['A) Reduce force magnitude/duration, pause aggressive torque, reassess radiographs, and reconsider treatment goals', 'B) Continue current heavy torque on rectangular SS but shorten appointments only', 'C) Ignore resorption because orthodontic forces never affect root length', 'D) Switch solely to bleaching trays as root therapy'],
     'answer': 'A) Reduce force magnitude/duration, pause aggressive torque, reassess radiographs, and reconsider treatment goals',
     'explanation': 'External apical root resorption risk rises with heavy force, long treatment, and torque—especially with short roots. The correct response is force reduction, possible pause, monitoring, and goal revision. Merely shortening visits while continuing heavy torque is a close insufficient near-miss. Denial or bleaching is wrong.',
     'choice_explanations': {'A': 'When resorption cues appear, lighten forces, limit torque/duration, monitor, and revise goals.', 'B': 'Near-miss: appointment timing changes do not offset ongoing heavy continuous torque that drives resorption.', 'C': 'Orthodontic force can cause iatrogenic root resorption; denial is incorrect.', 'D': 'Bleaching does not treat or reverse root resorption.'}
    },
   ],
   'extreme': [
        {
     'question': 'A 16-year-old with severe Class II division 1, overjet 10 mm, incompetent lips, and a history of traumatic upper incisor fracture presents for comprehensive care. Growth charts suggest little remaining mandibular growth. Cephalometrics show marked mandibular retrognathia and upright lower incisors. Which decision pathway best balances occlusion, face, and trauma risk?',
     'options': ['A) Promise complete skeletal correction using only Class II elastics without surgery counseling', 'B) Discuss camouflage limits versus orthognathic advancement after growth completion, protect incisors meanwhile, and avoid promising full skeletal correction with elastics alone', 'C) Extract all remaining healthy teeth to eliminate overjet without prosthetic plan', 'D) Defer any trauma protection because large overjet never increases injury risk'],
     'answer': 'B) Discuss camouflage limits versus orthognathic advancement after growth completion, protect incisors meanwhile, and avoid promising full skeletal correction with elastics alone',
     'explanation': 'With little residual growth, severe skeletal Class II needs honest camouflage-versus-surgery counseling plus interim trauma protection. Elastics-only skeletal promises are the overlapping mechanics near-miss—elastics move teeth, not adult mandibular length. Mutilating extractions or deferring trauma protection are clearly wrong.',
     'choice_explanations': {'A': 'Near-miss: Class II elastics are used in camouflage but cannot reliably create substantial adult mandibular skeletal advancement.', 'B': 'Post-growth severe skeletal Class II needs surgery-vs-camouflage counseling plus interim trauma protection.', 'C': 'Extracting healthy dentition without reconstruction is mutilating and not a Class II solution.', 'D': 'Increased overjet is a documented trauma risk factor; protection should not be deferred.'}
    },
        {
     'question': 'An adult interdisciplinary case shows pathologic migration of upper incisors, 6 mm pocketing, reduced bone height, and a diastema increasing over 2 years. The patient wants braces immediately for esthetics. Periodontal charting and radiographs confirm uncontrolled inflammation. What is the most appropriate sequenced decision?',
     'options': ['A) Bond immediately with light forces despite active periodontitis, postponing hygiene until alignment finishes', 'B) Extract all periodontally involved teeth before any hygiene phase', 'C) Stabilize periodontal disease first (cause-related therapy ± surgery), then consider limited orthodontics with light forces and retention planning', 'D) Place veneers only over inflamed bleeding tissues without periodontal care'],
     'answer': 'C) Stabilize periodontal disease first (cause-related therapy ± surgery), then consider limited orthodontics with light forces and retention planning',
     'explanation': 'Orthodontics in uncontrolled periodontitis can accelerate attachment loss. Periodontal stabilization first, then careful light-force movement, is correct. Starting ortho with “light forces” while inflammation remains uncontrolled is the overlapping near-miss. Premature extractions or veneers over inflamed tissue are wrong.',
     'choice_explanations': {'A': 'Near-miss: light forces matter later, but active periodontitis must be controlled before tooth movement begins.', 'B': 'Extractions before hygiene assessment skip reversible disease control and informed planning.', 'C': 'Stabilize periodontitis first; then consider limited light-force orthodontics and retention.', 'D': 'Veneering inflamed tissues traps plaque and ignores biologic foundation.'}
    },
        {
     'question': 'During combined orthodontic–orthognathic planning for skeletal open bite, models show dental compensation with already proclined upper and lower incisors, narrow maxilla, and gummy smile from vertical maxillary excess. Which complication-aware plan is most coherent?',
     'options': ['A) Extrude molars further with continuous anterior elastics as sole adult skeletal cure', 'B) Expand with bone-borne/skeletally anchored expansion alone and ignore vertical maxillary excess', 'C) Ignore vertical excess and finish with anterior bonding alone', 'D) Plan skeletal correction (often segmental maxillary surgery ± mandibular procedures) rather than further dental proclination that would decompensate poorly and relapse vertically'],
     'answer': 'D) Plan skeletal correction (often segmental maxillary surgery ± mandibular procedures) rather than further dental proclination that would decompensate poorly and relapse vertically',
     'explanation': 'Adult skeletal open bite with VME typically needs surgical (or major skeletal-anchorage) correction rather than more dental compensation. Bone-borne expansion may help transverse width but is a near-miss if vertical excess/open bite skeletal pattern is ignored. Molar extrusion or bonding alone worsens or leaves the skeletal problem.',
     'choice_explanations': {'A': 'Molar extrusion increases vertical dimension and can worsen open bite.', 'B': 'Near-miss: skeletal expansion can address transverse deficiency, but VME/open-bite skeletal pattern still needs vertical skeletal planning.', 'C': 'Anterior bonding without vertical skeletal correction leaves gummy smile and open bite uncorrected.', 'D': 'True skeletal open bite/VME requires skeletal surgery or equivalent skeletal strategies—not more dental proclination.'}
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
     'options': ['A) Subgingival biofilm within the periodontal pocket', 'B) Supragingival biofilm at the gingival margin without pocket extension', 'C) Sterile pulp tissue of intact virgin teeth', 'D) Keratinized palate remote from the gingival margin'],
     'answer': 'A) Subgingival biofilm within the periodontal pocket',
     'explanation': 'Periodontitis is driven largely by dysbiotic subgingival biofilm in pockets interacting with a susceptible host. Supragingival biofilm is a close related niche that initiates gingivitis but is not the primary progressive periodontitis habitat once pockets form. Pulp and distant palate are unrelated niches.',
     'choice_explanations': {'A': 'Subgingival pocket biofilm is the key microbial niche for periodontitis progression.', 'B': 'Near-miss: supragingival biofilm causes gingivitis and feeds subgingival ecosystems, but established periodontitis centers on subgingival pocket biofilm.', 'C': 'Intact pulp is not the periodontitis biofilm habitat.', 'D': 'Palatal mucosa remote from the sulcus is not the pocket niche.'}
    },
        {
     'question': 'Clinical attachment loss is measured as which combination?',
     'options': ['A) Probing depth alone without referencing the cementoenamel junction', 'B) Probing depth plus gingival recession relative to the cementoenamel junction (or equivalent landmark)', 'C) Pulp vitality test scores converted to millimeters', 'D) Salivary flow rate in mL/min as an attachment surrogate'],
     'answer': 'B) Probing depth plus gingival recession relative to the cementoenamel junction (or equivalent landmark)',
     'explanation': 'Clinical attachment level references the CEJ, combining probing depth with gingival margin position. Probing depth alone is the classic overlapping near-miss—it measures pocket depth but not cumulative attachment loss when margins migrate. Vitality and salivary tests assess other domains.',
     'choice_explanations': {'A': 'Near-miss: probing depth is related but does not equal CAL without CEJ/margin reference, especially with recession or hyperplasia.', 'B': 'CAL integrates pocket depth and gingival margin position relative to the CEJ.', 'C': 'Pulp tests assess endodontic status, not attachment level.', 'D': 'Salivary flow assesses dry-mouth risk, not CAL.'}
    },
        {
     'question': 'What is the principal goal of nonsurgical periodontal therapy (scaling and root planing)?',
     'options': ['A) Surgically eliminate every infrabony defect at the first visit before biofilm control', 'B) Chemically sterilize cementum with caustic agents as the sole therapy', 'C) Disrupt and reduce subgingival biofilm and calculus to allow inflammation resolution', 'D) Replace all amalgams regardless of periodontal status'],
     'answer': 'C) Disrupt and reduce subgingival biofilm and calculus to allow inflammation resolution',
     'explanation': 'Nonsurgical therapy aims to disrupt/reduce subgingival biofilm and calculus so inflammation can resolve. Jumping to resective/regenerative surgery before cause-related therapy is the sequencing near-miss. Caustic “sterilization” or blanket amalgam replacement is not SRP’s goal.',
     'choice_explanations': {'A': 'Near-miss: surgery may follow re-evaluation, but nonsurgical biofilm/calculus control comes first.', 'B': 'Caustic cementum sterilization is not modern nonsurgical periodontal therapy.', 'C': 'SRP aims to control subgingival biofilm/calculus load so inflammation can resolve.', 'D': 'Blanket amalgam replacement does not treat periodontitis etiology.'}
    },
   ],
   'medium': [
        {
     'question': 'A patient has bleeding on probing, 5–6 mm pockets, radiographic horizontal bone loss, and poor interdental cleaning. After oral hygiene instruction, what is the most appropriate next applied therapy?',
     'options': ['A) Immediate open-flap debridement at every 5 mm site before attempting nonsurgical therapy', 'B) Systemic antifungals as sole periodontitis therapy', 'C) Orthognathic surgery as first-line pocket therapy', 'D) Quadrant or full-mouth scaling and root planing with risk-factor counseling'],
     'answer': 'D) Quadrant or full-mouth scaling and root planing with risk-factor counseling',
     'explanation': 'After OHI, nonsurgical debridement is first-line for periodontitis with residual pockets. Immediate surgery at all 5 mm sites is the overlapping next-step near-miss—surgery is considered after cause-related therapy and re-evaluation. Antifungals and orthognathic surgery are unrelated first-line pocket care.',
     'choice_explanations': {'A': 'Near-miss: surgical access can help residual deep sites later, but SRP is the appropriate next therapy after OHI here.', 'B': 'Antifungals do not address bacterial dysbiosis of periodontitis.', 'C': 'Jaw surgery does not replace periodontal cause-related therapy.', 'D': 'Applied periodontitis care: OHI then SRP and risk-factor control before resective/regenerative surgery.'}
    },
        {
     'question': 'Which local anatomic factor most commonly perpetuates plaque retention and localized periodontal destruction adjacent to a restoration?',
     'options': ['A) Overhanging restoration margin that harbors biofilm', 'B) Open margin or deficient contact that traps interproximal plaque without a true overhang ledge', 'C) Perfectly polished supragingival margin flush with enamel', 'D) Well-contoured open embrasure allowing cleaning access'],
     'answer': 'A) Overhanging restoration margin that harbors biofilm',
     'explanation': 'Overhangs are classic local plaque traps that perpetuate localized periodontal destruction. Open margins/poor contacts are a close restorative near-miss that also retain plaque, but the question asks the most common overhang-type anatomic factor. Flush polished margins and cleansable embrasures favor health.',
     'choice_explanations': {'A': 'Restorative overhangs are classic local plaque traps that worsen localized periodontitis.', 'B': 'Near-miss: open margins/poor contacts also retain plaque, but overhanging ledges are the classic most-cited local factor in this stem.', 'C': 'Flush polished margins minimize retention rather than perpetuate disease.', 'D': 'Open cleansable embrasures facilitate hygiene rather than trap plaque.'}
    },
        {
     'question': 'In a medically controlled diabetic patient with periodontitis, which applied counseling point is most accurate?',
     'options': ['A) Diabetes increases periodontitis risk unidirectionally with no effect of periodontitis on glycemia', 'B) Bidirectional link: poorly controlled diabetes worsens periodontitis; periodontitis can impair glycemic control', 'C) Periodontal therapy is contraindicated in all diabetics', 'D) Only type 1 diabetes matters; type 2 is irrelevant to periodontal risk'],
     'answer': 'B) Bidirectional link: poorly controlled diabetes worsens periodontitis; periodontitis can impair glycemic control',
     'explanation': 'Diabetes and periodontitis interact bidirectionally. A unidirectional “diabetes worsens perio only” statement is the overlapping incomplete near-miss. Therapy is indicated with precautions; type 2 diabetes is a major risk modifier.',
     'choice_explanations': {'A': 'Near-miss: diabetes clearly worsens periodontitis, but the relationship is bidirectional—periodontitis can also impair glycemic control.', 'B': 'Poor glycemic control worsens periodontitis; periodontitis can worsen glycemic control—manage both.', 'C': 'Diabetics benefit from periodontal care with appropriate precautions.', 'D': 'Type 2 diabetes is a major periodontitis risk modifier.'}
    },
   ],
   'hard': [
        {
     'question': 'A 42-year-old nonsmoker shows molar deep vertical defects, first-molar furcation grade II, thin phenotype, and plaque scores improved after SRP but 7 mm residual vertical defects remain with bleeding. Which multi-cue next step is most rational?',
     'options': ['A) Repeat nonsurgical debridement indefinitely without considering surgical access for residual deep vertical/furcation defects', 'B) Extract all molars immediately without regenerative assessment', 'C) Consider periodontal surgery, often regenerative approaches for contained vertical/furcation defects after inflammation control', 'D) Place a cantilever bridge from canine to second molar without perio stability'],
     'answer': 'C) Consider periodontal surgery, often regenerative approaches for contained vertical/furcation defects after inflammation control',
     'explanation': 'After adequate SRP, residual deep vertical defects and grade II furcations may benefit from surgical/regenerative therapy. Endless nonsurgical-only care is the close sequencing near-miss when anatomy favors surgery. Automatic extraction or prosthetic loading of unstable periodontium is wrong.',
     'choice_explanations': {'A': 'Near-miss: re-debridement helps some sites, but persistent deep vertical/furcation defects after SRP often need surgical evaluation.', 'B': 'Not all such molars require extraction; regeneration may save teeth.', 'C': 'Residual deep vertical/furcation defects after inflammation control often warrant regenerative or resective surgical evaluation.', 'D': 'Prostheses on unstable periodontium accelerate failure.'}
    },
        {
     'question': 'A pregnant patient in the second trimester has pregnancy-associated gingival enlargement, bleeding, and plaque. Radiographs (already available pre-pregnancy) show mild bone loss. Which management vignette is most appropriate?',
     'options': ['A) Perform elective gingivectomy now for mild pregnancy enlargement before maximizing plaque control', 'B) Extract all first molars prophylactically in the first trimester', 'C) Take a full new FMX every month throughout pregnancy', 'D) Reinforce plaque control, provide gentle debridement as needed, and defer elective surgery until after delivery unless severe'],
     'answer': 'D) Reinforce plaque control, provide gentle debridement as needed, and defer elective surgery until after delivery unless severe',
     'explanation': 'Pregnancy-associated gingival enlargement usually responds to plaque control and gentle debridement; elective soft-tissue surgery is deferred unless severe/refractory. Elective gingivectomy during pregnancy for mild disease is the overlapping surgical near-miss. Prophylactic extractions and monthly FMX are clearly inappropriate.',
     'choice_explanations': {'A': 'Near-miss: gingivectomy can be used for severe refractory overgrowth, but mild pregnancy gingivitis is managed with hygiene/debridement and elective surgery is deferred.', 'B': 'Prophylactic molar extractions are not indicated for pregnancy gingivitis.', 'C': 'Monthly FMX contradicts ALARA; use radiographs only when justified.', 'D': 'Reinforce plaque control and gentle debridement; defer elective surgery until after delivery unless severe.'}
    },
        {
     'question': 'A patient on long-term calcium-channel blockers develops firm lobulated gingival overgrowth covering half the crowns, with pseudopockets and plaque. Blood pressure is stable. Which multi-cue plan fits best?',
     'options': ['A) Intensify hygiene, consult the physician about alternative antihypertensives, then consider gingivectomy if fibrous overgrowth persists', 'B) Perform gingivectomy immediately without hygiene improvement or drug review', 'C) Stop the antihypertensive unilaterally in the dental chair', 'D) Place orthodontic brackets under the overgrown tissue immediately'],
     'answer': 'A) Intensify hygiene, consult the physician about alternative antihypertensives, then consider gingivectomy if fibrous overgrowth persists',
     'explanation': 'Drug-influenced gingival enlargement is plaque-modulated; manage hygiene, physician-coordinated drug substitution, then surgery for residual fibrotic tissue. Immediate gingivectomy without hygiene/drug review is the overlapping treatment near-miss. Unilateral drug cessation or bracketing under overgrowth is wrong.',
     'choice_explanations': {'A': 'Drug-related overgrowth: hygiene + physician-coordinated drug review ± gingivectomy for residual fibrous tissue.', 'B': 'Near-miss: gingivectomy may be needed, but not before plaque control and consideration of drug substitution.', 'C': 'Stopping BP medication without physician coordination risks hypertensive crisis.', 'D': 'Orthodontics under uncleansable overgrowth worsens inflammation.'}
    },
   ],
   'extreme': [
        {
     'question': 'A 29-year-old presents with rapidly progressing attachment loss, sparse plaque relative to destruction, neutrophil dysfunction history, and angular bone defects around incisors and first molars. Family history is positive. Which differential-driven plan is most appropriate?',
     'options': ['A) Treat as chronic plaque-induced periodontitis with routine hygiene intervals only', 'B) Suspect historically termed aggressive/molar-incisor pattern periodontitis, perform microbial/host risk assessment as indicated, deliver intensive mechanical therapy ± adjunctive antimicrobials per protocol, and screen relatives', 'C) Assume trauma from occlusion alone explains angular defects without biofilm control', 'D) Provide only whitening trays because the chief complaint is esthetics'],
     'answer': 'B) Suspect historically termed aggressive/molar-incisor pattern periodontitis, perform microbial/host risk assessment as indicated, deliver intensive mechanical therapy ± adjunctive antimicrobials per protocol, and screen relatives',
     'explanation': 'Rapid molar-incisor destruction with discordant plaque and familial aggregation suggests a distinct host–microbe pattern needing intensive therapy and family awareness. Managing it as routine chronic periodontitis with ordinary intervals is the overlapping under-treatment near-miss. Occlusion-only or whitening-only plans are wrong.',
     'choice_explanations': {'A': 'Near-miss: it is still periodontitis, but the rapid molar-incisor/host pattern needs more intensive therapy and risk assessment than routine chronic recall alone.', 'B': 'Rapid molar-incisor destruction with host clues needs intensive mechanical therapy ± adjunctive antimicrobials and family screening.', 'C': 'Occlusal trauma may cofactor but does not replace anti-infective therapy.', 'D': 'Whitening does not stop attachment loss.'}
    },
        {
     'question': 'Three years after implant placement, a patient shows bleeding, 7 mm peri-implant probing, radiographic cratering around a screw-retained molar implant, excess cement history on the prior crown, and poor oral hygiene. The implant is still immobile. What complication-management sequence is best?',
     'options': ['A) Diagnose peri-implant mucositis and limit care to antiseptic rinses without addressing bone loss or cement', 'B) Tighten the implant by further torque into infected bone as sole therapy', 'C) Diagnose peri-implantitis, remove cement/plaque retentive factors, perform nonsurgical then often surgical decontamination/regeneration or resective therapy, and intensify maintenance', 'D) Prescribe antifungals alone without debridement or prosthetic correction'],
     'answer': 'C) Diagnose peri-implantitis, remove cement/plaque retentive factors, perform nonsurgical then often surgical decontamination/regeneration or resective therapy, and intensify maintenance',
     'explanation': 'Bleeding, deep peri-implant probing, and cratering indicate peri-implantitis, not mucositis alone. Calling it mucositis and using rinses only is the overlapping diagnostic near-miss that under-treats progressive bone loss. Further torque or antifungals alone are incorrect.',
     'choice_explanations': {'A': 'Near-miss: mucositis lacks progressive bone loss; radiographic cratering here indicates peri-implantitis needing more than rinses.', 'B': 'Additional torque does not resolve infection and may damage the bone–implant interface.', 'C': 'Peri-implantitis needs etiologic factor removal, decontamination (often surgical), and maintenance.', 'D': 'Bacterial biofilm/cement, not Candida alone, typically drive peri-implantitis.'}
    },
        {
     'question': 'A stage IV periodontitis patient needs replacement of failing upper molars. Residual ridges show severe vertical defects, sinus pneumatization, and uncontrolled interproximal plaque on abutments of an old bridge. The patient requests immediate full-arch fixed implants this week. Which decision is most defensible?',
     'options': ['A) Place implants immediately through active periodontal pockets without a hygiene phase', 'B) Guarantee lifelong implant success regardless of maintenance', 'C) Leave the uncleanable bridge and add cantilever pontics over inflamed abutments', 'D) Control periodontal infection first, then stage ridge/sinus evaluation and implant planning; do not place implants into uncontrolled periodontitis and uncleanable prosthetic designs'],
     'answer': 'D) Control periodontal infection first, then stage ridge/sinus evaluation and implant planning; do not place implants into uncontrolled periodontitis and uncleanable prosthetic designs',
     'explanation': 'Active periodontitis and poor hygiene raise peri-implantitis risk; infection control and maintainable design must precede implants. Immediate full-arch placement into uncontrolled disease is the overlapping impatient near-miss. Success guarantees or extending uncleanable bridges are wrong.',
     'choice_explanations': {'A': 'Near-miss: immediate implants can be used in selected clean, planned cases—but not into uncontrolled periodontitis and uncleanable designs.', 'B': 'No implant system guarantees lifelong success without maintenance.', 'C': 'Extending uncleanable inflamed bridgework worsens prognosis.', 'D': 'Stabilize periodontitis and plan staged reconstruction with maintainable prostheses before implants.'}
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
     'options': ['A) Spontaneous or lingering pain to thermal stimuli that persists after stimulus removal', 'B) Brief nonlingering sensitivity only to cold that resolves quickly after stimulus removal', 'C) Complete absence of response to vitality tests with a draining sinus tract', 'D) Pain only on biting that localizes with a bite stick and is relieved when pressure is released away from a crack'],
     'answer': 'A) Spontaneous or lingering pain to thermal stimuli that persists after stimulus removal',
     'explanation': 'Irreversible pulpitis features spontaneous or lingering thermal pain. Brief nonlingering cold sensitivity (reversible pulpitis) is the classic overlapping near-miss. Nonresponse with sinus tract suggests necrosis/chronic apical abscess; isolated bite pain suggests crack/periapical bite issues.',
     'choice_explanations': {'A': 'Lingering/spontaneous thermal pain characterizes irreversible pulpitis.', 'B': 'Near-miss: brief nonlingering cold sensitivity is reversible pulpitis, not irreversible.', 'C': 'No response with sinus tract suggests necrosis/chronic apical disease, not irreversible pulpitis symptoms.', 'D': 'Isolated bite pain points more to crack or periapical mechanical pain than classic irreversible pulpitis.'}
    },
        {
     'question': 'The working length in root canal treatment is ideally determined to which apical reference concept?',
     'options': ['A) At the radiographic apex or slightly beyond to ensure apical patency in all cases', 'B) Near the apical constriction / cemento-dentinal junction region short of overinstrumentation', 'C) Exactly at the midroot level for all teeth', 'D) Only to the pulp chamber floor without entering canals'],
     'answer': 'B) Near the apical constriction / cemento-dentinal junction region short of overinstrumentation',
     'explanation': 'Working length targets the apical constriction (near CDJ), usually slightly short of the radiographic apex. Instrumenting to/beyond the radiographic apex is the overlapping length near-miss that risks overinstrumentation. Midroot or chamber-only lengths leave untreated canal infection.',
     'choice_explanations': {'A': 'Near-miss: the radiographic apex is close to the target, but ideal length is the apical constriction slightly short of overinstrumenting beyond the apex.', 'B': 'Working length targets the apical constriction region, confirmed with apex locator and radiograph.', 'C': 'Midroot length leaves apical canal untreated.', 'D': 'Chamber-only treatment is not root canal therapy of the canal system.'}
    },
        {
     'question': 'Sodium hypochlorite is used as an endodontic irrigant primarily because it provides which dual action?',
     'options': ['A) Chelation and smear-layer removal as its sole primary irrigant actions', 'B) Radiopaque obturation of the canal space like gutta-percha', 'C) Tissue dissolution and antimicrobial activity within the canal system', 'D) Selective anesthesia of the inferior alveolar nerve'],
     'answer': 'C) Tissue dissolution and antimicrobial activity within the canal system',
     'explanation': 'NaOCl dissolves organic tissue and provides broad antimicrobial action. EDTA-style chelation/smear removal is the overlapping irrigant near-miss—important adjunctively, but not NaOCl’s primary dual action. NaOCl is neither obturation material nor a nerve block agent.',
     'choice_explanations': {'A': 'Near-miss: chelators (e.g., EDTA) remove smear layer; NaOCl’s primary dual roles are tissue dissolution and antimicrobial activity.', 'B': 'Gutta-percha/sealer provide obturation, not irrigant NaOCl.', 'C': 'NaOCl dissolves necrotic pulp tissue and disinfects the canal system.', 'D': 'Local anesthetics—not irrigants—block peripheral nerves.'}
    },
   ],
   'medium': [
        {
     'question': 'A tooth with necrotic pulp, sinus tract, and periapical radiolucency is best managed by which applied endodontic approach when restorability is adequate?',
     'options': ['A) Antibiotics alone without canal debridement', 'B) Indirect pulp cap over necrotic pulp tissue', 'C) Incise and drain the sinus tract as sole definitive therapy', 'D) Nonsurgical root canal treatment to eliminate intracanal infection, with restoration of the tooth'],
     'answer': 'D) Nonsurgical root canal treatment to eliminate intracanal infection, with restoration of the tooth',
     'explanation': 'Necrotic pulp with apical disease needs chemomechanical RCT (or extraction). Incising a sinus tract alone is a close acute-care near-miss that may help drainage temporarily but does not eliminate intracanal infection. Antibiotics alone or pulp capping necrotic tissue are incorrect.',
     'choice_explanations': {'A': 'Systemic antibiotics do not substitute for intracanal disinfection.', 'B': 'Pulp capping targets vital pulp scenarios, not necrotic infected canals.', 'C': 'Near-miss: soft-tissue drainage can help acute swelling, but definitive care is RCT/extraction of the source tooth.', 'D': 'Necrotic infected canals need RCT (or extraction) plus restoration—not antibiotics or pulp caps alone.'}
    },
        {
     'question': 'During instrumentation of a curved mesial canal, a ledge forms and the file no longer reaches prior working length. What is the most appropriate applied next concept?',
     'options': ['A) Re-establish glide path carefully with small flexible files; avoid forcing large stiff instruments that worsen the ledge', 'B) Bypass by immediately forcing a large stiff hand file to full working length past the ledge', 'C) Obturate short of the ledge without attempting to regain patency whenever apical infection remains', 'D) Flood the canal with undiluted eugenol as the sole corrective step'],
     'answer': 'A) Re-establish glide path carefully with small flexible files; avoid forcing large stiff instruments that worsen the ledge',
     'explanation': 'Ledge recovery uses small precurved flexible files and patience. Forcing a large stiff file to length is the overlapping aggressive near-miss that risks perforation/transport. Leaving untreated apical infection or using eugenol alone is wrong.',
     'choice_explanations': {'A': 'Regain the pathway with small flexible files; do not force large instruments that create perforations.', 'B': 'Near-miss: bypass is the goal, but forcing large stiff instruments deepens transportation/perforation risk.', 'C': 'Leaving infected apical canal untreated is not preferred when safe bypass is possible.', 'D': 'Eugenol does not correct a mechanical ledge.'}
    },
        {
     'question': 'A previously treated tooth has persistent apical radiolucency, inadequate obturation density, and missed second mesiobuccal canal suspected on CBCT. Which applied retreatment concept fits?',
     'options': ['A) Apical surgery first without considering orthograde retreatment of missed anatomy', 'B) Nonsurgical retreatment to remove old obturation, locate missed anatomy, disinfect, and re-obturate', 'C) Place a post and crown without addressing intracanal infection', 'D) Prescribe antifungals as definitive endodontic retreatment'],
     'answer': 'B) Nonsurgical retreatment to remove old obturation, locate missed anatomy, disinfect, and re-obturate',
     'explanation': 'Persistent disease with missed MB2 favors nonsurgical retreatment first when feasible. Apical surgery first is the overlapping advanced near-miss—surgery is considered if orthograde retreatment is infeasible. Crowning over infection or antifungal-only care is wrong.',
     'choice_explanations': {'A': 'Near-miss: apical surgery can be appropriate later, but missed canal anatomy is preferably addressed with nonsurgical retreatment first when feasible.', 'B': 'Failed RCT with missed anatomy warrants nonsurgical retreatment to disinfect the full canal system.', 'C': 'Restoring without infection control seals in bacteria.', 'D': 'Endodontic failure is primarily bacterial, not treated by antifungals alone.'}
    },
   ],
   'hard': [
        {
     'question': 'A 45-year-old has severe lingering cold pain on a maxillary first molar, referred pain to the ear, hypersensitive MB cusp, and a recent deep composite near the pulp horn. Cold test lingers 20 seconds on that tooth only; percussion is mild. Which diagnosis and first definitive therapy align?',
     'options': ['A) Reversible pulpitis—desensitizing measures and monitor without definitive pulp therapy', 'B) Symptomatic apical periodontitis—incise the palate as sole therapy', 'C) Symptomatic irreversible pulpitis—initiate root canal treatment (or extraction if unrestorable) after profound anesthesia', 'D) Myofascial pain—occlusal splint only without pulp testing correlation'],
     'answer': 'C) Symptomatic irreversible pulpitis—initiate root canal treatment (or extraction if unrestorable) after profound anesthesia',
     'explanation': 'Lingering cold localized to one tooth after deep restoration indicates symptomatic irreversible pulpitis; RCT/extraction is definitive. Reversible pulpitis is the classic overlapping diagnostic near-miss but lacks lingering pain. Palatal incision or myofascial-only care ignores the tooth-specific thermal findings.',
     'choice_explanations': {'A': 'Near-miss: reversible pulpitis causes brief sensitivity; lingering spontaneous/thermal pain indicates irreversible pulpitis.', 'B': 'No fluctuant abscess is described; mild percussion can coexist with irreversible pulpitis, but palate incision alone is not care.', 'C': 'Lingering localized cold pain after deep restoration = irreversible pulpitis → RCT/extraction.', 'D': 'A tooth-specific lingering cold test contradicts a purely myofascial diagnosis.'}
    },
        {
     'question': 'Mid-RCT on a mandibular molar, the patient suddenly tastes bleach, the cheek swells, and severe pain occurs after irrigant expression. Which multi-cue complication plan is correct?',
     'options': ['A) Continue irrigation with sterile saline under positive apical pressure to neutralize tissues beyond the apex', 'B) Ignore swelling because hypochlorite is harmless once diluted by tissue fluid', 'C) Perform immediate hemimandibulectomy as first-line care', 'D) Recognize NaOCl extrusion accident: stop irrigation, aspirate, cold compresses early, analgesia, follow-up, and complete RCT later when acute phase allows'],
     'answer': 'D) Recognize NaOCl extrusion accident: stop irrigation, aspirate, cold compresses early, analgesia, follow-up, and complete RCT later when acute phase allows',
     'explanation': 'NaOCl accidents need cessation of irrigant extrusion, supportive care, and delayed careful completion. Continuing any positive-pressure irrigation apically—even saline—is a close technique near-miss during the acute chemical injury phase. Denial or radical resection is wrong.',
     'choice_explanations': {'A': 'Near-miss: saline may be used carefully later to dilute residual irrigant in the canal, but continued forceful apical-positive irrigation worsens soft-tissue injury.', 'B': 'Extracanal NaOCl causes significant tissue damage and must not be ignored.', 'C': 'Hemimandibulectomy is not treatment for an irrigant accident.', 'D': 'Stop irrigation, support the patient, and complete RCT carefully after the acute phase.'}
    },
        {
     'question': 'A cracked tooth has pain on release of biting, occasional cold sensitivity, a visible fracture line staining with dye, and no deep probing defect. Radiograph is normal. Which multi-cue management direction is best?',
     'options': ['A) Confirm crack with transillumination/bite testing, remove diseased tissue, and provide cuspal coverage if the tooth is restorable and pulp status allows', 'B) Stabilize with a bonded direct restoration without cuspal coverage and reassess only if pain worsens', 'C) Extract immediately every tooth with any enamel craze line', 'D) Treat with topical fluoride varnish as definitive crack therapy'],
     'answer': 'A) Confirm crack with transillumination/bite testing, remove diseased tissue, and provide cuspal coverage if the tooth is restorable and pulp status allows',
     'explanation': 'Cracked tooth syndrome with pain on release needs diagnosis and usually cuspal coverage when restorable. A bonded direct fill without coverage is the overlapping under-protection near-miss that allows crack propagation. Extracting all craze lines or fluoride alone is wrong.',
     'choice_explanations': {'A': 'Restorable cracks need diagnosis, removal of pathology, and cuspal coverage when indicated.', 'B': 'Near-miss: bonding can help briefly, but unprotected cusps commonly allow crack propagation under load.', 'C': 'Enamel craze lines are common and not automatic extraction criteria.', 'D': 'Fluoride does not stabilize a structural crack.'}
    },
   ],
   'extreme': [
        {
     'question': 'A maxillary lateral incisor has failed twice after RCT, a persistent sinus tract, and CBCT showing a missed lateral canal and apical transportation. The tooth has a short post and adequate ferrule. The patient wants to keep the tooth. Which complex decision is most appropriate?',
     'options': ['A) Proceed directly to apical surgery without attempting orthograde retreatment of accessible missed anatomy', 'B) Attempt thorough nonsurgical retreatment with magnification to address missed anatomy if feasible; if not, consider apical surgery after infection control counseling, versus extraction/implant if prognosis poor', 'C) Cure the sinus tract with topical steroids alone indefinitely', 'D) Guarantee success with antibiotics for 12 months without canal revision'],
     'answer': 'B) Attempt thorough nonsurgical retreatment with magnification to address missed anatomy if feasible; if not, consider apical surgery after infection control counseling, versus extraction/implant if prognosis poor',
     'explanation': 'Persistent disease with missed lateral canal favors magnified nonsurgical retreatment when the post/ferrule allow access; apical surgery is the overlapping alternative if orthograde revision is infeasible. Steroids or long-term antibiotics without source control are wrong.',
     'choice_explanations': {'A': 'Near-miss: apical surgery is appropriate when orthograde retreatment cannot address anatomy, but accessible missed canals should be retreated nonsurgically first when feasible.', 'B': 'Retreatment under magnification ± later surgery, with extraction if prognosis remains poor.', 'C': 'Sinus tracts resolve only when infection is controlled.', 'D': 'Antibiotics cannot replace intracanal or surgical source control.'}
    },
        {
     'question': 'An immature permanent central incisor suffered intrusion trauma 8 weeks ago. The tooth is asymptomatic, radiograph shows early periapical change, pulp tests are negative, and apex is wide open. Which regenerative/apexification decision framework fits best?',
     'options': ['A) Perform immediate conventional RCT to the radiographic apex with dense gutta-percha in the wide-open immature canal as the only option', 'B) Assume vitality forever because the tooth is asymptomatic at one visit', 'C) Confirm pulp necrosis, then choose apexification (e.g., bioceramic barrier) or regenerative endodontic procedures based on protocols, stage of root development, and informed consent', 'D) Extract and place a malposed implant before skeletal growth completion routinely'],
     'answer': 'C) Confirm pulp necrosis, then choose apexification (e.g., bioceramic barrier) or regenerative endodontic procedures based on protocols, stage of root development, and informed consent',
     'explanation': 'Necrotic immature teeth need apexification or regenerative endodontics, not conventional mature-apex obturation alone. Conventional RCT to the apex in a blunderbuss canal is the overlapping technical near-miss that lacks an apical barrier/regenerative strategy. Assuming vitality or placing a growing-child implant is wrong.',
     'choice_explanations': {'A': 'Near-miss: mature-style gutta-percha fills are unsuitable as the sole approach in a wide-open apex without apexification/regenerative protocol.', 'B': 'Negative tests plus radiographic change indicate necrosis despite quiet symptoms.', 'C': 'Necrotic immature incisors need apexification or regenerative endodontics with consent.', 'D': 'Implants before growth completion risk infraocclusion.'}
    },
        {
     'question': 'During retreatment, a separated NiTi fragment lodges in the apical third of a curved MB canal of a strategic molar abutment. The tooth is symptomatic with apical radiolucency. Retrieval attempts begin to remove excessive dentin. What is the best complication-management judgment?',
     'options': ['A) Continue removing dentin indefinitely until the fragment is retrieved at any structural cost', 'B) Leave symptomatic apical disease without any disinfection attempt around/bypass the fragment', 'C) Tell the patient separated instruments always require immediate extraction', 'D) Balance retrieval versus bypass versus surgical options against remaining dentin thickness; stop when further chasing risks perforation/fracture, and discuss prognosis honestly'],
     'answer': 'D) Balance retrieval versus bypass versus surgical options against remaining dentin thickness; stop when further chasing risks perforation/fracture, and discuss prognosis honestly',
     'explanation': 'Separated apical fragments require risk–benefit judgment among retrieval, bypass, and surgery. Unlimited retrieval chasing is the overlapping aggressive near-miss that risks root destruction. Ignoring infection or mandatory extraction are wrong extremes.',
     'choice_explanations': {'A': 'Near-miss: retrieval is desirable, but unlimited dentin removal risks vertical root fracture and tooth loss.', 'B': 'Symptomatic apical periodontitis still requires a disinfection strategy around the obstacle.', 'C': 'Many separated-instrument cases remain restorable without extraction.', 'D': 'Judge retrieve vs bypass vs surgery against remaining dentin; counsel prognosis honestly.'}
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
     'options': ['A) A band of sound tooth structure encircling the preparation that resists fracture under crown leverage', 'B) A post-and-core complex that replaces missing coronal tooth structure inside the canal', 'C) The shade tab selected for porcelain matching only', 'D) The brand of temporary cement used during provisionalization'],
     'answer': 'A) A band of sound tooth structure encircling the preparation that resists fracture under crown leverage',
     'explanation': 'Ferrule is a circumferential collar of remaining axial tooth structure engaged by the crown. A post-and-core is the overlapping restorative near-miss that may rebuild the core but does not itself define ferrule. Shade and temporary cement are unrelated definitions.',
     'choice_explanations': {'A': 'Ferrule = circumferential sound tooth structure under the crown that resists fracture.', 'B': 'Near-miss: posts/cores replace missing structure, but ferrule specifically means remaining axial tooth structure encircling the preparation.', 'C': 'Shade selection is esthetic, not the ferrule definition.', 'D': 'Temporary cement brand is unrelated to ferrule anatomy.'}
    },
        {
     'question': 'What is the primary purpose of border molding when fabricating a complete denture impression?',
     'options': ['A) Capture the posterior palatal seal area alone without vestibular functional borders', 'B) Record the functional depth and width of the vestibule for a peripheral seal', 'C) Determine the patient’s freeway space and OVD in the same step', 'D) Select tooth shade for the anterior denture teeth'],
     'answer': 'B) Record the functional depth and width of the vestibule for a peripheral seal',
     'explanation': 'Border molding shapes impression peripheries to physiologic vestibules for peripheral seal. Posterior palatal seal is a related complete-denture retention concept (near-miss) but is not what border molding primarily records. Freeway space/OVD and shade are separate records.',
     'choice_explanations': {'A': 'Near-miss: posterior palatal seal aids maxillary retention but border molding specifically records functional vestibular borders.', 'B': 'Border molding captures functional vestibular borders for denture peripheral seal/retention.', 'C': 'Freeway space/OVD are established separately from border molding.', 'D': 'Shade selection is not accomplished by border molding.'}
    },
        {
     'question': 'In fixed prosthodontics, a key biologic reason to respect biologic width (supracrestal tissue attachment) is to avoid which outcome?',
     'options': ['A) Transient gingival blanching from a well-placed equigingival margin', 'B) Improved papillary fill from intentional deep margin placement within bone', 'C) Chronic inflammation and bone loss from restoration margins invading the attachment apparatus', 'D) Elimination of the need for oral hygiene around crowned teeth'],
     'answer': 'C) Chronic inflammation and bone loss from restoration margins invading the attachment apparatus',
     'explanation': 'Invading biologic width/supracrestal attachment causes chronic inflammation and bone loss. Mild blanching from careful equigingival margins is a close clinical near-miss that is not the harmful outcome of true attachment invasion. Deep bony margins and hygiene elimination are wrong concepts.',
     'choice_explanations': {'A': 'Near-miss: brief blanching can occur with retraction/margin placement, but biologic-width invasion causes persistent inflammation and bone loss.', 'B': 'Intentional invasion into attachment/bone harms periodontal health rather than improving it.', 'C': 'Margins invading the attachment apparatus provoke peri-restoration inflammation and bone loss.', 'D': 'Hygiene remains mandatory regardless of margin design.'}
    },
   ],
   'medium': [
        {
     'question': 'A patient will receive an RPD replacing several posterior teeth. Which applied design principle best protects abutment teeth?',
     'options': ['A) Rely on soft-tissue support alone with clasp retention and no planned rest seats', 'B) Use clasps that engage undercuts without reciprocal bracing arms', 'C) Omit guide planes so the path of insertion remains unrestricted', 'D) Provide adequate rest seats so occlusal loads are directed along the long axis and bases are properly supported'],
     'answer': 'D) Provide adequate rest seats so occlusal loads are directed along the long axis and bases are properly supported',
     'explanation': 'Rests transmit occlusal force axially and prevent tissue-borne settling that torques abutments. Soft-tissue-only support with clasps is the overlapping dangerous near-miss design. Unreciprocated clasps or omitted guide planes also harm abutments but rests are the key protective principle asked.',
     'choice_explanations': {'A': 'Near-miss: tissue-borne RPDs without rests settle and lever abutments—rests are essential protective elements.', 'B': 'Unreciprocated clasps can torque abutments during insertion/function.', 'C': 'Guide planes help control path of insertion and bracing.', 'D': 'Rests and supportive design direct RPD loads axially and spare abutments from torque.'}
    },
        {
     'question': 'When selecting occlusal vertical dimension for a complete denture wearer with worn dentition history, which applied approach is sound?',
     'options': ['A) Combine clinical rest position, speech (sibilant), esthetics, and residual ridge comfort rather than a single arbitrary number', 'B) Set OVD solely from the interocclusal rest space measured at one visit without phonetic or esthetic verification', 'C) Always open OVD by 10 mm regardless of rest space', 'D) Set OVD solely by the shade of the pink acrylic'],
     'answer': 'A) Combine clinical rest position, speech (sibilant), esthetics, and residual ridge comfort rather than a single arbitrary number',
     'explanation': 'OVD uses multiple correlates—rest space, phonetics, esthetics, and comfort. Using rest space alone without verification is the overlapping incomplete near-miss. Arbitrary large openings or acrylic shade are incorrect.',
     'choice_explanations': {'A': 'OVD is verified by rest space, phonetics, esthetics, and comfort together.', 'B': 'Near-miss: rest space is useful but should not be the sole determinant without phonetic/esthetic confirmation.', 'C': 'Blind 10 mm opening often exceeds freeway space and destabilizes dentures.', 'D': 'Acrylic shade does not encode vertical dimension.'}
    },
        {
     'question': 'A survey crown is planned for an RPD abutment. Which applied feature must be incorporated into the crown contour?',
     'options': ['A) Idealized anatomic contours without reference to a surveyor or planned path of insertion', 'B) Surveyed guide planes, rest seats, and appropriate undercut for the chosen clasp assembly', 'C) Elimination of all axial walls to soft tissue only', 'D) Occlusal anatomy copied from a deciduous molar only'],
     'answer': 'B) Surveyed guide planes, rest seats, and appropriate undercut for the chosen clasp assembly',
     'explanation': 'Survey crowns must provide planned guide planes, rests, and clasp undercuts. Natural-looking unsuveyed contours are the overlapping esthetic near-miss that can defeat RPD path and clasping. Soft-tissue-only abutments or primary molar anatomy are inappropriate.',
     'choice_explanations': {'A': 'Near-miss: anatomic contours matter esthetically, but without surveying they may lack guide planes, rests, and controlled undercuts.', 'B': 'Survey crowns must include designed guide planes, rests, and clasp undercuts.', 'C': 'Eliminating axial tooth structure destroys the abutment.', 'D': 'Primary molar anatomy is not the design template for adult survey crowns.'}
    },
   ],
   'hard': [
        {
     'question': 'A mandibular Kennedy Class I RPD candidate has distal extension ridges, periodontally reduced canines as abutments, and a history of prior denture sore spots. Which multi-cue design emphasis is most appropriate?',
     'options': ['A) Make the denture entirely tooth-borne on the canines with rigid bilateral distal occlusal loading only', 'B) Convert to a purely tissue-borne interim acrylic without rests or designed stress distribution', 'C) Maximize support from the edentulous ridge (accurate base adaptation/impression technique), use flexible stress distribution concepts, and protect weakened abutments', 'D) Use a maxillary complete denture design on the mandible unchanged'],
     'answer': 'C) Maximize support from the edentulous ridge (accurate base adaptation/impression technique), use flexible stress distribution concepts, and protect weakened abutments',
     'explanation': 'Kennedy I distal extensions need ridge support and abutment-protective stress distribution. Rigid tooth-only distal loading on weak canines is the overlapping biomechanical near-miss. Pure tissue-borne acrylic without design and copying maxillary CD design unchanged are wrong.',
     'choice_explanations': {'A': 'Near-miss: tooth support is desirable, but rigid distal loading solely on weakened canines overloads them; ridge share and stress distribution are required.', 'B': 'Undesigned tissue-borne acrylic lacks controlled rests/occlusion for definitive Kennedy I management.', 'C': 'Class I distal extensions need ridge support and abutment-protective stress distribution.', 'D': 'Maxillary complete-denture design principles do not transplant unchanged to a mandibular RPD.'}
    },
        {
     'question': 'An anterior single implant crown shows screw loosening twice, occlusal contacts heavier in excursive movements than adjacent teeth, and a shallow anterior guidance scheme. Which multi-cue correction is best?',
     'options': ['A) Increase centric contact density on the implant to improve perceived stability', 'B) Replace the screw with a larger-diameter screw without correcting excursive overload', 'C) Cement a crown over a loose screw without retrieving and retorquing', 'D) Correct occlusal scheme to lighten implant excursive contacts, ensure proper torque/preload, and reassess abutment fit before repeated failure'],
     'answer': 'D) Correct occlusal scheme to lighten implant excursive contacts, ensure proper torque/preload, and reassess abutment fit before repeated failure',
     'explanation': 'Implant screw loosening commonly reflects excursive overload and inadequate preload. Upsizing the screw without occlusal correction is a mechanical near-miss. Adding centric overload or cementing over a loose screw is wrong.',
     'choice_explanations': {'A': 'Heavier implant contacts increase overload risk rather than stabilizing the screw joint.', 'B': 'Near-miss: component replacement may be needed, but without correcting excursive overload, loosening recurs.', 'C': 'Cementing over a loose screw fails to restore preload and fit.', 'D': 'Lighten excursive contacts, verify fit, and apply correct torque/preload.'}
    },
        {
     'question': 'A patient with a high smile line needs a maxillary central crown. Preparation reveals a dark subgingival ferrule, thin biotype, and the patient refuses surgery. Which multi-cue prosthetic strategy is most coherent?',
     'options': ['A) Use opaque/masking strategies or material layering carefully, discuss gingival display limits, and consider conservative margin placement without violating biologic width', 'B) Place a metal-ceramic crown with deep subgingival margin to hide the dark substrate without biologic-width counseling', 'C) Promise perfect pink esthetics identical to virgin teeth without material limits', 'D) Attempt to bleach a metal post through opaque porcelain using peroxide trays alone'],
     'answer': 'A) Use opaque/masking strategies or material layering carefully, discuss gingival display limits, and consider conservative margin placement without violating biologic width',
     'explanation': 'Dark substrates and thin biotypes need masking strategies and realistic consent within biologic width. Deep subgingival metal-ceramic hide-the-margin tactics are the overlapping esthetic near-miss that risk attachment violation. Overpromising or bleaching through metal is wrong.',
     'choice_explanations': {'A': 'Mask dark substrates within biologic-width limits and set realistic high-smile-line expectations.', 'B': 'Near-miss: subgingival metal-ceramics are sometimes used for masking, but deep placement without biologic-width respect risks chronic inflammation.', 'C': 'Material physics and soft tissue set limits; overpromising harms consent quality.', 'D': 'Peroxide trays do not reliably mask metal show-through under ceramics.'}
    },
   ],
   'extreme': [
        {
     'question': "A completely edentulous patient with severely resorbed mandible, history of denture instability, and xerostomia from polypharmacy requests 'teeth in a day' fixed full-arch implants. CBCT shows limited anterior bone and proximity of the inferior alveolar nerves bilaterally. Which decision pathway is most responsible?",
     'options': ['A) Proceed with immediate fixed full-arch tilted implants despite inadequate bone and unaddressed xerostomia, promising same-day teeth', 'B) Explain anatomic limits, discuss implant-retained overdenture versus extensive grafting/alternative tilt strategies with realistic timelines, optimize saliva/prosthetic soft-tissue health, and avoid promising immediate fixed teeth when bone and soft tissue are inadequate', 'C) Place posterior implants into the mandibular canals to gain AP spread at any neurologic cost', 'D) Ignore xerostomia because saliva never affects denture or peri-implant comfort'],
     'answer': 'B) Explain anatomic limits, discuss implant-retained overdenture versus extensive grafting/alternative tilt strategies with realistic timelines, optimize saliva/prosthetic soft-tissue health, and avoid promising immediate fixed teeth when bone and soft tissue are inadequate',
     'explanation': 'Severely resorbed mandibles and xerostomia constrain immediate fixed full-arch promises; discuss overdenture vs grafting/tilt options with realistic timelines. Immediate tilted fixed full-arch despite inadequate tissue is the overlapping treatment near-miss. Canal penetration or ignoring xerostomia is wrong.',
     'choice_explanations': {'A': 'Near-miss: tilted immediate fixed concepts can help selected cases, but not when bone/soft tissue and xerostomia make promises unsafe.', 'B': 'Explain limits; consider overdenture vs staged/grafted/tilted options; optimize saliva; avoid unjustified same-day fixed guarantees.', 'C': 'Implants in the IAN canal risk permanent neurosensory injury.', 'D': 'Hyposalivation strongly affects prosthesis comfort and mucosal health.'}
    },
        {
     'question': 'An FPD from canine to second molar failed after the canine abutment split vertically. The premolars are missing; the molar has short clinical crown and short roots. The patient wants another five-unit bridge immediately. What complex prosthetic judgment is best?',
     'options': ['A) Recement the split canine fragments under a new longer cantilever bridge without addressing structure', 'B) Replace with another five-unit tooth-borne FPD using the short-rooted molar and a hopeless canine abutment', 'C) Recognize long-span FPD with poor abutments as high failure risk; consider implant replacement of missing units or removable options after extracting the fractured canine and evaluating the molar’s true abutment value', 'D) Promise that any span length is equally successful if porcelain is layered thickly'],
     'answer': 'C) Recognize long-span FPD with poor abutments as high failure risk; consider implant replacement of missing units or removable options after extracting the fractured canine and evaluating the molar’s true abutment value',
     'explanation': 'A vertically fractured canine and poor molar abutments make repeating a long-span FPD high risk. Remaking a similar five-unit bridge is the overlapping prosthetic near-miss. Recementing split roots or claiming porcelain overcomes span physics is wrong.',
     'choice_explanations': {'A': 'Split roots cannot be reliably recombined as abutments under load.', 'B': 'Near-miss: another tooth-borne long-span FPD repeats the failed biomechanics on inadequate abutments.', 'C': 'Failed long-span FPD with fractured abutment needs redesign (implants/RPD), not another overloaded bridge.', 'D': 'Porcelain thickness does not compensate for inadequate abutment support.'}
    },
        {
     'question': 'A maxillary complete denture opposes a Kennedy Class I RPD. The patient develops combination syndrome features: flabby anterior maxilla, papillary hyperplasia, mandibular posterior ridge resorption, and overgrown tuberosities. Which complication-management plan is most coherent?',
     'options': ['A) Add more anterior maxillary occlusal contact exclusively to stabilize the denture', 'B) Reline the maxillary denture with a soft liner only and leave mandibular posterior support uncorrected', 'C) Extract the mandibular residual ridge prophylactically to match the maxilla', 'D) Correct occlusal plane/posterior support, consider surgical management of hyperplasia/flabby tissue as needed, reline or remake prostheses, and educate about leaving dentures out at night'],
     'answer': 'D) Correct occlusal plane/posterior support, consider surgical management of hyperplasia/flabby tissue as needed, reline or remake prostheses, and educate about leaving dentures out at night',
     'explanation': 'Combination syndrome needs restored mandibular posterior support and soft-tissue/prosthesis correction. Soft-liner-only maxillary reline without posterior support correction is the overlapping incomplete near-miss. Increasing anterior contacts or resecting ridges is wrong.',
     'choice_explanations': {'A': 'Anterior-only contacts drive further maxillary flabby change and bone loss.', 'B': 'Near-miss: soft liners may comfort flabby tissue temporarily but do not correct missing mandibular posterior support driving combination syndrome.', 'C': 'Resecting mandibular ridges destroys support needed for the RPD.', 'D': 'Restore posterior support and manage hyperplastic/flabby tissues; remake/reline and give night-out instructions.'}
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
     'options': ['A) Mandibular first permanent molar', 'B) Mandibular central permanent incisor, which often erupts near the same period but is not usually first', 'C) Mandibular permanent third molar', 'D) Maxillary permanent canine'],
     'answer': 'A) Mandibular first permanent molar',
     'explanation': 'The mandibular first permanent molar typically erupts around age 6 and is usually the first permanent tooth. Mandibular central incisors erupt close in time and are the classic overlapping sequence near-miss, but first molars most often precede. Canines and third molars erupt much later.',
     'choice_explanations': {'A': 'Mandibular first permanent molars usually erupt first among permanent teeth (~age 6).', 'B': 'Near-miss: mandibular permanent centrals erupt early in the mixed dentition but typically after or not before the first permanent molars as the usual first permanent tooth.', 'C': 'Third molars erupt in late adolescence/early adulthood.', 'D': 'Permanent canines erupt later in the mixed dentition sequence.'}
    },
        {
     'question': 'A primary molar with a deep carious lesion is asymptomatic, has a healthy permanent successor, and more than a year before exfoliation. When pulp is exposed but vital and inflammation is limited to the coronal pulp, which therapy is most appropriate?',
     'options': ['A) Indirect pulp treatment leaving a thin layer of affected dentin without coronal pulp removal when exposure has already occurred', 'B) Pulpotomy with suitable medicament and a sealed restoration', 'C) Adult-length cast post and core as first-line', 'D) No restoration after leaving carious exposure open to saliva'],
     'answer': 'B) Pulpotomy with suitable medicament and a sealed restoration',
     'explanation': 'Vital primary molar with limited coronal pulp inflammation and exposure is typically treated with pulpotomy plus sealed restoration. Indirect pulp treatment is a close vital-pulp near-miss used when exposure is avoided; once exposure with coronal inflammation is present, pulpotomy is preferred. Adult posts or open exposures are wrong.',
     'choice_explanations': {'A': 'Near-miss: IPT is valuable for deep caries without exposure; here exposure with coronal pulp inflammation fits pulpotomy.', 'B': 'Vital primary molar with coronal pulp inflammation often receives pulpotomy plus sealed restoration.', 'C': 'Cast posts are unsuitable as primary pulp therapy.', 'D': 'Leaving exposures open risks pulp necrosis and infection.'}
    },
        {
     'question': 'Topical fluoride varnish is used in children primarily to achieve which effect?',
     'options': ['A) Replace dietary counseling and oral hygiene instruction entirely', 'B) Provide definitive arrest of all cavitated dentin lesions without restoration', 'C) Promote remineralization and reduce caries incidence/progression on enamel', 'D) Anesthetize the inferior alveolar nerve for extractions'],
     'answer': 'C) Promote remineralization and reduce caries incidence/progression on enamel',
     'explanation': 'Fluoride varnish favors remineralization and caries prevention. Expecting varnish alone to arrest all cavitated dentin lesions without restorative care is the overlapping prevention near-miss. It does not replace diet/hygiene advice or provide anesthesia.',
     'choice_explanations': {'A': 'Diet and hygiene counseling remain essential alongside fluoride.', 'B': 'Near-miss: varnish aids prevention/remineralization; cavitated dentin lesions still often need restorative/caries-management decisions.', 'C': 'Fluoride varnish aids enamel remineralization and caries prevention.', 'D': 'Local anesthetics—not fluoride—provide nerve block anesthesia.'}
    },
   ],
   'medium': [
        {
     'question': 'A 4-year-old sustains lateral luxation of a primary maxillary incisor with occlusal interference. The permanent successor bud is not apparently intruded on radiograph. Which applied management is most appropriate?',
     'options': ['A) Rigidly splint the primary incisor for 4 months using permanent-tooth avulsion protocols', 'B) Always leave interfering luxated primary teeth untreated regardless of bite trauma', 'C) Place an implant immediately in the 4-year-old socket', 'D) Reposition if needed for function/esthetics or extract if the tooth poses aspiration risk or interferes severely; avoid rigid prolonged immobilization typical of some permanent-tooth protocols'],
     'answer': 'D) Reposition if needed for function/esthetics or extract if the tooth poses aspiration risk or interferes severely; avoid rigid prolonged immobilization typical of some permanent-tooth protocols',
     'explanation': 'Primary luxation prioritizes the successor and airway safety; reposition or extract if interfering. Applying long rigid permanent-tooth splinting protocols is the overlapping trauma near-miss. Observation of interfering teeth, or implants, is wrong.',
     'choice_explanations': {'A': 'Near-miss: splinting concepts exist in trauma care, but prolonged rigid permanent-tooth protocols are inappropriate for most primary luxations.', 'B': 'Occlusal interference can traumatize tissues and needs management.', 'C': 'Implants are contraindicated in growing preschool children for such injuries.', 'D': 'Primary luxation: careful reposition or extract if interfering/unsafe; avoid adult-style prolonged rigid immobilization.'}
    },
        {
     'question': 'Space maintenance after early loss of a primary second molar is most critical to prevent which applied consequence?',
     'options': ['A) Mesial drift of the first permanent molar with loss of leeway/arch space', 'B) Distal drift of the primary first molar only without permanent molar involvement', 'C) Mandatory agenesis of the permanent successor', 'D) Spontaneous formation of a new primary tooth'],
     'answer': 'A) Mesial drift of the first permanent molar with loss of leeway/arch space',
     'explanation': 'Early loss of primary second molars allows first permanent molars to drift mesially, consuming premolar space. Focusing only on primary first molar distal movement is an incomplete space near-miss. Agenesis or regenerating a primary tooth is wrong.',
     'choice_explanations': {'A': 'Space maintainers prevent mesial molar drift and space loss after early primary second molar loss.', 'B': 'Near-miss: adjacent primary teeth may shift, but the critical consequence is mesial drift of the first permanent molar with arch-space loss.', 'C': 'Successor agenesis is genetic/developmental, not caused by space loss alone.', 'D': 'Humans do not regenerate a new primary tooth after loss.'}
    },
        {
     'question': 'A child with early childhood caries needs multiple extractions under general anesthesia. Which applied preoperative principle is essential?',
     'options': ['A) Feed a large meal immediately before induction to keep energy up', 'B) Medical history/NPO status review, informed consent including risks, and a comprehensive restorative/extraction plan to minimize repeat anesthesia', 'C) Obtain parental consent but intentionally treat only one quadrant to ensure multiple future GA visits', 'D) Skip medical history review because dental caries is never related to systemic disease'],
     'answer': 'B) Medical history/NPO status review, informed consent including risks, and a comprehensive restorative/extraction plan to minimize repeat anesthesia',
     'explanation': 'Pediatric GA dentistry needs medical/NPO review, consent, and comprehensive single-session planning. Planning fragmented GA visits is the overlapping inefficient near-miss that increases anesthetic exposure. Feeding before induction or skipping medical history is unsafe.',
     'choice_explanations': {'A': 'Pre-induction feeding violates NPO and risks aspiration.', 'B': 'Pediatric dental GA needs NPO/medical clearance, consent, and comprehensive single-session planning.', 'C': 'Near-miss: consent is necessary, but intentionally fragmenting care into many GA visits increases anesthetic risk.', 'D': 'Medical history is essential; systemic conditions and medications affect GA and dental risk.'}
    },
   ],
   'hard': [
        {
     'question': 'An 8-year-old has an avulsed permanent central incisor with 45 minutes dry extraoral time, an open apex, and the tooth brought in milk after an initial dry period. Which multi-cue replantation decision is best?',
     'options': ['A) Scrub the root vigorously with antiseptic and delay replantation until the next day', 'B) Discard the permanent incisor because open-apex teeth never reattach', 'C) Replant after gentle cleaning as indicated, flexible splint, pulp management strategy for open apex (often revascularization attempt vs endodontics timing per guidelines), and tetanus/antibiotics consideration per protocol', 'D) Replant and perform immediate complete root resection to the CEJ'],
     'answer': 'C) Replant after gentle cleaning as indicated, flexible splint, pulp management strategy for open apex (often revascularization attempt vs endodontics timing per guidelines), and tetanus/antibiotics consideration per protocol',
     'explanation': 'Avulsed permanent teeth should be replanted promptly with flexible splinting and staged pulp care, especially with open apex. Delaying after harsh scrubbing is a trauma-protocol near-miss that kills PDL cells. Discarding open-apex teeth or resecting to CEJ is wrong.',
     'choice_explanations': {'A': 'Near-miss: cleaning matters, but vigorous scrubbing and overnight delay destroy PDL prognosis.', 'B': 'Open-apex teeth can reattach and sometimes revascularize; they should not be discarded routinely.', 'C': 'Replant, flexible splint, and stage pulp care per open-apex biology and IADT-aligned protocols.', 'D': 'Resection to CEJ destroys the tooth rather than managing avulsion.'}
    },
        {
     'question': 'A 6-year-old with a deep carious primary second molar shows furcation radiolucency, mobility, and night pain. The permanent premolar is present. Which multi-cue therapy is most appropriate?',
     'options': ['A) Attempt pulpectomy and stainless-steel crown despite furcation radiolucency, mobility, and night pain', 'B) Perform adult molar uprighting with heavy orthodontic forces immediately', 'C) Ignore infection because primary teeth cannot affect permanent successors', 'D) Extract the primary molar and place a space maintainer if the successor will not erupt imminently'],
     'answer': 'D) Extract the primary molar and place a space maintainer if the successor will not erupt imminently',
     'explanation': 'Furcation involvement, mobility, and night pain exceed vital/nonvital pulp-therapy criteria for saving many primary molars—extraction ± space maintenance is indicated. Pulpectomy/SSC despite these findings is the overlapping heroic near-miss when infection is advanced. Ortho uprighting or ignoring successor risk is wrong.',
     'choice_explanations': {'A': 'Near-miss: pulpectomy/SSC can save some primary molars, but furcation pathosis with mobility and night pain usually indicates extraction.', 'B': 'Heavy adult ortho forces are not the acute infection treatment.', 'C': 'Primary molar infection can damage developing premolar follicles.', 'D': 'Infected nonrestorable primary molar with furcation disease → extract ± space maintainer.'}
    },
        {
     'question': 'A child with special healthcare needs has moderate caries, limited cooperative ability, and takes medication causing xerostomia. Behavioral attempts fail for quadrant dentistry. Which multi-cue plan is most appropriate?',
     'options': ['A) Use medical consultation as needed, consider sedation/GA pathways with caries-risk control (fluoride, diet, saliva substitutes), and prioritize infection control', 'B) Attempt lengthy quadrant dentistry with protective stabilization alone after failed basic behavior guidance, without considering sedation/GA alternatives', 'C) Withhold all fluoride because special needs children never get caries', 'D) Assume xerostomia medications are irrelevant to caries risk'],
     'answer': 'A) Use medical consultation as needed, consider sedation/GA pathways with caries-risk control (fluoride, diet, saliva substitutes), and prioritize infection control',
     'explanation': 'SHCN children often need advanced behavior guidance/sedation/GA plus aggressive prevention. Persisting with restraint-only lengthy care after failed basic guidance is the overlapping behavior near-miss. Withholding fluoride or ignoring xerostomia is wrong.',
     'choice_explanations': {'A': 'SHCN dentistry combines prevention, medical coordination, and appropriate sedation/GA pathways.', 'B': 'Near-miss: protective stabilization has a role, but after failed basic guidance and for extensive care, sedation/GA planning is often more appropriate.', 'C': 'SHCN populations often have higher caries risk; fluoride is important.', 'D': 'Xerostomia markedly elevates caries risk and needs management.'}
    },
   ],
   'extreme': [
        {
     'question': 'A 9-year-old with hemophilia A (moderate factor VIII deficiency) needs extraction of an abscessed primary molar. The child is otherwise stable; local swelling is mild. Which complex perioperative decision is best?',
     'options': ['A) Extract in office with local hemostatic packing only, postponing hematology contact until after bleeding occurs', 'B) Coordinate with hematology for factor replacement/hemostatic plan, use atraumatic technique and local hemostatic measures, and avoid unsupervised NSAID overuse; do not extract without hematologic planning', 'C) Give intramuscular aspirin for pain control before surgery', 'D) Perform elective full-mouth surgery under no hemostatic cover for efficiency'],
     'answer': 'B) Coordinate with hematology for factor replacement/hemostatic plan, use atraumatic technique and local hemostatic measures, and avoid unsupervised NSAID overuse; do not extract without hematologic planning',
     'explanation': 'Hemophilia extractions need hematology-coordinated systemic planning plus local measures. Local packing alone with delayed hematology contact is the overlapping incomplete near-miss. Aspirin or uncovered elective surgery is dangerous.',
     'choice_explanations': {'A': 'Near-miss: local hemostatics help, but moderate factor VIII deficiency needs planned systemic cover before invasive extraction—not after bleeding starts.', 'B': 'Coordinate factor/hemostasis plans with hematology; use atraumatic technique and local measures; avoid aspirin/NSAID misuse.', 'C': 'Aspirin impairs platelets and is inappropriate peri-extraction analgesia here.', 'D': 'Elective extensive surgery without hemostatic cover is dangerous.'}
    },
        {
     'question': 'After avulsion replantation of a permanent central with prolonged dry time, follow-up radiographs at 8 months show progressive replacement resorption (ankylosis) and infraocclusion in a growing child. Which long-term complication-management concept is most appropriate?',
     'options': ['A) Guarantee the ankylosed tooth will erupt normally with the jaw forever', 'B) Orthodontically extrude heavily against ankylosis as if the PDL were normal', 'C) Counsel about inevitable progressive infraocclusion/replacement resorption, plan decoronation or timed extraction with space maintenance/prosthetic transition to preserve alveolar ridge for future implant after growth', 'D) Place an immediate adult-length implant and porcelain crown in the growing child'],
     'answer': 'C) Counsel about inevitable progressive infraocclusion/replacement resorption, plan decoronation or timed extraction with space maintenance/prosthetic transition to preserve alveolar ridge for future implant after growth',
     'explanation': 'Replacement resorption/ankylosis infraoccludes with growth; decoronation or timed extraction preserves ridge for later implant. Forced orthodontic extrusion against ankylosis is the overlapping mechanical near-miss. Guaranteeing eruption or placing a pediatric implant is wrong.',
     'choice_explanations': {'A': 'Ankylosed teeth do not erupt with vertical alveolar growth.', 'B': 'Near-miss: orthodontic extrusion works with a vital PDL, but ankylosis (bone replacement of PDL) will not extrude normally.', 'C': 'Plan decoronation/timed extraction and space/prosthetic transition for future post-growth implant.', 'D': 'Implants before growth completion infraocclude relative to adjacent erupting teeth.'}
    },
        {
     'question': 'A 3-year-old with severe early childhood caries, failure-to-thrive concerns, facial swelling from a lower molar, and fever presents late Friday. Parents refuse hospital referral hoping for only antibiotics at home. Which decision prioritizes safety?',
     'options': ['A) Agree that antibiotics alone always cure pediatric fascial infections without drainage', 'B) Discharge with oral antibiotics and next-week clinic follow-up despite fever and facial swelling', 'C) Extract teeth in an uncooperative septic toddler in a non-airway-ready setting against best judgment', 'D) Explain odontogenic infection with systemic signs needs urgent source control and possible hospital IV care; do not rely on oral antibiotics alone, and document informed refusal if they decline after clear risk discussion'],
     'answer': 'D) Explain odontogenic infection with systemic signs needs urgent source control and possible hospital IV care; do not rely on oral antibiotics alone, and document informed refusal if they decline after clear risk discussion',
     'explanation': 'Fever/swelling in a young child needs urgent source control and possible hospital care. Outpatient oral antibiotics with delayed review is the overlapping under-escalation near-miss. Agreeing antibiotics always suffice or unsafe office extraction is wrong.',
     'choice_explanations': {'A': 'Antibiotics without drainage/extraction often fail in established abscesses.', 'B': 'Near-miss: antibiotics may accompany care, but systemic pediatric odontogenic infection with swelling needs urgent escalation—not routine delayed outpatient review alone.', 'C': 'Septic uncooperative children need controlled settings, not heroic unsafe extractions.', 'D': 'Urgent source control/hospital pathways; document informed refusal if parents decline after clear counseling.'}
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
     'options': ['A) Candida albicans', 'B) Candida glabrata as the most common overall cause in immunocompetent hosts', 'C) Herpes simplex virus type 1 as a yeast', 'D) Streptococcus mutans as a fungal pathogen causing scrapable plaques'],
     'answer': 'A) Candida albicans',
     'explanation': 'Candida albicans is the predominant yeast in oral thrush. Other Candida species (e.g., glabrata) are overlapping mycologic near-misses that can cause infection, especially with risk factors, but albicans remains most common overall. HSV and S. mutans are not yeasts causing classic thrush.',
     'choice_explanations': {'A': 'Oral thrush is most often Candida albicans overgrowth in a predisposed host.', 'B': 'Near-miss: non-albicans Candida can cause oral infection, but C. albicans is still the most common overall.', 'C': 'HSV causes viral ulcerations, not yeast plaques.', 'D': 'S. mutans is a cariogenic bacterium, not a fungus causing thrush.'}
    },
        {
     'question': 'Recurrent herpes labialis lesions are driven by reactivation of which virus typically latent in which ganglion?',
     'options': ['A) HSV-1 latent in the geniculate ganglion as the usual cold-sore reservoir', 'B) HSV-1 latent in the trigeminal ganglion', 'C) HPV-16 latent in the trigeminal ganglion causing cold sores', 'D) Epstein–Barr virus latent in the dorsal root ganglion causing lip vesicles'],
     'answer': 'B) HSV-1 latent in the trigeminal ganglion',
     'explanation': 'HSV-1 reactivates from trigeminal ganglion latency to cause herpes labialis. Geniculate ganglion latency is a close neuroanatomic near-miss more associated with facial nerve/HSV complications (e.g., Ramsay Hunt involves VZV in geniculate). HPV and EBV do not cause classic cold sores via those mechanisms.',
     'choice_explanations': {'A': 'Near-miss: geniculate ganglion involvement is more relevant to facial-nerve zoster/HSV complications, not the usual herpes labialis reservoir (trigeminal).', 'B': 'Herpes labialis: HSV-1 reactivation from trigeminal ganglion latency.', 'C': 'HPV-16 is linked to oropharyngeal cancer risk, not typical cold-sore vesicles.', 'D': 'EBV is linked to hairy leukoplakia/other disease, not classic herpes labialis from DRG.'}
    },
        {
     'question': 'A white patch that cannot be wiped off and is not clinically diagnostic as another disease is termed which clinical lesion pending diagnosis?',
     'options': ['A) Frictional keratosis clearly linked to a chronic biting habit and expected to resolve with habit control', 'B) Linea alba as an obligatory carcinoma', 'C) Leukoplakia (a clinical term requiring risk assessment and often biopsy)', 'D) Scrapable candidal pseudomembrane that wipes clean leaving normal mucosa'],
     'answer': 'C) Leukoplakia (a clinical term requiring risk assessment and often biopsy)',
     'explanation': 'Leukoplakia is a clinical diagnosis of exclusion for a persistent nonwipeable white patch not identifiable as another disease. Frictional keratosis is the overlapping white-patch near-miss that is identifiable by cause and may not be labeled leukoplakia. Linea alba and wipeable thrush are different entities.',
     'choice_explanations': {'A': 'Near-miss: frictional keratosis is a white lesion with an identifiable cause; leukoplakia is used when a nonwipeable white patch is not clinically diagnostic as another disease.', 'B': 'Linea alba is a benign frictional line, not obligatory cancer.', 'C': 'Nonwipeable undiagnosed white patch = clinical leukoplakia until assessed/biopsied as indicated.', 'D': 'Wipeable white plaques suggest pseudomembranous candidiasis, not leukoplakia.'}
    },
   ],
   'medium': [
        {
     'question': 'A patient with Sjögren syndrome reports dry mouth and rampant caries at cervical margins. Which applied dental management emphasis is most appropriate?',
     'options': ['A) Discourage fluoride because enamel is unaffected by hyposalivation', 'B) Rely on salivary stimulants alone without topical fluoride or recall intensification', 'C) Prescribe anticholinergics to further reduce saliva', 'D) Salivary substitutes/stimulants as indicated, meticulous hygiene, high-fluoride regimens, and frequent recall'],
     'answer': 'D) Salivary substitutes/stimulants as indicated, meticulous hygiene, high-fluoride regimens, and frequent recall',
     'explanation': 'Sjögren xerostomia needs saliva support, fluoride, hygiene, and close recall. Stimulants alone without fluoride/recall intensification is the overlapping incomplete near-miss. Discouraging fluoride or adding anticholinergics is wrong.',
     'choice_explanations': {'A': 'Hyposalivation increases—not decreases—need for fluoride protection.', 'B': 'Near-miss: stimulants help, but high-fluoride regimens and frequent recall are also essential in Sjögren caries risk.', 'C': 'Anticholinergics exacerbate xerostomia and caries risk.', 'D': 'Combine saliva support, hygiene, high fluoride, and frequent recall.'}
    },
        {
     'question': 'A middle-aged patient presents with bilateral white reticular buccal striae without ulceration and is otherwise comfortable. Which applied working diagnosis is most likely?',
     'options': ['A) Oral lichen planus (reticular form)', 'B) Oral lichenoid contact reaction limited to the area contacting a dental restoration', 'C) Acute necrotizing ulcerative gingivitis as the first diagnosis', 'D) Traumatic fibroma of the buccal mucosa exclusively'],
     'answer': 'A) Oral lichen planus (reticular form)',
     'explanation': 'Bilateral reticular buccal striae are classic for reticular OLP. Lichenoid contact reactions are the overlapping clinical near-miss but are typically localized to contacting restoratives rather than bilateral idiopathic striae. ANUG and fibroma present differently.',
     'choice_explanations': {'A': 'Bilateral reticular buccal striae are classic for reticular oral lichen planus.', 'B': 'Near-miss: lichenoid contact reactions can look similar but are usually localized to an offending restorative contact, not bilateral idiopathic striae.', 'C': 'ANUG presents with painful punched-out papillae and fetor, not bilateral reticular striae.', 'D': 'Fibroma is a localized reactive nodule, not bilateral striae.'}
    },
        {
     'question': 'Before prescribing systemic ketoconazole for suspected oral Candida in an older patient on multiple drugs, which applied precaution is most relevant?',
     'options': ['A) Assume no azole interacts with any hepatic cytochrome pathways', 'B) Review drug interactions and consider topical antifungals first when disease is limited', 'C) Give triple the dose if the patient takes warfarin without monitoring', 'D) Prefer systemic ketoconazole over topical agents for limited pseudomembranous candidiasis without interaction review'],
     'answer': 'B) Review drug interactions and consider topical antifungals first when disease is limited',
     'explanation': 'Limited oral candidiasis often starts with topical antifungals; systemic azoles need interaction/liver review. Choosing systemic ketoconazole first for limited disease is the overlapping prescribing near-miss. Ignoring CYP interactions or tripling warfarin-era doses is dangerous.',
     'choice_explanations': {'A': 'Azoles have well-known CYP interactions.', 'B': 'Prefer topical antifungals for limited disease and screen azole interactions/liver risk before systemic use.', 'C': 'Warfarin–azole interactions can potentiate anticoagulation dangerously.', 'D': 'Near-miss: systemic azoles are used for refractory/extensive disease, not as unreviewed first-line for limited thrush.'}
    },
   ],
   'hard': [
        {
     'question': 'A 58-year-old smoker has a speckled red-white patch on the lateral tongue that persists 4 weeks after removing a sharp cusp and treating Candida. The area is firm and nonwipeable. Which multi-cue next step is most appropriate?',
     'options': ['A) Reassure that all tongue patches are geographic tongue without exam correlation', 'B) Observe for another 3 months of empiric antifungal and habit therapy before considering biopsy', 'C) Biopsy to rule out epithelial dysplasia or carcinoma; persistent speculative lesions need histopathology', 'D) Treat with systemic antibiotics for 6 months as definitive care'],
     'answer': 'C) Biopsy to rule out epithelial dysplasia or carcinoma; persistent speculative lesions need histopathology',
     'explanation': 'Persistent speckled high-risk tongue lesions after removing reversible causes need biopsy. Prolonged further empiric observation is the overlapping delay near-miss. Geographic-tongue reassurance or long antibiotics are wrong.',
     'choice_explanations': {'A': 'Geographic tongue migrates and is not a firm fixed speckled high-risk patch.', 'B': 'Near-miss: short trials for reversible causes are reasonable, but after cusp removal and Candida treatment with persistence, further months of empiric delay are inappropriate.', 'C': 'Persistent high-risk red-white tongue lesions require biopsy after reversible causes are addressed.', 'D': 'Antibiotics do not treat dysplasia/neoplasia.'}
    },
        {
     'question': 'A patient develops acute onset unilateral facial vesicles on an erythematous base along a dermatome with severe burning pain, including intraoral ulcers on the same side. Which multi-cue diagnosis and care concept fit?',
     'options': ['A) Recurrent herpes labialis with cutaneous vesicles crossing the midline freely', 'B) Aphthous stomatitis confined to nonkeratinized mucosa as the full explanation of dermatomal skin vesicles', 'C) Allergic contact dermatitis from toothpaste affecting only the contralateral face', 'D) Herpes zoster (varicella-zoster reactivation)—early antiviral therapy and pain control; watch ocular involvement if V1'],
     'answer': 'D) Herpes zoster (varicella-zoster reactivation)—early antiviral therapy and pain control; watch ocular involvement if V1',
     'explanation': 'Unilateral dermatomal vesicles and pain indicate zoster. Recurrent herpes labialis is the overlapping HSV near-miss but is typically localized vermilion/perioral and not a broad unilateral dermatome with intraoral counterpart. Aphthae and contralateral allergy do not fit.',
     'choice_explanations': {'A': 'Near-miss: HSV labialis causes vesicular lip lesions, but unilateral dermatomal skin+oral distribution with severe burning indicates zoster (VZV).', 'B': 'Aphthae do not produce cutaneous dermatomal vesicles.', 'C': 'Contralateral toothpaste allergy does not explain ipsilateral dermatomal zoster.', 'D': 'Unilateral dermatomal vesicles ± oral ulcers = zoster; treat early and protect the eye if V1.'}
    },
        {
     'question': 'A patient on methotrexate for rheumatoid arthritis develops painful oral ulcers, pancytopenia on recent labs, and fever. Which multi-cue oral medicine action is most urgent?',
     'options': ['A) Urgent medical/rheumatology coordination for possible methotrexate toxicity/infection risk; do not attribute ulcers to simple aphthae alone', 'B) Manage as recurrent aphthous stomatitis with topical steroids only while continuing methotrexate unchanged', 'C) Increase methotrexate dose empirically to treat mouth ulcers', 'D) Perform elective soft-tissue grafts under pancytopenia'],
     'answer': 'A) Urgent medical/rheumatology coordination for possible methotrexate toxicity/infection risk; do not attribute ulcers to simple aphthae alone',
     'explanation': 'Oral ulcers with pancytopenia and fever on methotrexate suggest toxicity/infection risk needing urgent medical coordination. Treating as simple aphthae while continuing MTX unchanged is the overlapping under-recognition near-miss. Increasing MTX or elective surgery under pancytopenia is dangerous.',
     'choice_explanations': {'A': 'Ulcers with pancytopenia on MTX suggest toxicity—urgent medical coordination.', 'B': 'Near-miss: aphthae are common, but pancytopenia/fever are red flags for MTX toxicity that topical steroids alone do not address.', 'C': 'Increasing MTX worsens toxicity.', 'D': 'Elective surgery under pancytopenia risks hemorrhage/infection.'}
    },
   ],
   'extreme': [
        {
     'question': 'A 65-year-old with recent weight loss has a nonhealing indurated ulcer on the lateral tongue for 3 months, ipsilateral ear pain, tobacco/alcohol history, and a firm upper cervical node. Which differential-driven management pathway is correct?',
     'options': ['A) Treat with topical antifungals for 6 months before any consideration of cancer', 'B) Urgent referral for oncology workup of suspected oral squamous cell carcinoma (biopsy/imaging/neck evaluation); do not trial months of empiric mouthwash alone', 'C) Assume traumatic ulcer forever despite induration and lymphadenopathy', 'D) Extract all contralateral teeth as definitive therapy for the tongue ulcer'],
     'answer': 'B) Urgent referral for oncology workup of suspected oral squamous cell carcinoma (biopsy/imaging/neck evaluation); do not trial months of empiric mouthwash alone',
     'explanation': 'Chronic indurated tongue ulcer with otalgia and cervical node in a tobacco/alcohol user is SCC until proven otherwise. Prolonged antifungal trials are the overlapping delay near-miss. Chronic trauma assumptions or unrelated extractions are wrong.',
     'choice_explanations': {'A': 'Near-miss: antifungals treat Candida, but neoplastic features with nodes require urgent cancer workup—not months of empiric delay.', 'B': 'High-risk nonhealing indurated tongue ulcer ± nodes needs urgent cancer referral/biopsy.', 'C': 'Induration plus lymphadenopathy contradicts simple chronic trauma.', 'D': 'Contralateral extractions do not address tongue malignancy.'}
    },
        {
     'question': 'A patient with mucocutaneous blistering, desquamative gingivitis, and a positive Nikolsky sign has oral lesions that heal with scarring. Direct immunofluorescence is pending. Which complex differential management stance is best while awaiting results?',
     'options': ['A) Scale aggressively under loose epithelium without soft-tissue precautions', 'B) Treat empirically as erosive lichen planus with topical steroids alone without immunofluorescence workup', 'C) Differentiate pemphigus vulgaris vs mucous membrane pemphigoid (and others), avoid high-trauma dental care, coordinate dermatology/oral medicine immunosuppression planning, and protect the eyes if MMP suspected', 'D) Start random systemic chemotherapy in the dental chair without diagnosis'],
     'answer': 'C) Differentiate pemphigus vulgaris vs mucous membrane pemphigoid (and others), avoid high-trauma dental care, coordinate dermatology/oral medicine immunosuppression planning, and protect the eyes if MMP suspected',
     'explanation': 'Scarring Nikolsky-positive desquamative disease needs DIF-guided distinction of pemphigus vs MMP and specialty care. Empiric erosive lichen planus therapy without workup is the overlapping mucosal near-miss. Aggressive scaling or random chemotherapy is wrong.',
     'choice_explanations': {'A': 'Trauma to loose epithelium extends erosions.', 'B': 'Near-miss: erosive lichen planus is on the differential, but scarring Nikolsky-positive disease requires DIF to distinguish pemphigus/MMP before long-term empiric care.', 'C': 'Differentiate autoimmune blistering diseases; gentle dental care; specialty immunosuppression; eye vigilance for MMP.', 'D': 'Chemotherapy without diagnosis is inappropriate dental-chair practice.'}
    },
        {
     'question': 'An HIV-positive patient with low CD4 count presents with extensive oral candidiasis, hairy leukoplakia, and a purple palatal nodule suggestive of Kaposi sarcoma. He has stopped antiretroviral therapy. Which integrated decision is most appropriate?',
     'options': ['A) Treat only with bleaching trays because purple lesions are always hematomas', 'B) Manage oral Candida and hairy leukoplakia in isolation without addressing ART interruption or the palatal nodule', 'C) Excise the entire hard palate in office under LA as first-line KS cure without medical staging', 'D) Coordinate urgent medical restart/optimization of ART, manage opportunistic oral infections, and refer the palatal lesion for definitive KS evaluation/treatment'],
     'answer': 'D) Coordinate urgent medical restart/optimization of ART, manage opportunistic oral infections, and refer the palatal lesion for definitive KS evaluation/treatment',
     'explanation': 'Advanced HIV oral disease needs ART optimization plus targeted local care and KS referral. Treating Candida/hairy leukoplakia alone while ignoring ART and the purple nodule is the overlapping incomplete near-miss. Bleaching or office palatectomy is wrong.',
     'choice_explanations': {'A': 'Purple palatal nodules in advanced HIV raise KS concern, not routine hematoma/bleaching care.', 'B': 'Near-miss: local opportunistic infections need treatment, but ART restart and KS evaluation of the palatal nodule are essential parts of integrated care.', 'C': 'KS needs staging/systemic planning; blind total palatectomy under LA is not first-line.', 'D': 'Coordinate ART, manage opportunistic infections, and refer suspected KS—not denial or mutilating office surgery.'}
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
     'options': ['A) A layer of cutting debris that can occlude dentinal tubules and affect bonding/sealing', 'B) The hybrid layer of resin-infiltrated collagen formed after adhesive application', 'C) A sterile rubber dam sheet bonded to enamel', 'D) The pulp chamber roof exclusively'],
     'answer': 'A) A layer of cutting debris that can occlude dentinal tubules and affect bonding/sealing',
     'explanation': 'Smear layer is instrumentation debris that plugs tubules and affects bonding. The hybrid layer is the overlapping adhesive near-miss formed after conditioning/resin infiltration—not the smear layer itself. Rubber dam and pulp roof are unrelated.',
     'choice_explanations': {'A': 'Smear layer = instrumentation debris affecting tubule patency and adhesive behavior.', 'B': 'Near-miss: the hybrid layer is resin-infiltrated dentin created by adhesive procedures, not the cutting-debris smear layer.', 'C': 'Rubber dam is isolation equipment, not a tooth surface layer.', 'D': 'Pulp chamber roof is anatomy, not smear debris.'}
    },
        {
     'question': 'Which property most directly explains why enamel etchant (phosphoric acid) improves micromechanical retention for resin bonding?',
     'options': ['A) Complete dissolution of enamel prisms with no resin infiltration required for retention', 'B) Selective demineralization creating microporosities for resin tag formation', 'C) Conversion of enamel into gutta-percha-like material', 'D) Chemical anesthesia of odontoblasts within enamel'],
     'answer': 'B) Selective demineralization creating microporosities for resin tag formation',
     'explanation': 'Acid etching creates enamel microporosities for micromechanical resin bonding. Claiming etching alone retains without resin infiltration is the overlapping incomplete near-miss. Etchant does not create GP or anesthetize odontoblasts.',
     'choice_explanations': {'A': 'Near-miss: etching creates porosities, but retention depends on resin infiltration/tag formation—not acid alone.', 'B': 'Etching creates enamel microporosities for micromechanical resin bonding.', 'C': 'Gutta-percha is an endodontic obturant, not etched enamel.', 'D': 'Etchant is not a local anesthetic for odontoblasts.'}
    },
        {
     'question': 'Caries excavation ideally aims to remove which tissue while preserving maximally reparable dentin near the pulp when doing selective removal in deep lesions?',
     'options': ['A) All dentin until pulp exposure is mandatory in every deep lesion', 'B) Only extrinsic stain on intact enamel without assessing hardness', 'C) Soft, highly infected dentin while retaining firm, remineralizable dentin when indicated', 'D) Firm, discolored affected dentin near the pulp in every case, leaving soft infected dentin peripherally'],
     'answer': 'C) Soft, highly infected dentin while retaining firm, remineralizable dentin when indicated',
     'explanation': 'Selective removal targets soft infected dentin and may retain firm affected dentin to avoid exposure. Leaving soft infected dentin peripherally while only retaining deep firm dentin reverses the selective-removal logic (near-miss). Mandatory exposure or stain-only criteria are wrong.',
     'choice_explanations': {'A': 'Pulp exposure is not mandatory if sealed selective removal can avoid it.', 'B': 'Stain alone is not the excavation criterion; hardness/texture matter.', 'C': 'Remove soft infected dentin; retain firm remineralizable dentin when indicated, then seal.', 'D': 'Near-miss: selective protocols retain firm affected dentin centrally when indicated, but soft infected dentin—especially peripherally at the enamel-dentin junction—should not be left.'}
    },
   ],
   'medium': [
        {
     'question': 'A Class II composite keeps failing with proximal contact loss and food impaction. Which applied corrective principle is most important?',
     'options': ['A) Cure without a matrix because composites expand to form contacts', 'B) Use a circumferential matrix without wedging and accept a light contact', 'C) Ignore wedge adaptation because gingival overhangs prevent failure', 'D) Use proper matrix/wedge technique to establish tight anatomic contact before curing'],
     'answer': 'D) Use proper matrix/wedge technique to establish tight anatomic contact before curing',
     'explanation': 'Class II contacts require contoured matrix and wedge before curing. Using a matrix without adequate wedging/contour is the overlapping technique near-miss that still yields open contacts/overhangs. Curing without a matrix or accepting overhangs is wrong.',
     'choice_explanations': {'A': 'Composite polymerization does not create contacts without a contoured matrix.', 'B': 'Near-miss: a matrix is necessary but without proper wedging/contour, contacts remain open and gingival seal fails.', 'C': 'Overhangs trap plaque and worsen gingival outcomes.', 'D': 'Reliable Class II contacts require matrix and wedge systems before light-curing.'}
    },
        {
     'question': 'Postoperative sensitivity after a posterior composite is most often linked clinically to which applied factors?',
     'options': ['A) Occlusal prematurities, polymerization stress, or incomplete sealing of dentin', 'B) Ideal bonding with perfect seal but unavoidable pulp hyperemia lasting months', 'C) Choosing a shade that is slightly too light esthetically', 'D) Using rubber dam isolation during placement'],
     'answer': 'A) Occlusal prematurities, polymerization stress, or incomplete sealing of dentin',
     'explanation': 'Post-composite sensitivity commonly links to hyperocclusion, C-factor stress/gaps, or imperfect dentin seal. Assuming months of “normal” hyperemia despite perfect seal is the overlapping dismissive near-miss. Shade and rubber dam are not primary causes.',
     'choice_explanations': {'A': 'Check occlusion, bonding/seal, and stress management when composites cause sensitivity.', 'B': 'Near-miss: mild transient sensitivity can occur, but persistent symptoms should prompt search for high spots, gaps, or seal failures—not assumed inevitable hyperemia.', 'C': 'Shade mismatch is esthetic, not a sensitivity mechanism.', 'D': 'Rubber dam reduces contamination and typically helps bonding success.'}
    },
        {
     'question': 'When restoring a deep proximal box near the pulp with composite, which applied liner/base concept is most coherent with modern adhesive dentistry?',
     'options': ['A) Place a thick unsealed cotton pellet permanently under composite', 'B) Consider a thin bioactive/glass-ionomer or calcium silicate liner on the deepest dentin when indicated, then adhesive composite', 'C) Never seal dentin because tubules must remain widely open to saliva', 'D) Use zinc oxide–eugenol directly under all resins as the preferred bonding primer'],
     'answer': 'B) Consider a thin bioactive/glass-ionomer or calcium silicate liner on the deepest dentin when indicated, then adhesive composite',
     'explanation': 'Deep dentin may receive a thin GI/calcium-silicate liner then adhesive composite. Permanent cotton, open salivary tubules, or eugenol under resin are incorrect. (ZOE under resin is a classic material near-miss.)',
     'choice_explanations': {'A': 'Cotton pellets are temporary coverage, not permanent bases under composite.', 'B': 'Deep dentin may get a compatible liner then adhesive composite.', 'C': 'Dentin should be sealed from bacterial/salivary contamination.', 'D': 'Near-miss: ZOE can soothe/ temporize, but eugenol can interfere with resin polymerization and is not the preferred liner under composite.'}
    },
   ],
   'hard': [
        {
     'question': 'A premolar has an old MOD amalgam with a cracked marginal ridge, bite pain on release, and a hairline crack staining toward the pulp on removal of the restoration. Pulp tests are normal lingering-free. Which multi-cue restorative plan fits?',
     'options': ['A) Replace with a large bonded MOD composite without cuspal coverage and monitor the crack', 'B) Proceed straight to extraction without assessing restorable structure', 'C) Protect cusps with an onlay/crown after confirming restorable crack extent and vitality; do not place another large amalgam without cuspal coverage', 'D) Apply bleaching gel into the crack as definitive structural therapy'],
     'answer': 'C) Protect cusps with an onlay/crown after confirming restorable crack extent and vitality; do not place another large amalgam without cuspal coverage',
     'explanation': 'Cracks under large MOD restorations usually need cuspal coverage when restorable. A large bonded composite without coverage is the overlapping under-protection near-miss. Automatic extraction or bleach is wrong.',
     'choice_explanations': {'A': 'Near-miss: bonded composites can help temporarily, but unprotected cusps commonly allow crack propagation—cuspal coverage is preferred.', 'B': 'Many cracked teeth are restorable with coverage; extraction is not automatic.', 'C': 'Restorable cracked premolars after large MOD failure typically need cuspal coverage restorations.', 'D': 'Bleach does not provide structural reinforcement.'}
    },
        {
     'question': 'A cervical noncarious lesion on a canine shows abfraction-type morphology, heavy occlusal interferences, and gingival recession with sensitivity. Which multi-cue approach is most rational?',
     'options': ['A) Restore the cervical lesion with composite only and ignore occlusal interferences and brushing trauma', 'B) Prescribe antibiotics for abfraction', 'C) Extract the canine as first-line for sensitivity', 'D) Adjust occlusal prematurities as indicated, counsel on brushing technique, and restore with an appropriate flexible adhesive material if indicated for sensitivity/esthetics/plaque control'],
     'answer': 'D) Adjust occlusal prematurities as indicated, counsel on brushing technique, and restore with an appropriate flexible adhesive material if indicated for sensitivity/esthetics/plaque control',
     'explanation': 'Cervical lesions often combine stress, abrasion, and erosion—manage occlusion/habits and restore as needed. Restoring alone without etiology control is the overlapping incomplete near-miss. Antibiotics or extraction are wrong.',
     'choice_explanations': {'A': 'Near-miss: restoration may relieve sensitivity, but ignoring occlusal prematurities and brushing trauma invites recurrence/failure.', 'B': 'Abfraction/abrasion lesions are not treated with antibiotics.', 'C': 'Extraction is not first-line for cervical sensitivity.', 'D': 'Manage occlusal and habit factors and restore cervically with suitable adhesive materials when needed.'}
    },
        {
     'question': 'During deep caries removal on a vital molar, a pinpoint pulp exposure occurs with bright red hemorrhage that stops within 1–2 minutes. The tooth had no lingering spontaneous pain. Which multi-cue vital pulp therapy choice is most appropriate?',
     'options': ['A) Direct pulp cap or partial pulpotomy with hydraulic calcium silicate cement and immediate well-sealed restoration', 'B) Direct pulp cap with calcium hydroxide only, delaying the final restoration for several weeks while open to microleakage risk', 'C) Extract immediately without discussing vital pulp therapy options', 'D) Apply arsenical paste to mummify the entire pulp as modern standard care'],
     'answer': 'A) Direct pulp cap or partial pulpotomy with hydraulic calcium silicate cement and immediate well-sealed restoration',
     'explanation': 'Pinpoint vital exposures without irreversible symptoms can succeed with bioceramic capping/partial pulpotomy and an immediate excellent seal. Calcium hydroxide capping with delayed unsealed temporization is the overlapping vital-pulp near-miss with higher leakage failure risk. Extraction or arsenicals are wrong.',
     'choice_explanations': {'A': 'Controlled vital exposures without irreversible symptoms warrant bioceramic pulp capping/partial pulpotomy plus immediate seal.', 'B': 'Near-miss: Ca(OH)2 capping has been used, but delayed poorly sealed temporaries raise failure risk versus immediate well-sealed bioceramic care.', 'C': 'Many exposures are manageable with vital pulp therapy; extraction is not automatic.', 'D': 'Arsenical pulp mummification is obsolete and unsafe by modern standards.'}
    },
   ],
   'extreme': [
        {
     'question': 'A strategic maxillary canine abutment for an RPD has deep distal caries under an old crown, questionable remaining ferrule after excavation, lingering cold pain, and a patient who refuses implants. Which complex restorative–endodontic decision is best?',
     'options': ['A) Recement the old crown over soft caries and irreversible pulpitis symptoms', 'B) Assess restorability after caries control; if inadequate ferrule, discuss crown-lengthening/orthodontic extrusion versus extraction; if irreversible pulpitis and restorable, RCT plus core/crown with planned surveyed contours', 'C) Promise a veneer alone will replace missing ferrule and endodontic need', 'D) Proceed with RCT and crown without assessing remaining ferrule or RPD survey requirements'],
     'answer': 'B) Assess restorability after caries control; if inadequate ferrule, discuss crown-lengthening/orthodontic extrusion versus extraction; if irreversible pulpitis and restorable, RCT plus core/crown with planned surveyed contours',
     'explanation': 'Strategic abutments need honest ferrule/restorability assessment before RCT/crown. Doing RCT/crown without ferrule/survey assessment is the overlapping incomplete near-miss. Recementing over disease or veneers without structure is wrong.',
     'choice_explanations': {'A': 'Cementing over caries and pulpitis fails biologically and mechanically.', 'B': 'Assess ferrule/restorability, then RCT/crown with surveyed contours—or extraction/CL/extrusion pathways.', 'C': 'Veneers do not create ferrule or treat irreversible pulpitis.', 'D': 'Near-miss: RCT/crown may be needed, but only after confirming adequate ferrule and planning surveyed RPD contours.'}
    },
        {
     'question': 'A patient develops severe biting pain one week after a large MOD composite on a molar. The restoration has a high centric stop, a hairline crack is now visible under magnification, and cold lingers mildly. Which complication-management sequence is most appropriate?',
     'options': ['A) Add more composite bulk on the occlusal to strengthen without adjusting the high spot', 'B) Prescribe long-term opioids as the only intervention', 'C) Immediately adjust occlusion, reassess pulp status, consider cuspal coverage or endodontics if pulp becomes irreversible, and replace the structurally inadequate restoration design', 'D) Adjust the high spot only and leave the crack-prone large MOD design unchanged long term'],
     'answer': 'C) Immediately adjust occlusion, reassess pulp status, consider cuspal coverage or endodontics if pulp becomes irreversible, and replace the structurally inadequate restoration design',
     'explanation': 'Hyperocclusion with crack signs needs prompt occlusal correction plus structural redesign and pulp reassessment. Adjusting occlusion alone without addressing inadequate MOD design is the overlapping incomplete near-miss. Adding bulk or opioids alone is wrong.',
     'choice_explanations': {'A': 'Adding composite to a high restoration increases load and crack risk.', 'B': 'Opioids mask pain without correcting occlusion or structure.', 'C': 'Adjust occlusion, reassess pulp, and redesign for cuspal protection as needed.', 'D': 'Near-miss: occlusal adjustment is urgent, but a crack under a large MOD usually also needs cuspal-coverage redesign.'}
    },
        {
     'question': 'An extensive posterior composite shows recurrent caries at the gingival margin, open contact, and radiographic crestal bone loss localized to that interproximal. The patient wants just polish and bleach. Which decision is ethically and clinically correct?',
     'options': ['A) Polish and bleach only as requested without discussing disease findings', 'B) Repair the open margin with sealant and bleach, deferring contact correction', 'C) Place a permanent post into the pulp chamber empirically without diagnosis', 'D) Explain that recurrent caries and periodontal harm require replacing the restoration with proper contact/contour and addressing hygiene; bleaching/polishing alone is insufficient'],
     'answer': 'D) Explain that recurrent caries and periodontal harm require replacing the restoration with proper contact/contour and addressing hygiene; bleaching/polishing alone is insufficient',
     'explanation': 'Open contact and recurrent gingival caries with local bone loss need replacement and perio attention. Sealant repair plus bleach without correcting contact is the overlapping inadequate near-miss. Cosmetic-only care or empiric posts are wrong.',
     'choice_explanations': {'A': 'Withholding diagnosis to satisfy a cosmetic request is unethical and leaves disease active.', 'B': 'Near-miss: marginal repair is sometimes interim, but open contact with recurrent caries and bone loss requires full replacement and contour/contact correction.', 'C': 'Empiric posts without endodontic need violate tooth structure without benefit.', 'D': 'Replace the defective restoration with proper contact/contour and address hygiene/periodontal harm.'}
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
     'options': ['A) Keep radiation exposure as low as reasonably achievable while obtaining necessary diagnostic information', 'B) Minimize dose by avoiding all radiographs, including those that would change urgent treatment', 'C) Always take the maximum number of films possible for every visit', 'D) Use radiation for tooth bleaching activation routinely'],
     'answer': 'A) Keep radiation exposure as low as reasonably achievable while obtaining necessary diagnostic information',
     'explanation': 'ALARA balances diagnostic yield with dose minimization. Avoiding all indicated radiographs is the overlapping dose-misinterpretation near-miss. Maximal unjustified films or using x-rays to bleach are wrong.',
     'choice_explanations': {'A': 'ALARA = necessary diagnostic images at the lowest reasonable dose.', 'B': 'Near-miss: dose reduction matters, but ALARA does not mean withholding indicated radiographs that change care.', 'C': 'Unnecessary maximal film counts violate ALARA.', 'D': 'Ionizing dental x-rays are not a bleaching modality.'}
    },
        {
     'question': 'A periapical radiograph primarily images which structures?',
     'options': ['A) The crowns and alveolar crest only, similar to a bitewing field of view', 'B) The full tooth length including crown, root, and surrounding periapical bone', 'C) Only the mandibular condyle in motion', 'D) Only the skin surface without teeth'],
     'answer': 'B) The full tooth length including crown, root, and surrounding periapical bone',
     'explanation': 'Periapicals show the entire tooth and periapical bone. Bitewing-limited crown/crest imaging is the overlapping intraoral near-miss with a different primary purpose. Condyle motion and skin imaging use other modalities.',
     'choice_explanations': {'A': 'Near-miss: bitewings emphasize crowns/crestal bone; periapicals are chosen for full root and periapex.', 'B': 'Periapicals capture whole-tooth and periapical bone detail.', 'C': 'Condylar dynamics need TMJ-specific imaging, not standard PA.', 'D': 'Skin surface is not imaged for dental diagnosis on PA films.'}
    },
        {
     'question': 'Increasing the source-to-object distance while using proper collimation generally has which effect on image sharpness, all else equal?',
     'options': ['A) Decreases sharpness by increasing geometric penumbra', 'B) Has no effect on geometric unsharpness if mA is unchanged', 'C) Improves sharpness by reducing geometric penumbra (magnification of the focal spot blur)', 'D) Converts the image into a CT volumetric dataset'],
     'answer': 'C) Improves sharpness by reducing geometric penumbra (magnification of the focal spot blur)',
     'explanation': 'Greater source-to-object distance reduces geometric penumbra and can improve sharpness. Claiming the opposite penumbra effect is the overlapping geometry near-miss. mA alone does not define penumbra; distance change does not create CT volumes.',
     'choice_explanations': {'A': 'Near-miss: this reverses the geometric relationship—increasing source-to-object distance reduces, rather than increases, penumbra.', 'B': 'Geometric unsharpness depends on focal spot and distances, not mA alone.', 'C': 'Greater source-to-object distance reduces penumbra and can sharpen projection images.', 'D': 'CT requires specialized volumetric acquisition, not merely moving the tube farther.'}
    },
   ],
   'medium': [
        {
     'question': 'A bitewing radiograph is most appropriately selected for which applied diagnostic task?',
     'options': ['A) Diagnosing fracture of the mandibular condylar neck exclusively', 'B) Mapping the full extent of a large odontogenic sinus cyst alone', 'C) Replacing all need for clinical probing of periodontal pockets', 'D) Detecting interproximal caries and evaluating crestal bone height between posterior teeth'],
     'answer': 'D) Detecting interproximal caries and evaluating crestal bone height between posterior teeth',
     'explanation': 'Bitewings excel for posterior interproximal caries and crestal bone assessment. Using them as a full substitute for probing is a close periodontal assessment near-miss—radiographs complement probing. Condyle and large sinus lesions need wider imaging.',
     'choice_explanations': {'A': 'Condylar neck fractures need dedicated mandibular/TMJ imaging.', 'B': 'Large antral lesions need wider field imaging than bitewings.', 'C': 'Near-miss: bitewings help assess crestal bone but do not replace clinical probing depths.', 'D': 'Bitewings are for interproximal caries and posterior crestal bone evaluation.'}
    },
        {
     'question': 'Cervical burnout on a periapical radiograph is an applied optical/anatomic phenomenon that can mimic which disease?',
     'options': ['A) Root caries or radiolucent cervical lesions near the CEJ', 'B) Internal resorption centered in the pulp chamber', 'C) Condensing osteitis only', 'D) Impacted third molar follicle exclusively'],
     'answer': 'A) Root caries or radiolucent cervical lesions near the CEJ',
     'explanation': 'Cervical burnout can mimic cervical/root caries near the CEJ. Internal resorption is a radiolucent near-miss but is pulp-centered, not a cervical optical artifact. Condensing osteitis and follicles are different entities.',
     'choice_explanations': {'A': 'Cervical burnout can mimic cervical/root caries; confirm clinically.', 'B': 'Near-miss: internal resorption is radiolucent but located within the pulp canal/chamber space, not as cervical burnout at the CEJ.', 'C': 'Condensing osteitis is a periapical radiopacity, not a cervical radiolucent artifact.', 'D': 'Follicular spaces surround crowns of unerupted teeth, a different entity.'}
    },
        {
     'question': 'Compared with film, a well-exposed digital sensor system typically allows which applied dose advantage when used correctly?',
     'options': ['A) Unlimited retakes without any dose concern', 'B) Lower dose per image with comparable diagnostic task performance for many indications', 'C) Complete immunity of digital images to positioning errors', 'D) Elimination of the need for clinical indications'],
     'answer': 'B) Lower dose per image with comparable diagnostic task performance for many indications',
     'explanation': 'Digital receptors are more dose-efficient for many tasks, supporting ALARA—but retakes still add dose. Unlimited retakes is the overlapping digital-dose near-miss misconception. Positioning still matters; indications remain mandatory.',
     'choice_explanations': {'A': 'Near-miss: digital lowers dose per image, but each retake still adds patient dose.', 'B': 'Digital radiography often reduces dose per image with comparable diagnostic performance for many tasks.', 'C': 'Geometry/positioning errors still degrade digital images.', 'D': 'Clinical indications still govern when to expose.'}
    },
   ],
   'hard': [
        {
     'question': 'A panoramic radiograph shows a well-defined radiolucency at the mandibular angle with a radiopaque impacted third molar crown and a corticated follicular space greater than 5 mm. The patient has no caries in the tooth. Which multi-cue interpretation is most likely?',
     'options': ['A) Hyperplastic dental follicle within normal size limits without cystic change', 'B) Periapical cemento-osseous dysplasia of a vital central incisor', 'C) Dentigerous (follicular) cyst associated with the unerupted third molar until proven otherwise', 'D) Sialolith in the submandibular duct exclusively'],
     'answer': 'C) Dentigerous (follicular) cyst associated with the unerupted third molar until proven otherwise',
     'explanation': 'Pericoronal radiolucency >~5 mm around an unerupted crown suggests dentigerous cyst. Hyperplastic follicle is the overlapping pericoronal near-miss used for smaller/borderline follicular enlargements. PCOD and sialoliths are different patterns.',
     'choice_explanations': {'A': 'Near-miss: follicular hyperplasia is considered with milder enlargement; a corticated pericoronal lucency >5 mm suggests dentigerous cyst until proven otherwise.', 'B': 'PCOD is a periapical radiopaque/mixed lesion of anterior vital teeth, not third-molar follicles.', 'C': 'Enlarged pericoronal radiolucency on an impacted molar suggests dentigerous cyst.', 'D': 'Sialoliths are calcifications in salivary ducts, not pericoronal cysts.'}
    },
        {
     'question': 'A patient has a suspected vertical root fracture in an endodontically treated premolar with a narrow deep probing defect and a J-shaped radiolucency, but the 2D image is equivocal. Which multi-cue imaging decision is best?',
     'options': ['A) Take weekly full-head medical CT for six months routinely', 'B) Rely on repeated periapical parallax alone when management hinges on confirming a fracture in 3D', 'C) Diagnose fracture solely from bitewing caries depth without clinical signs', 'D) Consider limited-field CBCT when it may change management, accepting higher dose only if justified after clinical correlation'],
     'answer': 'D) Consider limited-field CBCT when it may change management, accepting higher dose only if justified after clinical correlation',
     'explanation': 'Suspected VRF with equivocal 2D imaging may justify limited CBCT when it changes management. Endless 2D parallax only is the overlapping under-imaging near-miss when 3D would alter extraction-vs-save decisions. Weekly medical CT or bitewing-only diagnosis is wrong.',
     'choice_explanations': {'A': 'Weekly full-head CT violates ALARA dramatically.', 'B': 'Near-miss: parallax helps some tasks, but when VRF decisions need 3D and 2D is equivocal, justified limited CBCT is preferred over endless 2D only.', 'C': 'Bitewings assess caries/bone, not definitive VRF diagnosis alone.', 'D': 'Justify limited CBCT for suspected VRF when 2D is equivocal and management would change.'}
    },
        {
     'question': 'On a periapical image, the zygomatic process of the maxilla obscures the roots of upper molars. Which multi-cue technique adjustment often helps?',
     'options': ['A) Change receptor placement/angulation (e.g., more distal/vertical adjustments) or use a different projection to move the zygoma shadow off the roots', 'B) Increase kVp/mA without changing geometry to “burn through” the zygoma', 'C) Ask for a mandibular occlusal film as the only view of maxillary molar roots', 'D) Interpret obscured roots as always missing without trying another angle'],
     'answer': 'A) Change receptor placement/angulation (e.g., more distal/vertical adjustments) or use a different projection to move the zygoma shadow off the roots',
     'explanation': 'Zygomatic superimposition is corrected by angulation/placement or alternate projections. Increasing exposure without geometry change is the overlapping technique near-miss that still leaves the shadow. Mandibular occlusals or assuming missing roots are wrong.',
     'choice_explanations': {'A': 'Reangle/reposition to move zygomatic superimposition off maxillary molar roots.', 'B': 'Near-miss: exposure changes may alter density but do not move the zygoma off the roots without geometric adjustment.', 'C': 'Mandibular occlusal projections do not image maxillary molar roots.', 'D': 'One obscured projection is insufficient to diagnose missing roots.'}
    },
   ],
   'extreme': [
        {
     'question': 'A 55-year-old with prior head/neck radiation for cancer needs extractions of periodontally hopeless teeth in the irradiated mandible field. Orthopantomogram shows mixed sclerosis. He asks for simple forceps removal today. Which complex risk-management decision is correct?',
     'options': ['A) Extract immediately with maximal flap reflection and bone removal without counseling ORN risk', 'B) Recognize osteoradionecrosis risk; coordinate oncology/OMFS, consider hyperbaric protocols where used, prefer atraumatic/surgical planning, and avoid casual extractions without risk counseling', 'C) Assure that radiated bone never develops healing complications', 'D) Proceed after a panoramic only, without specialist coordination, using routine forceps technique'],
     'answer': 'B) Recognize osteoradionecrosis risk; coordinate oncology/OMFS, consider hyperbaric protocols where used, prefer atraumatic/surgical planning, and avoid casual extractions without risk counseling',
     'explanation': 'Irradiated jaws have lifelong ORN risk after extraction; specialist-coordinated atraumatic planning and counseling are required. Routine forceps extraction after a pan alone is the overlapping under-prepared near-miss. Aggressive uncounselled surgery or denying risk is wrong.',
     'choice_explanations': {'A': 'Aggressive surgery without ORN counseling increases harm risk.', 'B': 'Post-radiation extractions need ORN risk counseling and specialist-coordinated atraumatic planning.', 'C': 'Radiation-damaged bone has impaired healing and ORN risk.', 'D': 'Near-miss: imaging helps, but irradiated-field extractions still need specialist risk planning—not casual routine forceps care.'}
    },
        {
     'question': 'CBCT ordered for implant planning incidentally shows a well-circumscribed radiopaque mass in the mandibular canal region with expansion, and the patient has lip paresthesia. Which differential-driven next step is most appropriate?',
     'options': ['A) Proceed with freehand implant drilling through the radiopaque canal mass', 'B) Continue implant planning with a shorter implant placed coronal to the mass without specialist evaluation of paresthesia', 'C) Stop routine implant drilling plans; refer for specialist evaluation of a possible benign neural tumor/other canal lesion before any implant osteotomy', 'D) Diagnose the finding as cervical burnout of a molar crown'],
     'answer': 'C) Stop routine implant drilling plans; refer for specialist evaluation of a possible benign neural tumor/other canal lesion before any implant osteotomy',
     'explanation': 'Canal-centered expanding radiopacity with paresthesia needs specialist workup before any osteotomy. Planning a shorter implant above the lesion without evaluating the neuropathy is the overlapping implant near-miss. Drilling through the mass or calling it cervical burnout is wrong.',
     'choice_explanations': {'A': 'Drilling through a canal mass can transect the IAN and worsen deficit.', 'B': 'Near-miss: avoiding the mass vertically still ignores a symptomatic canal lesion that needs diagnosis before elective implant surgery.', 'C': 'Incidental canal lesion + paresthesia mandates specialist workup before any implant osteotomy.', 'D': 'Cervical burnout occurs at tooth necks, not as expanding canal masses.'}
    },
        {
     'question': 'A pregnant patient in the first trimester has acute pulpal pain and suspected periapical pathology on a lower molar. She fears any radiographs. Which decision balances fetal concerns with dental diagnosis?',
     'options': ['A) Refuse all imaging forever and also refuse emergency dental treatment', 'B) Take a full-mouth series plus CBCT of both jaws just in case without indications', 'C) Use medical abdominal CT instead of a dental periapical for the tooth', 'D) Explain that with proper shielding and modern receptors, a necessary periapical has very low fetal dose and is justified when it changes urgent care; do not withhold indicated imaging that prevents infection progression'],
     'answer': 'D) Explain that with proper shielding and modern receptors, a necessary periapical has very low fetal dose and is justified when it changes urgent care; do not withhold indicated imaging that prevents infection progression',
     'explanation': 'Indicated shielded dental radiographs are acceptable in pregnancy when they change urgent care. Refusing all imaging and treatment is the overlapping fetal-dose fear near-miss. Unindicated FMX/CBCT or abdominal CT violates ALARA far more.',
     'choice_explanations': {'A': 'Near-miss: fetal dose concern is understandable, but indicated emergency dental imaging/treatment should not be refused outright when maternal infection risk is real.', 'B': 'Unindicated full-mouth + CBCT contradicts ALARA in pregnancy.', 'C': 'Abdominal CT delivers far higher dose and does not image teeth usefully.', 'D': 'Necessary shielded dental radiographs for acute care are appropriate; avoid both neglect and over-imaging.'}
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
     'options': ['A) Maxillary canine', 'B) Mandibular canine, which has a long root but typically shorter than the maxillary canine', 'C) Maxillary third molar', 'D) Mandibular central incisor'],
     'answer': 'A) Maxillary canine',
     'explanation': 'The maxillary canine usually has the longest root of the permanent dentition. The mandibular canine is the classic overlapping long-root near-miss but is typically shorter than the maxillary canine. Third molars and mandibular centrals are shorter/variable.',
     'choice_explanations': {'A': 'Maxillary canines characteristically have the longest roots among permanent teeth.', 'B': 'Near-miss: mandibular canines have long roots, but maxillary canines are typically longest overall.', 'C': 'Third molar roots are often short, fused, or variable—not the longest on average.', 'D': 'Mandibular central roots are comparatively short and narrow.'}
    },
        {
     'question': 'The cusp of Carabelli is most frequently associated with which tooth surface?',
     'options': ['A) Mesiolingual cusp region of the maxillary second molar, where Carabelli trait is less common than on first molars', 'B) Mesiolingual cusp region of the maxillary first molar', 'C) Incisal edge of the mandibular central incisor', 'D) Buccal pit of the mandibular canine'],
     'answer': 'B) Mesiolingual cusp region of the maxillary first molar',
     'explanation': 'Cusp of Carabelli, when present, is most frequent on the mesiolingual of maxillary first molars. Maxillary second molars can show the trait less often—the overlapping molar near-miss. Incisors and canines do not bear Carabelli cusps.',
     'choice_explanations': {'A': 'Near-miss: Carabelli trait can appear on maxillary second molars but is most frequently associated with first molars.', 'B': 'Cusp of Carabelli appears on the mesiolingual of maxillary first molars when present.', 'C': 'Incisors lack Carabelli cusps.', 'D': 'Canines do not bear a Carabelli cusp on a buccal pit.'}
    },
        {
     'question': 'Which primary tooth is most likely to exhibit a prominent mesial cervical crown bulge and a unique occlusal anatomy among primary molars commonly tested?',
     'options': ['A) Primary mandibular first molar, which also has a strong buccal cervical ridge but different occlusal form', 'B) Permanent maxillary first premolar exclusively as a primary tooth form', 'C) Primary maxillary first molar (distinct from permanent premolar form)', 'D) Primary mandibular central incisor exclusively as a molar form'],
     'answer': 'C) Primary maxillary first molar (distinct from permanent premolar form)',
     'explanation': 'Primary maxillary first molars have distinctive morphology with a prominent cervical bulge commonly tested. Primary mandibular first molars also have marked cervical ridges—the overlapping primary-molar near-miss—but the stem’s unique occlusal anatomy points to the maxillary primary first molar. Permanent premolars and primary centrals are wrong categories.',
     'choice_explanations': {'A': 'Near-miss: primary mandibular first molars have prominent cervical ridges, but the commonly tested unique occlusal anatomy here refers to the primary maxillary first molar.', 'B': 'Permanent premolars are not primary teeth.', 'C': 'Primary maxillary first molars have distinctive molar form with marked cervical bulge features emphasized in anatomy courses.', 'D': 'Primary mandibular centrals are incisors, not molars.'}
    },
   ],
   'medium': [
        {
     'question': 'Which applied anatomic feature of mandibular first molars most influences periodontal instrument adaptation buccally?',
     'options': ['A) Presence of a cusp of Carabelli on the buccal surface', 'B) A single conical root like a primary incisor always', 'C) The deep lingual concavity alone without cervical/furcation consideration', 'D) The cervical enamel contour and root trunk with possible buccal furcation involvement'],
     'answer': 'D) The cervical enamel contour and root trunk with possible buccal furcation involvement',
     'explanation': 'Mandibular first molar buccal instrumentation is guided by cervical contour, root trunk, and buccal furcation anatomy. Focusing only on lingual concavity is an incomplete anatomic near-miss. Carabelli and single-root assumptions are wrong.',
     'choice_explanations': {'A': 'Cusp of Carabelli is maxillary first molar mesiolingual, not mandibular buccal.', 'B': 'Mandibular first molars normally have two roots, not a single conical root.', 'C': 'Near-miss: lingual anatomy matters on the lingual side, but buccal adaptation is driven by buccal cervical contour/root trunk/furcation.', 'D': 'Mandibular first molar cervical/furcation anatomy guides buccal periodontal instrumentation.'}
    },
        {
     'question': 'For endodontic access, which applied pulp-chamber landmark relationship is most reliable in mature maxillary first molars?',
     'options': ['A) Pulp chamber floor is at the level of the CEJ region with canal orifices arranged accordingly (often MB, DB, P; MB2 common)', 'B) Pulp chamber floor lies well apical to the root furcation in mature maxillary first molars', 'C) There is never more than one canal in any maxillary molar', 'D) All canal orifices always exit through the occlusal enamel without a chamber floor map'],
     'answer': 'A) Pulp chamber floor is at the level of the CEJ region with canal orifices arranged accordingly (often MB, DB, P; MB2 common)',
     'explanation': 'In mature molars the chamber floor approximates CEJ level with MB/DB/P orifices and frequent MB2. Placing the floor at the furcation level is the overlapping access near-miss that leads to perforation. Single-canal assumptions or ignoring chamber-floor maps are wrong.',
     'choice_explanations': {'A': 'Maxillary first molar access uses CEJ-level chamber floor landmarks and anticipates MB2.', 'B': 'Near-miss: confusing floor level with furcation depth risks furcal perforation; the floor is near CEJ, not well apical at the furcation.', 'C': 'MB2 is common; assuming only one canal is a frequent cause of failure.', 'D': 'Orifices are mapped on the chamber floor, not as enamel-surface exits without chamber anatomy.'}
    },
        {
     'question': 'Occlusal contact on a maxillary premolar is applied clinically when adjusting a crown. Which anatomic feature primarily guides buccal cusp placement in the fossae of the antagonist?',
     'options': ['A) The guiding/non-supporting cusp tip contacts into opposing fossae as the primary holding contact', 'B) The supporting cusp relationship into opposing fossae/marginal ridge areas within the occlusal scheme', 'C) The color of the shade tab under metamerism only', 'D) The pulp chamber height alone without occlusal anatomy'],
     'answer': 'B) The supporting cusp relationship into opposing fossae/marginal ridge areas within the occlusal scheme',
     'explanation': 'Supporting cusps contact opposing fossae/marginal ridges. Assigning that holding contact to guiding/non-supporting cusps is the overlapping occlusion near-miss. Shade and pulp chamber height do not set contacts.',
     'choice_explanations': {'A': 'Near-miss: guiding cusps are involved in excursions; supporting cusps provide the primary fossa/marginal-ridge holding contacts.', 'B': 'Supporting cusp–fossa/marginal ridge relations guide premolar occlusal adjustment.', 'C': 'Shade selection is esthetic, not cusp–fossa anatomy.', 'D': 'Pulp chamber height does not set occlusal contact points.'}
    },
   ],
   'hard': [
        {
     'question': 'A radiograph of a mandibular second premolar suggests a single root, but the patient has persistent symptoms after apparent one-canal RCT. Clinically the crown has a large lingual cusp almost equal to the buccal. Which multi-cue anatomic suspicion is strongest?',
     'options': ['A) Assume mandibular second premolars never have anatomic variation', 'B) Diagnose only sinus disease without rechecking the tooth', 'C) Possible second canal/root variation—reassess anatomy with angled radiographs or CBCT and revise treatment', 'D) Conclude the equal lingual cusp proves the tooth is a mandibular first premolar with a single canal only'],
     'answer': 'C) Possible second canal/root variation—reassess anatomy with angled radiographs or CBCT and revise treatment',
     'explanation': 'Persistent symptoms after one-canal RCT in a mandibular premolar with a large lingual cusp suggest missed anatomy. Misidentifying it as a classic single-canal first-premolar pattern is the overlapping morphology near-miss. Assuming no variation or sinus-only diagnosis is wrong.',
     'choice_explanations': {'A': 'Anatomic variation in mandibular premolars is well documented.', 'B': 'Tooth-driven symptoms require dental re-evaluation before attributing solely to sinus disease.', 'C': 'Symptomatic premolars after one-canal RCT need search for missed canal anatomy, especially with suggestive crown form.', 'D': 'Near-miss: a large lingual cusp suggests more complex anatomy, not assurance of a single-canal first-premolar pattern.'}
    },
        {
     'question': 'During extraction planning, a maxillary first molar shows three divergent roots on CBCT with the palatal root into the sinus floor and closely approximated MB/DB roots. Which multi-cue anatomic implication is most important?',
     'options': ['A) Extract intact with heavy buccal force assuming divergence will follow a single path of withdrawal', 'B) Ignore sinus proximity because molars never communicate with the antrum', 'C) Extract via the nasal cavity as the standard first approach', 'D) Plan sectioning to reduce oroantral and root-fracture risk given divergence and sinus proximity'],
     'answer': 'D) Plan sectioning to reduce oroantral and root-fracture risk given divergence and sinus proximity',
     'explanation': 'Divergent sinus-approximating maxillary molar roots favor controlled sectioning. Intact heavy-force delivery along one path is the overlapping extraction near-miss that fractures roots and tears sinus membrane. Denying sinus risk or transnasal extraction is wrong.',
     'choice_explanations': {'A': 'Near-miss: forceps delivery can work for some molars, but marked divergence with sinus intimacy warrants planned sectioning to prevent OAC/root fracture.', 'B': 'Maxillary molar roots commonly approximate the sinus.', 'C': 'Transnasal extraction is not a dental standard approach for molars.', 'D': 'Divergent sinus-approximating maxillary molar roots favor controlled sectioning.'}
    },
        {
     'question': 'A student identifies a tooth with two roots (buccal and lingual), a mesial marginal ridge more cervical than distal, and a large buccal cusp with a nonfunctioning lingual cusp. Which multi-cue identification is most accurate?',
     'options': ['A) Maxillary first premolar', 'B) Mandibular first premolar with a similar dominant buccal cusp but usually one root', 'C) Maxillary central incisor', 'D) Mandibular second molar with five cusps'],
     'answer': 'A) Maxillary first premolar',
     'explanation': 'Two roots (buccal/lingual), cervical mesial marginal ridge, and dominant buccal cusp identify the maxillary first premolar. Mandibular first premolars share a dominant buccal cusp (near-miss) but are usually single-rooted. Centrals and mandibular second molars do not match.',
     'choice_explanations': {'A': 'Two-rooted premolar with dominant buccal cusp and characteristic mesial anatomy = maxillary first premolar.', 'B': 'Near-miss: mandibular first premolars also have a large buccal cusp, but they are typically single-rooted rather than buccal/lingual two-rooted.', 'C': 'Maxillary centrals are single-rooted incisors without buccal/lingual premolar cusps.', 'D': 'Mandibular second molars have molar occlusal schemes, not this premolar root/cusp pattern.'}
    },
   ],
   'extreme': [
        {
     'question': 'An extracted maxillary molar teaching specimen shows three roots, but the MB root has two canal orifices and a fin connecting to a second MB canal that joins near midroot. Clinically this pattern most informs which complex endodontic decision concept on a vital inflamed maxillary first molar?',
     'options': ['A) Assume MB roots never contain more than one canal in first molars', 'B) Access and instrumentation must actively negotiate MB2 anatomy; missing the second mesiobuccal canal is a common cause of persistent disease despite three canals filled', 'C) Obturate only the palatal canal because MB anatomy is irrelevant to symptoms', 'D) Instrument only the main MB canal when a fin is seen, assuming the second orifice always joins and needs no negotiation'],
     'answer': 'B) Access and instrumentation must actively negotiate MB2 anatomy; missing the second mesiobuccal canal is a common cause of persistent disease despite three canals filled',
     'explanation': 'MB2 is common and must be actively negotiated even when fins suggest joining. Assuming a joining fin means no negotiation is the overlapping anatomy near-miss that leaves infected tissue. Ignoring MB canals entirely is wrong.',
     'choice_explanations': {'A': 'MB2 prevalence is high; assuming a single MB canal is a classic error.', 'B': 'MB2 is a critical anatomic complexity in maxillary first molars; missing it risks failure.', 'C': 'MB canal infection can maintain symptoms even if the palatal canal is filled.', 'D': 'Near-miss: MB2 may join the MB1, but it still requires location and instrumentation; fins do not justify ignoring the second orifice.'}
    },
        {
     'question': 'A trauma case shows a horizontal root fracture in the apical third of a maxillary central with displaced coronal fragment. Anatomy of the pulp and periodontal ligament attachment informs which complex management differential?',
     'options': ['A) Always perform immediate RCT of both apical and coronal segments through the fracture without repositioning', 'B) Extract immediately every apical-third root fracture without reposition attempt', 'C) Reposition and flexible splint; pulp may survive especially with apical fractures; monitor vitality and consider endodontics of the coronal segment only if necrosis develops', 'D) Reposition and rigidly splint for 4 months, performing elective RCT of the apical segment in all cases'],
     'answer': 'C) Reposition and flexible splint; pulp may survive especially with apical fractures; monitor vitality and consider endodontics of the coronal segment only if necrosis develops',
     'explanation': 'Apical-third root fractures often allow pulp survival after repositioning and short-term flexible splinting; RCT of the coronal segment only if necrosis develops. Rigid long splinting with elective apical RCT is the overlapping trauma near-miss. Immediate both-segment RCT or automatic extraction is wrong.',
     'choice_explanations': {'A': 'Routine immediate RCT of apical and coronal segments is not first-line when pulp may recover.', 'B': 'Many apical-third fractures can be saved with repositioning/splinting.', 'C': 'Reposition, flexible splint, monitor; RCT coronal segment only if necrosis occurs.', 'D': 'Near-miss: repositioning is correct, but prolonged rigid fixation and elective apical-segment RCT are not standard first-line for apical-third fractures.'}
    },
        {
     'question': 'In planning a surgical endodontic approach to a palatal root of a maxillary first molar, the surgeon notes on CBCT that the root apex is enveloped by sinus membrane and a large greater palatine vessel canal is nearby. Which anatomy-driven complication plan is most appropriate?',
     'options': ['A) Curette aggressively through the sinus and greater palatine canal without planning', 'B) Assume palatal roots never relate to the maxillary sinus', 'C) Use a standard buccal-only approach and guarantee easy access to every palatal apex', 'D) Modify flap design and apex location strategy to avoid sinus perforation and vascular injury; consider intentional replantation or orthograde options if surgical risk outweighs benefit'],
     'answer': 'D) Modify flap design and apex location strategy to avoid sinus perforation and vascular injury; consider intentional replantation or orthograde options if surgical risk outweighs benefit',
     'explanation': 'Sinus-enveloped palatal apices near greater palatine vessels need modified surgical planning or alternative approaches. Guaranteeing buccal access to every palatal apex is the overlapping surgical near-miss. Aggressive curettage or denying sinus relationships is dangerous.',
     'choice_explanations': {'A': 'Aggressive sinus/vessel violation risks hemorrhage and oroantral complications.', 'B': 'Palatal roots commonly approximate or enter the sinus.', 'C': 'Near-miss: buccal surgery is common for some roots but frequently provides poor direct access to palatal apices—planning must account for that.', 'D': 'Sinus- and vessel-aware planning may lead to altered surgery or alternative treatment for palatal apices.'}
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


# Load expanded MCQ banks (100 unique questions per specialty) when available.
from pathlib import Path as _BankPath
import sys as _sys

_bank_root = _BankPath(__file__).resolve().parent
if str(_bank_root) not in _sys.path:
    _sys.path.insert(0, str(_bank_root))
if str(_bank_root.parent) not in _sys.path:
    _sys.path.insert(0, str(_bank_root.parent))
from bank_loader import apply_question_banks

apply_question_banks(SPECIALTIES, _bank_root / "question_banks")



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
