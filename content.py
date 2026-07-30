"""Undergraduate medicine study content organized by specialty and difficulty."""
from __future__ import annotations

import random

from quiz_bank import DIFFICULTIES, DIFFICULTY_LABELS, LABEL_TO_DIFFICULTY

SPECIALTY_ORDER = ['cardiology', 'ophthalmology', 'urology', 'neurology', 'pulmonology', 'gastroenterology', 'endocrinology', 'nephrology', 'orthopedics', 'dermatology', 'obgyn', 'pediatrics']

SPECIALTIES: dict[str, dict] = {'cardiology': {'label': 'Cardiology',
                'books': ["Braunwald's Heart Disease",
                          "Harrison's Principles of Internal Medicine — Cardiology",
                          'ECG Made Easy — John Hampton'],
                'pdf_notes': ['ACS spectrum: unstable angina, NSTEMI, STEMI — treat as '
                              'time-critical.',
                              'STEMI: ST elevation in contiguous leads ± new LBBB; '
                              'urgent reperfusion.',
                              'HF signs: orthopnea, raised JVP, crackles, edema; '
                              'confirm with BNP/echo.',
                              'MR = holosystolic to axilla; AS = crescendo-decrescendo '
                              'to carotids.',
                              'Secondary prevention after MI: antiplatelet, statin, '
                              'beta-blocker, ACEi as indicated.'],
                'questions': {'easy': [{'question': 'What does ECG primarily record?',
                                        'options': ['A) Electrical activity of the '
                                                    'heart',
                                                    'B) Mechanical contractility of '
                                                    'the ventricles',
                                                    'C) Coronary artery blood flow '
                                                    'velocity',
                                                    'D) Central venous pressure '
                                                    'waveform'],
                                        'answer': 'A) Electrical activity of the heart',
                                        'explanation': 'The electrocardiogram records '
                                                       'summed electrical potentials '
                                                       'from atrial and ventricular '
                                                       'myocytes as depolarization and '
                                                       'repolarization sweep across '
                                                       'the heart. Surface electrodes '
                                                       'display these voltage changes '
                                                       'as P, QRS, and T waves over '
                                                       'time. It does not directly '
                                                       'measure contractility, '
                                                       'coronary flow, or filling '
                                                       'pressures.',
                                        'choice_explanations': {
                                            'A': 'Surface ECG electrodes record summed '
                                                  'atrial and ventricular myocyte '
                                                  'depolarization and repolarization '
                                                  'voltages, displayed as P, QRS, and T '
                                                  'waves over time.',
                                            'B': 'Ventricular mechanical contractility '
                                                  'is the force of myocardial fiber '
                                                  'shortening that generates stroke '
                                                  'volume; it is assessed by '
                                                  'echocardiography or hemodynamics, '
                                                  'not by the ECG voltage tracing.',
                                            'C': 'Coronary blood-flow velocity is a '
                                                  'hemodynamic measure of blood moving '
                                                  'through epicardial arteries (Doppler '
                                                  'or angiography), whereas ECG records '
                                                  'only electrical potentials.',
                                            'D': 'Central venous pressure waveforms '
                                                  'reflect right-atrial filling '
                                                  'pressure from venous catheters and '
                                                  'are unrelated to the surface '
                                                  'electrical signals that constitute '
                                                  'an ECG.'
                                        }},
                                       {'question': 'Typical symptom of angina is?',
                                        'options': ['A) Pleuritic pain worse when '
                                                    'lying flat only',
                                                    'B) Retrosternal chest discomfort '
                                                    'provoked by exertion',
                                                    'C) Sharp chest pain reproduced by '
                                                    'chest-wall palpation',
                                                    'D) Burning epigastric pain '
                                                    'relieved solely by antacids'],
                                        'answer': 'B) Retrosternal chest discomfort '
                                                  'provoked by exertion',
                                        'explanation': 'Angina reflects myocardial '
                                                       'ischemia when coronary oxygen '
                                                       'supply cannot meet demand, '
                                                       'typically during exertion or '
                                                       'stress. Patients describe '
                                                       'retrosternal pressure or '
                                                       'tightness that may radiate to '
                                                       'the arm, neck, or jaw and '
                                                       'eases with rest or nitrates. '
                                                       'Musculoskeletal, purely '
                                                       'pleuritic, or isolated reflux '
                                                       'pain patterns point away from '
                                                       'classic ischemic angina.',
                                        'choice_explanations': {
                                            'A': 'Pleuritic pain worse when supine is '
                                                  'typical of pericarditis, which '
                                                  'inflames the pericardium and worsens '
                                                  'with inspiration or recumbency, not '
                                                  'supply–demand myocardial ischemia.',
                                            'B': 'Angina is transient myocardial '
                                                  'ischemia when coronary oxygen supply '
                                                  'cannot meet demand; it classically '
                                                  'causes retrosternal pressure or '
                                                  'tightness provoked by exertion and '
                                                  'relieved by rest or nitrates.',
                                            'C': 'Sharp pain reproduced by chest-wall '
                                                  'palpation indicates musculoskeletal '
                                                  'chest-wall pain, not ischemic '
                                                  'myocardial demand mismatch.',
                                            'D': 'Burning epigastric pain relieved only '
                                                  'by antacids points to acid-related '
                                                  'dyspepsia or reflux, a '
                                                  'gastrointestinal mechanism distinct '
                                                  'from coronary ischemia.'
                                        }},
                                       {'question': 'Aspirin in ACS is given mainly '
                                                    'to?',
                                        'options': ['A) Acute coronary vasodilation '
                                                    'via nitric oxide',
                                                    'B) Reduction of myocardial oxygen '
                                                    'demand via beta-blockade',
                                                    'C) Irreversible inhibition of '
                                                    'platelet aggregation',
                                                    'D) Dissolution of fibrin within '
                                                    'established thrombus'],
                                        'answer': 'C) Irreversible inhibition of '
                                                  'platelet aggregation',
                                        'explanation': 'In ACS, platelet activation at '
                                                       'a ruptured plaque drives '
                                                       'thrombus growth. Aspirin '
                                                       'irreversibly acetylates '
                                                       'platelet COX-1, blocking '
                                                       'thromboxane A2 synthesis and '
                                                       'reducing further aggregation. '
                                                       'Vasodilation, beta-blockade, '
                                                       'and fibrinolysis are separate '
                                                       'therapeutic mechanisms used in '
                                                       'other contexts.',
                                        'choice_explanations': {
                                            'A': 'Nitric oxide–mediated coronary '
                                                  'vasodilation is the mechanism of '
                                                  'nitrates, not aspirin, which acts on '
                                                  'platelet cyclooxygenase rather than '
                                                  'vascular smooth-muscle NO signaling.',
                                            'B': 'Beta-blockers reduce myocardial '
                                                  'oxygen demand by lowering heart rate '
                                                  'and contractility; aspirin does not '
                                                  'provide beta-adrenergic blockade.',
                                            'C': 'Aspirin irreversibly acetylates '
                                                  'platelet COX-1, blocking thromboxane '
                                                  'A2 synthesis and thereby reducing '
                                                  'further platelet aggregation on a '
                                                  'ruptured plaque in ACS.',
                                            'D': 'Fibrinolysis dissolves fibrin within '
                                                  'established thrombus and is the '
                                                  'action of plasminogen activators, '
                                                  'not of aspirin’s antiplatelet '
                                                  'effect.'
                                        }}],
                              'medium': [{'question': 'ST elevation in leads II, III, '
                                                      'and aVF most suggests occlusion '
                                                      'in which territory?',
                                          'options': ['A) Anterior wall (commonly LAD)',
                                                      'B) Lateral wall (commonly LCx)',
                                                      'C) Right ventricular free wall '
                                                      'alone without inferior '
                                                      'involvement',
                                                      'D) Inferior wall (commonly '
                                                      'RCA)'],
                                          'answer': 'D) Inferior wall (commonly RCA)',
                                          'explanation': 'Leads II, III, and aVF view '
                                                         'the inferior '
                                                         'left-ventricular wall, '
                                                         'usually supplied by the '
                                                         'right coronary artery (or a '
                                                         'dominant circumflex). ST '
                                                         'elevation in these '
                                                         'contiguous leads localizes '
                                                         'transmural ischemia to the '
                                                         'inferior territory. Anterior '
                                                         'STEMI involves precordial '
                                                         'leads; isolated lateral '
                                                         'changes map to LCx '
                                                         'territory.',
                                          'choice_explanations': {
                                              'A': 'Anterior-wall STEMI typically shows '
                                                    'ST elevation in precordial leads '
                                                    '(V1–V4) from LAD territory '
                                                    'ischemia, not in the inferior '
                                                    'leads II, III, and aVF.',
                                              'B': 'Lateral-wall ischemia (often LCx) '
                                                    'localizes to leads I, aVL, and/or '
                                                    'V5–V6 rather than the inferior '
                                                    'lead group II, III, and aVF.',
                                              'C': 'Isolated right-ventricular '
                                                    'infarction may accompany inferior '
                                                    'STEMI but is diagnosed with '
                                                    'right-sided leads (e.g., V4R); ST '
                                                    'elevation confined to II, III, and '
                                                    'aVF indicates inferior LV wall '
                                                    'involvement.',
                                              'D': 'Leads II, III, and aVF view the '
                                                    'inferior left-ventricular wall, '
                                                    'usually supplied by the RCA (or a '
                                                    'dominant circumflex), so ST '
                                                    'elevation there localizes '
                                                    'transmural ischemia to the '
                                                    'inferior territory.'
                                          }},
                                         {'question': 'Which murmur is holosystolic '
                                                      'and radiates to the axilla?',
                                          'options': ['A) Mitral regurgitation',
                                                      'B) Aortic stenosis',
                                                      'C) Mitral stenosis',
                                                      'D) Aortic regurgitation'],
                                          'answer': 'A) Mitral regurgitation',
                                          'explanation': 'Mitral regurgitation '
                                                         'produces a high-velocity '
                                                         'systolic jet from LV to LA '
                                                         'throughout systole, yielding '
                                                         'a holosystolic murmur that '
                                                         'radiates to the axilla. '
                                                         'Aortic stenosis is a '
                                                         'crescendo-decrescendo '
                                                         'systolic murmur to the '
                                                         'carotids; mitral stenosis is '
                                                         'diastolic; aortic '
                                                         'regurgitation is an early '
                                                         'diastolic decrescendo '
                                                         'murmur.',
                                          'choice_explanations': {
                                              'A': 'Mitral regurgitation produces a '
                                                    'high-velocity LV-to-LA systolic '
                                                    'jet throughout systole, yielding a '
                                                    'holosystolic murmur that radiates '
                                                    'to the axilla along the '
                                                    'regurgitant jet.',
                                              'B': 'Aortic stenosis generates a '
                                                    'crescendo–decrescendo systolic '
                                                    'ejection murmur that radiates to '
                                                    'the carotids, not a holosystolic '
                                                    'apical-to-axilla murmur.',
                                              'C': 'Mitral stenosis produces a '
                                                    'low-pitched diastolic rumble after '
                                                    'an opening snap as blood flows '
                                                    'across a narrowed mitral orifice '
                                                    'in diastole, not a holosystolic '
                                                    'murmur.',
                                              'D': 'Aortic regurgitation is an early '
                                                    'diastolic decrescendo murmur from '
                                                    'aortic-to-LV runoff after aortic '
                                                    'valve closure, not a holosystolic '
                                                    'murmur.'
                                          }},
                                         {'question': 'First-line symptom relief for '
                                                      'an acute angina episode is '
                                                      'often?',
                                          'options': ['A) Intravenous digoxin loading',
                                                      'B) Sublingual nitroglycerin',
                                                      'C) Immediate IV amiodarone '
                                                      'bolus',
                                                      'D) High-dose systemic '
                                                      'corticosteroid'],
                                          'answer': 'B) Sublingual nitroglycerin',
                                          'explanation': 'Sublingual nitroglycerin is '
                                                         'rapidly absorbed and '
                                                         'releases nitric oxide, '
                                                         'dilating veins (reducing '
                                                         'preload) and coronary '
                                                         'arteries. Lower wall tension '
                                                         'decreases myocardial oxygen '
                                                         'demand and often relieves an '
                                                         'acute angina episode within '
                                                         'minutes. Digoxin, '
                                                         'amiodarone, and steroids are '
                                                         'not first-line acute '
                                                         'anti-anginal relief.',
                                          'choice_explanations': {
                                              'A': 'Digoxin increases inotropy and can '
                                                    'control ventricular rate in AF, '
                                                    'but it is not rapid first-line '
                                                    'therapy for an acute anginal '
                                                    'episode driven by supply–demand '
                                                    'mismatch.',
                                              'B': 'Sublingual nitroglycerin is rapidly '
                                                    'absorbed and releases nitric '
                                                    'oxide, dilating veins (reducing '
                                                    'preload) and coronaries, which '
                                                    'lowers wall tension and often '
                                                    'relieves acute angina within '
                                                    'minutes.',
                                              'C': 'IV amiodarone is an antiarrhythmic '
                                                    'used for ventricular or atrial '
                                                    'tachyarrhythmias, not first-line '
                                                    'acute anti-anginal symptom relief.',
                                              'D': 'Systemic corticosteroids treat '
                                                    'inflammatory or adrenal conditions '
                                                    'and have no role as acute coronary '
                                                    'vasodilator or anti-ischemic '
                                                    'relief in angina.'
                                          }}],
                              'hard': [{'question': 'A patient with inferior STEMI '
                                                    'becomes hypotensive after '
                                                    'nitrates and has elevated JVP '
                                                    'with clear lungs. Which '
                                                    'associated process should you '
                                                    'suspect?',
                                        'options': ['A) Isolated left ventricular '
                                                    'apical aneurysm',
                                                    'B) Acute severe mitral stenosis',
                                                    'C) Right ventricular infarction',
                                                    'D) Primary hypertensive pulmonary '
                                                    'edema without RV involvement'],
                                        'answer': 'C) Right ventricular infarction',
                                        'explanation': 'The RV is often co-infarcted '
                                                       'with inferior STEMI because '
                                                       'both are commonly '
                                                       'RCA-dependent, and RV stroke '
                                                       'volume is highly '
                                                       'preload-dependent. Nitrates '
                                                       'pool venous blood, abruptly '
                                                       'cut RV preload, and cause '
                                                       'hypotension with elevated JVP '
                                                       'and clear lungs. This pattern '
                                                       'should prompt RV infarction '
                                                       'recognition and cautious fluid '
                                                       'resuscitation rather than '
                                                       'further preload reduction.',
                                        'choice_explanations': {
                                            'A': 'An apical LV aneurysm complicates '
                                                  'some anterior infarcts and may cause '
                                                  'heart failure or thrombus, but it '
                                                  'does not produce nitrate-triggered '
                                                  'hypotension with clear lungs and '
                                                  'elevated JVP.',
                                            'B': 'Acute severe mitral stenosis causes '
                                                  'diastolic obstruction to LV filling '
                                                  'with pulmonary congestion, not the '
                                                  'clear-lung, high-JVP, '
                                                  'preload-sensitive hypotension of RV '
                                                  'infarction.',
                                            'C': 'Inferior STEMI often co-infarcts the '
                                                  'RV (RCA territory); RV stroke volume '
                                                  'is preload-dependent, so nitrates '
                                                  'abruptly cut preload and cause '
                                                  'hypotension with elevated JVP and '
                                                  'clear lungs.',
                                            'D': 'Hypertensive pulmonary edema is '
                                                  'left-sided failure with wet lungs '
                                                  'and high afterload; it does not '
                                                  'match clear lungs plus '
                                                  'nitrate-induced hypotension from RV '
                                                  'preload dependence.'
                                        }},
                                       {'question': 'Which heart-failure therapy class '
                                                    'has strong mortality benefit in '
                                                    'HFrEF among the listed options?',
                                        'options': ['A) Digoxin monotherapy as sole '
                                                    'disease-modifying therapy',
                                                    'B) Short-acting dihydropyridine '
                                                    'calcium-channel blocker',
                                                    'C) Class Ic antiarrhythmic '
                                                    'started routinely in all HFrEF',
                                                    'D) Evidence-based beta-blocker '
                                                    '(e.g., carvedilol, bisoprolol, '
                                                    'metoprolol succinate)'],
                                        'answer': 'D) Evidence-based beta-blocker '
                                                  '(e.g., carvedilol, bisoprolol, '
                                                  'metoprolol succinate)',
                                        'explanation': 'In HFrEF, sustained '
                                                       'sympathetic activation worsens '
                                                       'remodeling, arrhythmias, and '
                                                       'mortality. Evidence-based '
                                                       'beta-blockers blunt this drive '
                                                       'and reduce mortality when '
                                                       'titrated appropriately. '
                                                       'Digoxin may help symptoms/rate '
                                                       'control but is not sole '
                                                       'mortality therapy; '
                                                       'short-acting nifedipine and '
                                                       'routine class Ic agents can '
                                                       'harm HFrEF patients.',
                                        'choice_explanations': {
                                            'A': 'Digoxin may improve symptoms or rate '
                                                  'control in selected HFrEF/AF '
                                                  'patients but is not sole '
                                                  'disease-modifying mortality therapy '
                                                  'compared with evidence-based '
                                                  'beta-blockers.',
                                            'B': 'Short-acting dihydropyridine '
                                                  'calcium-channel blockers can cause '
                                                  'reflex sympathetic activation and '
                                                  'are not mortality-reducing therapy '
                                                  'in HFrEF.',
                                            'C': 'Class Ic antiarrhythmics are '
                                                  'generally avoided in structural '
                                                  'heart disease/HFrEF because of '
                                                  'proarrhythmia and adverse outcomes, '
                                                  'not used routinely for mortality '
                                                  'benefit.',
                                            'D': 'Evidence-based beta-blockers '
                                                  '(carvedilol, bisoprolol, metoprolol '
                                                  'succinate) blunt sustained '
                                                  'sympathetic drive that worsens '
                                                  'remodeling and arrhythmias, reducing '
                                                  'mortality in HFrEF.'
                                        }},
                                       {'question': 'New LBBB with ischemic symptoms '
                                                    'can be treated as?',
                                        'options': ['A) STEMI equivalent in the '
                                                    'appropriate ischemic clinical '
                                                    'context',
                                                    'B) Benign age-related conduction '
                                                    'change requiring no urgency',
                                                    'C) Definitive '
                                                    'electrocardiographic proof of '
                                                    'pulmonary embolism',
                                                    'D) Isolated indication for '
                                                    'atropine without reperfusion '
                                                    'consideration'],
                                        'answer': 'A) STEMI equivalent in the '
                                                  'appropriate ischemic clinical '
                                                  'context',
                                        'explanation': 'New LBBB can accompany '
                                                       'extensive ischemic injury and '
                                                       'obscures ST-segment '
                                                       'interpretation. When it '
                                                       'appears with ongoing ischemic '
                                                       'symptoms, guidelines treat it '
                                                       'as a STEMI equivalent '
                                                       'warranting urgent reperfusion '
                                                       'assessment. It is not proof of '
                                                       'PE and does not by itself '
                                                       'mandate atropine.',
                                        'choice_explanations': {
                                            'A': 'New LBBB can accompany extensive '
                                                  'ischemic injury and obscures '
                                                  'ST-segment interpretation; with '
                                                  'ongoing ischemic symptoms it is '
                                                  'treated as a STEMI equivalent '
                                                  'warranting urgent reperfusion '
                                                  'assessment.',
                                            'B': 'Age-related conduction disease may be '
                                                  'chronic and incidental, but new LBBB '
                                                  'plus ischemic symptoms is an acute '
                                                  'coronary emergency pathway, not a '
                                                  'benign finding.',
                                            'C': 'Pulmonary embolism may cause '
                                                  'right-heart strain ECG changes, but '
                                                  'new LBBB with ischemic symptoms is '
                                                  'not definitive electrocardiographic '
                                                  'proof of PE.',
                                            'D': 'Atropine treats bradycardia from '
                                                  'excess vagal tone or AV block; new '
                                                  'ischemic LBBB requires reperfusion '
                                                  'consideration rather than atropine '
                                                  'alone.'
                                        }}],
                              'extreme': [{'question': 'A 72-year-old with prior CABG '
                                                       'presents with flash pulmonary '
                                                       'edema, unequal arm BPs, and a '
                                                       'tearing back pain. Troponin is '
                                                       'mildly up; ECG shows '
                                                       'non-specific ST changes. Which '
                                                       'diagnosis must be excluded '
                                                       'before dual antiplatelet '
                                                       'loading and anticoagulation '
                                                       'for presumed NSTE-ACS?',
                                           'options': ['A) Uncomplicated '
                                                       'non–ST-elevation ACS without '
                                                       'vascular complication',
                                                       'B) Acute aortic '
                                                       'syndrome/dissection',
                                                       'C) Isolated takotsubo '
                                                       'cardiomyopathy',
                                                       'D) Type 2 myocardial injury '
                                                       'from sepsis alone'],
                                           'answer': 'B) Acute aortic '
                                                     'syndrome/dissection',
                                           'explanation': 'Acute aortic dissection can '
                                                          'present with severe tearing '
                                                          'back/chest pain, pulse or '
                                                          'BP asymmetry, flash edema, '
                                                          'and secondary troponin '
                                                          'rise, closely mimicking '
                                                          'NSTE-ACS. Dual antiplatelet '
                                                          'therapy and anticoagulation '
                                                          'can catastrophically extend '
                                                          'dissection or delay '
                                                          'surgery. Unequal arm BPs '
                                                          'and tearing pain mandate '
                                                          'exclusion of aortic '
                                                          'syndrome first.',
                                           'choice_explanations': {
                                               'A': 'Uncomplicated NSTE-ACS can cause '
                                                     'troponin rise and ST changes, but '
                                                     'unequal arm BPs with tearing back '
                                                     'pain and flash edema mandate '
                                                     'excluding dissection before '
                                                     'antiplatelet/anticoagulant '
                                                     'loading.',
                                               'B': 'Acute aortic dissection can mimic '
                                                     'NSTE-ACS with pain, secondary '
                                                     'troponin rise, and flash edema; '
                                                     'dual antiplatelet therapy and '
                                                     'anticoagulation can extend the '
                                                     'flap, so unequal BPs and tearing '
                                                     'pain require exclusion first.',
                                               'C': 'Takotsubo cardiomyopathy causes '
                                                     'stress-related apical ballooning '
                                                     'and troponin rise without '
                                                     'coronary occlusion, but it does '
                                                     'not produce pulse/BP asymmetry '
                                                     'and tearing back pain of aortic '
                                                     'syndrome.',
                                               'D': 'Type 2 myocardial injury from '
                                                     'sepsis reflects supply–demand '
                                                     'mismatch without plaque rupture; '
                                                     'it lacks the vascular asymmetry '
                                                     'and tearing pain that define '
                                                     'suspected aortic dissection.'
                                           }},
                                          {'question': 'In suspected tamponade after '
                                                       'cardiac surgery, which '
                                                       'constellation is most '
                                                       'suggestive?',
                                           'options': ['A) Hypertension with bounding '
                                                       'pulses and wide pulse pressure',
                                                       'B) Isolated wheeze with normal '
                                                       'blood pressure and clear heart '
                                                       'sounds',
                                                       'C) Hypotension, raised filling '
                                                       'pressures, low '
                                                       'voltage/electrical alternans ± '
                                                       'muffled sounds',
                                                       'D) Fever alone without '
                                                       'hemodynamic or ECG change'],
                                           'answer': 'C) Hypotension, raised filling '
                                                     'pressures, low '
                                                     'voltage/electrical alternans ± '
                                                     'muffled sounds',
                                           'explanation': 'Cardiac tamponade is '
                                                          'obstructive shock: '
                                                          'pericardial fluid impairs '
                                                          'diastolic filling and '
                                                          'stroke volume falls. Clues '
                                                          'include hypotension, '
                                                          'elevated venous pressures, '
                                                          'muffled sounds, low '
                                                          'voltage, and electrical '
                                                          'alternans. Hypertension '
                                                          'with bounding pulses '
                                                          'suggests the opposite '
                                                          'physiology; isolated wheeze '
                                                          'or fever alone do not '
                                                          'define tamponade.',
                                           'choice_explanations': {
                                               'A': 'Hypertension with bounding pulses '
                                                     'and wide pulse pressure suggests '
                                                     'high-output or '
                                                     'aortic-regurgitation physiology, '
                                                     'the opposite of obstructive '
                                                     'filling failure in tamponade.',
                                               'B': 'Isolated wheeze with normal blood '
                                                     'pressure points to airway '
                                                     'disease; tamponade is obstructive '
                                                     'shock from impaired diastolic '
                                                     'filling, not bronchospasm.',
                                               'C': 'Tamponade is obstructive shock: '
                                                     'pericardial fluid impairs '
                                                     'diastolic filling so stroke '
                                                     'volume falls, producing '
                                                     'hypotension, raised venous '
                                                     'pressures, muffled sounds, low '
                                                     'voltage, and electrical '
                                                     'alternans.',
                                               'D': 'Fever alone without hemodynamic '
                                                     'compromise or ECG '
                                                     'voltage/alternans changes does '
                                                     'not indicate pericardial '
                                                     'constraint of filling.'
                                           }},
                                          {'question': 'A patient in AF with WPW '
                                                       'presents with very fast '
                                                       'irregular wide-complex '
                                                       'tachycardia and instability. '
                                                       'Which AV-nodal blocker '
                                                       'strategy is inappropriate?',
                                           'options': ['A) Avoid AV-nodal blockers and '
                                                       'perform synchronized '
                                                       'cardioversion if unstable',
                                                       'B) Proceed to expert-guided '
                                                       'management of '
                                                       'accessory-pathway conduction',
                                                       'C) Use procainamide or shock '
                                                       'pathways preferred over '
                                                       'AV-nodal blockers when stable '
                                                       'enough',
                                                       'D) Give IV verapamil, digoxin, '
                                                       'or adenosine as first-line '
                                                       'AV-nodal blockade'],
                                           'answer': 'D) Give IV verapamil, digoxin, '
                                                     'or adenosine as first-line '
                                                     'AV-nodal blockade',
                                           'explanation': 'In AF with WPW, atrial '
                                                          'impulses can conduct '
                                                          'rapidly over an accessory '
                                                          'pathway. AV-nodal blockers '
                                                          'preferentially block the AV '
                                                          'node and may paradoxically '
                                                          'increase accessory-pathway '
                                                          'conduction, risking VF. '
                                                          'Unstable patients need '
                                                          'immediate synchronized '
                                                          'cardioversion; AV-nodal '
                                                          'blockers are inappropriate '
                                                          'first-line therapy.',
                                           'choice_explanations': {
                                               'A': 'In unstable AF with WPW and very '
                                                     'fast irregular wide-complex '
                                                     'tachycardia, synchronized '
                                                     'cardioversion restores sinus '
                                                     'rhythm without preferentially '
                                                     'blocking the AV node relative to '
                                                     'the accessory pathway.',
                                               'B': 'Expert-guided management of '
                                                     'accessory-pathway–mediated AF '
                                                     'appropriately prioritizes '
                                                     'pathway-safe drugs or '
                                                     'cardioversion rather than '
                                                     'AV-nodal blockade.',
                                               'C': 'Procainamide (or shock) slows '
                                                     'accessory-pathway conduction when '
                                                     'the patient is stable enough for '
                                                     'medical therapy, avoiding '
                                                     'preferential AV-nodal block.',
                                               'D': 'IV verapamil, digoxin, or '
                                                     'adenosine block the AV node and '
                                                     'may paradoxically increase '
                                                     'conduction over the accessory '
                                                     'pathway in AF-WPW, risking '
                                                     'degeneration to VF—so they are '
                                                     'inappropriate first-line therapy.'
                                           }}]},
                'cases': {'easy': [{'title': 'Mild Exertional Chest Tightness',
                                    'stem': 'A 55-year-old man gets central chest '
                                            'tightness when climbing stairs. It eases '
                                            'after 3 minutes of rest. Exam and resting '
                                            'ECG are normal.',
                                    'question': 'Most likely diagnosis?',
                                    'answer': 'Stable angina (exertional myocardial '
                                              'ischemia).',
                                    'discussion': 'Pattern is predictable exertional '
                                                  'pain relieved by rest. Risk-factor '
                                                  'modification and anti-anginal '
                                                  'strategy follow assessment.',
                                    'book_hint': "Harrison's — Ischemic Heart "
                                                 'Disease'}],
                          'medium': [{'title': 'Crushing Pain with Anterior STE',
                                      'stem': 'A 58-year-old diabetic has crushing '
                                              'retrosternal pain for 40 minutes with '
                                              'diaphoresis. ECG shows ST elevation in '
                                              'V2–V4.',
                                      'question': 'Diagnosis and immediate reperfusion '
                                                  'idea?',
                                      'answer': 'Anterior STEMI — urgent PCI (or '
                                                'timely fibrinolysis if PCI '
                                                'unavailable).',
                                      'discussion': 'Anterior STE is typically LAD '
                                                    'territory. Time-critical '
                                                    'reperfusion saves myocardium.',
                                      'book_hint': 'Braunwald — ACS'}],
                          'hard': [{'title': 'Inferior MI then Hypotension',
                                    'stem': 'A 64-year-old with inferior STEMI '
                                            'receives nitroglycerin and becomes '
                                            'hypotensive. JVP is raised, lungs are '
                                            'clear, and right-sided ECG leads show ST '
                                            'elevation.',
                                    'question': 'What complication is most likely and '
                                                'what is a key initial hemodynamic '
                                                'step?',
                                    'answer': 'RV infarction — cautious IV fluids for '
                                              'preload (avoid nitrates/diuretics that '
                                              'drop preload).',
                                    'discussion': 'RV depends on preload; vasodilators '
                                                  'can cause profound hypotension. '
                                                  'Reperfusion remains essential.',
                                    'book_hint': 'Braunwald — RV infarction'}],
                          'extreme': [{'title': 'ACS Mimic with Pulse Deficit',
                                       'stem': 'A 68-year-old hypertensive man has '
                                               'sudden severe tearing chest pain '
                                               'radiating to the back, a pulse deficit '
                                               'between arms, and a new soft aortic '
                                               'regurgitation murmur. Troponin is '
                                               'borderline; ECG is non-diagnostic. The '
                                               'team is about to load dual '
                                               'antiplatelets for NSTE-ACS.',
                                       'question': 'What should you do first '
                                                   'conceptually?',
                                       'answer': 'Stop ACS '
                                                 'anticoagulation/antiplatelet pathway '
                                                 'and urgently evaluate for aortic '
                                                 'dissection (CT angiography if '
                                                 'stable).',
                                       'discussion': 'Dissection can cause coronary '
                                                     'ostial compromise and AR. Wrong '
                                                     'therapy worsens outcomes. '
                                                     'Stabilize BP and get definitive '
                                                     'imaging.',
                                       'book_hint': "Braunwald / Harrison's — Aortic "
                                                    'dissection'}]}},
 'ophthalmology': {'label': 'Ophthalmology',
                   'books': ["Kanski's Clinical Ophthalmology",
                             "Vaughan & Asbury's General Ophthalmology",
                             "Clinical Ophthalmology — Parsons' "],
                   'pdf_notes': ['Red eye emergencies: angle-closure glaucoma, '
                                 'keratitis, uveitis, endophthalmitis.',
                                 'RAPD: swinging flashlight test — optic nerve / '
                                 'severe retinal disease.',
                                 'Diabetic retinopathy: microaneurysms, hemorrhages, '
                                 'exudates ± neovascularization.',
                                 "CN III palsy: eye 'down and out'; CN VI: failed "
                                 'abduction.',
                                 'Cataract: reversible surgically; AMD: irreversible '
                                 'central loss if advanced.'],
                   'questions': {'easy': [{'question': 'What test checks for RAPD?',
                                           'options': ['A) Swinging flashlight test',
                                                       'B) Cover-uncover test for '
                                                       'tropia',
                                                       'C) Schirmer test for tear '
                                                       'production',
                                                       'D) Amsler grid for macular '
                                                       'distortion'],
                                           'answer': 'A) Swinging flashlight test',
                                           'explanation': 'An RAPD indicates '
                                                          'asymmetric afferent input '
                                                          'to the pupillary light '
                                                          'reflex, usually from '
                                                          'optic-nerve or severe '
                                                          'retinal disease. In the '
                                                          'swinging flashlight test, '
                                                          'light moved from the good '
                                                          'eye to the affected eye '
                                                          'causes paradoxical '
                                                          'dilation. Cover testing, '
                                                          'Schirmer, and Amsler assess '
                                                          'alignment, tears, and '
                                                          'macula—not RAPD.',
                                           'choice_explanations': {
                                               'A': 'The swinging flashlight test '
                                                     'compares consensual and direct '
                                                     'pupillary responses; paradoxical '
                                                     'dilation when light swings to the '
                                                     'affected eye demonstrates a '
                                                     'relative afferent pupillary '
                                                     'defect.',
                                               'B': 'The cover–uncover test detects '
                                                     'tropias by observing refixation '
                                                     'when one eye is covered, '
                                                     'assessing ocular alignment rather '
                                                     'than afferent pupillary input.',
                                               'C': 'Schirmer testing measures aqueous '
                                                     'tear production with filter-paper '
                                                     'wetting and does not evaluate the '
                                                     'afferent limb of the pupillary '
                                                     'light reflex.',
                                               'D': 'An Amsler grid screens central '
                                                     'macular distortion '
                                                     '(metamorphopsia) and scotomas, '
                                                     'not asymmetry of the pupillary '
                                                     'light reflex.'
                                           }},
                                          {'question': 'Painful red eye with '
                                                       'mid-dilated pupil suggests?',
                                           'options': ['A) Viral conjunctivitis',
                                                       'B) Acute angle-closure '
                                                       'glaucoma',
                                                       'C) Anterior uveitis (iritis)',
                                                       'D) Bacterial keratitis'],
                                           'answer': 'B) Acute angle-closure glaucoma',
                                           'explanation': 'Acute angle-closure occurs '
                                                          'when the peripheral iris '
                                                          'blocks the trabecular '
                                                          'meshwork, abruptly raising '
                                                          'IOP. High pressure produces '
                                                          'a painful red eye, corneal '
                                                          'edema, and a mid-dilated, '
                                                          'poorly reactive pupil. '
                                                          'Conjunctivitis usually has '
                                                          'a normal pupil; uveitis '
                                                          'often has a small pupil; '
                                                          'keratitis features a focal '
                                                          'corneal infiltrate.',
                                           'choice_explanations': {
                                               'A': 'Viral conjunctivitis causes '
                                                     'injected conjunctiva with '
                                                     'discharge but a normal pupil and '
                                                     'usually without the severe pain '
                                                     'and corneal edema of acute angle '
                                                     'closure.',
                                               'B': 'Acute angle-closure occurs when '
                                                     'the peripheral iris blocks the '
                                                     'trabecular meshwork, abruptly '
                                                     'raising IOP and producing a '
                                                     'painful red eye with corneal '
                                                     'edema and a mid-dilated, poorly '
                                                     'reactive pupil.',
                                               'C': 'Anterior uveitis typically '
                                                     'features ciliary flush and a '
                                                     'small, sometimes irregular pupil '
                                                     'from spasm or synechiae, not a '
                                                     'mid-dilated fixed pupil from '
                                                     'acutely high IOP.',
                                               'D': 'Bacterial keratitis presents with '
                                                     'a focal corneal infiltrate and '
                                                     'epithelial defect; the pupil is '
                                                     'not characteristically '
                                                     'mid-dilated from angle closure.'
                                           }},
                                          {'question': 'CN VI palsy mainly impairs?',
                                           'options': ['A) Adduction of the eye',
                                                       'B) Elevation in abduction '
                                                       '(superior rectus primary '
                                                       'action)',
                                                       'C) Abduction of the eye',
                                                       'D) Depression in adduction '
                                                       '(superior oblique primary '
                                                       'action)'],
                                           'answer': 'C) Abduction of the eye',
                                           'explanation': 'CN VI (abducens) innervates '
                                                          'only the lateral rectus, '
                                                          'which abducts the eye. '
                                                          'Palsy causes impaired '
                                                          'abduction and horizontal '
                                                          'diplopia worse on looking '
                                                          'toward the affected side. '
                                                          'Adduction is mediated by '
                                                          'medial rectus (CN III); '
                                                          'vertical actions map to '
                                                          'other extraocular '
                                                          'muscles.',
                                           'choice_explanations': {
                                               'A': 'Adduction is performed by the '
                                                     'medial rectus, innervated by CN '
                                                     'III; CN VI palsy does not '
                                                     'primarily impair adduction.',
                                               'B': 'Elevation in abduction is the '
                                                     'primary action of superior rectus '
                                                     '(CN III), not of the '
                                                     'abducens-innervated lateral '
                                                     'rectus.',
                                               'C': 'CN VI (abducens) innervates only '
                                                     'the lateral rectus, whose primary '
                                                     'action is abduction; palsy '
                                                     'therefore impairs abduction and '
                                                     'causes horizontal diplopia toward '
                                                     'the affected side.',
                                               'D': 'Depression in adduction is the '
                                                     'primary action of the superior '
                                                     'oblique (CN IV), not CN VI.'
                                           }}],
                                 'medium': [{'question': 'Diabetic retinopathy '
                                                         'microaneurysms are seen on?',
                                             'options': ['A) Slit-lamp exam of the '
                                                         'anterior chamber alone',
                                                         'B) Tonometry for intraocular '
                                                         'pressure alone',
                                                         'C) Color vision testing '
                                                         'alone',
                                                         'D) Dilated fundoscopy / '
                                                         'retinal examination'],
                                             'answer': 'D) Dilated fundoscopy / '
                                                       'retinal examination',
                                             'explanation': 'Diabetic retinopathy '
                                                            'begins with retinal '
                                                            'microvascular damage '
                                                            'forming microaneurysms, '
                                                            'hemorrhages, and '
                                                            'exudates. These lesions '
                                                            'are visualized by dilated '
                                                            'fundoscopy or retinal '
                                                            'imaging. Anterior-segment '
                                                            'slit-lamp exam, IOP '
                                                            'measurement, and color '
                                                            'testing do not '
                                                            'demonstrate '
                                                            'microaneurysms.',
                                             'choice_explanations': {
                                                 'A': 'Slit-lamp examination of the '
                                                       'anterior chamber assesses '
                                                       'cornea, iris, and aqueous; '
                                                       'diabetic microaneurysms lie in '
                                                       'the retinal microvasculature '
                                                       'and are not seen there.',
                                                 'B': 'Tonometry measures intraocular '
                                                       'pressure and does not visualize '
                                                       'retinal microaneurysms of '
                                                       'diabetic retinopathy.',
                                                 'C': 'Color vision testing assesses '
                                                       'cone function and optic-nerve '
                                                       'pathways but cannot display '
                                                       'retinal microaneurysms.',
                                                 'D': 'Diabetic microaneurysms arise '
                                                       'from retinal capillary wall '
                                                       'damage and are visualized on '
                                                       'dilated fundoscopy or retinal '
                                                       'imaging of the posterior '
                                                       'segment.'
                                             }},
                                            {'question': 'Sudden curtain-like field '
                                                         'loss suggests?',
                                             'options': ['A) Rhegmatogenous retinal '
                                                         'detachment until proven '
                                                         'otherwise',
                                                         'B) Central retinal vein '
                                                         'occlusion',
                                                         'C) Non-arteritic ischemic '
                                                         'optic neuropathy',
                                                         'D) Vitreous hemorrhage from '
                                                         'proliferative diabetic '
                                                         'retinopathy'],
                                             'answer': 'A) Rhegmatogenous retinal '
                                                       'detachment until proven '
                                                       'otherwise',
                                             'explanation': 'Rhegmatogenous detachment '
                                                            'separates neurosensory '
                                                            'retina from RPE; patients '
                                                            'often describe '
                                                            'photopsias, floaters, '
                                                            'then curtain-like field '
                                                            'loss. CRVO causes sudden '
                                                            'blurred vision with '
                                                            'retinal hemorrhages; '
                                                            'NAION causes altitudinal '
                                                            'field loss with disc '
                                                            'edema; vitreous '
                                                            'hemorrhage causes sudden '
                                                            'floaters/haze without a '
                                                            'progressive curtain of '
                                                            'detached retina.',
                                             'choice_explanations': {
                                                 'A': 'Rhegmatogenous detachment '
                                                       'separates neurosensory retina '
                                                       'from RPE after a tear; patients '
                                                       'often note photopsias and '
                                                       'floaters followed by '
                                                       'progressive curtain-like field '
                                                       'loss.',
                                                 'B': 'Central retinal vein occlusion '
                                                       'causes sudden blurred vision '
                                                       'with retinal hemorrhages and '
                                                       'venous dilation, not a '
                                                       'progressive curtain of detached '
                                                       'retina.',
                                                 'C': 'Non-arteritic ischemic optic '
                                                       'neuropathy typically produces '
                                                       'altitudinal field loss with '
                                                       'disc edema, a different '
                                                       'mechanism from retinal '
                                                       'detachment.',
                                                 'D': 'Vitreous hemorrhage causes '
                                                       'sudden floaters or haze from '
                                                       'blood in the vitreous cavity '
                                                       'without the progressive '
                                                       'peripheral curtain of a '
                                                       'detaching retina.'
                                             }},
                                            {'question': 'Orbital cellulitis vs '
                                                         'preseptal key worrying '
                                                         'features include?',
                                             'options': ['A) Isolated eyelid erythema '
                                                         'without motility or vision '
                                                         'change',
                                                         'B) Painful ophthalmoplegia, '
                                                         'proptosis, and vision change',
                                                         'C) Mild conjunctival '
                                                         'injection with clear cornea '
                                                         'and full motility',
                                                         'D) Unilateral lid swelling '
                                                         'that is painless and '
                                                         'non-tender'],
                                             'answer': 'B) Painful ophthalmoplegia, '
                                                       'proptosis, and vision change',
                                             'explanation': 'Orbital cellulitis '
                                                            'involves tissues '
                                                            'posterior to the septum, '
                                                            'often from ethmoid sinus '
                                                            'disease. Painful eye '
                                                            'movements, proptosis, and '
                                                            'vision change indicate '
                                                            'orbital involvement and '
                                                            'risk of cavernous sinus '
                                                            'or optic-nerve '
                                                            'compromise. Preseptal '
                                                            'cellulitis is limited to '
                                                            'the lid without orbital '
                                                            'signs.',
                                             'choice_explanations': {
                                                 'A': 'Isolated eyelid erythema without '
                                                       'motility or vision change is '
                                                       'consistent with preseptal '
                                                       'cellulitis limited to tissues '
                                                       'anterior to the orbital septum.',
                                                 'B': 'Orbital cellulitis involves '
                                                       'post-septal tissues; painful '
                                                       'ophthalmoplegia, proptosis, and '
                                                       'vision change indicate orbital '
                                                       'involvement with risk to the '
                                                       'optic nerve and cavernous '
                                                       'sinus.',
                                                 'C': 'Mild conjunctival injection with '
                                                       'clear cornea and full motility '
                                                       'reflects surface inflammation '
                                                       'without orbital soft-tissue '
                                                       'infection.',
                                                 'D': 'Painless non-tender unilateral '
                                                       'lid swelling lacks the '
                                                       'inflammatory orbital signs that '
                                                       'define orbital cellulitis.'
                                             }}],
                                 'hard': [{'question': 'A relative afferent pupillary '
                                                       'defect with normal fundoscopy '
                                                       'early on most suggests?',
                                           'options': ['A) Uncomplicated early nuclear '
                                                       'lens opacity without afferent '
                                                       'defect',
                                                       'B) Uncorrected refractive '
                                                       'error alone',
                                                       'C) Optic neuropathy (e.g., '
                                                       'optic neuritis or ischemic '
                                                       'optic neuropathy)',
                                                       'D) Mild dry-eye disease '
                                                       'without optic-nerve '
                                                       'involvement'],
                                           'answer': 'C) Optic neuropathy (e.g., optic '
                                                     'neuritis or ischemic optic '
                                                     'neuropathy)',
                                           'explanation': 'An RAPD means the afferent '
                                                          'limb of the pupillary light '
                                                          'reflex is weaker in one '
                                                          'eye. When the fundus still '
                                                          'looks normal, the lesion is '
                                                          'usually in the optic nerve '
                                                          '(neuritis, ischemic '
                                                          'neuropathy). Cataract, '
                                                          'refractive error, and dry '
                                                          'eye do not produce a true '
                                                          'RAPD.',
                                           'choice_explanations': {
                                               'A': 'Early nuclear cataract reduces '
                                                     'acuity by lens opacity but does '
                                                     'not asymmetrically impair the '
                                                     'afferent pupillary light reflex, '
                                                     'so it does not produce a true '
                                                     'RAPD.',
                                               'B': 'Uncorrected refractive error blurs '
                                                     'vision without damaging the optic '
                                                     'nerve or retina enough to create '
                                                     'an RAPD.',
                                               'C': 'An RAPD with a still-normal fundus '
                                                     'indicates weakened afferent '
                                                     'pupillary input, most often from '
                                                     'optic neuropathy such as optic '
                                                     'neuritis or ischemic optic '
                                                     'neuropathy.',
                                               'D': 'Mild dry-eye disease affects the '
                                                     'ocular surface tear film and does '
                                                     'not interrupt optic-nerve '
                                                     'afferent signaling to produce an '
                                                     'RAPD.'
                                           }},
                                          {'question': 'Painful third-nerve palsy '
                                                       'involving the pupil is '
                                                       'concerning for?',
                                           'options': ['A) Isolated microvascular '
                                                       'ischemic CN III palsy with '
                                                       'spared pupil',
                                                       'B) Myasthenia gravis '
                                                       'presenting as fatigable ptosis '
                                                       'alone',
                                                       'C) Horner syndrome from '
                                                       'sympathetic pathway '
                                                       'interruption',
                                                       'D) Posterior communicating '
                                                       'artery aneurysm compression '
                                                       'until excluded'],
                                           'answer': 'D) Posterior communicating '
                                                     'artery aneurysm compression '
                                                     'until excluded',
                                           'explanation': 'Parasympathetic '
                                                          'pupilloconstrictor fibers '
                                                          'travel superficially on CN '
                                                          'III and are compressed '
                                                          'early by a PCOM aneurysm. '
                                                          'Pupil-involving, painful '
                                                          'third-nerve palsy is a '
                                                          'neurosurgical emergency '
                                                          'until aneurysm is excluded. '
                                                          'Pupil-sparing microvascular '
                                                          'palsy, myasthenia, and '
                                                          'Horner syndrome have '
                                                          'different mechanisms and '
                                                          'pupil patterns.',
                                           'choice_explanations': {
                                               'A': 'Isolated microvascular ischemic CN '
                                                     'III palsy typically spares the '
                                                     'pupil because the superficial '
                                                     'parasympathetic fibers are less '
                                                     'affected; pupil involvement '
                                                     'argues against this benign '
                                                     'pattern.',
                                               'B': 'Myasthenia gravis causes fatigable '
                                                     'neuromuscular weakness with '
                                                     'pupils that remain reactive; it '
                                                     'does not compress CN III '
                                                     'parasympathetic fibers.',
                                               'C': 'Horner syndrome is '
                                                     'oculosympathetic interruption '
                                                     'causing miosis, ptosis, and '
                                                     'anhidrosis, not a dilated pupil '
                                                     'from CN III parasympathetic '
                                                     'failure.',
                                               'D': 'Parasympathetic pupilloconstrictor '
                                                     'fibers travel superficially on CN '
                                                     'III and are compressed early by a '
                                                     'posterior communicating artery '
                                                     'aneurysm, so painful '
                                                     'pupil-involving third-nerve palsy '
                                                     'requires aneurysm exclusion.'
                                           }},
                                          {'question': 'Central retinal artery '
                                                       'occlusion typically presents '
                                                       'as?',
                                           'options': ['A) Sudden painless monocular '
                                                       'vision loss',
                                                       'B) Gradual bilateral painless '
                                                       'central blur over months',
                                                       'C) Painful vision loss with '
                                                       'photophobia and ciliary flush',
                                                       'D) Transient binocular '
                                                       'diplopia without acuity loss'],
                                           'answer': 'A) Sudden painless monocular '
                                                     'vision loss',
                                           'explanation': 'CRAO abruptly stops '
                                                          'arterial perfusion to the '
                                                          'inner retina, causing '
                                                          'sudden, profound, painless '
                                                          'monocular vision loss—a '
                                                          'retinal arterial stroke. '
                                                          'Gradual bilateral blur '
                                                          'suggests cataract or '
                                                          'macular disease; painful '
                                                          'red-eye loss suggests '
                                                          'uveitis/keratitis/glaucoma; '
                                                          'binocular diplopia '
                                                          'localizes to motility, not '
                                                          'CRAO.',
                                           'choice_explanations': {
                                               'A': 'CRAO abruptly stops arterial '
                                                     'perfusion to the inner retina, '
                                                     'causing sudden, profound, '
                                                     'painless monocular vision '
                                                     'loss—effectively a retinal '
                                                     'arterial stroke.',
                                               'B': 'Gradual bilateral central blur '
                                                     'over months suggests progressive '
                                                     'media opacity (cataract) or '
                                                     'macular disease, not acute '
                                                     'arterial occlusion of one eye.',
                                               'C': 'Painful vision loss with '
                                                     'photophobia and ciliary flush '
                                                     'indicates inflammatory '
                                                     'anterior-segment disease '
                                                     '(uveitis/keratitis) or acute '
                                                     'glaucoma, not CRAO.',
                                               'D': 'Transient binocular diplopia '
                                                     'without acuity loss localizes to '
                                                     'ocular motility or brainstem '
                                                     'pathways, not monocular retinal '
                                                     'arterial occlusion.'
                                           }}],
                                 'extreme': [{'question': 'A patient with giant cell '
                                                          'arteritis risk (age >50, '
                                                          'jaw claudication, high ESR) '
                                                          'and sudden vision loss '
                                                          'needs which immediate '
                                                          'approach?',
                                              'options': ['A) Delay all steroids until '
                                                          'temporal-artery biopsy '
                                                          'returns, even if vision is '
                                                          'threatened',
                                                          'B) Start high-dose '
                                                          'corticosteroids urgently '
                                                          'when GCA/AION is strongly '
                                                          'suspected',
                                                          'C) Begin only topical '
                                                          'lubricants while awaiting '
                                                          'outpatient review',
                                                          'D) Proceed first to routine '
                                                          'refraction and spectacle '
                                                          'correction'],
                                              'answer': 'B) Start high-dose '
                                                        'corticosteroids urgently when '
                                                        'GCA/AION is strongly '
                                                        'suspected',
                                              'explanation': 'GCA can occlude '
                                                             'posterior ciliary '
                                                             'arteries and cause '
                                                             'arteritic AION with '
                                                             'abrupt vision loss. Once '
                                                             'GCA/AION is strongly '
                                                             'suspected (age >50, jaw '
                                                             'claudication, elevated '
                                                             'ESR/CRP), high-dose '
                                                             'steroids are started '
                                                             'immediately to protect '
                                                             'the fellow eye; biopsy '
                                                             'should not delay '
                                                             'treatment.',
                                              'choice_explanations': {
                                                  'A': 'Delaying steroids until biopsy '
                                                        'returns risks irreversible '
                                                        'fellow-eye arteritic AION '
                                                        'while GCA continues to occlude '
                                                        'posterior ciliary arteries.',
                                                  'B': 'When GCA/AION is strongly '
                                                        'suspected (age >50, jaw '
                                                        'claudication, elevated '
                                                        'ESR/CRP, sudden vision loss), '
                                                        'high-dose corticosteroids are '
                                                        'started immediately to protect '
                                                        'the fellow eye; biopsy must '
                                                        'not delay treatment.',
                                                  'C': 'Topical lubricants treat '
                                                        'surface dryness and do nothing '
                                                        'to halt vasculitic occlusion '
                                                        'of posterior ciliary arteries '
                                                        'in arteritic AION.',
                                                  'D': 'Refraction corrects optical '
                                                        'blur and is irrelevant to '
                                                        'emergency management of '
                                                        'arteritic ischemic optic '
                                                        'neuropathy.'
                                              }},
                                             {'question': 'In chemical eye injury, the '
                                                          'first action is?',
                                              'options': ['A) Complete visual-field '
                                                          'testing before any '
                                                          'irrigation',
                                                          'B) Tight patching of the '
                                                          'eye without irrigation',
                                                          'C) Immediate copious '
                                                          'irrigation',
                                                          'D) Oral antibiotics as the '
                                                          'sole initial measure'],
                                              'answer': 'C) Immediate copious '
                                                        'irrigation',
                                              'explanation': 'Chemical injury '
                                                             'continues damaging '
                                                             'ocular surface and '
                                                             'deeper tissues until the '
                                                             'agent is diluted and '
                                                             'removed. Immediate '
                                                             'copious irrigation is '
                                                             'therefore the first '
                                                             'action, before detailed '
                                                             'examination or other '
                                                             'therapies. Patching '
                                                             'without irrigation traps '
                                                             'the chemical; oral '
                                                             'antibiotics do not '
                                                             'neutralize alkali/acid '
                                                             'injury.',
                                              'choice_explanations': {
                                                  'A': 'Visual-field testing can wait; '
                                                        'chemical injury continues '
                                                        'tissue damage until the agent '
                                                        'is diluted, so irrigation '
                                                        'takes absolute priority.',
                                                  'B': 'Tight patching without '
                                                        'irrigation traps the chemical '
                                                        'against the ocular surface and '
                                                        'prolongs alkali or acid '
                                                        'injury.',
                                                  'C': 'Chemical injury keeps damaging '
                                                        'ocular surface and deeper '
                                                        'tissues until the agent is '
                                                        'diluted and removed, so '
                                                        'immediate copious irrigation '
                                                        'is the first action.',
                                                  'D': 'Oral antibiotics do not '
                                                        'neutralize or remove chemical '
                                                        'agents and are not the initial '
                                                        'measure in chemical eye '
                                                        'injury.'
                                              }},
                                             {'question': 'An immunosuppressed patient '
                                                          'with painful red eye, '
                                                          'hypopyon, and severe vision '
                                                          'loss may have?',
                                              'options': ['A) Uncomplicated allergic '
                                                          'conjunctivitis',
                                                          'B) Blepharitis without '
                                                          'intraocular involvement',
                                                          'C) Episcleritis with '
                                                          'preserved vision',
                                                          'D) Endophthalmitis until '
                                                          'proven otherwise'],
                                              'answer': 'D) Endophthalmitis until '
                                                        'proven otherwise',
                                              'explanation': 'Endophthalmitis is '
                                                             'infection of the '
                                                             'vitreous and aqueous, '
                                                             'producing severe pain, '
                                                             'marked vision loss, '
                                                             'injection, and often '
                                                             'hypopyon. '
                                                             'Immunosuppression and '
                                                             'recent intraocular '
                                                             'surgery raise risk and '
                                                             'demand urgent specialist '
                                                             'management. Mild surface '
                                                             'disease does not cause '
                                                             'hypopyon with profound '
                                                             'vision loss.',
                                              'choice_explanations': {
                                                  'A': 'Allergic conjunctivitis causes '
                                                        'itchy injection and chemosis '
                                                        'without hypopyon or severe '
                                                        'vision-threatening intraocular '
                                                        'infection.',
                                                  'B': 'Blepharitis is eyelid-margin '
                                                        'inflammation and does not '
                                                        'produce hypopyon with profound '
                                                        'vision loss from intraocular '
                                                        'infection.',
                                                  'C': 'Episcleritis is usually '
                                                        'sectoral redness with '
                                                        'preserved vision and without '
                                                        'hypopyon or severe intraocular '
                                                        'inflammation.',
                                                  'D': 'Endophthalmitis infects the '
                                                        'vitreous and aqueous, '
                                                        'producing severe pain, marked '
                                                        'vision loss, injection, and '
                                                        'often hypopyon—especially '
                                                        'concerning in immunosuppressed '
                                                        'or post-surgical patients.'
                                              }}]},
                   'cases': {'easy': [{'title': 'Red Eye After Dark Room',
                                       'stem': 'A 54-year-old hyperopic woman develops '
                                               'severe eye pain, halos, and nausea '
                                               'after leaving a dark cinema. Pupil is '
                                               'mid-dilated and poorly reactive.',
                                       'question': 'Most likely diagnosis?',
                                       'answer': 'Acute angle-closure glaucoma.',
                                       'discussion': 'Urgent IOP lowering and '
                                                     'ophthalmology referral; avoid '
                                                     'dilating drops.',
                                       'book_hint': "Kanski's Clinical Ophthalmology"}],
                             'medium': [{'title': 'Diabetic Blurry Vision',
                                         'stem': 'A 60-year-old with longstanding '
                                                 'diabetes has gradual blur. Fundus '
                                                 'shows hemorrhages, microaneurysms, '
                                                 'and hard exudates near the macula.',
                                         'question': 'Diagnosis category?',
                                         'answer': 'Diabetic retinopathy with possible '
                                                   'macular involvement.',
                                         'discussion': 'Glycemic/BP control + '
                                                       'ophthalmic management for '
                                                       'macular edema/proliferation.',
                                         'book_hint': "Kanski's Clinical "
                                                      'Ophthalmology'}],
                             'hard': [{'title': 'Pupil-Involving CN III',
                                       'stem': 'A 48-year-old with sudden unilateral '
                                               "ptosis, eye 'down and out', and a "
                                               'dilated poorly reactive pupil has a '
                                               'severe new headache. Decide the '
                                               'highest-yield urgent concept before '
                                               'results return.',
                                       'question': 'What dangerous cause must be '
                                                   'excluded?',
                                       'answer': 'Compressive CN III palsy from PCOM '
                                                 'aneurysm.',
                                       'discussion': 'Urgent neuroimaging/vascular '
                                                     'study; this is not a routine '
                                                     'outpatient palsy.',
                                       'book_hint': "Kanski's Clinical Ophthalmology"}],
                             'extreme': [{'title': 'GCA Threat to Vision',
                                          'stem': 'A 76-year-old woman with new '
                                                  'headache, jaw claudication, scalp '
                                                  'tenderness, and ESR 95 suddenly '
                                                  'loses vision in one eye. Fundus '
                                                  'suggests pale disc swelling. Avoid '
                                                  'interventions that could worsen an '
                                                  'unexcluded catastrophic '
                                                  'differential.',
                                          'question': 'Immediate management concept?',
                                          'answer': 'Treat as arteritic ischemic optic '
                                                    'neuropathy/GCA: urgent high-dose '
                                                    'steroids and urgent specialty '
                                                    'care; arrange temporal artery '
                                                    'biopsy without delaying steroids.',
                                          'discussion': 'Vision in the fellow eye is '
                                                        'at risk within days if '
                                                        'untreated.',
                                          'book_hint': "Kanski's Clinical "
                                                       'Ophthalmology'}]}},
 'urology': {'label': 'Urology',
             'books': ['Campbell-Walsh-Wein Urology',
                       "Smith's General Urology",
                       'Bailey & Love — Urology chapters'],
             'pdf_notes': ['Stone types: calcium oxalate most common; struvite with '
                           'urease organisms; uric acid radiolucent.',
                           'Loin→groin pain + hematuria = ureteric colic until proven '
                           'otherwise.',
                           'Painless hematuria: rule out malignancy (esp. smokers).',
                           'Pyelonephritis: fever + flank pain + UTI signs → '
                           'antibiotics ± imaging.',
                           'BPH: storage/voiding symptoms in older men; assess '
                           'PSA/exam judiciously.'],
             'questions': {'easy': [{'question': 'Most common kidney stone type?',
                                     'options': ['A) Calcium oxalate',
                                                 'B) Uric acid',
                                                 'C) Struvite (magnesium ammonium '
                                                 'phosphate)',
                                                 'D) Cystine'],
                                     'answer': 'A) Calcium oxalate',
                                     'explanation': 'Most urinary calculi are '
                                                    'calcium-based, and calcium '
                                                    'oxalate is the predominant '
                                                    'composition worldwide. '
                                                    'Supersaturation of calcium and '
                                                    'oxalate promotes crystal growth. '
                                                    'Uric acid, struvite, and cystine '
                                                    'stones are important but less '
                                                    'common overall.',
                                     'choice_explanations': {
                                         'A': 'Calcium oxalate is the predominant '
                                               'composition of most urinary calculi '
                                               'worldwide because supersaturation of '
                                               'calcium and oxalate promotes crystal '
                                               'nucleation and growth.',
                                         'B': 'Uric acid stones form in acidic urine '
                                               'with hyperuricosuria and are '
                                               'radiolucent on plain film, but they are '
                                               'less common overall than calcium '
                                               'oxalate stones.',
                                         'C': 'Struvite (magnesium ammonium phosphate) '
                                               'stones form in alkaline urine infected '
                                               'with urease-producing organisms and are '
                                               'less common than calcium oxalate '
                                               'calculi.',
                                         'D': 'Cystine stones arise from inherited '
                                               'cystinuria with defective dibasic '
                                               'amino-acid reabsorption and are rare '
                                               'compared with calcium oxalate stones.'
                                     }},
                                    {'question': 'Loin-to-groin pain classically '
                                                 'suggests?',
                                     'options': ['A) Acute pyelonephritis without '
                                                 'obstruction',
                                                 'B) Ureteric colic',
                                                 'C) Acute prostatitis',
                                                 'D) Renal vein thrombosis'],
                                     'answer': 'B) Ureteric colic',
                                     'explanation': 'A stone in the ureter triggers '
                                                    'visceral pain from spasm and '
                                                    'obstruction. Pain typically '
                                                    'begins in the flank and radiates '
                                                    'to the ipsilateral groin as the '
                                                    'stone migrates. Pyelonephritis '
                                                    'features fever and CVA '
                                                    'tenderness; prostatitis is '
                                                    'pelvic/perineal; renal vein '
                                                    'thrombosis has a different risk '
                                                    'context.',
                                     'choice_explanations': {
                                         'A': 'Acute pyelonephritis without obstruction '
                                               'features fever and costovertebral-angle '
                                               'tenderness but not the migrating '
                                               'loin-to-groin colic of a moving '
                                               'ureteric stone.',
                                         'B': 'A stone in the ureter triggers visceral '
                                               'pain from spasm and obstruction; pain '
                                               'begins in the flank and radiates to the '
                                               'ipsilateral groin as the calculus '
                                               'migrates.',
                                         'C': 'Acute prostatitis causes pelvic, '
                                               'perineal, or low-back pain with voiding '
                                               'symptoms, not classic loin-to-groin '
                                               'ureteric radiation.',
                                         'D': 'Renal vein thrombosis presents with '
                                               'flank pain and hematuria in '
                                               'hypercoagulable or nephrotic contexts, '
                                               'not the migrating colic pattern of '
                                               'ureteric stone passage.'
                                     }},
                                    {'question': 'First imaging often used for stones '
                                                 'in non-pregnant adults?',
                                     'options': ['A) Contrast-enhanced CT abdomen as '
                                                 'first test for all stone suspects',
                                                 'B) MRI pelvis as first-line stone '
                                                 'protocol',
                                                 'C) Non-contrast CT of the kidneys, '
                                                 'ureters, and bladder',
                                                 'D) Renal angiography'],
                                     'answer': 'C) Non-contrast CT of the kidneys, '
                                               'ureters, and bladder',
                                     'explanation': 'Non-contrast CT KUB detects '
                                                    'nearly all stone types by density '
                                                    'and shows size, location, and '
                                                    'secondary obstruction. It is '
                                                    'first-line imaging for suspected '
                                                    'urolithiasis in most non-pregnant '
                                                    'adults. Contrast CT, MRI, and '
                                                    'angiography are not first-line '
                                                    'stone protocols.',
                                     'choice_explanations': {
                                         'A': 'Contrast-enhanced CT is useful for many '
                                               'abdominal diagnoses but is not the '
                                               'first-line dedicated stone protocol; '
                                               'contrast can obscure some calculi.',
                                         'B': 'MRI is not first-line for detecting '
                                               'urinary calculi because stones are '
                                               'poorly visualized compared with CT '
                                               'density mapping.',
                                         'C': 'Non-contrast CT of the kidneys, ureters, '
                                               'and bladder detects nearly all stone '
                                               'types by density and shows size, '
                                               'location, and secondary obstruction in '
                                               'non-pregnant adults.',
                                         'D': 'Renal angiography images arterial '
                                               'anatomy and has no role as first-line '
                                               'imaging for suspected urolithiasis.'
                                     }}],
                           'medium': [{'question': 'Painless gross hematuria in an '
                                                   'older smoker is concerning for?',
                                       'options': ['A) Benign prostatic hyperplasia '
                                                   'alone',
                                                   'B) Stress urinary incontinence',
                                                   'C) Uncomplicated varicocele',
                                                   'D) Urothelial (bladder) carcinoma'],
                                       'answer': 'D) Urothelial (bladder) carcinoma',
                                       'explanation': 'Painless gross hematuria '
                                                      'implies urinary-tract bleeding '
                                                      'without obvious infection or '
                                                      'colic. In older adults, '
                                                      'especially smokers, urothelial '
                                                      'carcinoma of the bladder is a '
                                                      'leading concern requiring '
                                                      'cystoscopic evaluation. BPH may '
                                                      'cause LUTS or microhematuria '
                                                      'but painless gross hematuria '
                                                      'still needs cancer exclusion.',
                                       'choice_explanations': {
                                           'A': 'BPH causes lower urinary tract '
                                                 'symptoms and may be associated with '
                                                 'microscopic hematuria, but painless '
                                                 'gross hematuria in an older smoker '
                                                 'still requires exclusion of '
                                                 'urothelial cancer.',
                                           'B': 'Stress urinary incontinence is leakage '
                                                 'with increased abdominal pressure '
                                                 'from sphincter/support weakness and '
                                                 'does not explain painless gross '
                                                 'hematuria.',
                                           'C': 'Varicocele is dilated pampiniform '
                                                 'plexus veins and is unrelated to '
                                                 'painless gross hematuria concerning '
                                                 'for bladder cancer.',
                                           'D': 'Painless gross hematuria in older '
                                                 'adults, especially smokers, raises '
                                                 'concern for urothelial (bladder) '
                                                 'carcinoma and warrants cystoscopic '
                                                 'evaluation.'
                                       }},
                                      {'question': 'Fever + flank pain + UTI signs '
                                                   'suggest?',
                                       'options': ['A) Acute pyelonephritis',
                                                   'B) Uncomplicated cystitis without '
                                                   'upper-tract involvement',
                                                   'C) Asymptomatic bacteriuria',
                                                   'D) Chronic orchialgia without '
                                                   'infection'],
                                       'answer': 'A) Acute pyelonephritis',
                                       'explanation': 'Acute pyelonephritis is '
                                                      'bacterial infection of the '
                                                      'renal parenchyma and pelvis, '
                                                      'usually ascending from the '
                                                      'lower tract. Fever with flank '
                                                      'pain and UTI symptoms indicates '
                                                      'upper-tract infection needing '
                                                      'prompt antibiotics and risk '
                                                      'assessment for obstruction. '
                                                      'Cystitis lacks fever/flank '
                                                      'findings of pyelonephritis.',
                                       'choice_explanations': {
                                           'A': 'Acute pyelonephritis is bacterial '
                                                 'infection of the renal parenchyma and '
                                                 'pelvis; fever with flank pain and UTI '
                                                 'symptoms indicates upper-tract '
                                                 'infection requiring prompt '
                                                 'antibiotics.',
                                           'B': 'Uncomplicated cystitis is lower-tract '
                                                 'infection with dysuria and frequency '
                                                 'but without fever and flank pain of '
                                                 'pyelonephritis.',
                                           'C': 'Asymptomatic bacteriuria is '
                                                 'bacteriuria without symptoms and does '
                                                 'not present as fever with flank pain.',
                                           'D': 'Chronic orchialgia is persistent '
                                                 'testicular pain without infection and '
                                                 'lacks systemic UTI and flank findings '
                                                 'of pyelonephritis.'
                                       }},
                                      {'question': 'Testicular torsion key management '
                                                   'theme is?',
                                       'options': ['A) Elective outpatient ultrasound '
                                                   'follow-up in weeks',
                                                   'B) Time-critical testicular '
                                                   'ischemia requiring urgent '
                                                   'exploration',
                                                   'C) Antibiotics alone as definitive '
                                                   'therapy',
                                                   'D) Watchful waiting until '
                                                   'cremasteric reflex returns'],
                                       'answer': 'B) Time-critical testicular ischemia '
                                                 'requiring urgent exploration',
                                       'explanation': 'Testicular torsion twists the '
                                                      'spermatic cord, occluding '
                                                      'venous then arterial flow so '
                                                      'the gonad becomes ischemic '
                                                      'within hours. Salvage depends '
                                                      'on rapid surgical detorsion and '
                                                      'orchidopexy; imaging must not '
                                                      'delay exploration when clinical '
                                                      'suspicion is high.',
                                       'choice_explanations': {
                                           'A': 'Elective outpatient ultrasound weeks '
                                                 'later allows irreversible ischemic '
                                                 'necrosis; torsion salvage is measured '
                                                 'in hours.',
                                           'B': 'Torsion twists the spermatic cord, '
                                                 'occluding venous then arterial flow '
                                                 'so the gonad becomes ischemic within '
                                                 'hours; salvage requires urgent '
                                                 'surgical detorsion and orchidopexy.',
                                           'C': 'Antibiotics treat epididymo-orchitis '
                                                 'infection but do not restore blood '
                                                 'flow in spermatic-cord torsion.',
                                           'D': 'Waiting for cremasteric reflex return '
                                                 'delays reperfusion; absent reflex '
                                                 'with high clinical suspicion mandates '
                                                 'exploration, not observation.'
                                       }}],
                           'hard': [{'question': 'Stone with obstructed infected '
                                                 'kidney requires?',
                                     'options': ['A) Oral antibiotics alone with '
                                                 'delayed imaging in weeks',
                                                 'B) Elective lithotripsy after '
                                                 'infection resolves spontaneously '
                                                 'without drainage',
                                                 'C) Urgent decompression plus '
                                                 'antibiotics',
                                                 'D) Trial of alpha-blocker and '
                                                 'outpatient observation only'],
                                     'answer': 'C) Urgent decompression plus '
                                               'antibiotics',
                                     'explanation': 'An obstructing stone with '
                                                    'infection creates closed-space '
                                                    'pyohydronephrosis; bacteria '
                                                    'proliferate under pressure and '
                                                    'seed the bloodstream. Antibiotics '
                                                    'alone cannot reliably sterilize '
                                                    'an obstructed system—urgent '
                                                    'drainage (stent or nephrostomy) '
                                                    'plus antibiotics is required.',
                                     'choice_explanations': {
                                         'A': 'Oral antibiotics alone cannot reliably '
                                               'sterilize an obstructed infected '
                                               'collecting system, where bacteria '
                                               'proliferate under pressure and seed the '
                                               'bloodstream.',
                                         'B': 'Elective lithotripsy after hoping '
                                               'infection resolves without drainage '
                                               'leaves closed-space pyohydronephrosis '
                                               'untreated and risks septic shock.',
                                         'C': 'An obstructing stone with infection '
                                               'creates closed-space infection under '
                                               'pressure; urgent decompression (stent '
                                               'or nephrostomy) plus antibiotics is '
                                               'required.',
                                         'D': 'Alpha-blocker medical expulsive therapy '
                                               'and outpatient observation are for '
                                               'selected uncomplicated ureteric stones, '
                                               'not infected obstructed kidneys.'
                                     }},
                                    {'question': 'Post-obstructive diuresis occurs '
                                                 'after?',
                                     'options': ['A) Initiation of alpha-blocker '
                                                 'therapy for BPH symptoms',
                                                 'B) Elective ureteroscopy for an '
                                                 'asymptomatic non-obstructing stone',
                                                 'C) Treatment of uncomplicated '
                                                 'cystitis without prior retention',
                                                 'D) Relief of chronic urinary '
                                                 'obstruction'],
                                     'answer': 'D) Relief of chronic urinary '
                                               'obstruction',
                                     'explanation': 'After relief of prolonged urinary '
                                                    'obstruction, previously '
                                                    'compressed tubules may '
                                                    'transiently fail to concentrate '
                                                    'urine and reabsorb sodium and '
                                                    'water, producing post-obstructive '
                                                    'diuresis. Careful fluid and '
                                                    'electrolyte monitoring is '
                                                    'required. Beta-blockers, '
                                                    'orthopedic surgery, and vaccines '
                                                    'are unrelated triggers.',
                                     'choice_explanations': {
                                         'A': 'Alpha-blocker therapy relaxes prostatic '
                                               'and ureteric smooth muscle for LUTS or '
                                               'stone passage and does not trigger '
                                               'post-obstructive diuresis.',
                                         'B': 'Elective ureteroscopy for a '
                                               'non-obstructing asymptomatic stone does '
                                               'not unload chronically compressed '
                                               'tubules that drive post-obstructive '
                                               'diuresis.',
                                         'C': 'Treating uncomplicated cystitis '
                                               'addresses mucosal infection without '
                                               'prior chronic retention or obstruction '
                                               'that produces post-obstructive '
                                               'diuresis.',
                                         'D': 'After relief of prolonged urinary '
                                               'obstruction, previously compressed '
                                               'tubules may transiently fail to '
                                               'concentrate urine and reabsorb Na and '
                                               'water, producing post-obstructive '
                                               'diuresis.'
                                     }},
                                    {'question': 'High-riding testis and absent '
                                                 'cremasteric reflex suggest?',
                                     'options': ['A) Testicular torsion until proven '
                                                 'otherwise',
                                                 'B) Isolated hydrocele without '
                                                 'ischemia',
                                                 'C) Epididymo-orchitis as the only '
                                                 'possibility',
                                                 'D) Reducible inguinal hernia alone'],
                                     'answer': 'A) Testicular torsion until proven '
                                               'otherwise',
                                     'explanation': 'Intravaginal torsion shortens the '
                                                    'spermatic cord, pulling the '
                                                    'testis higher and interrupting '
                                                    'the cremasteric reflex. With '
                                                    'acute unilateral scrotal pain, '
                                                    'this constellation is torsion '
                                                    'until proven otherwise and '
                                                    'warrants urgent surgical '
                                                    'exploration.',
                                     'choice_explanations': {
                                         'A': 'Intravaginal torsion shortens the '
                                               'spermatic cord, elevating the testis '
                                               'and interrupting the cremasteric '
                                               'reflex; with acute scrotal pain this '
                                               'constellation is torsion until proven '
                                               'otherwise.',
                                         'B': 'Hydrocele is fluid in the tunica '
                                               'vaginalis and does not by itself cause '
                                               'a high-riding testis with absent '
                                               'cremasteric reflex from cord ischemia.',
                                         'C': 'Epididymo-orchitis can cause a painful '
                                               'swollen testis but usually preserves a '
                                               'lower-lying position and cremasteric '
                                               'reflex early; the classic torsion signs '
                                               'still mandate ruling out torsion.',
                                         'D': 'A reducible inguinal hernia is bowel or '
                                               'fat in the inguinal canal and does not '
                                               'produce the ischemic high-riding testis '
                                               'and lost cremasteric reflex of torsion.'
                                     }}],
                           'extreme': [{'question': 'Fournier gangrene is?',
                                        'options': ['A) Uncomplicated candidal '
                                                    'balanitis',
                                                    'B) Necrotizing infection of the '
                                                    'perineum/genitalia needing urgent '
                                                    'surgical debridement',
                                                    'C) Localized cellulitis without '
                                                    'fascial necrosis',
                                                    'D) Simple scrotal edema from '
                                                    'hypoalbuminemia'],
                                        'answer': 'B) Necrotizing infection of the '
                                                  'perineum/genitalia needing urgent '
                                                  'surgical debridement',
                                        'explanation': 'Fournier gangrene is a '
                                                       'synergistic necrotizing '
                                                       'soft-tissue infection of the '
                                                       'perineum and genitalia that '
                                                       'spreads along fascial planes. '
                                                       'Rapid necrosis and sepsis '
                                                       'demand immediate surgical '
                                                       'debridement plus broad '
                                                       'antibiotics—not topical '
                                                       'therapy for simple surface '
                                                       'infections.',
                                        'choice_explanations': {
                                            'A': 'Candidal balanitis is superficial '
                                                  'mucosal yeast infection treated '
                                                  'topically and is not necrotizing '
                                                  'fascial infection of the perineum.',
                                            'B': 'Fournier gangrene is synergistic '
                                                  'necrotizing soft-tissue infection of '
                                                  'the perineum and genitalia spreading '
                                                  'along fascial planes, requiring '
                                                  'immediate surgical debridement plus '
                                                  'broad antibiotics.',
                                            'C': 'Localized cellulitis without fascial '
                                                  'necrosis lacks the rapid deep '
                                                  'necrosis and systemic toxicity that '
                                                  'define Fournier gangrene.',
                                            'D': 'Simple scrotal edema from '
                                                  'hypoalbuminemia is noninfectious '
                                                  'fluid accumulation without '
                                                  'necrotizing infection.'
                                        }},
                                       {'question': 'Autonomic dysreflexia in spinal '
                                                    'cord injury with bladder '
                                                    'distension can cause?',
                                        'options': ['A) Isolated orthostatic '
                                                    'hypotension',
                                                    'B) Primary bradycardia without '
                                                    'blood-pressure change',
                                                    'C) Dangerous hypertensive crisis '
                                                    'from unchecked sympathetic '
                                                    'discharge',
                                                    'D) Transient mild thirst without '
                                                    'autonomic instability'],
                                        'answer': 'C) Dangerous hypertensive crisis '
                                                  'from unchecked sympathetic '
                                                  'discharge',
                                        'explanation': 'In SCI above splanchnic '
                                                       'sympathetic outflow, a noxious '
                                                       'stimulus below the lesion '
                                                       '(commonly bladder distension) '
                                                       'triggers unchecked sympathetic '
                                                       'vasoconstriction, causing '
                                                       'dangerous hypertension. '
                                                       'Management centers on sitting '
                                                       'upright and relieving the '
                                                       'precipitant (empty the '
                                                       'bladder).',
                                        'choice_explanations': {
                                            'A': 'Orthostatic hypotension is a fall in '
                                                  'BP on standing from autonomic '
                                                  'failure or volume depletion, '
                                                  'opposite to the hypertensive crisis '
                                                  'of autonomic dysreflexia.',
                                            'B': 'Primary bradycardia without BP change '
                                                  'does not describe autonomic '
                                                  'dysreflexia, in which below-lesion '
                                                  'stimuli drive massive sympathetic '
                                                  'vasoconstriction and hypertension.',
                                            'C': 'In SCI above splanchnic outflow, '
                                                  'bladder distension triggers '
                                                  'unchecked sympathetic '
                                                  'vasoconstriction below the lesion, '
                                                  'producing dangerous hypertensive '
                                                  'crisis (autonomic dysreflexia).',
                                            'D': 'Mild thirst without autonomic '
                                                  'instability is not the '
                                                  'pathophysiology of autonomic '
                                                  'dysreflexia from a noxious '
                                                  'below-lesion stimulus.'
                                        }},
                                       {'question': 'A trauma patient with pelvic '
                                                    'fracture and blood at the meatus '
                                                    'should avoid?',
                                        'options': ['A) Application of a pelvic binder '
                                                    'when indicated for unstable '
                                                    'pelvic fracture',
                                                    'B) Standard trauma primary survey '
                                                    '(ABCs)',
                                                    'C) Early blood typing and '
                                                    'crossmatch',
                                                    'D) Blind urethral catheterization '
                                                    'before assessing for urethral '
                                                    'injury'],
                                        'answer': 'D) Blind urethral catheterization '
                                                  'before assessing for urethral '
                                                  'injury',
                                        'explanation': 'Pelvic fracture with blood at '
                                                       'the meatus suggests urethral '
                                                       'disruption. Blind '
                                                       'catheterization can convert a '
                                                       'partial tear into complete '
                                                       'transection or create a false '
                                                       'passage. Retrograde '
                                                       'urethrogram (or specialist '
                                                       'assessment) should precede '
                                                       'catheter attempts; binder, '
                                                       'ABCs, and crossmatch remain '
                                                       'appropriate trauma care.',
                                        'choice_explanations': {
                                            'A': 'A pelvic binder reduces pelvic volume '
                                                  'and can tamponade bleeding in '
                                                  'unstable pelvic fractures and '
                                                  'remains appropriate when indicated.',
                                            'B': 'The trauma primary survey (ABCs) is '
                                                  'mandatory initial care and is not '
                                                  'contraindicated by suspected '
                                                  'urethral injury.',
                                            'C': 'Early blood typing and crossmatch '
                                                  'prepare for hemorrhage resuscitation '
                                                  'and should proceed in pelvic trauma.',
                                            'D': 'Blood at the meatus with pelvic '
                                                  'fracture suggests urethral '
                                                  'disruption; blind catheterization '
                                                  'can complete a partial tear or '
                                                  'create a false passage, so '
                                                  'urethrography or specialist '
                                                  'assessment should come first.'
                                        }}]},
             'cases': {'easy': [{'title': 'Sudden Flank Pain',
                                 'stem': 'A 30-year-old man has sudden severe left '
                                         'flank pain radiating to the groin and cannot '
                                         'find a comfortable position. Dipstick shows '
                                         'blood.',
                                 'question': 'Likely diagnosis?',
                                 'answer': 'Ureteric colic from a stone.',
                                 'discussion': 'Analgesia and imaging; watch for '
                                               'infection/obstruction.',
                                 'book_hint': 'Campbell-Walsh-Wein Urology'}],
                       'medium': [{'title': 'Feverish Flank Pain',
                                   'stem': 'A 27-year-old woman has fever, vomiting, '
                                           'and right flank tenderness with '
                                           'nitrite-positive urine.',
                                   'question': 'Diagnosis?',
                                   'answer': 'Acute pyelonephritis.',
                                   'discussion': 'Cultures + antibiotics; image if not '
                                                 'improving or complicated.',
                                   'book_hint': 'Campbell-Walsh-Wein Urology'}],
                       'hard': [{'title': 'Obstructing Stone + Fever',
                                 'stem': 'A 45-year-old with a 9 mm proximal ureteric '
                                         'stone develops fever, rigors, and '
                                         'hypotension. Decide the highest-yield urgent '
                                         'concept before results return.',
                                 'question': 'Priority concept?',
                                 'answer': 'Treat as obstructed infected kidney: '
                                           'resuscitation, antibiotics, urgent '
                                           'drainage (stent/nephrostomy).',
                                 'discussion': 'Delay can lead to septic shock.',
                                 'book_hint': 'Campbell-Walsh-Wein Urology'}],
                       'extreme': [{'title': 'Trauma + Blood at Meatus',
                                    'stem': 'A motorcyclist with pelvic fracture has '
                                            'blood at the urethral meatus and a '
                                            'high-riding prostate on exam. The intern '
                                            'reaches for a Foley catheter. Avoid '
                                            'interventions that could worsen an '
                                            'unexcluded catastrophic differential.',
                                    'question': 'What is the correct concept?',
                                    'answer': 'Do not attempt blind catheterization; '
                                              'evaluate for urethral injury first '
                                              'while continuing trauma resuscitation.',
                                    'discussion': 'Wrong catheterization can convert '
                                                  'partial to complete urethral '
                                                  'injury.',
                                    'book_hint': 'Campbell-Walsh-Wein Urology'}]}},
 'neurology': {'label': 'Neurology',
               'books': ["Adams and Victor's Principles of Neurology",
                         "Harrison's — Neurology",
                         'Clinical Neurology — Simon R. / Brazis'],
               'pdf_notes': ['Stroke = sudden focal deficit — time is brain; use '
                             'FAST/NIHSS pathways.',
                             'UMN vs LMN: spasticity/hyperreflexia vs '
                             'flaccid/hyporeflexia/fasciculations.',
                             'SAH: thunderclap headache — urgent non-contrast CT ± LP.',
                             'Meningitis: fever, neck stiffness, altered mentation — '
                             'early antibiotics.',
                             'Migraine: unilateral throbbing ± '
                             'nausea/photo-phonophobia; rule out red flags.'],
               'questions': {'easy': [{'question': 'Sudden face/arm weakness with '
                                                   'speech difficulty suggests?',
                                       'options': ['A) Acute stroke (ischemic or '
                                                   'hemorrhagic) until proven '
                                                   'otherwise',
                                                   'B) Bell palsy without limb or '
                                                   'speech involvement',
                                                   'C) Migraine aura without '
                                                   'persistent focal deficit',
                                                   'D) Peripheral vestibular neuritis '
                                                   'alone'],
                                       'answer': 'A) Acute stroke (ischemic or '
                                                 'hemorrhagic) until proven otherwise',
                                       'explanation': 'Sudden focal neurologic '
                                                      'deficits such as facial droop, '
                                                      'arm weakness, and speech '
                                                      'difficulty reflect acute '
                                                      'ischemia or hemorrhage in a '
                                                      'corresponding brain region. '
                                                      'Because neuronal injury is '
                                                      'time-dependent, this '
                                                      'presentation is stroke until '
                                                      'proven otherwise and triggers '
                                                      'urgent stroke pathways.',
                                       'choice_explanations': {
                                           'A': 'Sudden face and arm weakness with '
                                                 'speech difficulty reflects acute '
                                                 'ischemia or hemorrhage in a '
                                                 'corresponding brain region and is '
                                                 'treated as stroke until proven '
                                                 'otherwise because neuronal injury is '
                                                 'time-dependent.',
                                           'B': 'Bell palsy is idiopathic peripheral '
                                                 'facial-nerve weakness without arm '
                                                 'weakness or cortical speech deficits '
                                                 'that define central stroke syndromes.',
                                           'C': 'Migraine aura causes transient fully '
                                                 'reversible neurologic symptoms, '
                                                 'usually visual, without the '
                                                 'persistent sudden motor and speech '
                                                 'deficits of acute stroke.',
                                           'D': 'Peripheral vestibular neuritis causes '
                                                 'acute vertigo from vestibular-nerve '
                                                 'inflammation without face/arm '
                                                 'weakness or aphasia.'
                                       }},
                                      {'question': 'Meningism features include?',
                                       'options': ['A) Isolated tension-type headache '
                                                   'without fever or meningism',
                                                   'B) Neck stiffness with fever and '
                                                   'headache',
                                                   'C) Benign positional vertigo '
                                                   'without systemic signs',
                                                   'D) Cluster headache with autonomic '
                                                   'tearing alone'],
                                       'answer': 'B) Neck stiffness with fever and '
                                                 'headache',
                                       'explanation': 'Meningeal inflammation '
                                                      'sensitizes pain fibers, '
                                                      'producing headache with neck '
                                                      'stiffness (meningism), often '
                                                      'with fever and photophobia. '
                                                      'These features raise concern '
                                                      'for meningitis or subarachnoid '
                                                      'blood and warrant urgent '
                                                      'evaluation. Isolated primary '
                                                      'headache syndromes lack true '
                                                      'meningism with fever.',
                                       'choice_explanations': {
                                           'A': 'Isolated tension-type headache lacks '
                                                 'fever and true neck stiffness from '
                                                 'meningeal irritation.',
                                           'B': 'Meningeal inflammation sensitizes pain '
                                                 'fibers, producing headache with neck '
                                                 'stiffness (meningism), often with '
                                                 'fever and photophobia, raising '
                                                 'concern for meningitis or '
                                                 'subarachnoid blood.',
                                           'C': 'Benign positional vertigo is '
                                                 'canalithiasis causing brief '
                                                 'position-triggered vertigo without '
                                                 'systemic meningism.',
                                           'D': 'Cluster headache features unilateral '
                                                 'orbital pain with autonomic '
                                                 'tearing/rhinorrhea but not fever with '
                                                 'meningism of meningeal inflammation.'
                                       }},
                                      {'question': 'UMN signs include?',
                                       'options': ['A) Fasciculations with '
                                                   'hyporeflexia and atrophy',
                                                   'B) Flaccid paralysis with '
                                                   'areflexia from acute LMN lesion',
                                                   'C) Extensor plantar response '
                                                   '(Babinski) and spasticity',
                                                   'D) Pure sensory loss without '
                                                   'pyramidal signs'],
                                       'answer': 'C) Extensor plantar response '
                                                 '(Babinski) and spasticity',
                                       'explanation': 'Upper motor neuron lesions '
                                                      'remove descending inhibition of '
                                                      'spinal reflex arcs, yielding '
                                                      'spasticity, hyperreflexia, and '
                                                      'an extensor plantar (Babinski) '
                                                      'response. Fasciculations, '
                                                      'hyporeflexia, and flaccid '
                                                      'areflexic weakness indicate '
                                                      'lower motor neuron or '
                                                      'peripheral pathology.',
                                       'choice_explanations': {
                                           'A': 'Fasciculations with hyporeflexia and '
                                                 'atrophy indicate lower motor neuron '
                                                 'or peripheral nerve disease, not '
                                                 'upper motor neuron pathology.',
                                           'B': 'Flaccid paralysis with areflexia is '
                                                 'the acute lower motor neuron pattern, '
                                                 'opposite to chronic UMN spastic '
                                                 'hyperreflexic weakness.',
                                           'C': 'Upper motor neuron lesions remove '
                                                 'descending inhibition of spinal '
                                                 'reflex arcs, yielding spasticity, '
                                                 'hyperreflexia, and an extensor '
                                                 'plantar (Babinski) response.',
                                           'D': 'Pure sensory loss without pyramidal '
                                                 'signs localizes to sensory pathways '
                                                 'rather than the corticospinal UMN '
                                                 'system.'
                                       }}],
                             'medium': [{'question': 'Thunderclap headache first '
                                                     'exclude?',
                                         'options': ['A) Typical migraine without '
                                                     'thunderclap onset',
                                                     'B) Acute bacterial sinusitis',
                                                     'C) Uncomplicated tension-type '
                                                     'headache',
                                                     'D) Aneurysmal subarachnoid '
                                                     'hemorrhage'],
                                         'answer': 'D) Aneurysmal subarachnoid '
                                                   'hemorrhage',
                                         'explanation': 'Thunderclap headache reaches '
                                                        'maximal intensity within '
                                                        'seconds and is the classic '
                                                        'presentation of aneurysmal '
                                                        'SAH. Missed SAH is '
                                                        'catastrophic, so '
                                                        'sudden-maximal headache '
                                                        'requires urgent CT and, if '
                                                        'needed, LP—not attribution to '
                                                        'primary headache until SAH is '
                                                        'excluded.',
                                         'choice_explanations': {
                                             'A': 'Typical migraine builds over minutes '
                                                   'to hours and is not a thunderclap '
                                                   'reaching maximal intensity within '
                                                   'seconds that mandates SAH '
                                                   'exclusion.',
                                             'B': 'Acute bacterial sinusitis causes '
                                                   'facial pain and congestion, not the '
                                                   'instantaneous maximal headache of '
                                                   'aneurysmal SAH.',
                                             'C': 'Tension-type headache is '
                                                   'mild–moderate band-like pain '
                                                   'without thunderclap onset or '
                                                   'meningeal warning of SAH.',
                                             'D': 'Thunderclap headache reaches peak '
                                                   'intensity within seconds and is the '
                                                   'classic presentation of aneurysmal '
                                                   'subarachnoid hemorrhage, requiring '
                                                   'urgent CT ± LP before attributing '
                                                   'it to primary headache.'
                                         }},
                                        {'question': 'Absence seizures are most '
                                                     'typical in?',
                                         'options': ['A) School-age children with '
                                                     'brief staring spells',
                                                     'B) Elderly patients with new '
                                                     'atrial fibrillation',
                                                     'C) Neonates with physiologic '
                                                     'jaundice alone',
                                                     'D) Adults with classic migraine '
                                                     'with visual aura'],
                                         'answer': 'A) School-age children with brief '
                                                   'staring spells',
                                         'explanation': 'Absence seizures are '
                                                        'generalized childhood '
                                                        'seizures from oscillatory '
                                                        'thalamocortical discharges '
                                                        '(3-Hz spike-and-wave on EEG). '
                                                        'They appear as brief staring '
                                                        'spells lasting seconds with '
                                                        'immediate recovery. They are '
                                                        'not the typical seizure type '
                                                        'of AF-related stroke, '
                                                        'neonatal jaundice, or '
                                                        'migraine aura.',
                                         'choice_explanations': {
                                             'A': 'Absence seizures are generalized '
                                                   'childhood seizures from oscillatory '
                                                   'thalamocortical 3-Hz spike-and-wave '
                                                   'discharges, appearing as brief '
                                                   'staring spells lasting seconds with '
                                                   'immediate recovery.',
                                             'B': 'Elderly patients with new AF are at '
                                                   'risk for embolic stroke, not the '
                                                   'typical demographic or mechanism of '
                                                   'childhood absence epilepsy.',
                                             'C': 'Neonatal physiologic jaundice is '
                                                   'bilirubin accumulation from '
                                                   'immature conjugation and is '
                                                   'unrelated to absence seizure '
                                                   'pathophysiology.',
                                             'D': 'Migraine with visual aura is '
                                                   'cortical spreading depression, not '
                                                   'thalamocortical 3-Hz spike-and-wave '
                                                   'absence seizures.'
                                         }},
                                        {'question': 'Parkinsonism core motor feature '
                                                     'is?',
                                         'options': ['A) Hyperreflexia as the defining '
                                                     'core feature',
                                                     'B) Bradykinesia',
                                                     'C) Flaccid paralysis',
                                                     'D) Pure intention tremor without '
                                                     'bradykinesia'],
                                         'answer': 'B) Bradykinesia',
                                         'explanation': 'Parkinsonism reflects '
                                                        'nigrostriatal dopamine '
                                                        'deficiency slowing movement '
                                                        'initiation and execution. '
                                                        'Bradykinesia is the core '
                                                        'required motor feature; rest '
                                                        'tremor and rigidity commonly '
                                                        'accompany it. Hyperreflexia '
                                                        'suggests UMN disease; flaccid '
                                                        'paralysis and isolated '
                                                        'intention tremor suggest '
                                                        'other localizations.',
                                         'choice_explanations': {
                                             'A': 'Hyperreflexia is an upper motor '
                                                   'neuron sign and is not the defining '
                                                   'core motor feature required to '
                                                   'diagnose Parkinsonism.',
                                             'B': 'Parkinsonism reflects nigrostriatal '
                                                   'dopamine deficiency that slows '
                                                   'movement initiation and execution; '
                                                   'bradykinesia is the required core '
                                                   'motor feature.',
                                             'C': 'Flaccid paralysis indicates acute '
                                                   'lower motor neuron or peripheral '
                                                   'nerve failure, not extrapyramidal '
                                                   'bradykinesia of Parkinsonism.',
                                             'D': 'Pure intention tremor worsens toward '
                                                   'a target and localizes to '
                                                   'cerebellar circuits; without '
                                                   'bradykinesia it does not fulfill '
                                                   'Parkinsonism criteria.'
                                         }}],
                             'hard': [{'question': 'Status epilepticus initial '
                                                   'management concept?',
                                       'options': ['A) Observation for several hours '
                                                   'before any antiseizure medication',
                                                   'B) Levetiracetam monotherapy '
                                                   'without initial benzodiazepine '
                                                   'when seizing',
                                                   'C) Airway support plus early '
                                                   'benzodiazepine, then escalate '
                                                   'antiseizure medicines',
                                                   'D) Immediate neurosurgical '
                                                   'resection as the first step in all '
                                                   'SE'],
                                       'answer': 'C) Airway support plus early '
                                                 'benzodiazepine, then escalate '
                                                 'antiseizure medicines',
                                       'explanation': 'Status epilepticus causes '
                                                      'progressive neuronal injury and '
                                                      'systemic complications. After '
                                                      'ABCs, a benzodiazepine is given '
                                                      'promptly, then second-line '
                                                      'antiseizure drugs if seizures '
                                                      'continue. Delayed treatment '
                                                      'worsens outcomes; skipping the '
                                                      'benzodiazepine step or jumping '
                                                      'first to surgery is '
                                                      'inappropriate for initial SE '
                                                      'care.',
                                       'choice_explanations': {
                                           'A': 'Observing untreated status epilepticus '
                                                 'for hours allows progressive neuronal '
                                                 'injury and systemic complications; '
                                                 'early benzodiazepines are required.',
                                           'B': 'Initial therapy for active convulsive '
                                                 'status epilepticus is a '
                                                 'benzodiazepine; levetiracetam is a '
                                                 'second-line agent after or with that '
                                                 'step, not a replacement for it at '
                                                 'onset.',
                                           'C': 'Status epilepticus causes progressive '
                                                 'neuronal injury; after airway '
                                                 'support, a benzodiazepine is given '
                                                 'promptly, then second-line '
                                                 'antiseizure drugs if seizures '
                                                 'continue.',
                                           'D': 'Neurosurgical resection is not the '
                                                 'first step in initial status '
                                                 'epilepticus care, which is medical '
                                                 'stabilization and antiseizure '
                                                 'medication escalation.'
                                       }},
                                      {'question': 'Crossed cranial-nerve plus '
                                                   'contralateral body signs localize '
                                                   'to?',
                                       'options': ['A) Pure cortical convexity lesion '
                                                   'without brainstem signs',
                                                   'B) Distal peripheral nerve only',
                                                   'C) Muscle end-plate disorder alone',
                                                   'D) Brainstem'],
                                       'answer': 'D) Brainstem',
                                       'explanation': 'Crossed findings—ipsilateral '
                                                      'cranial-nerve signs with '
                                                      'contralateral body weakness or '
                                                      'sensory loss—are the hallmark '
                                                      'of brainstem localization where '
                                                      'cranial-nerve nuclei and long '
                                                      'tracts are closely packed. '
                                                      'Cortex, peripheral nerve, and '
                                                      'NMJ disorders do not produce '
                                                      'this crossed pattern.',
                                       'choice_explanations': {
                                           'A': 'Pure cortical convexity lesions '
                                                 'produce ipsilateral face/arm findings '
                                                 'without the crossed cranial-nerve '
                                                 'versus contralateral body pattern of '
                                                 'brainstem disease.',
                                           'B': 'Distal peripheral nerve lesions cause '
                                                 'deficits in a single nerve territory '
                                                 'without contralateral long-tract '
                                                 'findings.',
                                           'C': 'Muscle end-plate disorders (e.g., '
                                                 'myasthenia) cause fatigable weakness '
                                                 'without crossed brainstem '
                                                 'cranial-nerve and long-tract signs.',
                                           'D': 'Crossed findings—ipsilateral '
                                                 'cranial-nerve signs with '
                                                 'contralateral body weakness or '
                                                 'sensory loss—are the hallmark of '
                                                 'brainstem localization where '
                                                 'cranial-nerve nuclei and long tracts '
                                                 'are closely packed.'
                                       }},
                                      {'question': 'Myasthenia gravis fatigable '
                                                   'weakness often involves?',
                                       'options': ['A) Ocular and bulbar muscles '
                                                   '(fatigable ptosis, diplopia, '
                                                   'dysarthria)',
                                                   'B) Distal sensory neuropathy as '
                                                   'the primary feature',
                                                   'C) Upper motor neuron spastic '
                                                   'paraparesis alone',
                                                   'D) Cerebellar ataxia without '
                                                   'fatigable weakness'],
                                       'answer': 'A) Ocular and bulbar muscles '
                                                 '(fatigable ptosis, diplopia, '
                                                 'dysarthria)',
                                       'explanation': 'Myasthenia gravis is an '
                                                      'autoimmune attack on '
                                                      'postsynaptic acetylcholine '
                                                      'receptors, causing fatigable '
                                                      'weakness that preferentially '
                                                      'affects ocular and bulbar '
                                                      'muscles. Sensory loss, pure UMN '
                                                      'spasticity, and cerebellar '
                                                      'ataxia indicate other disease '
                                                      'categories.',
                                       'choice_explanations': {
                                           'A': 'Myasthenia gravis is autoimmune attack '
                                                 'on postsynaptic acetylcholine '
                                                 'receptors, causing fatigable weakness '
                                                 'that preferentially affects ocular '
                                                 'and bulbar muscles (ptosis, diplopia, '
                                                 'dysarthria).',
                                           'B': 'Distal sensory neuropathy is '
                                                 'peripheral sensory axon/myelin '
                                                 'disease and is not the primary '
                                                 'feature of a postsynaptic NMJ '
                                                 'disorder.',
                                           'C': 'Upper motor neuron spastic paraparesis '
                                                 'reflects corticospinal tract disease, '
                                                 'not fatigable NMJ transmission '
                                                 'failure.',
                                           'D': 'Cerebellar ataxia is disordered '
                                                 'coordination from cerebellar circuits '
                                                 'and occurs without the fatigable '
                                                 'weakness of myasthenia.'
                                       }}],
                             'extreme': [{'question': 'Spinal cord compression with '
                                                      'saddle anesthesia and retention '
                                                      'needs?',
                                          'options': ['A) Elective outpatient '
                                                      'physiotherapy starting in weeks',
                                                      'B) Urgent MRI and surgical '
                                                      'decompression pathway',
                                                      'C) Oral analgesia alone without '
                                                      'imaging',
                                                      'D) Delayed review after '
                                                      'incomplete bladder emptying is '
                                                      'ignored'],
                                          'answer': 'B) Urgent MRI and surgical '
                                                    'decompression pathway',
                                          'explanation': 'Saddle anesthesia with '
                                                         'urinary retention suggests '
                                                         'cauda equina or cord '
                                                         'compression. Cord/cauda '
                                                         'compression is '
                                                         'time-critical: urgent '
                                                         'imaging and decompression '
                                                         'can preserve sphincter and '
                                                         'motor function. Delayed '
                                                         'conservative care risks '
                                                         'permanent deficit.',
                                          'choice_explanations': {
                                              'A': 'Elective physiotherapy weeks later '
                                                    'allows permanent sphincter and '
                                                    'motor damage once cauda equina or '
                                                    'cord compression is established.',
                                              'B': 'Saddle anesthesia with urinary '
                                                    'retention suggests cauda equina or '
                                                    'cord compression; urgent MRI and '
                                                    'decompression can preserve '
                                                    'sphincter and motor function.',
                                              'C': 'Oral analgesia alone without '
                                                    'imaging leaves compressive cauda '
                                                    'equina pathology untreated while '
                                                    'neurologic injury progresses.',
                                              'D': 'Ignoring incomplete bladder '
                                                    'emptying delays diagnosis of '
                                                    'compressive cauda equina syndrome '
                                                    'and risks irreversible deficits.'
                                          }},
                                         {'question': 'Locked-in syndrome typically '
                                                      'localizes to?',
                                          'options': ['A) Bilateral occipital lobes',
                                                      'B) Dominant parietal cortex '
                                                      'alone',
                                                      'C) Bilateral ventral pons',
                                                      'D) Cervical dorsal columns '
                                                      'only'],
                                          'answer': 'C) Bilateral ventral pons',
                                          'explanation': 'Locked-in syndrome reflects '
                                                         'bilateral ventral pontine '
                                                         'injury (often basilar artery '
                                                         'occlusion) disrupting '
                                                         'corticospinal and '
                                                         'corticobulbar fibers while '
                                                         'sparing consciousness and '
                                                         'vertical eye movements '
                                                         'mediated more dorsally. '
                                                         'Occipital, parietal, and '
                                                         'dorsal-column lesions '
                                                         'produce different '
                                                         'syndromes.',
                                          'choice_explanations': {
                                              'A': 'Bilateral occipital lesions cause '
                                                    'cortical blindness (Anton’s '
                                                    'syndrome possible) but preserve '
                                                    'motor pathways, unlike locked-in '
                                                    'syndrome.',
                                              'B': 'Dominant parietal cortex lesions '
                                                    'cause aphasia, neglect, or '
                                                    'Gerstmann features without the '
                                                    'anarthric quadriplegia of ventral '
                                                    'pontine disruption.',
                                              'C': 'Locked-in syndrome reflects '
                                                    'bilateral ventral pontine injury '
                                                    '(often basilar occlusion) '
                                                    'disrupting corticospinal and '
                                                    'corticobulbar fibers while sparing '
                                                    'consciousness and vertical eye '
                                                    'movements more dorsally.',
                                              'D': 'Cervical dorsal-column injury '
                                                    'impairs proprioception and '
                                                    'vibration without producing the '
                                                    'de-efferented locked-in state from '
                                                    'ventral pons damage.'
                                          }},
                                         {'question': 'NMDA-receptor encephalitis is '
                                                      'often discussed in association '
                                                      'with?',
                                          'options': ['A) Thymoma as the most classic '
                                                      'tumor link',
                                                      'B) Small-cell lung cancer as '
                                                      'the primary association',
                                                      'C) Pheochromocytoma as the '
                                                      'usual trigger',
                                                      'D) Ovarian teratoma in young '
                                                      'women'],
                                          'answer': 'D) Ovarian teratoma in young '
                                                    'women',
                                          'explanation': 'Anti-NMDA-receptor '
                                                         'encephalitis often presents '
                                                         'with psychiatric features, '
                                                         'seizures, dyskinesias, and '
                                                         'autonomic instability; in '
                                                         'young women it is '
                                                         'classically associated with '
                                                         'ovarian teratoma. Thymoma '
                                                         'links to myasthenia; SCLC to '
                                                         'Lambert-Eaton and other '
                                                         'paraneoplastic syndromes.',
                                          'choice_explanations': {
                                              'A': 'Thymoma is the classic tumor '
                                                    'association of myasthenia gravis, '
                                                    'not anti-NMDA-receptor '
                                                    'encephalitis.',
                                              'B': 'Small-cell lung cancer associates '
                                                    'with Lambert–Eaton myasthenic '
                                                    'syndrome and several other '
                                                    'paraneoplastic syndromes, not the '
                                                    'classic ovarian teratoma link of '
                                                    'NMDA encephalitis.',
                                              'C': 'Pheochromocytoma is a '
                                                    'catecholamine-secreting adrenal '
                                                    'tumor and is not the usual trigger '
                                                    'of anti-NMDA-receptor '
                                                    'encephalitis.',
                                              'D': 'Anti-NMDA-receptor encephalitis '
                                                    'often presents with psychiatric '
                                                    'features, seizures, and '
                                                    'dyskinesias; in young women it is '
                                                    'classically associated with '
                                                    'ovarian teratoma.'
                                          }}]},
               'cases': {'easy': [{'title': 'Sudden Weakness',
                                   'stem': 'A 70-year-old develops sudden right '
                                           'arm/leg weakness and aphasia 40 minutes '
                                           'ago. Glucose is normal.',
                                   'question': 'Priority diagnosis pathway?',
                                   'answer': 'Acute stroke — activate stroke pathway.',
                                   'discussion': 'Time-critical imaging and '
                                                 'reperfusion eligibility.',
                                   'book_hint': "Adams and Victor / Harrison's "
                                                'Neurology'}],
                         'medium': [{'title': 'Worst Headache',
                                     'stem': 'A 45-year-old has the worst headache of '
                                             'life peaking in seconds with neck '
                                             'stiffness.',
                                     'question': 'What must be excluded?',
                                     'answer': 'Subarachnoid hemorrhage.',
                                     'discussion': 'Urgent non-contrast CT ± LP.',
                                     'book_hint': "Adams and Victor / Harrison's "
                                                  'Neurology'}],
                         'hard': [{'title': 'Fatigable Diplopia',
                                   'stem': 'A 34-year-old has fatigable ptosis and '
                                           'diplopia worse at night, improving with '
                                           'rest. Ice-pack test helps transiently. '
                                           'Labs and imaging are pending; you must '
                                           'choose the safest next clinical concept.',
                                   'question': 'Likely diagnosis?',
                                   'answer': 'Myasthenia gravis.',
                                   'discussion': 'Avoid certain drugs; assess '
                                                 'respiratory function; specialty '
                                                 'care.',
                                   'book_hint': "Adams and Victor / Harrison's "
                                                'Neurology'}],
                         'extreme': [{'title': 'Young Woman with Psychiatric then '
                                               'Seizure Cascade',
                                      'stem': 'A 24-year-old develops subacute '
                                              'psychosis, dyskinesias, autonomic '
                                              'instability, and refractory seizures. '
                                              'CT finds an ovarian teratoma. Multiple '
                                              'teams are involved; prioritize '
                                              'life/limb/vision threats and avoid '
                                              'harmful premature therapies.',
                                      'question': 'Syndrome to consider?',
                                      'answer': 'Anti-NMDA receptor encephalitis — '
                                                'immunotherapy + tumor removal '
                                                'pathway.',
                                      'discussion': 'Early recognition changes '
                                                    'outcome.',
                                      'book_hint': "Adams and Victor / Harrison's "
                                                   'Neurology'}]}},
 'pulmonology': {'label': 'Pulmonology',
                 'books': ["West's Respiratory Physiology",
                           "Harrison's — Respiratory Medicine",
                           "Crofton and Douglas's Respiratory Diseases"],
                 'pdf_notes': ['CAP: S. pneumoniae most common; assess CURB-65 '
                               'severity.',
                               'Asthma: reversible obstruction; COPD: largely '
                               'irreversible.',
                               'PE: sudden dyspnea/pleuritic pain post-risk — Wells + '
                               'CT PA pathway.',
                               'Tension pneumothorax: shock + tracheal deviation — '
                               'immediate decompression.',
                               'TB: chronic cough, night sweats, weight loss — '
                               'AFB/GeneXpert as available.'],
                 'questions': {'easy': [{'question': 'Common CAP organism?',
                                         'options': ['A) Streptococcus pneumoniae',
                                                     'B) Mycobacterium tuberculosis as '
                                                     'the usual CAP pathogen',
                                                     'C) Pneumocystis jirovecii in '
                                                     'immunocompetent hosts',
                                                     'D) Pseudomonas aeruginosa in '
                                                     'previously healthy adults'],
                                         'answer': 'A) Streptococcus pneumoniae',
                                         'explanation': 'Streptococcus pneumoniae '
                                                        'remains the most common '
                                                        'identified bacterial cause of '
                                                        'community-acquired pneumonia '
                                                        'in adults. TB, Pneumocystis, '
                                                        'and Pseudomonas are important '
                                                        'in specific host or exposure '
                                                        'contexts but are not the '
                                                        'typical CAP organism in '
                                                        'otherwise healthy community '
                                                        'patients.',
                                         'choice_explanations': {
                                             'A': 'Streptococcus pneumoniae remains the '
                                                   'most common identified bacterial '
                                                   'cause of community-acquired '
                                                   'pneumonia in adults.',
                                             'B': 'Mycobacterium tuberculosis causes '
                                                   'tuberculosis with different '
                                                   'epidemiology and chronicity and is '
                                                   'not the usual CAP pathogen in '
                                                   'otherwise healthy community adults.',
                                             'C': 'Pneumocystis jirovecii pneumonia '
                                                   'occurs mainly in immunocompromised '
                                                   'hosts, not as typical CAP in '
                                                   'immunocompetent patients.',
                                             'D': 'Pseudomonas aeruginosa is an '
                                                   'opportunistic pathogen in '
                                                   'structural lung disease, hospital, '
                                                   'or immunocompromised settings, not '
                                                   'the usual CAP organism in '
                                                   'previously healthy adults.'
                                         }},
                                        {'question': 'Asthma is characterized by?',
                                         'options': ['A) Fixed irreversible '
                                                     'obstruction from birth without '
                                                     'variability',
                                                     'B) Reversible airflow '
                                                     'obstruction with airway '
                                                     'hyperresponsiveness',
                                                     'C) Alveolar filling with '
                                                     'bacteria as the defining '
                                                     'mechanism',
                                                     'D) Pulmonary vascular '
                                                     'obliteration as the primary '
                                                     'process'],
                                         'answer': 'B) Reversible airflow obstruction '
                                                   'with airway hyperresponsiveness',
                                         'explanation': 'Asthma is characterized by '
                                                        'variable, reversible airway '
                                                        'obstruction and bronchial '
                                                        'hyperresponsiveness driven by '
                                                        'airway inflammation. Fixed '
                                                        'irreversible obstruction '
                                                        'describes COPD '
                                                        'emphysema/chronic bronchitis '
                                                        'patterns better; alveolar '
                                                        'infection and pure vascular '
                                                        'disease are different '
                                                        'entities.',
                                         'choice_explanations': {
                                             'A': 'Fixed irreversible obstruction from '
                                                   'birth without variability describes '
                                                   'developmental or severe COPD-like '
                                                   'fixed airflow limitation, not the '
                                                   'defining variable reversibility of '
                                                   'asthma.',
                                             'B': 'Asthma is characterized by variable, '
                                                   'reversible airway obstruction and '
                                                   'bronchial hyperresponsiveness '
                                                   'driven by airway inflammation.',
                                             'C': 'Alveolar filling with bacteria '
                                                   'defines pneumonia’s consolidative '
                                                   'infection, a different mechanism '
                                                   'from asthmatic bronchoconstriction '
                                                   'and inflammation.',
                                             'D': 'Pulmonary vascular obliteration is '
                                                   'the pathology of pulmonary vascular '
                                                   'disease/PH, not the airway-centric '
                                                   'physiology of asthma.'
                                         }},
                                        {'question': 'SpO2 measures?',
                                         'options': ['A) Partial pressure of arterial '
                                                     'carbon dioxide',
                                                     'B) Hemoglobin concentration',
                                                     'C) Approximate arterial oxygen '
                                                     'saturation of hemoglobin',
                                                     'D) Alveolar minute ventilation '
                                                     'directly'],
                                         'answer': 'C) Approximate arterial oxygen '
                                                   'saturation of hemoglobin',
                                         'explanation': 'Pulse oximetry estimates the '
                                                        'percentage of hemoglobin '
                                                        'saturated with oxygen using '
                                                        'light absorption. It does not '
                                                        'measure PaCO2, hemoglobin '
                                                        'amount, or ventilation '
                                                        'directly—ABG and other tests '
                                                        'are needed for those '
                                                        'parameters.',
                                         'choice_explanations': {
                                             'A': 'PaCO2 is the partial pressure of '
                                                   'arterial carbon dioxide measured on '
                                                   'arterial blood gas, not by pulse '
                                                   'oximetry light absorption.',
                                             'B': 'Hemoglobin concentration is the '
                                                   'amount of hemoglobin in blood (lab '
                                                   'CBC), whereas SpO2 estimates the '
                                                   'fraction of that hemoglobin that is '
                                                   'oxygen-saturated.',
                                             'C': 'Pulse oximetry (SpO2) estimates the '
                                                   'percentage of hemoglobin saturated '
                                                   'with oxygen using differential '
                                                   'light absorption at two '
                                                   'wavelengths.',
                                             'D': 'Alveolar minute ventilation is the '
                                                   'volume of fresh air reaching '
                                                   'alveoli per minute and is not '
                                                   'measured by a pulse oximeter.'
                                         }}],
                               'medium': [{'question': 'CURB-65 assesses?',
                                           'options': ['A) Pulmonary embolism pretest '
                                                       'probability',
                                                       'B) Asthma control over the '
                                                       'prior four weeks',
                                                       'C) Lung-cancer staging',
                                                       'D) Community-acquired '
                                                       'pneumonia severity and '
                                                       'disposition risk'],
                                           'answer': 'D) Community-acquired pneumonia '
                                                     'severity and disposition risk',
                                           'explanation': 'CURB-65 (Confusion, Urea, '
                                                          'Respiratory rate, Blood '
                                                          'pressure, age ≥65) '
                                                          'stratifies CAP severity and '
                                                          'helps guide site-of-care '
                                                          'decisions. Wells scoring '
                                                          'addresses PE probability; '
                                                          'asthma control and cancer '
                                                          'staging use different '
                                                          'tools.',
                                           'choice_explanations': {
                                               'A': 'Pulmonary embolism pretest '
                                                     'probability is estimated with '
                                                     'tools such as Wells or Geneva '
                                                     'scores, not CURB-65.',
                                               'B': 'Asthma control over weeks is '
                                                     'assessed with symptom/control '
                                                     'questionnaires and spirometry, '
                                                     'not CURB-65.',
                                               'C': 'Lung-cancer staging uses TNM '
                                                     'imaging and pathology systems, '
                                                     'not the CURB-65 pneumonia score.',
                                               'D': 'CURB-65 (Confusion, Urea, '
                                                     'Respiratory rate, Blood pressure, '
                                                     'age ≥65) stratifies '
                                                     'community-acquired pneumonia '
                                                     'severity and helps guide '
                                                     'site-of-care decisions.'
                                           }},
                                          {'question': 'Wells score helps for?',
                                           'options': ['A) Pulmonary embolism pretest '
                                                       'probability',
                                                       'B) COPD exacerbation severity '
                                                       'alone',
                                                       'C) Community-acquired '
                                                       'pneumonia mortality alone',
                                                       'D) Pulmonary hypertension WHO '
                                                       'group classification'],
                                           'answer': 'A) Pulmonary embolism pretest '
                                                     'probability',
                                           'explanation': 'The Wells score combines '
                                                          'clinical features to '
                                                          'estimate pretest '
                                                          'probability of PE and guide '
                                                          'D-dimer versus imaging '
                                                          'pathways. It is not a COPD, '
                                                          'CAP, or PH classification '
                                                          'instrument.',
                                           'choice_explanations': {
                                               'A': 'The Wells score combines clinical '
                                                     'features to estimate pretest '
                                                     'probability of pulmonary embolism '
                                                     'and guide D-dimer versus imaging '
                                                     'pathways.',
                                               'B': 'COPD exacerbation severity uses '
                                                     'clinical and blood-gas criteria '
                                                     'separate from the Wells PE score.',
                                               'C': 'Community-acquired pneumonia '
                                                     'mortality risk uses scores such '
                                                     'as CURB-65 or PSI, not Wells.',
                                               'D': 'Pulmonary hypertension WHO group '
                                                     'classification is based on '
                                                     'pathophysiology (precapillary vs '
                                                     'postcapillary, etc.), not the '
                                                     'Wells PE score.'
                                           }},
                                          {'question': 'COPD oxygen target in many '
                                                       'retainers is often?',
                                           'options': ['A) Unrestricted high-flow '
                                                       'oxygen to SpO2 100% in all '
                                                       'COPD patients',
                                                       'B) A controlled SpO2 target '
                                                       'such as 88–92% per protocol in '
                                                       'CO2 retainers',
                                                       'C) No supplemental oxygen even '
                                                       'if SpO2 is 70%',
                                                       'D) Oxygen titrated only to '
                                                       'relieve dyspnea without SpO2 '
                                                       'targets'],
                                           'answer': 'B) A controlled SpO2 target such '
                                                     'as 88–92% per protocol in CO2 '
                                                     'retainers',
                                           'explanation': 'In chronic CO2 retainers, '
                                                          'excessive oxygen can worsen '
                                                          'hypercapnia via V/Q change '
                                                          'and reduced hypoxic drive. '
                                                          'Controlled oxygen targeting '
                                                          '(often 88–92%) balances '
                                                          'hypoxemia treatment against '
                                                          'CO2 retention risk, guided '
                                                          'by protocol and ABG.',
                                           'choice_explanations': {
                                               'A': 'Unrestricted high-flow oxygen to '
                                                     'SpO2 100% can worsen hypercapnia '
                                                     'in chronic CO2 retainers via V/Q '
                                                     'change and reduced hypoxic drive.',
                                               'B': 'In chronic CO2 retainers, '
                                                     'controlled oxygen targeting '
                                                     '(often SpO2 88–92% per protocol) '
                                                     'treats hypoxemia while limiting '
                                                     'further CO2 retention, guided by '
                                                     'ABG.',
                                               'C': 'Withholding oxygen when SpO2 is '
                                                     '70% leaves dangerous hypoxemia '
                                                     'untreated; controlled titration '
                                                     'is required, not absolute refusal '
                                                     'of oxygen.',
                                               'D': 'Titrating only to dyspnea without '
                                                     'SpO2 targets ignores objective '
                                                     'hypoxemia and hypercapnia risk '
                                                     'monitoring in retainers.'
                                           }}],
                               'hard': [{'question': 'Tension pneumothorax treatment '
                                                     'concept?',
                                         'options': ['A) Urgent CT confirmation before '
                                                     'any decompression if unstable',
                                                     'B) High-dose IV steroid as '
                                                     'primary therapy',
                                                     'C) Immediate needle/finger '
                                                     'thoracostomy decompression then '
                                                     'definitive chest drain',
                                                     'D) Noninvasive ventilation alone '
                                                     'without decompression'],
                                         'answer': 'C) Immediate needle/finger '
                                                   'thoracostomy decompression then '
                                                   'definitive chest drain',
                                         'explanation': 'Tension pneumothorax causes '
                                                        'obstructive shock by raising '
                                                        'intrapleural pressure, '
                                                        'collapsing the lung, and '
                                                        'impairing venous return. '
                                                        'Unstable patients need '
                                                        'immediate decompression '
                                                        'followed by chest-tube '
                                                        'drainage; imaging must not '
                                                        'delay treatment.',
                                         'choice_explanations': {
                                             'A': 'Urgent CT before decompression '
                                                   'delays relief of obstructive shock '
                                                   'in an unstable tension pneumothorax '
                                                   'and is inappropriate when the '
                                                   'patient is crashing.',
                                             'B': 'High-dose IV steroids treat '
                                                   'inflammatory airway or adrenal '
                                                   'disease and do not decompress '
                                                   'pressurized intrapleural air.',
                                             'C': 'Tension pneumothorax raises '
                                                   'intrapleural pressure, collapses '
                                                   'the lung, and impairs venous '
                                                   'return; unstable patients need '
                                                   'immediate needle/finger '
                                                   'thoracostomy then definitive chest '
                                                   'drain.',
                                             'D': 'Noninvasive ventilation without '
                                                   'decompression can worsen tension '
                                                   'physiology by forcing more air into '
                                                   'the pleural space through a leak.'
                                         }},
                                        {'question': "Light's criteria relate to?",
                                         'options': ['A) Staging primary lung cancer',
                                                     'B) Calculating A-a oxygen '
                                                     'gradient',
                                                     'C) Diagnosing pulmonary '
                                                     'hypertension by echo criteria',
                                                     'D) Distinguishing pleural '
                                                     'exudate from transudate'],
                                         'answer': 'D) Distinguishing pleural exudate '
                                                   'from transudate',
                                         'explanation': "Light's criteria compare "
                                                        'pleural and serum protein/LDH '
                                                        'ratios to separate exudates '
                                                        '(infection, malignancy, '
                                                        'inflammation) from '
                                                        'transudates (heart failure, '
                                                        'cirrhosis). They do not stage '
                                                        'cancer, compute A-a gradient, '
                                                        'or diagnose PH.',
                                         'choice_explanations': {
                                             'A': 'Primary lung-cancer staging uses TNM '
                                                   'systems based on tumor extent, '
                                                   'nodes, and metastases—not Light’s '
                                                   'pleural fluid criteria.',
                                             'B': 'The A-a oxygen gradient compares '
                                                   'alveolar and arterial PO2 to assess '
                                                   'gas-exchange efficiency and is '
                                                   'unrelated to Light’s criteria.',
                                             'C': 'Pulmonary hypertension echo criteria '
                                                   'estimate pulmonary pressures and '
                                                   'right-heart effects, not pleural '
                                                   'fluid exudate versus transudate.',
                                             'D': 'Light’s criteria compare pleural and '
                                                   'serum protein/LDH ratios to '
                                                   'separate exudates (infection, '
                                                   'malignancy, inflammation) from '
                                                   'transudates (heart failure, '
                                                   'cirrhosis).'
                                         }},
                                        {'question': 'Massive hemoptysis priority is?',
                                         'options': ['A) Airway protection with '
                                                     'bleeding lung dependent (down)',
                                                     'B) Encourage vigorous coughing '
                                                     'unsupervised as sole therapy',
                                                     'C) Immediate full '
                                                     'anticoagulation before airway '
                                                     'control',
                                                     'D) Routine outpatient follow-up '
                                                     'without emergency assessment'],
                                         'answer': 'A) Airway protection with bleeding '
                                                   'lung dependent (down)',
                                         'explanation': 'Massive hemoptysis threatens '
                                                        'asphyxiation more than '
                                                        'exsanguination. Priority is '
                                                        'airway protection—often '
                                                        'positioning the bleeding side '
                                                        'down so blood does not flood '
                                                        'the good lung—then urgent '
                                                        'specialist control of '
                                                        'bleeding.',
                                         'choice_explanations': {
                                             'A': 'Massive hemoptysis threatens '
                                                   'asphyxiation; positioning the '
                                                   'bleeding lung dependent (down) '
                                                   'protects the contralateral lung '
                                                   'while urgent airway and bleeding '
                                                   'control proceed.',
                                             'B': 'Encouraging vigorous unsupervised '
                                                   'coughing as sole therapy does not '
                                                   'protect the good lung or control '
                                                   'life-threatening airway blood.',
                                             'C': 'Immediate full anticoagulation '
                                                   'worsens hemorrhage and is '
                                                   'contraindicated before airway '
                                                   'control in massive hemoptysis.',
                                             'D': 'Routine outpatient follow-up without '
                                                   'emergency assessment ignores the '
                                                   'immediate risk of asphyxiation from '
                                                   'massive bleeding into the airway.'
                                         }}],
                               'extreme': [{'question': 'ARDS Berlin concept includes?',
                                            'options': ['A) Chronic stable hypoxemia '
                                                        'from COPD without acute '
                                                        'bilateral infiltrates',
                                                        'B) Acute hypoxemic '
                                                        'respiratory failure with '
                                                        'bilateral opacities not fully '
                                                        'explained by heart failure',
                                                        'C) Isolated lobar pneumonia '
                                                        'fully explained by typical '
                                                        'CAP alone',
                                                        'D) Cardiogenic edema as the '
                                                        'required sole explanation for '
                                                        'all bilateral opacities'],
                                            'answer': 'B) Acute hypoxemic respiratory '
                                                      'failure with bilateral '
                                                      'opacities not fully explained '
                                                      'by heart failure',
                                            'explanation': 'The Berlin definition of '
                                                           'ARDS requires acute onset, '
                                                           'bilateral opacities, and '
                                                           'hypoxemia not fully '
                                                           'explained by cardiac '
                                                           'failure or fluid overload, '
                                                           'reflecting diffuse '
                                                           'alveolar damage. Chronic '
                                                           'COPD hypoxemia and simple '
                                                           'lobar CAP do not meet this '
                                                           'construct.',
                                            'choice_explanations': {
                                                'A': 'Chronic stable COPD hypoxemia '
                                                      'lacks the acute bilateral '
                                                      'opacities and noncardiogenic '
                                                      'hypoxemic failure required by '
                                                      'the Berlin ARDS definition.',
                                                'B': 'The Berlin definition of ARDS '
                                                      'requires acute onset, bilateral '
                                                      'opacities, and hypoxemia not '
                                                      'fully explained by cardiac '
                                                      'failure or fluid overload, '
                                                      'reflecting diffuse alveolar '
                                                      'damage.',
                                                'C': 'Isolated lobar pneumonia fully '
                                                      'explained by typical CAP does '
                                                      'not meet the diffuse bilateral '
                                                      'noncardiogenic criteria of ARDS.',
                                                'D': 'Cardiogenic edema as the sole '
                                                      'explanation for bilateral '
                                                      'opacities excludes ARDS; Berlin '
                                                      'criteria require hypoxemia not '
                                                      'fully explained by heart '
                                                      'failure.'
                                            }},
                                           {'question': 'Fat embolism triad after '
                                                        'fracture?',
                                            'options': ['A) Isolated deep-vein '
                                                        'thrombosis without pulmonary '
                                                        'or skin findings',
                                                        'B) Fever and productive cough '
                                                        'alone without neurologic or '
                                                        'petechial signs',
                                                        'C) Respiratory distress, '
                                                        'neurologic change, and '
                                                        'petechial rash',
                                                        'D) Chronic exertional dyspnea '
                                                        'without acute fracture '
                                                        'context'],
                                            'answer': 'C) Respiratory distress, '
                                                      'neurologic change, and '
                                                      'petechial rash',
                                            'explanation': 'Fat embolism syndrome '
                                                           'classically follows '
                                                           'long-bone or pelvic '
                                                           'fracture and presents with '
                                                           'the triad of acute '
                                                           'respiratory distress, '
                                                           'neurologic dysfunction, '
                                                           'and petechiae (often '
                                                           'axillary/conjunctival). '
                                                           'Isolated DVT or simple '
                                                           'pneumonia lacks this '
                                                           'triad.',
                                            'choice_explanations': {
                                                'A': 'Isolated DVT is lower-extremity '
                                                      'venous thrombosis without the '
                                                      'respiratory, neurologic, and '
                                                      'petechial triad of fat embolism '
                                                      'syndrome.',
                                                'B': 'Fever and productive cough alone '
                                                      'suggest pneumonia and lack the '
                                                      'neurologic change and petechiae '
                                                      'of fat embolism after fracture.',
                                                'C': 'Fat embolism syndrome classically '
                                                      'follows long-bone or pelvic '
                                                      'fracture and presents with acute '
                                                      'respiratory distress, neurologic '
                                                      'dysfunction, and petechial rash.',
                                                'D': 'Chronic exertional dyspnea '
                                                      'without acute fracture context '
                                                      'is not the acute post-fracture '
                                                      'triad of fat embolism syndrome.'
                                            }},
                                           {'question': 'Bronchial carcinoid can cause '
                                                        'which syndrome theme?',
                                            'options': ['A) Cushing syndrome from '
                                                        'ectopic ACTH as the usual '
                                                        'presentation of all bronchial '
                                                        'carcinoids',
                                                        'B) Isolated SIADH as the '
                                                        'defining carcinoid syndrome '
                                                        'feature',
                                                        'C) Hypoglycemia from insulin '
                                                        'secretion as the classic '
                                                        'carcinoid mediator effect',
                                                        'D) Carcinoid syndrome with '
                                                        'flushing and diarrhea when '
                                                        'vasoactive mediators reach '
                                                        'the systemic circulation '
                                                        '(often with metastases)'],
                                            'answer': 'D) Carcinoid syndrome with '
                                                      'flushing and diarrhea when '
                                                      'vasoactive mediators reach the '
                                                      'systemic circulation (often '
                                                      'with metastases)',
                                            'explanation': 'Bronchial carcinoid can '
                                                           'release vasoactive '
                                                           'mediators; classic '
                                                           'carcinoid syndrome '
                                                           '(flushing, diarrhea, '
                                                           'bronchospasm) typically '
                                                           'appears when mediators '
                                                           'escape hepatic metabolism, '
                                                           'often with metastatic '
                                                           'disease. Ectopic ACTH, '
                                                           'SIADH, and insulinoma '
                                                           'physiology are different '
                                                           'neuroendocrine '
                                                           'syndromes.',
                                            'choice_explanations': {
                                                'A': 'Ectopic ACTH secretion causing '
                                                      'Cushing syndrome can occur with '
                                                      'some neuroendocrine tumors but '
                                                      'is not the usual presentation of '
                                                      'all bronchial carcinoids nor the '
                                                      'definition of carcinoid '
                                                      'syndrome.',
                                                'B': 'SIADH causes hyponatremia from '
                                                      'inappropriate ADH and is a '
                                                      'different paraneoplastic theme '
                                                      'than classic carcinoid mediator '
                                                      'syndrome.',
                                                'C': 'Hypoglycemia from insulin '
                                                      'secretion defines insulinoma '
                                                      'physiology, not the '
                                                      'vasoactive-mediator flushing and '
                                                      'diarrhea of carcinoid syndrome.',
                                                'D': 'Carcinoid syndrome (flushing, '
                                                      'diarrhea, bronchospasm) occurs '
                                                      'when vasoactive mediators from '
                                                      'carcinoid reach the systemic '
                                                      'circulation, often with '
                                                      'metastases that bypass hepatic '
                                                      'metabolism.'
                                            }}]},
                 'cases': {'easy': [{'title': 'Fever + Productive Cough',
                                     'stem': 'A 60-year-old has fever, rusty sputum, '
                                             'and focal crackles. CXR shows lobar '
                                             'consolidation.',
                                     'question': 'Likely diagnosis?',
                                     'answer': 'Community-acquired pneumonia.',
                                     'discussion': 'Severity score + antibiotics + '
                                                   'oxygen if needed.',
                                     'book_hint': "Harrison's Respiratory / West"}],
                           'medium': [{'title': 'Post-Flight Dyspnea',
                                       'stem': 'A 42-year-old after a long flight has '
                                               'sudden dyspnea and pleuritic pain. '
                                               'SpO2 91%.',
                                       'question': 'Top diagnosis to exclude?',
                                       'answer': 'Pulmonary embolism.',
                                       'discussion': 'Risk stratify and image/treat '
                                                     'per pathway.',
                                       'book_hint': "Harrison's Respiratory / West"}],
                           'hard': [{'title': 'Asthma Near-Fatal',
                                     'stem': 'A teen with asthma is silent-chested, '
                                             'hypoxic, and tiring with rising CO2. '
                                             'Labs and imaging are pending; you must '
                                             'choose the safest next clinical concept.',
                                     'question': 'What does this imply?',
                                     'answer': 'Life-threatening asthma — escalate to '
                                               'emergency airway/ventilatory support '
                                               'pathway.',
                                     'discussion': 'A silent chest is ominous.',
                                     'book_hint': "Harrison's Respiratory / West"}],
                           'extreme': [{'title': 'Post-Op Hypoxemia + Petechiae',
                                        'stem': 'Day 2 after femoral nailing, a young '
                                                'man becomes confused and hypoxic with '
                                                'axillary petechiae. CT PA is negative '
                                                'for large PE. Multiple teams are '
                                                'involved; prioritize life/limb/vision '
                                                'threats and avoid harmful premature '
                                                'therapies.',
                                        'question': 'Consider?',
                                        'answer': 'Fat embolism syndrome — supportive '
                                                  'care and orthopaedic/ICU '
                                                  'collaboration.',
                                        'discussion': 'Classic triad after long-bone '
                                                      'instrumentation.',
                                        'book_hint': "Harrison's Respiratory / "
                                                     'West'}]}},
 'gastroenterology': {'label': 'Gastroenterology',
                      'books': ["Sleisenger and Fordtran's Gastrointestinal and Liver "
                                'Disease',
                                "Harrison's — Gastroenterology",
                                'Bailey & Love — Abdominal surgery chapters'],
                      'pdf_notes': ['Charcot triad = cholangitis; Reynolds pentad adds '
                                    'hypotension + confusion.',
                                    'H. pylori → PUD; test-and-treat in appropriate '
                                    'settings.',
                                    'Pancreatitis: epigastric pain to back + ↑ lipase; '
                                    'fluids and support.',
                                    "Appendicitis: periumbilical→RLQ pain, McBurney's "
                                    'tenderness.',
                                    'Cirrhosis complications: varices, ascites, '
                                    'encephalopathy, HCC surveillance.'],
                      'questions': {'easy': [{'question': 'Charcot triad indicates?',
                                              'options': ['A) Ascending cholangitis',
                                                          'B) Uncomplicated '
                                                          'cholelithiasis without '
                                                          'infection',
                                                          'C) Acute hepatitis A '
                                                          'without biliary obstruction',
                                                          'D) Peptic ulcer disease '
                                                          'without biliary sepsis'],
                                              'answer': 'A) Ascending cholangitis',
                                              'explanation': 'Charcot '
                                                             'triad—right-upper-quadrant '
                                                             'pain, fever, and '
                                                             'jaundice—indicates '
                                                             'ascending cholangitis '
                                                             'from infected biliary '
                                                             'obstruction. '
                                                             'Uncomplicated stones, '
                                                             'viral hepatitis, and '
                                                             'peptic ulcer lack this '
                                                             'infected-obstruction '
                                                             'pattern.',
                                              'choice_explanations': {
                                                  'A': 'Charcot '
                                                        'triad—right-upper-quadrant '
                                                        'pain, fever, and '
                                                        'jaundice—indicates ascending '
                                                        'cholangitis from infected '
                                                        'biliary obstruction.',
                                                  'B': 'Uncomplicated cholelithiasis '
                                                        'causes biliary colic without '
                                                        'fever and jaundice of infected '
                                                        'obstructed ducts.',
                                                  'C': 'Acute hepatitis A is '
                                                        'hepatocellular viral infection '
                                                        'with jaundice and hepatitis '
                                                        'labs but not the infected '
                                                        'biliary obstruction pattern of '
                                                        'Charcot triad.',
                                                  'D': 'Peptic ulcer disease is mucosal '
                                                        'ulceration from acid and H. '
                                                        'pylori/NSAIDs and does not '
                                                        'produce Charcot’s infected '
                                                        'biliary obstruction triad.'
                                              }},
                                             {'question': 'H. pylori is linked to?',
                                              'options': ['A) Celiac disease as the '
                                                          'primary H. pylori '
                                                          'manifestation',
                                                          'B) Peptic ulcer disease',
                                                          'C) Pancreatic '
                                                          'adenocarcinoma as the main '
                                                          'H. pylori link',
                                                          'D) Gilbert syndrome'],
                                              'answer': 'B) Peptic ulcer disease',
                                              'explanation': 'Helicobacter pylori '
                                                             'colonizes gastric '
                                                             'mucosa, driving chronic '
                                                             'gastritis and '
                                                             'substantially increasing '
                                                             'risk of duodenal and '
                                                             'gastric peptic ulcers '
                                                             '(and some gastric '
                                                             'cancers). It is not the '
                                                             'primary mechanism of '
                                                             'celiac disease, '
                                                             'pancreatic '
                                                             'adenocarcinoma, or '
                                                             'Gilbert syndrome.',
                                              'choice_explanations': {
                                                  'A': 'Celiac disease is '
                                                        'gluten-triggered small-bowel '
                                                        'autoimmune enteropathy '
                                                        '(HLA-DQ2/8), not primarily an '
                                                        'H. pylori gastric infection '
                                                        'manifestation.',
                                                  'B': 'Helicobacter pylori colonizes '
                                                        'gastric mucosa, driving '
                                                        'chronic gastritis and '
                                                        'substantially increasing risk '
                                                        'of duodenal and gastric peptic '
                                                        'ulcers.',
                                                  'C': 'Pancreatic adenocarcinoma '
                                                        'arises from pancreatic ductal '
                                                        'epithelium and is not the main '
                                                        'disease link of gastric H. '
                                                        'pylori colonization.',
                                                  'D': 'Gilbert syndrome is inherited '
                                                        'reduced hepatic bilirubin '
                                                        'conjugation causing mild '
                                                        'unconjugated '
                                                        'hyperbilirubinemia, unrelated '
                                                        'to H. pylori.'
                                              }},
                                             {'question': "McBurney's point relates "
                                                          'to?',
                                              'options': ['A) Acute cholecystitis',
                                                          'B) Sigmoid diverticulitis',
                                                          'C) Appendicitis',
                                                          'D) Left-sided ureteric '
                                                          'colic'],
                                              'answer': 'C) Appendicitis',
                                              'explanation': "McBurney's point lies "
                                                             'one-third of the way '
                                                             'from the right anterior '
                                                             'superior iliac spine to '
                                                             'the umbilicus and is the '
                                                             'classic site of maximal '
                                                             'tenderness in acute '
                                                             'appendicitis. '
                                                             'Cholecystitis, '
                                                             'diverticulitis, and left '
                                                             'ureteric colic localize '
                                                             'elsewhere.',
                                              'choice_explanations': {
                                                  'A': 'Acute cholecystitis localizes '
                                                        'to the right upper quadrant '
                                                        'and Murphy’s sign, not '
                                                        'McBurney’s point in the right '
                                                        'lower quadrant.',
                                                  'B': 'Sigmoid diverticulitis '
                                                        'typically causes '
                                                        'left-lower-quadrant pain, '
                                                        'opposite the right iliac fossa '
                                                        'tenderness of McBurney’s '
                                                        'point.',
                                                  'C': 'McBurney’s point lies one-third '
                                                        'of the way from the right ASIS '
                                                        'to the umbilicus and is the '
                                                        'classic site of maximal '
                                                        'tenderness in acute '
                                                        'appendicitis.',
                                                  'D': 'Left-sided ureteric colic '
                                                        'radiates to the left groin and '
                                                        'does not map to McBurney’s '
                                                        'right iliac fossa landmark.'
                                              }}],
                                    'medium': [{'question': 'Pancreatitis pain often '
                                                            'radiates to?',
                                                'options': ['A) The right shoulder tip '
                                                            'alone as the only '
                                                            'radiation pattern',
                                                            'B) The left groin '
                                                            'exclusively',
                                                            'C) The occiput',
                                                            'D) The back'],
                                                'answer': 'D) The back',
                                                'explanation': 'Acute pancreatitis '
                                                               'typically causes '
                                                               'severe epigastric pain '
                                                               'that radiates through '
                                                               'to the back because '
                                                               'the inflamed '
                                                               'retroperitoneal '
                                                               'pancreas lies against '
                                                               'posterior structures. '
                                                               'Shoulder-tip pain '
                                                               'suggests diaphragmatic '
                                                               'irritation (e.g., '
                                                               'biliary), and groin '
                                                               'pain suggests urologic '
                                                               'referred pain.',
                                                'choice_explanations': {
                                                    'A': 'Right shoulder-tip pain often '
                                                          'reflects diaphragmatic '
                                                          'irritation (e.g., biliary '
                                                          'disease) rather than the '
                                                          'typical through-to-back '
                                                          'radiation of pancreatitis.',
                                                    'B': 'Left groin radiation suggests '
                                                          'urologic referred pain '
                                                          '(ureteric colic), not '
                                                          'retroperitoneal pancreatic '
                                                          'inflammation.',
                                                    'C': 'Occipital pain is cranial and '
                                                          'unrelated to the '
                                                          'epigastric-to-back pattern '
                                                          'of acute pancreatitis.',
                                                    'D': 'Acute pancreatitis typically '
                                                          'causes severe epigastric '
                                                          'pain radiating through to '
                                                          'the back because the '
                                                          'inflamed retroperitoneal '
                                                          'pancreas lies against '
                                                          'posterior structures.'
                                                }},
                                               {'question': 'Variceal bleed risk is '
                                                            'highest in?',
                                                'options': ['A) Portal hypertension '
                                                            'from cirrhosis',
                                                            'B) Uncomplicated peptic '
                                                            'ulcer without portal '
                                                            'hypertension',
                                                            'C) Mild gastroesophageal '
                                                            'reflux disease',
                                                            'D) Diverticular bleeding '
                                                            'from colonic diverticula '
                                                            'as the same mechanism'],
                                                'answer': 'A) Portal hypertension from '
                                                          'cirrhosis',
                                                'explanation': 'Esophageal varices '
                                                               'form when portal '
                                                               'hypertension opens '
                                                               'portosystemic '
                                                               'collaterals; rupture '
                                                               'causes '
                                                               'life-threatening upper '
                                                               'GI bleeding, most '
                                                               'often in cirrhosis. '
                                                               'Peptic ulcer and '
                                                               'diverticular bleeding '
                                                               'are important but '
                                                               'mechanistically '
                                                               'distinct.',
                                                'choice_explanations': {
                                                    'A': 'Esophageal varices form when '
                                                          'portal hypertension opens '
                                                          'portosystemic collaterals; '
                                                          'rupture causes '
                                                          'life-threatening upper GI '
                                                          'bleeding, most often in '
                                                          'cirrhosis.',
                                                    'B': 'Uncomplicated peptic ulcer '
                                                          'bleeds from mucosal erosion '
                                                          'into vessels without the '
                                                          'portal-hypertensive '
                                                          'collateral mechanism of '
                                                          'varices.',
                                                    'C': 'Mild GERD is reflux of '
                                                          'gastric contents causing '
                                                          'heartburn without portal '
                                                          'hypertension or variceal '
                                                          'hemorrhage risk.',
                                                    'D': 'Diverticular bleeding is '
                                                          'arterial bleeding from '
                                                          'colonic diverticula, a '
                                                          'lower-GI mechanism distinct '
                                                          'from esophageal varices of '
                                                          'portal hypertension.'
                                                }},
                                               {'question': 'IBD alarm features '
                                                            'include?',
                                                'options': ['A) Occasional '
                                                            'postprandial bloating '
                                                            'alone',
                                                            'B) Bleeding, weight loss, '
                                                            'and nocturnal diarrhea',
                                                            'C) Infrequent soft stools '
                                                            'without systemic features',
                                                            'D) Mild intermittent '
                                                            'abdominal discomfort '
                                                            'without alarm signs'],
                                                'answer': 'B) Bleeding, weight loss, '
                                                          'and nocturnal diarrhea',
                                                'explanation': 'Alarm features in '
                                                               'suspected IBD include '
                                                               'rectal bleeding, '
                                                               'unintentional weight '
                                                               'loss, and nocturnal '
                                                               'diarrhea, which '
                                                               'increase likelihood of '
                                                               'inflammatory or '
                                                               'serious organic '
                                                               'disease and warrant '
                                                               'urgent investigation '
                                                               'rather than assuming '
                                                               'functional bowel '
                                                               'disease.',
                                                'choice_explanations': {
                                                    'A': 'Occasional postprandial '
                                                          'bloating alone is a common '
                                                          'functional symptom and is '
                                                          'not an IBD alarm feature.',
                                                    'B': 'Rectal bleeding, '
                                                          'unintentional weight loss, '
                                                          'and nocturnal diarrhea '
                                                          'increase likelihood of '
                                                          'inflammatory or serious '
                                                          'organic bowel disease and '
                                                          'warrant urgent '
                                                          'investigation.',
                                                    'C': 'Infrequent soft stools '
                                                          'without systemic features '
                                                          'lack the alarm signs that '
                                                          'raise concern for IBD.',
                                                    'D': 'Mild intermittent abdominal '
                                                          'discomfort without bleeding, '
                                                          'weight loss, or nocturnal '
                                                          'diarrhea does not constitute '
                                                          'IBD alarm features.'
                                                }}],
                                    'hard': [{'question': 'Reynolds pentad adds what '
                                                          'to Charcot triad?',
                                              'options': ['A) Isolated pruritus '
                                                          'without sepsis',
                                                          'B) Mild steatorrhea alone',
                                                          'C) Hypotension and mental '
                                                          'status change (confusion)',
                                                          'D) Asymptomatic '
                                                          'hyperbilirubinemia alone'],
                                              'answer': 'C) Hypotension and mental '
                                                        'status change (confusion)',
                                              'explanation': 'Reynolds pentad adds '
                                                             'hypotension and '
                                                             'confusion to Charcot '
                                                             'triad, indicating '
                                                             'cholangitis with septic '
                                                             'shock and organ '
                                                             'dysfunction. These '
                                                             'additions mark a '
                                                             'surgical/endoscopic '
                                                             'emergency beyond '
                                                             'uncomplicated biliary '
                                                             'colic or isolated '
                                                             'jaundice.',
                                              'choice_explanations': {
                                                  'A': 'Isolated pruritus from '
                                                        'cholestasis reflects bile-salt '
                                                        'deposition in skin without the '
                                                        'septic shock features of '
                                                        'Reynolds pentad.',
                                                  'B': 'Mild steatorrhea indicates fat '
                                                        'malabsorption and is not what '
                                                        'Reynolds pentad adds to '
                                                        'Charcot triad.',
                                                  'C': 'Reynolds pentad adds '
                                                        'hypotension and mental-status '
                                                        'change (confusion) to Charcot '
                                                        'triad, indicating cholangitis '
                                                        'with septic shock and organ '
                                                        'dysfunction.',
                                                  'D': 'Asymptomatic hyperbilirubinemia '
                                                        'alone lacks fever, pain, and '
                                                        'the septic features that '
                                                        'define Reynolds pentad.'
                                              }},
                                             {'question': 'SBP in ascites is diagnosed '
                                                          'by?',
                                              'options': ['A) Serum-ascites albumin '
                                                          'gradient alone without cell '
                                                          'count',
                                                          'B) Stool culture as the '
                                                          'primary SBP test',
                                                          'C) Abdominal wall '
                                                          'ultrasound without '
                                                          'paracentesis',
                                                          'D) Ascitic fluid PMN count '
                                                          'above diagnostic threshold '
                                                          'plus clinical context'],
                                              'answer': 'D) Ascitic fluid PMN count '
                                                        'above diagnostic threshold '
                                                        'plus clinical context',
                                              'explanation': 'Spontaneous bacterial '
                                                             'peritonitis is diagnosed '
                                                             'by ascitic fluid '
                                                             'analysis, typically an '
                                                             'absolute PMN count ≥250 '
                                                             'cells/µL in the '
                                                             'appropriate clinical '
                                                             'setting, often with '
                                                             'culture in blood-culture '
                                                             'bottles. SAAG classifies '
                                                             'portal hypertension; it '
                                                             'does not replace the '
                                                             'cell count for SBP.',
                                              'choice_explanations': {
                                                  'A': 'The serum-ascites albumin '
                                                        'gradient classifies portal '
                                                        'hypertension versus other '
                                                        'ascites causes but does not '
                                                        'replace ascitic PMN count for '
                                                        'diagnosing SBP.',
                                                  'B': 'Stool culture evaluates '
                                                        'intestinal pathogens and is '
                                                        'not the primary test for '
                                                        'spontaneous bacterial '
                                                        'peritonitis in ascitic fluid.',
                                                  'C': 'Abdominal wall ultrasound '
                                                        'without paracentesis cannot '
                                                        'measure ascitic neutrophil '
                                                        'counts needed to diagnose SBP.',
                                                  'D': 'Spontaneous bacterial '
                                                        'peritonitis is diagnosed by '
                                                        'ascitic fluid analysis, '
                                                        'typically an absolute PMN '
                                                        'count ≥250 cells/µL in the '
                                                        'appropriate clinical setting.'
                                              }},
                                             {'question': 'Boerhaave syndrome is?',
                                              'options': ['A) Full-thickness '
                                                          'esophageal perforation '
                                                          'after forceful vomiting',
                                                          'B) Partial mucosal tear of '
                                                          'Mallory-Weiss syndrome only',
                                                          'C) Spontaneous pneumothorax '
                                                          'unrelated to the esophagus',
                                                          'D) Perforated peptic ulcer '
                                                          'as the same entity'],
                                              'answer': 'A) Full-thickness esophageal '
                                                        'perforation after forceful '
                                                        'vomiting',
                                              'explanation': 'Boerhaave syndrome is '
                                                             'transmural esophageal '
                                                             'rupture, classically '
                                                             'after forceful vomiting, '
                                                             'causing mediastinitis '
                                                             'and septic shock. '
                                                             'Mallory-Weiss is a '
                                                             'mucosal tear with '
                                                             'bleeding; peptic '
                                                             'perforation and primary '
                                                             'pneumothorax are '
                                                             'different diagnoses.',
                                              'choice_explanations': {
                                                  'A': 'Boerhaave syndrome is '
                                                        'transmural esophageal rupture, '
                                                        'classically after forceful '
                                                        'vomiting, causing '
                                                        'mediastinitis and septic '
                                                        'shock.',
                                                  'B': 'Mallory–Weiss syndrome is a '
                                                        'partial mucosal tear at the '
                                                        'gastroesophageal junction that '
                                                        'causes bleeding without '
                                                        'full-thickness perforation.',
                                                  'C': 'Spontaneous pneumothorax is air '
                                                        'in the pleural space from '
                                                        'visceral pleural rupture and '
                                                        'is not esophageal perforation.',
                                                  'D': 'Perforated peptic ulcer is '
                                                        'full-thickness gastroduodenal '
                                                        'perforation into the '
                                                        'peritoneum, a different '
                                                        'anatomic entity from '
                                                        'esophageal Boerhaave rupture.'
                                              }}],
                                    'extreme': [{'question': 'Mesenteric ischemia '
                                                             'classic risk pattern?',
                                                 'options': ['A) Young patient with '
                                                             'chronic epigastric '
                                                             'burning relieved by food',
                                                             'B) Atrial fibrillation '
                                                             'with sudden severe '
                                                             'abdominal pain out of '
                                                             'proportion to '
                                                             'examination',
                                                             'C) Gradual '
                                                             'left-lower-quadrant pain '
                                                             'with diverticulosis risk '
                                                             'only',
                                                             'D) Biliary colic after '
                                                             'fatty meals without '
                                                             'vascular risk'],
                                                 'answer': 'B) Atrial fibrillation '
                                                           'with sudden severe '
                                                           'abdominal pain out of '
                                                           'proportion to examination',
                                                 'explanation': 'Acute mesenteric '
                                                                'ischemia from embolus '
                                                                'often occurs in AF: '
                                                                'sudden severe pain '
                                                                'out of proportion to '
                                                                'early physical '
                                                                'findings as bowel '
                                                                'becomes ischemic '
                                                                'before peritonitis '
                                                                'develops. Early CT '
                                                                'angiography and '
                                                                'revascularization '
                                                                'pathways are '
                                                                'critical.',
                                                 'choice_explanations': {
                                                     'A': 'Young patients with chronic '
                                                           'epigastric burning relieved '
                                                           'by food fit peptic ulcer '
                                                           'patterns, not embolic '
                                                           'mesenteric ischemia.',
                                                     'B': 'Acute mesenteric ischemia '
                                                           'from embolus often occurs '
                                                           'in atrial fibrillation: '
                                                           'sudden severe pain out of '
                                                           'proportion to early '
                                                           'physical findings as bowel '
                                                           'becomes ischemic before '
                                                           'peritonitis develops.',
                                                     'C': 'Gradual left-lower-quadrant '
                                                           'pain with diverticulosis '
                                                           'risk describes '
                                                           'diverticulitis, not sudden '
                                                           'embolic mesenteric '
                                                           'ischemia.',
                                                     'D': 'Biliary colic after fatty '
                                                           'meals is transient '
                                                           'cystic-duct obstruction by '
                                                           'gallstones without acute '
                                                           'mesenteric arterial '
                                                           'occlusion.'
                                                 }},
                                                {'question': 'Toxic megacolon is a '
                                                             'complication of?',
                                                 'options': ['A) Uncomplicated peptic '
                                                             'ulcer disease',
                                                             'B) Gilbert syndrome',
                                                             'C) Severe colitis such '
                                                             'as IBD flare or '
                                                             'Clostridioides difficile '
                                                             'infection',
                                                             'D) Mild gastroesophageal '
                                                             'reflux'],
                                                 'answer': 'C) Severe colitis such as '
                                                           'IBD flare or '
                                                           'Clostridioides difficile '
                                                           'infection',
                                                 'explanation': 'Toxic megacolon is '
                                                                'acute colonic '
                                                                'dilation with '
                                                                'systemic toxicity '
                                                                'complicating severe '
                                                                'colitis—classically '
                                                                'IBD or C. difficile. '
                                                                'It risks perforation '
                                                                'and requires urgent '
                                                                'medical/surgical '
                                                                'management, unlike '
                                                                'ulcer, Gilbert, or '
                                                                'reflux disease.',
                                                 'choice_explanations': {
                                                     'A': 'Uncomplicated peptic ulcer '
                                                           'is gastroduodenal mucosal '
                                                           'ulceration and does not '
                                                           'dilate the colon with '
                                                           'systemic toxicity of toxic '
                                                           'megacolon.',
                                                     'B': 'Gilbert syndrome is mild '
                                                           'unconjugated '
                                                           'hyperbilirubinemia from '
                                                           'reduced '
                                                           'glucuronyltransferase '
                                                           'activity, unrelated to '
                                                           'colonic dilation.',
                                                     'C': 'Toxic megacolon is acute '
                                                           'colonic dilation with '
                                                           'systemic toxicity '
                                                           'complicating severe '
                                                           'colitis—classically IBD '
                                                           'flare or Clostridioides '
                                                           'difficile—and risks '
                                                           'perforation.',
                                                     'D': 'Mild GERD is reflux '
                                                           'symptomology without '
                                                           'colitis or toxic colonic '
                                                           'dilation.'
                                                 }},
                                                {'question': 'Budd-Chiari involves?',
                                                 'options': ['A) Portal vein '
                                                             'thrombosis alone as the '
                                                             'identical syndrome',
                                                             'B) Extrahepatic '
                                                             'bile-duct stone without '
                                                             'venous occlusion',
                                                             'C) Hepatic artery '
                                                             'stenosis after '
                                                             'transplant as the '
                                                             'classic Budd-Chiari '
                                                             'definition',
                                                             'D) Hepatic venous '
                                                             'outflow obstruction'],
                                                 'answer': 'D) Hepatic venous outflow '
                                                           'obstruction',
                                                 'explanation': 'Budd-Chiari syndrome '
                                                                'is hepatic venous '
                                                                'outflow obstruction '
                                                                '(hepatic veins or '
                                                                'IVC), causing '
                                                                'congestion, '
                                                                'hepatomegaly, '
                                                                'ascites, and liver '
                                                                'dysfunction. Portal '
                                                                'vein thrombosis is a '
                                                                'related but distinct '
                                                                'vascular disorder; '
                                                                'biliary stones are '
                                                                'not venous outflow '
                                                                'disease.',
                                                 'choice_explanations': {
                                                     'A': 'Portal vein thrombosis '
                                                           'occludes portal inflow and '
                                                           'is a related but distinct '
                                                           'hepatic vascular disorder '
                                                           'from hepatic venous outflow '
                                                           'obstruction.',
                                                     'B': 'Extrahepatic bile-duct stone '
                                                           'causes '
                                                           'cholestasis/cholangitis and '
                                                           'is not hepatic venous '
                                                           'outflow occlusion.',
                                                     'C': 'Hepatic artery stenosis '
                                                           'after transplant is '
                                                           'arterial inflow disease, '
                                                           'not the classic definition '
                                                           'of Budd–Chiari hepatic '
                                                           'venous outflow obstruction.',
                                                     'D': 'Budd–Chiari syndrome is '
                                                           'hepatic venous outflow '
                                                           'obstruction (hepatic veins '
                                                           'or IVC), causing '
                                                           'congestion, hepatomegaly, '
                                                           'ascites, and liver '
                                                           'dysfunction.'
                                                 }}]},
                      'cases': {'easy': [{'title': 'RUQ Pain + Jaundice + Fever',
                                          'stem': 'A 50-year-old woman has RUQ pain, '
                                                  'fever, and jaundice.',
                                          'question': 'Likely diagnosis?',
                                          'answer': 'Ascending cholangitis.',
                                          'discussion': 'Antibiotics + biliary '
                                                        'drainage.',
                                          'book_hint': "Sleisenger / Harrison's GI"}],
                                'medium': [{'title': 'Alcohol + Epigastric Pain',
                                            'stem': 'A 40-year-old with heavy alcohol '
                                                    'use has severe epigastric pain to '
                                                    'the back and lipase 3× ULN.',
                                            'question': 'Diagnosis?',
                                            'answer': 'Acute pancreatitis.',
                                            'discussion': 'Supportive '
                                                          'fluids/analgesia; find '
                                                          'cause.',
                                            'book_hint': "Sleisenger / Harrison's GI"}],
                                'hard': [{'title': 'Coffee-Ground Emesis + Shock in '
                                                   'Cirrhosis',
                                          'stem': 'A cirrhotic patient vomits blood '
                                                  'and is hypotensive with tense '
                                                  'ascites. Labs and imaging are '
                                                  'pending; you must choose the safest '
                                                  'next clinical concept.',
                                          'question': 'Priorities?',
                                          'answer': 'ABCs/resuscitation, restrict '
                                                    'transfusion targets per protocol, '
                                                    'reverse coagulopathy '
                                                    'thoughtfully, antibiotics, '
                                                    'terlipressin/octreotide pathways, '
                                                    'urgent endoscopy.',
                                          'discussion': 'Variceal bleed until proven '
                                                        'otherwise.',
                                          'book_hint': "Sleisenger / Harrison's GI"}],
                                'extreme': [{'title': 'Pain Out of Proportion',
                                             'stem': 'An elderly patient with AF '
                                                     'develops sudden severe abdominal '
                                                     'pain but a soft abdomen early '
                                                     'on. Lactate rises. Multiple '
                                                     'teams are involved; prioritize '
                                                     'life/limb/vision threats and '
                                                     'avoid harmful premature '
                                                     'therapies.',
                                             'question': 'Fear which diagnosis?',
                                             'answer': 'Acute mesenteric ischemia — '
                                                       'urgent CT angiography and '
                                                       'surgical/interventional '
                                                       'pathway.',
                                             'discussion': 'Early exam can be falsely '
                                                           'reassuring.',
                                             'book_hint': "Sleisenger / Harrison's "
                                                          'GI'}]}},
 'endocrinology': {'label': 'Endocrinology',
                   'books': ['Williams Textbook of Endocrinology',
                             "Harrison's — Endocrinology",
                             "Greenspan's Basic & Clinical Endocrinology"],
                   'pdf_notes': ['DKA: hyperglycemia + ketones + acidosis; fluids, '
                                 'insulin, K+.',
                                 'Hashimoto → hypothyroidism; Graves → '
                                 'hyperthyroidism.',
                                 'Metformin first-line for many T2DM patients if eGFR '
                                 'allows.',
                                 'Hypocalcemia: Chvostek/Trousseau; check Mg and PTH.',
                                 'Adrenal crisis: shock + hyponatremia/hyperkalemia — '
                                 'give steroids/fluids urgently.'],
                   'questions': {'easy': [{'question': 'DKA includes?',
                                           'options': ['A) Hyperglycemia, '
                                                       'ketonemia/ketonuria, and '
                                                       'metabolic acidosis',
                                                       'B) Isolated hyperglycemia '
                                                       'without ketones or acidosis',
                                                       'C) Hypoglycemia with elevated '
                                                       'insulin alone',
                                                       'D) Hyperosmolar state without '
                                                       'acidosis or ketones as the DKA '
                                                       'definition'],
                                           'answer': 'A) Hyperglycemia, '
                                                     'ketonemia/ketonuria, and '
                                                     'metabolic acidosis',
                                           'explanation': 'Diabetic ketoacidosis '
                                                          'combines absolute/relative '
                                                          'insulin deficiency with '
                                                          'counter-regulatory hormone '
                                                          'excess, producing '
                                                          'hyperglycemia, ketone '
                                                          'generation, and '
                                                          'high-anion-gap metabolic '
                                                          'acidosis. Isolated '
                                                          'hyperglycemia or HHS '
                                                          'without significant '
                                                          'ketoacidosis are different '
                                                          'entities.',
                                           'choice_explanations': {
                                               'A': 'Diabetic ketoacidosis combines '
                                                     'absolute/relative insulin '
                                                     'deficiency with '
                                                     'counter-regulatory hormone '
                                                     'excess, producing hyperglycemia, '
                                                     'ketone generation, and '
                                                     'high-anion-gap metabolic '
                                                     'acidosis.',
                                               'B': 'Isolated hyperglycemia without '
                                                     'ketones or acidosis may be '
                                                     'uncontrolled diabetes or stress '
                                                     'hyperglycemia but does not '
                                                     'fulfill the DKA triad.',
                                               'C': 'Hypoglycemia with elevated insulin '
                                                     'suggests hyperinsulinemic '
                                                     'hypoglycemia (e.g., insulinoma or '
                                                     'exogenous insulin), the opposite '
                                                     'metabolic state from DKA.',
                                               'D': 'Hyperosmolar state without '
                                                     'significant acidosis or ketones '
                                                     'defines HHS, which is distinct '
                                                     'from DKA’s prominent '
                                                     'ketoacidosis.'
                                           }},
                                          {'question': 'First-line drug often for '
                                                       'T2DM?',
                                           'options': ['A) Immediate insulin pump '
                                                       'therapy for all new T2DM',
                                                       'B) Metformin when not '
                                                       'contraindicated',
                                                       'C) High-dose glucocorticoid as '
                                                       'glucose-lowering therapy',
                                                       'D) Somatostatin analogue as '
                                                       'first-line oral agent'],
                                           'answer': 'B) Metformin when not '
                                                     'contraindicated',
                                           'explanation': 'Metformin is guideline '
                                                          'first-line pharmacotherapy '
                                                          'for many adults with type 2 '
                                                          'diabetes when eGFR and '
                                                          'tolerability allow, '
                                                          'improving insulin '
                                                          'sensitivity and lowering '
                                                          'hepatic glucose output. '
                                                          'Insulin pumps, steroids, '
                                                          'and somatostatin analogues '
                                                          'are not standard first-line '
                                                          'T2DM drugs.',
                                           'choice_explanations': {
                                               'A': 'Immediate insulin pump therapy is '
                                                     'intensive insulin delivery used '
                                                     'in selected type 1 or advanced '
                                                     'diabetes care, not routine '
                                                     'first-line pharmacotherapy for '
                                                     'new T2DM.',
                                               'B': 'Metformin is guideline first-line '
                                                     'pharmacotherapy for many adults '
                                                     'with type 2 diabetes when eGFR '
                                                     'and tolerability allow, improving '
                                                     'insulin sensitivity and lowering '
                                                     'hepatic glucose output.',
                                               'C': 'High-dose glucocorticoids raise '
                                                     'glucose via gluconeogenesis and '
                                                     'insulin resistance and are not '
                                                     'glucose-lowering therapy.',
                                               'D': 'Somatostatin analogues suppress '
                                                     'hormone secretion in '
                                                     'neuroendocrine tumors and are not '
                                                     'first-line oral agents for T2DM.'
                                           }},
                                          {'question': 'Primary hypothyroidism labs '
                                                       'usually show?',
                                           'options': ['A) Suppressed TSH with high '
                                                       'free T4',
                                                       'B) Normal TSH with high free '
                                                       'T4',
                                                       'C) Elevated TSH with low free '
                                                       'T4',
                                                       'D) Low TSH with low free T4 as '
                                                       'the typical primary pattern'],
                                           'answer': 'C) Elevated TSH with low free T4',
                                           'explanation': 'Primary hypothyroidism is '
                                                          'failure of the thyroid '
                                                          'gland; pituitary TSH rises '
                                                          'in response while free T4 '
                                                          'falls. Suppressed TSH with '
                                                          'high T4 indicates '
                                                          'hyperthyroidism; low TSH '
                                                          'with low T4 suggests '
                                                          'central (secondary) '
                                                          'hypothyroidism.',
                                           'choice_explanations': {
                                               'A': 'Suppressed TSH with high free T4 '
                                                     'indicates primary hyperthyroidism '
                                                     'with negative feedback on the '
                                                     'pituitary, not primary '
                                                     'hypothyroidism.',
                                               'B': 'Normal TSH with high free T4 is '
                                                     'inconsistent with typical primary '
                                                     'hypothyroidism and may suggest '
                                                     'assay artifact or rare thyroid '
                                                     'hormone resistance patterns.',
                                               'C': 'Primary hypothyroidism is thyroid '
                                                     'gland failure; pituitary TSH '
                                                     'rises while free T4 falls, '
                                                     'yielding elevated TSH with low '
                                                     'free T4.',
                                               'D': 'Low TSH with low free T4 suggests '
                                                     'central (secondary) '
                                                     'hypothyroidism from '
                                                     'pituitary/hypothalamic failure, '
                                                     'not the high-TSH primary pattern.'
                                           }}],
                                 'medium': [{'question': 'Chvostek/Trousseau suggest?',
                                             'options': ['A) Hypercalcemia of '
                                                         'malignancy',
                                                         'B) Isolated hyperkalemia '
                                                         'without calcium change',
                                                         'C) Hyponatremia from SIADH',
                                                         'D) Hypocalcemia'],
                                             'answer': 'D) Hypocalcemia',
                                             'explanation': 'Chvostek and Trousseau '
                                                            'signs reflect '
                                                            'neuromuscular '
                                                            'irritability from low '
                                                            'ionized calcium. '
                                                            'Hypercalcemia tends to '
                                                            'cause the opposite '
                                                            '(lethargy, polyuria); '
                                                            'potassium and sodium '
                                                            'disorders have different '
                                                            'neuromuscular '
                                                            'signatures.',
                                             'choice_explanations': {
                                                 'A': 'Hypercalcemia of malignancy '
                                                       'tends to cause lethargy, '
                                                       'polyuria, and reduced '
                                                       'neuromuscular excitability—the '
                                                       'opposite of Chvostek/Trousseau '
                                                       'irritability.',
                                                 'B': 'Isolated hyperkalemia affects '
                                                       'cardiac conduction and muscle '
                                                       'membrane potential but does not '
                                                       'produce the classic Chvostek '
                                                       'and Trousseau signs of low '
                                                       'ionized calcium.',
                                                 'C': 'Hyponatremia from SIADH causes '
                                                       'neurologic symptoms from '
                                                       'hypo-osmolality, not the '
                                                       'peripheral neuromuscular '
                                                       'irritability signs of '
                                                       'hypocalcemia.',
                                                 'D': 'Chvostek and Trousseau signs '
                                                       'reflect neuromuscular '
                                                       'irritability from low ionized '
                                                       'calcium, with facial twitching '
                                                       'and carpal spasm on occlusive '
                                                       'ischemia.'
                                             }},
                                            {'question': 'Graves disease is a cause '
                                                         'of?',
                                             'options': ['A) Hyperthyroidism '
                                                         '(thyrotoxicosis)',
                                                         'B) Primary hypothyroidism '
                                                         'from gland failure',
                                                         'C) Central diabetes '
                                                         'insipidus',
                                                         'D) Primary adrenal '
                                                         'insufficiency as the main '
                                                         'Graves effect'],
                                             'answer': 'A) Hyperthyroidism '
                                                       '(thyrotoxicosis)',
                                             'explanation': 'Graves disease is '
                                                            'TSH-receptor-stimulating '
                                                            'antibody–mediated '
                                                            'hyperthyroidism with '
                                                            'goiter and often '
                                                            'orbitopathy. It raises '
                                                            'thyroid hormone '
                                                            'production rather than '
                                                            'causing primary '
                                                            'hypothyroidism, DI, or '
                                                            'Addison disease as its '
                                                            'core lesion.',
                                             'choice_explanations': {
                                                 'A': 'Graves disease is '
                                                       'TSH-receptor–stimulating '
                                                       'antibody–mediated '
                                                       'hyperthyroidism with goiter and '
                                                       'often orbitopathy, raising '
                                                       'thyroid hormone production.',
                                                 'B': 'Primary hypothyroidism from '
                                                       'gland failure is the opposite '
                                                       'thyroid state; Graves causes '
                                                       'thyrotoxicosis, not primary '
                                                       'gland failure.',
                                                 'C': 'Central diabetes insipidus is '
                                                       'ADH deficiency causing dilute '
                                                       'polyuria and is unrelated to '
                                                       'Graves TSH-receptor '
                                                       'stimulation.',
                                                 'D': 'Primary adrenal insufficiency is '
                                                       'cortisol/aldosterone deficiency '
                                                       'from adrenal destruction and is '
                                                       'not the main effect of Graves '
                                                       'disease.'
                                             }},
                                            {'question': 'Adrenal crisis needs?',
                                             'options': ['A) Fluid restriction as the '
                                                         'primary intervention',
                                                         'B) Urgent glucocorticoids '
                                                         'plus volume resuscitation',
                                                         'C) High-dose insulin '
                                                         'infusion without steroid '
                                                         'replacement',
                                                         'D) Radioiodine ablation '
                                                         'during shock'],
                                             'answer': 'B) Urgent glucocorticoids plus '
                                                       'volume resuscitation',
                                             'explanation': 'Adrenal crisis is '
                                                            'life-threatening cortisol '
                                                            'deficiency with shock and '
                                                            'electrolyte disturbance. '
                                                            'Immediate IV '
                                                            'hydrocortisone and '
                                                            'aggressive saline '
                                                            'resuscitation are '
                                                            'required; delay for '
                                                            'confirmatory testing is '
                                                            'dangerous once the '
                                                            'diagnosis is suspected.',
                                             'choice_explanations': {
                                                 'A': 'Fluid restriction worsens '
                                                       'hypovolemic shock of adrenal '
                                                       'crisis; volume expansion with '
                                                       'saline is required alongside '
                                                       'steroids.',
                                                 'B': 'Adrenal crisis is '
                                                       'life-threatening cortisol '
                                                       'deficiency with shock and '
                                                       'electrolyte disturbance; '
                                                       'immediate IV hydrocortisone and '
                                                       'aggressive saline resuscitation '
                                                       'are required.',
                                                 'C': 'High-dose insulin treats '
                                                       'hyperglycemia/hyperkalemia '
                                                       'contexts and does not replace '
                                                       'missing glucocorticoids in '
                                                       'adrenal crisis.',
                                                 'D': 'Radioiodine ablates thyroid '
                                                       'tissue in hyperthyroidism and '
                                                       'has no role during adrenal '
                                                       'shock.'
                                             }}],
                                 'hard': [{'question': 'HHS differs from DKA by?',
                                           'options': ['A) Prominent high-anion-gap '
                                                       'ketoacidosis as the defining '
                                                       'HHS feature',
                                                       'B) Severe hypoglycemia as the '
                                                       'usual presenting lab pattern',
                                                       'C) Marked hyperosmolarity with '
                                                       'little or no ketoacidosis',
                                                       'D) Isolated hyponatremia '
                                                       'without hyperglycemia'],
                                           'answer': 'C) Marked hyperosmolarity with '
                                                     'little or no ketoacidosis',
                                           'explanation': 'Hyperosmolar hyperglycemic '
                                                          'state features extreme '
                                                          'hyperglycemia and '
                                                          'hyperosmolarity with '
                                                          'profound dehydration, '
                                                          'typically with absent or '
                                                          'minimal ketosis—contrasting '
                                                          "with DKA's prominent "
                                                          'ketoacidosis. Management '
                                                          'emphasizes careful fluid '
                                                          'and electrolyte correction '
                                                          'plus insulin.',
                                           'choice_explanations': {
                                               'A': 'Prominent high-anion-gap '
                                                     'ketoacidosis defines DKA, whereas '
                                                     'HHS is characterized by little or '
                                                     'no ketoacidosis.',
                                               'B': 'Severe hypoglycemia is low glucose '
                                                     'and is not the presenting lab '
                                                     'pattern of HHS, which features '
                                                     'extreme hyperglycemia.',
                                               'C': 'Hyperosmolar hyperglycemic state '
                                                     'features extreme hyperglycemia '
                                                     'and hyperosmolarity with profound '
                                                     'dehydration and typically absent '
                                                     'or minimal ketosis.',
                                               'D': 'Isolated hyponatremia without '
                                                     'hyperglycemia does not define '
                                                     'HHS, which is driven by marked '
                                                     'hyperglycemia and effective '
                                                     'hyperosmolarity.'
                                           }},
                                          {'question': 'Sick euthyroid pattern often '
                                                       'shows?',
                                           'options': ['A) High free T4 with '
                                                       'suppressed TSH as the '
                                                       'sick-euthyroid hallmark',
                                                       'B) Very high TSH with '
                                                       'rock-bottom free T4 as the '
                                                       'typical nonthyroidal pattern',
                                                       'C) Isolated elevated '
                                                       'thyroglobulin as the defining '
                                                       'finding',
                                                       'D) Low T3 during systemic '
                                                       'illness without necessarily '
                                                       'indicating primary thyroid '
                                                       'disease'],
                                           'answer': 'D) Low T3 during systemic '
                                                     'illness without necessarily '
                                                     'indicating primary thyroid '
                                                     'disease',
                                           'explanation': 'Nonthyroidal illness (sick '
                                                          'euthyroid) commonly lowers '
                                                          'T3 via reduced peripheral '
                                                          'conversion during critical '
                                                          'illness; TSH and T4 may '
                                                          'also change, but this does '
                                                          'not automatically equal '
                                                          'primary thyroid failure. '
                                                          'Interpretation requires '
                                                          'clinical context once the '
                                                          'acute illness resolves.',
                                           'choice_explanations': {
                                               'A': 'High free T4 with suppressed TSH '
                                                     'is the hallmark of '
                                                     'thyrotoxicosis, not the typical '
                                                     'nonthyroidal illness (sick '
                                                     'euthyroid) pattern.',
                                               'B': 'Very high TSH with rock-bottom '
                                                     'free T4 indicates primary '
                                                     'hypothyroidism rather than the '
                                                     'usual sick-euthyroid '
                                                     'constellation during systemic '
                                                     'illness.',
                                               'C': 'Isolated elevated thyroglobulin '
                                                     'reflects thyroid tissue mass or '
                                                     'injury and is not the defining '
                                                     'finding of sick euthyroid '
                                                     'syndrome.',
                                               'D': 'Nonthyroidal illness commonly '
                                                     'lowers T3 via reduced peripheral '
                                                     'T4-to-T3 conversion during '
                                                     'critical illness without '
                                                     'necessarily indicating primary '
                                                     'thyroid disease.'
                                           }},
                                          {'question': 'Pheochromocytoma classic '
                                                       'spells?',
                                           'options': ['A) Paroxysmal headache, '
                                                       'palpitations, and sweating '
                                                       'with hypertension',
                                                       'B) Painless progressive weight '
                                                       'gain with moon facies alone',
                                                       'C) Cold intolerance and '
                                                       'delayed reflexes alone',
                                                       'D) Polyuria and polydipsia '
                                                       'from osmotic diuresis alone'],
                                           'answer': 'A) Paroxysmal headache, '
                                                     'palpitations, and sweating with '
                                                     'hypertension',
                                           'explanation': 'Pheochromocytoma '
                                                          'episodically releases '
                                                          'catecholamines, producing '
                                                          'the classic spell of '
                                                          'headache, palpitations, and '
                                                          'diaphoresis with '
                                                          'hypertension. Cushingoid '
                                                          'habitus, hypothyroid '
                                                          'features, and osmotic '
                                                          'polyuria point to other '
                                                          'endocrine disorders.',
                                           'choice_explanations': {
                                               'A': 'Pheochromocytoma episodically '
                                                     'releases catecholamines, '
                                                     'producing classic spells of '
                                                     'headache, palpitations, and '
                                                     'diaphoresis with hypertension.',
                                               'B': 'Painless progressive weight gain '
                                                     'with moon facies describes '
                                                     'Cushing syndrome from '
                                                     'glucocorticoid excess, not '
                                                     'catecholamine spells.',
                                               'C': 'Cold intolerance and delayed '
                                                     'reflexes are hypothyroid features '
                                                     'from low thyroid hormone, not '
                                                     'paroxysmal catecholamine release.',
                                               'D': 'Polyuria and polydipsia from '
                                                     'osmotic diuresis reflect '
                                                     'hyperglycemia, not the adrenergic '
                                                     'spell triad of pheochromocytoma.'
                                           }}],
                                 'extreme': [{'question': 'Myxedema coma treatment '
                                                          'concept?',
                                              'options': ['A) Outpatient oral '
                                                          'levothyroxine increase '
                                                          'alone without supportive '
                                                          'care',
                                                          'B) ICU-level care with '
                                                          'thyroid hormone '
                                                          'replacement, supportive '
                                                          'measures, and steroids if '
                                                          'concurrent adrenal '
                                                          'insufficiency is possible',
                                                          'C) Passive warming only '
                                                          'without hormone replacement',
                                                          'D) Iodine loading without '
                                                          'hormone replacement or '
                                                          'supportive care'],
                                              'answer': 'B) ICU-level care with '
                                                        'thyroid hormone replacement, '
                                                        'supportive measures, and '
                                                        'steroids if concurrent '
                                                        'adrenal insufficiency is '
                                                        'possible',
                                              'explanation': 'Myxedema coma is '
                                                             'decompensated '
                                                             'hypothyroidism with '
                                                             'hypothermia, altered '
                                                             'mentation, and organ '
                                                             'dysfunction. Management '
                                                             'is ICU supportive care '
                                                             'plus thyroid hormone; '
                                                             'empiric glucocorticoids '
                                                             'are given until adrenal '
                                                             'insufficiency is '
                                                             'excluded because '
                                                             'concurrent AI can '
                                                             'coexist (e.g., '
                                                             'hypopituitarism).',
                                              'choice_explanations': {
                                                  'A': 'Outpatient oral levothyroxine '
                                                        'alone without ICU support is '
                                                        'inadequate for myxedema coma '
                                                        'with hypothermia, '
                                                        'hypoventilation, and organ '
                                                        'dysfunction.',
                                                  'B': 'Myxedema coma is decompensated '
                                                        'hypothyroidism requiring ICU '
                                                        'supportive care plus thyroid '
                                                        'hormone; empiric '
                                                        'glucocorticoids are given '
                                                        'until adrenal insufficiency is '
                                                        'excluded.',
                                                  'C': 'Passive warming alone does not '
                                                        'replace missing thyroid '
                                                        'hormone or treat '
                                                        'respiratory/circulatory '
                                                        'failure of myxedema coma.',
                                                  'D': 'Iodine loading without hormone '
                                                        'replacement does not reverse '
                                                        'decompensated hypothyroidism '
                                                        'and is not appropriate primary '
                                                        'therapy.'
                                              }},
                                             {'question': 'Thyroid storm clinical '
                                                          'diagnosis needs?',
                                              'options': ['A) Mild TSH suppression '
                                                          'without clinical '
                                                          'thyrotoxicosis',
                                                          'B) Isolated anxiety without '
                                                          'fever, tachycardia, or '
                                                          'organ dysfunction',
                                                          'C) Severe thyrotoxicosis '
                                                          'with systemic '
                                                          'decompensation '
                                                          '(thermoregulatory, '
                                                          'cardiovascular, CNS)',
                                                          'D) Subclinical '
                                                          'hypothyroidism alone'],
                                              'answer': 'C) Severe thyrotoxicosis with '
                                                        'systemic decompensation '
                                                        '(thermoregulatory, '
                                                        'cardiovascular, CNS)',
                                              'explanation': 'Thyroid storm is a '
                                                             'clinical diagnosis of '
                                                             'life-threatening '
                                                             'thyrotoxicosis with '
                                                             'multiorgan '
                                                             'decompensation (fever, '
                                                             'tachyarrhythmia, CNS/GI '
                                                             'dysfunction). Scoring '
                                                             'systems aid recognition, '
                                                             'but treatment must not '
                                                             'await a single lab '
                                                             'threshold once the '
                                                             'syndrome is evident.',
                                              'choice_explanations': {
                                                  'A': 'Mild TSH suppression without '
                                                        'clinical thyrotoxicosis may be '
                                                        'subclinical hyperthyroidism '
                                                        'and lacks the multiorgan '
                                                        'decompensation of thyroid '
                                                        'storm.',
                                                  'B': 'Isolated anxiety without fever, '
                                                        'tachycardia, or organ '
                                                        'dysfunction is not thyroid '
                                                        'storm, which is '
                                                        'life-threatening thyrotoxic '
                                                        'decompensation.',
                                                  'C': 'Thyroid storm is a clinical '
                                                        'diagnosis of severe '
                                                        'thyrotoxicosis with systemic '
                                                        'decompensation affecting '
                                                        'thermoregulation, '
                                                        'cardiovascular, and CNS '
                                                        'systems.',
                                                  'D': 'Subclinical hypothyroidism is '
                                                        'elevated TSH with normal free '
                                                        'T4 and is the opposite thyroid '
                                                        'state from storm.'
                                              }},
                                             {'question': 'Insulinoma Whipple triad?',
                                              'options': ['A) Hyperglycemia with '
                                                          'ketones as the diagnostic '
                                                          'triad',
                                                          'B) Hypertension spells with '
                                                          'catecholamine excess alone',
                                                          'C) Weight loss with free T4 '
                                                          'elevation alone',
                                                          'D) Hypoglycemic symptoms, '
                                                          'documented low glucose, and '
                                                          'relief with glucose '
                                                          'administration'],
                                              'answer': 'D) Hypoglycemic symptoms, '
                                                        'documented low glucose, and '
                                                        'relief with glucose '
                                                        'administration',
                                              'explanation': "Whipple's triad supports "
                                                             'true hypoglycemia: '
                                                             'symptoms consistent with '
                                                             'low glucose, a low '
                                                             'measured glucose, and '
                                                             'resolution when glucose '
                                                             'is raised. Insulinoma is '
                                                             'a classic endogenous '
                                                             'hyperinsulinemic cause '
                                                             'once factitious and '
                                                             'other etiologies are '
                                                             'considered.',
                                              'choice_explanations': {
                                                  'A': 'Hyperglycemia with ketones '
                                                        'describes uncontrolled '
                                                        'diabetes/DKA physiology, not '
                                                        'Whipple’s triad of '
                                                        'hypoglycemia.',
                                                  'B': 'Hypertension spells with '
                                                        'catecholamine excess describe '
                                                        'pheochromocytoma, not the '
                                                        'hypoglycemic Whipple triad.',
                                                  'C': 'Weight loss with free T4 '
                                                        'elevation indicates '
                                                        'thyrotoxicosis, not documented '
                                                        'hypoglycemia relieved by '
                                                        'glucose.',
                                                  'D': 'Whipple’s triad supports true '
                                                        'hypoglycemia: symptoms '
                                                        'consistent with low glucose, a '
                                                        'documented low glucose, and '
                                                        'resolution when glucose is '
                                                        'raised.'
                                              }}]},
                   'cases': {'easy': [{'title': 'Polyuria + Kussmaul',
                                       'stem': 'A teen has polyuria, weight loss, '
                                               'Kussmaul breathing, glucose 430, pH '
                                               '7.15, urine ketones+++.',
                                       'question': 'Diagnosis?',
                                       'answer': 'DKA.',
                                       'discussion': 'Fluids, insulin, K+ care.',
                                       'book_hint': 'Williams Endocrinology'}],
                             'medium': [{'title': 'Heat Intolerance + Weight Loss',
                                         'stem': 'A 29-year-old has heat intolerance, '
                                                 'tremor, weight loss, diffuse goiter; '
                                                 'TSH suppressed, free T4 high.',
                                         'question': 'Category?',
                                         'answer': 'Thyrotoxicosis (e.g., Graves).',
                                         'discussion': 'Beta-blocker + antithyroid '
                                                       'strategy after workup.',
                                         'book_hint': 'Williams Endocrinology'}],
                             'hard': [{'title': 'Steroid-Dependent Patient Vomiting',
                                       'stem': 'A patient on chronic prednisone for '
                                               'autoimmune disease has '
                                               'gastroenteritis, hypotension, and '
                                               'hyponatremia. Labs and imaging are '
                                               'pending; you must choose the safest '
                                               'next clinical concept.',
                                       'question': 'What emergency?',
                                       'answer': 'Adrenal crisis risk — give '
                                                 'stress-dose steroids and IV fluids '
                                                 'while investigating.',
                                       'discussion': 'Never stop chronic steroids '
                                                     'abruptly.',
                                       'book_hint': 'Williams Endocrinology'}],
                             'extreme': [{'title': 'Thyroid Storm',
                                          'stem': 'A woman with untreated '
                                                  'hyperthyroidism develops fever, '
                                                  'delirium, tachyarrhythmia, and '
                                                  'vomiting after surgery. Multiple '
                                                  'teams are involved; prioritize '
                                                  'life/limb/vision threats and avoid '
                                                  'harmful premature therapies.',
                                          'question': 'Management concept?',
                                          'answer': 'Thyroid storm: supportive ICU '
                                                    'care, beta-blockade, antithyroid '
                                                    'drugs, iodine after thionamide, '
                                                    'steroids, treat trigger.',
                                          'discussion': 'Delay kills.',
                                          'book_hint': 'Williams Endocrinology'}]}},
 'nephrology': {'label': 'Nephrology',
                'books': ["Brenner & Rector's The Kidney",
                          "Harrison's — Nephrology",
                          'Comprehensive Clinical Nephrology — Feehally'],
                'pdf_notes': ['AKI types: pre-renal, intrinsic (ATN/AIN/GN), '
                              'post-renal.',
                              'Nephritic vs nephrotic: active sediment/HTN vs heavy '
                              'protein/edema.',
                              'Diabetic kidney disease: ACEI/ARB cornerstone with '
                              'glycemic/BP control.',
                              'eGFR guides drug dosing and CKD staging.',
                              'Hyperkalemia emergencies: ECG changes → calcium, shift, '
                              'remove K+.'],
                'questions': {'easy': [{'question': 'eGFR estimates?',
                                        'options': ['A) Kidney filtration function '
                                                    '(glomerular filtration rate)',
                                                    'B) Tubular concentrating ability '
                                                    'alone',
                                                    'C) Renal artery stenosis severity '
                                                    'by velocity alone',
                                                    'D) Bladder detrusor '
                                                    'contractility'],
                                        'answer': 'A) Kidney filtration function '
                                                  '(glomerular filtration rate)',
                                        'explanation': 'eGFR estimates glomerular '
                                                       'filtration rate from '
                                                       'creatinine (and sometimes '
                                                       'cystatin C) using demographic '
                                                       'variables. It reflects '
                                                       'filtration capacity, not '
                                                       'primarily concentrating '
                                                       'ability, renal-artery Doppler '
                                                       'stenosis grading, or bladder '
                                                       'function.',
                                        'choice_explanations': {
                                            'A': 'eGFR estimates glomerular filtration '
                                                  'rate from creatinine (and sometimes '
                                                  'cystatin C) using demographic '
                                                  'variables, reflecting kidney '
                                                  'filtration function.',
                                            'B': 'Tubular concentrating ability is '
                                                  'assessed by urine '
                                                  'osmolality/specific gravity '
                                                  'responses, not by the '
                                                  'creatinine-based eGFR filtration '
                                                  'estimate.',
                                            'C': 'Renal artery stenosis severity by '
                                                  'velocity is a Doppler ultrasound '
                                                  'hemodynamic assessment, not an eGFR '
                                                  'filtration estimate.',
                                            'D': 'Bladder detrusor contractility is a '
                                                  'urodynamic property of the bladder '
                                                  'muscle and is unrelated to '
                                                  'glomerular filtration estimation.'
                                        }},
                                       {'question': 'Nephrotic syndrome features '
                                                    'heavy?',
                                        'options': ['A) Isolated microscopic hematuria '
                                                    'without protein loss',
                                                    'B) Proteinuria (typically ≥3.5 '
                                                    'g/day) with hypoalbuminemia and '
                                                    'edema',
                                                    'C) Sterile pyuria alone',
                                                    'D) Mild reduction in eGFR without '
                                                    'protein leak'],
                                        'answer': 'B) Proteinuria (typically ≥3.5 '
                                                  'g/day) with hypoalbuminemia and '
                                                  'edema',
                                        'explanation': 'Nephrotic syndrome is defined '
                                                       'by heavy proteinuria, '
                                                       'hypoalbuminemia, edema, and '
                                                       'often hyperlipidemia from '
                                                       'glomerular barrier failure. '
                                                       'Isolated hematuria or pyuria '
                                                       'without heavy protein loss '
                                                       'indicates other glomerular or '
                                                       'interstitial patterns.',
                                        'choice_explanations': {
                                            'A': 'Isolated microscopic hematuria '
                                                  'without heavy protein loss indicates '
                                                  'glomerular or lower-tract bleeding '
                                                  'patterns other than nephrotic '
                                                  'syndrome.',
                                            'B': 'Nephrotic syndrome is defined by '
                                                  'heavy proteinuria (typically ≥3.5 '
                                                  'g/day), hypoalbuminemia, and edema '
                                                  'from glomerular barrier failure, '
                                                  'often with hyperlipidemia.',
                                            'C': 'Sterile pyuria suggests interstitial '
                                                  'inflammation or partially treated '
                                                  'infection, not the heavy protein '
                                                  'leak of nephrotic syndrome.',
                                            'D': 'Mild eGFR reduction without protein '
                                                  'leak is reduced filtration alone and '
                                                  'does not fulfill nephrotic-range '
                                                  'proteinuria with hypoalbuminemia.'
                                        }},
                                       {'question': 'ACEI/ARB are preferred in?',
                                        'options': ['A) Bilateral renal artery '
                                                    'stenosis as first-line ACEI '
                                                    'indication without caution',
                                                    'B) Acute hyperkalemia with anuria '
                                                    'as the preferred start setting',
                                                    'C) Diabetic kidney disease with '
                                                    'albuminuria',
                                                    'D) Pregnancy as a routine '
                                                    'initiation setting'],
                                        'answer': 'C) Diabetic kidney disease with '
                                                  'albuminuria',
                                        'explanation': 'ACE inhibitors and ARBs reduce '
                                                       'intraglomerular pressure and '
                                                       'albuminuria and slow diabetic '
                                                       'CKD progression when monitored '
                                                       'for creatinine and potassium. '
                                                       'They are contraindicated or '
                                                       'used with extreme caution in '
                                                       'bilateral RAS, advanced '
                                                       'hyperkalemia, and pregnancy.',
                                        'choice_explanations': {
                                            'A': 'Bilateral renal artery stenosis is a '
                                                  'setting of caution or '
                                                  'contraindication for ACEI/ARB '
                                                  'because efferent dilation can '
                                                  'critically drop filtration pressure.',
                                            'B': 'Acute hyperkalemia with anuria is a '
                                                  'reason to avoid starting ACEI/ARB, '
                                                  'which can worsen potassium '
                                                  'retention, not a preferred '
                                                  'initiation setting.',
                                            'C': 'ACE inhibitors and ARBs reduce '
                                                  'intraglomerular pressure and '
                                                  'albuminuria and slow diabetic CKD '
                                                  'progression when creatinine and '
                                                  'potassium are monitored.',
                                            'D': 'ACEI/ARB are teratogenic and '
                                                  'contraindicated in pregnancy, so '
                                                  'pregnancy is not a routine '
                                                  'initiation setting.'
                                        }}],
                              'medium': [{'question': 'RBC casts suggest?',
                                          'options': ['A) Acute tubular necrosis',
                                                      'B) Postrenal obstruction alone',
                                                      'C) Simple orthostatic '
                                                      'proteinuria',
                                                      'D) Glomerulonephritis'],
                                          'answer': 'D) Glomerulonephritis',
                                          'explanation': 'RBC casts form when '
                                                         'erythrocytes leak through '
                                                         'damaged glomeruli and become '
                                                         'embedded in Tamm–Horsfall '
                                                         'protein in tubules—highly '
                                                         'suggestive of '
                                                         'glomerulonephritis. ATN '
                                                         'shows muddy-brown granular '
                                                         'casts; obstruction lacks '
                                                         'active urinary sediment of '
                                                         'that type.',
                                          'choice_explanations': {
                                              'A': 'Acute tubular necrosis classically '
                                                    'shows muddy-brown granular casts '
                                                    'from tubular epithelial debris, '
                                                    'not RBC casts of glomerular '
                                                    'bleeding.',
                                              'B': 'Postrenal obstruction alone '
                                                    'typically lacks an active '
                                                    'glomerular sediment with RBC '
                                                    'casts.',
                                              'C': 'Simple orthostatic proteinuria is '
                                                    'benign positional protein leak '
                                                    'without RBC cast formation from '
                                                    'glomerulonephritis.',
                                              'D': 'RBC casts form when erythrocytes '
                                                    'leak through damaged glomeruli and '
                                                    'embed in Tamm–Horsfall protein in '
                                                    'tubules, highly suggestive of '
                                                    'glomerulonephritis.'
                                          }},
                                         {'question': 'Post-renal AKI first check?',
                                          'options': ['A) Urinary tract obstruction '
                                                      '(bladder scan / renal '
                                                      'ultrasound)',
                                                      'B) Immediate kidney biopsy '
                                                      'before excluding obstruction',
                                                      'C) Empiric high-dose loop '
                                                      'diuretic without assessing '
                                                      'retention',
                                                      'D) Assuming prerenal azotemia '
                                                      'without imaging when retention '
                                                      'is possible'],
                                          'answer': 'A) Urinary tract obstruction '
                                                    '(bladder scan / renal ultrasound)',
                                          'explanation': 'Postrenal AKI is reversible '
                                                         'if obstruction is relieved '
                                                         'promptly. Bladder '
                                                         'catheterization/scan and '
                                                         'ultrasound look for '
                                                         'hydronephrosis or retention '
                                                         'before invasive workups. '
                                                         'Missing obstruction while '
                                                         'pursuing biopsy or diuresis '
                                                         'delays salvage of renal '
                                                         'function.',
                                          'choice_explanations': {
                                              'A': 'Postrenal AKI is reversible if '
                                                    'obstruction is relieved promptly; '
                                                    'bladder scan/catheterization and '
                                                    'renal ultrasound look for '
                                                    'retention or hydronephrosis first.',
                                              'B': 'Immediate kidney biopsy before '
                                                    'excluding obstruction risks '
                                                    'missing a rapidly reversible '
                                                    'postrenal cause and delays '
                                                    'decompression.',
                                              'C': 'Empiric high-dose loop diuretic '
                                                    'without assessing retention may '
                                                    'worsen volume status if the '
                                                    'problem is obstruction rather than '
                                                    'fluid overload.',
                                              'D': 'Assuming prerenal azotemia without '
                                                    'imaging when retention is possible '
                                                    'can miss obstructive uropathy that '
                                                    'needs drainage.'
                                          }},
                                         {'question': 'Hyperkalemia with peaked T '
                                                      'waves needs?',
                                          'options': ['A) Oral sodium polystyrene as '
                                                      'the only immediate step for ECG '
                                                      'changes',
                                                      'B) Membrane stabilization with '
                                                      'intravenous calcium among other '
                                                      'stepwise measures',
                                                      'C) Hemodialysis as the sole '
                                                      'option before any temporizing '
                                                      'therapy',
                                                      'D) Fluid restriction alone '
                                                      'without cardiac protection'],
                                          'answer': 'B) Membrane stabilization with '
                                                    'intravenous calcium among other '
                                                    'stepwise measures',
                                          'explanation': 'Peaked T waves signal '
                                                         'cardiac membrane instability '
                                                         'from hyperkalemia. IV '
                                                         'calcium antagonizes cardiac '
                                                         'effects within minutes while '
                                                         'insulin/glucose, '
                                                         'beta-agonists, bicarbonate '
                                                         '(selected cases), and '
                                                         'removal therapies address '
                                                         'potassium shift and '
                                                         'elimination.',
                                          'choice_explanations': {
                                              'A': 'Oral sodium polystyrene exchanges '
                                                    'potassium in the gut slowly and '
                                                    'does not immediately stabilize '
                                                    'cardiac membranes when ECG changes '
                                                    'are present.',
                                              'B': 'Peaked T waves signal cardiac '
                                                    'membrane instability from '
                                                    'hyperkalemia; IV calcium '
                                                    'antagonizes cardiac effects within '
                                                    'minutes while other measures shift '
                                                    'and remove potassium.',
                                              'C': 'Hemodialysis removes potassium '
                                                    'effectively but is not the sole '
                                                    'immediate step before temporizing '
                                                    'membrane stabilization and '
                                                    'intracellular shift therapies.',
                                              'D': 'Fluid restriction alone does not '
                                                    'protect the myocardium from '
                                                    'hyperkalemic conduction '
                                                    'abnormalities.'
                                          }}],
                              'hard': [{'question': 'ATN muddy brown casts follow?',
                                        'options': ['A) Glomerular basement-membrane '
                                                    'rupture as the primary ATN lesion',
                                                    'B) Isolated collecting-system '
                                                    'stone without tubular necrosis',
                                                    'C) Ischemic or toxic tubular '
                                                    'injury',
                                                    'D) Minimal-change disease '
                                                    'podocytopathy'],
                                        'answer': 'C) Ischemic or toxic tubular injury',
                                        'explanation': 'Acute tubular necrosis follows '
                                                       'ischemic or nephrotoxic insult '
                                                       'to tubular epithelium; '
                                                       'muddy-brown granular casts are '
                                                       'the classic urinary finding. '
                                                       'GBM rupture suggests '
                                                       'aggressive GN; stones and '
                                                       'minimal-change disease have '
                                                       'different sediment and '
                                                       'clinical pictures.',
                                        'choice_explanations': {
                                            'A': 'Glomerular basement-membrane rupture '
                                                  'underlies aggressive '
                                                  'glomerulonephritides with RBC casts, '
                                                  'not the tubular epithelial injury of '
                                                  'ATN.',
                                            'B': 'An isolated collecting-system stone '
                                                  'causes obstruction without '
                                                  'necessarily producing muddy-brown '
                                                  'casts of tubular necrosis.',
                                            'C': 'Acute tubular necrosis follows '
                                                  'ischemic or nephrotoxic insult to '
                                                  'tubular epithelium; muddy-brown '
                                                  'granular casts are the classic '
                                                  'urinary finding.',
                                            'D': 'Minimal-change disease is '
                                                  'podocytopathy causing nephrotic '
                                                  'syndrome with usually bland '
                                                  'sediment, not ATN muddy-brown casts.'
                                        }},
                                       {'question': 'AIN often linked to?',
                                        'options': ['A) Ischemic ATN from prolonged '
                                                    'hypotension as the identical '
                                                    'mechanism',
                                                    'B) Anti-GBM disease as the usual '
                                                    'AIN cause',
                                                    'C) Simple prerenal azotemia from '
                                                    'volume depletion alone',
                                                    'D) Drug hypersensitivity (e.g., '
                                                    'antibiotics, NSAIDs, PPIs) with '
                                                    'interstitial inflammation ± WBC '
                                                    'casts/eosinophiluria'],
                                        'answer': 'D) Drug hypersensitivity (e.g., '
                                                  'antibiotics, NSAIDs, PPIs) with '
                                                  'interstitial inflammation ± WBC '
                                                  'casts/eosinophiluria',
                                        'explanation': 'Acute interstitial nephritis '
                                                       'is often a drug-induced '
                                                       'T-cell–mediated reaction '
                                                       'presenting with AKI, sterile '
                                                       'pyuria, WBC casts, and '
                                                       'sometimes '
                                                       'rash/fever/eosinophiluria. It '
                                                       'is distinct from ischemic ATN, '
                                                       'anti-GBM crescentic disease, '
                                                       'and pure prerenal physiology.',
                                        'choice_explanations': {
                                            'A': 'Ischemic ATN from prolonged '
                                                  'hypotension is tubular epithelial '
                                                  'ischemic injury, a different '
                                                  'mechanism from drug-induced '
                                                  'interstitial hypersensitivity of '
                                                  'AIN.',
                                            'B': 'Anti-GBM disease is autoimmune attack '
                                                  'on glomerular basement membrane '
                                                  'causing crescentic GN, not the usual '
                                                  'cause of AIN.',
                                            'C': 'Simple prerenal azotemia is reduced '
                                                  'perfusion without intrinsic '
                                                  'interstitial inflammation and WBC '
                                                  'casts of AIN.',
                                            'D': 'Acute interstitial nephritis is often '
                                                  'a drug-induced T-cell–mediated '
                                                  'reaction (antibiotics, NSAIDs, PPIs) '
                                                  'with interstitial inflammation ± WBC '
                                                  'casts/eosinophiluria.'
                                        }},
                                       {'question': 'Indications for urgent dialysis '
                                                    'include?',
                                        'options': ['A) Severe refractory '
                                                    'hyperkalemia, acidosis, volume '
                                                    'overload, or uremic emergencies',
                                                    'B) Mild creatinine rise without '
                                                    'complications',
                                                    'C) Asymptomatic microscopic '
                                                    'hematuria alone',
                                                    'D) Stable CKD stage 3 without '
                                                    'acute indications'],
                                        'answer': 'A) Severe refractory hyperkalemia, '
                                                  'acidosis, volume overload, or '
                                                  'uremic emergencies',
                                        'explanation': 'Urgent dialysis indications '
                                                       'are often remembered as AEIOU: '
                                                       'acidosis, electrolytes (severe '
                                                       'hyperK), intoxications, '
                                                       'overload, and uremic symptoms '
                                                       '(pericarditis, '
                                                       'encephalopathy). Mild lab '
                                                       'changes without these '
                                                       'complications do not mandate '
                                                       'emergency dialysis.',
                                        'choice_explanations': {
                                            'A': 'Urgent dialysis indications include '
                                                  'severe refractory hyperkalemia, '
                                                  'acidosis, volume overload, and '
                                                  'uremic emergencies (pericarditis, '
                                                  'encephalopathy)—the AEIOU framework.',
                                            'B': 'Mild creatinine rise without '
                                                  'complications does not mandate '
                                                  'emergency dialysis.',
                                            'C': 'Asymptomatic microscopic hematuria '
                                                  'alone is a diagnostic clue, not an '
                                                  'indication for urgent dialysis.',
                                            'D': 'Stable CKD stage 3 without acute '
                                                  'AEIOU indications is managed '
                                                  'medically and does not require '
                                                  'emergency dialysis.'
                                        }}],
                              'extreme': [{'question': 'Tumor lysis electrolyte '
                                                       'pattern?',
                                           'options': ['A) Hypokalemia, '
                                                       'hypophosphatemia, '
                                                       'hypercalcemia, and '
                                                       'hypouricemia',
                                                       'B) Hyperkalemia, '
                                                       'hyperphosphatemia, '
                                                       'hypocalcemia, and '
                                                       'hyperuricemia',
                                                       'C) Isolated hyponatremia '
                                                       'without phosphate or urate '
                                                       'change',
                                                       'D) Hypercalcemia with '
                                                       'hypophosphatemia as the TLS '
                                                       'signature'],
                                           'answer': 'B) Hyperkalemia, '
                                                     'hyperphosphatemia, hypocalcemia, '
                                                     'and hyperuricemia',
                                           'explanation': 'Tumor lysis releases '
                                                          'intracellular potassium, '
                                                          'phosphate, and nucleic '
                                                          'acids; uric acid rises and '
                                                          'phosphate binds calcium, '
                                                          'lowering serum calcium. '
                                                          'Recognizing this pattern '
                                                          'guides prevention with '
                                                          'hydration, uric-acid '
                                                          'lowering, and electrolyte '
                                                          'management.',
                                           'choice_explanations': {
                                               'A': 'Hypokalemia, hypophosphatemia, '
                                                     'hypercalcemia, and hypouricemia '
                                                     'is the opposite electrolyte '
                                                     'pattern from tumor lysis release '
                                                     'of intracellular contents.',
                                               'B': 'Tumor lysis releases intracellular '
                                                     'potassium, phosphate, and nucleic '
                                                     'acids; uric acid rises and '
                                                     'phosphate binds calcium, '
                                                     'producing hyperkalemia, '
                                                     'hyperphosphatemia, hypocalcemia, '
                                                     'and hyperuricemia.',
                                               'C': 'Isolated hyponatremia without '
                                                     'phosphate or urate change does '
                                                     'not capture the classic '
                                                     'multi-electrolyte signature of '
                                                     'tumor lysis syndrome.',
                                               'D': 'Hypercalcemia with '
                                                     'hypophosphatemia suggests '
                                                     'PTH-related or other '
                                                     'hypercalcemic states, not the '
                                                     'hyperphosphatemic hypocalcemia of '
                                                     'TLS.'
                                           }},
                                          {'question': 'Hepatorenal syndrome concept?',
                                           'options': ['A) Intrinsic ATN as the '
                                                       'required first diagnosis in '
                                                       'all cirrhotic AKI',
                                                       'B) Postrenal obstruction as '
                                                       'the defining HRS mechanism',
                                                       'C) Functional renal failure in '
                                                       'advanced liver disease after '
                                                       'excluding shock, nephrotoxins, '
                                                       'and obstruction',
                                                       'D) Primary glomerular '
                                                       'nephrotic syndrome unrelated '
                                                       'to liver disease'],
                                           'answer': 'C) Functional renal failure in '
                                                     'advanced liver disease after '
                                                     'excluding shock, nephrotoxins, '
                                                     'and obstruction',
                                           'explanation': 'Hepatorenal syndrome is '
                                                          'functional renal '
                                                          'vasoconstriction in '
                                                          'advanced cirrhosis with '
                                                          'portal hypertension after '
                                                          'volume resuscitation and '
                                                          'exclusion of shock, '
                                                          'nephrotoxins, and '
                                                          'obstruction. Distinguishing '
                                                          'HRS from ATN guides '
                                                          'vasoconstrictor and '
                                                          'transplant-oriented '
                                                          'therapy.',
                                           'choice_explanations': {
                                               'A': 'Intrinsic ATN can complicate '
                                                     'cirrhosis with shock or toxins '
                                                     'but is not the required first '
                                                     'diagnosis for all cirrhotic AKI; '
                                                     'HRS is functional after '
                                                     'exclusions.',
                                               'B': 'Postrenal obstruction is '
                                                     'mechanical blockage and must be '
                                                     'excluded before diagnosing '
                                                     'hepatorenal syndrome, but it is '
                                                     'not the defining HRS mechanism.',
                                               'C': 'Hepatorenal syndrome is functional '
                                                     'renal vasoconstriction in '
                                                     'advanced cirrhosis with portal '
                                                     'hypertension after volume '
                                                     'resuscitation and exclusion of '
                                                     'shock, nephrotoxins, and '
                                                     'obstruction.',
                                               'D': 'Primary glomerular nephrotic '
                                                     'syndrome is glomerular barrier '
                                                     'disease unrelated to the '
                                                     'functional renal failure of '
                                                     'hepatorenal syndrome.'
                                           }},
                                          {'question': 'Contrast nephropathy '
                                                       'prevention theme?',
                                           'options': ['A) Mandate high-osmolar '
                                                       'contrast in all CKD patients',
                                                       'B) Routine NSAID loading '
                                                       'before contrast exposure',
                                                       'C) Withhold all IV fluids in '
                                                       'dehydrated high-risk patients',
                                                       'D) Optimize volume status and '
                                                       'avoid unnecessary contrast in '
                                                       'high-risk patients'],
                                           'answer': 'D) Optimize volume status and '
                                                     'avoid unnecessary contrast in '
                                                     'high-risk patients',
                                           'explanation': 'Contrast-associated AKI '
                                                          'risk rises with CKD, '
                                                          'diabetes, and hypovolemia. '
                                                          'Prevention emphasizes '
                                                          'assessing necessity, using '
                                                          'the lowest adequate '
                                                          'contrast dose, and '
                                                          'optimizing hydration—not '
                                                          'dehydrating patients or '
                                                          'adding nephrotoxins.',
                                           'choice_explanations': {
                                               'A': 'High-osmolar contrast increases '
                                                     'nephrotoxicity risk and should be '
                                                     'avoided in favor of '
                                                     'lower-osmolar/iso-osmolar agents '
                                                     'when contrast is necessary.',
                                               'B': 'Routine NSAID loading adds '
                                                     'afferent arteriolar constriction '
                                                     'and nephrotoxicity around '
                                                     'contrast exposure rather than '
                                                     'protecting the kidney.',
                                               'C': 'Withholding IV fluids in '
                                                     'dehydrated high-risk patients '
                                                     'worsens contrast-associated AKI '
                                                     'risk; hydration is a key '
                                                     'preventive measure.',
                                               'D': 'Contrast-associated AKI risk rises '
                                                     'with CKD, diabetes, and '
                                                     'hypovolemia; prevention '
                                                     'emphasizes necessity assessment, '
                                                     'lowest adequate dose, and '
                                                     'optimizing volume status.'
                                           }}]},
                'cases': {'easy': [{'title': 'Oliguria after Diarrhea',
                                    'stem': 'Elderly man with gastroenteritis has dry '
                                            'mucosa and creatinine rise that improves '
                                            'with IV fluids.',
                                    'question': 'AKI type?',
                                    'answer': 'Pre-renal AKI.',
                                    'discussion': 'Restore volume; avoid nephrotoxins.',
                                    'book_hint': "Brenner & Rector / Harrison's"}],
                          'medium': [{'title': 'Edema + 4.8 g/day Protein',
                                      'stem': 'A 21-year-old has periorbital edema, '
                                              'albumin 2.1, proteinuria 4.8 g/day.',
                                      'question': 'Syndrome?',
                                      'answer': 'Nephrotic syndrome.',
                                      'discussion': 'Find cause; manage '
                                                    'edema/thrombosis risk.',
                                      'book_hint': "Brenner & Rector / Harrison's"}],
                          'hard': [{'title': 'Pulmonary-Renal Theme',
                                    'stem': 'A young adult has hemoptysis, rising '
                                            'creatinine, and dysmorphic RBCs/RBC '
                                            'casts. Labs and imaging are pending; you '
                                            'must choose the safest next clinical '
                                            'concept.',
                                    'question': 'Concern?',
                                    'answer': 'Pulmonary-renal syndrome (e.g., '
                                              'ANCA/anti-GBM pathways) — urgent '
                                              'specialty labs and therapy.',
                                    'discussion': 'Delay risks irreversible '
                                                  'lung/kidney injury.',
                                    'book_hint': "Brenner & Rector / Harrison's"}],
                          'extreme': [{'title': 'Refractory HyperK after TLS',
                                       'stem': 'A leukemia patient day 1 of chemo has '
                                               'K 7.4, phosphate high, calcium low, '
                                               'uric acid high, and ECG changes. '
                                               'Multiple teams are involved; '
                                               'prioritize life/limb/vision threats '
                                               'and avoid harmful premature therapies.',
                                       'question': 'Diagnosis and action concept?',
                                       'answer': 'Tumor lysis syndrome — ECG '
                                                 'stabilization, shift/remove K, '
                                                 'rasburicase/allopurinol pathways, '
                                                 'ICU/nephrology, possible dialysis.',
                                       'discussion': 'Anticipate TLS in high-burden '
                                                     'tumors.',
                                       'book_hint': "Brenner & Rector / Harrison's"}]}},
 'orthopedics': {'label': 'Orthopedics',
                 'books': ["Apley's System of Orthopaedics and Fractures",
                           "Campbell's Operative Orthopaedics",
                           'Bailey & Love — Orthopaedics chapters'],
                 'pdf_notes': ['Compartment syndrome: pain out of proportion — '
                               'emergency fasciotomy pathway.',
                               'Colles fracture: FOOSH → distal radius dorsal '
                               'angulation.',
                               'Ottawa ankle rules guide X-ray after sprain.',
                               'Hip fracture: shortened externally rotated limb in '
                               'elderly fall.',
                               'Fat embolism after long-bone fracture: hypoxia, neuro, '
                               'petechiae.'],
                 'questions': {'easy': [{'question': 'Ottawa ankle rules help decide '
                                                     'need for?',
                                         'options': ['A) Radiographs after ankle '
                                                     'sprain when rules are positive',
                                                     'B) Immediate MRI for every ankle '
                                                     'sprain',
                                                     'C) Bone scan as first-line acute '
                                                     'imaging',
                                                     'D) No imaging pathway regardless '
                                                     'of inability to bear weight'],
                                         'answer': 'A) Radiographs after ankle sprain '
                                                   'when rules are positive',
                                         'explanation': 'Ottawa ankle rules use '
                                                        'tenderness and weight-bearing '
                                                        'ability to decide when '
                                                        'ankle/foot X-rays are needed '
                                                        'after sprain, reducing '
                                                        'unnecessary films while '
                                                        'catching clinically important '
                                                        'fractures.',
                                         'choice_explanations': {
                                             'A': 'Ottawa ankle rules use bony '
                                                   'tenderness and weight-bearing '
                                                   'ability to decide when ankle/foot '
                                                   'radiographs are needed after '
                                                   'sprain, reducing unnecessary films '
                                                   'while detecting important '
                                                   'fractures.',
                                             'B': 'Immediate MRI for every ankle sprain '
                                                   'is unnecessary; clinical decision '
                                                   'rules triage who needs plain '
                                                   'radiographs first.',
                                             'C': 'Bone scan detects metabolic bone '
                                                   'activity and is not first-line '
                                                   'acute imaging after ankle sprain.',
                                             'D': 'Inability to bear weight is an '
                                                   'Ottawa indication for radiographs; '
                                                   'a no-imaging pathway regardless of '
                                                   'that finding would miss fractures.'
                                         }},
                                        {'question': 'Colles fracture typically '
                                                     'follows?',
                                         'options': ['A) Direct blow causing isolated '
                                                     'scaphoid waist fracture only',
                                                     'B) FOOSH injury with distal '
                                                     'radius fracture and dorsal '
                                                     'angulation',
                                                     'C) Fall on a flexed wrist with '
                                                     'volar angulation (Smith pattern) '
                                                     'as the same lesion',
                                                     'D) Twisting injury producing '
                                                     'isolated medial malleolus '
                                                     'fracture'],
                                         'answer': 'B) FOOSH injury with distal radius '
                                                   'fracture and dorsal angulation',
                                         'explanation': 'A Colles fracture is a distal '
                                                        'radius fracture from fall on '
                                                        'an outstretched hand, '
                                                        'classically with dorsal '
                                                        'displacement/angulation of '
                                                        'the distal fragment. Smith '
                                                        'fractures angulate volarly; '
                                                        'scaphoid and ankle fractures '
                                                        'are different injuries.',
                                         'choice_explanations': {
                                             'A': 'A direct blow causing isolated '
                                                   'scaphoid waist fracture is a '
                                                   'different carpal injury pattern '
                                                   'from the classic distal radius '
                                                   'Colles fracture.',
                                             'B': 'A Colles fracture is a distal radius '
                                                   'fracture from fall on an '
                                                   'outstretched hand, classically with '
                                                   'dorsal displacement/angulation of '
                                                   'the distal fragment.',
                                             'C': 'Fall on a flexed wrist with volar '
                                                   'angulation describes a Smith '
                                                   'fracture, the volar-angulated '
                                                   'counterpart rather than the same '
                                                   'Colles lesion.',
                                             'D': 'Twisting injury producing isolated '
                                                   'medial malleolus fracture is an '
                                                   'ankle injury, not a distal radius '
                                                   'Colles fracture.'
                                         }},
                                        {'question': 'Open fracture needs?',
                                         'options': ['A) Delayed antibiotics until '
                                                     'after multiple days of '
                                                     'observation',
                                                     'B) Closed casting alone without '
                                                     'antibiotic coverage',
                                                     'C) Early antibiotics plus urgent '
                                                     'orthopedic management',
                                                     'D) Outpatient follow-up without '
                                                     'wound and fracture care'],
                                         'answer': 'C) Early antibiotics plus urgent '
                                                   'orthopedic management',
                                         'explanation': 'Open fractures communicate '
                                                        'with the environment and risk '
                                                        'deep infection and '
                                                        'osteomyelitis. Early IV '
                                                        'antibiotics, tetanus status, '
                                                        'and urgent surgical '
                                                        'debridement/fixation pathways '
                                                        'reduce infection and improve '
                                                        'outcomes.',
                                         'choice_explanations': {
                                             'A': 'Delaying antibiotics for days after '
                                                   'open fracture allows bacterial '
                                                   'colonization of exposed bone and '
                                                   'soft tissue, raising osteomyelitis '
                                                   'risk.',
                                             'B': 'Closed casting alone without '
                                                   'antibiotic coverage does not '
                                                   'address contamination of an open '
                                                   'fracture communicating with the '
                                                   'environment.',
                                             'C': 'Open fractures communicate with the '
                                                   'environment and risk deep '
                                                   'infection; early IV antibiotics '
                                                   'plus urgent orthopedic '
                                                   'debridement/fixation pathways '
                                                   'reduce infection.',
                                             'D': 'Outpatient follow-up without wound '
                                                   'and fracture care leaves '
                                                   'contamination and instability '
                                                   'untreated in open fractures.'
                                         }}],
                               'medium': [{'question': 'Compartment syndrome key early '
                                                       'feature?',
                                           'options': ['A) Absent distal pulses as the '
                                                       'earliest and most sensitive '
                                                       'finding',
                                                       'B) Painless swelling without '
                                                       'tenderness',
                                                       'C) Isolated fever without limb '
                                                       'findings',
                                                       'D) Pain out of proportion and '
                                                       'pain on passive stretch'],
                                           'answer': 'D) Pain out of proportion and '
                                                     'pain on passive stretch',
                                           'explanation': 'Compartment syndrome '
                                                          'elevates intracompartmental '
                                                          'pressure, ischemicizing '
                                                          'muscle and nerve. Early '
                                                          'clues are severe pain out '
                                                          'of proportion and pain on '
                                                          'passive stretch; '
                                                          'pulselessness is a late '
                                                          'finding. Urgent fasciotomy '
                                                          'is required once '
                                                          'diagnosed.',
                                           'choice_explanations': {
                                               'A': 'Absent distal pulses are a late '
                                                     'finding after prolonged '
                                                     'compartment ischemia; relying on '
                                                     'pulselessness misses early '
                                                     'compartment syndrome.',
                                               'B': 'Painless swelling without '
                                                     'tenderness is inconsistent with '
                                                     'the severe ischemic muscle pain '
                                                     'of rising compartment pressure.',
                                               'C': 'Isolated fever without limb '
                                                     'findings suggests systemic '
                                                     'infection, not acute compartment '
                                                     'hypertension.',
                                               'D': 'Compartment syndrome elevates '
                                                     'intracompartmental pressure, '
                                                     'ischemicizing muscle and nerve; '
                                                     'early clues are pain out of '
                                                     'proportion and pain on passive '
                                                     'stretch.'
                                           }},
                                          {'question': 'Fat embolism classic setting?',
                                           'options': ['A) After long-bone (or pelvic) '
                                                       'fracture',
                                                       'B) After uncomplicated distal '
                                                       'phalanx tuft fracture alone',
                                                       'C) After simple ankle sprain '
                                                       'without fracture',
                                                       'D) After elective soft-tissue '
                                                       'laceration repair alone'],
                                           'answer': 'A) After long-bone (or pelvic) '
                                                     'fracture',
                                           'explanation': 'Fat emboli classically '
                                                          'follow femoral or other '
                                                          'long-bone fractures (and '
                                                          'some orthopedic '
                                                          'procedures), presenting '
                                                          '24–72 hours later with '
                                                          'respiratory and neurologic '
                                                          'features ± petechiae.',
                                           'choice_explanations': {
                                               'A': 'Fat emboli classically follow '
                                                     'femoral or other long-bone (or '
                                                     'pelvic) fractures, presenting '
                                                     '24–72 hours later with '
                                                     'respiratory and neurologic '
                                                     'features ± petechiae.',
                                               'B': 'Uncomplicated distal phalanx tuft '
                                                     'fracture is a small distal injury '
                                                     'that is not the classic setting '
                                                     'for fat embolism syndrome.',
                                               'C': 'Simple ankle sprain without '
                                                     'fracture lacks the marrow fat '
                                                     'embolization associated with '
                                                     'major long-bone fractures.',
                                               'D': 'Elective soft-tissue laceration '
                                                     'repair alone does not release '
                                                     'marrow fat into the circulation '
                                                     'as in long-bone fracture.'
                                           }},
                                          {'question': 'Septic arthritis urgency?',
                                           'options': ['A) Empiric oral antibiotics '
                                                       'for weeks without aspiration',
                                                       'B) Urgent joint aspiration for '
                                                       'culture then prompt '
                                                       'antibiotics',
                                                       'C) Watchful waiting until '
                                                       'cartilage is destroyed',
                                                       'D) Steroid injection before '
                                                       'excluding infection'],
                                           'answer': 'B) Urgent joint aspiration for '
                                                     'culture then prompt antibiotics',
                                           'explanation': 'Septic arthritis rapidly '
                                                          'destroys cartilage. Urgent '
                                                          'aspiration for Gram '
                                                          'stain/culture should '
                                                          'precede antibiotics when '
                                                          'feasible, then prompt IV '
                                                          'antibiotics and often '
                                                          'surgical drainage—steroids '
                                                          'and delay worsen joint '
                                                          'outcomes.',
                                           'choice_explanations': {
                                               'A': 'Empiric oral antibiotics for weeks '
                                                     'without aspiration delays '
                                                     'organism identification and '
                                                     'adequate source control while '
                                                     'cartilage is destroyed.',
                                               'B': 'Septic arthritis rapidly destroys '
                                                     'cartilage; urgent aspiration for '
                                                     'Gram stain/culture should precede '
                                                     'antibiotics when feasible, then '
                                                     'prompt IV antibiotics and often '
                                                     'drainage.',
                                               'C': 'Watchful waiting until cartilage '
                                                     'is destroyed allows irreversible '
                                                     'joint damage from enzymatic and '
                                                     'pressure injury of untreated '
                                                     'septic arthritis.',
                                               'D': 'Steroid injection before excluding '
                                                     'infection suppresses local '
                                                     'immunity and can worsen septic '
                                                     'arthritis.'
                                           }}],
                               'hard': [{'question': 'Salter-Harris injuries involve?',
                                         'options': ['A) Only the adult articular '
                                                     'cartilage surface without physis',
                                                     'B) Isolated muscle belly strain',
                                                     'C) The physis (growth plate)',
                                                     'D) Pure ligament sprain without '
                                                     'bony growth-plate involvement'],
                                         'answer': 'C) The physis (growth plate)',
                                         'explanation': 'Salter–Harris classification '
                                                        'describes fractures involving '
                                                        'the pediatric physis. Injury '
                                                        'pattern determines growth '
                                                        'disturbance risk and '
                                                        'management. Adult articular '
                                                        'injuries and soft-tissue '
                                                        'sprains are classified '
                                                        'differently.',
                                         'choice_explanations': {
                                             'A': 'Adult articular cartilage surface '
                                                   'injury without physis is classified '
                                                   'differently from pediatric '
                                                   'Salter–Harris physeal fractures.',
                                             'B': 'Isolated muscle belly strain is '
                                                   'myofiber injury without involvement '
                                                   'of the growth plate.',
                                             'C': 'Salter–Harris classification '
                                                   'describes fractures involving the '
                                                   'pediatric physis (growth plate), '
                                                   'with pattern determining growth '
                                                   'disturbance risk.',
                                             'D': 'Pure ligament sprain without bony '
                                                   'growth-plate involvement is '
                                                   'soft-tissue injury, not a '
                                                   'Salter–Harris physeal fracture.'
                                         }},
                                        {'question': 'Cauda equina red flags include?',
                                         'options': ['A) Isolated mechanical low-back '
                                                     'pain without neurologic change',
                                                     'B) Unilateral ankle jerk '
                                                     'asymmetry alone without '
                                                     'sphincter signs',
                                                     'C) Chronic intermittent sciatica '
                                                     'without red flags',
                                                     'D) Saddle anesthesia with bowel '
                                                     'or bladder dysfunction'],
                                         'answer': 'D) Saddle anesthesia with bowel or '
                                                   'bladder dysfunction',
                                         'explanation': 'Cauda equina compression '
                                                        'produces saddle anesthesia, '
                                                        'sphincter dysfunction, and '
                                                        'often bilateral leg symptoms. '
                                                        'These red flags demand urgent '
                                                        'MRI and decompression to '
                                                        'preserve continence and '
                                                        'sexual function.',
                                         'choice_explanations': {
                                             'A': 'Isolated mechanical low-back pain '
                                                   'without neurologic change lacks the '
                                                   'saddle anesthesia and sphincter '
                                                   'dysfunction of cauda equina '
                                                   'compression.',
                                             'B': 'Unilateral ankle jerk asymmetry '
                                                   'alone without sphincter signs may '
                                                   'reflect radiculopathy but is not '
                                                   'the full cauda equina red-flag '
                                                   'constellation.',
                                             'C': 'Chronic intermittent sciatica '
                                                   'without red flags is usually '
                                                   'compressive radiculopathy managed '
                                                   'electively, not emergency cauda '
                                                   'equina syndrome.',
                                             'D': 'Cauda equina compression produces '
                                                   'saddle anesthesia with bowel or '
                                                   'bladder dysfunction, demanding '
                                                   'urgent MRI and decompression to '
                                                   'preserve continence.'
                                         }},
                                        {'question': 'Pathologic fracture suggests?',
                                         'options': ['A) Underlying bone weakness from '
                                                     'tumor, osteoporosis, or '
                                                     'metabolic bone disease',
                                                     'B) Normal bone subjected only to '
                                                     'high-energy trauma as the '
                                                     'definition',
                                                     'C) Isolated soft-tissue '
                                                     'contusion without fracture',
                                                     'D) Greenstick injury in a '
                                                     'healthy child as the pathologic '
                                                     'definition'],
                                         'answer': 'A) Underlying bone weakness from '
                                                   'tumor, osteoporosis, or metabolic '
                                                   'bone disease',
                                         'explanation': 'A pathologic fracture occurs '
                                                        'through bone weakened by '
                                                        'tumor, osteoporosis, '
                                                        'infection, or metabolic '
                                                        'disease, often after minimal '
                                                        'trauma. Recognizing it '
                                                        'prompts evaluation for the '
                                                        'underlying bone pathology.',
                                         'choice_explanations': {
                                             'A': 'A pathologic fracture occurs through '
                                                   'bone weakened by tumor, '
                                                   'osteoporosis, infection, or '
                                                   'metabolic disease, often after '
                                                   'minimal trauma, prompting '
                                                   'evaluation of the underlying bone '
                                                   'pathology.',
                                             'B': 'Normal bone subjected only to '
                                                   'high-energy trauma defines a '
                                                   'traumatic fracture through healthy '
                                                   'bone, not a pathologic fracture.',
                                             'C': 'Isolated soft-tissue contusion '
                                                   'without fracture is bruise of '
                                                   'muscle/fat without cortical '
                                                   'failure.',
                                             'D': 'Greenstick injury in a healthy child '
                                                   'is an incomplete pediatric fracture '
                                                   'of relatively normal bone, not the '
                                                   'definition of pathologic fracture '
                                                   'through diseased bone.'
                                         }}],
                               'extreme': [{'question': 'Necrotizing fasciitis clue?',
                                            'options': ['A) Mild localized cellulitis '
                                                        'improving on oral antibiotics',
                                                        'B) Pain out of proportion, '
                                                        'rapid spread, and systemic '
                                                        'toxicity',
                                                        'C) Chronic venous stasis '
                                                        'dermatitis without toxicity',
                                                        'D) Uncomplicated superficial '
                                                        'abrasion'],
                                            'answer': 'B) Pain out of proportion, '
                                                      'rapid spread, and systemic '
                                                      'toxicity',
                                            'explanation': 'Necrotizing fasciitis '
                                                           'features severe pain out '
                                                           'of proportion, rapid '
                                                           'progression, and systemic '
                                                           'toxicity, sometimes with '
                                                           'crepitus. It is a surgical '
                                                           'emergency requiring '
                                                           'immediate debridement—not '
                                                           'observation as simple '
                                                           'cellulitis.',
                                            'choice_explanations': {
                                                'A': 'Mild localized cellulitis '
                                                      'improving on oral antibiotics '
                                                      'lacks the rapid deep necrosis '
                                                      'and systemic toxicity of '
                                                      'necrotizing fasciitis.',
                                                'B': 'Necrotizing fasciitis features '
                                                      'severe pain out of proportion, '
                                                      'rapid progression, and systemic '
                                                      'toxicity, sometimes with '
                                                      'crepitus, and requires immediate '
                                                      'surgical debridement.',
                                                'C': 'Chronic venous stasis dermatitis '
                                                      'is inflammatory skin change from '
                                                      'venous hypertension without '
                                                      'necrotizing fascial infection.',
                                                'D': 'Uncomplicated superficial '
                                                      'abrasion is epidermal injury '
                                                      'without deep fascial necrosis.'
                                            }},
                                           {'question': 'Pelvic binder indication '
                                                        'theme?',
                                            'options': ['A) Stable isolated pubic '
                                                        'ramus fracture without '
                                                        'hemodynamic concern',
                                                        'B) Acetabular fracture '
                                                        'already fully fixed in the OR',
                                                        'C) Unstable pelvic fracture '
                                                        'with concern for '
                                                        'life-threatening hemorrhage',
                                                        'D) Chronic pelvic deformity '
                                                        'without acute bleeding'],
                                            'answer': 'C) Unstable pelvic fracture '
                                                      'with concern for '
                                                      'life-threatening hemorrhage',
                                            'explanation': 'A pelvic binder '
                                                           'temporarily reduces pelvic '
                                                           'volume and can tamponade '
                                                           'venous/cancellous bleeding '
                                                           'in unstable pelvic ring '
                                                           'injuries during '
                                                           'resuscitation. It is not '
                                                           'needed for every minor '
                                                           'stable pelvic fracture.',
                                            'choice_explanations': {
                                                'A': 'Stable isolated pubic ramus '
                                                      'fracture without hemodynamic '
                                                      'concern usually does not need a '
                                                      'binder for life-threatening '
                                                      'pelvic hemorrhage.',
                                                'B': 'An acetabular fracture already '
                                                      'fully fixed in the OR no longer '
                                                      'needs temporary binder tamponade '
                                                      'for acute unstable ring '
                                                      'bleeding.',
                                                'C': 'A pelvic binder temporarily '
                                                      'reduces pelvic volume and can '
                                                      'tamponade venous/cancellous '
                                                      'bleeding in unstable pelvic ring '
                                                      'injuries during resuscitation.',
                                                'D': 'Chronic pelvic deformity without '
                                                      'acute bleeding is not an '
                                                      'indication for emergency binder '
                                                      'placement.'
                                            }},
                                           {'question': 'Rhabdomyolysis AKI risk from?',
                                            'options': ['A) Isolated hypercalcemia '
                                                        'without muscle necrosis',
                                                        'B) Simple dehydration without '
                                                        'rhabdomyolysis',
                                                        'C) Postrenal obstruction from '
                                                        'prostate enlargement alone',
                                                        'D) Myoglobinuria after crush '
                                                        'injury or extreme exertion'],
                                            'answer': 'D) Myoglobinuria after crush '
                                                      'injury or extreme exertion',
                                            'explanation': 'Rhabdomyolysis releases '
                                                           'myoglobin and potassium '
                                                           'from necrotic muscle; '
                                                           'myoglobin is nephrotoxic '
                                                           'and can cause AKI after '
                                                           'crush, immobilization, or '
                                                           'extreme exertion. '
                                                           'Aggressive IV fluids are '
                                                           'the mainstay of kidney '
                                                           'protection.',
                                            'choice_explanations': {
                                                'A': 'Isolated hypercalcemia without '
                                                      'muscle necrosis does not release '
                                                      'myoglobin that causes pigment '
                                                      'nephropathy.',
                                                'B': 'Simple dehydration without '
                                                      'rhabdomyolysis can cause '
                                                      'prerenal AKI but is not '
                                                      'myoglobinuric kidney injury from '
                                                      'muscle breakdown.',
                                                'C': 'Postrenal obstruction from '
                                                      'prostate enlargement is '
                                                      'mechanical blockage, a different '
                                                      'AKI mechanism from myoglobin '
                                                      'toxicity.',
                                                'D': 'Rhabdomyolysis releases myoglobin '
                                                      'and potassium from necrotic '
                                                      'muscle after crush injury or '
                                                      'extreme exertion; myoglobin is '
                                                      'nephrotoxic and can cause AKI.'
                                            }}]},
                 'cases': {'easy': [{'title': 'Elderly Fall + Shortened Leg',
                                     'stem': 'An 83-year-old falls; leg is shortened '
                                             'and externally rotated; cannot bear '
                                             'weight.',
                                     'question': 'Likely injury?',
                                     'answer': 'Hip fracture.',
                                     'discussion': 'X-ray, analgesia, VTE prophylaxis, '
                                                   'early ortho.',
                                     'book_hint': "Apley's Orthopaedics"}],
                           'medium': [{'title': 'Pain After Cast',
                                       'stem': 'A tibial fracture in cast has severe '
                                               'pain on passive toe stretch and a '
                                               'tense leg. Pulses present.',
                                       'question': 'Diagnosis?',
                                       'answer': 'Compartment syndrome — urgent '
                                                 'fasciotomy pathway.',
                                       'discussion': 'Do not wait for pulselessness.',
                                       'book_hint': "Apley's Orthopaedics"}],
                           'hard': [{'title': 'Hot Swollen Knee + Fever',
                                     'stem': 'A 45-year-old cannot bear weight on a '
                                             'hot swollen knee with fever. CRP high. '
                                             'Labs and imaging are pending; you must '
                                             'choose the safest next clinical concept.',
                                     'question': 'Action concept?',
                                     'answer': 'Septic arthritis until proven '
                                               'otherwise — urgent aspiration before '
                                               'antibiotics if possible, then treat.',
                                     'discussion': 'Delay destroys cartilage.',
                                     'book_hint': "Apley's Orthopaedics"}],
                           'extreme': [{'title': 'Crush Injury + Dark Urine',
                                        'stem': 'After an earthquake crush injury, a '
                                                'patient has tense swollen thighs, K '
                                                '6.8, dark urine, and rising '
                                                'creatinine. Multiple teams are '
                                                'involved; prioritize life/limb/vision '
                                                'threats and avoid harmful premature '
                                                'therapies.',
                                        'question': 'Concerns?',
                                        'answer': 'Rhabdomyolysis ± compartment '
                                                  'syndrome — aggressive fluids per '
                                                  'protocol, electrolyte management, '
                                                  'surgical decompression if '
                                                  'compartment syndrome, dialysis if '
                                                  'needed.',
                                        'discussion': 'HyperK can kill before renal '
                                                      'failure does.',
                                        'book_hint': "Apley's Orthopaedics"}]}},
 'dermatology': {'label': 'Dermatology',
                 'books': ["Rook's Textbook of Dermatology",
                           "Fitzpatrick's Dermatology",
                           "Habif's Clinical Dermatology"],
                 'pdf_notes': ['ABCDE for melanoma; urgent specialist referral for '
                               'suspicious lesions.',
                               'Impetigo: honey-colored crusts — contagious.',
                               'Psoriasis: silvery scale, Auspitz, extensor surfaces '
                               'common.',
                               'Scabies: nocturnal itch, finger webs — treat patient + '
                               'contacts.',
                               'Cellulitis vs abscess: antibiotics ± drainage if '
                               'collection.'],
                 'questions': {'easy': [{'question': 'Honey-colored crusts suggest?',
                                         'options': ['A) Impetigo',
                                                     'B) Pemphigus vulgaris',
                                                     'C) Bullous pemphigoid',
                                                     'D) Discoid lupus erythematosus'],
                                         'answer': 'A) Impetigo',
                                         'explanation': 'Honey-colored crusts on '
                                                        'erosions, especially on the '
                                                        'face of children, are classic '
                                                        'for nonbullous impetigo from '
                                                        'Staphylococcus aureus or '
                                                        'Streptococcus pyogenes. '
                                                        'Autoimmune blistering '
                                                        'diseases and discoid lupus '
                                                        'have different morphologies '
                                                        'and demographics.',
                                         'choice_explanations': {
                                             'A': 'Honey-colored crusts on erosions, '
                                                   'especially on children’s faces, are '
                                                   'classic for nonbullous impetigo '
                                                   'from Staphylococcus aureus or '
                                                   'Streptococcus pyogenes.',
                                             'B': 'Pemphigus vulgaris is autoimmune '
                                                   'acantholysis with flaccid bullae '
                                                   'and erosions, typically in '
                                                   'middle-aged adults, not '
                                                   'honey-crusted pediatric impetigo.',
                                             'C': 'Bullous pemphigoid is autoimmune '
                                                   'subepidermal tense bullae in '
                                                   'elderly patients, morphologically '
                                                   'distinct from honey-colored '
                                                   'impetigo crusts.',
                                             'D': 'Discoid lupus erythematosus produces '
                                                   'scarring erythematous plaques with '
                                                   'follicular plugging, not '
                                                   'honey-colored '
                                                   'staphylococcal/streptococcal '
                                                   'crusts.'
                                         }},
                                        {'question': 'ABCDE screens for?',
                                         'options': ['A) Seborrheic keratosis alone',
                                                     'B) Melanoma',
                                                     'C) Dermatofibroma alone',
                                                     'D) Lipoma alone'],
                                         'answer': 'B) Melanoma',
                                         'explanation': 'ABCDE (Asymmetry, Border '
                                                        'irregularity, Color '
                                                        'variegation, Diameter, '
                                                        'Evolution) screens pigmented '
                                                        'lesions for melanoma risk and '
                                                        'guides biopsy decisions. '
                                                        'Seborrheic keratoses, '
                                                        'dermatofibromas, and lipomas '
                                                        'have different clinical '
                                                        'signatures.',
                                         'choice_explanations': {
                                             'A': 'Seborrheic keratosis is a benign '
                                                   'stuck-on epidermal proliferation '
                                                   'and is not what ABCDE melanoma '
                                                   'screening targets.',
                                             'B': 'ABCDE (Asymmetry, Border '
                                                   'irregularity, Color variegation, '
                                                   'Diameter, Evolution) screens '
                                                   'pigmented lesions for melanoma risk '
                                                   'and guides biopsy decisions.',
                                             'C': 'Dermatofibroma is a benign dermal '
                                                   'fibrous nodule, usually after '
                                                   'trauma, and is not the target of '
                                                   'ABCDE melanoma screening.',
                                             'D': 'Lipoma is a benign subcutaneous fat '
                                                   'tumor without the pigmented ABCDE '
                                                   'features used for melanoma '
                                                   'detection.'
                                         }},
                                        {'question': 'Auspitz sign relates to?',
                                         'options': ['A) Atopic dermatitis',
                                                     'B) Lichen planus',
                                                     'C) Psoriasis',
                                                     'D) Nummular eczema without '
                                                     'Auspitz bleeding'],
                                         'answer': 'C) Psoriasis',
                                         'explanation': 'Auspitz sign is pinpoint '
                                                        'bleeding when psoriatic scale '
                                                        'is removed, reflecting '
                                                        'dilated dermal papillae under '
                                                        'thinned epidermis. Atopic '
                                                        'dermatitis, lichen planus, '
                                                        'and nummular eczema are '
                                                        'diagnosed by other '
                                                        'morphologic clues.',
                                         'choice_explanations': {
                                             'A': 'Atopic dermatitis is eczematous '
                                                   'barrier dysfunction with itch and '
                                                   'flexure involvement, diagnosed '
                                                   'without Auspitz pinpoint bleeding.',
                                             'B': 'Lichen planus shows pruritic purple '
                                                   'polygonal papules with Wickham '
                                                   'striae, not Auspitz bleeding of '
                                                   'psoriasis.',
                                             'C': 'Auspitz sign is pinpoint bleeding '
                                                   'when psoriatic scale is removed, '
                                                   'reflecting dilated dermal papillae '
                                                   'under thinned epidermis.',
                                             'D': 'Nummular eczema forms coin-shaped '
                                                   'eczematous plaques without the '
                                                   'classic Auspitz phenomenon of '
                                                   'psoriasis.'
                                         }}],
                               'medium': [{'question': 'Scabies itch is worse?',
                                           'options': ['A) Facial pruritus triggered '
                                                       'by ultraviolet exposure '
                                                       '(polymorphous light eruption '
                                                       'pattern)',
                                                       'B) Cold-induced wheals of cold '
                                                       'urticaria on the trunk',
                                                       'C) Painless hypopigmented '
                                                       'macules of pityriasis '
                                                       'versicolor',
                                                       'D) At night, especially in '
                                                       'finger web spaces and other '
                                                       'burrow sites'],
                                           'answer': 'D) At night, especially in '
                                                     'finger web spaces and other '
                                                     'burrow sites',
                                           'explanation': 'Sarcoptes scabiei burrows '
                                                          'in stratum corneum; intense '
                                                          'nocturnal pruritus in webs, '
                                                          'wrists, and genitals is '
                                                          'characteristic. '
                                                          'Sun-triggered facial itch '
                                                          'and cold urticaria suggest '
                                                          'other diagnoses; '
                                                          'hypopigmented patches '
                                                          'suggest pityriasis '
                                                          'versicolor or vitiligo.',
                                           'choice_explanations': {
                                               'A': 'Facial pruritus triggered by '
                                                     'ultraviolet exposure fits '
                                                     'polymorphous light eruption, not '
                                                     'nocturnal burrow-site itch of '
                                                     'scabies.',
                                               'B': 'Cold-induced wheals of cold '
                                                     'urticaria are mast-cell–mediated '
                                                     'physical urticaria, unrelated to '
                                                     'Sarcoptes burrows.',
                                               'C': 'Painless hypopigmented macules of '
                                                     'pityriasis versicolor are '
                                                     'Malassezia-related pigment change '
                                                     'without the intense nocturnal '
                                                     'itch of scabies.',
                                               'D': 'Sarcoptes scabiei burrows in '
                                                     'stratum corneum; intense '
                                                     'nocturnal pruritus in finger '
                                                     'webs, wrists, and genitals is '
                                                     'characteristic.'
                                           }},
                                          {'question': 'Cellulitis features?',
                                           'options': ['A) Spreading erythema, warmth, '
                                                       'and tenderness of the skin and '
                                                       'soft tissue',
                                                       'B) Well-demarcated silvery '
                                                       'plaques on extensor surfaces',
                                                       'C) Annular plaque from '
                                                       'granuloma annulare without '
                                                       'cellulitis signs',
                                                       'D) Noninflammatory '
                                                       'subcutaneous lipoma'],
                                           'answer': 'A) Spreading erythema, warmth, '
                                                     'and tenderness of the skin and '
                                                     'soft tissue',
                                           'explanation': 'Cellulitis is bacterial '
                                                          'infection of dermis and '
                                                          'subcutaneous tissue '
                                                          'producing expanding '
                                                          'erythema, warmth, swelling, '
                                                          'and tenderness. Psoriasis '
                                                          'plaques, granuloma '
                                                          'annulare, and lipomas are '
                                                          'morphologically distinct.',
                                           'choice_explanations': {
                                               'A': 'Cellulitis is bacterial infection '
                                                     'of dermis and subcutaneous tissue '
                                                     'producing expanding erythema, '
                                                     'warmth, swelling, and tenderness.',
                                               'B': 'Well-demarcated silvery plaques on '
                                                     'extensor surfaces describe plaque '
                                                     'psoriasis, an immune-mediated '
                                                     'epidermal hyperplasia, not '
                                                     'soft-tissue infection.',
                                               'C': 'Annular plaque of granuloma '
                                                     'annulare is a granulomatous '
                                                     'dermal disorder without the '
                                                     'warmth and spreading erythema of '
                                                     'cellulitis.',
                                               'D': 'Noninflammatory subcutaneous '
                                                     'lipoma is a soft fat tumor '
                                                     'without infectious inflammatory '
                                                     'skin signs.'
                                           }},
                                          {'question': 'SJS/TEN are?',
                                           'options': ['A) Mild irritant contact '
                                                       'dermatitis only',
                                                       'B) Severe cutaneous adverse '
                                                       'drug reactions with epidermal '
                                                       'necrosis',
                                                       'C) Simple morbilliform drug '
                                                       'rash without necrosis',
                                                       'D) Chronic plaque psoriasis '
                                                       'exacerbation alone'],
                                           'answer': 'B) Severe cutaneous adverse drug '
                                                     'reactions with epidermal '
                                                     'necrosis',
                                           'explanation': 'Stevens–Johnson syndrome '
                                                          'and toxic epidermal '
                                                          'necrolysis are severe '
                                                          'drug-induced reactions with '
                                                          'widespread epidermal '
                                                          'necrosis and mucosal '
                                                          'involvement, carrying high '
                                                          'morbidity. Mild drug '
                                                          'exanthems and psoriasis '
                                                          'lack this necrolytic '
                                                          'mucocutaneous pattern.',
                                           'choice_explanations': {
                                               'A': 'Mild irritant contact dermatitis '
                                                     'is barrier injury from irritants '
                                                     'without widespread epidermal '
                                                     'necrosis of SJS/TEN.',
                                               'B': 'Stevens–Johnson syndrome and toxic '
                                                     'epidermal necrolysis are severe '
                                                     'drug-induced reactions with '
                                                     'widespread epidermal necrosis and '
                                                     'mucosal involvement.',
                                               'C': 'Simple morbilliform drug rash is a '
                                                     'common exanthem without '
                                                     'sheet-like necrolysis and severe '
                                                     'mucosal disease of SJS/TEN.',
                                               'D': 'Chronic plaque psoriasis '
                                                     'exacerbation is immune-mediated '
                                                     'epidermal hyperplasia, not acute '
                                                     'drug-induced necrolysis.'
                                           }}],
                               'hard': [{'question': 'Nikolsky sign can be positive '
                                                     'in?',
                                         'options': ['A) Uncomplicated urticaria '
                                                     'without epidermal detachment',
                                                     'B) Acne vulgaris',
                                                     'C) SJS/TEN and certain other '
                                                     'blistering diseases (e.g., '
                                                     'pemphigus)',
                                                     'D) Vitiligo'],
                                         'answer': 'C) SJS/TEN and certain other '
                                                   'blistering diseases (e.g., '
                                                   'pemphigus)',
                                         'explanation': 'Nikolsky sign—lateral '
                                                        'pressure causing sheet-like '
                                                        'epidermal separation—is '
                                                        'positive in TEN/SJS and in '
                                                        'pemphigus, reflecting loss of '
                                                        'keratinocyte adhesion. '
                                                        'Urticaria, acne, and vitiligo '
                                                        'do not show true Nikolsky '
                                                        'positivity.',
                                         'choice_explanations': {
                                             'A': 'Uncomplicated urticaria is dermal '
                                                   'edema from mast-cell mediators '
                                                   'without sheet-like epidermal '
                                                   'detachment of a positive Nikolsky '
                                                   'sign.',
                                             'B': 'Acne vulgaris is follicular '
                                                   'inflammation with comedones and '
                                                   'papules and does not show Nikolsky '
                                                   'epidermal shearing.',
                                             'C': 'Nikolsky sign—lateral pressure '
                                                   'causing sheet-like epidermal '
                                                   'separation—is positive in TEN/SJS '
                                                   'and in pemphigus from loss of '
                                                   'keratinocyte adhesion.',
                                             'D': 'Vitiligo is autoimmune melanocyte '
                                                   'loss causing depigmentation without '
                                                   'epidermal detachment.'
                                         }},
                                        {'question': 'Erythema migrans suggests?',
                                         'options': ['A) Secondary syphilis as the '
                                                     'identical lesion name',
                                                     'B) Fixed drug eruption as the '
                                                     'usual EM cause',
                                                     'C) Erythema multiforme target '
                                                     'lesions as the same entity',
                                                     'D) Early Lyme disease (erythema '
                                                     'migrans)'],
                                         'answer': 'D) Early Lyme disease (erythema '
                                                   'migrans)',
                                         'explanation': 'Erythema migrans is the '
                                                        'expanding annular rash of '
                                                        'early Lyme borreliosis after '
                                                        'Ixodes tick bite. Erythema '
                                                        'multiforme shows targetoid '
                                                        'lesions often post-herpes; '
                                                        'syphilis and fixed drug '
                                                        'eruptions are different '
                                                        'morphologies and etiologies.',
                                         'choice_explanations': {
                                             'A': 'Secondary syphilis produces '
                                                   'disseminated mucocutaneous lesions '
                                                   'including palms/soles but is not '
                                                   'identically named erythema migrans '
                                                   'of Lyme disease.',
                                             'B': 'Fixed drug eruption is a recurrent '
                                                   'drug-induced plaque at the same '
                                                   'site and is not the expanding '
                                                   'annular Lyme rash.',
                                             'C': 'Erythema multiforme shows targetoid '
                                                   'lesions often post-herpes and is a '
                                                   'different entity from erythema '
                                                   'migrans of early Lyme.',
                                             'D': 'Erythema migrans is the expanding '
                                                   'annular rash of early Lyme '
                                                   'borreliosis after Ixodes tick bite.'
                                         }},
                                        {'question': 'Necrotizing infection vs simple '
                                                     'cellulitis clue?',
                                         'options': ['A) Extreme pain, crepitus, and '
                                                     'rapid clinical deterioration',
                                                     'B) Mild warmth responding '
                                                     'quickly to oral antibiotics',
                                                     'C) Chronic bilateral venous '
                                                     'stasis changes only',
                                                     'D) Localized folliculitis '
                                                     'without systemic signs'],
                                         'answer': 'A) Extreme pain, crepitus, and '
                                                   'rapid clinical deterioration',
                                         'explanation': 'Necrotizing soft-tissue '
                                                        'infection differs from simple '
                                                        'cellulitis by pain out of '
                                                        'proportion, rapid spread, '
                                                        'crepitus/gas, and early '
                                                        'sepsis. Suspicion mandates '
                                                        'urgent surgical exploration '
                                                        'rather than observation on '
                                                        'oral antibiotics alone.',
                                         'choice_explanations': {
                                             'A': 'Extreme pain, crepitus, and rapid '
                                                   'clinical deterioration distinguish '
                                                   'necrotizing soft-tissue infection '
                                                   'from simple cellulitis and mandate '
                                                   'urgent surgical exploration.',
                                             'B': 'Mild warmth responding quickly to '
                                                   'oral antibiotics is the expected '
                                                   'course of uncomplicated cellulitis, '
                                                   'not necrotizing infection.',
                                             'C': 'Chronic bilateral venous stasis '
                                                   'changes reflect venous hypertension '
                                                   'without acute necrotizing fascial '
                                                   'infection.',
                                             'D': 'Localized folliculitis is '
                                                   'superficial follicular infection '
                                                   'without systemic toxicity and deep '
                                                   'necrosis.'
                                         }}],
                               'extreme': [{'question': 'Purpura fulminans '
                                                        'association?',
                                            'options': ['A) Uncomplicated atopic '
                                                        'eczema flare',
                                                        'B) Severe sepsis, especially '
                                                        'meningococcemia',
                                                        'C) Mild viral exanthem '
                                                        'without shock',
                                                        'D) Localized contact '
                                                        'dermatitis'],
                                            'answer': 'B) Severe sepsis, especially '
                                                      'meningococcemia',
                                            'explanation': 'Purpura fulminans is acute '
                                                           'purpuric skin necrosis '
                                                           'from disseminated '
                                                           'intravascular coagulation '
                                                           'and dermal vascular '
                                                           'thrombosis, classically '
                                                           'with meningococcal sepsis. '
                                                           'It is a medical emergency '
                                                           'distinct from benign '
                                                           'eczematous or contact '
                                                           'eruptions.',
                                            'choice_explanations': {
                                                'A': 'Uncomplicated atopic eczema flare '
                                                      'is barrier-related inflammation '
                                                      'without DIC-driven purpuric skin '
                                                      'necrosis of purpura fulminans.',
                                                'B': 'Purpura fulminans is acute '
                                                      'purpuric skin necrosis from '
                                                      'disseminated intravascular '
                                                      'coagulation and dermal vascular '
                                                      'thrombosis, classically with '
                                                      'meningococcal sepsis.',
                                                'C': 'Mild viral exanthem without shock '
                                                      'lacks the retiform purpura and '
                                                      'necrotic skin of purpura '
                                                      'fulminans.',
                                                'D': 'Localized contact dermatitis is '
                                                      'type IV or irritant epidermal '
                                                      'inflammation without septic DIC '
                                                      'skin necrosis.'
                                            }},
                                           {'question': 'Calciphylaxis occurs mainly '
                                                        'in?',
                                            'options': ['A) Healthy adolescents '
                                                        'without metabolic disease',
                                                        'B) Patients with isolated '
                                                        'mild fatty liver alone',
                                                        'C) Patients with advanced '
                                                        'kidney disease (often '
                                                        'dialysis-dependent)',
                                                        'D) Children with '
                                                        'uncomplicated atopic '
                                                        'dermatitis'],
                                            'answer': 'C) Patients with advanced '
                                                      'kidney disease (often '
                                                      'dialysis-dependent)',
                                            'explanation': 'Calciphylaxis (calcific '
                                                           'uremic arteriolopathy) '
                                                           'causes painful ischemic '
                                                           'skin necrosis mainly in '
                                                           'end-stage kidney disease '
                                                           'with disordered '
                                                           'calcium–phosphate '
                                                           'metabolism. It is rare '
                                                           'outside advanced '
                                                           'CKD/dialysis contexts.',
                                            'choice_explanations': {
                                                'A': 'Healthy adolescents without '
                                                      'metabolic disease rarely develop '
                                                      'calciphylaxis, which is tied to '
                                                      'disordered mineral metabolism in '
                                                      'advanced CKD.',
                                                'B': 'Isolated mild fatty liver alone '
                                                      'is not the usual setting of '
                                                      'calcific uremic arteriolopathy.',
                                                'C': 'Calciphylaxis (calcific uremic '
                                                      'arteriolopathy) causes painful '
                                                      'ischemic skin necrosis mainly in '
                                                      'end-stage kidney disease, often '
                                                      'dialysis-dependent, with '
                                                      'disordered calcium–phosphate '
                                                      'metabolism.',
                                                'D': 'Children with uncomplicated '
                                                      'atopic dermatitis have '
                                                      'eczematous barrier disease, not '
                                                      'calcific arteriolar occlusion of '
                                                      'calciphylaxis.'
                                            }},
                                           {'question': 'Toxic shock associations '
                                                        'include?',
                                            'options': ['A) Primary herpes simplex '
                                                        'gingivostomatitis alone',
                                                        'B) Uncomplicated dermatophyte '
                                                        'infection',
                                                        'C) Drug-induced '
                                                        'photosensitivity alone',
                                                        'D) Staphylococcal or '
                                                        'streptococcal '
                                                        'exotoxin–mediated disease'],
                                            'answer': 'D) Staphylococcal or '
                                                      'streptococcal exotoxin–mediated '
                                                      'disease',
                                            'explanation': 'Toxic shock syndromes are '
                                                           'mediated by superantigen '
                                                           'toxins from S. aureus or '
                                                           'S. pyogenes, causing '
                                                           'fever, shock, multiorgan '
                                                           'failure, and diffuse '
                                                           'erythema. Antiviral, '
                                                           'antifungal, and '
                                                           'photosensitivity disorders '
                                                           'are different '
                                                           'mechanisms.',
                                            'choice_explanations': {
                                                'A': 'Primary herpes simplex '
                                                      'gingivostomatitis is viral '
                                                      'mucosal infection and is not '
                                                      'superantigen toxin–mediated '
                                                      'toxic shock.',
                                                'B': 'Uncomplicated dermatophyte '
                                                      'infection is keratinophilic '
                                                      'fungal disease of skin/nails '
                                                      'without '
                                                      'staphylococcal/streptococcal '
                                                      'toxin shock.',
                                                'C': 'Drug-induced photosensitivity is '
                                                      'phototoxic or photoallergic skin '
                                                      'injury from drugs plus UV light, '
                                                      'a different mechanism from toxic '
                                                      'shock.',
                                                'D': 'Toxic shock syndromes are '
                                                      'mediated by superantigen toxins '
                                                      'from S. aureus or S. pyogenes, '
                                                      'causing fever, shock, multiorgan '
                                                      'failure, and diffuse erythema.'
                                            }}]},
                 'cases': {'easy': [{'title': 'Child with Facial Crusts',
                                     'stem': 'A 5-year-old has honey-colored crusts '
                                             'around the mouth after a scratch.',
                                     'question': 'Diagnosis?',
                                     'answer': 'Impetigo.',
                                     'discussion': 'Topical/systemic antibiotics per '
                                                   'extent; hygiene.',
                                     'book_hint': 'Habif / Rook / Fitzpatrick'}],
                           'medium': [{'title': 'Changing Mole',
                                       'stem': 'A 50-year-old has an asymmetrical '
                                               'multi-colored mole that grew over 3 '
                                               'months.',
                                       'question': 'Concern?',
                                       'answer': 'Melanoma — urgent dermatology '
                                                 'excision pathway.',
                                       'discussion': 'Do not shave biopsy suspicious '
                                                     'melanoma.',
                                       'book_hint': 'Habif / Rook / Fitzpatrick'}],
                           'hard': [{'title': 'Drug Rash + Mucosal Erosions',
                                     'stem': 'Days after a new anticonvulsant, a '
                                             'patient has fever, widespread dusky '
                                             'rash, and oral/genital erosions. Labs '
                                             'and imaging are pending; you must choose '
                                             'the safest next clinical concept.',
                                     'question': 'Fear?',
                                     'answer': 'SJS/TEN spectrum — stop drug, '
                                               'supportive care, specialty/burn '
                                               'pathways.',
                                     'discussion': 'Mucosal involvement is a red flag.',
                                     'book_hint': 'Habif / Rook / Fitzpatrick'}],
                           'extreme': [{'title': 'Purpuric Shock in Student',
                                        'stem': 'A college student rapidly develops '
                                                'fever, hypotension, and extensive '
                                                'purpura. Multiple teams are involved; '
                                                'prioritize life/limb/vision threats '
                                                'and avoid harmful premature '
                                                'therapies.',
                                        'question': 'Priority?',
                                        'answer': 'Meningococcemia/sepsis pathway — '
                                                  'immediate antibiotics after '
                                                  'cultures if possible, '
                                                  'resuscitation, infection control.',
                                        'discussion': 'Do not delay antibiotics for LP '
                                                      'if unstable.',
                                        'book_hint': 'Habif / Rook / Fitzpatrick'}]}},
 'obgyn': {'label': 'Obstetrics & Gynecology',
           'books': ['Williams Obstetrics',
                     "Beckmann and Ling's Obstetrics and Gynecology",
                     "DC Dutta's Textbook of Obstetrics"],
           'pdf_notes': ['PPH 4 Ts: Tone (atony most common), Trauma, Tissue, '
                         'Thrombin.',
                         'Ectopic: positive hCG + empty uterus + pain/spotting — '
                         'emergency awareness.',
                         'Pre-eclampsia after 20 weeks: HTN + proteinuria/organ '
                         'dysfunction.',
                         'Antenatal care milestones: dating, anomaly scan, Rh, '
                         'vaccines as indicated.',
                         'Doppler FHR typically ~10–12 weeks.'],
           'questions': {'easy': [{'question': 'Most common PPH cause?',
                                   'options': ['A) Uterine atony',
                                               'B) Retained products of conception as '
                                               'more common than atony',
                                               'C) Uterine inversion as the most '
                                               'frequent cause',
                                               'D) Coagulopathy as the single most '
                                               'common primary cause'],
                                   'answer': 'A) Uterine atony',
                                   'explanation': 'Uterine atony—failure of myometrial '
                                                  'contraction after delivery—is the '
                                                  'most common cause of postpartum '
                                                  'hemorrhage. Retained tissue, '
                                                  'trauma, inversion, and coagulopathy '
                                                  'are important but less frequent '
                                                  "primary causes; the '4 Ts' "
                                                  'framework still starts with tone.',
                                   'choice_explanations': {
                                       'A': 'Uterine atony—failure of myometrial '
                                             'contraction after delivery—is the most '
                                             'common cause of postpartum hemorrhage; '
                                             'without contraction, spiral arteries '
                                             'continue to bleed.',
                                       'B': 'Retained products of conception cause '
                                             'bleeding by preventing full uterine '
                                             'contraction and leaving vascular tissue '
                                             'in situ, but they are less common than '
                                             'atony as the primary cause.',
                                       'C': 'Uterine inversion is rare catastrophic '
                                             'invagination of the fundus and is not the '
                                             'most frequent PPH cause.',
                                       'D': 'Coagulopathy impairs clot formation and '
                                             'can worsen PPH but is not the single most '
                                             'common primary cause compared with atony.'
                                   }},
                                  {'question': 'Ectopic risk rises with?',
                                   'options': ['A) Prior uncomplicated term vaginal '
                                               'birth alone',
                                               'B) Prior PID or other tubal damage',
                                               'C) Folic acid supplementation',
                                               'D) Blood group O as an independent '
                                               'major risk'],
                                   'answer': 'B) Prior PID or other tubal damage',
                                   'explanation': 'Ectopic pregnancy risk rises when '
                                                  'tubal architecture is damaged—prior '
                                                  'PID, tubal surgery, or prior '
                                                  'ectopic—impairing blastocyst '
                                                  'transport. Uncomplicated prior '
                                                  'birth, folate, and blood group are '
                                                  'not major ectopic risk drivers.',
                                   'choice_explanations': {
                                       'A': 'Prior uncomplicated term vaginal birth '
                                             'alone does not damage tubal architecture '
                                             'and is not a major ectopic risk factor.',
                                       'B': 'Ectopic pregnancy risk rises when tubal '
                                             'architecture is damaged—prior PID, tubal '
                                             'surgery, or prior ectopic—impairing '
                                             'blastocyst transport to the uterus.',
                                       'C': 'Folic acid supplementation supports '
                                             'neural-tube prevention and does not '
                                             'increase ectopic implantation risk.',
                                       'D': 'Blood group O is not an independent major '
                                             'risk driver for ectopic pregnancy '
                                             'compared with tubal damage.'
                                   }},
                                  {'question': 'Fetal heart by Doppler often from?',
                                   'options': ['A) At 4 weeks by Doppler in all '
                                               'pregnancies',
                                               'B) Only after 28 weeks',
                                               "C) Approximately 10–12 weeks' "
                                               'gestation',
                                               'D) Never before quickening at 20 '
                                               'weeks'],
                                   'answer': "C) Approximately 10–12 weeks' gestation",
                                   'explanation': 'Handheld Doppler commonly detects '
                                                  'fetal heart tones around 10–12 '
                                                  'weeks, depending on habitus and '
                                                  'equipment. Earlier detection '
                                                  'usually requires transvaginal '
                                                  'ultrasound; waiting until the third '
                                                  'trimester is unnecessary for '
                                                  'routine dating/viability checks.',
                                   'choice_explanations': {
                                       'A': 'At 4 weeks, embryonic cardiac activity is '
                                             'generally too early for reliable handheld '
                                             'Doppler detection in all pregnancies; '
                                             'ultrasound is needed earlier.',
                                       'B': 'Waiting only until after 28 weeks is '
                                             'unnecessarily late; Doppler commonly '
                                             'detects fetal heart tones much earlier in '
                                             'the second month of the second trimester '
                                             'window.',
                                       'C': 'Handheld Doppler commonly detects fetal '
                                             'heart tones around 10–12 weeks’ '
                                             'gestation, depending on habitus and '
                                             'equipment.',
                                       'D': 'Quickening at ~20 weeks is maternal '
                                             'perception of movement; fetal heart tones '
                                             'are detectable by Doppler well before '
                                             'that.'
                                   }}],
                         'medium': [{'question': 'Pre-eclampsia is HTN after 20 weeks '
                                                 'plus?',
                                     'options': ['A) Isolated edema without '
                                                 'hypertension',
                                                 'B) Gestational diabetes alone',
                                                 'C) Physiologic first-trimester '
                                                 'nausea alone',
                                                 'D) Proteinuria or end-organ '
                                                 'dysfunction features'],
                                     'answer': 'D) Proteinuria or end-organ '
                                               'dysfunction features',
                                     'explanation': 'Pre-eclampsia is new hypertension '
                                                    'after 20 weeks plus proteinuria '
                                                    'or maternal organ dysfunction '
                                                    '(renal, hepatic, neurologic, '
                                                    'hematologic) or uteroplacental '
                                                    'dysfunction. Edema alone is '
                                                    'nonspecific; GDM and early nausea '
                                                    'are separate conditions.',
                                     'choice_explanations': {
                                         'A': 'Isolated edema without hypertension is '
                                               'nonspecific in pregnancy and does not '
                                               'define pre-eclampsia.',
                                         'B': 'Gestational diabetes is '
                                               'pregnancy-related glucose intolerance '
                                               'and is a separate diagnosis from '
                                               'pre-eclampsia.',
                                         'C': 'Physiologic first-trimester nausea '
                                               'occurs before 20 weeks and is unrelated '
                                               'to pre-eclampsia’s diagnostic criteria.',
                                         'D': 'Pre-eclampsia is new hypertension after '
                                               '20 weeks plus proteinuria or maternal '
                                               'end-organ dysfunction (renal, hepatic, '
                                               'neurologic, hematologic) or '
                                               'uteroplacental dysfunction.'
                                     }},
                                    {'question': 'Ectopic classic combo?',
                                     'options': ['A) Positive pregnancy test, empty '
                                                 'uterus on ultrasound, and pain or '
                                                 'bleeding',
                                                 'B) Negative hCG with intrauterine '
                                                 'pregnancy on scan',
                                                 'C) Intrauterine gestational sac with '
                                                 'fetal pole and no pain',
                                                 'D) Missed menses with closed cervix '
                                                 'and no ultrasound findings needed'],
                                     'answer': 'A) Positive pregnancy test, empty '
                                               'uterus on ultrasound, and pain or '
                                               'bleeding',
                                     'explanation': 'Ectopic pregnancy classically '
                                                    'combines a positive hCG, an empty '
                                                    'uterine cavity, and unilateral '
                                                    'pain or bleeding. An intrauterine '
                                                    'gestation makes ectopic unlikely '
                                                    '(except rare heterotopic '
                                                    'pregnancy). Early diagnosis '
                                                    'prevents rupture.',
                                     'choice_explanations': {
                                         'A': 'Ectopic pregnancy classically combines a '
                                               'positive pregnancy test, an empty '
                                               'uterine cavity on ultrasound, and '
                                               'unilateral pain or bleeding.',
                                         'B': 'Negative hCG with an intrauterine '
                                               'pregnancy is physiologically '
                                               'inconsistent and does not describe '
                                               'ectopic pregnancy.',
                                         'C': 'An intrauterine gestational sac with '
                                               'fetal pole indicates intrauterine '
                                               'pregnancy and makes ectopic unlikely '
                                               'except rare heterotopic pregnancy.',
                                         'D': 'Missed menses alone without hCG and '
                                               'ultrasound evaluation is insufficient '
                                               'to diagnose or exclude ectopic '
                                               'pregnancy.'
                                     }},
                                    {'question': 'Shoulder dystocia is?',
                                     'options': ['A) A normal second-stage variant '
                                                 'needing no maneuvers',
                                                 'B) An obstetric emergency when the '
                                                 'shoulders fail to deliver after the '
                                                 'head',
                                                 'C) Failure of placental separation '
                                                 'after 30 minutes as the same entity',
                                                 'D) Cord prolapse after membrane '
                                                 'rupture as the identical diagnosis'],
                                     'answer': 'B) An obstetric emergency when the '
                                               'shoulders fail to deliver after the '
                                               'head',
                                     'explanation': 'Shoulder dystocia is impaction of '
                                                    'the fetal shoulders after '
                                                    'delivery of the head, risking '
                                                    'hypoxia and brachial plexus '
                                                    'injury. It requires immediate '
                                                    'help and maneuvers (McRoberts, '
                                                    'suprapubic pressure)—not '
                                                    'expectant delay.',
                                     'choice_explanations': {
                                         'A': 'Shoulder dystocia is not a normal '
                                               'second-stage variant; delayed delivery '
                                               'of the shoulders risks hypoxia and '
                                               'brachial plexus injury.',
                                         'B': 'Shoulder dystocia is an obstetric '
                                               'emergency when the fetal shoulders fail '
                                               'to deliver after the head, requiring '
                                               'immediate help and maneuvers such as '
                                               'McRoberts and suprapubic pressure.',
                                         'C': 'Failure of placental separation after 30 '
                                               'minutes defines retained placenta, a '
                                               'third-stage problem distinct from '
                                               'shoulder dystocia.',
                                         'D': 'Cord prolapse is umbilical cord descent '
                                               'after membrane rupture with risk of '
                                               'cord compression, a different emergency '
                                               'from shoulder impaction.'
                                     }}],
                         'hard': [{'question': 'Magnesium sulfate in obstetrics is '
                                               'used for?',
                                   'options': ['A) First-line tocolysis for all '
                                               'preterm labor',
                                               'B) Routine induction agent at term for '
                                               'all women',
                                               'C) Seizure prophylaxis and treatment '
                                               'in pre-eclampsia/eclampsia',
                                               'D) Antibiotic prophylaxis for group B '
                                               'streptococcus'],
                                   'answer': 'C) Seizure prophylaxis and treatment in '
                                             'pre-eclampsia/eclampsia',
                                   'explanation': 'Magnesium sulfate is used to '
                                                  'prevent and treat eclamptic '
                                                  'seizures in pre-eclampsia with '
                                                  'severe features and eclampsia; it '
                                                  'also offers fetal neuroprotection '
                                                  'in selected preterm births. It is '
                                                  'not a routine induction agent or '
                                                  'GBS antibiotic.',
                                   'choice_explanations': {
                                       'A': 'Magnesium sulfate is not first-line '
                                             'tocolysis for all preterm labor; other '
                                             'agents are used for tocolysis when '
                                             'indicated.',
                                       'B': 'Routine induction at term uses oxytocin or '
                                             'prostaglandins, not magnesium sulfate as '
                                             'an induction agent for all women.',
                                       'C': 'Magnesium sulfate prevents and treats '
                                             'eclamptic seizures in pre-eclampsia with '
                                             'severe features and eclampsia by raising '
                                             'the seizure threshold.',
                                       'D': 'Group B streptococcus prophylaxis uses '
                                             'antibiotics such as penicillin, not '
                                             'magnesium sulfate.'
                                   }},
                                  {'question': 'Placenta previa bleeding is typically?',
                                   'options': ['A) Painful bleeding with a hypertonic '
                                               'tender uterus (abruption pattern)',
                                               'B) Passage of tissue with cramping at '
                                               '8 weeks as the defining previa feature',
                                               'C) Amenorrhea without bleeding',
                                               'D) Painless vaginal bleeding'],
                                   'answer': 'D) Painless vaginal bleeding',
                                   'explanation': 'Placenta previa overlies the '
                                                  'cervical os; bleeding is typically '
                                                  'painless as the placenta shears '
                                                  'with lower-segment change. Painful '
                                                  'bleeding with uterine hypertonus '
                                                  'suggests abruption instead.',
                                   'choice_explanations': {
                                       'A': 'Painful bleeding with a hypertonic tender '
                                             'uterus is the classic abruption pattern '
                                             'from premature placental separation, not '
                                             'previa.',
                                       'B': 'Passage of tissue with cramping at 8 weeks '
                                             'describes early pregnancy loss, not '
                                             'placenta previa bleeding later in '
                                             'pregnancy.',
                                       'C': 'Amenorrhea without bleeding is absence of '
                                             'menses and does not describe previa '
                                             'hemorrhage.',
                                       'D': 'Placenta previa overlies the cervical os; '
                                             'bleeding is typically painless as the '
                                             'placenta shears with lower-segment change '
                                             'and cervical effacement.'
                                   }},
                                  {'question': 'HELLP relates to?',
                                   'options': ['A) Hemolysis, elevated liver enzymes, '
                                               'and low platelets',
                                               'B) Hyperemesis with normal liver '
                                               'enzymes and platelets',
                                               'C) Isolated gestational '
                                               'thrombocytopenia without hemolysis or '
                                               'liver injury',
                                               'D) Cholestasis of pregnancy with '
                                               'pruritus and bile acids alone'],
                                   'answer': 'A) Hemolysis, elevated liver enzymes, '
                                             'and low platelets',
                                   'explanation': 'HELLP syndrome (Hemolysis, Elevated '
                                                  'Liver enzymes, Low Platelets) is a '
                                                  'severe pre-eclampsia spectrum '
                                                  'disorder requiring urgent obstetric '
                                                  'management. Hyperemesis, isolated '
                                                  'gestational thrombocytopenia, and '
                                                  'cholestasis are distinct '
                                                  'entities.',
                                   'choice_explanations': {
                                       'A': 'HELLP syndrome denotes Hemolysis, Elevated '
                                             'Liver enzymes, and Low Platelets—a severe '
                                             'pre-eclampsia spectrum disorder requiring '
                                             'urgent obstetric management.',
                                       'B': 'Hyperemesis with normal liver enzymes and '
                                             'platelets is intractable early pregnancy '
                                             'vomiting without the HELLP laboratory '
                                             'triad.',
                                       'C': 'Isolated gestational thrombocytopenia is '
                                             'mild platelet reduction without hemolysis '
                                             'or liver injury of HELLP.',
                                       'D': 'Cholestasis of pregnancy features pruritus '
                                             'and elevated bile acids with usually '
                                             'preserved synthetic function, distinct '
                                             'from HELLP.'
                                   }}],
                         'extreme': [{'question': 'Amniotic fluid embolism theme?',
                                      'options': ['A) Gradual postpartum blues over '
                                                  'days without shock',
                                                  'B) Sudden cardiorespiratory '
                                                  'collapse and coagulopathy in labor '
                                                  'or immediate postpartum',
                                                  'C) Isolated retained placenta '
                                                  'without hemodynamic change',
                                                  'D) Mild transient hypotension after '
                                                  'epidural without hypoxia or DIC'],
                                      'answer': 'B) Sudden cardiorespiratory collapse '
                                                'and coagulopathy in labor or '
                                                'immediate postpartum',
                                      'explanation': 'Amniotic fluid embolism presents '
                                                     'with abrupt hypoxia, '
                                                     'hypotension/cardiovascular '
                                                     'collapse, and often disseminated '
                                                     'intravascular coagulation during '
                                                     'labor or immediately postpartum. '
                                                     'It is a clinical diagnosis '
                                                     'requiring immediate '
                                                     'resuscitation.',
                                      'choice_explanations': {
                                          'A': 'Gradual postpartum blues over days is '
                                                'mood lability without sudden '
                                                'cardiorespiratory collapse and DIC of '
                                                'amniotic fluid embolism.',
                                          'B': 'Amniotic fluid embolism presents with '
                                                'abrupt hypoxia, '
                                                'hypotension/cardiovascular collapse, '
                                                'and often DIC during labor or '
                                                'immediately postpartum.',
                                          'C': 'Isolated retained placenta without '
                                                'hemodynamic change is a third-stage '
                                                'delivery problem without the '
                                                'catastrophic AFE triad.',
                                          'D': 'Mild transient hypotension after '
                                                'epidural without hypoxia or DIC is '
                                                'usually sympathectomy-related and '
                                                'lacks the AFE clinical picture.'
                                      }},
                                     {'question': 'Acute fatty liver of pregnancy '
                                                  'overlaps with?',
                                      'options': ['A) First-trimester hyperemesis '
                                                  'without liver synthetic failure',
                                                  'B) Uncomplicated gestational '
                                                  'thrombocytopenia alone',
                                                  'C) A late-pregnancy acute '
                                                  'liver-failure phenotype',
                                                  'D) Intrahepatic cholestasis with '
                                                  'pruritus but preserved synthetic '
                                                  'function as identical AFLP'],
                                      'answer': 'C) A late-pregnancy acute '
                                                'liver-failure phenotype',
                                      'explanation': 'Acute fatty liver of pregnancy '
                                                     'is a third-trimester '
                                                     'mitochondrial hepatopathy '
                                                     'presenting with liver failure, '
                                                     'coagulopathy, hypoglycemia, and '
                                                     'encephalopathy that overlaps '
                                                     'clinically with HELLP/severe '
                                                     'pre-eclampsia and requires '
                                                     'urgent delivery and supportive '
                                                     'care.',
                                      'choice_explanations': {
                                          'A': 'First-trimester hyperemesis without '
                                                'liver synthetic failure is early '
                                                'intractable vomiting, not the '
                                                'late-pregnancy liver-failure phenotype '
                                                'of AFLP.',
                                          'B': 'Uncomplicated gestational '
                                                'thrombocytopenia alone lacks the '
                                                'coagulopathy, hypoglycemia, and liver '
                                                'failure of acute fatty liver of '
                                                'pregnancy.',
                                          'C': 'Acute fatty liver of pregnancy is a '
                                                'third-trimester mitochondrial '
                                                'hepatopathy presenting with a '
                                                'late-pregnancy acute liver-failure '
                                                'phenotype (coagulopathy, hypoglycemia, '
                                                'encephalopathy).',
                                          'D': 'Intrahepatic cholestasis with pruritus '
                                                'but preserved synthetic function is '
                                                'bile-acid–related itching, not '
                                                'identical to AFLP’s synthetic liver '
                                                'failure.'
                                      }},
                                     {'question': 'Uterine rupture risk rises with?',
                                      'options': ['A) Primiparous spontaneous labor '
                                                  'with no uterine surgery',
                                                  'B) Elective repeat cesarean before '
                                                  'labor as the highest rupture '
                                                  'setting',
                                                  'C) Uncomplicated vacuum extraction '
                                                  'without scar as the main risk',
                                                  'D) Prior cesarean scar undergoing '
                                                  'labor'],
                                      'answer': 'D) Prior cesarean scar undergoing '
                                                'labor',
                                      'explanation': 'Uterine rupture risk is highest '
                                                     'with labor in a scarred uterus '
                                                     '(prior cesarean), especially '
                                                     'with induction or dysfunctional '
                                                     'labor. Unscarred primiparous '
                                                     'labor has much lower risk; '
                                                     'rupture presents with fetal '
                                                     'distress, loss of station, and '
                                                     'maternal shock.',
                                      'choice_explanations': {
                                          'A': 'Primiparous spontaneous labor with no '
                                                'uterine surgery has a low baseline '
                                                'rupture risk compared with labor in a '
                                                'scarred uterus.',
                                          'B': 'Elective repeat cesarean before labor '
                                                'avoids labor stress on a scar and is '
                                                'not the highest rupture-risk setting '
                                                'compared with trial of labor after '
                                                'cesarean.',
                                          'C': 'Uncomplicated vacuum extraction without '
                                                'scar is instrumental vaginal delivery '
                                                'risk, not the main uterine rupture '
                                                'risk driver of a prior cesarean scar '
                                                'in labor.',
                                          'D': 'Uterine rupture risk rises most with '
                                                'labor in a scarred uterus after prior '
                                                'cesarean, especially with induction or '
                                                'dysfunctional labor.'
                                      }}]},
           'cases': {'easy': [{'title': 'Boggy Uterus Bleeding',
                               'stem': 'After vaginal delivery, heavy bleeding with a '
                                       'soft boggy uterus.',
                               'question': 'First concept?',
                               'answer': 'Atony — massage + oxytocin and PPH protocol.',
                               'discussion': 'Tone is most common.',
                               'book_hint': 'Williams Obstetrics'}],
                     'medium': [{'title': 'Positive hCG + Unilateral Pain',
                                 'stem': 'Positive pregnancy test, spotting, '
                                         'unilateral pelvic pain, empty uterus, '
                                         'adnexal mass.',
                                 'question': 'Diagnosis?',
                                 'answer': 'Ectopic pregnancy until proven otherwise.',
                                 'discussion': 'Stability guides medical vs surgical '
                                               'care.',
                                 'book_hint': 'Williams Obstetrics'}],
                     'hard': [{'title': 'Seizure at 34 Weeks',
                               'stem': 'A primip at 34 weeks with headache and HTN has '
                                       'a tonic-clonic seizure. Labs and imaging are '
                                       'pending; you must choose the safest next '
                                       'clinical concept.',
                               'question': 'Diagnosis and drug concept?',
                               'answer': 'Eclampsia — magnesium sulfate and '
                                         'maternal/fetal stabilization; delivery '
                                         'planning.',
                               'discussion': 'Protect airway and control seizure.',
                               'book_hint': 'Williams Obstetrics'}],
                     'extreme': [{'title': 'Collapse Minutes After Delivery',
                                  'stem': 'Suddenly after delivery a woman becomes '
                                          'hypoxic, hypotensive, and coagulopathic '
                                          'without visible atony initially. Multiple '
                                          'teams are involved; prioritize '
                                          'life/limb/vision threats and avoid harmful '
                                          'premature therapies.',
                                  'question': 'Consider?',
                                  'answer': 'Amniotic fluid embolism among other '
                                            'catastrophic differentials — ACLS '
                                            'obstetric modifications, correct '
                                            'coagulopathy, supportive ICU care.',
                                  'discussion': 'Diagnosis of exclusion but act fast.',
                                  'book_hint': 'Williams Obstetrics'}]}},
 'pediatrics': {'label': 'Pediatrics',
                'books': ['Nelson Textbook of Pediatrics',
                          'Illustrated Textbook of Paediatrics — Lissauer',
                          "Forfar and Arneil's Textbook of Pediatrics"],
                'pdf_notes': ['ORS first-line for most pediatric dehydration from '
                              'diarrhea.',
                              'MMR is live; know live vs inactivated vaccines.',
                              'Kawasaki: prolonged fever + mucocutaneous signs → '
                              'coronary risk.',
                              'APGAR at 1 and 5 minutes guides immediate newborn '
                              'status.',
                              'Always calculate pediatric doses by weight; watch fluid '
                              'rates.'],
                'questions': {'easy': [{'question': 'ORS is first-line for?',
                                        'options': ['A) Most dehydrating diarrheal '
                                                    'illnesses when the child can '
                                                    'still drink',
                                                    'B) All children with severe shock '
                                                    'as the only initial fluid '
                                                    'strategy',
                                                    'C) Isolated constipation without '
                                                    'fluid loss',
                                                    'D) Surgical abdomen with '
                                                    'peritonitis as preferred sole '
                                                    'therapy'],
                                        'answer': 'A) Most dehydrating diarrheal '
                                                  'illnesses when the child can still '
                                                  'drink',
                                        'explanation': 'Oral rehydration solution '
                                                       'replaces water and '
                                                       'electrolytes using '
                                                       'glucose–sodium cotransport and '
                                                       'is first-line for most '
                                                       'children with dehydrating '
                                                       'diarrhea who can drink. IV '
                                                       'fluids are needed for severe '
                                                       'shock or inability to tolerate '
                                                       'oral intake.',
                                        'choice_explanations': {
                                            'A': 'Oral rehydration solution replaces '
                                                  'water and electrolytes via '
                                                  'glucose–sodium cotransport and is '
                                                  'first-line for most children with '
                                                  'dehydrating diarrhea who can still '
                                                  'drink.',
                                            'B': 'Children with severe shock need IV '
                                                  '(or IO) resuscitation; ORS alone is '
                                                  'not the only initial fluid strategy '
                                                  'when perfusion is critically '
                                                  'impaired.',
                                            'C': 'Isolated constipation is hard stool '
                                                  'without diarrheal fluid and '
                                                  'electrolyte losses that ORS is '
                                                  'designed to replace.',
                                            'D': 'Surgical abdomen with peritonitis '
                                                  'requires surgical evaluation and IV '
                                                  'therapy, not ORS as preferred sole '
                                                  'therapy.'
                                        }},
                                       {'question': 'MMR vaccine type?',
                                        'options': ['A) Inactivated whole-virus only',
                                                    'B) Live attenuated',
                                                    'C) Toxoid vaccine',
                                                    'D) Pure polysaccharide conjugate '
                                                    'identical to tetanus toxoid'],
                                        'answer': 'B) Live attenuated',
                                        'explanation': 'MMR is a live attenuated '
                                                       'vaccine and is generally '
                                                       'contraindicated in significant '
                                                       'immunocompromise and '
                                                       'pregnancy. Inactivated, '
                                                       'toxoid, and polysaccharide '
                                                       'vaccines are different '
                                                       'platforms used for other '
                                                       'pathogens.',
                                        'choice_explanations': {
                                            'A': 'Inactivated whole-virus vaccines '
                                                  '(e.g., some influenza/polio '
                                                  'formulations) use killed virus; MMR '
                                                  'is live attenuated instead.',
                                            'B': 'MMR is a live attenuated vaccine that '
                                                  'replicates limitedly to induce '
                                                  'immunity and is generally '
                                                  'contraindicated in significant '
                                                  'immunocompromise and pregnancy.',
                                            'C': 'Toxoid vaccines (tetanus, diphtheria) '
                                                  'use inactivated toxins, a different '
                                                  'platform from live attenuated MMR.',
                                            'D': 'Pure polysaccharide or conjugate '
                                                  'vaccines target bacterial capsules '
                                                  'and are not the live attenuated '
                                                  'viral platform of MMR, nor identical '
                                                  'to tetanus toxoid.'
                                        }},
                                       {'question': 'APGAR is done at?',
                                        'options': ['A) Only at 30 minutes after birth',
                                                    'B) Only at hospital discharge',
                                                    'C) 1 and 5 minutes of life '
                                                    '(commonly), with further scores '
                                                    'if needed',
                                                    'D) Once at conception dating '
                                                    'ultrasound'],
                                        'answer': 'C) 1 and 5 minutes of life '
                                                  '(commonly), with further scores if '
                                                  'needed',
                                        'explanation': 'The Apgar score assesses '
                                                       'appearance, pulse, grimace, '
                                                       'activity, and respiration at 1 '
                                                       'and 5 minutes to summarize '
                                                       'early transition; further '
                                                       'scores are recorded if the '
                                                       '5-minute score remains low. It '
                                                       'is not a discharge readiness '
                                                       'tool.',
                                        'choice_explanations': {
                                            'A': 'Apgar scoring at only 30 minutes '
                                                  'misses the standard early transition '
                                                  'assessments at 1 and 5 minutes.',
                                            'B': 'Hospital discharge assessment is '
                                                  'separate from the Apgar score '
                                                  'summarizing immediate postnatal '
                                                  'transition.',
                                            'C': 'The Apgar score assesses appearance, '
                                                  'pulse, grimace, activity, and '
                                                  'respiration at 1 and 5 minutes of '
                                                  'life, with further scores if the '
                                                  '5-minute score remains low.',
                                            'D': 'Conception dating ultrasound '
                                                  'estimates gestational age and is '
                                                  'unrelated to postnatal Apgar '
                                                  'transition scoring.'
                                        }}],
                              'medium': [{'question': 'Kawasaki complication?',
                                          'options': ['A) Isolated mitral stenosis as '
                                                      'the classic sequela',
                                                      'B) Chronic interstitial lung '
                                                      'fibrosis as the main '
                                                      'complication',
                                                      'C) Avascular necrosis of the '
                                                      'femoral head as the defining '
                                                      'feature',
                                                      'D) Coronary artery aneurysms'],
                                          'answer': 'D) Coronary artery aneurysms',
                                          'explanation': 'Kawasaki disease is a '
                                                         'medium-vessel vasculitis of '
                                                         'childhood; coronary artery '
                                                         'aneurysms are the major '
                                                         'complication prevented by '
                                                         'timely IVIG. Cardiac '
                                                         'involvement—not mitral '
                                                         'stenosis, pulmonary '
                                                         'fibrosis, or femoral '
                                                         'AVN—drives follow-up '
                                                         'echocardiography.',
                                          'choice_explanations': {
                                              'A': 'Isolated mitral stenosis is '
                                                    'rheumatic or congenital valve '
                                                    'narrowing and is not the classic '
                                                    'sequela of Kawasaki vasculitis.',
                                              'B': 'Chronic interstitial lung fibrosis '
                                                    'is a pulmonary parenchymal '
                                                    'process, not the main Kawasaki '
                                                    'complication.',
                                              'C': 'Avascular necrosis of the femoral '
                                                    'head is ischemic bone necrosis '
                                                    '(e.g., steroid-related or Perthes) '
                                                    'and is not the defining Kawasaki '
                                                    'feature.',
                                              'D': 'Kawasaki disease is medium-vessel '
                                                    'vasculitis of childhood; coronary '
                                                    'artery aneurysms are the major '
                                                    'complication prevented by timely '
                                                    'IVIG.'
                                          }},
                                         {'question': 'Fever in a neonate is?',
                                          'options': ['A) A serious infection until '
                                                      'proven otherwise',
                                                      'B) Always a benign viral '
                                                      'illness needing no evaluation',
                                                      'C) Routine teething without '
                                                      'workup in all neonates',
                                                      'D) Ignored if the infant still '
                                                      'feeds occasionally'],
                                          'answer': 'A) A serious infection until '
                                                    'proven otherwise',
                                          'explanation': 'Neonates have immature '
                                                         'immunity and can deteriorate '
                                                         'rapidly from bacterial '
                                                         'sepsis/meningitis. Fever in '
                                                         'this age group mandates '
                                                         'urgent full evaluation and '
                                                         'empiric therapy pathways—not '
                                                         'attribution to teething.',
                                          'choice_explanations': {
                                              'A': 'Neonates have immature immunity and '
                                                    'can deteriorate rapidly from '
                                                    'bacterial sepsis/meningitis, so '
                                                    'fever is a serious infection until '
                                                    'proven otherwise and mandates '
                                                    'urgent evaluation.',
                                              'B': 'Assuming always benign viral '
                                                    'illness without evaluation is '
                                                    'unsafe in neonates, who may lack '
                                                    'focal signs despite invasive '
                                                    'bacterial disease.',
                                              'C': 'Teething does not cause true fever '
                                                    'requiring dismissal of workup in '
                                                    'neonates; fever still needs '
                                                    'infection evaluation.',
                                              'D': 'Occasional feeding is not '
                                                    'reassurance against neonatal '
                                                    'sepsis; fever in this age still '
                                                    'requires urgent pathways.'
                                          }},
                                         {'question': 'Croup hallmark?',
                                          'options': ['A) Expiratory wheeze as the '
                                                      'sole hallmark without '
                                                      'upper-airway signs',
                                                      'B) Barking cough and '
                                                      'inspiratory stridor',
                                                      'C) Drooling and tripoding as '
                                                      'the typical croup posture',
                                                      'D) Productive lobar '
                                                      'consolidation as the defining '
                                                      'feature'],
                                          'answer': 'B) Barking cough and inspiratory '
                                                    'stridor',
                                          'explanation': 'Viral croup '
                                                         '(laryngotracheobronchitis) '
                                                         'produces subglottic edema '
                                                         'with a barking cough and '
                                                         'stridor, often after a viral '
                                                         'prodrome. Drooling/tripoding '
                                                         'suggests epiglottitis; '
                                                         'expiratory wheeze suggests '
                                                         'lower-airway disease such as '
                                                         'bronchiolitis or asthma.',
                                          'choice_explanations': {
                                              'A': 'Expiratory wheeze as the sole '
                                                    'hallmark without upper-airway '
                                                    'signs points to lower-airway '
                                                    'disease (bronchiolitis/asthma), '
                                                    'not subglottic croup.',
                                              'B': 'Viral croup '
                                                    '(laryngotracheobronchitis) '
                                                    'produces subglottic edema with a '
                                                    'barking cough and inspiratory '
                                                    'stridor, often after a viral '
                                                    'prodrome.',
                                              'C': 'Drooling and tripoding suggest '
                                                    'epiglottitis with supraglottic '
                                                    'swelling, a different emergency '
                                                    'from typical croup.',
                                              'D': 'Productive lobar consolidation '
                                                    'defines pneumonia’s alveolar '
                                                    'infection, not the barking '
                                                    'cough/stridor of croup.'
                                          }}],
                              'hard': [{'question': 'Pyloric stenosis classic?',
                                        'options': ['A) Bilious vomiting from day one '
                                                    'of life',
                                                    'B) Chronic constipation starting '
                                                    'in adolescence',
                                                    'C) Projectile non-bilious '
                                                    'vomiting at about 2–8 weeks of '
                                                    'age',
                                                    'D) Painless rectal bleeding at 2 '
                                                    'years without vomiting'],
                                        'answer': 'C) Projectile non-bilious vomiting '
                                                  'at about 2–8 weeks of age',
                                        'explanation': 'Infantile hypertrophic pyloric '
                                                       'stenosis causes progressive '
                                                       'gastric outlet obstruction, '
                                                       'typically with projectile '
                                                       'non-bilious vomiting in weeks '
                                                       '2–8, visible peristalsis, and '
                                                       'a palpable olive. Bilious '
                                                       'emesis suggests more distal '
                                                       'obstruction.',
                                        'choice_explanations': {
                                            'A': 'Bilious vomiting from day one of life '
                                                  'suggests distal intestinal '
                                                  'obstruction (malrotation/atresia), '
                                                  'not pyloric stenosis’s non-bilious '
                                                  'gastric outlet obstruction.',
                                            'B': 'Chronic constipation starting in '
                                                  'adolescence is a later childhood '
                                                  'bowel issue, not infantile '
                                                  'hypertrophic pyloric stenosis.',
                                            'C': 'Infantile hypertrophic pyloric '
                                                  'stenosis causes progressive gastric '
                                                  'outlet obstruction with projectile '
                                                  'non-bilious vomiting at about 2–8 '
                                                  'weeks of age.',
                                            'D': 'Painless rectal bleeding at 2 years '
                                                  'without vomiting suggests entities '
                                                  'such as Meckel diverticulum polyp, '
                                                  'not pyloric stenosis.'
                                        }},
                                       {'question': 'Intussusception stool?',
                                        'options': ['A) Acholic pale stools from '
                                                    'biliary atresia as the same '
                                                    'finding',
                                                    'B) Melena from duodenal ulcer as '
                                                    'the typical toddler pattern',
                                                    'C) Steatorrhea from pancreatic '
                                                    'insufficiency as the classic '
                                                    'intussusception stool',
                                                    'D) Redcurrant-jelly stool (a late '
                                                    'sign)'],
                                        'answer': 'D) Redcurrant-jelly stool (a late '
                                                  'sign)',
                                        'explanation': 'Intussusception may produce '
                                                       'currant-jelly stool from '
                                                       'ischemia and mucus late in the '
                                                       'course; earlier clues are '
                                                       'intermittent severe colic and '
                                                       'lethargy with a possible '
                                                       'sausage mass. Pale stools, '
                                                       'melena, and steatorrhea '
                                                       'indicate other diseases.',
                                        'choice_explanations': {
                                            'A': 'Acholic pale stools from biliary '
                                                  'atresia reflect absent bile pigment '
                                                  'delivery to the intestine, not '
                                                  'ischemic currant-jelly stool of '
                                                  'intussusception.',
                                            'B': 'Melena from duodenal ulcer is '
                                                  'upper-GI digested blood and is not '
                                                  'the typical toddler intussusception '
                                                  'stool pattern.',
                                            'C': 'Steatorrhea from pancreatic '
                                                  'insufficiency is fat-laden stool '
                                                  'from maldigestion, not ischemic '
                                                  'mucus-bloody currant-jelly stool.',
                                            'D': 'Intussusception may produce '
                                                  'redcurrant-jelly stool from ischemia '
                                                  'and mucus as a late sign; earlier '
                                                  'clues include intermittent colic and '
                                                  'lethargy.'
                                        }},
                                       {'question': 'Congenital adrenal hyperplasia '
                                                    'crisis in boys may show?',
                                        'options': ['A) Salt-wasting adrenal crisis '
                                                    'with shock, hyponatremia, and '
                                                    'hyperkalemia',
                                                    'B) Isolated hypertension without '
                                                    'electrolyte change',
                                                    'C) Cushingoid obesity from birth '
                                                    'without crisis',
                                                    'D) Hypoglycemia only without '
                                                    'mineralocorticoid features'],
                                        'answer': 'A) Salt-wasting adrenal crisis with '
                                                  'shock, hyponatremia, and '
                                                  'hyperkalemia',
                                        'explanation': 'In salt-wasting 21-hydroxylase '
                                                       'deficiency, boys lack '
                                                       'ambiguous genitalia and may '
                                                       'present in the first weeks '
                                                       'with vomiting, shock, '
                                                       'hyponatremia, and hyperkalemia '
                                                       'from aldosterone deficiency—an '
                                                       'endocrine emergency treated '
                                                       'with fluids, glucose, and '
                                                       'steroids.',
                                        'choice_explanations': {
                                            'A': 'In salt-wasting 21-hydroxylase '
                                                  'deficiency, boys may present in the '
                                                  'first weeks with shock, '
                                                  'hyponatremia, and hyperkalemia from '
                                                  'aldosterone deficiency—an adrenal '
                                                  'crisis emergency.',
                                            'B': 'Isolated hypertension without '
                                                  'electrolyte change is more '
                                                  'consistent with other CAH enzyme '
                                                  'blocks (e.g., 11-beta) than classic '
                                                  'salt-wasting crisis.',
                                            'C': 'Cushingoid obesity from birth '
                                                  'reflects glucocorticoid excess '
                                                  'phenotypes, not salt-wasting '
                                                  'mineralocorticoid deficiency crisis.',
                                            'D': 'Hypoglycemia only without '
                                                  'mineralocorticoid features '
                                                  'incompletely describes salt-wasting '
                                                  'CAH, which prominently includes '
                                                  'hyponatremia and hyperkalemia.'
                                        }}],
                              'extreme': [{'question': 'Ductal-dependent congenital '
                                                       'heart lesion presenting in '
                                                       'shock when the duct closes '
                                                       'needs?',
                                           'options': ['A) Indomethacin to close the '
                                                       'duct as first therapy in '
                                                       'ductal-dependent systemic flow',
                                                       'B) Prostaglandin E1 infusion '
                                                       'while resuscitating, under '
                                                       'specialty guidance',
                                                       'C) Fluid restriction alone '
                                                       'without ductal patency support',
                                                       'D) Outpatient cardiology '
                                                       'review in weeks without '
                                                       'prostaglandin'],
                                           'answer': 'B) Prostaglandin E1 infusion '
                                                     'while resuscitating, under '
                                                     'specialty guidance',
                                           'explanation': 'Ductal-dependent congenital '
                                                          'heart lesions present with '
                                                          'shock or cyanosis as the '
                                                          'ductus arteriosus closes. '
                                                          'PGE1 reopens/maintains '
                                                          'ductal flow while '
                                                          'resuscitation and urgent '
                                                          'cardiology/cardiac surgery '
                                                          'pathways proceed. '
                                                          'Indomethacin would close '
                                                          'the duct and worsen '
                                                          'systemic or pulmonary '
                                                          'flow.',
                                           'choice_explanations': {
                                               'A': 'Indomethacin closes the ductus '
                                                     'arteriosus and would worsen '
                                                     'ductal-dependent systemic or '
                                                     'pulmonary blood flow in '
                                                     'ductal-dependent congenital heart '
                                                     'disease presenting in shock.',
                                               'B': 'Ductal-dependent congenital heart '
                                                     'lesions present with shock or '
                                                     'cyanosis as the duct closes; '
                                                     'prostaglandin E1 '
                                                     'reopens/maintains ductal flow '
                                                     'during resuscitation under '
                                                     'specialty guidance.',
                                               'C': 'Fluid restriction alone without '
                                                     'maintaining ductal patency fails '
                                                     'to restore duct-dependent '
                                                     'systemic or pulmonary perfusion.',
                                               'D': 'Outpatient cardiology review in '
                                                     'weeks without prostaglandin '
                                                     'leaves critical ductal-dependent '
                                                     'lesions untreated during ductal '
                                                     'closure.'
                                           }},
                                          {'question': 'Non-accidental injury clue?',
                                           'options': ['A) Age-appropriate bruising on '
                                                       'shins in a cruising toddler '
                                                       'alone',
                                                       'B) Documented witnessed '
                                                       'accidental fall matching exam '
                                                       'findings',
                                                       'C) Injury inconsistent with '
                                                       'the history or developmental '
                                                       'stage',
                                                       'D) Isolated viral petechiae '
                                                       'with known enteroviral illness '
                                                       'and reassuring workup'],
                                           'answer': 'C) Injury inconsistent with the '
                                                     'history or developmental stage',
                                           'explanation': 'Non-accidental injury is '
                                                          'suggested when trauma is '
                                                          'inconsistent with history '
                                                          'or developmental capability '
                                                          '(e.g., femur fracture in a '
                                                          'nonambulatory infant), '
                                                          'patterned bruises, or '
                                                          'occult fractures. '
                                                          'Age-appropriate shin '
                                                          'bruises and consistent '
                                                          'accidental mechanisms are '
                                                          'less concerning.',
                                           'choice_explanations': {
                                               'A': 'Age-appropriate bruising on shins '
                                                     'in a cruising toddler is a common '
                                                     'accidental pattern and alone is '
                                                     'not a non-accidental injury clue.',
                                               'B': 'A documented witnessed accidental '
                                                     'fall matching exam findings '
                                                     'supports an accidental mechanism '
                                                     'rather than abuse.',
                                               'C': 'Non-accidental injury is suggested '
                                                     'when trauma is inconsistent with '
                                                     'the history or developmental '
                                                     'stage (e.g., femur fracture in a '
                                                     'nonambulatory infant).',
                                               'D': 'Isolated viral petechiae with '
                                                     'known enteroviral illness and '
                                                     'reassuring workup reflect '
                                                     'infection-related petechiae, not '
                                                     'inflicted trauma.'
                                           }},
                                          {'question': 'Acute epiglottitis classic '
                                                       'presentation (less common with '
                                                       'Hib vaccine)?',
                                           'options': ['A) Barking cough with mild '
                                                       'stridor managed as routine '
                                                       'croup at home',
                                                       'B) Bilateral expiratory wheeze '
                                                       'treated only with inhaled '
                                                       'bronchodilator',
                                                       'C) Simple viral rhinitis '
                                                       'without toxicity',
                                                       'D) Toxic appearance, drooling, '
                                                       'and tripoding—avoid agitating '
                                                       'the airway; obtain airway '
                                                       'expertise'],
                                           'answer': 'D) Toxic appearance, drooling, '
                                                     'and tripoding—avoid agitating '
                                                     'the airway; obtain airway '
                                                     'expertise',
                                           'explanation': 'Epiglottitis presents with '
                                                          'a toxic child, drooling, '
                                                          'and tripoding from '
                                                          'supraglottic swelling. '
                                                          'Airway examination that '
                                                          'agitates the child can '
                                                          'precipitate complete '
                                                          'obstruction; keep the child '
                                                          'calm and summon experienced '
                                                          'airway support. Hib '
                                                          'vaccination has made '
                                                          'classic epiglottitis '
                                                          'uncommon but not '
                                                          'extinct.',
                                           'choice_explanations': {
                                               'A': 'Barking cough with mild stridor '
                                                     'managed as routine croup at home '
                                                     'describes '
                                                     'laryngotracheobronchitis, not the '
                                                     'toxic drooling tripoding child of '
                                                     'epiglottitis.',
                                               'B': 'Bilateral expiratory wheeze '
                                                     'treated only with bronchodilator '
                                                     'suggests lower-airway reactive '
                                                     'disease, not supraglottic '
                                                     'epiglottitis.',
                                               'C': 'Simple viral rhinitis without '
                                                     'toxicity lacks airway obstruction '
                                                     'signs of epiglottitis.',
                                               'D': 'Epiglottitis presents with a toxic '
                                                     'child, drooling, and tripoding '
                                                     'from supraglottic swelling; avoid '
                                                     'agitating the airway and obtain '
                                                     'experienced airway expertise.'
                                           }}]},
                'cases': {'easy': [{'title': 'Diarrhea + Sunken Eyes',
                                    'stem': 'An 18-month-old with watery diarrhea has '
                                            'sunken eyes but still drinks.',
                                    'question': 'Initial therapy?',
                                    'answer': 'ORS.',
                                    'discussion': 'IV if severe/shock.',
                                    'book_hint': 'Nelson Pediatrics'}],
                          'medium': [{'title': 'Fever 6 Days + Strawberry Tongue',
                                      'stem': 'A 3-year-old has ≥5 days fever, '
                                              'conjunctivitis, strawberry tongue, '
                                              'rash, cervical nodes.',
                                      'question': 'Diagnosis?',
                                      'answer': 'Kawasaki disease.',
                                      'discussion': 'IVIG to reduce coronary risk.',
                                      'book_hint': 'Nelson Pediatrics'}],
                          'hard': [{'title': 'Bilious Vomiting Neonate',
                                    'stem': 'A 3-day-old has bilious vomiting and '
                                            'abdominal distension. Labs and imaging '
                                            'are pending; you must choose the safest '
                                            'next clinical concept.',
                                    'question': 'Emergency concern?',
                                    'answer': 'Malrotation with midgut volvulus until '
                                              'excluded — urgent surgical evaluation.',
                                    'discussion': 'Bilious vomiting in neonate is an '
                                                  'emergency.',
                                    'book_hint': 'Nelson Pediatrics'}],
                          'extreme': [{'title': 'Neonate in Shock Day 5',
                                       'stem': 'A previously well term neonate becomes '
                                               'grey, hypotensive, and acidotic on day '
                                               '5 of life as the duct closes. Femoral '
                                               'pulses are weak. Multiple teams are '
                                               'involved; prioritize life/limb/vision '
                                               'threats and avoid harmful premature '
                                               'therapies.',
                                       'question': 'Concept?',
                                       'answer': 'Possible ductal-dependent congenital '
                                                 'heart disease — ABC resuscitation '
                                                 'and urgent prostaglandin under '
                                                 'specialist guidance plus cardiology.',
                                       'discussion': 'Sepsis remains on the '
                                                     'differential too.',
                                       'book_hint': 'Nelson Pediatrics'}]}}}


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
        "🩺 *CharaNas Medicine*\n"
        "Undergraduate Medicine Department\n\n"
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
